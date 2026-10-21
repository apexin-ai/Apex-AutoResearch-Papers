# Director coordination — Part 4 of 14

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/46/46a4a073b0cc4314da71.json)

## Round 95

### Tool call

_source line 974 · 2026-05-18T09:02:10.377454+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 975 · 2026-05-18T09:02:12.542500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-18T09:02:12.543015+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in Base LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Class
…[truncated 585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 977 · 2026-05-18T09:02:12.894736+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 978 · 2026-05-18T09:02:13.146378+00:00_

# Round 16 (fresh review) — updated by Research Director 2026-05-18 post-R16 fixes complete

- id: "R1-W1"
  summary: "Baseline hyperparameter inconsistency"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 8
  resolution: "method.tex unified to est200/md6. Verified R8."
  resolution_round: 8

- id: "R1-W5"
  summary: "Downstream experiment too small"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 13
  resolution: "TOST demoted from Contribution to supporting analysis. §4.4 moved to Appendix in R13."
  resolution_round: 13

- id: "R7-W1"
  summary: "gen-0 seed sharing inflating headline + gen-1/gen-2+ topic confound"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 7
  last_seen_round: 15
  mentions:
    - {round: 9, reviewers: "R1,R2", note: "Abstract reports both binary and 3-class."}
    - {round: 10, reviewers: "R1,R2", note: "Recurred as R10-N1."}
    - {round: 11, reviewers: "R1,R2", note: "Abstract still leads with 3-class."}
    - {round: 12, reviewers: "R1,R2", note: "Intro was still 3-class-first."}
    - {round: 13, reviewers: "R1,R2", note: "MF2+MF4: Abstract leads with cross-model not LOGO. Gen-0 bias not quantified."}
    - {round: 14, reviewers: "R1,R2", note: "Fresh review: 3-class needs gen-0 leakage caveat wherever it appears."}
    - {round: 15, reviewers: "R1,R2", note: "Escalated: beyond gen-0 headline, shared seeds create topic fingerprint in gen-1/gen-2+ that LOGO cannot isolate. Need disjoint-seed LOGO experiment. Cross-domain (Appendix G) partially mitigates but insufficient (3 gens × 200 seeds)."}
  action_items:
    - {round: 10, action: "Use leak-free binary F1 as headline", assigned_to: "Paper Agent", status: "done"}
    - {round: 11, action: "Abstract lead with binary", assigned_to: "Paper Agent", status: "done"}
    - {round: 12, action: "Intro restructured to binary-first", assigned_to: "
…[truncated 24880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-18T09:02:15.807193+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on my search results, I found some information about EMNLP 2026 submissions, though the results primarily show workshop a
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5429
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-18T09:02:37.387808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit template author instructions"
  }
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-18T09:02:37.899698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline commitment ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline commitment ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-18T09:02:39.555473+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-18T09:02:39.608104+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-18T09:02:43.943952+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template author instructions"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Allow Early Submissions to ACL 2026 in the October ARR Cycle | ACL Member Portal","url":"https://www.aclweb.org/portal/content/allow-early-submissions-acl-2026-october-arr-cycle"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key details:

## Page Limits

ARR submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers)
…[truncated 1088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6556
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-18T09:02:44.044805+00:00_

Web search results for query: "EMNLP 2026 submission deadline commitment ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here's information about EMNLP 2026 submission deadlines and ARR cycle commitment:

## Submission Deadline

The ARR submission deadline for EMNLP 2026 (both long and short papers) is May 25, 2026.

## ARR Cycle and Commitment

Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6145
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-18T09:02:48.062510+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-18T09:02:48.363757+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-18T09:02:48.414263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers main conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for papers main conference"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-18T09:02:58.782724+00:00_

Web search results for query: "site:2026.emnlp.org call for papers main conference"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

I found the Call for Main Conference Papers for EMNLP 2026. Here are the key details:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Conference Details
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Special Theme
The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era. This reflects how large language models have shifted the landscape of NLP research.

## Submission Process
Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment l
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 10368
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-18T09:03:01.595596+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 991 · 2026-05-18T09:03:01.696324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-18T09:03:06.565567+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements: page limits (long/short paper, with/without references, appendix rules), template name and version, anonymity rules, checklist requirements, formatting rules, ARR submission deadline for May 2026 cycle, commitment deadline, and any special instructions. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements: page limits (long/short paper, with/without references, appendix rules), template name and version, anonymity rules, checklist requirements, formatting rules, ARR submission deadline for May 2026 cycle, commitment deadline, and any special instructions. Be exhaustive."
  }
}
```

</details>

---


### Tool call

_source line 993 · 2026-05-18T09:03:07.369688+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission formatting requirements: page limits for long and short papers, template version, anonymity rules, supplementary material rules, responsible NLP checklist, citation format, and any restrictions. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL submission formatting requirements: page limits for long and short papers, template version, anonymity rules, supplementary material rules, responsible NLP checklist, citation format, and any restrictions. Be exhaustive."
  }
}
```

</details>

---


### Tool result

_source line 994 · 2026-05-18T09:03:12.058112+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long papers:** 8 pages (content) + 1 additional page in final version = up to 9 pages total
- **Short papers:** 4 pages (content) + 1 additional page in final version = up to 5 pages total
- References appear to fall outside these limits (standard ACL practice referenced but not explicitly detailed here)

## Key Deadlines
- **ARR May 2026 submission deadline:** May 25, 2026
- **Reviewer registration deadline:** May 27, 2026
- **EMNLP commitment deadline:** August 2, 2026
- All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')"

## Anonymity & Review Process
- "The reviewing process will continue to be double-blind"
- "Following the ACL and ARR policies, there is no anonymity period requirement"
- Authors cannot modify author lists during commitment phase (reordering only allowed)

## Required Policies & Checklists
Submissions must comply with:
- ACL Publication Ethics Policy
- ARR Ethics Policy including "responsible NLP research checklist"
- ACL Disclosure Policy (coordinated disclosure)
- Limitations section required
- Two-way anonymized review instructions

## Templates & Formatting
The document directs authors to follow "all of the ARR submission requirements" and references "Paper Submission and Templates" but does not specify template name/version details in this excerpt.

## Special Instructions
- Optional supplementary materials allowed
- Writing assistance permitted; AI-generated papers prohibited
- Papers must address "thinly sliced contributions" and citation integrity concerns

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 5492
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-18T09:03:14.418197+00:00_

# ACL Rolling Review: Submission Formatting Requirements

## Page Limits

**Long Papers:**
- "up to eight (8) pages of content"
- Unlimited space after conclusion for limitations (mandatory) and optional ethical considerations section
- Unlimited reference pages

**Short Papers:**
- "up to four (4) pages of content"
- Unlimited space after conclusion for limitations (mandatory) and optional ethical considerations section
- Unlimited reference pages

Papers exceeding length requirements or missing limitations sections face desk rejection.

## Template & Style

- Must follow the official ACL style template from GitHub (acl-org/acl-style-files)
- Adhere to "\*ACL" conference formatting guidelines at acl-org.github.io/ACLPUB/formatting.html
- No modifications to style files or alternative templates permitted
- Non-conforming submissions rejected without review

## Anonymity Rules

Papers must exclude author names, affiliations, and self-identifying references. Instead of "We previously showed," use "Smith previously showed." Avoid references to non-reviewable documents. Supplementary materials require anonymization; cloud storage links (Dropbox, Google Drive) prohibited. Violations result in desk rejection.

## Responsible NLP Checklist

Completion is mandatory during submission. Incorrect, incomplete, or misleading responses trigger desk rejection. Checklist content informs review decisions.

## Citation Format for Concurrent Work

```
Anonymous (2026). Paper title. Under review.
```

Concurrent submissions on related topics with overlapping authors must cite each other and discuss differences in related work.

## Supplementary Materials

Appendices, software, and data permitted but optional. Reviewers not required to review appendix content. Critical material belongs in main papers. Appendices follow double-column format (exceptions per ACLPUB guidelines) and don't count toward page limits. Software/data submitted as single .tgz or .zip archives, fully anonymized. Rep
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 7048
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-18T09:03:19.290806+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"project_config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 1 -name \"config*\" 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"project_config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 1 -name \"config*\" 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-18T09:03:19.391538+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-18T09:03:23.105377+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/gen-depth-fingerprint.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/gen-depth-fingerprint.yml 2>/dev/null || echo \"not found\"",
  "description": "Read project config for external review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/gen-depth-fingerprint.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/gen-depth-fingerprint.yml 2>/dev/null || echo \"not found\"",
    "description": "Read project config for external review"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-18T09:03:23.206368+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_paper_agent.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_09731295942d3269e0517509703bed15.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_16c7228d5f50b6e03f04861201ad7ee0.json
mcp_config_worker_1f20be951a19580275e4408889e77c7a.json
mcp_config_worker_283b0e963b3fe46d2fa23009ef282bc2.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
mcp_config_worker_58a2c13c6faae79a50aeb3914e8975c6.json
mcp_config_worker_5b83a101e2d66f0bdbaffa07ffd78ceb.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_650c6f8dfdc8ee5805ef2ab17b16e08c.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_6ed01710fcd9d363c828e4eb42b74d6b.json
mcp_config_worker_6f0b694c30c8a0575c498898ae58e765.json
mcp_config_worker_710092c1ff80917ff9f19703a3ad1f01.json
mcp_config_worker_72d677611154f03f46a3b1682311338f.json
mcp_config_worker_7a15ae22dd5282ab8fe3e0cea065cab9.json
mcp_config_worker_7e02a6eac7ecafae897d9e964cb36d2f.json
mcp_config_worker_7f289b4cf49d35629c3aa93f15a08233.json
mcp_config_worker_7fc16ee950d4cc0902b80c47aa5b8063.json
mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
mcp_config_worker_8fdc57f80f0cafc42cc1047c9dc7ebf1.json
mcp_config_work
…[truncated 763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-18T09:03:27.071074+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml 2>/dev/null || echo \"not found\"",
  "description": "Find project-specific config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/ 2>/dev/null && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml 2>/dev/null || echo \"not found\"",
    "description": "Find project-specific config"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-18T09:03:27.121793+00:00_

gen-depth-fingerprint.yaml
svs_formal_verification.yaml
---
execution:
  gpu_ids:
  - cuda:0
  - cuda:1
  - cuda:2
  - cuda:3
  project_path: /root/gen-depth-fingerprint
  servers:
  - bjb2-18868
feishu:
  chat_id: oc_dbd68d7879a81efc0c108e9844b15d0b
  operational_chat_id: oc_a189a3add89efad7437b5c9f3e05fbf3
  review_paper_path: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
  review_round: 16
  review_supplementary_paths: ''
  submission_chat_id: oc_999770e4e57bfc6eabd12fc1f64af1ef
project:
  created_at: '2026-05-14T16:13:51.441Z'
  description: Provenance Depth Estimation for Risk-Aware Curation of Synthetic Text
  name: gen-depth-fingerprint
  phase: research
  source_idea_id: idea_009
rules:
  writing:
  - created_at: '2026-05-17T17:22:45Z'
    id: 89ee27
    text: overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-18T09:03:34.400640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1003 · 2026-05-18T09:03:34.401011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-18T09:03:34.701825+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, and the resulting recursive chains progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base (pretrained) models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary, consistent with a location shift in the token-level NLL distribution whose shape exhibits negligible depth effects (Cohen's $d < 0.10$ vs.\ $d > 0.75$ for drifting features).
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under eight-generator leave-one-generator-out (LOGO) evaluation and 0.764 on cross-model chains (five-generator subset), using a single 410M-parameter reference model.
7	The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-18T09:03:34.702238+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	How this evolution proceeds is a fundamental question that connects to both model collapse theory \cite{curse_of_recursion, self_consuming_mad} and data provenance.
6	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, evidence that LLM text already re-enters training pipelines at scale.
7	Yet existing detection methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions and obscure qualitative differences: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
8	
9	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
10	No existing method addresses this task in non-paraphrastic continuation chains.
11	
12	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.
13	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while distributional shape exhibits negligible depth effects (Cohen's $d < 0.10$ for shape features vs.\ $d > 0.75$ for drifting features): the s
…[truncated 2186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-18T09:03:34.702424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-18T09:03:35.153523+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8,defactify_dataset}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal,corn_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attributi
…[truncated 5644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-18T09:03:35.153922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-18T09:03:35.705379+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Depth fingerprinting framework. (a)~Recursive generation chains are constructed by iteratively feeding text through a generator $G$. (b)~Seven features are extracted per text: five NLL statistics from a Pythia-410M reference model and two surface diversity measures. Horizontal bars show Spearman $\rho$ with generation depth and reveal differential depth response: drifting features ($|\rho| > 0.6$) capture the monotonic location shift, while stationary features ($|\rho| < 0.1$) provide a stable baseline. (c)~An XGBoost classifier trained under Leave-One-Generator-Out (LOGO) cross-validation predicts depth class (gen-0\,/\,gen-1\,/\,gen-2+).}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight gen
…[truncated 9383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-18T09:03:35.705877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-18T09:03:36.659716+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\ref{app:confusion}).
11	Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.
12	The Pythia-1B/2.8B crossover between three-class and binary scores (0.806 vs.\ 0.798 and 0.718 vs.\ 0.724, respectively) reflects differences in gen-0 classification accuracy rather than in depth discrimination per se.
13	
14	\paragraph{Cross-model generalization.}
15	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.}
16	This protocol differs from LOGO (all generators appear in training), so the difference from single-generator LOGO (binary 0.694) reflects both protocol and generator-subset effects; the 5-generator LOGO average is 0.734 for reference.
17	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
18	
19	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, which confirms transfer acr
…[truncated 10732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-18T09:03:36.760367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-18T09:03:37.061479+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The near-stationarity of shape features is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape while allowing location to drift.
5	Temperature ablation supports this as a tendency rather than a guarantee: within $t \in [0.5, 0.7]$ the signal is preserved (Pythia-2.8B improves, Qwen3-1.7B is stable), but at $t{=}0.9$ both degrade sharply ($-$26.0\,pp for Pythia, $-$18.5\,pp for Qwen; Appendix~\ref{app:sampling-sensitivity}), and prompt-type dependence further modulates the effect (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}).
6	
7	Instruction-tuned models show substantially weaker cross-generator fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base; 3-class degradation of 17--20\,pp across three model families).
8	Spearman analysis reveals that instruction tuning does not merely attenuate but reverses the direction of entropy-depth associations: entropy\_mean $\rho$ flips from ${\approx}{-}0.6$ (base) to $+0.2$--$+0.5$ (instruct) consistently across Qwen3-1.7B, OLMo-2-1B, and Llama-3.2-3B, while surface features (TTR, hapax ratio) exhibit model-dependent responses ranging from reversal to near-zero collapse.
9	This is consistent with instruction tuning shifting the generation attractor to a different fixed point relative to the reference model, rather than destroying the iterative dynamics that DDR exploits.
10	The reversal restricts current applicability to base models and constitutes the primary scope limitation.
11	At the document level within base models, gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging; the gen-1\,/\,gen-2+ boundary concentrates 86\% of binary errors as false negatives, with larger generators exacerbating this (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%; Appendix~\ref{app:error-analysis}).
12	Cross-temperature transfer degrades subst
…[truncated 1116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-18T09:03:37.062006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-18T09:03:37.262705+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution whose shape exhibits negligible depth effects (Cohen's $d < 0.10$ vs.\ $d > 0.75$ for drifting features).
5	A lightweight 7-feature ensemble detects this drift with leak-free binary F1\,=\,0.694 under eight-generator LOGO evaluation (0.764 on cross-model chains; five-generator subset).
6	The signal degrades substantially under instruction tuning and may further compress at larger scales (our largest generator is 8B); these limitations define the current scope boundaries.
7	All code, data, and trained models will be released upon publication.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-18T09:03:37.313218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-18T09:03:37.363923+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, 
…[truncated 2339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-18T09:03:43.763079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-18T09:03:43.863745+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
10	\paragraph{Licenses.}
11	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
12	Wikipedia seed passages are distributed under CC BY-SA 3.0.
13	
14	\paragraph{Compute budget.}
15	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
16	
17	\paragraph{Software.}
18	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-18T09:03:44.214819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-18T09:03:44.916714+00:00_

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
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benc
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 701
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-18T09:03:44.967224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-18T09:03:45.017694+00:00_

100	\label{app:ablation-table}
101	\input{appendix_ablation}
102	
103	\input{appendix_feature_correlation}
104	
105	\section{Cross-Family Reference Models}
106	\label{app:cross-ref}
107	\input{table4}
108	
109	\input{appendix_seed_control}
110	
111	\input{appendix_qualitative_examples}
112	
113	\end{document}
114	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-18T09:04:37.817432+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, ethics.tex，以及 15 个 appendix）\n- **标题**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n- **目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Findings\n- **截止日期**: 2026-05-25 (AoE)\n\n### Venue 格式要求\n- **页数**: Long paper 8 页正文 + 无限 references + 无限 appendix（appendix 不计入页数但审稿人不要求审阅）\n- **模板**: ACL style template (acl-org/acl-style-files)\n- **匿名**: Double-blind（作者姓名/机构不可出现，自引需第三人称）\n- **必须包含**: Limitations section（不计入页数）、Responsible NLP Checklist\n- **引用格式**: natbib\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法严谨性**\n   - DDR（differential depth response）的定义是否严谨？\"near-stationary\" 的量化标准（Cohen's d < 0.10）是否充分？\n   - 7 个特征的选择是否有理论依据还是事后合理化（post-hoc rationalization）？\n   - KS test、Levene test、Spearman ρ、Cohen's d 的使用是否正确？多重比较校正是否充分？\n   - Task formulation（3-class ordinal classification）的合理性\n\n2. **实验设计**\n   - LOGO 评估协议是否能真正测试跨 generator 泛化？\n   - Gen-0 seed sharing 问题：binary F1 排除 gen-0 是否足够？seed demeaning 和 independent-seed 实验是否真正排除了 topic fingerprint confound？\n   - Baseline 比较公平性：将 binary detection scores \"repurposed\" 为 ordinal predictors 是否合理？\n   - Temperature/prompt-type sensitivity：这些限制对论文 claim 的影响如何？\n   - 8 个 generator 的覆盖面（0.6B-8B base models only）是否足够？\n\n3. **统计分析**\n   - Bootstrap CI 计算是否正确？\n   - Bonferroni correction 的范围是否恰当？\n   - 效应量报告是否完整？\n   - 交叉引用的数字是否一致（Table 1 vs Table 2 vs 正文数字）？\n\n4. **可复现性**\n   - 实验细节是否足够复现？\n   - Hyperparameter 选择是否有理由？\n   - 代码/数据承诺是否明确？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。\n\n**评分标准**：5 = Consider for Award（~前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, ethics.tex，以及 15 个 appendix）\n- **标题**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n- **目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Findings\n- **截止日期**: 2026-05-25 (AoE)\n\n### Venue 格式要求\n- **页数**: Long paper 8 页正文 + 无限 references + 无限 appendix（appendix 不计入页数但审稿人不要求审阅）\n- **模板**: ACL style template (acl-org/acl-style-files)\n- **匿名**: Double-blind（作者姓名/机构不可出现，自引需第三人称）\n- **必须包含**: Limitations section（不计入页数）、Responsible NLP Checklist\n- **引用格式**: natbib\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法严谨性**\n   - DDR（differential depth response）的定义是否严谨？\"near-stationary\" 的量化标准（Cohen's d < 0.10）是否充分？\n   - 7 个特征的选择是否有理论依据还是事后合理化（post-hoc rationalization）？\n   - KS test、Levene test、Spearman ρ、Cohen's d 的使用是否正确？多重比较校正是否充分？\n   - Task formulation（3-class ordinal classification）的合理性\n\n2. **实验设计**\n   - LOGO 评估协议是否能真正测试跨 generator 泛化？\n   - Gen-0 seed sharing 问题：binary F1 排除 gen-0 是否足够？seed demeaning 和 independent-seed 实验是否真正排除了 topic fingerprint confound？\n   - Baseline 比较公平性：将 binary detection scores \"repurposed\" 为 ordinal predictors 是否合理？\n   - Temperature/prompt-type sensitivity：这些限制对论文 claim 的影响如何？\n   - 8 个 generator 的覆盖面（0.6B-8B base models only）是否足够？\n\n3. **统计分析**\n   - Bootstrap CI 计算是否正确？\n   - Bonferroni correction 的范围是否恰当？\n   - 效应量报告是否完整？\n   - 交叉引用的数字是否一致（Table 1 vs Table 2 vs 正文数字）？\n\n4. **可复现性**\n   - 实验细节是否足够复现？\n   - Hyperparameter 选择是否有理由？\n   - 代码/数据承诺是否明确？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。\n\n**评分标准**：5 = Consider for Award（~前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-18T09:04:59.436230+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21618
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-18T09:04:59.637155+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 写作质量 + 格式合规 + 相关工作覆盖**\n\n### 论文信息\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, ethics.tex，以及 15 个 appendix）\n- **标题**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n- **目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Findings\n- **截止日期**: 2026-05-25 (AoE)\n\n### Venue 格式要求\n- **页数**: Long paper 8 页正文 + 无限 references + 无限 appendix（appendix 不计入页数但审稿人不要求审阅）\n- **模板**: ACL style template (acl-org/acl-style-files)\n- **匿名**: Double-blind（作者姓名/机构不可出现，自引需第三人称）\n- **必须包含**: Limitations section（不计入页数）、Responsible NLP Checklist\n- **引用格式**: natbib\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献**\n   - \"Generation depth classification\" 作为任务定义的新颖性如何？\n   - DDR 的发现是否是真正的 insight 还是已知现象的重新包装（model collapse drift 的重新发现）？\n   - 论文定位为 \"phenomenon paper\" 而非方法论文——这种定位是否合理？贡献是否达到 Findings 的门槛？\n   - 与两个 concurrent works（Broken Telephone, Markovian Chains）的区分是否充分？\n\n2. **写作质量**\n   - Abstract 是否在 30 秒内传达价值？是否有数据堆砌？\n   - Introduction 叙事线是否连贯（大问题 → 缺口 → 洞察 → 方法 → 贡献）？\n   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？\n   - **AI 写作痕迹检查**（硬规则）：\n     - em-dash（—）和解释性 en-dash（–）\n     - -ing 短语结尾（\"highlighting...\"，\"demonstrating...\"）\n     - 过度分段（每 2-3 句就换段）\n     - \"Furthermore/Moreover/Additionally\" 连续使用\n     - 用词黑名单：delve into, leverage, utilize, facilitate, a myriad of, notably, it is worth noting\n   - 专有名词/缩写首次出现是否有定义？\n   - 图表 caption 是否自包含？\n\n3. **格式合规**\n   - 正文是否在 8 页以内？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 行号是否开启（`\\linenumbers`）？\n   - 作者是否匿名（`\\author{Anonymous}`）？\n   - Limitations section 是否存在且充实？\n   - Ethics statement 是否存在？\n   - 是否缺少 Responsible NLP Checklist？\n\n4. **相关工作覆盖**\n   - 引用是否覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否有重要遗漏（特别是 stylometry、ordinal classification、data provenance 方向）？\n   - bib 条目质量：是否有 orphan entries、title/author 不匹配、缺少 pages/volume？\n   - 引用密度是否达到 EMNLP 论文的量级？\n\n5. **图表规范**\n   - 信息密度是否足够？\n   - 字体大小是否 >= 7pt？\n   - 最优加粗/次优下划线是否一致？\n   - 小数精度是否全表统一？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 ARR 评分标准）→ Detailed Comments。\n\n**评分标准**：5 = Consider for Award（~前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 写作质量 + 格式合规 + 相关工作覆盖**\n\n### 论文信息\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, ethics.tex，以及 15 个 appendix）\n- **标题**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n- **目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **投稿类别**: Findings\n- **截止日期**: 2026-05-25 (AoE)\n\n### Venue 格式要求\n- **页数**: Long paper 8 页正文 + 无限 references + 无限 appendix（appendix 不计入页数但审稿人不要求审阅）\n- **模板**: ACL style template (acl-org/acl-style-files)\n- **匿名**: Double-blind（作者姓名/机构不可出现，自引需第三人称）\n- **必须包含**: Limitations section（不计入页数）、Responsible NLP Checklist\n- **引用格式**: natbib\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献**\n   - \"Generation depth classification\" 作为任务定义的新颖性如何？\n   - DDR 的发现是否是真正的 insight 还是已知现象的重新包装（model collapse drift 的重新发现）？\n   - 论文定位为 \"phenomenon paper\" 而非方法论文——这种定位是否合理？贡献是否达到 Findings 的门槛？\n   - 与两个 concurrent works（Broken Telephone, Markovian Chains）的区分是否充分？\n\n2. **写作质量**\n   - Abstract 是否在 30 秒内传达价值？是否有数据堆砌？\n   - Introduction 叙事线是否连贯（大问题 → 缺口 → 洞察 → 方法 → 贡献）？\n   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？\n   - **AI 写作痕迹检查**（硬规则）：\n     - em-dash（—）和解释性 en-dash（–）\n     - -ing 短语结尾（\"highlighting...\"，\"demonstrating...\"）\n     - 过度分段（每 2-3 句就换段）\n     - \"Furthermore/Moreover/Additionally\" 连续使用\n     - 用词黑名单：delve into, leverage, utilize, facilitate, a myriad of, notably, it is worth noting\n   - 专有名词/缩写首次出现是否有定义？\n   - 图表 caption 是否自包含？\n\n3. **格式合规**\n   - 正文是否在 8 页以内？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 行号是否开启（`\\linenumbers`）？\n   - 作者是否匿名（`\\author{Anonymous}`）？\n   - Limitations section 是否存在且充实？\n   - Ethics statement 是否存在？\n   - 是否缺少 Responsible NLP Checklist？\n\n4. **相关工作覆盖**\n   - 引用是否覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否有重要遗漏（特别是 stylometry、ordinal classification、data provenance 方向）？\n   - bib 条目质量：是否有 orphan entries、title/author 不匹配、缺少 pages/volume？\n   - 引用密度是否达到 EMNLP 论文的量级？\n\n5. **图表规范**\n   - 信息密度是否足够？\n   - 字体大小是否 >= 7pt？\n   - 最优加粗/次优下划线是否一致？\n   - 小数精度是否全表统一？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 ARR 评分标准）→ Detailed Comments。\n\n**评分标准**：5 = Consider for Award（~前2.5%），4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-18T09:05:01.495671+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1858
}
```

</details>

---


### Assistant

_source line 1028 · 2026-05-18T09:05:06.408293+00:00_

Round 1 审稿任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）已启动
- **Reviewer 2**（新颖性 + 写作质量 + 格式合规 + 相关工作覆盖）已启动

等待两位 Reviewer 返回独立审稿结果，收到后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 1029 · 2026-05-18T09:14:21.132262+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告 — Round 1

**论文**: "Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains"
**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 论文提出了一个新颖且有意义的任务（生成深度分类），DDR 分解有实证支持，实验设计全面，但严格限于 base models（0.6B-8B）且 instruction tuning 导致信号近乎崩溃，实际应用场景极为有限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 主要 claim 有充分实验支持，DDR 分解有内部一致性问题（entropy_std/min 不符合二分框架），阈值选择为 post-hoc |
| **Excitement** | 3.0/5 | 新颖任务定义，但实际适用范围狭窄（仅 base models, 0.6B-8B, 温度敏感），限制了影响力 |
| **Reproducibility** | 4/5 | 实验细节充足，明确承诺开源代码和数据，但部分 hyperparameter 选择缺少理由 |
| **Confidence** | 4/5 | 熟悉机器生成文本检测和统计分析方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR 二分框架的内部一致性缺陷

- 具体位置：Section 4.2, Figure 1b
- 问题：DDR 是本文核心贡献，将 7 个特征分为 "drifting"（|ρ| > 0.10）和 "stationary"（|ρ| < 0.10, d < 0.10）。但 Section 4.2 承认 entropy_std（d = 0.55, |ρ| = 0.16）和 entropy_min（pooled d = 0.40）不符合这一框架（"the remaining two require qualification"）。这意味着 7 个特征中有 2 个不满足论文自定义的分类标准，DDR 的"两类特征行为截然不同"这一核心叙事被削弱。
- 为什么影响接收：DDR 分解是 Abstract 和 Introduction 的核心卖点。如果 7 个特征中有 28.6% 不符合框架，审稿人会质疑这是一个 clean empirical finding 还是事后合理化。
- 建议修改方向：(a) 将特征明确分为三类（drifting / intermediate / stationary），修改 DDR 叙事以反映这一连续谱；(b) 或者提供统计检验（如 equivalence test）为 entropy_std/min 的分类提供正式支持；(c) 讨论为什么 entropy_std 有高 d 但低 |ρ|（非单调性关系？）

**N2** [critical] Instruction tuning 导致信号崩溃，实际应用价值存疑

- 具体位置：Section 9 (Limitations), p9
- 问题：OLMo-2-1B-Instruct LOGO F1 = 0.338（vs. base 0.763），Qwen3-0.6B 类似。论文承认"depth signal degrades substantially under instruction tuning"。但现实中几乎所有 LLM 生成文本来自 instruction-tuned 或 RLHF-aligned 模型。如果方法在最常见场景下失效，"depth fingerprinting" 作为检测工具的实际价值极为有限。
- 为什么影响接收：论文 Introduction (Section 1) 以"LLM-generated text increasingly re-enters the web"为动机，暗示了实际检测应用。但方法仅适用于 base model 输出（在现实中极为罕见），动机与方法适用范围之间存在严重脱节。
- 建议修改方向：(a) 重新 frame 论文贡献为分析性/科学性发现（understanding distributional drift under recursive generation），而非检测工具；(b) 至少在 2-3 个主流 instruction-tuned models 上报告完整结果，即使是负面结果也应系统性呈现；(c) Discussion 中明确讨论从 base 到 instruction-tuned 的 gap 为何如此大（instruction tuning 是否消除了 depth-dependent 信号？还是引入了更强的 confound？）

**N3** [critical] 模型规模覆盖不足（0.6B-8B），claim 泛化性缺乏支撑

- 具体位置：Section 3.2, Table 1, Section 9
- 问题：8 个 generator 全部在 0.6B-8B 范围。Discussion (Section 5) 承认"larger models generate text closer to human"，而 Table 1 已显示 Mistral-7B 和 Qwen3-8B（最大模型）的 F1 相对较低（Mistral-7B binary F1 = 0.633, Qwen3-8B binary F1 = 0.692）。这一下降趋势暗示 depth signal 在更大模型上可能进一步消失，但论文没有任何 >8B 的数据点。
- 为什么影响接收：论文标题和 Abstract 使用"Base LLM Text Chains"而非"Small Base LLM Text Chains"，暗示了更广的适用范围。缺少 >8B 的数据使得读者无法判断方法在 13B/70B 模型上是否还有效。
- 建议修改方向：添加至少一个 >8B 模型（如 Llama-3.1-13B 或更大）的实验，即使只是 pilot 结果，以验证 depth signal 的 scaling trend。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Baseline 比较方法论不公平

- 具体位置：Section 4.3, Table 2
- 问题：Section 4.3 将 binary detection 方法（FastDetectGPT, Binoculars, Avg-LogProb, LD-Score）的检测分数"repurposed as ordinal depth predictors"。这些方法本身为 binary 检测设计，其输出分数的 ordinal discriminative power 并未被优化。用它们的原始分数作为 XGBoost 特征与专门为 depth classification 设计的 7 个特征做对比，不是 apples-to-apples 比较。
- 建议：(a) 为每个 baseline 提取与论文类似的 distributional features（如 NLL 统计量），然后用同一分类器；(b) 或者承认 baseline 比较是 convenience comparison 而非 fair competition，并据此调低相关 claim。

**W2** [warning] DDR 阈值选择为 post-hoc，缺少先验理由

- 具体位置：Section 4.2
- 问题：|ρ| = 0.10 和 d = 0.10 作为 drifting/stationary 分界线，没有先验理论依据。Section 4.2 补充说"shifting these descriptive thresholds by ±0.10 does not alter feature grouping"，这是敏感性分析但不等于理论动机。Cohen (1988) 定义 d < 0.20 为"negligible"，论文的 0.10 更严格但无解释。
- 建议：引用 Cohen 或 Lakens (2017) 的 equivalence testing 框架（论文在 Appendix L 已用 TOST），将 DDR 的统计支持前置到正文。

**W3** [warning] 温度敏感性限制实际适用性

- 具体位置：Appendix H (p16), Appendix O (Figure 9, p24)
- 问题：t=0.7→1.0 跨温度迁移导致 3-class F1 从 0.947 下降到 0.726（−22 pp），Qwen3-1.7B 在跨温度条件下 3-class F1 降至 0.418。实际 LLM 使用中温度设定差异很大（0.0-1.5），且用户通常不知道也无法控制来源文本的温度。
- 建议：Discussion 中更突出讨论温度作为一个实际部署的核心障碍，而非仅在附录中处理。

**W4** [warning] Gen-0 seed sharing 导致 3-class F1 膨胀

- 具体位置：Section 3.2, Section 4.1
- 问题：所有 generator 共享同一 1000 个 Wikipedia seed 作为 gen-0，导致 LOGO 评估中 gen-0 出现在训练和测试中（train-test overlap）。论文正确指出 gen-0 per-class F1 = 0.94 是膨胀的，并采用 binary F1（排除 gen-0）= 0.694 作为主要指标。但论文 Table 1 和 Section 4.1 第一段仍突出报告"3-class LOGO macro F1 = 0.762"，且 Abstract 将任务定义为"generation depth classification (gen-0/gen-1/gen-2+)"。
- 建议：(a) 在 Abstract 中更明确区分两个指标及其含义；(b) 考虑在 Table 1 中将 3-class F1 标注 caveat 或降级呈现。

**W5** [warning] Feature selection 缺少系统化方法论

- 具体位置：Section 3.3
- 问题：7 个特征从 NLL 分布统计量（mean, std, min, max, tail decay）和词汇多样性指标（TTR, hapax ratio）中选取。选择理由是"two complementary views of distributional drift"，但为什么恰好是这 7 个？为什么不包括 NLL skewness/kurtosis、句法复杂度、perplexity 变异系数等？LOFO 分析（Appendix F）验证了已选特征的贡献，但这是事后验证而非先验特征选择。
- 建议：讨论特征空间的探索过程，或至少说明为什么这些特征是充分的（不一定最优）。

---

## 小问题（不影响接收）

1. **Figure 1b 信息密度过高**：7 个特征 × 多个统计量在一张小图中，打印后难以辨认具体数值。建议拆分或提供 supplementary table 对应。

2. **"Depth fingerprinting" 术语**：Fingerprinting 通常指唯一识别（如 browser fingerprinting），但本文做的是分类（classification）。术语可能引起误解。

3. **Appendix 数量过多（15+）**：虽然审稿人不要求阅读附录，但如此多的附录暗示正文未能有效组织核心信息。部分关键结果（如 TOST equivalence testing, Appendix L）应前置到正文。

4. **引用格式**：verify_references 显示 4 个 bib 条目有轻微作者名格式差异（如 Gutiérrez vs guti\'errez），建议统一。

5. **Wikipedia-only seeds**：主实验仅用 Wikipedia，Appendix J 显示跨域（Academic, Code, News）performance 下降（binary F1 降至 0.628-0.746），但正文对此讨论不足。

---

## 主要优势

1. **新颖的任务定义**：将 binary 检测扩展为 ordinal depth classification 是一个有意义的 conceptual contribution，与 model collapse 和数据质量文献有清晰连接。

2. **DDR 观察的经验价值**：尽管框架有内部一致性问题，"drifting vs. stationary" 的分解确实捕捉了递归生成中 NLL 分布变化的不同维度，这一经验发现对理解 LLM 文本退化有科学价值。

3. **全面的 confound 控制**：seed sharing control（seed demeaning + independent seed, §4.1）、length confound（Appendix B）、domain generalization（Appendix J）、temperature sensitivity（Appendix H/O）、prompt-type robustness（Appendix C）。这种系统性的 confound 分析在 AI-text detection 文献中较为少见，值得肯定。

4. **诚实的局限性报告**：论文在 Limitations section 和 Discussion 中坦诚报告了 instruction tuning 信号崩溃、模型规模限制、温度敏感性等负面结果，没有试图掩盖核心弱点。

5. **统计方法论整体规范**：Bootstrap CI、Bonferroni correction、McNemar test、TOST equivalence testing（附录）的使用整体正确。效应量（Cohen's d, Spearman ρ）的系统性报告符合良好的统计实践。

6. **计算效率优势**：单个 410M 参考模型 + 7 个特征 + XGBoost = 极低推理成本（相对于 neural baseline）。这是一个实际部署优势（如果适用场景存在的话）。

---

## 向作者提问

1. 是否有任何 >8B base model 的实验数据（即使是 pilot）？Llama-3.1-13B 或 Qwen-14B 等模型是否显示 depth signal 存在？

2. Instruction tuning 导致信号崩溃的根本原因是什么？是 instruction tuning 消除了 NLL 分布的 depth-dependent 结构，还是引入了更强的 prompt-dependent 变异覆盖了 depth signal？

3. 参考模型选择（Pythia-410M）的敏感性如何？如果用 Qwen-0.5B 或 OLMo-1B 作参考模型，DDR 模式是否一致？Section 4.2 提到"reference-specific (LOGO) F1 varies by ≤0.013 across Pythia, OLMo, and Qwen reference models"，但仅在同一 LOGO 实验中验证，未测试完全不同规模/家族的参考模型。

4. entropy_std 为什么有高 Cohen's d（0.55）但低 Spearman ρ（0.16）？这是否意味着 depth 与 entropy_std 之间存在非单调关系？如果是，DDR 的"单调漂移 vs. 静态"二分法是否过于简化？

5. 3-class 分类中 gen-1 vs. gen-2+ 的 confusion（Figure 5b 显示 gen-1 recall = 75%, gen-2+ recall = 73.7%）主要来自哪些 generator？是否某些 generator family 的 gen-1 和 gen-2+ 在特征空间中根本不可分？

---

## 缺失引用

1. **Kirchenbauer et al., 2024** "On the Reliability of Watermarks for Large Language Models" (ICLR 2024) — 与 watermarking 的 depth-robustness 讨论相关
2. **Tang et al., 2024** "The Science of Detecting LLM-Generated Text" (Communications of the ACM) — detection 领域的综合性综述，应在 Related Work 中引用
3. **Li et al., 2024** "Deepfake Text Detection in the Wild" (WWW 2024) — 关于 wild-setting 检测的直接相关工作
4. 论文引用 59 篇文献，对于一篇 EMNLP long paper（含 15+ appendices）偏少。尤其是 model collapse 相关文献（仅引用 3 篇核心论文）和 stylometry 文献（仅引用 2 篇综述）的覆盖可以更完整。

---

## Overall Assessment 详细理由

**评分: 3.0 (Findings)**

本文的主要贡献是：(1) 提出了生成深度分类这一新任务，(2) 发现了 DDR 现象，(3) 展示了简单特征 + 分类器可以在 base model 设定下实现跨生成器泛化。这些贡献对 AI-text detection 社区有科学参考价值。

但以下因素阻止本文达到 Conference (4.0) 水平：
- Instruction tuning 信号崩溃（F1: 0.763 → 0.338）使方法缺乏实际部署场景
- 模型规模限于 0.6B-8B，无法验证 depth signal 在大模型上的存在性
- DDR 框架有内部一致性问题（2/7 特征不符合框架）
- Baseline 比较方法论不够公平

论文适合 Findings track：它提供了一个有意义的实证发现和分析框架，尽管实际影响力受限。作者若能 (a) 在修改中添加至少一个 >8B 模型和一个 instruction-tuned model 的系统结果，(b) 修正 DDR 叙事以反映三分类而非二分类，(c) 重新 frame 贡献为分析性发现，论文有潜力提升至 3.5（Borderline Conference）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1030 · 2026-05-18T09:14:29.274498+00:00_

Reviewer 1 审稿报告已收到，评分 3.0 (Findings)。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 97

## Round 97

6 recorded events


### User

_source line 1031 · 2026-05-18T09:14:30.713447+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告已提交至 Review Director。

**审稿结果摘要：**

- **Overall: 3.0 (Findings)**
- **Soundness: 3.5/5** | **Excitement: 3.0/5** | **Reproducibility: 4/5**

**3 个 Must-Fix 问题：**
1. DDR 二分框架内部不一致（entropy_std/min 不符合 drifting/stationary 划分，7 个特征中 2 个例外）
2. Instruction tuning 导致信号崩溃（F1: 0.763→0.338），实际应用场景极为有限
3. 模型规模仅覆盖 0.6B-8B，无 >8B 数据点验证 depth signal 的 scaling trend

**5 个 Should-Fix 问题：** Baseline 比较不公平、DDR 阈值 post-hoc、温度敏感性讨论不足、Gen-0 seed sharing 膨胀 3-class F1、特征选择缺少系统化方法论

---

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿意见

**论文**: "Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains"
**审查侧重**: 新颖性 + 写作质量 + 格式合规 + 相关工作覆盖

---

## 总体评分

**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 扎实的实证研究揭示了递归生成链中的差异深度响应(DDR)现象，但新颖性受限于与并发工作的重叠、仅限 base model 的生态效度局限，以及潜在的页数超限问题。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 方法论合理，LOGO 交叉验证设计良好，但 DDR 发现与 model collapse drift 的因果区分不充分 |
| Excitement | 2.5/5 | 现象本身有趣但不令人兴奋；与 Broken Telephone / Markovian Chains 的增量有限 |
| Reproducibility | 4.0/5 | 特征定义清晰，评估协议详尽，承诺开源代码和数据 |
| Overall Assessment | 2.5/5 | Borderline Findings — 需要加强新颖性论证并修复格式问题 |
| Reviewer Confidence | 4/5 | 熟悉 AI 文本检测、model collapse、stylometry 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文页数疑似超过 8 页限制
- 具体位置：Page 8-9（Section 5 Discussion 从 Page 8 底部开始，Section 6 Conclusion 在 Page 9 中部，Limitations 在 Page 9 下半部分）
- 问题：ACL ARR Long Paper 限制为 8 页正文内容（Limitations/Ethics/References/Appendix 不计入）。从 PDF 渲染来看，Section 6 Conclusion 结束位置约在第 9 页中部，主体内容约为 8.5-8.7 页，超出限制。
- 为什么影响接收：ARR CFP 明确写道 "Submissions that exceed the length requirements ... will be desk rejected."
- 建议修改方向：压缩 Discussion（当前约 1.5 栏）和 Results 中的部分冗余分析，将更多细节移入 Appendix。Figure 3 (LOGO binary F1 对比图) 可以考虑用 inline text 替代或缩小。

**N2** [critical] 新颖性与并发工作的区分不充分
- 具体位置：Section 2 (Related Work, lines 27-41)，Section 5 (Discussion)
- 问题：论文承认两个并发工作 — Broken Telephone (Mohamed et al., 2025) 和 Markovian Chains (Geng et al., 2026) — 均研究了 LLM 递归生成链中的信息退化。论文声称"both works independently converge on approximately three distinguishable classes"(Section 2），但对自身超越这两项工作的 **增量贡献** 阐述不足。具体而言：
  1. Broken Telephone 已经展示了递归生成导致信息失真，语义收敛到固定点 — 论文的 DDR 发现中"drifting features"部分与此高度重叠。
  2. Markovian Chains 已经建立了理论框架解释收敛动态 — 论文的 DDR 是否只是该理论预测的实证验证？
  3. 论文声称自己的区分在于"our DDR decomposition reveals what converges (location properties)"（Section 2），但这一区分的实质贡献量需要更有力的论证。
- 为什么影响接收：审稿人可能认为这是对已知现象的重新包装，而非独立的新贡献。
- 建议修改方向：
  (a) 在 Introduction 中明确列出本文相对于两个并发工作的 unique contribution（例如：DDR 的 drifting/stationary 分解、handcrafted feature 的实用分类器、cross-generator 泛化能力等）
  (b) 如果可能，补充一个直接对比实验：用 Broken Telephone 或 Markovian Chains 的方法在相同数据上运行，量化差异

**N3** [critical] DDR 发现与 model collapse drift 的因果关系未厘清
- 具体位置：Section 4.2 (Differential Depth Response)，Section 5 (Discussion)
- 问题：论文将 DDR 定位为核心发现，并在 Discussion 中将其与 model collapse literature 联系起来（"consistent with recursive generation inducing a location shift in the token-level NLL distribution"）。但论文未充分论证 DDR 是一个 **独立于** model collapse drift 的新现象，还是同一现象在 inference-time 递归生成中的 **直接表现**。
  - 如果 DDR 只是 model collapse drift 在 individual text 层面的微观表现，那么论文的 contribution 更多是"验证"而非"发现"。
  - 论文的 Limitations 部分（Page 9）提到 "the DDR framework ... is distinct from model collapse"，但论证仅一句话，不够有力。
- 为什么影响接收：核心 claim 的新颖性直接决定论文价值。
- 建议修改方向：设计一个实验或分析来严格区分 DDR 与 model collapse drift（例如：在不涉及 retraining 的纯 inference 链上，对比 DDR 信号与 training-time collapse 的信号强度差异，或展示 DDR 的 stationary component 在 model collapse 文献中没有对应物）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 仅限 Base Model，生态效度受限
- 具体位置：Section 3.1, Limitations (Page 9)
- 问题：所有 8 个生成器都是 base (pretrained) model。论文在 Limitations 中承认 instruction-tuned 模型下 signal 大幅退化（OLMo-2-IB-Instruct LOGO F1 = 0.338 vs. 0.763 base），但这正是当前实际最常用的模型类型。如果 depth signal 在 instruct model 上几乎消失，论文声称的 practical implication（如 data curation, provenance tracking）的可信度大打折扣。
- 建议：在 Discussion 中更坦诚地讨论这一局限，避免 over-claim；或者补充至少 2-3 个 instruct model 的实验以展示 signal 退化的 gradient。

**W2** [warning] Abstract 数据密度过高
- 具体位置：Abstract (Page 1)
- 问题：Abstract 在约 200 词内包含了至少 8 个具体数值（gen-0/gen-1/gen-2+、0.68-8B、F1=0.694、0.764、Cohen's d < 0.10、d > 0.75、410M、7-feature）。这削弱了 Abstract 的叙事力——审稿人在 30 秒内难以从密集数字中提取核心价值。
- 建议：减少到 3-4 个最关键的数字，将其余移入正文。例如保留 F1 和 Cohen's d 范围，删除具体参数量和特征数量。

**W3** [warning] 3-class F1 = 0.762 的实用性论证不足
- 具体位置：Section 4.1 (Table 1)，Section 5 (Discussion)
- 问题：7-feature ensemble 在 LOGO 8-generator 评估下 3-class macro F1 = 0.762，binary F1 = 0.694。考虑到这是 handcrafted features + XGBoost 的简单 pipeline，性能本身不构成方法论贡献。论文定位为 "phenomenon paper"，但 Discussion 中又暗示 practical applications（data curation, provenance）。如果是 phenomenon paper，应弱化 practical claims；如果追求实用性，F1 = 0.762 需要与实际部署场景的需求对比。
- 建议：明确论文定位——如果是 phenomenon paper，聚焦 DDR 发现的理论意义；如果追求实用性，需要更强的 baseline 和更高的性能。

**W4** [warning] Responsible NLP Research Checklist 缺失
- 具体位置：论文 PDF 中未发现 Responsible NLP Checklist
- 问题：ACL ARR 要求提交 Responsible NLP Research Checklist。虽然 checklist 可能作为 OpenReview 独立表单提交，但部分 venue 要求将其附在论文末尾。需确认 EMNLP 2026 的具体要求。
- 建议：确认提交流程；若需附在论文中，务必在提交前添加。

**W5** [warning] Introduction 叙事缺少从 "大问题" 到 "具体贡献" 的平滑过渡
- 具体位置：Section 1 Introduction (Pages 1-2)
- 问题：Introduction 的开头直接进入 "LLM-generated text increasingly re-enters the web" 的具体场景，缺少更高层次的 framing（为什么 text provenance matters for the broader NLP community）。从第二段的 "binary real-vs-synthetic detection" 到 "generation depth classification" 的跳跃较大，读者可能不清楚为什么需要从 binary 扩展到 depth classification。
- 建议：第一段开头用 1-2 句建立更宏观的动机（例如 training data quality assurance, content authenticity），然后再切入递归生成链的具体问题。

---

## 小问题（不影响接收）

1. **Table 1** (Page 7)：表中 "---" 用于表示缺失值，在 ACL 论文中不常见，建议用 "—" 或 "N/A"。
2. **Figure 1** (Page 4)：subplot (b) 中的 horizontal bar labels 字体较小（接近 7pt 下限），在打印时可读性可能受影响。
3. **Bib entry 小问题**（来自引用验证工具）：
   - `self_consuming_mad`：OpenAlex 记录的 first author 是 Casco-Rodriguez，而 bib 中为 Alemohammad — 需确认哪个正确。
   - `llama3`：OpenAlex first author 为 Aaron（可能是排序问题），bib 中为 Grattafiori — 这是 Llama 3 论文的已知作者列表变更，可忽略。
   - `qwen3`：author 为 "Qwen Team"，OpenAlex 为 "Yang" — 集体作者 vs. 个人作者的差异。
4. **术语一致性**："generation depth" 和 "recursive generation depth" 在全文中交替使用，建议统一为一个术语。
5. **Section 3.3** (Page 5)："entropy_min" 作为 feature name 缺少解释——是 reference model 的 token-level entropy 的 minimum 吗？虽然在上下文中可推断，但首次出现时应明确定义。

---

## 相关工作覆盖评估

**引用数量**：59 篇引用，对 EMNLP 论文而言属于合理范围。

**覆盖完整性**：
- ✅ AI 文本检测方法：覆盖全面（DetectGPT, Fast-DetectGPT, Binoculars, GLTR, Ghostbuster, RADAR, DNA-GPT 等）
- ✅ Model collapse 理论：覆盖充分（Shumailov et al., Alemohammad et al., Dohmatob et al., Gerstgrasser et al.）
- ✅ 并发工作：已引用 Broken Telephone 和 Markovian Chains
- ✅ Ordinal classification 方法：CORAL, CORN, Frank-Hall
- ✅ 数据质量/水印：DSIR, QuRating, CCNet, SynthID, Kirchenbauer et al.
- ⚠️ Stylometry：仅引用 Stamatatos (2009) 和 Koppel (2009)，缺少 2015 年后的更新综述（如 Neal et al., 2017 "Surveying Stylometry Techniques and Applications"；Stamatatos 2009 虽是经典但已 17 年）
- ⚠️ 缺少 **多步文本处理链检测** 的相关工作 — 例如 translation chain detection、multi-step paraphrase 检测等，这些与 recursive generation chain 有概念上的相似性
- ⚠️ Fine-grained AI text detection 的引用偏少 — Beyond Binary (Cheng et al., 2025) 是唯一一篇 fine-grained 方向的工作，但该领域还有 Pu et al. (2023) "Deepfake Text Detection in the Wild" 等

**引用验证结果**（基于 OpenAlex 在线核查）：
- 48/59 条目验证通过
- 7 条未在 OpenAlex 中找到（detectgpt, reliable_detection, detection_possibilities, defactify_dataset, aaronson_watermark, pythia, xgboost）— 这些都是知名论文，未找到可能是 OpenAlex 索引覆盖问题，不构成 fake citation 风险
- 4 条存在 author 不匹配（self_consuming_mad, qwen3, gutierrez_ordinal_survey, llama3）— 均为 author 排序或编码差异，属于 minor bib formatting 问题
- 0 条 orphan entries（所有 bib 条目均被引用）
- 0 条 missing entries（所有 \cite 命令都有对应 bib 条目）

---

## AI 写作痕迹检查

**结论：写作风格干净，AI 痕迹极少。**

| 检查项 | 数量 | 评估 |
|--------|------|------|
| Em-dash (—) in prose | 0 | ✅ 仅出现在文件头注释中 |
| 解释性 en-dash ( – ) | 0 | ✅ |
| AI 用词黑名单 (delve, leverage, utilize 等) | 0 | ✅ |
| Furthermore/Moreover/Additionally | 0 | ✅ |
| -ing 短语滥用 | 2 处 ("enabling") | ✅ 在自然技术语境中，可接受 |
| LaTeX "---" | 23 处 | ✅ 全部在表格中作占位符，非行文 em-dash |

---

## 主要优势

1. **实验设计严谨**：LOGO (Leave-One-Generator-Out) 交叉验证是评估 cross-generator 泛化能力的正确选择；seed sharing across generators 有效控制了 topic confound。
2. **DDR 分解框架有分析价值**：将特征分为 drifting（entropy, TTR, hapax ratio）和 stationary（tail decay）两类，提供了理解递归生成链统计特性的有用透镜。
3. **丰富的 ablation 和 robustness 分析**：15 个 appendix 覆盖了 length confound、temperature sensitivity、prompt-type generalization、cross-domain evaluation、error analysis、LOFO analysis 等，显示了充分的实验工作量。
4. **写作质量良好**：AI 写作痕迹极少，行文简洁。
5. **引用完整性高**：59 篇引用全部有对应 bib 条目，无 orphan 或 missing 引用。

---

## Questions for Authors

1. DDR 的 stationary component（shape features 如 tail decay）在 model collapse 文献中是否有对应物？如果 model collapse 也展示了类似的 shape stationarity，DDR 的独立性如何成立？
2. 如果将 base model 替换为 instruction-tuned model（signal 大幅退化），是否意味着 depth fingerprinting 在 real-world 场景中基本不可用？作者如何回应这一质疑？
3. "Continue the following text" 是唯一的 generation prompt。在 open-ended generation（如 "Write an essay about..."）或 task-specific generation 下，DDR pattern 是否仍然成立？
4. 论文使用 Pythia-410M 作为 reference model 提取 NLL-based features。如果 reference model 的规模或架构改变，feature stability 如何？这是否引入了对 reference model 选择的隐性依赖？

---

## 总结

本文定义了 generation depth classification 任务并发现了 DDR 现象，实验工作扎实，写作质量良好。但三个核心问题限制了论文的竞争力：(1) 正文可能超过 8 页限制（desk reject 风险），(2) 与 Broken Telephone / Markovian Chains 两个并发工作的新颖性区分不充分，(3) 仅限 base model 的设定严重限制了实际应用价值。如果能解决页数问题、加强新颖性论证、并更坦诚地讨论 base-model-only 的局限，论文有潜力达到 Findings 门槛。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-18T09:15:07.256785+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 扎实的实证研究揭示了递归生成链中的差异深度响应(DDR)现象，但新颖性受限于与并发工作的重叠、仅限 base model 的生态效度局限，以及潜在的页数超限问题。\n\n**Soundness**: 3.0/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数疑似超过 8 页限制\n- ACL ARR Long Paper 限制为 8 页正文（Limitations/Ethics/References/Appendix 不计入）。从 PDF 渲染来看，Section 6 Conclusion 结束位置约在第 9 页中部，主体内容约为 8.5-8.7 页，超出限制。\n- ARR CFP: \"Submissions that exceed the length requirements ... will be desk rejected.\"\n\n**N2** [critical] 新颖性与并发工作的区分不充分\n- Broken Telephone 已展示递归生成导致信息失真，语义收敛到固定点 — DDR 的\"drifting features\"与此高度重叠。\n- Markovian Chains 已建立理论框架解释收敛动态 — DDR 是否只是该理论预测的实证验证？\n- \"our DDR decomposition reveals what converges (location properties)\" 这一区分的实质贡献量需更有力论证。\n\n**N3** [critical] DDR 发现与 model collapse drift 的因果关系未厘清\n- DDR 是独立于 model collapse drift 的新现象，还是同一现象在 inference-time 递归生成中的直接表现？\n- Discussion 中的区分（\"distinct from model collapse\"）仅一句话，论证不够有力。\n\n### Should-Fix 问题\n\n**W1** [warning] 仅限 Base Model，生态效度受限\n- instruction-tuned 模型下 signal 大幅退化（OLMo-2-1B-Instruct F1=0.338 vs. 0.763 base），实际最常用的模型类型。\n- data curation/provenance tracking 的 practical implication 可信度受限。\n\n**W2** [warning] Abstract 数据密度过高\n- 约 200 词内至少 8 个具体数值，削弱叙事力。审稿人 30 秒内难以提取核心价值。\n\n**W3** [warning] 3-class F1 = 0.762 的实用性论证不足\n- handcrafted features + XGBoost 的简单 pipeline，性能不构成方法论贡献。\n- 如果是 phenomenon paper 应弱化 practical claims；如果追求实用性需更强 baseline 和更高性能。\n\n**W4** [warning] Responsible NLP Research Checklist 缺失\n- ACL ARR 要求提交 Responsible NLP Research Checklist。论文 PDF 中未发现。\n\n**W5** [warning] Introduction 叙事缺少从\"大问题\"到\"具体贡献\"的平滑过渡\n- 开头直接进入具体场景，缺少更高层次 framing。从 binary detection 到 depth classification 的跳跃较大。\n\n### 小问题\n1. Table 1 中 \"---\" 不常见\n2. Figure 1 subplot (b) 字体接近 7pt 下限\n3. Bib entry author 不匹配（self_consuming_mad, qwen3, llama3）\n4. \"generation depth\" vs \"recursive generation depth\" 术语不一致\n5. entropy_min 首次出现时定义不够明确\n\n### 缺失引用\n- Stylometry 方向需 2015 后更新综述\n- 多步文本处理链检测相关工作\n- Fine-grained AI text detection 引用偏少\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 扎实的实证研究揭示了递归生成链中的差异深度响应(DDR)现象，但新颖性受限于与并发工作的重叠、仅限 base model 的生态效度局限，以及潜在的页数超限问题。\n\n**Soundness**: 3.0/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数疑似超过 8 页限制\n- ACL ARR Long Paper 限制为 8 页正文（Limitations/Ethics/References/Appendix 不计入）。从 PDF 渲染来看，Section 6 Conclusion 结束位置约在第 9 页中部，主体内容约为 8.5-8.7 页，超出限制。\n- ARR CFP: \"Submissions that exceed the length requirements ... will be desk rejected.\"\n\n**N2** [critical] 新颖性与并发工作的区分不充分\n- Broken Telephone 已展示递归生成导致信息失真，语义收敛到固定点 — DDR 的\"drifting features\"与此高度重叠。\n- Markovian Chains 已建立理论框架解释收敛动态 — DDR 是否只是该理论预测的实证验证？\n- \"our DDR decomposition reveals what converges (location properties)\" 这一区分的实质贡献量需更有力论证。\n\n**N3** [critical] DDR 发现与 model collapse drift 的因果关系未厘清\n- DDR 是独立于 model collapse drift 的新现象，还是同一现象在 inference-time 递归生成中的直接表现？\n- Discussion 中的区分（\"distinct from model collapse\"）仅一句话，论证不够有力。\n\n### Should-Fix 问题\n\n**W1** [warning] 仅限 Base Model，生态效度受限\n- instruction-tuned 模型下 signal 大幅退化（OLMo-2-1B-Instruct F1=0.338 vs. 0.763 base），实际最常用的模型类型。\n- data curation/provenance tracking 的 practical implication 可信度受限。\n\n**W2** [warning] Abstract 数据密度过高\n- 约 200 词内至少 8 个具体数值，削弱叙事力。审稿人 30 秒内难以提取核心价值。\n\n**W3** [warning] 3-class F1 = 0.762 的实用性论证不足\n- handcrafted features + XGBoost 的简单 pipeline，性能不构成方法论贡献。\n- 如果是 phenomenon paper 应弱化 practical claims；如果追求实用性需更强 baseline 和更高性能。\n\n**W4** [warning] Responsible NLP Research Checklist 缺失\n- ACL ARR 要求提交 Responsible NLP Research Checklist。论文 PDF 中未发现。\n\n**W5** [warning] Introduction 叙事缺少从\"大问题\"到\"具体贡献\"的平滑过渡\n- 开头直接进入具体场景，缺少更高层次 framing。从 binary detection 到 depth classification 的跳跃较大。\n\n### 小问题\n1. Table 1 中 \"---\" 不常见\n2. Figure 1 subplot (b) 字体接近 7pt 下限\n3. Bib entry author 不匹配（self_consuming_mad, qwen3, llama3）\n4. \"generation depth\" vs \"recursive generation depth\" 术语不一致\n5. entropy_min 首次出现时定义不够明确\n\n### 缺失引用\n- Stylometry 方向需 2015 后更新综述\n- 多步文本处理链检测相关工作\n- Fine-grained AI text detection 引用偏少\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-18T09:15:38.127941+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30871
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-18T09:15:38.328826+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 二分框架的内部一致性缺陷\n- 7 个特征中 entropy_std（d=0.55, |ρ|=0.16）和 entropy_min（pooled d=0.40）不符合 drifting/stationary 二分框架。\n- Section 4.2 承认\"the remaining two require qualification\"，意味着 28.6% 的特征不符合论文自定义的分类标准。\n- DDR 的\"两类特征行为截然不同\"核心叙事被削弱。\n- 建议：将特征明确分为三类（drifting/intermediate/stationary），或提供 equivalence test 支持。\n\n**N2** [critical] Instruction tuning 导致信号崩溃，实际应用价值存疑\n- OLMo-2-1B-Instruct LOGO F1=0.338（vs. base 0.763）。\n- Introduction 以\"LLM-generated text re-enters the web\"为动机暗示实际检测应用，但方法仅适用于 base model 输出。\n- 动机与方法适用范围之间存在严重脱节。\n- 建议：重新 frame 为分析性/科学性发现，或至少在 2-3 个 instruct models 上报告完整结果。\n\n**N3** [critical] 模型规模覆盖不足（0.6B-8B），claim 泛化性缺乏支撑\n- 8 个 generator 全在 0.6B-8B。Table 1 显示 Mistral-7B（F1=0.633）和 Qwen3-8B（F1=0.692）下降趋势。\n- 标题\"Base LLM Text Chains\"暗示更广适用范围，但无 >8B 数据点。\n- 建议：添加至少一个 >8B 模型的实验。\n\n### Should-Fix 问题\n\n**W1** [warning] Baseline 比较方法论不公平\n- 将 binary detection 方法的分数\"repurposed as ordinal depth predictors\"与专门设计的 7 特征比较，不是 apples-to-apples。\n- 建议：为 baseline 提取类似 distributional features，或承认是 convenience comparison。\n\n**W2** [warning] DDR 阈值选择为 post-hoc，缺少先验理由\n- |ρ|=0.10 和 d=0.10 作为分界线无先验理论依据。\n- 建议：引用 Cohen 或 Lakens (2017) equivalence testing 框架。\n\n**W3** [warning] 温度敏感性限制实际适用性\n- t=0.7→1.0 跨温度迁移：Qwen3-1.7B F1 从 0.789 降至 0.418。\n- 建议：Discussion 中更突出讨论温度作为核心部署障碍。\n\n**W4** [warning] Gen-0 seed sharing 导致 3-class F1 膨胀\n- 所有 generator 共享 1000 个 Wikipedia seed，LOGO 中 gen-0 训练/测试重叠。\n- Table 1 仍突出 3-class F1=0.762，Abstract 定义任务为 gen-0/gen-1/gen-2+。\n- 建议：Abstract 更明确区分两个指标含义。\n\n**W5** [warning] Feature selection 缺少系统化方法论\n- 为什么恰好这 7 个特征？为什么不包括 NLL skewness/kurtosis、句法复杂度等？\n- LOFO 是事后验证而非先验选择。\n- 建议：讨论特征空间探索过程。\n\n### 小问题\n1. Figure 1b 信息密度过高\n2. \"Depth fingerprinting\" 术语可能引起误解（fingerprinting vs classification）\n3. Appendix 数量过多（15+）\n4. 引用格式：4 个 bib 条目有作者名格式差异\n5. Wikipedia-only seeds，跨域 performance 下降讨论不足\n\n### 缺失引用\n1. Kirchenbauer et al., 2024 (ICLR) — watermarking depth-robustness\n2. Tang et al., 2024 (CACM) — detection 综述\n3. Li et al., 2024 (WWW) — wild-setting 检测\n4. Model collapse 引用仅 3 篇，stylometry 仅 2 篇\n\n### 向作者提问\n1. 是否有 >8B base model 数据？\n2. Instruction tuning 信号崩溃的根本原因？\n3. 参考模型选择敏感性？\n4. entropy_std 高 d 但低 ρ 的原因？\n5. gen-1 vs. gen-2+ confusion 的 generator-specific 分析？\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 二分框架的内部一致性缺陷\n- 7 个特征中 entropy_std（d=0.55, |ρ|=0.16）和 entropy_min（pooled d=0.40）不符合 drifting/stationary 二分框架。\n- Section 4.2 承认\"the remaining two require qualification\"，意味着 28.6% 的特征不符合论文自定义的分类标准。\n- DDR 的\"两类特征行为截然不同\"核心叙事被削弱。\n- 建议：将特征明确分为三类（drifting/intermediate/stationary），或提供 equivalence test 支持。\n\n**N2** [critical] Instruction tuning 导致信号崩溃，实际应用价值存疑\n- OLMo-2-1B-Instruct LOGO F1=0.338（vs. base 0.763）。\n- Introduction 以\"LLM-generated text re-enters the web\"为动机暗示实际检测应用，但方法仅适用于 base model 输出。\n- 动机与方法适用范围之间存在严重脱节。\n- 建议：重新 frame 为分析性/科学性发现，或至少在 2-3 个 instruct models 上报告完整结果。\n\n**N3** [critical] 模型规模覆盖不足（0.6B-8B），claim 泛化性缺乏支撑\n- 8 个 generator 全在 0.6B-8B。Table 1 显示 Mistral-7B（F1=0.633）和 Qwen3-8B（F1=0.692）下降趋势。\n- 标题\"Base LLM Text Chains\"暗示更广适用范围，但无 >8B 数据点。\n- 建议：添加至少一个 >8B 模型的实验。\n\n### Should-Fix 问题\n\n**W1** [warning] Baseline 比较方法论不公平\n- 将 binary detection 方法的分数\"repurposed as ordinal depth predictors\"与专门设计的 7 特征比较，不是 apples-to-apples。\n- 建议：为 baseline 提取类似 distributional features，或承认是 convenience comparison。\n\n**W2** [warning] DDR 阈值选择为 post-hoc，缺少先验理由\n- |ρ|=0.10 和 d=0.10 作为分界线无先验理论依据。\n- 建议：引用 Cohen 或 Lakens (2017) equivalence testing 框架。\n\n**W3** [warning] 温度敏感性限制实际适用性\n- t=0.7→1.0 跨温度迁移：Qwen3-1.7B F1 从 0.789 降至 0.418。\n- 建议：Discussion 中更突出讨论温度作为核心部署障碍。\n\n**W4** [warning] Gen-0 seed sharing 导致 3-class F1 膨胀\n- 所有 generator 共享 1000 个 Wikipedia seed，LOGO 中 gen-0 训练/测试重叠。\n- Table 1 仍突出 3-class F1=0.762，Abstract 定义任务为 gen-0/gen-1/gen-2+。\n- 建议：Abstract 更明确区分两个指标含义。\n\n**W5** [warning] Feature selection 缺少系统化方法论\n- 为什么恰好这 7 个特征？为什么不包括 NLL skewness/kurtosis、句法复杂度等？\n- LOFO 是事后验证而非先验选择。\n- 建议：讨论特征空间探索过程。\n\n### 小问题\n1. Figure 1b 信息密度过高\n2. \"Depth fingerprinting\" 术语可能引起误解（fingerprinting vs classification）\n3. Appendix 数量过多（15+）\n4. 引用格式：4 个 bib 条目有作者名格式差异\n5. Wikipedia-only seeds，跨域 performance 下降讨论不足\n\n### 缺失引用\n1. Kirchenbauer et al., 2024 (ICLR) — watermarking depth-robustness\n2. Tang et al., 2024 (CACM) — detection 综述\n3. Li et al., 2024 (WWW) — wild-setting 检测\n4. Model collapse 引用仅 3 篇，stylometry 仅 2 篇\n\n### 向作者提问\n1. 是否有 >8B base model 数据？\n2. Instruction tuning 信号崩溃的根本原因？\n3. 参考模型选择敏感性？\n4. entropy_std 高 d 但低 ρ 的原因？\n5. gen-1 vs. gen-2+ confusion 的 generator-specific 分析？\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-18T09:15:40.041546+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1712
}
```

</details>

---


### Assistant

_source line 1036 · 2026-05-18T09:15:44.002698+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1037 · 2026-05-18T09:15:45.511021+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall: 2.5/5 (Borderline Findings)**
- 3 个 Must-Fix 问题：(1) 正文约 8.5-8.7 页，超 8 页限制有 desk reject 风险；(2) 与 Broken Telephone / Markovian Chains 的增量贡献区分不够充分；(3) DDR 发现与 model collapse drift 的因果关系未厘清
- 4 个 Should-Fix 问题：仅限 base model 的生态效度、Abstract 数据堆砌、3-class F1=0.762 的实用性定位模糊、Responsible NLP Checklist 可能缺失
- AI 写作痕迹检查通过（极少 AI 标志）
- 引用覆盖合理（59 篇，stylometry 方向略薄）
- 引用验证：48/59 在线验证通过，0 orphan，0 missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1038 · 2026-05-18T09:15:51.661555+00:00_

两位 Reviewer 的 Round 1 报告和交叉分享任务均已分派。等待交叉回应返回后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1039 · 2026-05-18T09:17:54.889073+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — Reviewer 2 Round 1 意见

---

## Must-Fix 问题回应

### [AGREE] R2-N1: 正文页数疑似超过 8 页限制

同意这是一个需要核实的严重问题。从 PDF 渲染来看（p8-p9），Section 4.3 和 Section 5 (Discussion) 在 p8 底部衔接，Section 6 (Conclusion) 在 p9 约 55-60% 处结束，Limitations 从此处才开始。这意味着 Sections 1-6 的主体内容约占 8.3-8.5 页，确实可能超出 ACL ARR Long Paper 的 8 页限制。

ARR CFP 明确规定超长提交将 desk reject，这是格式合规硬伤。但需要指出两点不确定性：(1) 精确页数需用 ACL 官方工具（如 aclpubcheck）验证，PDF 视觉估计可能有 ±0.1 页误差；(2) 如果作者通过压缩 Table 2 或 Figure 3 的空间即可在限制内，问题的严重性会降低。无论如何，**作者必须在修改中确认合规**。

### [REBUT] R2-N2: 新颖性与并发工作的区分不充分

R2 的担忧有一定道理，但我认为低估了本文的 incremental novelty。

1. **Broken Telephone (Mohamed et al., 2025)** 研究的是递归生成中的**语义信息失真**（information distortion, convergence to fixed points）。它不做深度分类，不分析特征层面的行为差异，没有提出 drifting vs. stationary 的二分法。本文的 DDR 提供了**特征层面的操作化分解**（Section 4.2: 哪些特征随深度漂移，哪些不变），这是 Broken Telephone 没有的具体贡献。

2. **Markovian Chains (Geng et al., 2026)** 建立了收敛动态的理论框架，但其分析层面是**分布整体的收敛性质**（Markov chain convergence），而非**单个文本的可分类特征**。本文从"理论上存在收敛"到"用 7 个特征实现跨生成器的深度分类"（LOGO binary F1 = 0.694, Table 1），中间有不小的实证 gap。

3. 关键区分：Broken Telephone 和 Markovian Chains 都没有尝试 **detection/classification task**。本文的核心贡献不仅是"DDR 存在"，还包括 (a) LOGO 跨生成器泛化协议，(b) 与 binary detection baselines 的系统对比（Table 2），(c) 全面的 confound 控制（seed demeaning, independent seeds, cross-temperature, cross-domain）。这些是 task-oriented 贡献，不是并发工作的简单重复。

**但我同意**论文 Related Work (Section 2) 对这两篇工作的区分论证确实不够清晰。Section 2 用"our DDR decomposition reveals what converges"一句话带过，需要扩展为一段完整的 positioning 论证。这是 writing 问题，不是 novelty 问题。

### [REBUT] R2-N3: DDR 与 model collapse drift 的因果关系未厘清

R2 认为 DDR 与 model collapse 的关系需要更有力论证，这一点我部分不同意。

**概念上二者有清晰区别**：Model collapse 是一个 **training-time** 现象（模型在自身输出上重新训练后退化，Shumailov et al., 2024; Dohmatob et al., 2025），DDR 是一个 **inference-time** 现象（同一个模型在递归生成中文本统计量的变化）。本文 Section 5 (Discussion) 确实只用一句话区分，但 Section 1 (Introduction) 的 framing 已隐含了这一区别：论文研究的是"text chains"而非"model re-training"。

不过，R2 的深层担忧有合理之处：DDR 的 drifting features（entropy mean 向低方向漂移 = 可预测性增加，TTR/hapax 下降 = 多样性降低）**定性上与 model collapse 预测的退化方向一致**（Alemohammad et al., 2024 的 MAD 效应）。论文应明确回应：这种方向一致性是否暗示 inference-time recursive generation 是 model collapse 的微型版本？还是仅仅是统计上的巧合？Discussion 中增加 1-2 段分析会显著加强论文。

**但我不认为这构成 Must-Fix**——DDR 作为一个 inference-time 的实证观察，其价值不依赖于与 model collapse 的因果关系是否被完全厘清。将此降级为 Should-Fix 更合适。

---

## Should-Fix 问题回应

### [AGREE] R2-W1: 仅限 Base Model，生态效度受限

完全同意，这也是我自己审稿中的 **N2 (critical)**。Instruction tuning 导致 LOGO F1 从 0.763 下降到 0.338（Section 9, Limitations），信号近乎崩溃。现实中绝大多数 LLM 输出来自 instruction-tuned 模型，这严重限制了论文声称的 data provenance tracking 应用场景。

我在自己的审稿中进一步建议：作者应将论文 framing 从"检测工具"转向"分析性/科学性发现"，以匹配方法的实际适用范围。

### [AGREE] R2-W2: Abstract 数据密度过高

同意。Abstract 中至少出现了以下数值：0.6B-8B, 8 models, 5 families, Cohen's d < 0.10, d > 0.75, 7-feature, F1 = 0.694, F1 = 0.764。在 ~200 词篇幅内堆砌 8+ 个数字确实削弱了叙事力。按 CLAUDE.md 中的写作规范（§2.2: "Abstract 不是 Results 的缩写，最多引用 2-3 个关键数字"），当前 Abstract 明显超标。

建议保留 binary F1 = 0.694（核心指标）和 cross-model F1 = 0.764（泛化证据），其他数字移入正文。

### [REBUT] R2-W3: 3-class F1 = 0.762 的实用性论证不足

R2 认为 handcrafted features + XGBoost 的简单 pipeline "性能不构成方法论贡献"。我部分不同意。

1. **简单性本身是一种贡献**：Figure 3 (p8) 显示 7-feature ensemble 在 binary F1 vs. inference cost 的 tradeoff 中，用单个 410M 参考模型 + 极低计算量达到与多 detector 组合可比的性能。在 AI-text detection 领域，过度依赖大型 neural baselines（如 fine-tuned RoBERTa）导致部署成本高昂，轻量级方案有独立价值。

2. **但我同意论文的 positioning 有问题**：论文同时声称 scientific discovery (DDR) 和 practical detection，两条线互相削弱。如果定位为 phenomenon paper with practical implications，DDR 是 main contribution 而 classifier 是 proof-of-concept，叙事会更清晰。

3. **F1 = 0.694 本身确实不足以支撑 standalone practical claim**：在实际部署中，binary F1 < 0.70 意味着约 30% 的错误率，这对于 high-stakes 应用（如学术诚信检测）不够可靠。

综合：R2 的方向正确，但"性能不构成方法论贡献"过于绝对。应建议作者**明确 primary contribution 是 DDR 发现**，classifier 是 proof-of-concept 验证。

### [AGREE] R2-W4: Responsible NLP Research Checklist 缺失

如果 Checklist 确实未包含在提交材料中，这是 ARR 提交的合规问题。但需注意两点：(1) ARR 的 Checklist 通常在 OpenReview 系统中单独填写，不一定出现在 PDF 内；(2) 论文确实包含了 Limitations section 和 Ethics Statement (Section 10)，这满足了部分合规要求。

**我无法确认 Checklist 是否在 PDF 中缺失**——从我阅读的 24 页 PDF 来看，未在附录末尾看到 Checklist，但它可能以单独文件提交。建议 Director 向作者确认。

### [AGREE] R2-W5: Introduction 叙事缺少从"大问题"到"具体贡献"的平滑过渡

部分同意。Introduction 开头以 model collapse 和 LLM text on the web 为切入点，然后跳转到 binary detection 的局限性，再引出 depth classification。这个叙事链是合理的，但缺少一个关键的中间环节：**为什么 depth 本身是重要的信息维度？** 论文假设读者已经接受"知道生成深度比知道是否 AI 生成更有价值"，但这一前提需要更有力的 motivation（如 data curation 场景中 depth 如何指导决策、多步污染对下游模型训练的差异影响等）。

不过，我不认为这比我自己在审稿中提出的问题（N1-N3）更严重，将其保持在 Should-Fix 级别是恰当的。

---

## 小问题回应

1. **Table 1 "---"**：[AGREE] 不标准，应使用 "—" 或 "N/A"
2. **Figure 1b 字体**：[AGREE] 这也是我在审稿中提到的信息密度过高问题
3. **Bib entry 不匹配**：[AGREE] 引用验证工具确认 self_consuming_mad, qwen3, llama3, gutierrez_ordinal_survey 有作者名格式差异
4. **术语不一致**：[AGREE] "generation depth" vs "recursive generation depth" 应统一
5. **entropy_min 定义**：[AGREE] 首次出现应明确定义为"token-level NLL 分布的最小值"

---

## 对 R2 Overall 评分的意见

R2 给出 2.5 (Borderline Findings)，我给出 3.0 (Findings)。差异主要来自：

1. **新颖性评估**：R2 认为与 Broken Telephone / Markovian Chains 重叠严重（降低 excitement 到 2.5）。我认为 DDR 的特征层面分解 + 跨生成器分类是增量贡献，不是简单重复。Excitement 应为 3.0。

2. **页数问题**：如果确认超限，这是严重的格式问题，但属于可修复的技术性问题（压缩 1-2 段即可），不应大幅影响 scientific merit 评估。

3. **Checklist 缺失**：同上，属于合规修复问题，不影响科学贡献评分。

**我维持 3.0 (Findings) 评分**，但同意如果页数超限问题属实且未修复，应降至 2.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1040 · 2026-05-18T09:17:59.691857+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1041 · 2026-05-18T09:18:09.483506+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

**Must-Fix 回应：**
- **[AGREE] R2-N1** 页数超限：PDF 视觉估计主体约 8.3-8.5 页，确需核实和修复
- **[REBUT] R2-N2** 新颖性：Broken Telephone / Markovian Chains 不做深度分类，DDR 的特征层面分解和 LOGO 评估协议是增量贡献，但 Related Work 的 positioning 论证确实需加强
- **[REBUT] R2-N3** DDR vs model collapse：两者有清晰的 training-time vs inference-time 概念区别，建议从 critical 降级为 should-fix，但同意 Discussion 需扩展论证

**Should-Fix 回应：**
- **[AGREE] R2-W1** base model 限制（与我自己的 N2 一致）
- **[AGREE] R2-W2** Abstract 数字过多
- **[REBUT] R2-W3** 简单 pipeline 的价值：简单性本身有价值，但同意应将 DDR 定位为 primary contribution
- **[AGREE] R2-W4** Checklist 需确认（可能在系统中单独提交）
- **[AGREE] R2-W5** Introduction 缺少"为什么 depth 重要"的中间论证

**评分差异**：维持我的 3.0 (Findings) vs R2 的 2.5，主要分歧在新颖性评估上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1042 · 2026-05-18T09:18:13.896914+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 101

## Round 101

12 recorded events


### User

_source line 1043 · 2026-05-18T09:18:56.133911+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题回应

**[AGREE] R1-N1: DDR 二分框架的内部一致性缺陷**

同意这是论文的核心叙事弱点。

论文 Section 4.2 (Page 7) 原文承认 "the remaining two require qualification"，其中：
- entropy_std: d=0.55（中等效应量）但 |ρ|=0.16（低单调性），论文将其归为 near-stationary 是基于 "pooled CV shift (<3% vs >15% for drifting features)"——这是用不同标准来强行归类。
- entropy_min: pooled |ρ|=0.40（不低），但论文辩称其变化集中在 gen-0/gen-1 边界，gen-1 vs gen-2+ 时 d=0.03。

R1 指出 28.6% 特征不符合二分框架，这一量化非常准确。论文试图用 "shifting these descriptive thresholds by ±0.10 does not alter feature grouping"（Section 4.2）来辩护，但这本身是 post-hoc 稳健性检验，不能替代框架定义的严谨性。

**补充意见**：三分法（drifting/intermediate/stationary）不仅更诚实，而且可能增强论文贡献——intermediate 特征的存在本身就是一个有趣的发现，可能暗示 DDR 是一个连续谱而非二元对立。这比强行塞入二分框架更有科学价值。

---

**[AGREE] R1-N2: Instruction tuning 导致信号崩溃，实际应用价值存疑**

完全同意，这也是我 Round 1 审稿中的 W1。

OLMo-2-1B-Instruct LOGO F1=0.338 vs base 0.763（Limitations, Page 9）意味着 depth signal 在 instruction-tuned model 上基本消失。考虑到当前绝大多数 web-facing LLM 输出来自 instruct/RLHF model，Introduction 中 "LLM-generated text increasingly re-enters the web and seeds subsequent generation"（Section 1, Page 1）的动机与方法的实际适用范围存在严重脱节。

我认为 R1 的两个建议都合理：
1. 重新 frame 为分析性发现（研究 base model 的递归生成统计特性），弱化 practical application claims；
2. 或者补充 2-3 个 instruct model 的完整实验以展示 signal 退化梯度。

方案 1 对投稿时间压力更现实。

---

**[REBUT] R1-N3: 模型规模覆盖不足（0.6B-8B），claim 泛化性缺乏支撑**

部分同意缺少 >8B 数据点，但反驳 R1 关于"下降趋势"的具体论断。

R1 声称 "Table 1 显示 Mistral-7B（F1=0.633）和 Qwen3-8B（F1=0.692）下降趋势"，暗示规模增大导致 signal 衰减。但从 Figure 6 (Page 22) 的 per-generator LOGO F1 来看，**同族内的规模趋势并不单调**：
- **Pythia 族**: 1B→0.718, 2.8B→0.724（规模增大，F1 **略升**）
- **Qwen3 族**: 0.6B→0.691, 1.7B→0.709, 8B→0.692（先升后降，但 8B ≈ 0.6B）
- Mistral-7B 的 F1=0.633 是最低的，但它是唯一的 Mistral 代表，无法区分规模效应与架构效应

因此，数据更多支持的是 **架构/家族差异** 而非 **规模衰减趋势**。Mistral 的低 F1 可能来自其架构特性（如 Sliding Window Attention），而非 7B 参数量本身。

**但我同意**：缺少 >8B 数据点确实是一个 gap。论文标题 "Base LLM Text Chains" 暗示了广泛适用性，至少应补充一个 13B+ 模型（如 Llama-3-13B 或 Qwen3-14B）或在 Limitations 中明确声明规模边界。将此从 critical 降为 warning 更合适。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: Baseline 比较方法论不公平**

同意。Section 4.3 (Page 8) 将 Fast-DetectGPT、Binoculars、LD-Score 的单一分数 "repurposed as ordinal depth predictors" 与专门设计的 7-feature ensemble 比较，确实不是 apples-to-apples。

论文的 framing "To contextualize the 7-feature ensemble's discriminative power"（Section 4.3 开头）在一定程度上缓解了这一问题——它没有声称 "beat" baselines，而是声称 "contextualize"。但 Table 2 的呈现方式（并排比较、加粗最优）仍然暗示了竞争性对比。

R1 建议为 baseline 提取类似 distributional features 是理想方案但工作量较大。更 pragmatic 的修改是在 Section 4.3 开头明确声明："This comparison is intended to demonstrate that single detection scores do not capture ordinal depth structure, not to claim methodological superiority over these purpose-built detectors."

---

**[REBUT] R1-W2: DDR 阈值选择为 post-hoc，缺少先验理由**

部分反驳。R1 声称 "无先验理论依据"，但论文有两层辩护被 R1 忽略：

1. **Appendix L** (Page 20) 明确引用了 Lakens (2017) 的 equivalence testing 框架，并运行了 TOST（Two One-Sided Tests）检验。这正是 R1 建议引用的文献，说明作者已经做了这一步。
2. **d < 0.10 的理论基础**：Cohen's d=0.2 是公认的 "small" effect，d < 0.10 低于 "small" 的一半，在行为科学中被广泛视为 "negligible"。这不是随意选择。
3. Section 4.2 (Page 7) 报告 "shifting these descriptive thresholds by ±0.10 does not alter feature grouping"——即阈值选择具有稳健性。

**但我同意**：这些论证散落在正文和附录中，主线叙事（Section 4.2）未充分展开。建议在 Section 4.2 中补充一句引用 Cohen's benchmarks 的说明，并将 Appendix L 的 equivalence test 结果在正文中用一句话概括。

---

**[AGREE] R1-W3: 温度敏感性限制实际适用性**

部分同意，但需补充关键上下文。

R1 引用的 Qwen3-1.7B 从 F1=0.789 降至 0.418 是真实的（Figure 9b, Page 24）。但 **这是一个孤立的异常值**，不是普遍现象。Figure 9(b) 中其他 5 个 generator 在 0.7→1.0 跨温度条件下的表现：
- OLMo-2-1B: 0.763 → 0.763（完全稳定）
- Pythia-1B: 0.854 → 0.854（完全稳定）
- Pythia-2.8B: 0.804 → 0.804（完全稳定）
- Qwen3-0.6B: 0.820 → 0.820（完全稳定）
- Qwen3-8B: 0.688 → 0.702（略微提升）

**Qwen3-1.7B 是唯一出现灾难性退化的 generator**。这更可能是该 generator 在 T=1.0 下的特殊行为（论文 Appendix I 讨论了其 "higher fluency may further compress feature variance"），而非温度迁移的普遍问题。

因此，R1 的建议（Discussion 中更突出讨论温度障碍）是对的，但 framing 应该是 "temperature sensitivity is generator-specific, with Qwen3-1.7B as a cautionary case" 而非 "temperature is a general deployment barrier"。

---

**[AGREE] R1-W4: Gen-0 seed sharing 导致 3-class F1 膨胀**

同意。这是一个 subtle 但重要的评估方法论问题。

论文在 Table 1 脚注 (Page 7) 已承认："3-class F1 may carry upward bias from gen-0 seed sharing across generators; binary F1 is leak-free." 从 Confusion Matrix (Figure 5, Page 22) 看，gen-0 的 recall 高达 99.4%，远高于 gen-1 (75.0%) 和 gen-2+ (73.7%)，这与 seed sharing 导致的 gen-0 "泄露" 一致。

**但有一个缓解因素**：论文的 binary F1=0.694 完全排除了 gen-0，是 leak-free 的。Section 4.1 的 seed-sharing control 实验（Page 6，"An independent-seed experiment using completely disjoint seed pools per generator"）显示 binary F1 从 0.694 降至 0.646-0.666——下降约 4-7%，说明 seed sharing 的膨胀效应存在但有限。

同意 R1 的建议：Abstract 应更明确区分 3-class F1（含 gen-0 共享偏差）和 binary F1（leak-free）的含义。

---

**[AGREE] R1-W5: Feature selection 缺少系统化方法论**

同意。Section 3.3 (Page 5) 仅说 "We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed"——这是按语义分组，不是解释为什么选择这 7 个特征而非其他候选。

缺失的候选特征包括：
- NLL skewness/kurtosis（同样来自 reference model，计算成本为零）
- 句法复杂度（dependency parse depth 等）
- Zipf's law exponent（类似于 hapax ratio 但更理论化）
- Repetition metrics（n-gram repetition rate，与 model collapse 直接相关）

Appendix F 的 LOFO 分析是事后验证（"六个特征正贡献"），而非事前选择的理由。论文应至少补充一段解释特征空间探索过程，或承认这是 hypothesis-driven 而非 exhaustive search。

---

### 关于 R1 小问题的补充

**R1 小问题 2**（"Depth fingerprinting" 术语可能引起误解）：**同意**。"Fingerprinting" 在 NLP/security 领域通常指 unique identification（如 browser fingerprinting, model fingerprinting），而本文做的是 ordinal classification。标题用 "fingerprinting" 可能引导读者期望一个 identification system 而非 classification system。但改标题风险较大，建议在 Introduction 中加一句明确定义。

**R1 小问题 5**（Wikipedia-only seeds, 跨域下降）：**同意**。这与我 Round 1 审稿中的 N1（页数超限讨论）相关——如果需要压缩正文，建议将 cross-domain 分析从 Appendix 提升到正文 Discussion 中简要提及，因为这是 ecological validity 的核心问题。

### 关于 R1 缺失引用

R1 提到 4 组缺失引用。我核查后认为：
- **Kirchenbauer et al., 2024 (ICLR) watermarking depth-robustness**：已在论文中引用 (`watermark_llm`, Kirchenbauer et al., 2023, ICML)，R1 可能指的是同一组的后续工作（2024 ICLR 版本）。如果确有 2024 ICLR 论文，应补充。
- **Tang et al., 2024 (CACM) detection survey**：论文已引用 Wu et al. (2025) Computational Linguistics survey 和 Jawahar et al. (2020) survey，再加一篇综述是合理的。
- **Model collapse 仅 3 篇，stylometry 仅 2 篇**：同意 stylometry 偏少（我在 Round 1 也指出了这一点），model collapse 有 4 篇（Shumailov, Alemohammad, Dohmatob, Gerstgrasser）而非 3 篇。

---

## 总结：与 R1 的一致性评估

| R1 问题 | R2 判断 | 关键分歧 |
|---------|---------|----------|
| N1 DDR 框架缺陷 | AGREE | 无分歧，建议三分法 |
| N2 Instruct 信号崩溃 | AGREE | 无分歧 |
| N3 规模覆盖不足 | REBUT(部分) | R1 称存在下降趋势，数据不支持；但缺 >8B 数据是事实 |
| W1 Baseline 不公平 | AGREE | 无分歧 |
| W2 DDR 阈值 post-hoc | REBUT(部分) | 论文已引用 Lakens (2017) equivalence testing，R1 可能遗漏 Appendix L |
| W3 温度敏感性 | AGREE(部分) | Qwen3-1.7B 是孤立异常值，非普遍问题 |
| W4 Gen-0 膨胀 | AGREE | 无分歧 |
| W5 特征选择 | AGREE | 无分歧 |

**整体判断**：R1 给出 3.0 (Findings)，我给出 2.5 (Borderline Findings)。分歧主要在于：R1 认为实验设计和现象发现足够支撑 Findings，而我认为 (1) 与并发工作的增量贡献不充分，(2) 页数超限是 desk reject 风险——这两点 R1 未充分关注。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-18T09:19:25.424766+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"Compilation done\" && pdfinfo main.pdf 2>/dev/null | grep Pages",
  "description": "Compile paper and check total page count",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"Compilation done\" && pdfinfo main.pdf 2>/dev/null | grep Pages",
    "description": "Compile paper and check total page count",
    "timeout": "120000"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-18T09:19:28.039543+00:00_

Compilation done
Pages:           26
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_director_fec00603

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 2614
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-18T09:19:35.725624+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess, re\n\n# Find where Limitations section starts (it doesn't count toward page limit)\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n\n# Find page breaks and key section locations\npages = text.split('\\f')\nfor i, page in enumerate(pages[:12], 1):\n    # Check for section headers\n    for header in ['Limitations', 'Ethics Statement', 'References', 'Conclusion', 'Discussion']:\n        if header in page:\n            # Find approximate position\n            pos = page.index(header)\n            total = len(page)\n            pct = pos / total * 100 if total > 0 else 0\n            print(f'Page {i}: \\\"{header}\\\" found at ~{pct:.0f}% of page')\n\"\n",
  "description": "Check where key sections start in the PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess, re\n\n# Find where Limitations section starts (it doesn't count toward page limit)\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n\n# Find page breaks and key section locations\npages = text.split('\\f')\nfor i, page in enumerate(pages[:12], 1):\n    # Check for section headers\n    for header in ['Limitations', 'Ethics Statement', 'References', 'Conclusion', 'Discussion']:\n        if header in page:\n            # Find approximate position\n            pos = page.index(header)\n            total = len(page)\n            pct = pos / total * 100 if total > 0 else 0\n            print(f'Page {i}: \\\"{header}\\\" found at ~{pct:.0f}% of page')\n\"\n",
    "description": "Check where key sections start in the PDF"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-18T09:19:35.977342+00:00_

Page 8: "Conclusion" found at ~79% of page
Page 8: "Discussion" found at ~15% of page
Page 9: "Limitations" found at ~12% of page
Page 9: "Ethics Statement" found at ~84% of page
Page 10: "References" found at ~50% of page
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_director_fec00603

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-18T09:19:50.691560+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-18T09:19:50.743789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-18T09:23:17.571230+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# Round 17 (fresh review) — updated by Review Director 2026-05-18\n\n# === Recurring issues (reopened or updated) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"8 pages confirmed R14.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。两位 Reviewer 均 AGREE 为 desk reject 风险。\"}\n  action_items:\n    - {round: 13, action: \"Compress to 8 pages\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 17, action: \"压缩 Discussion/Results 约 0.2 页，确保 Conclusion 在 Page 8 内结束\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness — repurposed binary detectors\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"Detectors not designed for ordinal. Frame as 'repurposed baselines'.\"}\n    - {round: 15, reviewers: \"R1,R2\", note: \"Partial consensus: framework fair, threshold-based binary comparison nice-to-have.\"}\n    - {round: 16, reviewers: \"R1,R2\", note: \"R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled. Partial consensus.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: 两位 Reviewer 均 AGREE。建议在 §4.3 开头明确声明这是 contextualization 而非 methodological superiority claim。\"}\n  action_items:\n    - {round: 14, action: \"Method §3.4 states 'repurposed as depth predictors'\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"§4.3 开头加声明：comparison intended to demonstrate single scores lack ordinal structure, not claim superiority\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction insufficient — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison. Geng et al. 2026 needs verification.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: R2 升为 Must-Fix（增量贡献不充分），R1 REBUT（DDR 特征分解 + LOGO 协议是增量贡献，但 Related Work positioning 需加强）。部分分歧：novelty vs writing issue。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded: detailed 3-way comparison.\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Introduction 中明确列出相对并发工作的 unique contribution（特征层面 DDR 分解 + 跨生成器分类 + confound 控制体系）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"R16 fresh: Intro still opens with instruct-model evidence. Dynamical system framing present but secondary.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: Instruct F1=0.338 vs base 0.763。两位 Reviewer 均 AGREE Introduction 动机（LLM text re-enters web）与方法适用范围（仅 base models）严重脱节。建议重新 frame 为分析性/科学性发现。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"重新 frame 论文贡献为科学发现（understanding distributional drift），弱化 practical detection/curation claims\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === New R17 issues ===\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致 — entropy_std/min 不符合 drifting/stationary 划分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"entropy_std (d=0.55, |ρ|=0.16) 和 entropy_min (pooled |ρ|=0.40) 不符合二分框架。7 特征中 28.6% 例外。两位 Reviewer 均 AGREE，建议三分法（drifting/intermediate/stationary）。\"}\n  action_items:\n    - {round: 17, action: \"将 DDR 特征分为三类（drifting/intermediate/stationary），修改 Abstract/Intro/Results 叙事\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高（~8 个数值在 200 词内）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。建议保留 2-3 个关键数字（binary F1, cross-model F1），其余移入正文。\"}\n  action_items:\n    - {round: 17, action: \"Abstract 精简至 3-4 个关键数字\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论 — 为什么是这 7 个特征\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。缺少 NLL skewness/kurtosis、句法复杂度、Zipf exponent、repetition metrics 等候选讨论。LOFO 是事后验证非先验选择。\"}\n  action_items:\n    - {round: 17, action: \"§3.3 补充特征空间探索说明或承认 hypothesis-driven selection\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B 数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R1 升为 Must-Fix（下降趋势），R2 REBUT 降级 warning（Pythia 族内规模增大 F1 略升，趋势非单调）。共识：缺 >8B 数据是 gap，Limitations 应明确声明规模边界。\"}\n  action_items:\n    - {round: 17, action: \"Limitations 明确 0.6B-8B 规模边界；如可能补充一个 >8B 模型 pilot 结果\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。从 binary detection 到 depth classification 的跳跃缺少动机：为什么 depth 是重要的信息维度？\"}\n  action_items:\n    - {round: 17, action: \"Introduction 补充 depth 的信息价值论证（如 data curation 场景中 depth 如何指导决策）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升为 Must-Fix，R1 REBUT 降级 Should-Fix（training-time vs inference-time 概念区别清晰）。共识：Discussion 需扩展 1-2 段分析 DDR 与 model collapse 的方向一致性原因。\"}\n  action_items:\n    - {round: 17, action: \"Discussion 增加 DDR vs model collapse 的系统性区分段落（inference-time reversible drift vs training-time irreversible collapse）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"'generation depth' vs 'recursive generation depth' 交替使用。'Fingerprinting' 通常指唯一识别而非分类。\"}\n  action_items:\n    - {round: 17, action: \"统一术语；Introduction 中明确定义 fingerprinting 在本文的含义\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M2\"\n  summary: \"Stylometry 引用偏少 + 缺少 detection survey (Tang et al. 2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Stylometry 仅 2 篇经典综述（Stamatatos 2009, Koppel 2009），缺 2015 后更新。Detection survey 可补充 Tang et al. 2024 CACM。\"}\n  action_items:\n    - {round: 17, action: \"补充 stylometry 近年综述 + Tang et al. 2024 detection survey\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Historical resolved issues (unchanged) ===\n\n- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 13\n  resolution: \"TOST demoted from Contribution to supporting analysis. §4.4 moved to Appendix in R13.\"\n  resolution_round: 13\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline + gen-1/gen-2+ topic confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 15\n  resolution: \"Two independent seed controls converge: demeaning F1=0.701, disjoint-seed F1=0.680. Both confirm depth signal is generative degradation, not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 16\n  resolution: \"Cohen's d computed and reported throughout (shape d<0.10, drifting d=0.76-1.17). All qualitative 'comparatively stable' replaced with quantitative 'near-stationary' + effect size numbers. KS omnibus caveat added. Multi-test convergence argument explicit.\"\n  resolution_round: 16\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 14\n  resolution: \"Phenomenon paper positioning. Accepted as Findings-appropriate. R14 fresh reviewers confirm.\"\n  resolution_round: 13\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"LOGO binary F1=0.694 leads in Abstract. Confirmed R14.\"\n  resolution_round: 14\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"Contribution 3 deleted R12. §4.4 moved to Appendix R13.\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Title changed. Discussion explains bottleneck.\"\n  resolution_round: 13\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"Downstream moved to Appendix. Intro reframed to corpus-level flagging. Null result honestly reported in §4.3.\"\n  resolution_round: 15\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 15\n  resolution: \"Temperature data corrected (tc_fix, fixed top_p). Dual-model Pythia+Qwen LOGO numbers in Results/Discussion/Limitations/Appendix. Acknowledged as scope limitation.\"\n  resolution_round: 15\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Title changed. Confirmed R12.\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"§4.1 now explicitly notes Pythia generators share family with reference model, advantage may partly reflect same-family affinity. Cross-ref spread ≤0.013 across 3 families cited as mitigation.\"\n  resolution_round: 16\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms; contribution claims need adjustment\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 15\n  resolution: \"Contributions split: (1) task+DDR=science, (2) 7-feature=efficient implementation. No performance superiority claim. Cost comparison explicit.\"\n  resolution_round: 15\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"§3.4 explains all subsets.\"\n  resolution_round: 13\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Caption states identical configuration. R14 not escalated.\"\n  resolution_round: 13\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification discussion insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Discussion explains gen-1/gen-2+ boundary bottleneck.\"\n  resolution_round: 13\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Restructured to 3 paragraphs R12, compressed R13.\"\n  resolution_round: 12\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Footnote added in §3.3. R14 notes minor residual.\"\n  resolution_round: 13\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification added in method.tex.\"\n  resolution_round: 13\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"6-gen subset note added.\"\n  resolution_round: 13\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"'Six-fold magnitude gap' framing + threshold sensitivity sentence.\"\n  resolution_round: 13\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Switched to PDF.\"\n  resolution_round: 13\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification rewritten.\"\n  resolution_round: 13\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Confirmed correct.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Bonferroni correction scope not specified\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Scope specified in method.tex.\"\n  resolution_round: 13\n\n- id: \"R12-M2\"\n  summary: \"Pythia-1B vs 2.8B crossover undiscussed\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Crossover explanation added.\"\n  resolution_round: 13\n\n- id: \"R12-M3\"\n  summary: \"Generation failure rate causes not reported\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"2746 chain breaks reported.\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Some bib entries missing pages/volume\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Fixed.\"\n  resolution_round: 13\n\n- id: \"R13-SF7\"\n  summary: \"Model scale limited (0.6B-8B), no >10B model\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: R1 升 Must-Fix，R2 部分 REBUT（趋势非单调）。共识：gap 存在但趋势判断有分歧。\"}\n  resolution: \"Acknowledged limitation. Conclusion updated R14. Wont_fix due to compute constraints.\"\n  resolution_round: 14\n\n- id: \"R13-M1\"\n  summary: \"Appendix D 'Notably' AI writing marker\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Deleted and rewritten.\"\n  resolution_round: 13\n\n- id: \"R13-M5\"\n  summary: \"Figure 1 strip plot label area\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Confirmed acceptable.\"\n  resolution_round: 13\n\n- id: \"R13-RV1\"\n  summary: \"Instruct comparison uses different LOGO subsets\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Subset qualifiers added.\"\n  resolution_round: 13\n\n- id: \"R13-RV2\"\n  summary: \"Table 1 vs baselines F1 discrepancy\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Caption explains pooled vs macro-average.\"\n  resolution_round: 13\n\n- id: \"R13-RV3\"\n  summary: \"Instruct experiments missing registry\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Preliminary experiments predating registry.\"\n  resolution_round: 13\n\n- id: \"R14-W1\"\n  summary: \"Feature selection circular reasoning — 'not post-hoc' removed\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Circular claim removed. Feature correlation appendix added. entropy_min justified by four-number NLL summary argument.\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"DDR vs model collapse distinction weak\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Related Work §2.2 now explicitly contrasts DDR (reversible, decomposed) vs model collapse (irreversible, aggregate).\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"Cross-domain evaluation confounded by temperature mismatch\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Acknowledged in Limitations. Not escalated in R15.\"\n  resolution_round: 15\n\n- id: \"R14-W5\"\n  summary: \"Seed-sharing potential topic fingerprint confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Resolved jointly with R7-W1. Two independent seed controls confirm depth signal is not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R14-W6\"\n  summary: \"Missing references — stylometric systems, CORN loss\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"3 citations added. Related Work updated to discuss feature-based detection overlap.\"\n  resolution_round: 14\n\n- id: \"R14-W7\"\n  summary: \"AI writing style traces persist\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Comprehensive -ing cleanup + Conclusion scale correction. R15 confirms clean.\"\n  resolution_round: 14\n\n- id: \"R15-N1\"\n  summary: \"Cross-model chains vs LOGO evaluation protocol incomparability\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Causal claim deleted. Protocol difference acknowledged. 5-gen LOGO average reported as fair reference.\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"Feature redundancy — effective dimensionality ~5\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Effective dimensionality ~5 acknowledged in §4.2. TTR-hapax correlation r=0.97 stated. LOFO marginal gains justify retention.\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"DDR novelty positioning — known drift vs novel decomposition\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Intro explicitly distinguishes known drift (model collapse) vs novel structured decomposition (our contribution).\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"Prompt type limitation not reflected in main results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Prompt-type sensitivity paragraph added to §4.2 Results with all F1 values and LOPTO cross-prompt transfer.\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"KS test cannot verify location/shape decomposition — omnibus test\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§4.2 now states KS is omnibus; location/shape decomposition rests on convergence of Spearman ρ, Levene, CV shift, and Cohen's d, not KS alone.\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"Disjoint-seed experiment lacks bootstrap CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Per-direction bootstrap CIs present in both §4.1 and Appendix. Overall F1=0.680 with directional breakdown.\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"gen-0 3-class F1 still appears prominently without consistent leakage caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 1 header has dagger footnote. Caption explicitly states '3-class F1 may carry upward bias from gen-0 seed sharing; binary F1 is leak-free.'\"\n  resolution_round: 16\n\n- id: \"R16-W3\"\n  summary: \"Table 1 vs Table 2 use different evaluation protocols\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 2 caption explicitly explains protocol difference from Table 1.\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"5 orphan bib entries + 5 bib title/author mismatches\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"5 orphan entries removed. Bib entries verified against published versions.\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"(a) §2.2 front-load training vs inference distinction. (b) Figure 1 |ρ|=0.10 threshold. (c) method.tex which-clause density. (d) B/W hatching. (e) Abstract parameter clarification. (f) Appendix consolidation.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R17 未专门检查这些细项。Figure 1b 字体接近 7pt 下限被两位 Reviewer 提及。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 front-loads training-loop vs inference-chain distinction (done). method.tex which-clause reduction (in progress). Other items low priority.\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# Round 17 (fresh review) — updated by Review Director 2026-05-18\n\n# === Recurring issues (reopened or updated) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"8 pages confirmed R14.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。两位 Reviewer 均 AGREE 为 desk reject 风险。\"}\n  action_items:\n    - {round: 13, action: \"Compress to 8 pages\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 17, action: \"压缩 Discussion/Results 约 0.2 页，确保 Conclusion 在 Page 8 内结束\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness — repurposed binary detectors\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"Detectors not designed for ordinal. Frame as 'repurposed baselines'.\"}\n    - {round: 15, reviewers: \"R1,R2\", note: \"Partial consensus: framework fair, threshold-based binary comparison nice-to-have.\"}\n    - {round: 16, reviewers: \"R1,R2\", note: \"R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled. Partial consensus.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: 两位 Reviewer 均 AGREE。建议在 §4.3 开头明确声明这是 contextualization 而非 methodological superiority claim。\"}\n  action_items:\n    - {round: 14, action: \"Method §3.4 states 'repurposed as depth predictors'\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"§4.3 开头加声明：comparison intended to demonstrate single scores lack ordinal structure, not claim superiority\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction insufficient — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison. Geng et al. 2026 needs verification.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: R2 升为 Must-Fix（增量贡献不充分），R1 REBUT（DDR 特征分解 + LOGO 协议是增量贡献，但 Related Work positioning 需加强）。部分分歧：novelty vs writing issue。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded: detailed 3-way comparison.\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Introduction 中明确列出相对并发工作的 unique contribution（特征层面 DDR 分解 + 跨生成器分类 + confound 控制体系）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"R16 fresh: Intro still opens with instruct-model evidence. Dynamical system framing present but secondary.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: Instruct F1=0.338 vs base 0.763。两位 Reviewer 均 AGREE Introduction 动机（LLM text re-enters web）与方法适用范围（仅 base models）严重脱节。建议重新 frame 为分析性/科学性发现。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"重新 frame 论文贡献为科学发现（understanding distributional drift），弱化 practical detection/curation claims\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === New R17 issues ===\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致 — entropy_std/min 不符合 drifting/stationary 划分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"entropy_std (d=0.55, |ρ|=0.16) 和 entropy_min (pooled |ρ|=0.40) 不符合二分框架。7 特征中 28.6% 例外。两位 Reviewer 均 AGREE，建议三分法（drifting/intermediate/stationary）。\"}\n  action_items:\n    - {round: 17, action: \"将 DDR 特征分为三类（drifting/intermediate/stationary），修改 Abstract/Intro/Results 叙事\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高（~8 个数值在 200 词内）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。建议保留 2-3 个关键数字（binary F1, cross-model F1），其余移入正文。\"}\n  action_items:\n    - {round: 17, action: \"Abstract 精简至 3-4 个关键数字\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论 — 为什么是这 7 个特征\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。缺少 NLL skewness/kurtosis、句法复杂度、Zipf exponent、repetition metrics 等候选讨论。LOFO 是事后验证非先验选择。\"}\n  action_items:\n    - {round: 17, action: \"§3.3 补充特征空间探索说明或承认 hypothesis-driven selection\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B 数据点\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R1 升为 Must-Fix（下降趋势），R2 REBUT 降级 warning（Pythia 族内规模增大 F1 略升，趋势非单调）。共识：缺 >8B 数据是 gap，Limitations 应明确声明规模边界。\"}\n  action_items:\n    - {round: 17, action: \"Limitations 明确 0.6B-8B 规模边界；如可能补充一个 >8B 模型 pilot 结果\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。从 binary detection 到 depth classification 的跳跃缺少动机：为什么 depth 是重要的信息维度？\"}\n  action_items:\n    - {round: 17, action: \"Introduction 补充 depth 的信息价值论证（如 data curation 场景中 depth 如何指导决策）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升为 Must-Fix，R1 REBUT 降级 Should-Fix（training-time vs inference-time 概念区别清晰）。共识：Discussion 需扩展 1-2 段分析 DDR 与 model collapse 的方向一致性原因。\"}\n  action_items:\n    - {round: 17, action: \"Discussion 增加 DDR vs model collapse 的系统性区分段落（inference-time reversible drift vs training-time irreversible collapse）\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"'generation depth' vs 'recursive generation depth' 交替使用。'Fingerprinting' 通常指唯一识别而非分类。\"}\n  action_items:\n    - {round: 17, action: \"统一术语；Introduction 中明确定义 fingerprinting 在本文的含义\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M2\"\n  summary: \"Stylometry 引用偏少 + 缺少 detection survey (Tang et al. 2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Stylometry 仅 2 篇经典综述（Stamatatos 2009, Koppel 2009），缺 2015 后更新。Detection survey 可补充 Tang et al. 2024 CACM。\"}\n  action_items:\n    - {round: 17, action: \"补充 stylometry 近年综述 + Tang et al. 2024 detection survey\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Historical resolved issues (unchanged) ===\n\n- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 13\n  resolution: \"TOST demoted from Contribution to supporting analysis. §4.4 moved to Appendix in R13.\"\n  resolution_round: 13\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline + gen-1/gen-2+ topic confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 15\n  resolution: \"Two independent seed controls converge: demeaning F1=0.701, disjoint-seed F1=0.680. Both confirm depth signal is generative degradation, not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 16\n  resolution: \"Cohen's d computed and reported throughout (shape d<0.10, drifting d=0.76-1.17). All qualitative 'comparatively stable' replaced with quantitative 'near-stationary' + effect size numbers. KS omnibus caveat added. Multi-test convergence argument explicit.\"\n  resolution_round: 16\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 14\n  resolution: \"Phenomenon paper positioning. Accepted as Findings-appropriate. R14 fresh reviewers confirm.\"\n  resolution_round: 13\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"LOGO binary F1=0.694 leads in Abstract. Confirmed R14.\"\n  resolution_round: 14\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"Contribution 3 deleted R12. §4.4 moved to Appendix R13.\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Title changed. Discussion explains bottleneck.\"\n  resolution_round: 13\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"Downstream moved to Appendix. Intro reframed to corpus-level flagging. Null result honestly reported in §4.3.\"\n  resolution_round: 15\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 15\n  resolution: \"Temperature data corrected (tc_fix, fixed top_p). Dual-model Pythia+Qwen LOGO numbers in Results/Discussion/Limitations/Appendix. Acknowledged as scope limitation.\"\n  resolution_round: 15\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Title changed. Confirmed R12.\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"§4.1 now explicitly notes Pythia generators share family with reference model, advantage may partly reflect same-family affinity. Cross-ref spread ≤0.013 across 3 families cited as mitigation.\"\n  resolution_round: 16\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms; contribution claims need adjustment\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 15\n  resolution: \"Contributions split: (1) task+DDR=science, (2) 7-feature=efficient implementation. No performance superiority claim. Cost comparison explicit.\"\n  resolution_round: 15\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"§3.4 explains all subsets.\"\n  resolution_round: 13\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Caption states identical configuration. R14 not escalated.\"\n  resolution_round: 13\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification discussion insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Discussion explains gen-1/gen-2+ boundary bottleneck.\"\n  resolution_round: 13\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Restructured to 3 paragraphs R12, compressed R13.\"\n  resolution_round: 12\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Footnote added in §3.3. R14 notes minor residual.\"\n  resolution_round: 13\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification added in method.tex.\"\n  resolution_round: 13\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"6-gen subset note added.\"\n  resolution_round: 13\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"'Six-fold magnitude gap' framing + threshold sensitivity sentence.\"\n  resolution_round: 13\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Switched to PDF.\"\n  resolution_round: 13\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification rewritten.\"\n  resolution_round: 13\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Confirmed correct.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Bonferroni correction scope not specified\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Scope specified in method.tex.\"\n  resolution_round: 13\n\n- id: \"R12-M2\"\n  summary: \"Pythia-1B vs 2.8B crossover undiscussed\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Crossover explanation added.\"\n  resolution_round: 13\n\n- id: \"R12-M3\"\n  summary: \"Generation failure rate causes not reported\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"2746 chain breaks reported.\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Some bib entries missing pages/volume\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Fixed.\"\n  resolution_round: 13\n\n- id: \"R13-SF7\"\n  summary: \"Model scale limited (0.6B-8B), no >10B model\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: R1 升 Must-Fix，R2 部分 REBUT（趋势非单调）。共识：gap 存在但趋势判断有分歧。\"}\n  resolution: \"Acknowledged limitation. Conclusion updated R14. Wont_fix due to compute constraints.\"\n  resolution_round: 14\n\n- id: \"R13-M1\"\n  summary: \"Appendix D 'Notably' AI writing marker\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Deleted and rewritten.\"\n  resolution_round: 13\n\n- id: \"R13-M5\"\n  summary: \"Figure 1 strip plot label area\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Confirmed acceptable.\"\n  resolution_round: 13\n\n- id: \"R13-RV1\"\n  summary: \"Instruct comparison uses different LOGO subsets\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Subset qualifiers added.\"\n  resolution_round: 13\n\n- id: \"R13-RV2\"\n  summary: \"Table 1 vs baselines F1 discrepancy\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Caption explains pooled vs macro-average.\"\n  resolution_round: 13\n\n- id: \"R13-RV3\"\n  summary: \"Instruct experiments missing registry\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Preliminary experiments predating registry.\"\n  resolution_round: 13\n\n- id: \"R14-W1\"\n  summary: \"Feature selection circular reasoning — 'not post-hoc' removed\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Circular claim removed. Feature correlation appendix added. entropy_min justified by four-number NLL summary argument.\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"DDR vs model collapse distinction weak\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Related Work §2.2 now explicitly contrasts DDR (reversible, decomposed) vs model collapse (irreversible, aggregate).\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"Cross-domain evaluation confounded by temperature mismatch\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Acknowledged in Limitations. Not escalated in R15.\"\n  resolution_round: 15\n\n- id: \"R14-W5\"\n  summary: \"Seed-sharing potential topic fingerprint confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Resolved jointly with R7-W1. Two independent seed controls confirm depth signal is not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R14-W6\"\n  summary: \"Missing references — stylometric systems, CORN loss\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"3 citations added. Related Work updated to discuss feature-based detection overlap.\"\n  resolution_round: 14\n\n- id: \"R14-W7\"\n  summary: \"AI writing style traces persist\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Comprehensive -ing cleanup + Conclusion scale correction. R15 confirms clean.\"\n  resolution_round: 14\n\n- id: \"R15-N1\"\n  summary: \"Cross-model chains vs LOGO evaluation protocol incomparability\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Causal claim deleted. Protocol difference acknowledged. 5-gen LOGO average reported as fair reference.\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"Feature redundancy — effective dimensionality ~5\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Effective dimensionality ~5 acknowledged in §4.2. TTR-hapax correlation r=0.97 stated. LOFO marginal gains justify retention.\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"DDR novelty positioning — known drift vs novel decomposition\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Intro explicitly distinguishes known drift (model collapse) vs novel structured decomposition (our contribution).\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"Prompt type limitation not reflected in main results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Prompt-type sensitivity paragraph added to §4.2 Results with all F1 values and LOPTO cross-prompt transfer.\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"KS test cannot verify location/shape decomposition — omnibus test\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§4.2 now states KS is omnibus; location/shape decomposition rests on convergence of Spearman ρ, Levene, CV shift, and Cohen's d, not KS alone.\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"Disjoint-seed experiment lacks bootstrap CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Per-direction bootstrap CIs present in both §4.1 and Appendix. Overall F1=0.680 with directional breakdown.\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"gen-0 3-class F1 still appears prominently without consistent leakage caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 1 header has dagger footnote. Caption explicitly states '3-class F1 may carry upward bias from gen-0 seed sharing; binary F1 is leak-free.'\"\n  resolution_round: 16\n\n- id: \"R16-W3\"\n  summary: \"Table 1 vs Table 2 use different evaluation protocols\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 2 caption explicitly explains protocol difference from Table 1.\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"5 orphan bib entries + 5 bib title/author mismatches\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"5 orphan entries removed. Bib entries verified against published versions.\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"(a) §2.2 front-load training vs inference distinction. (b) Figure 1 |ρ|=0.10 threshold. (c) method.tex which-clause density. (d) B/W hatching. (e) Abstract parameter clarification. (f) Appendix consolidation.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R17 未专门检查这些细项。Figure 1b 字体接近 7pt 下限被两位 Reviewer 提及。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 front-loads training-loop vs inference-chain distinction (done). method.tex which-clause reduction (in progress). Other items low priority.\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-18T09:23:17.672886+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 25412}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-18T09:25:15.052845+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n**截止日期**: 2026-05-25 (AoE)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+相关工作）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务，将传统 binary（human vs. AI）检测扩展为三类分类（gen-0/gen-1/gen-2+），并发现 differential depth response (DDR)：递归生成中，central-tendency 特征（entropy mean, TTR, hapax ratio）随深度单调漂移，而 shape 特征（entropy max, tail decay）保持近似静态。基于 7 个特征 + XGBoost 分类器，在 8 个 base model generator (0.6B-8B) 的 LOGO 评估下达到 leak-free binary F1=0.694。实验设计全面，包含 seed sharing 控制、cross-model chains、temperature/prompt-type sensitivity 分析等。\n\n---\n\n## Strengths\n\n1. **新颖的任务定义**: 从 binary detection 扩展到 ordinal depth classification 是概念上有意义的贡献，与 model collapse 和 data provenance 文献有清晰连接。[R1, R2 AGREE]\n\n2. **系统化的 confound 控制**: Seed demeaning + independent-seed 实验排除 topic fingerprint（§4.1）、length-matched subsampling 排除长度混淆（Appendix B）、cross-domain/temperature/prompt-type robustness 分析。这种系统性在 AI-text detection 文献中较为少见。[R1, R2 AGREE]\n\n3. **DDR 分解的分析价值**: 将特征分为 drifting 和 stationary 两类，提供了理解递归生成统计特性的有用分析框架。Cohen's d、Spearman ρ、Levene test、CV shift 多维度验证。[R1, R2 AGREE]\n\n4. **诚实的局限性报告**: Instruction tuning 信号崩溃、模型规模限制、温度敏感性等负面结果均如实报告，未掩盖核心弱点。[R1]\n\n5. **写作质量良好**: AI 写作痕迹极少（0 em-dash, 0 黑名单词汇）。引用完整（59 篇，0 orphan，0 missing）。[R2]\n\n6. **计算效率优势**: 单个 410M 参考模型 + 7 特征 + XGBoost = 9.7 ms/text，相比 multi-detector ensemble (22.8 ms) 成本优势显著。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, CONSENSUS] **正文页数超限（~8.12 页 vs. 8 页限制）**\n- PDF 编译核实：Conclusion 结束于 Page 9 约 12%，Limitations 从此处开始。主体内容（Sections 1-6）约 8.12 页。\n- ARR CFP: \"Submissions that exceed the length requirements will be desk rejected.\"\n- 两位 Reviewer 均 AGREE 这是 desk reject 风险。\n- **Action**: 压缩 Discussion (当前约 1.5 栏) 和 Results 中部分冗余分析，确保 Conclusion 在 Page 8 内结束。\n\n**MF2** [critical, CONSENSUS] **DDR 二分框架内部不一致**\n- entropy_std (d=0.55, |ρ|=0.16) 和 entropy_min (pooled |ρ|=0.40) 不符合 drifting/stationary 二分框架。7 个特征中 28.6% 需要\"qualification\"（§4.2 原文承认）。\n- 两位 Reviewer 均 AGREE：建议改为三分法（drifting/intermediate/stationary），这比强行塞入二分框架更诚实，且 intermediate 类本身是有趣的发现。\n- **Action**: 修改 DDR 叙事为三分类；Abstract/Intro/Results 同步更新。\n\n**MF3** [critical, CONSENSUS] **Instruction tuning 信号崩溃 + 论文 framing 脱节**\n- OLMo-2-1B-Instruct LOGO F1=0.338 vs. base 0.763（Limitations, Page 9）。\n- Introduction 以\"LLM text re-enters the web\"为动机，暗示实际检测应用；但方法仅适用于 base model 输出，在当前 LLM 生态中极为少见。\n- 两位 Reviewer 均 AGREE：动机与适用范围严重脱节。\n- **Action**: 重新 frame 论文贡献为分析性/科学性发现（understanding distributional drift under recursive generation），弱化 practical detection/curation claims。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, DIVERGENT] **与并发工作（Broken Telephone, Markovian Chains）增量贡献区分不充分**\n- R2 升为 Must-Fix：DDR 的 drifting features 与 Broken Telephone 的信息失真高度重叠；DDR 可能只是 Markovian Chains 理论预测的实证验证。\n- R1 REBUT：DDR 提供特征层面的操作化分解 + LOGO 跨生成器分类 + 全面 confound 控制，这些是 task-oriented 贡献。但同意 Related Work positioning 论证不够清晰。\n- **共识方向**: novelty 存在但 positioning 不足。§2.2 和 Introduction 需明确列出 unique contributions。\n\n**SF2** [warning, DIVERGENT] **DDR vs model collapse 因果区分不足**\n- R2 升为 Must-Fix：DDR 是否只是 model collapse 在 inference-time 的微观表现？\n- R1 REBUT 降级 Should-Fix：training-time vs inference-time 概念区别清晰；但同意 Discussion 需扩展论证。\n- **共识方向**: Discussion 增加 1-2 段系统性分析。\n\n**SF3** [warning, CONSENSUS] **Baseline 比较方法论不够公平**\n- 将 binary detection 方法的分数 repurposed 为 ordinal depth predictors，与专门设计的 7 特征比较不是 apples-to-apples。\n- §4.3 的 \"contextualize\" framing 部分缓解，但 Table 2 的并排呈现暗示竞争性对比。\n- **Action**: §4.3 开头明确声明比较意图。\n\n**SF4** [warning, CONSENSUS] **Abstract 数据密度过高**\n- ~200 词内 8+ 个具体数值，削弱叙事力。\n- **Action**: 精简至 3-4 个关键数字。\n\n**SF5** [warning, CONSENSUS] **Feature selection 缺少系统化方法论**\n- 未讨论为什么选这 7 个特征而非 NLL skewness/kurtosis、句法复杂度、repetition metrics 等。LOFO 是事后验证。\n- **Action**: §3.3 补充特征空间探索说明。\n\n**SF6** [warning, DIVERGENT] **模型规模覆盖不足（0.6B-8B）**\n- R1 升为 Must-Fix（Table 1 显示下降趋势）。R2 部分 REBUT：Pythia 族内规模增大 F1 略升，趋势非单调，更可能是架构差异而非规模衰减。\n- **共识**: 缺少 >8B 数据点是 gap。Limitations 应明确声明规模边界。\n\n**SF7** [warning, CONSENSUS] **Introduction 缺少\"why depth matters\"的中间论证**\n- 从 binary detection 到 depth classification 的跳跃缺少动机论证。\n- **Action**: 补充 depth 的信息价值说明。\n\n### Nice-to-Have\n\n1. DDR 阈值（|ρ|=0.10, d=0.10）在正文中引用 Cohen's benchmarks + 概括 Appendix L 的 equivalence test 结果 [R1 提出, R2 部分 REBUT: Appendix L 已有 Lakens 2017]\n2. 术语统一：\"generation depth\" vs \"recursive generation depth\"；Introduction 明确定义 \"fingerprinting\" 含义 [R1, R2]\n3. Table 1 中 \"---\" 改为 \"—\" 或 \"N/A\" [R2]\n4. Bib entry author 格式统一（self_consuming_mad, qwen3, llama3）[R1, R2]\n5. Stylometry 引用补充 2015 后综述 + Tang et al. 2024 CACM detection survey [R1, R2]\n6. Responsible NLP Checklist 确认包含在提交材料中 [R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n| # | 问题 | 严重性 |\n|---|------|--------|\n| MF1 | 正文超 8 页限制 | critical |\n| MF2 | DDR 二分框架不一致 | critical |\n| MF3 | Instruct 信号崩溃 + framing 脱节 | critical |\n| SF3 | Baseline 比较不公平 | warning |\n| SF4 | Abstract 数据密度 | warning |\n| SF5 | Feature selection 方法论 | warning |\n| SF7 | Introduction 动机不足 | warning |\n\n## Reviewer Divergence\n\n| # | 问题 | R1 | R2 | 分歧实质 |\n|---|------|-----|-----|----------|\n| SF1 | 并发工作增量 | Should-Fix (writing issue) | Must-Fix (novelty concern) | R1 认为 DDR 特征分解 + LOGO 是增量贡献，R2 认为增量不充分 |\n| SF2 | DDR vs model collapse | Should-Fix | Must-Fix | R1 认为概念区别清晰，R2 认为因果关系需论证 |\n| SF6 | 模型规模 >8B | Must-Fix (下降趋势) | Warning (趋势非单调) | 数据解读不同：R1 看整体趋势，R2 看族内趋势 |\n\n---\n\n## Questions for Authors\n\n1. 是否有任何 >8B base model 的实验数据（即使是 pilot）？\n2. Instruction tuning 信号崩溃的根本原因：是消除了 depth-dependent NLL 结构，还是引入了更强的 prompt-dependent 变异？\n3. entropy_std 为什么有高 Cohen's d (0.55) 但低 Spearman ρ (0.16)？是否存在非单调关系？\n4. 如果将论文重新定位为 phenomenon paper，core contribution 是否应仅聚焦 DDR 发现而非 classification pipeline？\n5. DDR 的 stationary component 在 model collapse 文献中是否有对应物？\n\n---\n\n## Missing References\n\n1. **Tang et al., 2024** \"The Science of Detecting LLM-Generated Text\" (CACM) — detection 综合综述\n2. **Neal et al., 2017** \"Surveying Stylometry Techniques and Applications\" — 补充 stylometry 近年综述\n3. **Kirchenbauer et al., 2024** (ICLR) — watermarking depth-robustness（如与已引用 2023 ICML 版本不同）\n4. Stylometry 方向仅引 Stamatatos (2009) 和 Koppel (2009)，缺 2015 后更新\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.0 | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 2.5 | 3.0 |\n\n**评分理由**:\n\n本文的核心贡献——generation depth classification 任务定义 + DDR 现象发现——对 AI-text detection 和 model collapse 社区有科学参考价值。实验设计全面，confound 控制系统化，统计方法论整体规范，写作质量良好。\n\n阻止达到 Conference (4.0) 的主要因素：\n1. **适用范围根本性受限**：仅 base models (0.6B-8B)，instruction tuning 下信号近乎崩溃（F1: 0.763→0.338），几乎无实际部署场景\n2. **DDR 框架内部不一致**：28.6% 特征不符合二分框架，核心叙事需修正\n3. **与并发工作的增量论证不足**：Broken Telephone 和 Markovian Chains 覆盖了相邻的研究空间，论文的 unique positioning 需更有力论证\n4. **页数超限**：~8.12 页，存在 desk reject 风险\n\n论文适合 Findings track：提供了有意义的实证发现和分析框架，尽管实际影响力受限。若能修复页数问题、将 DDR 改为三分类、重新 frame 为科学发现、加强与并发工作的区分论证，有潜力稳固在 Findings (3.0) 水平。\n\n**Confidence: 4/5**（两位 Reviewer 均熟悉 AI-text detection、model collapse、统计分析方法）\n\n---\n\n## Detailed Comments (by Section)\n\n### Abstract\n- 数据密度过高（8+ 数字/200 词），建议精简至 binary F1 + cross-model F1 + Cohen's d 范围\n- \"shape features remain near-stationary\" 需改为三分类表述\n\n### Introduction (§1)\n- 开头动机（\"LLM text re-enters web\"）与方法适用范围（仅 base models）脱节，需重新 frame\n- 缺少\"为什么 depth 比 binary 更重要\"的中间论证\n- Contribution 列表清晰，但应删除或弱化 practical implication 相关表述\n\n### Related Work (§2)\n- 与 Broken Telephone / Markovian Chains 的区分需扩展为完整段落，明确列出 3 个 unique contributions\n- Stylometry 引用仅 2 篇经典综述（2009），需补充近年更新\n- 引用密度整体合理（59 篇），0 orphan / 0 missing\n\n### Method (§3)\n- Feature selection 缺少系统化方法论说明（为什么这 7 个而非其他候选）\n- \"entropy_min\" 首次出现时应明确定义\n- 其他方面（task formulation, generation chain construction, evaluation protocol）清晰完整\n\n### Results (§4)\n- DDR 描述需从二分改为三分（drifting/intermediate/stationary）\n- Table 1 的 3-class F1 caveat 已到位（dagger footnote），但 Abstract 和 §4.1 第一段仍突出 3-class 数字\n- Baseline 比较 (§4.3) 需明确声明 contextualization 意图\n- 统计方法整体规范（Bootstrap CI, Bonferroni, McNemar, Cohen's d）\n\n### Discussion (§5)\n- 需增加 DDR vs model collapse 的系统性区分段落\n- 温度敏感性讨论可更突出（当前主要在 Appendix）\n- 需压缩以解决页数超限\n\n### Conclusion (§6)\n- 需压缩以确保在 Page 8 内结束\n\n### Limitations\n- 内容充实且诚实，覆盖了核心弱点\n- instruct model 结果如重新 frame 为科学发现，此处的讨论需相应调整\n\n### Ethics Statement\n- 覆盖充分（许可证、计算预算、软件版本）\n\n### Appendix\n- 15 个 appendix 数量偏多，建议合并相关分析（如 temperature sensitivity + cross-temp transfer）\n- 关键结果（如 equivalence test, Appendix L）可在正文中一句话概括",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\"\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n**截止日期**: 2026-05-25 (AoE)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+相关工作）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务，将传统 binary（human vs. AI）检测扩展为三类分类（gen-0/gen-1/gen-2+），并发现 differential depth response (DDR)：递归生成中，central-tendency 特征（entropy mean, TTR, hapax ratio）随深度单调漂移，而 shape 特征（entropy max, tail decay）保持近似静态。基于 7 个特征 + XGBoost 分类器，在 8 个 base model generator (0.6B-8B) 的 LOGO 评估下达到 leak-free binary F1=0.694。实验设计全面，包含 seed sharing 控制、cross-model chains、temperature/prompt-type sensitivity 分析等。\n\n---\n\n## Strengths\n\n1. **新颖的任务定义**: 从 binary detection 扩展到 ordinal depth classification 是概念上有意义的贡献，与 model collapse 和 data provenance 文献有清晰连接。[R1, R2 AGREE]\n\n2. **系统化的 confound 控制**: Seed demeaning + independent-seed 实验排除 topic fingerprint（§4.1）、length-matched subsampling 排除长度混淆（Appendix B）、cross-domain/temperature/prompt-type robustness 分析。这种系统性在 AI-text detection 文献中较为少见。[R1, R2 AGREE]\n\n3. **DDR 分解的分析价值**: 将特征分为 drifting 和 stationary 两类，提供了理解递归生成统计特性的有用分析框架。Cohen's d、Spearman ρ、Levene test、CV shift 多维度验证。[R1, R2 AGREE]\n\n4. **诚实的局限性报告**: Instruction tuning 信号崩溃、模型规模限制、温度敏感性等负面结果均如实报告，未掩盖核心弱点。[R1]\n\n5. **写作质量良好**: AI 写作痕迹极少（0 em-dash, 0 黑名单词汇）。引用完整（59 篇，0 orphan，0 missing）。[R2]\n\n6. **计算效率优势**: 单个 410M 参考模型 + 7 特征 + XGBoost = 9.7 ms/text，相比 multi-detector ensemble (22.8 ms) 成本优势显著。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, CONSENSUS] **正文页数超限（~8.12 页 vs. 8 页限制）**\n- PDF 编译核实：Conclusion 结束于 Page 9 约 12%，Limitations 从此处开始。主体内容（Sections 1-6）约 8.12 页。\n- ARR CFP: \"Submissions that exceed the length requirements will be desk rejected.\"\n- 两位 Reviewer 均 AGREE 这是 desk reject 风险。\n- **Action**: 压缩 Discussion (当前约 1.5 栏) 和 Results 中部分冗余分析，确保 Conclusion 在 Page 8 内结束。\n\n**MF2** [critical, CONSENSUS] **DDR 二分框架内部不一致**\n- entropy_std (d=0.55, |ρ|=0.16) 和 entropy_min (pooled |ρ|=0.40) 不符合 drifting/stationary 二分框架。7 个特征中 28.6% 需要\"qualification\"（§4.2 原文承认）。\n- 两位 Reviewer 均 AGREE：建议改为三分法（drifting/intermediate/stationary），这比强行塞入二分框架更诚实，且 intermediate 类本身是有趣的发现。\n- **Action**: 修改 DDR 叙事为三分类；Abstract/Intro/Results 同步更新。\n\n**MF3** [critical, CONSENSUS] **Instruction tuning 信号崩溃 + 论文 framing 脱节**\n- OLMo-2-1B-Instruct LOGO F1=0.338 vs. base 0.763（Limitations, Page 9）。\n- Introduction 以\"LLM text re-enters the web\"为动机，暗示实际检测应用；但方法仅适用于 base model 输出，在当前 LLM 生态中极为少见。\n- 两位 Reviewer 均 AGREE：动机与适用范围严重脱节。\n- **Action**: 重新 frame 论文贡献为分析性/科学性发现（understanding distributional drift under recursive generation），弱化 practical detection/curation claims。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, DIVERGENT] **与并发工作（Broken Telephone, Markovian Chains）增量贡献区分不充分**\n- R2 升为 Must-Fix：DDR 的 drifting features 与 Broken Telephone 的信息失真高度重叠；DDR 可能只是 Markovian Chains 理论预测的实证验证。\n- R1 REBUT：DDR 提供特征层面的操作化分解 + LOGO 跨生成器分类 + 全面 confound 控制，这些是 task-oriented 贡献。但同意 Related Work positioning 论证不够清晰。\n- **共识方向**: novelty 存在但 positioning 不足。§2.2 和 Introduction 需明确列出 unique contributions。\n\n**SF2** [warning, DIVERGENT] **DDR vs model collapse 因果区分不足**\n- R2 升为 Must-Fix：DDR 是否只是 model collapse 在 inference-time 的微观表现？\n- R1 REBUT 降级 Should-Fix：training-time vs inference-time 概念区别清晰；但同意 Discussion 需扩展论证。\n- **共识方向**: Discussion 增加 1-2 段系统性分析。\n\n**SF3** [warning, CONSENSUS] **Baseline 比较方法论不够公平**\n- 将 binary detection 方法的分数 repurposed 为 ordinal depth predictors，与专门设计的 7 特征比较不是 apples-to-apples。\n- §4.3 的 \"contextualize\" framing 部分缓解，但 Table 2 的并排呈现暗示竞争性对比。\n- **Action**: §4.3 开头明确声明比较意图。\n\n**SF4** [warning, CONSENSUS] **Abstract 数据密度过高**\n- ~200 词内 8+ 个具体数值，削弱叙事力。\n- **Action**: 精简至 3-4 个关键数字。\n\n**SF5** [warning, CONSENSUS] **Feature selection 缺少系统化方法论**\n- 未讨论为什么选这 7 个特征而非 NLL skewness/kurtosis、句法复杂度、repetition metrics 等。LOFO 是事后验证。\n- **Action**: §3.3 补充特征空间探索说明。\n\n**SF6** [warning, DIVERGENT] **模型规模覆盖不足（0.6B-8B）**\n- R1 升为 Must-Fix（Table 1 显示下降趋势）。R2 部分 REBUT：Pythia 族内规模增大 F1 略升，趋势非单调，更可能是架构差异而非规模衰减。\n- **共识**: 缺少 >8B 数据点是 gap。Limitations 应明确声明规模边界。\n\n**SF7** [warning, CONSENSUS] **Introduction 缺少\"why depth matters\"的中间论证**\n- 从 binary detection 到 depth classification 的跳跃缺少动机论证。\n- **Action**: 补充 depth 的信息价值说明。\n\n### Nice-to-Have\n\n1. DDR 阈值（|ρ|=0.10, d=0.10）在正文中引用 Cohen's benchmarks + 概括 Appendix L 的 equivalence test 结果 [R1 提出, R2 部分 REBUT: Appendix L 已有 Lakens 2017]\n2. 术语统一：\"generation depth\" vs \"recursive generation depth\"；Introduction 明确定义 \"fingerprinting\" 含义 [R1, R2]\n3. Table 1 中 \"---\" 改为 \"—\" 或 \"N/A\" [R2]\n4. Bib entry author 格式统一（self_consuming_mad, qwen3, llama3）[R1, R2]\n5. Stylometry 引用补充 2015 后综述 + Tang et al. 2024 CACM detection survey [R1, R2]\n6. Responsible NLP Checklist 确认包含在提交材料中 [R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n| # | 问题 | 严重性 |\n|---|------|--------|\n| MF1 | 正文超 8 页限制 | critical |\n| MF2 | DDR 二分框架不一致 | critical |\n| MF3 | Instruct 信号崩溃 + framing 脱节 | critical |\n| SF3 | Baseline 比较不公平 | warning |\n| SF4 | Abstract 数据密度 | warning |\n| SF5 | Feature selection 方法论 | warning |\n| SF7 | Introduction 动机不足 | warning |\n\n## Reviewer Divergence\n\n| # | 问题 | R1 | R2 | 分歧实质 |\n|---|------|-----|-----|----------|\n| SF1 | 并发工作增量 | Should-Fix (writing issue) | Must-Fix (novelty concern) | R1 认为 DDR 特征分解 + LOGO 是增量贡献，R2 认为增量不充分 |\n| SF2 | DDR vs model collapse | Should-Fix | Must-Fix | R1 认为概念区别清晰，R2 认为因果关系需论证 |\n| SF6 | 模型规模 >8B | Must-Fix (下降趋势) | Warning (趋势非单调) | 数据解读不同：R1 看整体趋势，R2 看族内趋势 |\n\n---\n\n## Questions for Authors\n\n1. 是否有任何 >8B base model 的实验数据（即使是 pilot）？\n2. Instruction tuning 信号崩溃的根本原因：是消除了 depth-dependent NLL 结构，还是引入了更强的 prompt-dependent 变异？\n3. entropy_std 为什么有高 Cohen's d (0.55) 但低 Spearman ρ (0.16)？是否存在非单调关系？\n4. 如果将论文重新定位为 phenomenon paper，core contribution 是否应仅聚焦 DDR 发现而非 classification pipeline？\n5. DDR 的 stationary component 在 model collapse 文献中是否有对应物？\n\n---\n\n## Missing References\n\n1. **Tang et al., 2024** \"The Science of Detecting LLM-Generated Text\" (CACM) — detection 综合综述\n2. **Neal et al., 2017** \"Surveying Stylometry Techniques and Applications\" — 补充 stylometry 近年综述\n3. **Kirchenbauer et al., 2024** (ICLR) — watermarking depth-robustness（如与已引用 2023 ICML 版本不同）\n4. Stylometry 方向仅引 Stamatatos (2009) 和 Koppel (2009)，缺 2015 后更新\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.0 | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 2.5 | 3.0 |\n\n**评分理由**:\n\n本文的核心贡献——generation depth classification 任务定义 + DDR 现象发现——对 AI-text detection 和 model collapse 社区有科学参考价值。实验设计全面，confound 控制系统化，统计方法论整体规范，写作质量良好。\n\n阻止达到 Conference (4.0) 的主要因素：\n1. **适用范围根本性受限**：仅 base models (0.6B-8B)，instruction tuning 下信号近乎崩溃（F1: 0.763→0.338），几乎无实际部署场景\n2. **DDR 框架内部不一致**：28.6% 特征不符合二分框架，核心叙事需修正\n3. **与并发工作的增量论证不足**：Broken Telephone 和 Markovian Chains 覆盖了相邻的研究空间，论文的 unique positioning 需更有力论证\n4. **页数超限**：~8.12 页，存在 desk reject 风险\n\n论文适合 Findings track：提供了有意义的实证发现和分析框架，尽管实际影响力受限。若能修复页数问题、将 DDR 改为三分类、重新 frame 为科学发现、加强与并发工作的区分论证，有潜力稳固在 Findings (3.0) 水平。\n\n**Confidence: 4/5**（两位 Reviewer 均熟悉 AI-text detection、model collapse、统计分析方法）\n\n---\n\n## Detailed Comments (by Section)\n\n### Abstract\n- 数据密度过高（8+ 数字/200 词），建议精简至 binary F1 + cross-model F1 + Cohen's d 范围\n- \"shape features remain near-stationary\" 需改为三分类表述\n\n### Introduction (§1)\n- 开头动机（\"LLM text re-enters web\"）与方法适用范围（仅 base models）脱节，需重新 frame\n- 缺少\"为什么 depth 比 binary 更重要\"的中间论证\n- Contribution 列表清晰，但应删除或弱化 practical implication 相关表述\n\n### Related Work (§2)\n- 与 Broken Telephone / Markovian Chains 的区分需扩展为完整段落，明确列出 3 个 unique contributions\n- Stylometry 引用仅 2 篇经典综述（2009），需补充近年更新\n- 引用密度整体合理（59 篇），0 orphan / 0 missing\n\n### Method (§3)\n- Feature selection 缺少系统化方法论说明（为什么这 7 个而非其他候选）\n- \"entropy_min\" 首次出现时应明确定义\n- 其他方面（task formulation, generation chain construction, evaluation protocol）清晰完整\n\n### Results (§4)\n- DDR 描述需从二分改为三分（drifting/intermediate/stationary）\n- Table 1 的 3-class F1 caveat 已到位（dagger footnote），但 Abstract 和 §4.1 第一段仍突出 3-class 数字\n- Baseline 比较 (§4.3) 需明确声明 contextualization 意图\n- 统计方法整体规范（Bootstrap CI, Bonferroni, McNemar, Cohen's d）\n\n### Discussion (§5)\n- 需增加 DDR vs model collapse 的系统性区分段落\n- 温度敏感性讨论可更突出（当前主要在 Appendix）\n- 需压缩以解决页数超限\n\n### Conclusion (§6)\n- 需压缩以确保在 Page 8 内结束\n\n### Limitations\n- 内容充实且诚实，覆盖了核心弱点\n- instruct model 结果如重新 frame 为科学发现，此处的讨论需相应调整\n\n### Ethics Statement\n- 覆盖充分（许可证、计算预算、软件版本）\n\n### Appendix\n- 15 个 appendix 数量偏多，建议合并相关分析（如 temperature sensitivity + cross-temp transfer）\n- 关键结果（如 equivalence test, Appendix L）可在正文中一句话概括",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-18T09:25:19.118890+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1054 · 2026-05-18T09:25:31.903367+00:00_

审稿报告已投递至 Research Director。

---

**Round 17 审稿完成汇报**

**Overall Score: 3.0 (Findings)**（R1: 3.0, R2: 2.5）

**3 个 Must-Fix（共识）**：
1. **正文超 8 页限制**（~8.12 页）— desk reject 风险，需压缩 Discussion/Results
2. **DDR 二分框架内部不一致** — entropy_std/min 不符合二分划分（28.6% 例外），需改为三分法
3. **Instruct 信号崩溃 + framing 脱节** — F1: 0.763→0.338，Introduction 动机与适用范围脱节，需重新 frame 为科学发现

**7 个 Should-Fix**：并发工作增量论证不足、DDR vs model collapse 区分、baseline 比较公平性、Abstract 数据密度、feature selection 方法论、模型规模覆盖、Introduction 动机缺失

**主要分歧**：R1 认为 DDR 特征分解 + LOGO 协议构成充分增量贡献（3.0），R2 认为与 Broken Telephone/Markovian Chains 重叠严重 + 页数风险应降分（2.5）。综合评定 3.0，适合 Findings track。

Issue Tracker 已同步更新（12 个活跃 issue：3 critical + 6 warning + 3 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1055 · 2026-05-18T09:25:34.668141+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

**回应要点总结**：

- **5 项 AGREE**（N1 DDR 框架缺陷、N2 instruct 信号崩溃、W1 baseline 不公平、W4 gen-0 膨胀、W5 特征选择）
- **2 项 REBUT（部分）**：
  - N3 规模覆盖：同意缺 >8B 数据，但反驳"下降趋势"说法——Pythia 族内 1B→2.8B F1 略升，Qwen3 族内非单调，Mistral 低 F1 可能是架构而非规模效应
  - W2 DDR 阈值：R1 遗漏了 Appendix L 已引用 Lakens (2017) equivalence testing，d<0.10 低于 Cohen's "small" effect 有理论基础
- **1 项 AGREE（部分）**：W3 温度敏感性——Qwen3-1.7B 是唯一灾难性退化的 generator，其余 5 个完全稳定，应 frame 为 generator-specific 异常而非 general barrier
- **与 R1 的主要分歧**：R1 给 3.0，我给 2.5，差异在于并发工作的增量贡献和页数超限风险

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1056 · 2026-05-18T09:25:43.709715+00:00_

审稿报告已提交。Round 17 审稿完成。

**最终结果：Overall Score 3.0 (Findings)**

关键发现：
- **3 个 Must-Fix**：页数超限 (~8.12页)、DDR 二分框架需改三分法、instruct 信号崩溃与论文 framing 脱节
- **7 个 Should-Fix**：并发工作区分、DDR vs model collapse 论证、baseline 比较声明、Abstract 精简、feature selection 方法论、>8B 规模 gap、Introduction 动机
- **6 个 Nice-to-Have**：阈值引用、术语统一、表格格式、bib 修正、引用补充、Checklist 确认

Issue Tracker 已同步更新（`review_issues.yaml`），报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 103

## Round 103

70 recorded events


### User

_source line 1057 · 2026-05-18T10:14:49.918293+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2025
- 截止日期: 2025-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-18T10:14:55.232316+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-18T10:14:55.283226+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-18T10:14:58.094603+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-18T10:14:58.145127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-18T10:15:10.195389+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-18T10:15:10.246023+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-18T10:15:13.570948+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-18T10:15:13.671833+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-18T10:15:16.889651+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-18T10:15:16.940205+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-18T10:15:19.608092+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_project_file request_external_review director_post_to_reviewer submit_review_report update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_project_file request_external_review director_post_to_reviewer submit_review_report update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-18T10:15:19.608436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-18T10:15:22.118519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-18T10:15:22.219240+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-18T10:15:25.131015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "external review status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "external review status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-18T10:15:25.181542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-18T10:15:29.499343+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-18T10:15:29.650434+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_050_temp_curve_t09** (failed): DDR signal at t=0.9 degrades relative to t=0.7 but less severely than t=1.0, establishing monotonic temperature sensitivity\n- **exp_049_temp_curve_t05** (failed): DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\n- **exp_051_independent_seed** (success): Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\n  [independent_seed_results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/exp_051_independent_seed/data/independent_seed_results.txt)\n\n## 趋势\n成功 33 / 负向 1 / 失败 10 / 共 45\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-18T10:15:33.617207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-18T10:15:34.470917+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in Base LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Class
…[truncated 585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-18T10:15:34.471304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2025 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2025 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-18T10:15:34.923628+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-18T10:15:42.956673+00:00_

Web search results for query: "EMNLP 2025 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2025 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/11"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"},{"title":"LINGUIST List 36.640 Confs: The 2025 Conference on Empirical Methods in Natural Language Processing / China","url":"https://linguistlist.org/issues/36/640/"},{"title":"EMNLP 2025 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2025%2FConference"},{"title":"[EMNLP 2025] Call for Main Conference Papers","url":"https://groups.google.com/g/ml-news/c/HKZ_H_iiM_A"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025) – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2025"}]

Based on the search results, here is comprehensive information about EMNLP 2025 call for papers:

## Key Submission Deadlines

The ARR submission deadline for long and short papers is May 19, 2025, with a commitment deadline of July 31, 2025 and notification of acceptance on August 20, 2025. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Paper Types and Requirements

EMNLP 2025 
…[truncated 1619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 8485
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-18T10:15:43.007401+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8083
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-18T10:15:57.691070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission deadline 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission deadline 2026"
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-18T10:15:57.942516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 cycle deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 cycle deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-18T10:15:58.545338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-18T10:15:58.897547+00:00_

1	
2	# Round 18 submission — updated by Research Director 2026-05-18
3	# R17 fixes applied: MF2 tri-partition, MF3 Intro restructure, SF1-SF5, N1-N5
4	
5	# === Issues addressed in R18 ===
6	
7	- id: "R13-MF1"
8	  summary: "正文超 8 页限制"
9	  category: format
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 17
14	  mentions:
15	    - {round: 14, reviewers: "R1,R2", note: "8 pages confirmed R14."}
16	    - {round: 17, reviewers: "R1,R2", note: "Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。"}
17	    - {round: 18, reviewers: "Director", note: "Discussion compressed, Conclusion on page 8. Verified with pdftotext."}
18	  action_items:
19	    - {round: 13, action: "Compress to 8 pages", assigned_to: "Director", status: "done"}
20	    - {round: 17, action: "压缩 Discussion/Results 约 0.2 页", assigned_to: "Director", status: "done"}
21	  resolution: "Discussion compressed. Conclusion fits on page 8. Body = 8 pages verified."
22	  resolution_round: 18
23	
24	- id: "R14-W4"
25	  summary: "Baseline comparison fairness — repurposed binary detectors"
26	  category: experiment
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 14
30	  last_seen_round: 17
31	  mentions:
32	    - {round: 14, reviewers: "R1,R2", note: "Detectors not designed for ordinal. Frame as 'repurposed baselines'."}
33	    - {round: 15, reviewers: "R1,R2", note: "Partial consensus: framework fair, threshold-based binary comparison nice-to-have."}
34	    - {round: 16, reviewers: "R1,R2", note: "R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled."}
35	    - {round: 17, reviewers: "R1,R2", note: "两位 Reviewer 均 AGREE。§4.3 开头加声明。"}
36	  action_items:
37	    - {round: 14, action: "Method §3.4 states 'repurposed as depth predictors'", assigned_to: "Agent", status: "done"}
38	    - {round: 17, action: "§4.3 contextualization statement", assigned_to: "Director", status: "done"}
39	  resolution: "§4.3 opens with 'To contextualize depth discr
…[truncated 26452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-18T10:15:58.897925+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-18T10:16:11.594532+00:00_

Web search results for query: "ACL Rolling Review May 2026 cycle deadline submission"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review - ACL Rolling Review | LinkedIn","url":"https://www.linkedin.com/in/acl-rolling-review-a16282315/"}]

Based on the search results, I found information about the ACL Rolling Review cycle schedule. However, the search results don't contain a specific May 2026 cycle deadline. Let me search for more detailed schedule information.

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{
…[truncated 3397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 13652
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-18T10:16:17.050707+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission deadline 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's the information about EMNLP 2026's call for papers and ARR submission deadline:

## EMNLP 2026 Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 19359
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-18T10:16:17.101483+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 18203
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-18T10:16:43.864237+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit template anonymization appendix rules site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit template anonymization appendix rules site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-18T10:16:44.223656+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission requirements responsible NLP checklist page limits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission requirements responsible NLP checklist page limits"
  }
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-18T10:16:46.131066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-18T10:16:46.633251+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, and the resulting recursive chains progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base (pretrained) models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting (Cohen's $d > 0.75$), intermediate, and near-stationary ($d < 0.10$) groups, consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-18T10:16:46.633611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-18T10:16:47.135867+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	How this evolution proceeds is a fundamental question that connects to both model collapse theory \cite{curse_of_recursion, self_consuming_mad} and data provenance.
6	Yet existing detection methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions and obscure qualitative differences: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	This is not hypothetical: estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and such text already re-enters training pipelines at scale.
8	
9	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting} (identifying generative provenance from distributional statistics).
10	No existing method addresses this task in non-paraphrastic continuation chains.
11	
12	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d
…[truncated 2453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-18T10:16:47.136357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-18T10:16:47.538437+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Depth fingerprinting framework. (a)~Recursive generation chains are constructed by iteratively feeding text through a generator $G$. (b)~Seven features are extracted per text: five NLL statistics from a Pythia-410M reference model and two surface diversity measures. Horizontal bars show Spearman $\rho$ with generation depth and reveal differential depth response: drifting features ($|\rho| > 0.6$) capture the monotonic location shift, while stationary features ($|\rho| < 0.1$) provide a stable baseline. (c)~An XGBoost classifier trained under Leave-One-Generator-Out (LOGO) cross-validation predicts depth class (gen-0\,/\,gen-1\,/\,gen-2+).}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight gen
…[truncated 9523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-18T10:16:47.538920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-18T10:16:47.589805+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.}
14	This protocol differs from LOGO (all generators appear in training), so the difference from single-generator LOGO (binary 0.694) reflects both protocol and generator-subset effects; the 5-generator LOGO average is 0.734 for reference.
15	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
16	
17	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, which confirms transfer across architectural families.
18	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633). This may partly reflect same-family affinity with the Pythia-410M reference model rather than scale alone, though cross-reference experiments show the e
…[truncated 9376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-18T10:16:50.208079+00:00_

Web search results for query: "ACL Rolling Review 2026 submission requirements responsible NLP checklist page limits"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/about/submissions"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"}]

Based on the search results, here's what I found regarding ACL Rolling Review 2026 submission requirements:

## Responsible NLP Checklist

Authors must complete a responsible NLP research checklist as part of their paper submiss
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5984
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-18T10:16:55.478826+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit template anonymization appendix rules site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

I found some relevant information about EMNLP 2026 author guidelines from the official website. Here's what the search results contain:

## Appendix Rules
Authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper; to avoid misunderstandings regarding the nature of the appendix, especially for final papers with excessive appendix length, the EMNLP 2026 Industry Track chairs reserve the right to include a statement that it is not mandatory for reviewers to review the material presented in the appendix.

## Anonymization Requirements
Industry Track submissions must neither include the authors' names nor their affiliations. Additionally, submissions should avoid links to non-anonymised repositories; code should be submitted as a
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 11614
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-18T10:17:05.021226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-18T10:17:05.523856+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{tang2024science}, \citet{wu_survey_2025}, and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8,defactify_dataset}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal,corn_ordinal}) and the finding that combining drifting, intermediate, and near-stationary features yields consistent cross-generator performa
…[truncated 5843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-18T10:17:05.574497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-18T10:17:06.428661+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape while allowing location to drift.
5	Temperature and prompt-type ablations (\S\ref{sec:results-differential}) support this as a tendency rather than a guarantee: the signal degrades sharply at $t{=}0.9$ and varies across prompt types.
6	
7	Instruction tuning substantially weakens the signal (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base; 17--20\,pp degradation across three families) and reverses entropy-depth associations ($\rho$ flips from ${\approx}{-}0.6$ to $+0.2$--$+0.5$), consistent with shifting the generation attractor rather than destroying the iterative dynamics.
8	This restricts current applicability to base models; at the document level, gen-1 per-class F1\,=\,0.63 suffices for corpus-level flagging but not automated filtering (Appendix~\ref{app:error-analysis}).
9	Cross-temperature transfer degrades substantially at $t{=}1.0$ (Appendix~\ref{app:cross-temp}).
10	
11	Three classes represent the practical resolution ceiling (5-class F1 ${\approx}$0.50; Appendix~\ref{app:finer-depth}), and the gen-1/gen-2+ boundary rather than ordinal structure is the bottleneck.
12	DDR is distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}: inference-chain drift occurs with fixed parameters, is fully reversible, and leaves distributional shape near-stationary (Cohen's $d < 0.10$; variance ratios 0.98--1.12 vs.\ 1.90--2.20 for drifting features).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-18T10:17:06.579635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-18T10:17:06.881171+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response (DDR) across eight base-model generators from five families: three features drift monotonically with depth ($d > 0.75$), one shows an intermediate non-monotonic shift ($d{=}0.55$), and three remain near-stationary ($d < 0.10$).
5	A 7-feature ensemble detects this drift with leak-free binary F1\,=\,0.694 (LOGO) and 0.764 (cross-model chains).
6	Current applicability is restricted to base models; instruction tuning and larger scales remain open.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-18T10:17:06.881512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-18T10:17:07.082630+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, 
…[truncated 2339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-18T10:17:07.082967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-18T10:17:07.133362+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-18T10:17:12.796443+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-18T10:17:14.410811+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 23\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 1488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1614
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-18T10:17:14.662221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-18T10:17:15.013925+00:00_

1	% ===== Statistics =====
2	
3	@book{cohen1988statistical,
4	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
5	  author = {Cohen, Jacob},
6	  edition = {2nd},
7	  publisher = {Lawrence Erlbaum Associates},
8	  year = {1988},
9	}
10	
11	@article{tang2024science,
12	  title = {{The Science of Detecting LLM-Generated Text}},
13	  author = {Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},
14	  journal = {Communications of the ACM},
15	  volume = {67},
16	  number = {4},
17	  pages = {50--59},
18	  year = {2024},
19	}
20	
21	@article{neal2017surveying,
22	  title = {{Surveying Stylometry Techniques and Applications}},
23	  author = {Neal, Tempestt and Sundararajan, Kalaivani and Fatima, Aneez and Yan, Yiming and Xiang, Yingfei and Woodard, Damon L.},
24	  journal = {ACM Computing Surveys},
25	  volume = {50},
26	  number = {6},
27	  pages = {1--36},
28	  year = {2017},
29	}
30	
31	% ===== Detection =====
32	
33	@inproceedings{detectgpt,
34	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
35	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
36	  booktitle = {Proceedings of the International Conference on Machine Learning},
37	  year = {2023},
38	}
39	
40	@inproceedings{gltr,
41	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
42	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
43	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
44	  year = {2019},
45	}
46	
47	@inproceedings{dna_gpt,
48	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
49	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
50	  booktitle = {Proceedings of the International Conference on Learning Representations},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-18T10:17:15.014355+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-18T10:17:15.064940+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/review_context.yaml
/home/ubuntu/.age
…[truncated 3222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-18T10:17:19.253735+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-18T10:17:20.365796+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_15.md:180:外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_13.md:186:外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_6.md:16:**外部审稿**: 已跳过（用户未提交至 paperreview.ai）
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_6.md:162:**状态**: 已跳过（用户未提交至 paperreview.ai）
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_11.md:173:项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_2.md:177:项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:1
…[truncated 1176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-18T10:17:20.372899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-18T10:17:20.473619+00:00_

100	\label{app:ablation-table}
101	\input{appendix_ablation}
102	
103	\input{appendix_feature_correlation}
104	
105	\section{Cross-Family Reference Models}
106	\label{app:cross-ref}
107	\input{table4}
108	
109	\input{appendix_seed_control}
110	
111	\input{appendix_qualitative_examples}
112	
113	\end{document}
114	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-18T10:18:20.758843+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May 2026 cycle\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 正文 8 页（不含 Limitations/Ethics/References/Appendix）\n- 模板: ACL 2023 template（`\\usepackage[review]{acl}`）\n- 匿名: Two-way anonymized (double-blind)\n- Limitations section 必须有（不计入页数）\n- Responsible NLP Checklist 必填\n- Appendix 无页数限制，但审稿人不强制审阅\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n请从以下维度严格审查：\n\n1. **DDR 框架有效性**：\n   - 三分法（drifting / intermediate / near-stationary）的分界标准是否充分论证？阈值选择是否任意？\n   - \"location shift while shape remains stable\" 的声明是否有足够统计支撑？KS test / Cohen's d / Levene test 的综合使用是否合理？\n   - entropy_std 作为唯一 intermediate feature 的分类是否令人信服？\n\n2. **实验设计与控制**：\n   - Seed sharing 在 LOGO 评估中的影响是否充分控制？gen-0 leak 的处理方式是否恰当？\n   - Binary F1=0.694 作为 primary metric 的选择是否合理？这个性能水平是否足以支撑论文声明？\n   - Length confound control (binary F1 从 0.770 降到 0.724) 的解释是否充分？\n   - Temperature sensitivity（t=0.9 时 -26pp）对方法通用性的影响是否被低估？\n\n3. **Baseline 对比公平性**：\n   - \"repurposed as depth predictors\" 的 framing 是否足以解释 4-detector ensemble 实际表现更好（0.708 vs 0.705）？\n   - 7-feature 方法的真实优势是否仅在推理效率（9.7ms vs 22.8ms）？\n\n4. **统计声明可靠性**：\n   - Bonferroni 校正的范围是否正确？\n   - Bootstrap CI 的使用是否恰当？\n   - Cross-reference experiments (spread ≤0.013) 是否足以声称 DDR 是 \"property of recursive generation\"？\n\n5. **可重复性**：\n   - 实验描述是否足够复现？\n   - 超参数选择（XGBoost: est=200, depth=6, lr=0.1）是否有 tuning？是否有 bias？\n\n请按以下结构输出审稿报告：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，区分 Must-Fix / Should-Fix / Nice-to-Have）\n- Questions（需要作者回答的问题）\n- Missing References\n- Detailed Comments（逐 Section）\n- Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May 2026 cycle\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 正文 8 页（不含 Limitations/Ethics/References/Appendix）\n- 模板: ACL 2023 template（`\\usepackage[review]{acl}`）\n- 匿名: Two-way anonymized (double-blind)\n- Limitations section 必须有（不计入页数）\n- Responsible NLP Checklist 必填\n- Appendix 无页数限制，但审稿人不强制审阅\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n请从以下维度严格审查：\n\n1. **DDR 框架有效性**：\n   - 三分法（drifting / intermediate / near-stationary）的分界标准是否充分论证？阈值选择是否任意？\n   - \"location shift while shape remains stable\" 的声明是否有足够统计支撑？KS test / Cohen's d / Levene test 的综合使用是否合理？\n   - entropy_std 作为唯一 intermediate feature 的分类是否令人信服？\n\n2. **实验设计与控制**：\n   - Seed sharing 在 LOGO 评估中的影响是否充分控制？gen-0 leak 的处理方式是否恰当？\n   - Binary F1=0.694 作为 primary metric 的选择是否合理？这个性能水平是否足以支撑论文声明？\n   - Length confound control (binary F1 从 0.770 降到 0.724) 的解释是否充分？\n   - Temperature sensitivity（t=0.9 时 -26pp）对方法通用性的影响是否被低估？\n\n3. **Baseline 对比公平性**：\n   - \"repurposed as depth predictors\" 的 framing 是否足以解释 4-detector ensemble 实际表现更好（0.708 vs 0.705）？\n   - 7-feature 方法的真实优势是否仅在推理效率（9.7ms vs 22.8ms）？\n\n4. **统计声明可靠性**：\n   - Bonferroni 校正的范围是否正确？\n   - Bootstrap CI 的使用是否恰当？\n   - Cross-reference experiments (spread ≤0.013) 是否足以声称 DDR 是 \"property of recursive generation\"？\n\n5. **可重复性**：\n   - 实验描述是否足够复现？\n   - 超参数选择（XGBoost: est=200, depth=6, lr=0.1）是否有 tuning？是否有 bias？\n\n请按以下结构输出审稿报告：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，区分 Must-Fix / Should-Fix / Nice-to-Have）\n- Questions（需要作者回答的问题）\n- Missing References\n- Detailed Comments（逐 Section）\n- Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-18T10:18:40.251382+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19492
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-18T10:18:40.353077+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 完整性 + 写作质量\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May 2026 cycle\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 正文 8 页（不含 Limitations/Ethics/References/Appendix）\n- 模板: ACL 2023 template（`\\usepackage[review]{acl}`）\n- 匿名: Two-way anonymized (double-blind)\n- Limitations section 必须有（不计入页数）\n- Responsible NLP Checklist 必填\n- Appendix 无页数限制，但审稿人不强制审阅\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n请从以下维度严格审查：\n\n1. **新颖性与增量贡献**：\n   - 相对于 concurrent work (Broken Telephone, Markovian Chains)，本文的增量贡献是否足够？\n   - \"generation depth classification\" 作为新 task formulation 的价值有多大？是否只是 binary detection 的自然扩展？\n   - DDR tri-partition 相对于 model collapse 文献中已知的 aggregate drift 观察，真实增量在哪里？\n   - 7 个特征（5 个 NLL 统计 + TTR + hapax）都是标准统计量，方法新颖性是否被过度声称？\n\n2. **Related Work 覆盖与定位**：\n   - 引用是否充分覆盖直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - Stylometry 引用是否足够？（仅 3 篇）\n   - §2.2 对 Broken Telephone 和 Markovian Chains 的区分论证是否充分？\n   - Data contamination / data provenance 文献线是否缺失？\n\n3. **叙事连贯性**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线？\n   - Introduction 中 \"base-model restriction\" 的动机是否充分？从大问题切入到 base-model-only scope 的过渡是否自然？\n   - \"Why depth matters\" 的论证是否在 Introduction 中清晰展开？\n   - Discussion 是否充分回应了 Results 中的关键发现和局限？\n\n4. **写作质量 & AI 痕迹**：\n   - 检查 em-dash (—) 和 en-dash (–) 的不当使用\n   - 检查 \"-ing\" 分词短语结尾\n   - 检查过度分段\n   - 检查 \"Furthermore\" / \"Moreover\" / \"Additionally\" 连续使用\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, myriad, plethora 等）\n   - 检查专有名词首次出现是否有定义\n\n5. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 图表知识密度、字体大小（≥7pt）、caption 自包含性\n   - Bib 格式一致性（pages/volume 是否完整）\n   - Limitations section 是否充分\n   - 是否遗漏 Responsible NLP Checklist？\n\n请按以下结构输出审稿报告：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，区分 Must-Fix / Should-Fix / Nice-to-Have）\n- Questions（需要作者回答的问题）\n- Missing References\n- Detailed Comments（逐 Section）\n- Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 完整性 + 写作质量\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May 2026 cycle\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 正文 8 页（不含 Limitations/Ethics/References/Appendix）\n- 模板: ACL 2023 template（`\\usepackage[review]{acl}`）\n- 匿名: Two-way anonymized (double-blind)\n- Limitations section 必须有（不计入页数）\n- Responsible NLP Checklist 必填\n- Appendix 无页数限制，但审稿人不强制审阅\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n请从以下维度严格审查：\n\n1. **新颖性与增量贡献**：\n   - 相对于 concurrent work (Broken Telephone, Markovian Chains)，本文的增量贡献是否足够？\n   - \"generation depth classification\" 作为新 task formulation 的价值有多大？是否只是 binary detection 的自然扩展？\n   - DDR tri-partition 相对于 model collapse 文献中已知的 aggregate drift 观察，真实增量在哪里？\n   - 7 个特征（5 个 NLL 统计 + TTR + hapax）都是标准统计量，方法新颖性是否被过度声称？\n\n2. **Related Work 覆盖与定位**：\n   - 引用是否充分覆盖直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - Stylometry 引用是否足够？（仅 3 篇）\n   - §2.2 对 Broken Telephone 和 Markovian Chains 的区分论证是否充分？\n   - Data contamination / data provenance 文献线是否缺失？\n\n3. **叙事连贯性**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线？\n   - Introduction 中 \"base-model restriction\" 的动机是否充分？从大问题切入到 base-model-only scope 的过渡是否自然？\n   - \"Why depth matters\" 的论证是否在 Introduction 中清晰展开？\n   - Discussion 是否充分回应了 Results 中的关键发现和局限？\n\n4. **写作质量 & AI 痕迹**：\n   - 检查 em-dash (—) 和 en-dash (–) 的不当使用\n   - 检查 \"-ing\" 分词短语结尾\n   - 检查过度分段\n   - 检查 \"Furthermore\" / \"Moreover\" / \"Additionally\" 连续使用\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, myriad, plethora 等）\n   - 检查专有名词首次出现是否有定义\n\n5. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 图表知识密度、字体大小（≥7pt）、caption 自包含性\n   - Bib 格式一致性（pages/volume 是否完整）\n   - Limitations section 是否充分\n   - 是否遗漏 Responsible NLP Checklist？\n\n请按以下结构输出审稿报告：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，区分 Must-Fix / Should-Fix / Nice-to-Have）\n- Questions（需要作者回答的问题）\n- Missing References\n- Detailed Comments（逐 Section）\n- Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-18T10:18:41.971728+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1618
}
```

</details>

---


### Assistant

_source line 1126 · 2026-05-18T10:18:46.284807+00:00_

两位 Reviewer 已分配：

- **Reviewer 1** (方法严谨性 + 实验设计) → 已派发
- **Reviewer 2** (新颖性 + 完整性 + 写作质量) → 已派发

等待两位 Reviewer 的 Round 1 独立审稿结果返回后，进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1127 · 2026-05-18T10:26:53.469678+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 via ARR May 2026
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## Summary

本文提出 generation depth classification 这一新任务，将 LLM 文本分类为 gen-0（人类）/ gen-1（一次生成）/ gen-2+（多次递归生成），而非传统的 binary real-vs-synthetic 检测。作者定义了 differential depth response (DDR) 三分法（drifting / intermediate / near-stationary），使用 7 个标准统计特征（5 个 NLL 统计量 + TTR + hapax ratio）+ XGBoost 分类器，在 8 个 base model 生成器、5 个模型族上取得 3-class LOGO F1 = 0.694。实验设计扎实（LOGO 交叉验证、cross-model chains、多项消融），但方法论新颖性有限，且 base-model-only 约束显著限制了实际影响力。

---

## Strengths

**S1. 清晰且有意义的任务定义。** Generation depth classification 是一个被明确定义的新任务。相对于 binary detection（real vs. synthetic），depth classification 提供了更细粒度的 provenance 信息。这是对现有 AI-generated text detection 文献的自然且有价值的扩展。

**S2. 严谨的实验设计。** LOGO（Leave-One-Generator-Out）交叉验证协议设计合理，能真实反映跨生成器泛化能力。共享 seed passages、bootstrap CIs、class-balanced subsampling、等价性检验（TOST）等统计工具的使用体现了良好的实验方法论素养。

**S3. 全面且诚实的消融分析。** 附录覆盖 12 页，包含 length confound (Appendix B)、prompt type (Appendix C)、5-class fine-grained classification (Appendix D)、QLoRA end-to-end (Appendix E)、LOFO (Appendix F)、confusion matrix (Appendix G)、classifier sensitivity (Appendix H)、robustness to perturbation (Appendix I)、cross-domain (Appendix J)、error analysis (Appendix K)、downstream utility (Appendix L)、margin sensitivity (Appendix M)、feature distribution (Appendix N)、cross-temperature (Appendix O)。每个消融都有明确目的，且正文中有引用。

**S4. DDR 三分法提供了有用的实证框架。** 将特征分为 drifting（entropy mean, TTR, hapax ratio shift monotonically with depth）、intermediate（entropy std）和 near-stationary（entropy max, tail decay, entropy min）的观察，虽然不算深刻的理论贡献，但为理解递归生成的统计签名提供了实用的组织框架。

**S5. Limitations 章节坦诚。** 明确承认了 base-model restriction、instruction-tuning confound、depth signal 在 depth 2+ 后退化、reference model dependency 等限制，没有过度宣传。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 方法论新颖性不足——7 个特征均为标准统计量，分类器为 off-the-shelf XGBoost。**

- 具体位置：§3.3 Feature Extraction (p.4-5), §3.4 Evaluation Protocol (p.5-6)
- 问题：论文使用的 7 个特征（entropy mean/std/min/max、tail decay、TTR、hapax ratio）都是文献中已广泛使用的标准统计量。NLL 统计量直接来自已有 AI-text detection 方法（DetectGPT, Binoculars 等使用 perplexity/NLL），TTR 和 hapax ratio 是经典 stylometry 指标（Neal et al., 2017）。分类器是 XGBoost（Chen & Guestrin, 2016），无任何架构改进。论文声称 "our LOGO evaluation de facto compares against the full features" (p.5)，但对比的 baseline（Avg-LogProb, FastDetectGPT, Binoculars, LD-Score）都是 binary detection 方法，并非为 depth classification 设计的。这使得 "方法贡献" 主要停留在 "把已有特征组合起来用于新任务"，这对于顶会的贡献门槛可能不够。
- 建议：(a) 考虑设计 depth-specific 特征（如跨 depth 的分布演化率、NLL 分布的高阶矩变化模式等），而非仅用标准特征；(b) 或者更明确地将论文定位为 empirical study / dataset paper，降低对方法新颖性的声称。

**N2 [critical] Base-model-only 约束严重限制实际影响力，且动机论证不充分。**

- 具体位置：§1 Introduction (p.1, "We restrict to base (pretrained) models as a deliberate design choice, since instruction-tuning introduces confounds"), §Limitations (p.9)
- 问题：现实中几乎所有部署的 LLM 都是 instruction-tuned（ChatGPT, Claude, Gemini 等）。论文将 base-model restriction 描述为 "deliberate design choice"，但 §Limitations (p.9) 承认 "preliminary experiments confirm that depth signal degrades substantially under instruction tuning (OLMo-2.8B-Instruct drops to LOGO F1 = 0.338)"。F1 从 0.694 降到 0.338（接近 random baseline 0.33），这意味着方法在实际场景中可能完全失效。Introduction 中 "instruction tuning introduces confounds" 不足以说服审稿人——如果 confound 使方法失效，那方法本身的鲁棒性值得质疑。论文也未讨论 chat-format 或 RLHF 模型的影响。
- 为什么影响接收：如果方法仅在 base model 上有效而在 instruction-tuned model 上近乎失效，其实际应用价值大打折扣。审稿人会质疑：谁会在实践中遇到大量 base-model 生成的递归文本链？
- 建议：(a) 至少在正文中纳入 instruction-tuned 模型的实验结果（而非仅在 Limitations 中一句话提及）；(b) 详细分析 instruction-tuning 为什么破坏 depth signal，是否有恢复方法；(c) 更明确地论证 base-model 场景的重要性（例如 LLM pretraining data 中的合成文本主要来自 base model continuation）。

**N3 [critical] DDR 三分法相对于 model collapse 已知观察的增量贡献不清晰。**

- 具体位置：§1 Introduction (p.1-2), §4.2 Differential Depth Response (p.7), §2.1 (p.2)
- 问题：Model collapse 文献（Shumailov et al., 2024; Dohmatob et al., 2025）已经记录了递归生成导致的分布退化：词汇多样性下降、概率分布向高频 token 集中等。论文声称 DDR 三分法 "has no analogue in model collapse studies" (p.2)，但：(a) "drifting features"（entropy mean, TTR, hapax ratio 单调移动）本质上就是 model collapse 中已知的"分布逐渐退化"现象；(b) "near-stationary features"（shape 保持稳定）可以从模型输出分布的数学性质直接推导——如果模型的 softmax 分布形状相对稳定（由 temperature 和 architecture 决定），而仅位置参数（哪些 token 被赋予高概率）发生变化，那么 shape features 天然近乎不变。论文 §2.2 试图与 Broken Telephone 和 Markovian Chains 区分，但未充分论证 DDR 的独特增量。
- 建议：更精确地定义 DDR 相对于已知 model collapse 效应的具体新观察，避免 "naming existing phenomena" 的印象。如果主要贡献是"将 aggregate drift 分解为 location shift vs. shape stability"，应更明确地说明这一分解的理论意义和实践价值。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Depth signal 在 gen-2+ 后迅速退化，动摇 "depth fingerprinting" 的 framing。**

- 具体位置：Appendix D (p.14-15), §5 Discussion (p.8)
- 问题：5-class fine-grained classification（gen-0 到 gen-4）的 LOGO F1 仅为 0.50 (Appendix D, Table 5)，且 Appendix D 分析表明 "the degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.259 and 0.259 F1 respectively"。论文在正文中将 depths 2-4 合并为 "gen-2+"，这本质上承认方法无法做细粒度 depth 分辨。论文标题使用 "Depth Fingerprinting" 暗示了较高的深度分辨能力，但实际上方法只能做 3-class 分类（human / first-gen / multi-gen），更接近 "粗粒度 provenance detection" 而非 "fingerprinting"。
- 建议：(a) 考虑调整标题和 framing 以准确反映能力边界；(b) 在正文中更充分地讨论 3-class 和 5-class 的性能差距。

**W2 [warning] Reference model dependency 是重要的实际限制，讨论不充分。**

- 具体位置：§5 Discussion (p.7-8), Appendix J Cross-Domain (p.18)
- 问题：方法的 5 个 NLL 特征依赖于固定的 reference model（Pythia-410M）。§5 提到 "reference model calibration is critical for cross-domain deployment" (p.7)，但 Appendix J 显示跨域评估时 3-class F1 降至 0.622-0.634（Code/News/Academic domains, Table 14），论文将此解读为 "depth signal remains robust even when the human-vs-machine boundary becomes less distinct"，但绝对性能下降仍然显著。更重要的是，论文未讨论：如果目标文本不是由 base model 续写 Wikipedia 段落，而是任意 domain/genre，方法性能如何？Reference model 的选择对不同生成器家族是否存在系统性偏差？
- 建议：(a) 系统评估多个 reference model 的影响；(b) 讨论在不知道生成器家族的情况下如何选择 reference model。

**W3 [warning] Downstream utility 结果反而弱化了论文动机。**

- 具体位置：Appendix L (p.19-20)
- 问题：论文在 Introduction 中以 data curation 作为关键应用场景来论证 depth classification 的重要性。但 Appendix L 的 downstream utility 实验显示：depth-aware curation 和 random subsampling 在 perplexity 上"practically indistinguishable"（TOST 确认等价，Δ = 0.020, p = 1.1 × 10⁻¹²）。论文将此解释为 "provenance transparency, rather than content removal, is the objective"，但这实质上表明 depth 信息对数据质量没有可检测的影响。如果知道 depth 不能改善 downstream task performance，为什么用户应该关心文本的 generation depth？
- 建议：寻找更有说服力的应用场景来支撑动机，或坦诚地将贡献定位在科学理解（understanding recursive generation dynamics）而非实际应用。

**W4 [warning] Stylometry 引用覆盖不足。**

- 具体位置：§2.3 Vocabulary Diversity and Stylometry (p.3)
- 问题：论文使用 TTR 和 hapax ratio 作为核心特征（2/7），但 stylometry 相关引用仅有 Stamatatos (2009), Koppel et al. (2009), Neal et al. (2017) 三篇 survey，加上 Uchendu et al. (2020) 的 attribution 工作。考虑到这两个特征在 DDR 三分法中被归为 drifting（核心贡献之一），相关文献覆盖应更充分。缺失的相关工作包括：computational stylistics 在 text authorship verification 中的应用、TTR 变体（如 Moving Average TTR, HD-D）的讨论、以及 lexical richness measures 的比较文献。
- 建议：扩展 §2.3，增加 stylometric feature selection 的文献覆盖。

**W5 [warning] Data contamination / data provenance 文献线缺失。**

- 具体位置：§2 Related Work (p.2-3)
- 问题：论文多次提及 data provenance 和 data curation 作为应用动机，但 Related Work 中缺少对 data provenance / contamination detection 文献的系统覆盖。除了 Min-K% (Shi et al., 2024) 之外，未引用 data contamination detection 领域的重要工作（如 Oren et al. 2024 "Proving test set contamination in black box language models"; Golchin & Surdeanu 2024 "Time Travel in LLMs"; Deng et al. 2024 "Investigating data contamination in modern benchmarks" 等）。Data provenance tracking systems 的文献也完全缺失。
- 建议：增加一个简短的 paragraph 讨论 data provenance 和 contamination detection 的相关工作，明确本文方法与这些工作的区别（depth of generation vs. membership/contamination）。

### Nice-to-Have 问题（不影响接收）

**M1.** §3.2 (p.4) 仅测试了 temperature t=0.7 和 nucleus sampling p=0.9。现实中 LLM 使用的 temperature 范围更广（0.0-1.5+），且不同 API 可能使用不同的 sampling 策略（top-k, min-p 等）。虽然 Appendix H (temperature sensitivity) 补充了 t=0.5 的结果，但覆盖仍然有限。

**M2.** Table 1 (p.7) 中 per-generator 结果显示 Mistral-7B 的 3-class F1 最低（0.633），但正文讨论不足。Mistral-7B 为什么更难分类？是否与模型架构、训练数据、或 generation characteristics 有关？

**M3.** Figure 1 (p.4) 的 framework 概览图信息密度偏低——(a) 部分是 trivial 的 pipeline 示意图，可以压缩。

**M4.** 正文第 8 页 §6 Conclusion 最后一句 "Three classes represent the practical resolution ceiling" 与前文 "depth fingerprinting" 的 framing 存在 tension，如 W1 所述。

---

## Questions（需要作者回答）

**Q1.** 为什么选择 Pythia-410M 作为 reference model 而非其他模型？是否尝试过其他 reference model（如 GPT-2, Llama 等），结果差异如何？

**Q2.** DDR 三分法的 threshold（ρ > 0.60 为 drifting，ρ < 0.10 为 near-stationary）是如何确定的？是否进行了 sensitivity analysis？如果更换 threshold，三分法是否仍然成立？

**Q3.** 论文声称 depth signal 是 "prompt-type dependent"（§Limitations, p.9）：continuation chains 信号最强，paraphrase chains 最弱。在 real-world scenario 中，攻击者可以选择 paraphrase-style 递归来规避检测。作者如何看待这一限制？

**Q4.** 如果 gen-2+ 的样本在 downstream utility 实验中与 random sample 等价（Appendix L），那么 depth classification 的实际应用价值体现在哪里？论文提到 "transparency"，能否给出更具体的使用场景？

**Q5.** Instruction-tuned model 上 F1 降至 0.338 的原因是什么？是 depth signal 本身消失了，还是 instruction tuning 引入了新的 confound 使特征不再 discriminative？

---

## Missing References

1. **Data contamination detection**: Oren et al. (2024) "Proving test set contamination in black box language models"; Golchin & Surdeanu (2024) "Time Travel in LLMs: Tracing Data Contamination in Large Language Models"
2. **Lexical richness measures**: McCarthy & Jarvis (2010) "MTLD, vocd-D, and HD-D: A validation study of sophisticated approaches to lexical diversity assessment"
3. **TTR variants**: Covington & McFall (2010) "Cutting the Gordian Knot: The Moving-Average Type-Token Ratio (MATTR)"
4. **Recursive LLM generation / self-play**: Huang et al. (2023) "Large Language Models Cannot Self-Correct Reasoning Yet Without External Feedback" (relevant context for iterative generation limitations)
5. **Data provenance**: Longpre et al. (2024) "Data Authenticity, Consent, and Provenance for AI Are All Broken"

---

## Detailed Comments（逐 Section）

### Abstract (p.1)
- 基本满足四个必答问题（问题、重要性、方法、结果），篇幅约 200 words，在合理范围内。
- "depth fingerprinting (identifying generative provenance from distributional statistics)" 术语首次出现即有定义，良好。
- "DDR" 缩写在 Abstract 中首次出现已展开定义 ✓
- 可以更直接地说明 base-model restriction——当前 Abstract 未提及此约束，可能给读者造成方法适用于所有 LLM 的印象。

### Introduction (p.1-2)
- 叙事线基本连贯：LLM 文本泛滥 → recursive chains → binary detection 不够 → depth classification。
- 从大问题（"LLM-generated text increasingly re-enters the web"）切入到具体贡献的过渡尚可，但 "base-model restriction" 的引入有些突兀（p.1 最后一段）。
- Contribution 列表有两条，对应后续 sections 有明确支撑 ✓
- "7–17% of recent scientific papers and peer reviews contain substantial LLM-modified content" (p.1) 引用了 Liang et al. (2024a,b)，但这些数据描述的是 instruction-tuned model 的影响，与本文的 base-model scope 存在 tension。

### Related Work (p.2-3)
- 结构清晰，分为 AI-Generated Text Detection (§2.1)、Model Collapse and Iterative Generation (§2.2)、Vocabulary Diversity and Stylometry (§2.3) 三个主题。
- §2.1 覆盖了主要的 detection 方法，引用量适当。
- §2.2 对 Broken Telephone 和 Markovian Chains 的区分论述存在但不够深入。核心区分 "their setting constrains each step to be a near-paraphrase of the previous output" vs. "our continuation chains pose no such constraint" (p.3) 是有效的。
- §2.3 偏薄（如 W4 所述）。
- 缺少 data provenance/contamination 线（如 W5 所述）。

### Method (p.3-5)
- §3.1 Task Formulation 清晰，generation depth 的数学定义明确。
- §3.2 Generation Chain Construction：8 generators from 5 families，覆盖了主流 base models。但 temperature 固定为 t=0.7, p=0.9 且最大长度 256 tokens，这些参数选择的 justification 不足。
- §3.3 Feature Extraction：7 个特征的选择有动机（"reference-model features" + "surface features"），但特征空间很小（仅 7 维），论文未讨论为何不使用更丰富的特征集（如 n-gram distributions, syntactic features, embedding-based features 等）。
- §3.4 Evaluation Protocol：LOGO 和 cross-model chains 协议设计良好。Baseline 选择合理但都是 binary detection 方法，缺少针对 multi-class detection 的 baseline。

### Results (p.6-7)
- Table 1 报告清晰，bootstrap CIs 增加可信度。
- §4.2 DDR 部分（p.7）数据呈现紧凑。Spearman 相关系数和 Cohen's d 效应量的使用是恰当的。
- 但 "feature complementarity" 的论述（p.7, "The full 7-feature set ... outperforms surface-only and reference-only"）比较粗略，缺少 feature interaction 的分析。

### Discussion (p.7-8)
- 覆盖了 distributional shift quantification、feature complementarity、cross-family reference models、temperature sensitivity、prompt-type sensitivity、comparison with detection baselines。
- 讨论点较多但每个点的深度不够——更像是 results 的延续而非深入分析。
- 未充分讨论方法的 failure modes 和 theoretical limitations。

### Conclusion (p.8-9)
- 简洁，总结了主要贡献。
- "Three classes represent the practical resolution ceiling" 是诚实的总结。
- "Current applicability is restricted to base models" 的承认值得肯定。

### Limitations (p.9)
- 覆盖了 base-model restriction、instruction-tuning、prompt-type dependency、depth signal degradation 等关键限制 ✓
- 写作诚实，未回避关键限制。

### Ethics Statement (p.9)
- 覆盖了 dual-use concern（depth estimation 可能被用于压制 machine-generated text）✓
- 提到 privacy（不涉及个人数据）✓

---

## 写作质量 & AI 痕迹检查

**Em-dash/En-dash**: 从 PDF 视觉检查来看，论文主要使用括号和逗号进行解释性插入，未见大量 em-dash (—) 滥用。少数 en-dash 用于数字范围（如 "0.6B–8B", "pp. 12–18" 等）属于合理使用。

**-ing 分词短语结尾**: 偶见但不严重。例如 p.2 "collapsing discriminative margins"，p.5 "giving the classifier access to the full marginal distribution shape" 等。整体频率在可接受范围。

**过度分段**: 论文段落长度适中，未见明显的过度分段问题。

**过渡词堆砌**: 未见 "Furthermore/Moreover/Additionally" 的连续使用。

**用词黑名单**: 未检测到 "delve", "leverage", "utilize", "myriad", "plethora" 等 AI 高频词。

**专有名词定义**: DDR、LOGO、TTR、hapax ratio 等专有术语首次出现均有定义 ✓

**总体写作评价**: 写作质量中等偏上，结构清晰，AI 痕迹不明显。主要问题在于部分段落信息密度可以更高（如 Discussion 中多个小段落可以合并深化），以及 Introduction 中 base-model restriction 的 framing 需要加强。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 ≤ 8 | ✓ | Conclusion 在 p.8 结束 |
| ACL template | ✓ | "Anonymous ACL submission" 可见 |
| 匿名化 | ✓ | 未见作者信息泄露 |
| Limitations section | ✓ | p.9 |
| Ethics Statement | ✓ | p.9 |
| Responsible NLP Checklist | ⚠️ | 未在 PDF 中发现，可能通过 ARR 系统单独提交 |
| 图表字体 ≥ 7pt | ✓ | Figure 1-9 字体大小合理 |
| Caption 自包含 | ✓ | 各图表 caption 信息完整 |
| Bib 格式 | ⚠️ | verify_references 显示 5 个 mismatch（多为 first_author 编码问题）和 7 个 not_found（含 DetectGPT, XGBoost, Pythia 等知名论文，可能是 OpenAlex API 限制）|
| 引用覆盖 | ⚠️ | Stylometry 和 data provenance 线覆盖不足（W4, W5） |

---

## 总体评分

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（LOGO, bootstrap CIs, 等价性检验），但 base-model-only 约束下 instruction-tuned 结果近乎失效（F1=0.338）未充分讨论，reference model dependency 分析不足 |
| Excitement | 2.5/5 | 任务定义有意义，但方法仅使用标准特征+标准分类器，DDR 是经验观察而非方法创新，base-model restriction 限制了实际兴趣 |
| Reproducibility | 4/5 | 代码未提供但实验细节充分（§3.2-3.4），特征定义明确，生成参数完整记录，基本可复现 |
| Overall Assessment | **3.0** (Findings) | 任务定义有价值，实验全面，但方法论新颖性有限（标准特征+XGBoost），核心贡献 DDR 更像经验观察而非理论贡献，base-model-only 约束严重限制实际影响力 |
| Confidence | 4/5 | 仔细阅读了全文含所有附录，熟悉 AI-generated text detection 和 model collapse 文献 |

### 一句话总结

论文定义了一个有意义的新任务（generation depth classification），实验设计扎实且全面，但方法论新颖性不足（标准特征+标准分类器），核心发现 DDR 是对已知 model collapse 效应的重新组织而非新发现，且 base-model-only 约束使得实际影响力有限，适合 Findings track 发表。

### 主要优势
- 清晰定义了 generation depth classification 新任务
- 严谨的 LOGO 交叉验证和统计检验
- 全面的消融分析（12 页附录）
- 诚实的 Limitations 讨论

### 接收条件
若作者能 (1) 提供 instruction-tuned model 的正式实验并分析 depth signal 退化原因，(2) 更清晰地论证 DDR 相对于已知 model collapse 效应的增量，(3) 找到更有说服力的应用场景，则论文可提升至 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1128 · 2026-05-18T10:27:02.096638+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 105

## Round 105

6 recorded events


### User

_source line 1129 · 2026-05-18T10:27:03.222682+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿报告

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审查侧重**: 方法严谨性 + 实验设计

---

## Summary

本文提出 "depth fingerprinting"，将 LLM 递归生成文本的深度检测从二分类（人/机）推进到多分类（gen-0 / gen-1 / gen-2+）。核心贡献包括：(1) 提取 7 个文本特征（5 个 NLL 分布特征 + 2 个表面多样性特征），(2) 提出 Differential Depth Response (DDR) 三分法框架将特征分为 drifting / intermediate / near-stationary，(3) 使用 XGBoost 在 Leave-One-Generator-Out (LOGO) 评估下达到 binary F1 = 0.694（gen-1 vs gen-2+）。问题定义新颖，实验设计系统，但绝对性能有限、baseline 对比框架不完全公平、DDR 框架论证不充分。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 | 核心方法论可接受，统计检验使用合理（Bonferroni、bootstrap CI、TOST），但 DDR 阈值论证不足（N1），baseline 实际优于所提方法但 framing 含糊（N2） |
| **Excitement** | 3 / 5 | 问题定义新颖有价值（从二分类到深度分类），但 binary F1 = 0.694 的性能水平和仅限 base model 的适用范围限制了实际影响力 |
| **Reproducibility** | 3.5 / 5 | 特征定义清晰，超参数明确，reference model 指定；但未提及代码/数据开源计划，XGBoost 超参数无 tuning 或 sensitivity 分析 |
| **Reviewer Confidence** | 4 / 5 | 对 AI text detection、统计方法论和实验设计领域较为熟悉 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] DDR 三分法阈值论证不足，"framework" 定位过度

- **具体位置**: Section 4.2, page 7; Figure 2
- **问题**: DDR 将 7 个特征分为 drifting（|ρ| > 0.60）、intermediate（entropy_std 独占）、near-stationary（|ρ| < 0.10）三组。但：
  1. 阈值 0.60 和 0.10 的选择缺乏理论依据。论文引用 Cohen (1988) 的效应量标准，但 Cohen 的 benchmarks 是为效应量 d 设计的（small=0.2, medium=0.5, large=0.8），直接套用于 Spearman ρ 的分组缺乏正当性。
  2. 仅 7 个特征分成 3/1/3，intermediate 类别只有 entropy_std 一个成员。以 N=7 的样本量建立三分类 "framework" 在统计上不具说服力，无法排除这是小样本偶然分布。
  3. Levene test 对 shape features 也拒绝了等方差假设（p < 10⁻¹⁹，Section 4.2），论文用 CV shift < 2% vs > 15% 来辩护 "near-stationary" 是 practical characterization。但 "statistically significantly changing yet practically negligible" 的论证需要更严谨的 equivalence testing（而非仅报告 CV 差异）。
- **为什么影响接收**: DDR 三分法是论文的核心分析框架（贡献 2），如果阈值是 arbitrary 的，整个 DDR 叙事都站不住脚。将对 7 个特征的描述性观察提升为 "framework" 是 overclaiming。
- **建议修改方向**: (1) 对阈值做 sensitivity analysis（例如变动 ±0.1 观察分组是否稳定）；(2) 承认这是 empirical observation 而非 general framework；(3) 对 shape features 用 TOST equivalence testing（论文在 Appendix M 已对 downstream utility 使用了 TOST，可一致化）。

### N2 [critical] Baseline 对比框架不公平：4-detector ensemble 在所有指标上优于所提方法

- **具体位置**: Table 2, page 8; Section 4.3
- **问题**: Table 2 显示：
  - 4-detector ensemble: 3-cl F1 = 0.785, Binary F1 = 0.706 (或 0.708)
  - 7-feature (ours): 3-cl F1 = 0.724, Binary F1 = 0.705
  - 4-det. + surface: 3-cl F1 = 0.798, Binary F1 = 0.708

  4-detector ensemble 在 3-class F1 上领先 **6.1 pp**，binary F1 上基本持平。论文的 framing 是 "Multi-detector ensembles achieve moderately higher F1 at 2.4× the computational cost"（page 8），但 2.4× 对应的是 22.8ms vs 9.7ms，绝对差异仅 **13ms/text**，在实际应用中几乎可忽略。
  
  论文正文 Section 4.3 开头声称 "to contextualize depth discrimination ability rather than claim competitive advantage over detection-optimized methods"。但随后的文字和 Table 2 的排列实际上在做 competitive comparison，且结论暗示效率优势抵消了性能差距。13ms 的差异不足以构成有意义的 efficiency advantage。

- **为什么影响接收**: 如果 repurposed existing detectors 比 proposed method 更好（且代价很小），论文的 practical contribution 需要重新定位。
- **建议修改方向**: (1) 诚实承认 4-detector ensemble 在准确性上更优；(2) 将贡献重新定位为 "interpretability + analytical insight (DDR)"，而非 accuracy vs efficiency trade-off；(3) 或提供更强的 efficiency argument（如 batch 处理大规模 corpus 的场景）。

### N3 [critical] Binary F1 = 0.694 的性能水平与 "fingerprinting" 声明之间存在落差

- **具体位置**: Abstract; Section 4.1, page 6; Title
- **问题**: 
  - 标题 "Depth Fingerprinting" 暗示可靠的深度识别能力。"Fingerprinting" 在安全/取证领域意味着高可靠性。
  - 但 primary metric binary F1 = 0.694 意味着约 30% 的 gen-1 和 gen-2+ 样本被错分。
  - Per-generator 性能差异大：Mistral-7B 的 binary F1 仅 0.633（Figure 6a），而 Pythia-2.8B 达到 0.724。
  - 5-class fine-grained 评估 F1 仅 0.50（Appendix D），实际只能区分 gen-0 / gen-1 / gen-2+，且 gen-1↔gen-2+ 的混淆率很高（confusion matrix Figure 5b: gen-1 recall 75%, gen-2+ recall 73.7%）。
- **为什么影响接收**: 标题和 framing 与实际性能水平之间的 gap 可能让审稿人质疑论文的诚实度。
- **建议修改方向**: (1) 将 "fingerprinting" 改为更审慎的措辞（如 "detection" 或 "estimation"）；(2) 在 abstract 和 introduction 明确声明这是 proof-of-concept / feasibility study；(3) 讨论 F1=0.694 在实际应用中意味着什么。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] Temperature sensitivity 严重限制通用性

- **具体位置**: Appendix H, page 16; Limitations, page 9
- **问题**: t=0.9 时 Pythia-2.8B 下降 26pp，Qwen3-1.7B 下降 18.5pp。大量实际 LLM 部署使用 t=0.7-1.0 范围。论文在 Limitations 中承认了这一点，但 Section 4.2 和 Discussion 中对 DDR 作为 "property of recursive generation" 的声明未充分限定（qualify）这一条件依赖性。
- **建议**: 在所有提及 DDR 普遍性的地方加上 temperature 条件限定；在 abstract 中提及 temperature 限制。

### W2 [warning] 仅限 base models 极大限制实际应用价值

- **具体位置**: Limitations, page 9
- **问题**: 论文承认 "current applicability is restricted to base models; instruction tuning and larger scales remain open"，且 "preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning." 这意味着方法对现实中最常用的 LLM（instruction-tuned / RLHF models）无效。
- **建议**: 在 abstract 或 introduction 早期明确这一 scope restriction，而非仅在 Limitations 中提及。

### W3 [warning] Gen-0 seed sharing 导致 3-class 结果系统性膨胀

- **具体位置**: Section 3.2, Section 4.1, page 6
- **问题**: 论文正确识别了 LOGO 中 gen-0 seed 共享问题并使用 binary F1 作为 primary metric。但 Table 1（page 7）和 Table 2（page 8）仍然突出显示 3-class F1（0.762 和 0.724），而 gen-0 near-perfect 分类（F1 ≈ 0.94）系统性抬高了这些数字。读者可能误读 3-class F1 为方法的真实区分力。
- **建议**: (1) Table 1 增加一列 "binary F1 (gen-1 vs gen-2+)"；(2) 在所有报告 3-class F1 的地方标注 "inflated by gen-0 overlap"。

### W4 [warning] XGBoost 超参数缺少 tuning 说明和 sensitivity 分析

- **具体位置**: Section 3.4, page 6
- **问题**: est=200, depth=6, lr=0.1 的参数选择未说明来源。是默认值？Grid search 结果？Pilot experiments？Appendix E 对 QLoRA 做了 hyperparameter robustness（rank 16 vs 32），但主模型 XGBoost 没有对应分析。depth=6 with 7 features 意味着树可以用所有特征的所有交互，可能过拟合。
- **建议**: 报告 XGBoost 超参数的选择过程，或至少做一个简单的 sensitivity analysis（如 depth={3,4,5,6,8}）。

### W5 [warning] Cross-reference model 实验（spread ≤ 0.013）的声明过强

- **具体位置**: Section 4.2, page 7; Appendix R (Table 21)
- **问题**: 论文声称 "DDR is a property of recurring generation" 基于不同 reference model 下 LOGO F1 spread ≤ 0.013。但这仅说明 **features 对 reference model 选择鲁棒**，不直接支持 "DDR 是递归生成的内在属性"。这是两个不同的声明。前者是 robustness to implementation choice，后者是 fundamental property claim。
- **建议**: 将措辞调整为 "feature computation is robust to reference model choice"，与 "DDR 作为内在属性" 的声明分开论证。

### W6 [warning] Depth 2-4 合并显著限制 "depth fingerprinting" 的声明

- **具体位置**: Section 3.1, page 3-4; Appendix D, page 14
- **问题**: 5-class 评估 F1 = 0.50，gen-2/3/4 无法有效区分。论文承认 "3-class granularity as the practical ceiling"（Appendix D），但 title 用 "Depth" 暗示更精细的分辨率。实际上方法只能区分 "人写的 / 第一代 / 更多代"，这更接近 provenance classification 而非 depth fingerprinting。
- **建议**: 在 title 或 abstract 中更明确地传达 3-class 的粒度限制。

---

## 小问题（不影响接收）

1. **Abstract**: "five NLL distribution and two surface diversity measures" 中 NLL 首次出现未展开为 "negative log-likelihood"。
2. **Section 3.3**: "We select ranks 100-1000 because high-frequency tokens (ranks < 100) exhibit minimal discriminative variance across depths" 缺少引用支撑或 pilot experiment 说明。
3. **Figure 1 caption**: "(b) Seven features are extracted per text: five NLL statistics from a Pythia-410M reference model and two surface diversity measures." 但图中横轴标注了具体 Spearman ρ 值，caption 未提及这些值的含义。
4. **Table 1**: Footnote 标记 (†) 在 binary F1 列上，但解释在表注中不够醒目。
5. **引用格式**: cohen1988statistical 的 year 在 OpenAlex 匹配为 1989（第二版），bib 中用 1988（原始版）。两者均可接受，但应确认引用的是哪个版本。
6. **Appendix 数量过多**（A-R，18 个 appendix）。建议合并相关 appendix，减少读者导航成本。

---

## Questions to Authors

**Q1**: DDR 阈值（|ρ| > 0.60 和 |ρ| < 0.10）的 sensitivity 如何？如果将 drifting 阈值降为 0.50 或 near-stationary 阈值升为 0.15，三分法是否还成立？

**Q2**: LOGO 中 generator family 级别的 hold-out 是如何处理的？例如 Pythia-1B 和 Pythia-2.8B 是同时 held out 还是分别？如果分别，同 family 不同 size 的模型在 train set 中存在会否导致 family-level 信息泄漏？

**Q3**: Downstream utility 实验（Appendix L）显示 depth-aware subsampling 与随机 subsampling 产生的 perplexity 几乎无差异（TOST 确认 equivalence）。如果 depth 信息对 downstream task 没有实际帮助，depth classification 的主要应用场景是什么？

**Q4**: 论文使用 Pythia-410M 作为 reference model。是否测试过更大的 reference model（如 Pythia-2.8B）？Reference model capacity 与检测性能的关系是什么？

**Q5**: 对于 Table 2 中 4-detector ensemble 在所有指标上优于 7-feature method 的结果，作者如何看待方法的 practical value proposition？

**Q6**: Prompt-type sensitivity（Appendix C）显示 continuation chains 产生最强信号。但在实际场景中，递归生成可能用不同的 prompt types。方法在混合 prompt type 条件下的表现如何？

---

## Missing References

- 无明显重要遗漏。AI text detection 和 model collapse 的引用覆盖充分。
- 可考虑补充：关于 iterative self-refinement 对文本分布影响的更多工作（如 Burns et al., 2023 关于 RLHF iterative training 的分析），以及关于 generation depth 在 training data curation 中的应用文献。

---

## 主要优势

1. **问题定义新颖且有价值**: 从 binary detection 推进到 generation depth classification 是有意义的新方向，在数据溯源和合成数据管理中有潜在应用。
2. **系统性实验设计**: LOGO 评估框架设计严谨；8 个 base model generators from 5 families 的覆盖面合理；explicit 处理 gen-0 seed sharing 问题体现了方法论意识。
3. **统计方法运用规范**: Bonferroni correction、bootstrap CI、TOST equivalence testing、Levene test 等工具的综合使用表明作者具备统计素养。
4. **诚实的 Limitations section**: 主动承认 base model 限制、temperature sensitivity、instruction tuning degradation，这在同类论文中不常见。
5. **丰富的 ablation 和 robustness 分析**: 附录涵盖 length confound、classifier alternatives、LOFO、cross-domain、error analysis、downstream utility、margin sensitivity 等，分析深度超过平均水平。
6. **Concurrent work 定位清晰**: 与 Mohamed et al. (2025) 和 Geng et al. (2026) 的区别论述清楚（open-ended continuation vs. paraphrastic/feedback loop）。

---

## 总体评分

**Overall Assessment**: **3.0 — Findings**

**一句话总结**: 问题定义新颖、实验设计系统、统计分析规范，但核心性能有限（binary F1 = 0.694）、DDR 框架论证不充分、baseline 实际优于所提方法、仅适用于 base models，整体达到 Findings 水准但不足以进入主会议。

**置信度**: 4 / 5（Quite sure）

**详细理由**: 

本文的最大价值在于问题定义本身：将 AI text detection 从 binary 推进到 depth estimation 是一个自然且重要的推进方向。DDR 的观察（drifting features 单调偏移、shape features 稳定）作为 empirical finding 是有价值的。然而：

1. DDR 被过度包装为 "framework"，实际上是对 7 个特征行为的描述性分类，阈值选择缺乏理论基础（N1）。
2. Existing detectors 组合后在所有指标上优于所提方法，且效率差异仅 13ms/text（N2），削弱了 practical contribution。
3. Binary F1 = 0.694 与 title 中 "Fingerprinting" 的隐含精度承诺不匹配（N3）。
4. 方法仅适用于 base models + 低 temperature 条件（W1, W2），在实际部署中的适用范围极窄。

如果作者能 (a) 对 DDR 阈值做 sensitivity analysis 并降低 "framework" 声明，(b) 诚实重新定位 baseline 对比，(c) 将 title/framing 调整为 feasibility study，本文可以成为一篇 solid Findings paper。但就当前状态而言，overclaiming 和性能限制之间的 gap 使得主会议接收偏弱。


---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings track)**。

主要发现：
- **3 个 Must-Fix 问题**：(1) 方法论新颖性不足（7 个标准特征 + off-the-shelf XGBoost），(2) base-model-only 约束限制实际影响力（instruction-tuned model 上 F1 从 0.694 骤降至 0.338），(3) DDR 三分法相对于已知 model collapse 效应的增量贡献论证不清晰
- **5 个 Should-Fix 问题**：depth signal 在 gen-2+ 后退化（5-class F1 仅 0.50）、reference model dependency 讨论不足、downstream utility 结果反而弱化动机、stylometry 引用覆盖不足、data provenance 文献线缺失
- **优势**：任务定义清晰、LOGO 实验设计严谨、12 页附录消融全面、Limitations 坦诚
- **写作质量**：中等偏上，AI 痕迹不明显，格式基本合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-18T10:27:48.446992+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + 写作质量）的完整审稿报告。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1 [critical] 方法论新颖性不足——7 个特征均为标准统计量，分类器为 off-the-shelf XGBoost。**\n- 论文使用的 7 个特征（entropy mean/std/min/max、tail decay、TTR、hapax ratio）都是文献中已广泛使用的标准统计量。分类器是 XGBoost，无任何架构改进。对比的 baseline 都是 binary detection 方法，并非为 depth classification 设计的。方法贡献主要停留在\"把已有特征组合起来用于新任务\"。\n\n**R2-N2 [critical] Base-model-only 约束严重限制实际影响力，且动机论证不充分。**\n- 现实中几乎所有部署的 LLM 都是 instruction-tuned。OLMo-Instruct LOGO F1 = 0.338（接近 random baseline 0.33）。Introduction 中 \"instruction tuning introduces confounds\" 不足以说服审稿人。\n\n**R2-N3 [critical] DDR 三分法相对于 model collapse 已知观察的增量贡献不清晰。**\n- Model collapse 文献已记录词汇多样性下降、概率分布向高频 token 集中。\"drifting features\" 本质上就是已知的\"分布退化\"现象；\"near-stationary features\" 可从 softmax 分布数学性质推导。DDR 是否仅是 \"naming existing phenomena\"？\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1 [warning] Depth signal 在 gen-2+ 后迅速退化，动摇 \"depth fingerprinting\" framing。**\n- 5-class F1 仅 0.50，gen-2/gen-3 per-class F1 仅 0.259。标题 \"Depth Fingerprinting\" 暗示较高深度分辨能力，但实际仅 3-class。\n\n**R2-W2 [warning] Reference model dependency 是重要实际限制，讨论不充分。**\n- 5 个 NLL 特征依赖 Pythia-410M。跨域评估 3-class F1 降至 0.622-0.634。未讨论不知道生成器家族时如何选择 reference model。\n\n**R2-W3 [warning] Downstream utility 结果反而弱化论文动机。**\n- Appendix L 显示 depth-aware curation 与 random subsampling 在 perplexity 上 \"practically indistinguishable\"（TOST 确认等价）。如果 depth 信息不影响 downstream performance，为什么用户应该关心？\n\n**R2-W4 [warning] Stylometry 引用覆盖不足。**\n- TTR 和 hapax ratio 是核心特征（2/7），但 stylometry 引用仅 3 篇 survey。缺少 TTR 变体（MATTR, HD-D）和 lexical richness measures 比较文献。\n\n**R2-W5 [warning] Data contamination / data provenance 文献线缺失。**\n- 论文以 data provenance 为应用动机，但 Related Work 缺少 contamination detection 文献（Oren et al. 2024, Golchin & Surdeanu 2024 等）和 data provenance tracking systems。\n\n### Reviewer 2 的 Overall Assessment\n- Overall: 3.0 (Findings)\n- Soundness: 3.5/5, Excitement: 2.5/5, Reproducibility: 4/5\n- 写作质量中等偏上，AI 痕迹不明显，格式基本合规\n- 一句话：任务定义有意义，实验全面，但方法论新颖性不足，DDR 更像经验观察而非理论贡献，base-model-only 约束限制影响力\n\n---\n\n请对以上每个 Must-Fix (R2-N1, R2-N2, R2-N3) 和 Should-Fix (R2-W1 到 R2-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + 写作质量）的完整审稿报告。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1 [critical] 方法论新颖性不足——7 个特征均为标准统计量，分类器为 off-the-shelf XGBoost。**\n- 论文使用的 7 个特征（entropy mean/std/min/max、tail decay、TTR、hapax ratio）都是文献中已广泛使用的标准统计量。分类器是 XGBoost，无任何架构改进。对比的 baseline 都是 binary detection 方法，并非为 depth classification 设计的。方法贡献主要停留在\"把已有特征组合起来用于新任务\"。\n\n**R2-N2 [critical] Base-model-only 约束严重限制实际影响力，且动机论证不充分。**\n- 现实中几乎所有部署的 LLM 都是 instruction-tuned。OLMo-Instruct LOGO F1 = 0.338（接近 random baseline 0.33）。Introduction 中 \"instruction tuning introduces confounds\" 不足以说服审稿人。\n\n**R2-N3 [critical] DDR 三分法相对于 model collapse 已知观察的增量贡献不清晰。**\n- Model collapse 文献已记录词汇多样性下降、概率分布向高频 token 集中。\"drifting features\" 本质上就是已知的\"分布退化\"现象；\"near-stationary features\" 可从 softmax 分布数学性质推导。DDR 是否仅是 \"naming existing phenomena\"？\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1 [warning] Depth signal 在 gen-2+ 后迅速退化，动摇 \"depth fingerprinting\" framing。**\n- 5-class F1 仅 0.50，gen-2/gen-3 per-class F1 仅 0.259。标题 \"Depth Fingerprinting\" 暗示较高深度分辨能力，但实际仅 3-class。\n\n**R2-W2 [warning] Reference model dependency 是重要实际限制，讨论不充分。**\n- 5 个 NLL 特征依赖 Pythia-410M。跨域评估 3-class F1 降至 0.622-0.634。未讨论不知道生成器家族时如何选择 reference model。\n\n**R2-W3 [warning] Downstream utility 结果反而弱化论文动机。**\n- Appendix L 显示 depth-aware curation 与 random subsampling 在 perplexity 上 \"practically indistinguishable\"（TOST 确认等价）。如果 depth 信息不影响 downstream performance，为什么用户应该关心？\n\n**R2-W4 [warning] Stylometry 引用覆盖不足。**\n- TTR 和 hapax ratio 是核心特征（2/7），但 stylometry 引用仅 3 篇 survey。缺少 TTR 变体（MATTR, HD-D）和 lexical richness measures 比较文献。\n\n**R2-W5 [warning] Data contamination / data provenance 文献线缺失。**\n- 论文以 data provenance 为应用动机，但 Related Work 缺少 contamination detection 文献（Oren et al. 2024, Golchin & Surdeanu 2024 等）和 data provenance tracking systems。\n\n### Reviewer 2 的 Overall Assessment\n- Overall: 3.0 (Findings)\n- Soundness: 3.5/5, Excitement: 2.5/5, Reproducibility: 4/5\n- 写作质量中等偏上，AI 痕迹不明显，格式基本合规\n- 一句话：任务定义有意义，实验全面，但方法论新颖性不足，DDR 更像经验观察而非理论贡献，base-model-only 约束限制影响力\n\n---\n\n请对以上每个 Must-Fix (R2-N1, R2-N2, R2-N3) 和 Should-Fix (R2-W1 到 R2-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-18T10:28:09.452878+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21005
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-18T10:28:09.754323+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿报告。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1 [critical] DDR 三分法阈值论证不足，\"framework\" 定位过度**\n- 阈值 0.60 和 0.10 缺乏理论依据。Cohen (1988) 的 benchmarks 是为 d 设计的，直接套用于 Spearman ρ 缺乏正当性。仅 7 个特征分成 3/1/3，intermediate 只有 entropy_std。以 N=7 建立三分类 \"framework\" 在统计上不具说服力。Levene test 拒绝等方差但论文用 CV shift 辩护 \"near-stationary\"，需要 equivalence testing 而非仅报告 CV 差异。\n\n**R1-N2 [critical] Baseline 对比框架不公平：4-detector ensemble 在所有指标上优于所提方法**\n- Table 2 显示 4-det ensemble: 3-cl F1 = 0.785 vs 7-feature: 0.724（差 6.1pp），binary F1 基本持平。效率差异仅 13ms/text（22.8 vs 9.7ms），在实际应用中几乎可忽略。论文 framing 暗示效率优势抵消性能差距，但 13ms 差异不足以构成有意义的 efficiency advantage。\n\n**R1-N3 [critical] Binary F1 = 0.694 的性能水平与 \"fingerprinting\" 声明之间存在落差**\n- \"Fingerprinting\" 在安全/取证领域意味着高可靠性。Binary F1 = 0.694 意味着约 30% 的样本被错分。Per-generator 差异大（Mistral-7B: 0.633 vs Pythia-2.8B: 0.724）。5-class F1 仅 0.50。标题和 framing 与实际性能水平之间的 gap 可能让审稿人质疑论文的诚实度。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1 [warning] Temperature sensitivity 严重限制通用性**\n- t=0.9 时 Pythia-2.8B 下降 26pp，Qwen3-1.7B 下降 18.5pp。DDR 作为 \"property of recursive generation\" 的声明未充分限定 temperature 条件依赖性。\n\n**R1-W2 [warning] 仅限 base models 极大限制实际应用价值**\n- 方法对 instruction-tuned / RLHF models 无效。建议在 abstract 或 introduction 早期明确 scope restriction。\n\n**R1-W3 [warning] Gen-0 seed sharing 导致 3-class 结果系统性膨胀**\n- Table 1 和 Table 2 仍突出显示 3-class F1，gen-0 near-perfect 分类（F1 ≈ 0.94）系统性抬高这些数字。读者可能误读。\n\n**R1-W4 [warning] XGBoost 超参数缺少 tuning 说明和 sensitivity 分析**\n- est=200, depth=6, lr=0.1 选择未说明来源。depth=6 with 7 features 可能过拟合。\n\n**R1-W5 [warning] Cross-reference model 实验（spread ≤ 0.013）的声明过强**\n- 仅说明 features 对 reference model 选择鲁棒，不直接支持 \"DDR 是递归生成的内在属性\"。这是两个不同声明。\n\n**R1-W6 [warning] Depth 2-4 合并显著限制 \"depth fingerprinting\" 声明**\n- 方法只能区分 \"人写的 / 第一代 / 更多代\"，更接近 provenance classification 而非 depth fingerprinting。\n\n### Reviewer 1 的 Overall Assessment\n- Overall: 3.0 (Findings)\n- Soundness: 3/5, Excitement: 3/5, Reproducibility: 3.5/5\n- 置信度: 4/5\n- 一句话：问题定义新颖、实验设计系统、统计分析规范，但核心性能有限、DDR 框架论证不充分、baseline 实际优于所提方法、仅适用于 base models\n\n---\n\n请对以上每个 Must-Fix (R1-N1, R1-N2, R1-N3) 和 Should-Fix (R1-W1 到 R1-W6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿报告。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1 [critical] DDR 三分法阈值论证不足，\"framework\" 定位过度**\n- 阈值 0.60 和 0.10 缺乏理论依据。Cohen (1988) 的 benchmarks 是为 d 设计的，直接套用于 Spearman ρ 缺乏正当性。仅 7 个特征分成 3/1/3，intermediate 只有 entropy_std。以 N=7 建立三分类 \"framework\" 在统计上不具说服力。Levene test 拒绝等方差但论文用 CV shift 辩护 \"near-stationary\"，需要 equivalence testing 而非仅报告 CV 差异。\n\n**R1-N2 [critical] Baseline 对比框架不公平：4-detector ensemble 在所有指标上优于所提方法**\n- Table 2 显示 4-det ensemble: 3-cl F1 = 0.785 vs 7-feature: 0.724（差 6.1pp），binary F1 基本持平。效率差异仅 13ms/text（22.8 vs 9.7ms），在实际应用中几乎可忽略。论文 framing 暗示效率优势抵消性能差距，但 13ms 差异不足以构成有意义的 efficiency advantage。\n\n**R1-N3 [critical] Binary F1 = 0.694 的性能水平与 \"fingerprinting\" 声明之间存在落差**\n- \"Fingerprinting\" 在安全/取证领域意味着高可靠性。Binary F1 = 0.694 意味着约 30% 的样本被错分。Per-generator 差异大（Mistral-7B: 0.633 vs Pythia-2.8B: 0.724）。5-class F1 仅 0.50。标题和 framing 与实际性能水平之间的 gap 可能让审稿人质疑论文的诚实度。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1 [warning] Temperature sensitivity 严重限制通用性**\n- t=0.9 时 Pythia-2.8B 下降 26pp，Qwen3-1.7B 下降 18.5pp。DDR 作为 \"property of recursive generation\" 的声明未充分限定 temperature 条件依赖性。\n\n**R1-W2 [warning] 仅限 base models 极大限制实际应用价值**\n- 方法对 instruction-tuned / RLHF models 无效。建议在 abstract 或 introduction 早期明确 scope restriction。\n\n**R1-W3 [warning] Gen-0 seed sharing 导致 3-class 结果系统性膨胀**\n- Table 1 和 Table 2 仍突出显示 3-class F1，gen-0 near-perfect 分类（F1 ≈ 0.94）系统性抬高这些数字。读者可能误读。\n\n**R1-W4 [warning] XGBoost 超参数缺少 tuning 说明和 sensitivity 分析**\n- est=200, depth=6, lr=0.1 选择未说明来源。depth=6 with 7 features 可能过拟合。\n\n**R1-W5 [warning] Cross-reference model 实验（spread ≤ 0.013）的声明过强**\n- 仅说明 features 对 reference model 选择鲁棒，不直接支持 \"DDR 是递归生成的内在属性\"。这是两个不同声明。\n\n**R1-W6 [warning] Depth 2-4 合并显著限制 \"depth fingerprinting\" 声明**\n- 方法只能区分 \"人写的 / 第一代 / 更多代\"，更接近 provenance classification 而非 depth fingerprinting。\n\n### Reviewer 1 的 Overall Assessment\n- Overall: 3.0 (Findings)\n- Soundness: 3/5, Excitement: 3/5, Reproducibility: 3.5/5\n- 置信度: 4/5\n- 一句话：问题定义新颖、实验设计系统、统计分析规范，但核心性能有限、DDR 框架论证不充分、baseline 实际优于所提方法、仅适用于 base models\n\n---\n\n请对以上每个 Must-Fix (R1-N1, R1-N2, R1-N3) 和 Should-Fix (R1-W1 到 R1-W6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-18T10:28:11.311777+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1557
}
```

</details>

---


### Assistant

_source line 1134 · 2026-05-18T10:28:14.065722+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 106

## Round 106

2 recorded events


### User

_source line 1135 · 2026-05-18T10:28:16.732617+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

报告核心结论：

- **Overall: 3.0 (Findings)**，置信度 4/5
- **3 个 Must-Fix**：DDR 阈值论证不足（N1）、baseline 实际优于所提方法但 framing 不诚实（N2）、F1=0.694 与 "Fingerprinting" title 之间的落差（N3）
- **6 个 Should-Fix**：temperature sensitivity（W1）、仅限 base models（W2）、gen-0 seed sharing 膨胀 3-class 数字（W3）、XGBoost 超参数无 sensitivity analysis（W4）、cross-reference 声明过强（W5）、depth 合并限制实际分辨率（W6）
- **主要优势**：问题定义新颖、LOGO 实验设计严谨、统计方法规范、Limitations 诚实、ablation 丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1136 · 2026-05-18T10:28:21.986850+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1137 · 2026-05-18T10:29:21.916168+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 问题

### [AGREE] R2-N1: 方法论新颖性不足

同意 R2 的判断。7 个特征均为标准统计量（entropy 变体是 NLL 分布的基本矩/分位数，TTR/hapax ratio 是经典 stylometry 指标），XGBoost 是 off-the-shelf 分类器，方法层面没有技术创新。

不过我要补充一个 nuance：本文的贡献定位更接近 **empirical discovery**（发现 recursive generation chain 存在可检测的 depth signal）而非 **method innovation**。Section 1 的 contribution list 也确实以 "characterizing DDR" 和 "demonstrating feasibility" 为主。问题在于论文在某些地方的 framing（如 "DDR framework"、"Depth Fingerprinting"）暗示了比实际更高的方法论贡献。如果作者将贡献准确定位为 "empirical study + feasibility demonstration"，这个问题会大幅缓解。

同时，R2 指出 "baseline 都是 binary detection 方法，并非为 depth classification 设计的" 这一点值得强调。由于不存在 prior depth-classification methods，baseline 对比天然受限。但这也反过来说明这个方向确实是新的。

**结论**: 方法新颖性确实不足，但 **问题定义的新颖性** 有一定价值。关键是 framing 是否匹配实际贡献。

---

### [AGREE] R2-N2: Base-model-only 约束严重限制实际影响力

完全同意。这是本文最致命的实际限制。

我在 W2 中也指出了相同问题。OLMo-Instruct LOGO F1 = 0.338 不仅接近 random baseline（0.33），且论文在 Limitations（page 9）中进一步承认 "instruction tuning substantially weakens the signal"，这意味着 DDR 现象本身可能是 **base model 特有的 artifact**，而非 recursive generation 的 universal property。

论文的辩护 "instruction tuning introduces confounds (length regulation, format constraints, safety-driven shaping)" 不够有力，因为：
1. 如果 instruction tuning 的 "confounds" 足以完全消除 depth signal，那 depth signal 可能本身就不够 robust。
2. 现实中 recursive generation 更可能发生在 instruction-tuned models 上（用户用 ChatGPT/Claude 生成文本再喂给 ChatGPT/Claude），base model 的 recursive chain 是人为构造的实验设定而非自然场景。

**结论**: 同意 R2。论文应更早、更明确地声明 scope restriction，且需要讨论 base-model-only 结果是否可外推。

---

### [REBUT] R2-N3: DDR 相对于 model collapse 文献的增量贡献

部分不同意 R2 的判断。R2 认为 DDR 仅是 "naming existing phenomena"，但忽略了几个区别：

1. **机制不同**: Model collapse 文献（Shumailov et al., 2024; Alemohammad et al., 2024）研究的是 **retraining on synthetic data** 导致的分布退化，涉及模型参数更新。本文的 recursive generation chain 是 **repeated prompting without retraining**，模型参数固定不变。在固定模型下仅通过 iterative prompting 就能产生可检测的 distributional shift，这并非 model collapse 文献的直接推论。Section 5（Discussion, page 8）明确指出 "DDR is distinct from model collapse"，且给出了关键区别："iterative-chain drift occurs with fixed parameters, is fully reversible, and leaves distributional shape near-stationary (Cohen's d < 0.10)." Model collapse 涉及不可逆的参数退化，DDR 是可逆的分布偏移。

2. **Shape stability 是非 trivial 发现**: R2 称 "near-stationary features 可从 softmax 分布数学性质推导"，但没有给出具体推导。如果 recursive generation 仅是概率分布收缩，entropy_max、tail_decay 也应该 drift。论文的实验发现是 entropy_max 和 tail_decay 几乎不变（|ρ| < 0.10, d < 0.06），而 entropy_mean 和 TTR 大幅 drift。这种 "location shift with shape stability" 的分离并非先验可预期的。

3. **然而**，R2 的核心批评——DDR 三分法是否提供了足够的 **分析工具价值**——仍然成立。如我在 N1 中指出的，以 7 个特征的经验观察建立 "framework" 确实 overclaiming。DDR 更适合定位为 empirical finding 而非 analytical framework。

**结论**: 部分反驳。DDR 与 model collapse 有实质区别（机制、可逆性、shape stability），不仅仅是 "naming existing phenomena"。但 R2 关于 DDR 的 analytical contribution 有限的判断是对的——它是一个有价值的 empirical observation，而非 general framework。建议作者在修改中明确与 model collapse 的机制区别，同时降低 "framework" 声明。

---

## Should-Fix 问题

### [AGREE] R2-W1: Depth signal 在 gen-2+ 后迅速退化

完全同意。我在 W6 中提出了相同观点。5-class F1 = 0.50，gen-2/gen-3 per-class F1 = 0.259（Appendix D, page 14），说明方法无法提供标题所暗示的 fine-grained depth resolution。"Depth Fingerprinting" 标题应修改。

---

### [REBUT] R2-W2: Reference model dependency 讨论不充分

部分不同意。论文在 Appendix R（Table 21, page 20 附近）测试了 cross-family reference models（OLMo-2-1B、Qwen3-0.6B 替代 Pythia-410M），LOGO F1 spread ≤ 0.013，说明 NLL 特征对 reference model choice 有相当的鲁棒性。这已经是 reasonable 的 robustness check。

然而 R2 关于 cross-domain 退化（3-class F1 降至 0.622-0.634）的担忧是合理的。但这更多是 domain shift 问题而非 reference model dependency 问题。两者应分开讨论。

**结论**: Reference model robustness 已有合理验证；cross-domain 泛化是独立问题，R2 将两者混为一谈。但 "不知道生成器家族时如何选择 reference model" 确实是实际部署的 open question，应在 Discussion 或 Limitations 中讨论。

---

### [AGREE] R2-W3: Downstream utility 结果反而弱化论文动机

同意。我在 Q3 中也提出了相同问题。Appendix L 的 TOST equivalence 结果（depth-aware 与 random subsampling 在 perplexity 上 indistinguishable）直接削弱了 Introduction 中以 data curation 为动机的叙事。论文需要重新考虑 depth classification 的 primary use case：如果不是 downstream performance，那更合理的应用场景可能是 **audit/provenance tracking**（"这段文本经过了几轮 LLM 处理？"）而非 data quality filtering。建议作者调整动机叙事以匹配实际结果。

---

### [AGREE] R2-W4: Stylometry 引用覆盖不足

同意但认为 severity 较低。TTR 和 hapax ratio 是 2/7 的核心特征，仅引 3 篇 survey 确实不够。MATTR (Covington & McFall, 2010)、HD-D (McCarthy & Jarvis, 2010) 是 TTR 的已知改进版本，论文未讨论为何选择原始 TTR 而非这些变体。这不影响接收决定但会被 area chair 注意到。

---

### [AGREE] R2-W5: Data contamination / provenance 文献线缺失

同意。论文以 data provenance 为应用动机（Introduction page 1-2, Section 6 Conclusion），但 Related Work 完全没有覆盖 data contamination detection（如 Oren et al., 2024 "Proving Test Set Contamination in Black Box Language Models"; Golchin & Surdeanu, 2024）和 data provenance tracking systems。这是 Related Work 的明显空缺，尤其是当论文自己声称这些是应用场景时。

---

## 综合意见

与 R2 的总体评分一致：**3.0 (Findings)**。

两位 Reviewer 的核心共识：
1. **问题定义新颖有价值**（depth classification 作为新方向）
2. **DDR 是 empirical observation 而非 general framework**（overclaiming 需修正）
3. **Base-model-only 是致命实际限制**（R2-N2, R1-W2）
4. **Binary F1 = 0.694 性能有限**（R1-N3, R2-W1）
5. **Baseline 对比 framing 需要更诚实**（R1-N2）

两位 Reviewer 分歧点：
- R2-N3：我认为 DDR 与 model collapse 有实质机制区别，不是简单的 "naming existing phenomena"，但同意 analytical contribution 有限。
- R2-W2：Reference model robustness 已有合理测试（spread ≤ 0.013），R2 的担忧更多是 cross-domain 泛化问题而非 reference model dependency。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1138 · 2026-05-18T10:29:28.974751+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1139 · 2026-05-18T10:29:33.680231+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

对 R2 的 8 条意见，我的回应分布：
- **5 条 AGREE**: N1（方法新颖性不足）、N2（base-model-only 限制）、W1（depth signal 退化）、W3（downstream utility 弱化动机）、W4（stylometry 引用不足）、W5（contamination/provenance 文献缺失）
- **2 条 REBUT**: N3（DDR 与 model collapse 有实质机制区别，不是 naming existing phenomena）、W2（reference model robustness 已有合理验证，R2 混淆了 reference model dependency 与 cross-domain 泛化）

核心共识：Overall 3.0 (Findings)，问题定义新颖但方法贡献有限、适用范围过窄。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1140 · 2026-05-18T10:29:38.461712+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 109

## Round 109

10 recorded events


### User

_source line 1141 · 2026-05-18T10:31:30.696331+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 的逐条评估

---

### Must-Fix 问题

**[AGREE] R1-N1: DDR 三分法阈值论证不足，"framework" 定位过度**

同意核心论点。我在自己的 N3 中也指出 DDR 三分法更像经验观察而非理论贡献。R1 提出的具体问题都成立：

1. **N=7 建 framework 统计不够**：7 个特征分成 3/1/3，intermediate 类只有一个成员（entropy_std），这更像是 ad hoc 分组而非 robust partition。如果增加或更换特征，三分法是否仍成立？论文未讨论。
2. **ρ 阈值缺乏理论依据**：虽然论文在 Appendix M (p.20) 提供了 margin sensitivity analysis（TOST 跨多个 equivalence margins），这是 R1 可能未注意到的一个缓解因素，但 0.60/0.10 的具体切分点确实缺少形式化论证。
3. **Levene test vs. equivalence testing**：R1 指出 Levene test 拒绝等方差但论文用 CV shift 辩护 "near-stationary"，这是合理的方法论批评。拒绝零假设（方差相等）不等于接受替代假设（差异大到有实际意义）。论文确实在 Appendix M 使用了 TOST，但未将其直接应用于 near-stationary 特征的分类判定。

**补充**：论文 §4.2 (p.7) 中 Cohen's d 用于量化效应量是恰当的（d < 0.10 for near-stationary, d > 0.60 for drifting），但 R1 正确指出 Cohen's d 的 small/medium/large benchmark 原本针对两组均值比较，直接套用于 Spearman ρ 需要更多论证。

---

**[REBUT] R1-N2: Baseline 对比框架不公平：4-detector ensemble 在所有指标上优于所提方法**

R1 的核心数据引用存在错误，导致对 performance gap 的评估过大。

1. **数据纠正**：R1 称 "3-cl F1 = 0.785 vs 7-feature: 0.724（差 6.1pp）"。但论文 p.8 正文明确写道：*"Multi-detector ensembles achieve higher 3-class F1 (0.785 vs. 0.774, +2.1 pp)"*。R1 的 0.724 可能混淆了 Table 1 的 leak-free binary F1 (0.694) 与 Table 2 的 3-class F1。实际 3-class F1 差距为 ~2.1pp，不是 6.1pp。
2. **论文的 framing 并未声称 competitive advantage**：p.8 原文 "To contextualize depth discrimination ability rather than claim competitive advantage over detection-optimized methods, we repose four single-score detection methods..." 论文明确说不是在声称优于这些方法，而是做 contextualization。R1 将此解读为论文在声称优势，与原文不符。
3. **效率差异需要在 scale 下评估**：R1 认为 13ms 差异可忽略，但论文报告的是 2.4× inference time 和 3.2× GPU memory。对于大规模 data curation pipeline（处理数百万文档），2.4× 的差距意味着从例如 11 小时变为 27 小时。更重要的是 3.2× GPU memory 差距意味着 4-detector ensemble 需要同时加载多个检测模型（论文 Table 2 caption: "4-det ensemble: two models, 1.4B params (2,868 MB)" vs "7-feature: one model (495 MB)"），这在资源受限环境下有实际意义。

**但我部分同意 R1 的潜在关切**：即使 gap 只有 2.1pp，4-detector ensemble 确实在 3-class F1 上优于提出的方法，论文应更直接地承认这一点，而不是通过效率论证来模糊性能差距。

---

**[AGREE] R1-N3: Binary F1 = 0.694 的性能水平与 "fingerprinting" 声明之间存在落差**

完全同意。我在 W1 中也提出了相同的问题。补充几点：

1. **"Fingerprinting" 的语义期望**：R1 准确指出，在安全/取证领域，fingerprinting 意味着高可靠的唯一识别。Leak-free binary F1 = 0.694（gen-1 vs gen-2+）意味着约 30% 的分类错误率。从 confusion matrix (Figure 5, p.22) 可以看到，gen-1 ↔ gen-2+ 是主要混淆方向（gen-1 recall 75.0%, gen-2+ recall 73.7%），这与 "fingerprinting" 的高精度内涵不符。
2. **Per-generator 差异加剧问题**：Figure 6 (p.22) 显示 per-generator 3-class F1 从 0.633 (Mistral-7B) 到 0.724 (Pythia-2.8B)，跨度大。这意味着方法的可靠性高度依赖于未知的生成器身份，进一步削弱 "fingerprinting" 的可靠性声明。
3. **5-class F1 = 0.50**（Appendix D, Table 5, p.14）进一步说明 fine-grained depth 分辨能力有限。

**建议与 R1 一致**：将标题中 "Fingerprinting" 改为更准确的措辞，如 "Depth Profiling" 或 "Depth Classification"。Conclusion 中 "Three classes represent the practical resolution ceiling" (p.8) 的诚实表述与标题形成矛盾。

---

### Should-Fix 问题

**[AGREE] R1-W1: Temperature sensitivity 严重限制通用性**

同意。我在 M1 中也标记了 temperature 覆盖不足。R1 提供了更具体的数据：t=0.9 时 Pythia-2.8B 下降 26pp、Qwen3-1.7B 下降 18.5pp。从 Appendix H (p.16) 和 Appendix O (p.24) 的数据来看，temperature mismatch 确实会显著降低性能，且不同生成器对 temperature 变化的敏感度差异极大（Qwen3-1.7B 在 cross-temperature 条件下 3-class F1 从 0.810 降至 0.418，而 Pythia-2.8B 保持 0.804）。DDR 声称是 "property of recursive generation" 需要更明确地限定 temperature/sampling 条件。

---

**[AGREE] R1-W2: 仅限 base models 极大限制实际应用价值**

完全同意。这与我的 N2 一致，我将其列为 Must-Fix。R1 将其列为 Should-Fix，我认为这实际上应该升级为 Must-Fix，因为 instruction-tuned model 上 F1 降至 0.338（p.9 Limitations）意味着方法在最常见的实际场景中几乎失效。R1 的建议（在 abstract/introduction 早期明确 scope restriction）是合理且最低限度的修改。

---

**[REBUT] R1-W3: Gen-0 seed sharing 导致 3-class 结果系统性膨胀**

部分不同意 R1 的严重程度评估。

1. **论文已明确处理此问题**：p.6 明确指出 "binary F1 (gen-1 vs. gen-2+) may carry upward bias from gen-0 seed sharing across generators" 并因此报告 leak-free binary F1 (gen-1 vs. gen-2+)。这说明作者意识到并正面处理了该问题。
2. **Gen-0 near-perfect classification 是合理的**：Gen-0 是人类撰写的 Wikipedia 原文，与 LLM 生成的 gen-1/gen-2+ 有天然的分布差异。即使不共享 seed，gen-0 的分类精度也应该很高（这就是 binary real-vs-synthetic detection 已经做得很好的原因）。因此 gen-0 的高 F1 并不完全是 seed sharing 的"膨胀"——部分是任务本身的固有可区分性。
3. **但 R1 对 Table 1/2 展示方式的批评有一定道理**：论文在正文中同时报告 3-class F1 (0.762) 和 leak-free binary F1 (0.694)，但标题数字（Abstract 中 "binary F1 = 0.694"）确实选择了更保守的数字。读者可能在 Table 1/2 中先看到更高的 3-class F1 而产生乐观印象。

**结论**：问题存在但论文已有缓解措施。建议在 Table 1/2 的 caption 中更突出地提醒 gen-0 的影响，但不需要作为 Should-Fix。

---

**[AGREE] R1-W4: XGBoost 超参数缺少 tuning 说明和 sensitivity 分析**

同意。论文 p.6 仅提供了 "estimators=200, depth=6, lr=0.1"，未说明选择来源。但补充一点：论文在 Appendix H (Classifier Sensitivity, p.16) 评估了替代分类器（Logistic Regression, Random Forest），结果差异不大（"Both tree-based classifiers achieve LOGO F1 ≥ 0.79, and even a linear model reaches 0.725"）。这在一定程度上说明结果对分类器选择不太敏感，间接缓解了超参数 sensitivity 的担忧。但 XGBoost 本身的超参数 sensitivity 仍未被讨论。

---

**[AGREE] R1-W5: Cross-reference model 实验的声明过强**

同意。R1 精确地识别了逻辑跳跃："features 对 reference model 选择鲁棒" ≠ "DDR 是递归生成的内在属性"。论文 p.7 的 "Cross-family reference models" 分析（spread ≤ 0.013 across reference models）仅说明 NLL features 的 relative ranking 在不同 reference model 下保持一致，不能直接推出 DDR 是生成过程的 intrinsic property。后者需要理论分析或更广泛的实验证据（例如不同 domain、不同 generation paradigm 下 DDR 是否仍然成立）。

---

**[AGREE] R1-W6: Depth 2-4 合并显著限制 "depth fingerprinting" 声明**

完全同意。这与我的 W1 完全一致。5-class F1 = 0.50 (Appendix D) 且 gen-2/gen-3 各自仅 0.259 F1，说明方法本质上是 "3-class provenance classification"（human / first-gen / multi-gen）而非 "depth fingerprinting"。论文 Conclusion (p.8) 中 "Three classes represent the practical resolution ceiling" 与标题的 tension 已被两位 reviewer 独立指出，应该修改。

---

### 综合评估

R1 的审稿整体严谨，多数批评有理有据。主要分歧在 R1-N2：R1 的数据引用有误（0.724 vs 实际约 0.764-0.774），导致对 performance gap 的评估过大。论文明确说了不是在声称 competitive advantage，而是做 contextualization。

两位 reviewer 的共识点：
1. **DDR 作为 "framework" 的定位过强**（R1-N1, R2-N3）
2. **"Fingerprinting" 标题与实际能力不匹配**（R1-N3, R2-W1）
3. **Base-model-only 约束是核心限制**（R1-W2, R2-N2）
4. **Depth 2+ 合并限制了 framing**（R1-W6, R2-W1）
5. **方法论新颖性有限**（R2-N1——R1 未直接提及此点，但 R1-N3 中 "实际性能不足" 的批评间接相关）

**我维持 Overall 3.0 (Findings) 的评分**。R1 也给出 3.0。两位 reviewer 独立收敛到相同评分和相似的核心关切，增强了评估的可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-18T10:32:43.985094+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-18T10:32:44.035723+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-18T10:32:49.360458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-18T10:32:49.411246+00:00_

1	
2	# Round 18 submission — updated by Research Director 2026-05-18
3	# R17 fixes applied: MF2 tri-partition, MF3 Intro restructure, SF1-SF5, N1-N5
4	
5	# === Issues addressed in R18 ===
6	
7	- id: "R13-MF1"
8	  summary: "正文超 8 页限制"
9	  category: format
10	  severity: critical
11	  status: resolved
12	  first_raised_round: 13
13	  last_seen_round: 17
14	  mentions:
15	    - {round: 14, reviewers: "R1,R2", note: "8 pages confirmed R14."}
16	    - {round: 17, reviewers: "R1,R2", note: "Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。"}
17	    - {round: 18, reviewers: "Director", note: "Discussion compressed, Conclusion on page 8. Verified with pdftotext."}
18	  action_items:
19	    - {round: 13, action: "Compress to 8 pages", assigned_to: "Director", status: "done"}
20	    - {round: 17, action: "压缩 Discussion/Results 约 0.2 页", assigned_to: "Director", status: "done"}
21	  resolution: "Discussion compressed. Conclusion fits on page 8. Body = 8 pages verified."
22	  resolution_round: 18
23	
24	- id: "R14-W4"
25	  summary: "Baseline comparison fairness — repurposed binary detectors"
26	  category: experiment
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 14
30	  last_seen_round: 17
31	  mentions:
32	    - {round: 14, reviewers: "R1,R2", note: "Detectors not designed for ordinal. Frame as 'repurposed baselines'."}
33	    - {round: 15, reviewers: "R1,R2", note: "Partial consensus: framework fair, threshold-based binary comparison nice-to-have."}
34	    - {round: 16, reviewers: "R1,R2", note: "R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled."}
35	    - {round: 17, reviewers: "R1,R2", note: "两位 Reviewer 均 AGREE。§4.3 开头加声明。"}
36	  action_items:
37	    - {round: 14, action: "Method §3.4 states 'repurposed as depth predictors'", assigned_to: "Agent", status: "done"}
38	    - {round: 17, action: "§4.3 contextualization statement", assigned_to: "Director", status: "done"}
39	  resolution: "§4.3 opens with 'To contextualize depth discr
…[truncated 3380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-18T10:36:26.554945+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# Round 18 review — Review Director consolidated 2026-05-18\n# R18 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)\n# Both reviewers: 3.0 (Findings). Cross-responses completed.\n\n# === New issues raised in R18 review ===\n\n- id: \"R18-N1\"\n  summary: \"DDR 'framework' overclaim — 阈值论证不足, N=7 不足以建立 framework\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；Cohen d benchmarks 针对效应量非 Spearman ρ；N=7 特征分 3/1/3 不具统计说服力；Levene test 拒绝等方差但用 CV shift 辩护需 equivalence testing。R2 AGREE，补充 Appendix M TOST 存在但未直接用于 near-stationary 分类判定。两位共识：DDR 应定位为 empirical observation 非 general framework。\"}\n  action_items:\n    - {round: 18, action: \"对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N2\"\n  summary: \"'Fingerprinting' 标题与 3-class 实际能力不匹配 (binary F1=0.694, 5-class F1=0.50)\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N3：fingerprinting 在安全/取证领域意味着高可靠性，F1=0.694 约 30% 错分率不匹配。R2 AGREE，补充 per-generator F1 跨度 0.633-0.724，5-class F1=0.50 gen-2/3 仅 0.259。Conclusion 'three classes = practical ceiling' 与标题矛盾。建议改为 Depth Profiling/Classification。\"}\n  action_items:\n    - {round: 18, action: \"将标题中 'Fingerprinting' 改为更准确的措辞（Depth Classification/Profiling/Detection）；在 Abstract 明确 3-class 粒度限制\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N3\"\n  summary: \"方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-N1：7 个特征均为标准统计量（NLL 基本矩/分位数 + 经典 stylometry），XGBoost 无架构改进，baseline 都是 binary detection 非 depth classification。R1 AGREE，补充贡献定位应为 empirical discovery 非 method innovation，问题定义的新颖性有一定价值。两位共识：需更明确定位为 empirical study + feasibility demonstration。\"}\n  action_items:\n    - {round: 18, action: \"调整贡献声明：明确定位为 empirical study / phenomenon paper，降低方法创新声称；考虑在 §1 contribution list 中区分 'task formulation' 和 'empirical finding' 贡献\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Baseline 4-det ensemble 在 3-class F1 上优于所提方法 (0.785 vs 0.774)，framing 需更直接承认\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N2 原判 critical（引用 gap 6.1pp），R2 REBUT 纠正数据错误（实际 gap 2.1pp）。R2 指出论文明确说 'contextualize not claim advantage'，且 2.4× inference + 3.2× GPU memory 在大规模场景有意义。但两位均同意论文应更直接承认 4-det ensemble 在准确性上更优。降为 warning。\"}\n  action_items:\n    - {round: 18, action: \"§4.3 更直接承认 4-det ensemble 在 3-class F1 上优于 7-feature；效率论证改为 large-scale batch processing 场景而非泛泛的 '2.4×'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Temperature sensitivity 未充分限定 DDR 普遍性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W1：t=0.9 时 Pythia -26pp, Qwen -18.5pp。DDR 'property of recursive generation' 声明需限定 temperature 条件。R2 AGREE，补充 cross-temperature 退化数据（Qwen F1 0.810→0.418）。\"}\n  action_items:\n    - {round: 18, action: \"在 Abstract 和所有提及 DDR 普遍性处加 temperature/sampling 条件限定（如 'under standard decoding regimes (t≤0.7)'）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W3\"\n  summary: \"XGBoost 超参数选择未说明来源，缺 sensitivity analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W4：est=200, depth=6, lr=0.1 选择来源不明。R2 AGREE 但指出 Appendix H classifier sensitivity（LR, RF 等替代分类器结果差异不大）部分缓解。降为 info。\"}\n  action_items:\n    - {round: 18, action: \"报告超参数选择来源（default/grid search/pilot）；可选做 depth={3,4,5,6,8} sensitivity\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W4\"\n  summary: \"Cross-reference model 实验声明过强：'robust to reference choice' ≠ 'DDR is intrinsic property'\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W5：spread ≤0.013 仅说明 features 对 reference model 选择鲁棒，不直接支持 'DDR 是递归生成内在属性'。R2 AGREE。两个不同声明，逻辑跳跃。\"}\n  action_items:\n    - {round: 18, action: \"将 'DDR is a property of recursive generation' 改为 'feature computation is robust to reference model choice'；intrinsic property 声明需独立论证\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W5\"\n  summary: \"Stylometry 引用覆盖不足 + data contamination/provenance 文献线缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-W4：TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体讨论。R2-W5：以 data provenance 为动机但缺 contamination detection 文献（Oren 2024, Golchin 2024 等）。R1 均 AGREE。\"}\n  action_items:\n    - {round: 18, action: \"§2.3 增加 TTR 变体文献（McCarthy & Jarvis 2010, Covington & McFall 2010）；§2.4 增加 data provenance/contamination paragraph\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Existing issues updated with R18 review mentions ===\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Intro still opens with instruct-model evidence.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Introduction 动机与方法适用范围脱节。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF3: Intro restructured. 7-17% moved from position 2 to supporting evidence after binary detection critique. Dynamical system framing leads. Base-model restriction at L15 with explicit justification.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: 两位 Reviewer 均再次标记。R1-W2 + R2-N2（升为 critical）。OLMo-Instruct F1=0.338 接近 random。Intro restructure 有改善但核心 gap 仍存在：Abstract 未提及 base-model restriction，读者可能误以为方法适用于所有 LLM。需在 Abstract 和 Intro 更早声明 scope。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"MF3: move 7-17% to supporting evidence position\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 18, action: \"Abstract 中明确 base-model restriction；Intro 中更早声明 scope；正文纳入 instruction-tuned 实验结果（非仅 Limitations 一句话提及）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction insufficient — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升为 Must-Fix（增量贡献不充分），R1 REBUT。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF1: §2.2 (iii) replaced with conceptual framing. SF2: contrast language strengthened. Intro contribution list uses tri-partition language.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2-N3 再次标记 DDR 增量不清晰。R1 REBUT（机制有实质区别：fixed params, reversible, shape stability）但同意 analytical contribution 有限。部分改善——§2.2 区分论述存在且有效，但 DDR 整体定位需从 framework 降级为 empirical observation（与 R18-N1 关联）。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded: detailed 3-way comparison.\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Strengthen §2.2 positioning + Intro unique contributions\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF3 restructure improves flow: binary detection insufficient → qualitative differences exist → 'This is not hypothetical: 7-17%' → depth classification formulation.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2-W3 指出 downstream utility 实验反而弱化动机（TOST 确认 depth-aware 与 random subsampling 等价）。R1 AGREE。如果 depth 信息不影响 downstream performance，'why depth matters' 需要重新论证——从 data quality filtering 转为 audit/provenance tracking。\"}\n  action_items:\n    - {round: 17, action: \"Intro 补充 depth 信息价值论证\", assigned_to: \"Director\", status: \"in_progress\"}\n    - {round: 18, action: \"调整动机叙事：从 data curation/quality 转为 provenance transparency/audit；或找到更有说服力的应用场景\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升 Must-Fix，R1 降级 Should-Fix。Discussion 需扩展。\"}\n    - {round: 18, reviewers: \"Director\", note: \"§2.2 contrast strengthened ('In contrast, fully reversible... d<0.10'). Discussion already has DDR vs model collapse paragraph. Page limit prevents further expansion.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R1 cross-response REBUT R2-N3，认为机制有实质区别（fixed params, reversible, shape stability ≠ model collapse 的不可逆参数退化）。R2 接受机制区别但仍认为 analytical contribution 有限。§2.2 改善被 R1 认可（Strength 6: concurrent work positioning clear）。改善但未完全解决。\"}\n  action_items:\n    - {round: 17, action: \"Discussion DDR vs model collapse 区分加强\", assigned_to: \"Director\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 front-load, Figure 1 threshold, method.tex which-clause density, B/W hatching, Abstract params, Appendix consolidation.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Figure 1b 字体接近 7pt 下限。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2 确认写作质量中等偏上，AI 痕迹不明显，格式基本合规。Figure 字体 ≥7pt。R1 minor items: Abstract NLL 未展开, Figure 1 caption 缺 ρ 说明, Appendix 过多(18个)建议合并。\"}\n  action_items:\n    - {round: 16, action: \"Various minor fixes\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Previously resolved issues (unchanged) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"8 pages confirmed R14.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。\"}\n    - {round: 18, reviewers: \"Director\", note: \"Discussion compressed, Conclusion on page 8. Verified with pdftotext.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2 格式检查确认正文 ≤8 页 (Conclusion on p.8)。\"}\n  action_items:\n    - {round: 13, action: \"Compress to 8 pages\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 17, action: \"压缩 Discussion/Results 约 0.2 页\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Discussion compressed. Conclusion fits on page 8. Body = 8 pages verified.\"\n  resolution_round: 18\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness — repurposed binary detectors\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"Detectors not designed for ordinal. Frame as 'repurposed baselines'.\"}\n    - {round: 15, reviewers: \"R1,R2\", note: \"Partial consensus: framework fair, threshold-based binary comparison nice-to-have.\"}\n    - {round: 16, reviewers: \"R1,R2\", note: \"R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。§4.3 开头加声明。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: §4.3 contextualization framing acknowledged by R2 ('论文明确说不是在声称优于这些方法')。但 R18-W1 提出新问题：需更直接承认 4-det ensemble 在 3-class F1 上更优。\"}\n  action_items:\n    - {round: 14, action: \"Method §3.4 states 'repurposed as depth predictors'\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"§4.3 contextualization statement\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"§4.3 opens with 'To contextualize depth discrimination ability rather than claim competitive advantage over detection-optimized methods'. Applied in R16/R17.\"\n  resolution_round: 18\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致 — entropy_std/min 不符合 drifting/stationary 划分\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"entropy_std (d=0.55) 和 entropy_min (pooled |ρ|=0.40) 不符合二分框架。建议三分法。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF2: Full tri-partition (3/1/3) applied across abstract, intro, method, results, discussion, conclusion, related_work, appendices.\"}\n  action_items:\n    - {round: 17, action: \"三分法 across all files\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) consistently applied across all 8+ files.\"\n  resolution_round: 18\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高（~8 个数值在 200 词内）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"建议保留 2-3 个关键数字。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF4: Reduced to 4 key numbers.\"}\n  resolution: \"Abstract trimmed from ~8 to 4 essential numbers.\"\n  resolution_round: 18\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"缺少候选讨论。LOFO 是事后验证非先验选择。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF5: Added justification in §3.3.\"}\n  resolution: \"Feature selection rationale added: interpretable distributional statistics enable DDR tri-partition analysis.\"\n  resolution_round: 18\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B 数据点\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R1 升 Must-Fix，R2 REBUT（趋势非单调）。共识：gap 存在。\"}\n  resolution: \"Acknowledged in Limitations. Compute constraints prevent >8B experiments.\"\n  resolution_round: 18\n\n- id: \"R17-W4-old\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证 (deprecated — see R17-W4)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"'generation depth' vs 'recursive generation depth' 交替使用。'Fingerprinting' 未定义。\"}\n    - {round: 18, reviewers: \"Director\", note: \"N2: 'depth fingerprinting' defined in Intro L9.\"}\n  resolution: \"Fingerprinting defined in Intro. Terminology consistent.\"\n  resolution_round: 18\n\n- id: \"R17-M2\"\n  summary: \"Stylometry 引用偏少 + 缺少 detection survey (Tang et al. 2024)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Stylometry 仅 2 篇经典。缺 Tang et al. 2024 CACM。\"}\n    - {round: 18, reviewers: \"Director\", note: \"N5: Tang et al. 2024 added. Neal et al. 2017 added.\"}\n  resolution: \"Tang et al. 2024 and Neal et al. 2017 added.\"\n  resolution_round: 18\n\n- id: \"R13-SF7\"\n  summary: \"Model scale limited (0.6B-8B), no >10B model\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"Acknowledged limitation. Wont_fix due to compute constraints.\"\n  resolution_round: 14\n\n- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 13\n  resolution: \"TOST demoted from Contribution to supporting analysis.\"\n  resolution_round: 13\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline + gen-1/gen-2+ topic confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 15\n  resolution: \"Two independent seed controls converge: demeaning F1=0.701, disjoint-seed F1=0.680.\"\n  resolution_round: 15\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 16\n  resolution: \"Cohen's d computed and reported.\"\n  resolution_round: 16\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 14\n  resolution: \"Phenomenon paper positioning.\"\n  resolution_round: 13\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"LOGO binary F1=0.694 leads in Abstract.\"\n  resolution_round: 14\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"Contribution 3 deleted R12.\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Title changed. Discussion explains bottleneck.\"\n  resolution_round: 13\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"Downstream moved to Appendix. Null result honestly reported.\"\n  resolution_round: 15\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 15\n  resolution: \"Temperature data corrected. Dual-model numbers reported.\"\n  resolution_round: 15\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Title changed.\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Same-family affinity noted. Cross-ref spread ≤0.013.\"\n  resolution_round: 16\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms; contribution claims need adjustment\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 15\n  resolution: \"Contributions split: task+DDR=science, 7-feature=efficient implementation.\"\n  resolution_round: 15\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"§3.4 explains all subsets.\"\n  resolution_round: 13\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Caption states identical configuration.\"\n  resolution_round: 13\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification discussion insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Discussion explains gen-1/gen-2+ boundary bottleneck.\"\n  resolution_round: 13\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Restructured to 3 paragraphs R12.\"\n  resolution_round: 12\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Footnote added in §3.3.\"\n  resolution_round: 13\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification added in method.tex.\"\n  resolution_round: 13\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"6-gen subset note added.\"\n  resolution_round: 13\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Six-fold magnitude gap framing + threshold sensitivity.\"\n  resolution_round: 13\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Switched to PDF.\"\n  resolution_round: 13\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification rewritten.\"\n  resolution_round: 13\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Confirmed correct.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Bonferroni correction scope not specified\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Scope specified in method.tex.\"\n  resolution_round: 13\n\n- id: \"R12-M2\"\n  summary: \"Pythia-1B vs 2.8B crossover undiscussed\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Crossover explanation added.\"\n  resolution_round: 13\n\n- id: \"R12-M3\"\n  summary: \"Generation failure rate causes not reported\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"2746 chain breaks reported.\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Some bib entries missing pages/volume\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Fixed.\"\n  resolution_round: 13\n\n- id: \"R13-M1\"\n  summary: \"Appendix D 'Notably' AI writing marker\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Deleted and rewritten.\"\n  resolution_round: 13\n\n- id: \"R13-M5\"\n  summary: \"Figure 1 strip plot label area\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Confirmed acceptable.\"\n  resolution_round: 13\n\n- id: \"R13-RV1\"\n  summary: \"Instruct comparison uses different LOGO subsets\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Subset qualifiers added.\"\n  resolution_round: 13\n\n- id: \"R13-RV2\"\n  summary: \"Table 1 vs baselines F1 discrepancy\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Caption explains pooled vs macro-average.\"\n  resolution_round: 13\n\n- id: \"R13-RV3\"\n  summary: \"Instruct experiments missing registry\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Preliminary experiments predating registry.\"\n  resolution_round: 13\n\n- id: \"R14-W1\"\n  summary: \"Feature selection circular reasoning\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Circular claim removed.\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"DDR vs model collapse distinction weak\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Related Work §2.2 contrasts DDR vs model collapse.\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"Cross-domain evaluation confounded by temperature mismatch\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Acknowledged in Limitations.\"\n  resolution_round: 15\n\n- id: \"R14-W5\"\n  summary: \"Seed-sharing potential topic fingerprint confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Two independent seed controls confirm depth signal is not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R14-W6\"\n  summary: \"Missing references — stylometric systems, CORN loss\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"3 citations added.\"\n  resolution_round: 14\n\n- id: \"R14-W7\"\n  summary: \"AI writing style traces persist\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Comprehensive cleanup. R15 confirms clean.\"\n  resolution_round: 14\n\n- id: \"R15-N1\"\n  summary: \"Cross-model chains vs LOGO evaluation protocol incomparability\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Causal claim deleted. Protocol difference acknowledged.\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"Feature redundancy — effective dimensionality ~5\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Effective dimensionality ~5 acknowledged. TTR-hapax r=0.97.\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"DDR novelty positioning\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Intro distinguishes known drift vs novel structured decomposition.\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"Prompt type limitation not reflected in main results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Prompt-type sensitivity paragraph added to §4.2.\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"KS test cannot verify location/shape decomposition\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Decomposition rests on convergence of ρ, Levene, CV shift, and Cohen's d.\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"Disjoint-seed experiment lacks bootstrap CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Per-direction bootstrap CIs present.\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"gen-0 3-class F1 still appears prominently without leakage caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 1 dagger footnote + caption explicit leakage warning.\"\n  resolution_round: 16\n\n- id: \"R16-W3\"\n  summary: \"Table 1 vs Table 2 use different evaluation protocols\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 2 caption explains protocol difference.\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"5 orphan bib entries + bib title/author mismatches\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"5 orphans removed. Entries verified.\"\n  resolution_round: 16\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Phenomenon paper positioning.\"\n  resolution_round: 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# Round 18 review — Review Director consolidated 2026-05-18\n# R18 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)\n# Both reviewers: 3.0 (Findings). Cross-responses completed.\n\n# === New issues raised in R18 review ===\n\n- id: \"R18-N1\"\n  summary: \"DDR 'framework' overclaim — 阈值论证不足, N=7 不足以建立 framework\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；Cohen d benchmarks 针对效应量非 Spearman ρ；N=7 特征分 3/1/3 不具统计说服力；Levene test 拒绝等方差但用 CV shift 辩护需 equivalence testing。R2 AGREE，补充 Appendix M TOST 存在但未直接用于 near-stationary 分类判定。两位共识：DDR 应定位为 empirical observation 非 general framework。\"}\n  action_items:\n    - {round: 18, action: \"对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N2\"\n  summary: \"'Fingerprinting' 标题与 3-class 实际能力不匹配 (binary F1=0.694, 5-class F1=0.50)\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N3：fingerprinting 在安全/取证领域意味着高可靠性，F1=0.694 约 30% 错分率不匹配。R2 AGREE，补充 per-generator F1 跨度 0.633-0.724，5-class F1=0.50 gen-2/3 仅 0.259。Conclusion 'three classes = practical ceiling' 与标题矛盾。建议改为 Depth Profiling/Classification。\"}\n  action_items:\n    - {round: 18, action: \"将标题中 'Fingerprinting' 改为更准确的措辞（Depth Classification/Profiling/Detection）；在 Abstract 明确 3-class 粒度限制\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N3\"\n  summary: \"方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-N1：7 个特征均为标准统计量（NLL 基本矩/分位数 + 经典 stylometry），XGBoost 无架构改进，baseline 都是 binary detection 非 depth classification。R1 AGREE，补充贡献定位应为 empirical discovery 非 method innovation，问题定义的新颖性有一定价值。两位共识：需更明确定位为 empirical study + feasibility demonstration。\"}\n  action_items:\n    - {round: 18, action: \"调整贡献声明：明确定位为 empirical study / phenomenon paper，降低方法创新声称；考虑在 §1 contribution list 中区分 'task formulation' 和 'empirical finding' 贡献\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Baseline 4-det ensemble 在 3-class F1 上优于所提方法 (0.785 vs 0.774)，framing 需更直接承认\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N2 原判 critical（引用 gap 6.1pp），R2 REBUT 纠正数据错误（实际 gap 2.1pp）。R2 指出论文明确说 'contextualize not claim advantage'，且 2.4× inference + 3.2× GPU memory 在大规模场景有意义。但两位均同意论文应更直接承认 4-det ensemble 在准确性上更优。降为 warning。\"}\n  action_items:\n    - {round: 18, action: \"§4.3 更直接承认 4-det ensemble 在 3-class F1 上优于 7-feature；效率论证改为 large-scale batch processing 场景而非泛泛的 '2.4×'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Temperature sensitivity 未充分限定 DDR 普遍性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W1：t=0.9 时 Pythia -26pp, Qwen -18.5pp。DDR 'property of recursive generation' 声明需限定 temperature 条件。R2 AGREE，补充 cross-temperature 退化数据（Qwen F1 0.810→0.418）。\"}\n  action_items:\n    - {round: 18, action: \"在 Abstract 和所有提及 DDR 普遍性处加 temperature/sampling 条件限定（如 'under standard decoding regimes (t≤0.7)'）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W3\"\n  summary: \"XGBoost 超参数选择未说明来源，缺 sensitivity analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W4：est=200, depth=6, lr=0.1 选择来源不明。R2 AGREE 但指出 Appendix H classifier sensitivity（LR, RF 等替代分类器结果差异不大）部分缓解。降为 info。\"}\n  action_items:\n    - {round: 18, action: \"报告超参数选择来源（default/grid search/pilot）；可选做 depth={3,4,5,6,8} sensitivity\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W4\"\n  summary: \"Cross-reference model 实验声明过强：'robust to reference choice' ≠ 'DDR is intrinsic property'\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-W5：spread ≤0.013 仅说明 features 对 reference model 选择鲁棒，不直接支持 'DDR 是递归生成内在属性'。R2 AGREE。两个不同声明，逻辑跳跃。\"}\n  action_items:\n    - {round: 18, action: \"将 'DDR is a property of recursive generation' 改为 'feature computation is robust to reference model choice'；intrinsic property 声明需独立论证\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W5\"\n  summary: \"Stylometry 引用覆盖不足 + data contamination/provenance 文献线缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-W4：TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体讨论。R2-W5：以 data provenance 为动机但缺 contamination detection 文献（Oren 2024, Golchin 2024 等）。R1 均 AGREE。\"}\n  action_items:\n    - {round: 18, action: \"§2.3 增加 TTR 变体文献（McCarthy & Jarvis 2010, Covington & McFall 2010）；§2.4 增加 data provenance/contamination paragraph\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Existing issues updated with R18 review mentions ===\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Intro still opens with instruct-model evidence.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Introduction 动机与方法适用范围脱节。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF3: Intro restructured. 7-17% moved from position 2 to supporting evidence after binary detection critique. Dynamical system framing leads. Base-model restriction at L15 with explicit justification.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: 两位 Reviewer 均再次标记。R1-W2 + R2-N2（升为 critical）。OLMo-Instruct F1=0.338 接近 random。Intro restructure 有改善但核心 gap 仍存在：Abstract 未提及 base-model restriction，读者可能误以为方法适用于所有 LLM。需在 Abstract 和 Intro 更早声明 scope。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"MF3: move 7-17% to supporting evidence position\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 18, action: \"Abstract 中明确 base-model restriction；Intro 中更早声明 scope；正文纳入 instruction-tuned 实验结果（非仅 Limitations 一句话提及）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction insufficient — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升为 Must-Fix（增量贡献不充分），R1 REBUT。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF1: §2.2 (iii) replaced with conceptual framing. SF2: contrast language strengthened. Intro contribution list uses tri-partition language.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2-N3 再次标记 DDR 增量不清晰。R1 REBUT（机制有实质区别：fixed params, reversible, shape stability）但同意 analytical contribution 有限。部分改善——§2.2 区分论述存在且有效，但 DDR 整体定位需从 framework 降级为 empirical observation（与 R18-N1 关联）。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded: detailed 3-way comparison.\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Strengthen §2.2 positioning + Intro unique contributions\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF3 restructure improves flow: binary detection insufficient → qualitative differences exist → 'This is not hypothetical: 7-17%' → depth classification formulation.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2-W3 指出 downstream utility 实验反而弱化动机（TOST 确认 depth-aware 与 random subsampling 等价）。R1 AGREE。如果 depth 信息不影响 downstream performance，'why depth matters' 需要重新论证——从 data quality filtering 转为 audit/provenance tracking。\"}\n  action_items:\n    - {round: 17, action: \"Intro 补充 depth 信息价值论证\", assigned_to: \"Director\", status: \"in_progress\"}\n    - {round: 18, action: \"调整动机叙事：从 data curation/quality 转为 provenance transparency/audit；或找到更有说服力的应用场景\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升 Must-Fix，R1 降级 Should-Fix。Discussion 需扩展。\"}\n    - {round: 18, reviewers: \"Director\", note: \"§2.2 contrast strengthened ('In contrast, fully reversible... d<0.10'). Discussion already has DDR vs model collapse paragraph. Page limit prevents further expansion.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R1 cross-response REBUT R2-N3，认为机制有实质区别（fixed params, reversible, shape stability ≠ model collapse 的不可逆参数退化）。R2 接受机制区别但仍认为 analytical contribution 有限。§2.2 改善被 R1 认可（Strength 6: concurrent work positioning clear）。改善但未完全解决。\"}\n  action_items:\n    - {round: 17, action: \"Discussion DDR vs model collapse 区分加强\", assigned_to: \"Director\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 front-load, Figure 1 threshold, method.tex which-clause density, B/W hatching, Abstract params, Appendix consolidation.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Figure 1b 字体接近 7pt 下限。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2 确认写作质量中等偏上，AI 痕迹不明显，格式基本合规。Figure 字体 ≥7pt。R1 minor items: Abstract NLL 未展开, Figure 1 caption 缺 ρ 说明, Appendix 过多(18个)建议合并。\"}\n  action_items:\n    - {round: 16, action: \"Various minor fixes\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Previously resolved issues (unchanged) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"8 pages confirmed R14.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Fresh R17: PDF 核实 Conclusion 结束于 Page 9 约 12%，主体约 8.12 页。\"}\n    - {round: 18, reviewers: \"Director\", note: \"Discussion compressed, Conclusion on page 8. Verified with pdftotext.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: R2 格式检查确认正文 ≤8 页 (Conclusion on p.8)。\"}\n  action_items:\n    - {round: 13, action: \"Compress to 8 pages\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 17, action: \"压缩 Discussion/Results 约 0.2 页\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Discussion compressed. Conclusion fits on page 8. Body = 8 pages verified.\"\n  resolution_round: 18\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness — repurposed binary detectors\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - {round: 14, reviewers: \"R1,R2\", note: \"Detectors not designed for ordinal. Frame as 'repurposed baselines'.\"}\n    - {round: 15, reviewers: \"R1,R2\", note: \"Partial consensus: framework fair, threshold-based binary comparison nice-to-have.\"}\n    - {round: 16, reviewers: \"R1,R2\", note: \"R1: dimension asymmetry. R2 REBUT: same XGBoost = controlled.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"两位 Reviewer 均 AGREE。§4.3 开头加声明。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R18 review: §4.3 contextualization framing acknowledged by R2 ('论文明确说不是在声称优于这些方法')。但 R18-W1 提出新问题：需更直接承认 4-det ensemble 在 3-class F1 上更优。\"}\n  action_items:\n    - {round: 14, action: \"Method §3.4 states 'repurposed as depth predictors'\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"§4.3 contextualization statement\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"§4.3 opens with 'To contextualize depth discrimination ability rather than claim competitive advantage over detection-optimized methods'. Applied in R16/R17.\"\n  resolution_round: 18\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致 — entropy_std/min 不符合 drifting/stationary 划分\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"entropy_std (d=0.55) 和 entropy_min (pooled |ρ|=0.40) 不符合二分框架。建议三分法。\"}\n    - {round: 18, reviewers: \"Director\", note: \"MF2: Full tri-partition (3/1/3) applied across abstract, intro, method, results, discussion, conclusion, related_work, appendices.\"}\n  action_items:\n    - {round: 17, action: \"三分法 across all files\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) consistently applied across all 8+ files.\"\n  resolution_round: 18\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高（~8 个数值在 200 词内）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"建议保留 2-3 个关键数字。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF4: Reduced to 4 key numbers.\"}\n  resolution: \"Abstract trimmed from ~8 to 4 essential numbers.\"\n  resolution_round: 18\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"缺少候选讨论。LOFO 是事后验证非先验选择。\"}\n    - {round: 18, reviewers: \"Director\", note: \"SF5: Added justification in §3.3.\"}\n  resolution: \"Feature selection rationale added: interpretable distributional statistics enable DDR tri-partition analysis.\"\n  resolution_round: 18\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B 数据点\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"R1 升 Must-Fix，R2 REBUT（趋势非单调）。共识：gap 存在。\"}\n  resolution: \"Acknowledged in Limitations. Compute constraints prevent >8B experiments.\"\n  resolution_round: 18\n\n- id: \"R17-W4-old\"\n  summary: \"Introduction 缺少 'why depth matters' 的中间论证 (deprecated — see R17-W4)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"'generation depth' vs 'recursive generation depth' 交替使用。'Fingerprinting' 未定义。\"}\n    - {round: 18, reviewers: \"Director\", note: \"N2: 'depth fingerprinting' defined in Intro L9.\"}\n  resolution: \"Fingerprinting defined in Intro. Terminology consistent.\"\n  resolution_round: 18\n\n- id: \"R17-M2\"\n  summary: \"Stylometry 引用偏少 + 缺少 detection survey (Tang et al. 2024)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Stylometry 仅 2 篇经典。缺 Tang et al. 2024 CACM。\"}\n    - {round: 18, reviewers: \"Director\", note: \"N5: Tang et al. 2024 added. Neal et al. 2017 added.\"}\n  resolution: \"Tang et al. 2024 and Neal et al. 2017 added.\"\n  resolution_round: 18\n\n- id: \"R13-SF7\"\n  summary: \"Model scale limited (0.6B-8B), no >10B model\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"Acknowledged limitation. Wont_fix due to compute constraints.\"\n  resolution_round: 14\n\n- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 13\n  resolution: \"TOST demoted from Contribution to supporting analysis.\"\n  resolution_round: 13\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline + gen-1/gen-2+ topic confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 15\n  resolution: \"Two independent seed controls converge: demeaning F1=0.701, disjoint-seed F1=0.680.\"\n  resolution_round: 15\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 16\n  resolution: \"Cohen's d computed and reported.\"\n  resolution_round: 16\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 14\n  resolution: \"Phenomenon paper positioning.\"\n  resolution_round: 13\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  resolution: \"LOGO binary F1=0.694 leads in Abstract.\"\n  resolution_round: 14\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"Contribution 3 deleted R12.\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Title changed. Discussion explains bottleneck.\"\n  resolution_round: 13\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"Downstream moved to Appendix. Null result honestly reported.\"\n  resolution_round: 15\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 15\n  resolution: \"Temperature data corrected. Dual-model numbers reported.\"\n  resolution_round: 15\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Title changed.\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Same-family affinity noted. Cross-ref spread ≤0.013.\"\n  resolution_round: 16\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms; contribution claims need adjustment\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 15\n  resolution: \"Contributions split: task+DDR=science, 7-feature=efficient implementation.\"\n  resolution_round: 15\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"§3.4 explains all subsets.\"\n  resolution_round: 13\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Caption states identical configuration.\"\n  resolution_round: 13\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification discussion insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Discussion explains gen-1/gen-2+ boundary bottleneck.\"\n  resolution_round: 13\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Restructured to 3 paragraphs R12.\"\n  resolution_round: 12\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Footnote added in §3.3.\"\n  resolution_round: 13\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification added in method.tex.\"\n  resolution_round: 13\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"6-gen subset note added.\"\n  resolution_round: 13\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Six-fold magnitude gap framing + threshold sensitivity.\"\n  resolution_round: 13\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Switched to PDF.\"\n  resolution_round: 13\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Justification rewritten.\"\n  resolution_round: 13\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Confirmed correct.\"\n  resolution_round: 12\n\n- id: \"R12-M1\"\n  summary: \"Bonferroni correction scope not specified\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Scope specified in method.tex.\"\n  resolution_round: 13\n\n- id: \"R12-M2\"\n  summary: \"Pythia-1B vs 2.8B crossover undiscussed\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Crossover explanation added.\"\n  resolution_round: 13\n\n- id: \"R12-M3\"\n  summary: \"Generation failure rate causes not reported\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"2746 chain breaks reported.\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Some bib entries missing pages/volume\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Fixed.\"\n  resolution_round: 13\n\n- id: \"R13-M1\"\n  summary: \"Appendix D 'Notably' AI writing marker\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Deleted and rewritten.\"\n  resolution_round: 13\n\n- id: \"R13-M5\"\n  summary: \"Figure 1 strip plot label area\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Confirmed acceptable.\"\n  resolution_round: 13\n\n- id: \"R13-RV1\"\n  summary: \"Instruct comparison uses different LOGO subsets\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Subset qualifiers added.\"\n  resolution_round: 13\n\n- id: \"R13-RV2\"\n  summary: \"Table 1 vs baselines F1 discrepancy\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Caption explains pooled vs macro-average.\"\n  resolution_round: 13\n\n- id: \"R13-RV3\"\n  summary: \"Instruct experiments missing registry\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"Preliminary experiments predating registry.\"\n  resolution_round: 13\n\n- id: \"R14-W1\"\n  summary: \"Feature selection circular reasoning\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Circular claim removed.\"\n  resolution_round: 14\n\n- id: \"R14-W2\"\n  summary: \"DDR vs model collapse distinction weak\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"Related Work §2.2 contrasts DDR vs model collapse.\"\n  resolution_round: 14\n\n- id: \"R14-W3\"\n  summary: \"Cross-domain evaluation confounded by temperature mismatch\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Acknowledged in Limitations.\"\n  resolution_round: 15\n\n- id: \"R14-W5\"\n  summary: \"Seed-sharing potential topic fingerprint confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Two independent seed controls confirm depth signal is not topic fingerprint.\"\n  resolution_round: 15\n\n- id: \"R14-W6\"\n  summary: \"Missing references — stylometric systems, CORN loss\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"3 citations added.\"\n  resolution_round: 14\n\n- id: \"R14-W7\"\n  summary: \"AI writing style traces persist\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"Comprehensive cleanup. R15 confirms clean.\"\n  resolution_round: 14\n\n- id: \"R15-N1\"\n  summary: \"Cross-model chains vs LOGO evaluation protocol incomparability\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Causal claim deleted. Protocol difference acknowledged.\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"Feature redundancy — effective dimensionality ~5\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Effective dimensionality ~5 acknowledged. TTR-hapax r=0.97.\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"DDR novelty positioning\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Intro distinguishes known drift vs novel structured decomposition.\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"Prompt type limitation not reflected in main results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Prompt-type sensitivity paragraph added to §4.2.\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"KS test cannot verify location/shape decomposition\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Decomposition rests on convergence of ρ, Levene, CV shift, and Cohen's d.\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"Disjoint-seed experiment lacks bootstrap CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Per-direction bootstrap CIs present.\"\n  resolution_round: 16\n\n- id: \"R16-W2\"\n  summary: \"gen-0 3-class F1 still appears prominently without leakage caveat\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 1 dagger footnote + caption explicit leakage warning.\"\n  resolution_round: 16\n\n- id: \"R16-W3\"\n  summary: \"Table 1 vs Table 2 use different evaluation protocols\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Table 2 caption explains protocol difference.\"\n  resolution_round: 16\n\n- id: \"R16-M1\"\n  summary: \"5 orphan bib entries + bib title/author mismatches\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"5 orphans removed. Entries verified.\"\n  resolution_round: 16\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Phenomenon paper positioning.\"\n  resolution_round: 5"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-18T10:36:26.656887+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 31272}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-18T10:39:02.437855+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 18\n\n**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 via ARR May 2026 cycle (deadline: 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）+ R2（新颖性 + 完整性 + 写作质量）\n**交叉回应**: 已完成（R1 ↔ R2 全部逐条回应）\n\n---\n\n## Summary\n\n本文提出 generation depth classification，将 LLM 递归生成文本检测从 binary (real vs. synthetic) 推进到 3-class (gen-0 / gen-1 / gen-2+)。核心发现是 Differential Depth Response (DDR)：7 个标准统计特征在递归生成中呈现三分响应模式（3 drifting / 1 intermediate / 3 near-stationary），使用 XGBoost 在 8 个 base model 生成器的 Leave-One-Generator-Out 评估下达到 leak-free binary F1 = 0.694。论文实验设计严谨、消融全面，但方法论新颖性有限、DDR 被过度包装为 \"framework\"、标题与实际能力不匹配、且仅限 base model 的约束严重限制实际影响力。\n\n---\n\n## Strengths\n\n**S1. 问题定义新颖且有意义。** Generation depth classification 是对 binary detection 的自然且有价值的推进。在数据溯源和合成数据管理中有潜在应用价值。没有 prior depth-classification 方法存在，方向确实是新的。[R1, R2 共识]\n\n**S2. 严谨的实验设计和统计方法。** LOGO 交叉验证设计合理；8 个生成器覆盖 5 个模型族；bootstrap CIs、Bonferroni correction、TOST equivalence testing、class-balanced subsampling 等统计工具使用规范。主动识别并处理 gen-0 seed sharing 问题（采用 binary F1 作为 primary metric）。[R1, R2 共识]\n\n**S3. 全面且诚实的消融分析。** 12 页附录覆盖 length confound、prompt type、5-class granularity、QLoRA、LOFO、classifier sensitivity、robustness to perturbation、cross-domain、error analysis、downstream utility、feature distributions、cross-temperature 等。每个消融有明确目的且在正文中有引用。[R1, R2 共识]\n\n**S4. 坦诚的 Limitations。** 主动承认 base-model restriction、instruction-tuning degradation (F1=0.338)、temperature sensitivity、3-class ceiling、reference model dependency 等限制。在同类论文中不常见。[R1, R2 共识]\n\n**S5. Concurrent work 定位清晰。** §2.2 对 Broken Telephone 和 Markovian Chains 的区分论述有效（open-ended continuation vs. paraphrastic/feedback loop），且指出两个独立工作收敛于 ~3 class ceiling 的互补解释。[R1 Strength 6]\n\n**S6. 写作质量合格。** AI 痕迹不明显（无 em-dash 滥用、-ing phrase 结尾少、过渡词使用适度），格式基本合规（8 页正文、匿名、行号、ACL template）。[R2 写作检查]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**MF1 [critical, consensus] DDR \"framework\" overclaim + 阈值论证不足**\n- R1-N1 提出，R2 AGREE\n- |ρ| > 0.60 / |ρ| < 0.10 的分组阈值缺乏理论依据（Cohen d benchmarks 不适用于 Spearman ρ）\n- N=7 特征分成 3/1/3，intermediate 仅 entropy_std 一个成员，不足以建立 \"framework\"\n- Levene test 拒绝等方差但论文用 CV shift 辩护，需要 TOST equivalence testing（论文在 Appendix M 已对 downstream 使用 TOST，可一致化）\n- **要求**：(a) 对 ρ 阈值做 sensitivity analysis (±0.10)；(b) 对 near-stationary 特征用 TOST；(c) 将 DDR 从 \"framework\" 降级为 \"empirical pattern\"\n\n**MF2 [critical, consensus] \"Fingerprinting\" 标题与 3-class 实际能力不匹配**\n- R1-N3 提出，R2 AGREE（R2 自身 W1 同点）\n- Binary F1 = 0.694 意味着 ~30% 错分率；per-generator F1 跨度 0.633-0.724；5-class F1 仅 0.50（gen-2/gen-3 各 0.259）\n- \"Fingerprinting\" 在安全/取证语境意味着高可靠性识别，与实际性能不符\n- Conclusion \"three classes = practical ceiling\" 与标题矛盾\n- **要求**：将 \"Fingerprinting\" 改为更准确的措辞（如 \"Depth Classification\" / \"Depth Profiling\"）；在 Abstract 声明 3-class 粒度限制\n\n**MF3 [critical, consensus] 方法论新颖性不足 + 贡献定位需调整**\n- R2-N1 提出，R1 AGREE\n- 7 个特征均为标准统计量（NLL 基本矩/分位数 + 经典 stylometry），XGBoost 无改进\n- Baseline 均为 binary detection 方法（无 prior depth classification method 可比较），限制了 competitive comparison 的意义\n- R1 补充：贡献定位应为 \"empirical discovery + feasibility demonstration\"，问题定义的新颖性有价值\n- **要求**：明确定位为 empirical study / phenomenon paper，降低方法创新声称；在 §1 contribution list 中区分 \"task formulation\" 和 \"empirical finding\"\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF1 [critical, consensus] Base-model-only 约束限制实际影响力，scope 声明不足**\n- R2-N2 (Must-Fix) + R1-W2，两位均标记\n- OLMo-Instruct LOGO F1 = 0.338 接近 random；instruction tuning reverses ρ from -0.6 to +0.2~+0.5\n- Abstract 未提及 base-model restriction；Introduction §1 L15 有提及但位置偏后\n- 现实中递归生成更可能发生在 instruction-tuned models 上\n- **要求**：Abstract 中声明 base-model restriction；正文纳入 instruction-tuned 实验结果（非仅 Limitations 一句话）；论证 base-model 场景的重要性\n\n**SF2 [warning, consensus] Temperature sensitivity 未充分限定 DDR 普遍性声明**\n- R1-W1 提出，R2 AGREE\n- t=0.9 时 Pythia -26pp, Qwen -18.5pp；cross-temperature Qwen F1 0.810→0.418\n- DDR \"property of recursive generation\" 声明需限定 temperature/sampling 条件\n- **要求**：在 Abstract 和所有 DDR 普遍性声明处加条件限定\n\n**SF3 [warning, consensus] Downstream utility 结果弱化论文动机**\n- R2-W3 提出，R1 AGREE\n- Appendix L TOST 确认 depth-aware 与 random subsampling 在 perplexity 上等价\n- Introduction 以 data curation 为动机，但实验表明 depth 信息不影响 downstream performance\n- **要求**：调整动机叙事（从 data quality filtering 转为 provenance transparency/audit），或找到更有说服力的应用场景\n\n**SF4 [warning, consensus] Baseline 4-det ensemble 优于所提方法，需更直接承认**\n- R1-N2 提出（原判 critical），R2 REBUT 纠正数据错误\n- R2 纠正：3-class F1 gap 是 2.1pp（0.785 vs 0.774），非 R1 引用的 6.1pp；论文明确说 \"contextualize not claim advantage\"\n- R2 认可效率差异（2.4× inference + 3.2× GPU memory）在大规模场景有意义\n- 两位均同意应更直接承认 4-det ensemble 在 3-class 准确性上更优\n- **要求**：§4.3 更明确承认性能差距；效率论证聚焦 large-scale batch processing 场景\n\n**SF5 [warning, consensus] Cross-reference model 声明过强**\n- R1-W5 提出，R2 AGREE\n- Spread ≤ 0.013 仅说明 features 对 reference model 选择鲁棒 ≠ \"DDR 是递归生成内在属性\"\n- **要求**：区分 \"robustness to implementation choice\" 和 \"fundamental property claim\"\n\n**SF6 [warning, consensus] Stylometry 引用 + data contamination/provenance 文献线缺失**\n- R2-W4 + R2-W5 提出，R1 均 AGREE\n- TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体\n- 以 data provenance 为动机但 Related Work 缺 contamination detection 文献\n- **要求**：§2.3 增加 lexical richness 文献；§2 增加 data provenance/contamination paragraph\n\n**SF7 [info→warning, partial consensus] Gen-0 seed sharing + XGBoost 超参数**\n- R1-W3（gen-0 膨胀）：R2 partial REBUT，论文已处理（binary F1 as primary metric），但 Table 1/2 展示可改进\n- R1-W4（XGBoost 超参数）：R2 AGREE with caveat（Appendix H classifier alternatives 部分缓解）\n- **建议**：Table 1/2 caption 更突出 gen-0 影响提醒；报告 XGBoost 超参数选择来源\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 明确达成共识：\n\n1. **[AGREE] DDR 应定位为 empirical observation 而非 general framework** (R1-N1 + R2-N3)\n2. **[AGREE] \"Fingerprinting\" 标题需修改** (R1-N3 + R2-W1)\n3. **[AGREE] Base-model-only 是核心实际限制** (R1-W2 + R2-N2)\n4. **[AGREE] 方法论新颖性有限，贡献在于 task formulation + empirical finding** (R2-N1 + R1 AGREE)\n5. **[AGREE] Downstream utility 弱化动机** (R2-W3 + R1 AGREE)\n6. **[AGREE] Temperature sensitivity 需更强限定** (R1-W1 + R2 AGREE)\n7. **[AGREE] Depth 2-4 merge 限制 framing** (R1-W6 + R2-W1)\n8. **[AGREE] Missing references: stylometry 变体 + data provenance** (R2-W4/W5 + R1 AGREE)\n9. **[AGREE] Cross-reference 声明需降级** (R1-W5 + R2 AGREE)\n\n## Reviewer Divergence\n\n**D1. DDR vs model collapse 增量 (R2-N3 vs R1 partial REBUT)**\n- R2 认为 DDR 仅是 \"naming existing phenomena\"\n- R1 反驳：DDR 与 model collapse 有实质机制区别（fixed params, reversible, shape stability ≠ 不可逆参数退化）；shape stability (d < 0.10) 非先验可预期\n- **共识部分**：两位均同意 DDR 的 analytical contribution 有限，应定位为 empirical observation\n- **未解决**：DDR 是否提供了超越 model collapse 文献的真正新洞察——R1 认为有（机制区别），R2 认为有限\n\n**D2. Baseline comparison severity (R1-N2 vs R2 REBUT)**\n- R1 原判 critical (gap 6.1pp)\n- R2 纠正数据错误 (实际 2.1pp)，指出论文明确说 contextualize not compete\n- **已解决**：降为 warning (SF4)，两位均同意需更直接承认 4-det ensemble 优势\n\n**D3. Gen-0 seed sharing severity (R1-W3 vs R2 partial REBUT)**\n- R1 认为 Table 1/2 展示误导\n- R2 认为论文已有缓解措施（binary F1 as primary），gen-0 高分部分源于任务固有可区分性\n- **已解决**：非关键问题，改进 caption 即可\n\n---\n\n## Questions（需作者回答）\n\n**Q1.** DDR 阈值 |ρ| > 0.60 / |ρ| < 0.10 的 sensitivity 如何？如果变动 ±0.10，三分法是否还成立？[R1-Q1, R2-Q2]\n\n**Q2.** LOGO 中 Pythia-1B 和 Pythia-2.8B 是同时 held out 还是分别？如果分别，同 family 不同 size 的模型在 train set 中是否导致 family-level 信息泄漏？[R1-Q2]\n\n**Q3.** Downstream utility 实验显示 depth-aware 与 random subsampling 等价（TOST confirmed）。如果 depth 信息不影响 downstream performance，depth classification 的主要应用场景是什么？[R1-Q3, R2-Q4]\n\n**Q4.** Instruction-tuned model 上 F1 降至 0.338 的原因：是 depth signal 本身消失，还是 instruction tuning 引入新 confound 使特征不再 discriminative？[R2-Q5]\n\n**Q5.** 方法在混合 prompt type 条件下的表现如何？实际递归生成可能混合不同 prompt types。[R1-Q6, R2-Q3]\n\n**Q6.** Table 2 中 4-detector ensemble 在 3-class F1 上优于 7-feature method。作者如何定位方法的 practical value proposition？[R1-Q5]\n\n---\n\n## Missing References\n\n1. **Lexical richness measures**: McCarthy & Jarvis (2010) \"MTLD, vocd-D, and HD-D\"; Covington & McFall (2010) \"MATTR\" [R2-W4]\n2. **Data contamination detection**: Oren et al. (2024) \"Proving test set contamination in black box language models\"; Golchin & Surdeanu (2024) \"Time Travel in LLMs\" [R2-W5]\n3. **Data provenance**: Longpre et al. (2024) \"Data Authenticity, Consent, and Provenance for AI Are All Broken\" [R2-W5]\n4. **Iterative generation analysis**: Huang et al. (2023) \"Large Language Models Cannot Self-Correct Reasoning Yet Without External Feedback\" [R2 suggested]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**EMNLP 2026 评分标准**: 3 = Findings（可被 Findings 接收）\n\n**两位 Reviewer 独立评分**:\n- R1: 3.0 (Findings), Soundness 3/5, Excitement 3/5, Reproducibility 3.5/5, Confidence 4/5\n- R2: 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Confidence 4/5\n\n**综合评分**:\n| 维度 | 综合分 | 理由 |\n|------|--------|------|\n| Soundness | 3.25/5 | 实验设计和统计方法严谨，但 DDR 阈值论证不足，baseline 实际更优 |\n| Excitement | 2.75/5 | 问题定义新颖，但方法仅用标准特征，base-model-only 限制实际兴趣 |\n| Reproducibility | 3.75/5 | 特征定义和实验参数清晰，但代码未开源，XGBoost 超参数来源不明 |\n| Confidence | 4/5 | 两位 Reviewer 独立收敛到相同评分和高度重合的核心关切 |\n\n**评分理由**:\n\n本文的核心价值在于 **问题定义**（generation depth classification 是新方向）和 **实证发现**（DDR 三分模式作为 empirical observation 有价值）。实验设计严谨、消融全面、Limitations 坦诚，这些都是优点。\n\n阻止进入主会议的关键问题：\n1. **方法论贡献有限**：7 个标准特征 + XGBoost，无技术创新，贡献停留在 \"把已有工具组合用于新任务\"\n2. **DDR overclaim**：将 7 个特征的描述性分组提升为 \"framework\"，阈值缺乏理论基础\n3. **标题误导**：\"Fingerprinting\" 暗示高可靠性，实际 F1=0.694 且仅 3-class 粒度\n4. **适用范围极窄**：仅 base model + t ≤ 0.7，instruction-tuned models 上近乎失效\n\n作为 **Findings paper**，论文有足够价值：新任务定义 + 系统性实证分析 + 诚实的限制讨论。但需要修正 overclaiming（标题、DDR framework 定位、baseline 对比 framing）以匹配实际贡献水平。\n\n**提升至 Borderline Conference (3.5) 的条件**:\n1. 修正标题和 DDR 定位（从 framework 降级为 empirical pattern）\n2. Abstract 中声明 base-model restriction 和 3-class 粒度限制\n3. 对 DDR 阈值做 sensitivity analysis + TOST\n4. 正文纳入 instruction-tuned 实验结果并分析 depth signal 退化原因\n5. 调整动机叙事（从 data curation 转为 provenance audit）\n6. 补充 missing references\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 四个必答问题基本覆盖 ✓\n- DDR/LLM 缩写已定义 ✓\n- 数据密度适当（R17 修改后从 ~8 降至 4 个数字）✓\n- **缺失**：未声明 base-model restriction——读者可能误以为方法适用于所有 LLM [SF1]\n- **缺失**：未声明 temperature 条件依赖 [SF2]\n\n### Introduction\n- 叙事线基本连贯：recursive chains as dynamical system → binary detection insufficient → depth classification → DDR\n- R18 restructure 有改善（dynamical system framing leads, base-model restriction at L15）\n- **问题**：7-17% LLM content 引用（Liang et al.）描述 instruction-tuned models 影响，与 base-model scope 存在 tension [SF1]\n- **问题**：从 binary detection 到 \"why depth matters\" 的论证仍有跳跃——downstream utility null result 弱化了 data curation 动机 [SF3]\n- Contribution list 需区分 task formulation 和 empirical finding [MF3]\n\n### Related Work\n- §2.1 Detection 覆盖充分 ✓\n- §2.2 Model Collapse + concurrent work 区分有效（R1 Strength 6）✓\n- §2.3 Stylometry 偏薄，缺 TTR 变体文献 [SF6]\n- §2.4 Data provenance/contamination 文献线缺失 [SF6]\n\n### Method\n- Task formulation 清晰，generation chain construction 详细 ✓\n- Feature extraction 动机合理（interpretable statistics for DDR analysis）✓\n- LOGO 和 cross-model chain 协议设计严谨 ✓\n- XGBoost 超参数来源不明 [SF7]\n- Temperature 固定 t=0.7 justification 不足 [SF2]\n\n### Results\n- Table 1 清晰，bootstrap CIs ✓\n- DDR 数据呈现紧凑 ✓\n- §4.3 contextualization framing 合理但需更直接承认 4-det advantage [SF4]\n- Feature complementarity 论述偏粗略 [R2]\n- Cross-reference 声明需降级 [SF5]\n\n### Discussion\n- 覆盖了 instruction tuning、temperature、prompt type、resolution ceiling ✓\n- 篇幅受限（8 页约束），各点深度不够\n- DDR vs model collapse 区分已有改善，但可进一步强化可逆性 + shape stability 论证 [R17-W5]\n\n### Conclusion\n- 简洁诚实 ✓\n- \"Three classes = practical ceiling\" 与标题矛盾 [MF2]\n\n### Limitations\n- 覆盖全面：base-model, instruction-tuning, temperature, prompt-type, scale, domain, reference model ✓\n- 在同类论文中属于高质量 Limitations section\n\n### Ethics\n- 覆盖 dual-use, privacy, licenses, compute budget ✓\n\n### Format Compliance\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✓ |\n| ACL template [review] | ✓ |\n| 匿名化 | ✓ |\n| 行号 | ✓ |\n| Limitations section | ✓ |\n| Ethics Statement | ✓ |\n| Responsible NLP Checklist | ⚠️ 未在 PDF 中发现，可能通过 ARR 系统单独提交 |\n| 图表字体 ≥ 7pt | ✓ |\n| Bib 格式 | ⚠️ 部分条目需验证 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 18\n\n**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 via ARR May 2026 cycle (deadline: 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）+ R2（新颖性 + 完整性 + 写作质量）\n**交叉回应**: 已完成（R1 ↔ R2 全部逐条回应）\n\n---\n\n## Summary\n\n本文提出 generation depth classification，将 LLM 递归生成文本检测从 binary (real vs. synthetic) 推进到 3-class (gen-0 / gen-1 / gen-2+)。核心发现是 Differential Depth Response (DDR)：7 个标准统计特征在递归生成中呈现三分响应模式（3 drifting / 1 intermediate / 3 near-stationary），使用 XGBoost 在 8 个 base model 生成器的 Leave-One-Generator-Out 评估下达到 leak-free binary F1 = 0.694。论文实验设计严谨、消融全面，但方法论新颖性有限、DDR 被过度包装为 \"framework\"、标题与实际能力不匹配、且仅限 base model 的约束严重限制实际影响力。\n\n---\n\n## Strengths\n\n**S1. 问题定义新颖且有意义。** Generation depth classification 是对 binary detection 的自然且有价值的推进。在数据溯源和合成数据管理中有潜在应用价值。没有 prior depth-classification 方法存在，方向确实是新的。[R1, R2 共识]\n\n**S2. 严谨的实验设计和统计方法。** LOGO 交叉验证设计合理；8 个生成器覆盖 5 个模型族；bootstrap CIs、Bonferroni correction、TOST equivalence testing、class-balanced subsampling 等统计工具使用规范。主动识别并处理 gen-0 seed sharing 问题（采用 binary F1 作为 primary metric）。[R1, R2 共识]\n\n**S3. 全面且诚实的消融分析。** 12 页附录覆盖 length confound、prompt type、5-class granularity、QLoRA、LOFO、classifier sensitivity、robustness to perturbation、cross-domain、error analysis、downstream utility、feature distributions、cross-temperature 等。每个消融有明确目的且在正文中有引用。[R1, R2 共识]\n\n**S4. 坦诚的 Limitations。** 主动承认 base-model restriction、instruction-tuning degradation (F1=0.338)、temperature sensitivity、3-class ceiling、reference model dependency 等限制。在同类论文中不常见。[R1, R2 共识]\n\n**S5. Concurrent work 定位清晰。** §2.2 对 Broken Telephone 和 Markovian Chains 的区分论述有效（open-ended continuation vs. paraphrastic/feedback loop），且指出两个独立工作收敛于 ~3 class ceiling 的互补解释。[R1 Strength 6]\n\n**S6. 写作质量合格。** AI 痕迹不明显（无 em-dash 滥用、-ing phrase 结尾少、过渡词使用适度），格式基本合规（8 页正文、匿名、行号、ACL template）。[R2 写作检查]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**MF1 [critical, consensus] DDR \"framework\" overclaim + 阈值论证不足**\n- R1-N1 提出，R2 AGREE\n- |ρ| > 0.60 / |ρ| < 0.10 的分组阈值缺乏理论依据（Cohen d benchmarks 不适用于 Spearman ρ）\n- N=7 特征分成 3/1/3，intermediate 仅 entropy_std 一个成员，不足以建立 \"framework\"\n- Levene test 拒绝等方差但论文用 CV shift 辩护，需要 TOST equivalence testing（论文在 Appendix M 已对 downstream 使用 TOST，可一致化）\n- **要求**：(a) 对 ρ 阈值做 sensitivity analysis (±0.10)；(b) 对 near-stationary 特征用 TOST；(c) 将 DDR 从 \"framework\" 降级为 \"empirical pattern\"\n\n**MF2 [critical, consensus] \"Fingerprinting\" 标题与 3-class 实际能力不匹配**\n- R1-N3 提出，R2 AGREE（R2 自身 W1 同点）\n- Binary F1 = 0.694 意味着 ~30% 错分率；per-generator F1 跨度 0.633-0.724；5-class F1 仅 0.50（gen-2/gen-3 各 0.259）\n- \"Fingerprinting\" 在安全/取证语境意味着高可靠性识别，与实际性能不符\n- Conclusion \"three classes = practical ceiling\" 与标题矛盾\n- **要求**：将 \"Fingerprinting\" 改为更准确的措辞（如 \"Depth Classification\" / \"Depth Profiling\"）；在 Abstract 声明 3-class 粒度限制\n\n**MF3 [critical, consensus] 方法论新颖性不足 + 贡献定位需调整**\n- R2-N1 提出，R1 AGREE\n- 7 个特征均为标准统计量（NLL 基本矩/分位数 + 经典 stylometry），XGBoost 无改进\n- Baseline 均为 binary detection 方法（无 prior depth classification method 可比较），限制了 competitive comparison 的意义\n- R1 补充：贡献定位应为 \"empirical discovery + feasibility demonstration\"，问题定义的新颖性有价值\n- **要求**：明确定位为 empirical study / phenomenon paper，降低方法创新声称；在 §1 contribution list 中区分 \"task formulation\" 和 \"empirical finding\"\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF1 [critical, consensus] Base-model-only 约束限制实际影响力，scope 声明不足**\n- R2-N2 (Must-Fix) + R1-W2，两位均标记\n- OLMo-Instruct LOGO F1 = 0.338 接近 random；instruction tuning reverses ρ from -0.6 to +0.2~+0.5\n- Abstract 未提及 base-model restriction；Introduction §1 L15 有提及但位置偏后\n- 现实中递归生成更可能发生在 instruction-tuned models 上\n- **要求**：Abstract 中声明 base-model restriction；正文纳入 instruction-tuned 实验结果（非仅 Limitations 一句话）；论证 base-model 场景的重要性\n\n**SF2 [warning, consensus] Temperature sensitivity 未充分限定 DDR 普遍性声明**\n- R1-W1 提出，R2 AGREE\n- t=0.9 时 Pythia -26pp, Qwen -18.5pp；cross-temperature Qwen F1 0.810→0.418\n- DDR \"property of recursive generation\" 声明需限定 temperature/sampling 条件\n- **要求**：在 Abstract 和所有 DDR 普遍性声明处加条件限定\n\n**SF3 [warning, consensus] Downstream utility 结果弱化论文动机**\n- R2-W3 提出，R1 AGREE\n- Appendix L TOST 确认 depth-aware 与 random subsampling 在 perplexity 上等价\n- Introduction 以 data curation 为动机，但实验表明 depth 信息不影响 downstream performance\n- **要求**：调整动机叙事（从 data quality filtering 转为 provenance transparency/audit），或找到更有说服力的应用场景\n\n**SF4 [warning, consensus] Baseline 4-det ensemble 优于所提方法，需更直接承认**\n- R1-N2 提出（原判 critical），R2 REBUT 纠正数据错误\n- R2 纠正：3-class F1 gap 是 2.1pp（0.785 vs 0.774），非 R1 引用的 6.1pp；论文明确说 \"contextualize not claim advantage\"\n- R2 认可效率差异（2.4× inference + 3.2× GPU memory）在大规模场景有意义\n- 两位均同意应更直接承认 4-det ensemble 在 3-class 准确性上更优\n- **要求**：§4.3 更明确承认性能差距；效率论证聚焦 large-scale batch processing 场景\n\n**SF5 [warning, consensus] Cross-reference model 声明过强**\n- R1-W5 提出，R2 AGREE\n- Spread ≤ 0.013 仅说明 features 对 reference model 选择鲁棒 ≠ \"DDR 是递归生成内在属性\"\n- **要求**：区分 \"robustness to implementation choice\" 和 \"fundamental property claim\"\n\n**SF6 [warning, consensus] Stylometry 引用 + data contamination/provenance 文献线缺失**\n- R2-W4 + R2-W5 提出，R1 均 AGREE\n- TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体\n- 以 data provenance 为动机但 Related Work 缺 contamination detection 文献\n- **要求**：§2.3 增加 lexical richness 文献；§2 增加 data provenance/contamination paragraph\n\n**SF7 [info→warning, partial consensus] Gen-0 seed sharing + XGBoost 超参数**\n- R1-W3（gen-0 膨胀）：R2 partial REBUT，论文已处理（binary F1 as primary metric），但 Table 1/2 展示可改进\n- R1-W4（XGBoost 超参数）：R2 AGREE with caveat（Appendix H classifier alternatives 部分缓解）\n- **建议**：Table 1/2 caption 更突出 gen-0 影响提醒；报告 XGBoost 超参数选择来源\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 明确达成共识：\n\n1. **[AGREE] DDR 应定位为 empirical observation 而非 general framework** (R1-N1 + R2-N3)\n2. **[AGREE] \"Fingerprinting\" 标题需修改** (R1-N3 + R2-W1)\n3. **[AGREE] Base-model-only 是核心实际限制** (R1-W2 + R2-N2)\n4. **[AGREE] 方法论新颖性有限，贡献在于 task formulation + empirical finding** (R2-N1 + R1 AGREE)\n5. **[AGREE] Downstream utility 弱化动机** (R2-W3 + R1 AGREE)\n6. **[AGREE] Temperature sensitivity 需更强限定** (R1-W1 + R2 AGREE)\n7. **[AGREE] Depth 2-4 merge 限制 framing** (R1-W6 + R2-W1)\n8. **[AGREE] Missing references: stylometry 变体 + data provenance** (R2-W4/W5 + R1 AGREE)\n9. **[AGREE] Cross-reference 声明需降级** (R1-W5 + R2 AGREE)\n\n## Reviewer Divergence\n\n**D1. DDR vs model collapse 增量 (R2-N3 vs R1 partial REBUT)**\n- R2 认为 DDR 仅是 \"naming existing phenomena\"\n- R1 反驳：DDR 与 model collapse 有实质机制区别（fixed params, reversible, shape stability ≠ 不可逆参数退化）；shape stability (d < 0.10) 非先验可预期\n- **共识部分**：两位均同意 DDR 的 analytical contribution 有限，应定位为 empirical observation\n- **未解决**：DDR 是否提供了超越 model collapse 文献的真正新洞察——R1 认为有（机制区别），R2 认为有限\n\n**D2. Baseline comparison severity (R1-N2 vs R2 REBUT)**\n- R1 原判 critical (gap 6.1pp)\n- R2 纠正数据错误 (实际 2.1pp)，指出论文明确说 contextualize not compete\n- **已解决**：降为 warning (SF4)，两位均同意需更直接承认 4-det ensemble 优势\n\n**D3. Gen-0 seed sharing severity (R1-W3 vs R2 partial REBUT)**\n- R1 认为 Table 1/2 展示误导\n- R2 认为论文已有缓解措施（binary F1 as primary），gen-0 高分部分源于任务固有可区分性\n- **已解决**：非关键问题，改进 caption 即可\n\n---\n\n## Questions（需作者回答）\n\n**Q1.** DDR 阈值 |ρ| > 0.60 / |ρ| < 0.10 的 sensitivity 如何？如果变动 ±0.10，三分法是否还成立？[R1-Q1, R2-Q2]\n\n**Q2.** LOGO 中 Pythia-1B 和 Pythia-2.8B 是同时 held out 还是分别？如果分别，同 family 不同 size 的模型在 train set 中是否导致 family-level 信息泄漏？[R1-Q2]\n\n**Q3.** Downstream utility 实验显示 depth-aware 与 random subsampling 等价（TOST confirmed）。如果 depth 信息不影响 downstream performance，depth classification 的主要应用场景是什么？[R1-Q3, R2-Q4]\n\n**Q4.** Instruction-tuned model 上 F1 降至 0.338 的原因：是 depth signal 本身消失，还是 instruction tuning 引入新 confound 使特征不再 discriminative？[R2-Q5]\n\n**Q5.** 方法在混合 prompt type 条件下的表现如何？实际递归生成可能混合不同 prompt types。[R1-Q6, R2-Q3]\n\n**Q6.** Table 2 中 4-detector ensemble 在 3-class F1 上优于 7-feature method。作者如何定位方法的 practical value proposition？[R1-Q5]\n\n---\n\n## Missing References\n\n1. **Lexical richness measures**: McCarthy & Jarvis (2010) \"MTLD, vocd-D, and HD-D\"; Covington & McFall (2010) \"MATTR\" [R2-W4]\n2. **Data contamination detection**: Oren et al. (2024) \"Proving test set contamination in black box language models\"; Golchin & Surdeanu (2024) \"Time Travel in LLMs\" [R2-W5]\n3. **Data provenance**: Longpre et al. (2024) \"Data Authenticity, Consent, and Provenance for AI Are All Broken\" [R2-W5]\n4. **Iterative generation analysis**: Huang et al. (2023) \"Large Language Models Cannot Self-Correct Reasoning Yet Without External Feedback\" [R2 suggested]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**EMNLP 2026 评分标准**: 3 = Findings（可被 Findings 接收）\n\n**两位 Reviewer 独立评分**:\n- R1: 3.0 (Findings), Soundness 3/5, Excitement 3/5, Reproducibility 3.5/5, Confidence 4/5\n- R2: 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Confidence 4/5\n\n**综合评分**:\n| 维度 | 综合分 | 理由 |\n|------|--------|------|\n| Soundness | 3.25/5 | 实验设计和统计方法严谨，但 DDR 阈值论证不足，baseline 实际更优 |\n| Excitement | 2.75/5 | 问题定义新颖，但方法仅用标准特征，base-model-only 限制实际兴趣 |\n| Reproducibility | 3.75/5 | 特征定义和实验参数清晰，但代码未开源，XGBoost 超参数来源不明 |\n| Confidence | 4/5 | 两位 Reviewer 独立收敛到相同评分和高度重合的核心关切 |\n\n**评分理由**:\n\n本文的核心价值在于 **问题定义**（generation depth classification 是新方向）和 **实证发现**（DDR 三分模式作为 empirical observation 有价值）。实验设计严谨、消融全面、Limitations 坦诚，这些都是优点。\n\n阻止进入主会议的关键问题：\n1. **方法论贡献有限**：7 个标准特征 + XGBoost，无技术创新，贡献停留在 \"把已有工具组合用于新任务\"\n2. **DDR overclaim**：将 7 个特征的描述性分组提升为 \"framework\"，阈值缺乏理论基础\n3. **标题误导**：\"Fingerprinting\" 暗示高可靠性，实际 F1=0.694 且仅 3-class 粒度\n4. **适用范围极窄**：仅 base model + t ≤ 0.7，instruction-tuned models 上近乎失效\n\n作为 **Findings paper**，论文有足够价值：新任务定义 + 系统性实证分析 + 诚实的限制讨论。但需要修正 overclaiming（标题、DDR framework 定位、baseline 对比 framing）以匹配实际贡献水平。\n\n**提升至 Borderline Conference (3.5) 的条件**:\n1. 修正标题和 DDR 定位（从 framework 降级为 empirical pattern）\n2. Abstract 中声明 base-model restriction 和 3-class 粒度限制\n3. 对 DDR 阈值做 sensitivity analysis + TOST\n4. 正文纳入 instruction-tuned 实验结果并分析 depth signal 退化原因\n5. 调整动机叙事（从 data curation 转为 provenance audit）\n6. 补充 missing references\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 四个必答问题基本覆盖 ✓\n- DDR/LLM 缩写已定义 ✓\n- 数据密度适当（R17 修改后从 ~8 降至 4 个数字）✓\n- **缺失**：未声明 base-model restriction——读者可能误以为方法适用于所有 LLM [SF1]\n- **缺失**：未声明 temperature 条件依赖 [SF2]\n\n### Introduction\n- 叙事线基本连贯：recursive chains as dynamical system → binary detection insufficient → depth classification → DDR\n- R18 restructure 有改善（dynamical system framing leads, base-model restriction at L15）\n- **问题**：7-17% LLM content 引用（Liang et al.）描述 instruction-tuned models 影响，与 base-model scope 存在 tension [SF1]\n- **问题**：从 binary detection 到 \"why depth matters\" 的论证仍有跳跃——downstream utility null result 弱化了 data curation 动机 [SF3]\n- Contribution list 需区分 task formulation 和 empirical finding [MF3]\n\n### Related Work\n- §2.1 Detection 覆盖充分 ✓\n- §2.2 Model Collapse + concurrent work 区分有效（R1 Strength 6）✓\n- §2.3 Stylometry 偏薄，缺 TTR 变体文献 [SF6]\n- §2.4 Data provenance/contamination 文献线缺失 [SF6]\n\n### Method\n- Task formulation 清晰，generation chain construction 详细 ✓\n- Feature extraction 动机合理（interpretable statistics for DDR analysis）✓\n- LOGO 和 cross-model chain 协议设计严谨 ✓\n- XGBoost 超参数来源不明 [SF7]\n- Temperature 固定 t=0.7 justification 不足 [SF2]\n\n### Results\n- Table 1 清晰，bootstrap CIs ✓\n- DDR 数据呈现紧凑 ✓\n- §4.3 contextualization framing 合理但需更直接承认 4-det advantage [SF4]\n- Feature complementarity 论述偏粗略 [R2]\n- Cross-reference 声明需降级 [SF5]\n\n### Discussion\n- 覆盖了 instruction tuning、temperature、prompt type、resolution ceiling ✓\n- 篇幅受限（8 页约束），各点深度不够\n- DDR vs model collapse 区分已有改善，但可进一步强化可逆性 + shape stability 论证 [R17-W5]\n\n### Conclusion\n- 简洁诚实 ✓\n- \"Three classes = practical ceiling\" 与标题矛盾 [MF2]\n\n### Limitations\n- 覆盖全面：base-model, instruction-tuning, temperature, prompt-type, scale, domain, reference model ✓\n- 在同类论文中属于高质量 Limitations section\n\n### Ethics\n- 覆盖 dual-use, privacy, licenses, compute budget ✓\n\n### Format Compliance\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✓ |\n| ACL template [review] | ✓ |\n| 匿名化 | ✓ |\n| 行号 | ✓ |\n| Limitations section | ✓ |\n| Ethics Statement | ✓ |\n| Responsible NLP Checklist | ⚠️ 未在 PDF 中发现，可能通过 ARR 系统单独提交 |\n| 图表字体 ≥ 7pt | ✓ |\n| Bib 格式 | ⚠️ 部分条目需验证 |"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-18T10:39:06.604480+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 1150 · 2026-05-18T10:39:16.544343+00:00_

审稿报告已投递至 Research Director。

---

**圆桌审稿 Round 18 完成总结**：

- **评分**：3.0 / 5.0 (Findings)，两位 Reviewer 独立收敛
- **3 个 Must-Fix**：DDR "framework" overclaim + 阈值论证不足、"Fingerprinting" 标题不匹配、方法论新颖性不足需调整贡献定位
- **7 个 Should-Fix**：base-model scope 声明、temperature 限定、downstream utility 动机调整、baseline 对比 framing、cross-reference 声明降级、missing references（stylometry + data provenance）、gen-0 展示 + XGBoost 超参数
- **1 个分歧**（已部分解决）：DDR vs model collapse 增量——R1 认为机制有实质区别，R2 认为 analytical contribution 有限；共识为 DDR 应定位为 empirical observation
- **Issue Tracker**：新增 8 个 issue (R18-N1~N3, R18-W1~W5)，更新 5 个现有 in_progress issue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1151 · 2026-05-18T10:39:19.276468+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

对 R1 的 9 个问题（3 Must-Fix + 6 Should-Fix）的回应摘要：

- **AGREE**: R1-N1 (DDR 阈值), R1-N3 (fingerprinting 名不副实), R1-W1 (温度敏感), R1-W2 (base-model 限制), R1-W4 (超参数), R1-W5 (声明过强), R1-W6 (depth 合并)
- **REBUT**: R1-N2 (baseline 对比) — R1 引用的数据有误（0.724 vs 实际约 0.764-0.774，gap 是 ~2.1pp 不是 6.1pp），且论文原文明确说是 contextualization 而非 claim superiority
- **部分 REBUT**: R1-W3 (gen-0 膨胀) — 论文已报告 leak-free binary F1，gen-0 高准确率部分是任务固有的可区分性

两位 reviewer 独立收敛到 Overall 3.0 (Findings) 和高度一致的核心关切。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1152 · 2026-05-18T10:39:29.294777+00:00_

审稿报告已提交至 Research Director，Issue Tracker 已同步更新。

**Round 18 审稿总结**：

- **评分**：3.0 (Findings)，两位 Reviewer 独立收敛
- **3 个 Must-Fix**：(1) DDR "framework" overclaim + 阈值论证不足；(2) "Fingerprinting" 标题与 3-class 实际能力不匹配；(3) 方法论新颖性不足，贡献定位需调整
- **7 个 Should-Fix**：base-model scope 声明不足、temperature 限定不够、downstream utility 弱化动机、baseline 对比 framing、cross-reference 声明过强、missing references、gen-0 展示 + XGBoost 超参数
- **核心共识**：问题定义新颖有价值，实验严谨，但贡献应明确定位为 empirical study / phenomenon paper，需修正标题和 DDR 定位以匹配实际贡献水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 111

## Round 111

56 recorded events


### User

_source line 1153 · 2026-05-18T12:31:33.615216+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference - Long Paper
- 截止日期: 2025-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-18T12:31:40.333626+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-18T12:31:40.384388+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-18T12:31:44.097830+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-18T12:31:44.098292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-18T12:31:48.598835+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-18T12:31:48.649449+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-18T12:31:52.665454+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-18T12:31:52.716103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-18T12:31:57.383483+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-18T12:31:57.885746+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_050_temp_curve_t09** (failed): DDR signal at t=0.9 degrades relative to t=0.7 but less severely than t=1.0, establishing monotonic temperature sensitivity\n- **exp_049_temp_curve_t05** (failed): DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\n- **exp_051_independent_seed** (success): Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\n  [independent_seed_results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/exp_051_independent_seed/data/independent_seed_results.txt)\n\n## 趋势\n成功 33 / 负向 1 / 失败 10 / 共 45\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-18T12:31:57.886110+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-18T12:31:59.743384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-18T12:32:00.195565+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Classifi
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-18T12:32:00.296329+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-18T12:32:09.281225+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's a summary of the key EMNLP 2026 submission guidelines and ARR-related information:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational te
…[truncated 2189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 11395
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-18T12:32:09.281958+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 3977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8985
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-18T12:32:18.998073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper template guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper template guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-18T12:32:19.801637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-18T12:32:20.303514+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, and the resulting recursive chains progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base (pretrained) models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting (Cohen's $d > 0.75$), intermediate, and near-stationary ($d < 0.10$) groups under standard decoding ($t \leq 0.7$), consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-18T12:32:20.404169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-18T12:32:20.755515+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	How this evolution proceeds is a fundamental question that connects to both model collapse theory \cite{curse_of_recursion, self_consuming_mad} and data provenance.
6	Yet binary detection decisions \cite{fast_detectgpt,binoculars,ld_score,detectgpt} obscure the provenance structure of recursive text: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	This is not hypothetical: estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and such text already re-enters training pipelines at scale.
8	
9	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and term this \emph{depth profiling} (characterizing generative provenance from distributional statistics).
10	No existing method addresses this task in non-paraphrastic continuation chains.
11	
12	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d < 0.10$).
13	This is consistent with recursive generation 
…[truncated 1765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-18T12:32:20.806312+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 1176 · 2026-05-18T12:32:20.856876+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-18T12:32:26.579894+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper template guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's the information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.

## Te
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7581
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-18T12:32:31.901775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-18T12:32:32.253425+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Depth profiling pipeline. (a)~Recursive generation chains are constructed by iteratively feeding text through a generator $G$. (b)~Seven features are extracted per text: five NLL statistics from a Pythia-410M reference model and two surface diversity measures. Horizontal bars show Spearman $\rho$ with generation depth and reveal the DDR tri-partition: drifting features ($|\rho| > 0.6$) capture the monotonic location shift, while near-stationary features ($|\rho| < 0.1$) provide a stable baseline. (c)~An XGBoost classifier trained under Leave-One-Generator-Out (LOGO) cross-validation predicts depth class (gen-0\,/\,gen-1\,/\,gen-2+).}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight generators
…[truncated 9811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-18T12:32:32.304088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-18T12:32:32.755702+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.}
14	This protocol differs from LOGO (all generators appear in training), so the difference from single-generator LOGO (binary 0.694) reflects both protocol and generator-subset effects; the 5-generator LOGO average is 0.734 for reference.
15	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
16	
17	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, which confirms transfer across architectural families.
18	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633). This may partly reflect same-family affinity with the Pythia-410M reference model rather than scale alone, though cross-reference experiments show the e
…[truncated 9587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-18T12:32:32.756128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-18T12:32:33.208023+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape while allowing location to drift.
5	Temperature and prompt-type ablations (\S\ref{sec:results-differential}) support this as a tendency rather than a guarantee: the signal degrades sharply at $t{=}0.9$ and varies across prompt types.
6	
7	Instruction tuning substantially weakens the signal (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base; 17--20\,pp degradation across three families) and reverses entropy-depth associations ($\rho$ flips from ${\approx}{-}0.6$ to $+0.2$--$+0.5$), consistent with shifting the generation attractor rather than destroying the iterative dynamics.
8	This restricts current applicability to base models; at the document level, gen-1 per-class F1\,=\,0.63 suffices for corpus-level flagging but not automated filtering (Appendix~\ref{app:error-analysis}).
9	Cross-temperature transfer degrades substantially at $t{=}1.0$ (Appendix~\ref{app:cross-temp}).
10	
11	Three classes represent the practical ceiling (5-class F1 ${\approx}$0.50; Appendix~\ref{app:finer-depth}), with the gen-1/gen-2+ boundary as the bottleneck.
12	DDR is distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}: inference-chain drift is fully reversible under fixed parameters and leaves distributional shape near-stationary ($d < 0.10$; variance ratios 0.98--1.12).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-18T12:32:33.208338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-18T12:32:34.162035+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and identified a differential depth response (DDR) tri-partition across eight base-model generators from five families.
5	A 7-feature ensemble exploiting this tri-partition achieves leak-free binary F1\,=\,0.694 (LOGO) and 0.764 (cross-model chains).
6	Current applicability is restricted to base models; instruction tuning and larger scales remain open.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-18T12:32:34.212801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-18T12:32:34.664555+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{tang2024science}, \citet{wu_survey_2025}, and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8,defactify_dataset}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal,corn_ordinal}) and the finding that combining drifting, intermediate, and near-stationary features yields consistent cross-generator performa
…[truncated 5570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-18T12:32:34.664945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-18T12:32:35.216271+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instr
…[truncated 2329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-18T12:32:35.517283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-18T12:32:35.517659+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-18T12:32:35.567992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-18T12:32:35.919687+00:00_

1	# Round 18 review — Review Director consolidated 2026-05-18
2	# R18 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)
3	# Both reviewers: 3.0 (Findings). Cross-responses completed.
4	
5	# === New issues raised in R18 review ===
6	
7	- id: "R18-N1"
8	  summary: "DDR 'framework' overclaim — 阈值论证不足, N=7 不足以建立 framework"
9	  category: method
10	  severity: critical
11	  status: open
12	  first_raised_round: 18
13	  last_seen_round: 18
14	  mentions:
15	    - {round: 18, reviewers: "R1,R2", note: "R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；Cohen d benchmarks 针对效应量非 Spearman ρ；N=7 特征分 3/1/3 不具统计说服力；Levene test 拒绝等方差但用 CV shift 辩护需 equivalence testing。R2 AGREE，补充 Appendix M TOST 存在但未直接用于 near-stationary 分类判定。两位共识：DDR 应定位为 empirical observation 非 general framework。"}
16	  action_items:
17	    - {round: 18, action: "对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'", assigned_to: "", status: "open"}
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R18-N2"
22	  summary: "'Fingerprinting' 标题与 3-class 实际能力不匹配 (binary F1=0.694, 5-class F1=0.50)"
23	  category: framing
24	  severity: critical
25	  status: open
26	  first_raised_round: 18
27	  last_seen_round: 18
28	  mentions:
29	    - {round: 18, reviewers: "R1,R2", note: "R1-N3：fingerprinting 在安全/取证领域意味着高可靠性，F1=0.694 约 30% 错分率不匹配。R2 AGREE，补充 per-generator F1 跨度 0.633-0.724，5-class F1=0.50 gen-2/3 仅 0.259。Conclusion 'three classes = practical ceiling' 与标题矛盾。建议改为 Depth Profiling/Classification。"}
30	  action_items:
31	    - {round: 18, action: "将标题中 'Fingerprinting' 改为更准确的措辞（Depth Classification/Profiling/Detection）；在 Abstract 明确 3-class 粒度限制", assigned_to: "", status: "open"}
32	  resolution: ""
33	  resolution_round: null
34	
35	- id: "R18-N3"
36	  summary: "方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost"
37	  category: method
38	  severity: critical
39	  status: open
40	  first_raised_round: 18
41	  last_seen_round: 18
42	  ment
…[truncated 32848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-18T12:33:16.433396+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-18T12:33:17.838712+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-18T12:33:18.296641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-18T12:33:18.698788+00:00_

1	% ===== Lexical Richness =====
2	
3	@article{mccarthy2010mtld,
4	  title = {{MTLD, vocd-D, and HD-D: A Validation Study of Sophisticated Approaches to Lexical Diversity Assessment}},
5	  author = {McCarthy, Philip M. and Jarvis, Scott},
6	  journal = {Behavior Research Methods},
7	  volume = {42},
8	  number = {2},
9	  pages = {381--392},
10	  year = {2010},
11	}
12	
13	@article{covington2010mattr,
14	  title = {{Cutting the Gordian Knot: The Moving-Average Type-Token Ratio (MATTR)}},
15	  author = {Covington, Michael A. and McFall, Joe D.},
16	  journal = {Journal of Quantitative Linguistics},
17	  volume = {17},
18	  number = {2},
19	  pages = {94--100},
20	  year = {2010},
21	}
22	
23	% ===== Data Provenance / Contamination =====
24	
25	@inproceedings{oren2024proving,
26	  title = {{Proving Test Set Contamination in Black Box Language Models}},
27	  author = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laber, Faisal and Stern, Avi},
28	  booktitle = {Proceedings of the International Conference on Learning Representations},
29	  year = {2024},
30	}
31	
32	@inproceedings{golchin2024time,
33	  title = {{Time Travel in LLMs: Tracing Data Contamination in Large Language Models}},
34	  author = {Golchin, Shahriar and Surdeanu, Mihai},
35	  booktitle = {Proceedings of the International Conference on Learning Representations},
36	  year = {2024},
37	}
38	
39	@inproceedings{longpre2024data,
40	  title = {{Data Authenticity, Consent, and Provenance for AI Are All Broken: What Will It Take to Fix Them?}},
41	  author = {Longpre, Shayne and Mahari, Robert and Lee, Naana and Luccioni, Sasha and Jernite, Yacine and others},
42	  booktitle = {Proceedings of the International Conference on Machine Learning},
43	  year = {2024},
44	}
45	
46	% ===== Statistics =====
47	
48	@book{cohen1988statistical,
49	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
50	  author = {Cohen, Jacob},
51	  edition = {2nd},
52	  publisher = {Lawrence Erlbaum Asso
…[truncated 1920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-18T12:33:18.749556+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-18T12:33:18.800132+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-18T12:33:22.813691+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-18T12:33:22.864239+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/review_context.yaml
/home/ubuntu/.age
…[truncated 3222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-18T12:33:28.235538+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-18T12:33:28.587345+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-18T12:33:28.789782+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-18T12:33:28.940762+00:00_

Found 15 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/feishu_group_oc_999770e4e57bfc6eabd12fc1f64af1ef_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/feishu_group_oc_dbd68d7879a81efc0c108e9844b15d0b_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/archive/feishu_group_oc_dbd68d7879a81efc0c108e9844b15d0b_director_20260518T012849_318682.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/archive/feishu_group_oc_dbd68d7879a81efc0c108e9844b15d0b_director_20260517T170201_792115.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/archive/feishu_group_oc_dbd68d7879a81efc0c108e9844b15d0b_director_20260515T135932_964533.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/worker_diagnose_qwen17b-sighup-root-cause_20260514T220218.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_diagnose_qwen17b-sighup-root-cause_20260514T220218.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-18T12:33:32.756200+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "glob": "AGENTS.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
    "glob": "AGENTS.md",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-18T12:33:32.806769+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1208 · 2026-05-18T12:33:34.409222+00:00_

现在读取项目配置检查外部审稿设置，并读取剩余的附录内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 112

## Round 112

64 recorded events


### User

_source line 1209 · 2026-05-18T23:21:16.308716+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2025-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-18T23:21:21.961714+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-18T23:21:22.012536+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-18T23:21:25.074284+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-18T23:21:25.124871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-18T23:21:29.296201+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-18T23:21:29.346834+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-18T23:21:32.240491+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+director_get_project_overview",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+director_get_project_overview",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-18T23:21:32.240851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-18T23:21:32.692653+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-18T23:21:32.693074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-18T23:21:32.843869+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-18T23:21:32.944825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-18T23:21:35.906359+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+submit_review_report",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+submit_review_report",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-18T23:21:35.906792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-18T23:21:36.408952+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-18T23:21:36.409288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-18T23:21:36.861612+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-18T23:21:36.861948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-18T23:21:37.063123+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+read_project_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-18T23:21:37.113786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-18T23:21:42.034458+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-18T23:21:42.938676+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 提交前最终检查（OpenReview form, AI disclosure）\n\n## 温度扩展实验结果（全部完成，已写入论文）\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\n|-------|------|-----------|--------|-------------|\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\n\n## 其他近期结论\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\n\n## 论文状态\n全部编辑完成，编译 0 errors，27 页。\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\n- appendix_tost.tex（8×7 per-generator TOST table）\n- appendix_classifier.tex OLMo 版本脚
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-18T23:21:43.441094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-18T23:21:45.399930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-18T23:21:45.852839+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\linenumbers
14	
15	\graphicspath{{../chart/}}
16	
17	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base LLM Text Chains}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	\input{related_work}
28	\input{method}
29	\input{results}
30	
31	\input{discussion}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\appendix
39	
40	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
41	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
42	
43	\input{appendix_dataset_stats}
44	\FloatBarrier
45	
46	\section{Length Confound Analysis}
47	\label{app:length}
48	\input{appendix_length}
49	\FloatBarrier
50	
51	\section{Prompt Type Generalization}
52	\label{app:prompt-type}
53	\input{appendix_prompt_type}
54	\FloatBarrier
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	\FloatBarrier
60	
61	\section{End-to-End Depth Classification (QLoRA)}
62	\label{app:qlora}
63	\input{appendix_qlora}
64	\FloatBarrier
65	
66	\section{Leave-One-Feature-Out Analysis}
67	\label{app:lofo}
68	\input{appendix_lofo}
69	\FloatBarrier
70	
71	\section{Confusion Matrix}
72	\label{app:confusion}
73	\input{appendix_confusion_matrix}
74	\FloatBarrier
75	
76	\section{Classifier Sensitivity}
77	\label{app:classifier}
78	\input{appendix_classifier}
79	\FloatBarrier
80	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-18T23:21:46.104140+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-18T23:21:46.255035+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-18T23:21:51.325712+00:00_

Web search results for query: "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the web search results, here's information about ACL Rolling Review (ARR) submission guidelines for 2025-2026:

## Submission Requirements and Format

All long, short, and theme papers must follow the ACL Author Guidelines and use the official ACL style tem
…[truncated 1575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7884
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-18T23:21:55.744670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review CFP 2025 long paper page limit short paper submission format requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review CFP 2025 long paper page limit short paper submission format requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-18T23:21:56.196728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-18T23:21:57.150967+00:00_

80	
81	\section{Robustness to Text Perturbation}
82	\label{app:human-edit}
83	\input{appendix_human_edit}
84	\FloatBarrier
85	
86	\section{Cross-Domain Generalization}
87	\label{app:domain}
88	\input{appendix_domain}
89	\FloatBarrier
90	
91	\section{Error Analysis of Binary Classification}
92	\label{app:error-analysis}
93	\input{appendix_error_analysis}
94	\FloatBarrier
95	
96	\section{Downstream Utility}
97	\label{app:downstream}
98	\input{appendix_downstream}
99	\FloatBarrier
100	
101	\section{Cross-Model Chain Per-Class Detail}
102	\label{app:cross-model-detail}
103	\input{appendix_cross_model_detail}
104	\FloatBarrier
105	
106	\section{Feature Distribution Analysis}
107	\label{app:feature-distributions}
108	\input{appendix_feature_distributions}
109	\FloatBarrier
110	
111	\section{Cross-Temperature Transfer}
112	\label{app:cross-temp}
113	\input{appendix_cross_temp}
114	\FloatBarrier
115	
116	\section{Feature Ablation}
117	\label{app:ablation-table}
118	\input{appendix_ablation}
119	\FloatBarrier
120	
121	\input{appendix_feature_correlation}
122	\FloatBarrier
123	
124	\section{Cross-Family Reference Models}
125	\label{app:cross-ref}
126	\input{table4}
127	\FloatBarrier
128	
129	\input{appendix_seed_control}
130	\FloatBarrier
131	
132	\input{appendix_tost}
133	\FloatBarrier
134	
135	\input{appendix_qualitative_examples}
136	
137	\end{document}
138	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-18T23:21:57.151334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-18T23:21:57.603994+00:00_

1	# Round 18 review — Review Director consolidated 2026-05-18
2	# R18 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)
3	# Both reviewers: 3.0 (Findings). Cross-responses completed.
4	
5	# === New issues raised in R18 review ===
6	
7	- id: "R18-N1"
8	  summary: "DDR 'framework' overclaim — 阈值论证不足, N=7 不足以建立 framework"
9	  category: method
10	  severity: critical
11	  status: open
12	  first_raised_round: 18
13	  last_seen_round: 18
14	  mentions:
15	    - {round: 18, reviewers: "R1,R2", note: "R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；Cohen d benchmarks 针对效应量非 Spearman ρ；N=7 特征分 3/1/3 不具统计说服力；Levene test 拒绝等方差但用 CV shift 辩护需 equivalence testing。R2 AGREE，补充 Appendix M TOST 存在但未直接用于 near-stationary 分类判定。两位共识：DDR 应定位为 empirical observation 非 general framework。"}
16	  action_items:
17	    - {round: 18, action: "对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'", assigned_to: "", status: "open"}
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R18-N2"
22	  summary: "'Fingerprinting' 标题与 3-class 实际能力不匹配 (binary F1=0.694, 5-class F1=0.50)"
23	  category: framing
24	  severity: critical
25	  status: open
26	  first_raised_round: 18
27	  last_seen_round: 18
28	  mentions:
29	    - {round: 18, reviewers: "R1,R2", note: "R1-N3：fingerprinting 在安全/取证领域意味着高可靠性，F1=0.694 约 30% 错分率不匹配。R2 AGREE，补充 per-generator F1 跨度 0.633-0.724，5-class F1=0.50 gen-2/3 仅 0.259。Conclusion 'three classes = practical ceiling' 与标题矛盾。建议改为 Depth Profiling/Classification。"}
30	  action_items:
31	    - {round: 18, action: "将标题中 'Fingerprinting' 改为更准确的措辞（Depth Classification/Profiling/Detection）；在 Abstract 明确 3-class 粒度限制", assigned_to: "", status: "open"}
32	  resolution: ""
33	  resolution_round: null
34	
35	- id: "R18-N3"
36	  summary: "方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost"
37	  category: method
38	  severity: critical
39	  status: open
40	  first_raised_round: 18
41	  last_seen_round: 18
42	  ment
…[truncated 32848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-18T23:21:58.006063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment",
  "allowed_domains": "['aclweb.org', '2026.aclweb.org', '2026.emnlp.org', 'emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment",
    "allowed_domains": "['aclweb.org', '2026.aclweb.org', '2026.emnlp.org', 'emnlp.org']"
  }
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-18T23:22:04.286798+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, here's the information about EMNLP 2026 call for papers submission deadline and ARR commitment:

## EMNLP 2026 Paper Submission

Papers must be submitted, at latest, by the ARR 2026 May cycle
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6280
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-18T23:22:05.492425+00:00_

Web search results for query: "ACL Rolling Review CFP 2025 long paper page limit short paper submission format requirements"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025) – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2025"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the ACL Rolling Review Call for Papers, here are the key submission requirements for 2025:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Submission Format Requirements

Papers must follow ACL formatting, and authors are en
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 9747
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-18T23:22:08.956770+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 1247 · 2026-05-18T23:22:09.007421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-18T23:22:14.981941+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL key information: 1) All deadlines (ARR submission deadline, commitment deadline, notification date, camera-ready), 2) Page limits for long and short papers, 3) Template requirements, 4) Anonymity rules, 5) Appendix rules, 6) Any special requirements for ARR May 2026 cycle, 7) Responsible NLP checklist requirements. Return exact dates and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL key information: 1) All deadlines (ARR submission deadline, commitment deadline, notification date, camera-ready), 2) Page limits for long and short papers, 3) Template requirements, 4) Anonymity rules, 5) Appendix rules, 6) Any special requirements for ARR May 2026 cycle, 7) Responsible NLP checklist requirements. Return exact dates and numbers."
  }
}
```

</details>

---


### Tool call

_source line 1249 · 2026-05-18T23:22:17.993495+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission requirements: 1) Exact page limits for long papers and short papers (content pages, not counting references/appendices), 2) Template name and version, 3) Required sections (Limitations, Ethics), 4) Anonymity rules, 5) Appendix rules (inline or separate PDF?), 6) May 2026 cycle deadline, 7) Any formatting changes for 2025-2026 cycles. Return exact numbers and dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL submission requirements: 1) Exact page limits for long papers and short papers (content pages, not counting references/appendices), 2) Template name and version, 3) Required sections (Limitations, Ethics), 4) Anonymity rules, 5) Appendix rules (inline or separate PDF?), 6) May 2026 cycle deadline, 7) Any formatting changes for 2025-2026 cycles. Return exact numbers and dates."
  }
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-18T23:22:20.403596+00:00_

# EMNLP 2026 Key Information

## 1. ALL DEADLINES (UTC-12:00)
- **ARR submission:** May 25, 2026
- **Reviewer registration:** May 27, 2026
- **Author response/discussion:** July 7-13, 2026
- **Meta-review released:** July 30, 2026
- **EMNLP commitment:** August 2, 2026
- **Acceptance notification:** August 20, 2026
- **Camera-ready submission:** September 20, 2026
- **Main Conference:** October 24-29, 2026

## 2. PAGE LIMITS
- **Long papers:** 8 pages (9 pages for final accepted versions)
- **Short papers:** 4 pages (5 pages for final accepted versions)

## 3. TEMPLATE REQUIREMENTS
The call references "ARR submission requirements" but directs authors to follow guidelines at the ARR CFP link without specifying template details in this document.

## 4. ANONYMITY RULES
"There is no anonymity period requirement" following ACL and ARR policies. The review process maintains double-blind peer review—reviewers don't see authors; authors don't see reviewers.

## 5. APPENDIX RULES
"Optional Supplementary Materials (Appendices, Software and Data)" are permitted per ARR guidelines, though specific formatting rules are referenced externally.

## 6. ARR MAY 2026 SPECIAL REQUIREMENT
Authors must "explicitly declare which conference they intend to commit to at submission time," with selection binding for EMNLP 2026.

## 7. RESPONSIBLE NLP CHECKLIST
The document references the "responsible NLP research checklist" as required but provides no specific details beyond linking to the ARR ethics policy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 5421
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-18T23:22:26.329630+00:00_

# ACL Rolling Review Submission Requirements

## Page Limits
- **Long papers:** Up to 8 pages of content + unlimited references and limitations section
- **Short papers:** Up to 4 pages of content + unlimited references and limitations section

## Template
The document specifies use of the "official ACL style template" available at GitHub (acl-org/acl-style-files), but does not provide a version number.

## Required Sections
- **Limitations:** Mandatory dedicated section at paper's end before references (does not count toward page limit). Papers lacking this section face desk rejection.
- **Ethics:** Optional section titled "Ethical considerations" is recommended but not mandatory.

## Anonymity Rules
Papers must exclude author names and affiliations. Self-citations require third-person format: use "Smith previously showed (Smith, 1991)" rather than "We previously showed (Smith, 1991)." Supplementary materials and repository links must also be anonymized.

## Appendix Rules
Appendices appear after references in the submitted PDF and do not count toward page limits. Starting July 2025, appendices must follow double-column formatting (with specified exceptions) or face desk rejection.

## May 2026 Deadline
The document does not specify a May 2026 submission deadline.

## 2025-2026 Formatting Changes
Starting July 2025, appendices not conforming to double-column format (except approved exceptions) will trigger desk rejection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 8336
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-18T23:22:36.076844+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-18T23:22:37.282088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-18T23:22:37.483353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-18T23:22:37.734807+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, and the resulting recursive chains progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base (pretrained) models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting (Cohen's $d > 0.75$), intermediate, and near-stationary ($d < 0.10$) groups under standard decoding ($t \leq 0.7$), consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-18T23:22:37.887769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-18T23:22:37.888375+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	How this evolution proceeds is a fundamental question that connects to both model collapse theory \cite{curse_of_recursion, self_consuming_mad} and data provenance.
6	Yet binary detection decisions \cite{fast_detectgpt,binoculars,ld_score,detectgpt} obscure the provenance structure of recursive text: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	This is not hypothetical: estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and such text already re-enters training pipelines at scale.
8	
9	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and term this \emph{depth profiling} (characterizing generative provenance from distributional statistics).
10	No existing method addresses this task in non-paraphrastic continuation chains.
11	
12	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d < 0.10$).
13	This is consistent with recursive generation 
…[truncated 1765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-18T23:22:42.156160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-18T23:22:42.608332+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-18T23:22:42.608676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-18T23:22:42.659203+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source te
…[truncated 3786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-18T23:22:46.422223+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-18T23:22:46.472877+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-18T23:22:49.986619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null | head -10",
  "description": "Find yaml config files for project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*/gen-depth*\" 2>/dev/null | head -10",
    "description": "Find yaml config files for project"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-18T23:22:50.037235+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-18T23:22:53.250235+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config in project config"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-18T23:22:53.300882+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-18T23:23:54.112663+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (AoE)\n- **页数限制**: Long paper 正文 ≤8 页，references/appendix/limitations 不计入\n- **模板**: ACL style (`\\usepackage[review]{acl}`)，double-blind\n- **匿名规则**: 作者名和隶属必须隐藏，self-citation 用第三人称\n- **附录规则**: 必须 double-column 格式（2025年7月起 desk reject 新规）；inline 在同一 PDF 中\n- **Limitations section**: 必须有，缺失 = desk reject\n\n### 论文路径\n`projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n（及其 `\\input` 的所有子文件，同目录下）\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点审查：\n\n1. **DDR (Differential Depth Response) 论证**\n   - 三分法（drifting / intermediate / near-stationary）的统计依据是否充分\n   - Cohen's d 阈值和 Spearman ρ 阈值的选择是否有理论/经验基础\n   - 7 个特征的选择过程是否存在循环论证\n   - DDR 从 empirical observation 到 mechanism claim 的逻辑跳跃是否合理\n\n2. **评估协议**\n   - LOGO (Leave-One-Generator-Out) 设计是否存在数据泄漏\n   - gen-0 共享种子带来的 train/test overlap 是否充分处理\n   - Binary F1=0.694 的统计可信度（CI、显著性检验）\n   - 跨模型/跨温度泛化实验是否充分\n\n3. **消融分析**\n   - Feature ablation 是否完整（single-feature, group ablation, LOFO）\n   - Classifier sensitivity（XGBoost 超参数选择、替代分类器对比）\n   - Temperature sensitivity 是否限制了方法的普适性声明\n\n4. **统计方法**\n   - 使用的统计检验是否正确（Bonferroni、TOST equivalence testing、bootstrap CI）\n   - 效应量指标的选择和报告是否规范\n   - 样本量是否支持所做的统计推断\n\n5. **格式合规性（基本检查）**\n   - 正文是否 ≤8 页\n   - 行号、匿名是否正确\n\n请按 ARR reviewer 标准出具完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分制) → Confidence。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (AoE)\n- **页数限制**: Long paper 正文 ≤8 页，references/appendix/limitations 不计入\n- **模板**: ACL style (`\\usepackage[review]{acl}`)，double-blind\n- **匿名规则**: 作者名和隶属必须隐藏，self-citation 用第三人称\n- **附录规则**: 必须 double-column 格式（2025年7月起 desk reject 新规）；inline 在同一 PDF 中\n- **Limitations section**: 必须有，缺失 = desk reject\n\n### 论文路径\n`projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n（及其 `\\input` 的所有子文件，同目录下）\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点审查：\n\n1. **DDR (Differential Depth Response) 论证**\n   - 三分法（drifting / intermediate / near-stationary）的统计依据是否充分\n   - Cohen's d 阈值和 Spearman ρ 阈值的选择是否有理论/经验基础\n   - 7 个特征的选择过程是否存在循环论证\n   - DDR 从 empirical observation 到 mechanism claim 的逻辑跳跃是否合理\n\n2. **评估协议**\n   - LOGO (Leave-One-Generator-Out) 设计是否存在数据泄漏\n   - gen-0 共享种子带来的 train/test overlap 是否充分处理\n   - Binary F1=0.694 的统计可信度（CI、显著性检验）\n   - 跨模型/跨温度泛化实验是否充分\n\n3. **消融分析**\n   - Feature ablation 是否完整（single-feature, group ablation, LOFO）\n   - Classifier sensitivity（XGBoost 超参数选择、替代分类器对比）\n   - Temperature sensitivity 是否限制了方法的普适性声明\n\n4. **统计方法**\n   - 使用的统计检验是否正确（Bonferroni、TOST equivalence testing、bootstrap CI）\n   - 效应量指标的选择和报告是否规范\n   - 样本量是否支持所做的统计推断\n\n5. **格式合规性（基本检查）**\n   - 正文是否 ≤8 页\n   - 行号、匿名是否正确\n\n请按 ARR reviewer 标准出具完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分制) → Confidence。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-18T23:24:10.003070+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15890
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-18T23:24:10.805901+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (AoE)\n- **页数限制**: Long paper 正文 ≤8 页，references/appendix/limitations 不计入\n- **模板**: ACL style (`\\usepackage[review]{acl}`)，double-blind\n- **匿名规则**: 作者名和隶属必须隐藏，self-citation 用第三人称\n- **附录规则**: 必须 double-column 格式（2025年7月起 desk reject 新规）；inline 在同一 PDF 中\n- **Limitations section**: 必须有，缺失 = desk reject\n\n### 论文路径\n`projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n（及其 `\\input` 的所有子文件，同目录下）\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点审查：\n\n1. **新颖性评估**\n   - 问题定义（generation depth classification）是否足够新颖？与 binary detection 的区别是否有实质意义？\n   - DDR 相对于 model collapse 文献中已有的 drift 观察，增量贡献是否清晰？\n   - 方法本身（7 个标准特征 + XGBoost）是否有足够的技术创新？如果定位为 empirical study / phenomenon paper，这种定位是否合理？\n\n2. **Related Work 完整性**\n   - 与 concurrent work（如 Broken Telephone、Markovian Chains 等递归生成相关工作）的区分是否充分\n   - Stylometry 文献覆盖是否充分（TTR/hapax 是核心特征，相关文献是否到位）\n   - Data provenance / contamination detection 文献是否覆盖\n   - 引用数量和质量是否达到 EMNLP 标准\n\n3. **Framing 一致性**\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线\n   - 标题与论文实际能力的匹配度\n   - Base-model-only scope 是否在 Abstract 和 Introduction 中清楚声明\n   - 贡献声明与实际交付是否一致\n\n4. **写作质量**\n   - AI 写作痕迹检查：em-dash (—)、-ing 分词结尾、过度分段、过渡词堆砌\n   - 专有名词首次出现是否有定义\n   - 图表知识密度和可读性\n   - 附录数量（18个）是否过多，是否可合并\n\n5. **格式合规性（详细检查）**\n   - ACL template 版本是否正确\n   - 页数限制（正文 ≤8 页）\n   - 行号、匿名化\n   - 附录 double-column 格式\n   - Limitations section 存在性\n   - Reference 格式（natbib）\n   - Responsible NLP Checklist（如存在）\n\n请按 ARR reviewer 标准出具完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分制) → Confidence。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25 (AoE)\n- **页数限制**: Long paper 正文 ≤8 页，references/appendix/limitations 不计入\n- **模板**: ACL style (`\\usepackage[review]{acl}`)，double-blind\n- **匿名规则**: 作者名和隶属必须隐藏，self-citation 用第三人称\n- **附录规则**: 必须 double-column 格式（2025年7月起 desk reject 新规）；inline 在同一 PDF 中\n- **Limitations section**: 必须有，缺失 = desk reject\n\n### 论文路径\n`projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n（及其 `\\input` 的所有子文件，同目录下）\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点审查：\n\n1. **新颖性评估**\n   - 问题定义（generation depth classification）是否足够新颖？与 binary detection 的区别是否有实质意义？\n   - DDR 相对于 model collapse 文献中已有的 drift 观察，增量贡献是否清晰？\n   - 方法本身（7 个标准特征 + XGBoost）是否有足够的技术创新？如果定位为 empirical study / phenomenon paper，这种定位是否合理？\n\n2. **Related Work 完整性**\n   - 与 concurrent work（如 Broken Telephone、Markovian Chains 等递归生成相关工作）的区分是否充分\n   - Stylometry 文献覆盖是否充分（TTR/hapax 是核心特征，相关文献是否到位）\n   - Data provenance / contamination detection 文献是否覆盖\n   - 引用数量和质量是否达到 EMNLP 标准\n\n3. **Framing 一致性**\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线\n   - 标题与论文实际能力的匹配度\n   - Base-model-only scope 是否在 Abstract 和 Introduction 中清楚声明\n   - 贡献声明与实际交付是否一致\n\n4. **写作质量**\n   - AI 写作痕迹检查：em-dash (—)、-ing 分词结尾、过度分段、过渡词堆砌\n   - 专有名词首次出现是否有定义\n   - 图表知识密度和可读性\n   - 附录数量（18个）是否过多，是否可合并\n\n5. **格式合规性（详细检查）**\n   - ACL template 版本是否正确\n   - 页数限制（正文 ≤8 页）\n   - 行号、匿名化\n   - 附录 double-column 格式\n   - Limitations section 存在性\n   - Reference 格式（natbib）\n   - Responsible NLP Checklist（如存在）\n\n请按 ARR reviewer 标准出具完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分制) → Confidence。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-18T23:24:12.225520+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1419
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-18T23:24:16.336007+00:00_

两位 Reviewer 已收到任务，正在独立审稿。等待审稿结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1273 · 2026-05-18T23:30:42.611735+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

### Paper Summary

本文提出 generation depth classification 任务，将文本分类为 gen-0（人类写的）、gen-1（第一代 LLM 输出）、gen-2+（递归生成两次以上），而非传统的二分类（real vs. synthetic）。核心发现是 differential depth response (DDR)：7 个特征在递归生成下表现出三分结构——3 个 drifting（entropy_mean, TTR, hapax_ratio）、1 个 intermediate（entropy_std）、3 个 near-stationary（entropy_max, tail_decay, entropy_min）。基于 8 个 base model（5 个家族，0.6B-8B）构建 37K 文本数据集，7 特征 XGBoost 分类器在 LOGO 评估下 binary F1=0.694。论文明确限制于 base model，instruction tuning 显著削弱信号。

---

### Summary of Strengths

**S1. 任务定义新颖且有意义。** 从 binary detection 扩展到 ordinal depth classification 是一个自然且有价值的推进，连接了 model collapse 理论和 data provenance 实践。contribution 定位清晰——"empirical rather than methodological"（Introduction L20），避免了 overclaim。

**S2. 实验设计系统且控制变量意识强。** 论文展示了对实验方法论的深度理解：(a) 识别并处理了 gen-0 seed sharing 问题，采用 binary F1 作为 primary metric；(b) independent-seed control（Appendix P）排除了 topic-level leakage（F1 差距仅 1.4pp）；(c) length-matched subsampling（Appendix B）确认长度仅贡献约 6% 的分类性能；(d) seed-level demeaning 验证 depth signal 独立于 seed content。这些控制实验使得 core claim 可信度高。

**S3. DDR 三分结构有多维统计支撑。** Spearman ρ、Cohen's d、KS test、Levene test、TOST equivalence testing、CV shift 六个指标交叉验证，且 per-generator TOST（Appendix Q）确认三分结构不是 pooling artifact。entropy_min 在所有 8 个 generator 上通过等价性检验是有说服力的。

**S4. 消融分析全面。** Feature ablation（group-level §4.2 + LOFO Appendix F + 排列重要性）、classifier sensitivity（3 个替代分类器 + 3 个 ordinal 方法, Appendix G）、temperature sensitivity（4 个 generator × 3 个温度）、prompt-type sensitivity（3 种 prompt + LOPTO 迁移）覆盖了主要 confound 维度。

**S5. Limitations 诚实且详尽。** base model 限制、instruction tuning 退化、temperature sensitivity、scale effect、single domain、reference model dependency 都有明确讨论。这种科学诚实度在同类论文中少见。

**S6. 引用体系完整。** 67 篇引用覆盖了 detection、model collapse、stylometry、data provenance、ordinal classification 等所有相关子领域。包含了 2025-2026 年的最新工作（broken_telephone, markovian_chains, chainwash 等）。与 concurrent work 的比较（§2.2 broken_telephone 和 markovian_chains）做得好，明确了互补关系。

---

### Summary of Weaknesses

#### Must-Fix 问题（影响接收决定）

**N1 [critical] DDR 阈值缺乏先验理论/经验基础，存在 post-hoc 风险**
- 具体位置：§3.3 (Feature complementarity), §4.2
- 问题：DDR 三分的核心依据是 Cohen's d 阈值（drifting: d>0.75, near-stationary: d<0.10）和 Spearman ρ 阈值（drifting: |ρ|>0.60, near-stationary: |ρ|<0.10）。这些切分点没有来自理论推导或先验经验的支撑。论文提供了一个 robustness check——"shifting thresholds by ±0.10 does not alter grouping"（§4.2 L67），但这只说明三分对阈值微调稳定，不说明三分本身是数据中的自然结构而非人为施加的。
- 核心担忧：如果三分是 post-hoc 从数据中"读出来"的（7 个特征 → 观察分布 → 选择阈值使其形成 clean partition），那 DDR 作为论文的 primary contribution 的 novelty 就减弱了——它可能只是对已知现象（recursive generation shifts mean but not shape）的一个 descriptive restatement。
- 为什么影响接收：DDR 三分是论文的唯一核心贡献（作者明确说 "our contributions are empirical"），如果三分的存在性论证不充分，论文的 novelty 就成问题。
- 建议修改方向：(a) 提供 gap statistics / silhouette analysis / clustering evidence 证明三分在特征空间中是自然 emerge 的而非人为划分；(b) 或者在一个 held-out 数据集（不同 generator/domain）上预注册阈值并验证三分结构的 replicability；(c) 或者将 DDR 重新定位为 descriptive framework 而非 discovery，降低 novelty claim 的强度。

**N2 [critical] 特征选择过程不透明，存在循环论证风险**
- 具体位置：§3.3 (Feature Extraction)
- 问题：论文说 7 个特征 "motivated by two complementary views of distributional drift"（§3.3 L30-31），但没有说明：(a) 是否存在一个更大的初始特征集被缩减？(b) 特征选择是在 DDR 分析之前还是之后确定的？(c) 是否有被排除的特征因不符合三分结构而被丢弃？如果特征是在观察到 DDR 模式后精心挑选的（选那些恰好符合 drifting/stationary 分类的），则三分结构的整洁性是循环论证的产物。
- entropy_min 的处理特别可疑：论文承认它几乎完全冗余（LOFO ΔF1=+0.01pp），但仍保留的理由是 "completes the four-number NLL summary"（§3.3 L50）。这像是为了维持三分结构（3/1/3）的对称性而保留的。
- 建议：明确报告特征选择的时间线和过程。如果是迭代的（先选特征再观察 DDR），说明哪些特征被考虑过但排除了、为什么。

**N3 [critical] 实际应用价值存疑：base model 限制 + 负面 downstream 结果**
- 具体位置：§5 Discussion, Appendix L (Downstream Utility), Limitations
- 问题：(a) Instruction tuning 使信号严重退化——OLMo-Instruct LOGO F1 从 0.763 降至 0.338（§5 L9），而现实中部署的 LLM 几乎都是 instruction-tuned 的。(b) Downstream utility 实验（Appendix L）得到明确的负面结果：depth-aware curation 在等量数据下不优于 random subsampling（PPL 2.387 vs 2.367，TOST 确认等价）。(c) 这两个结果组合起来意味着：方法在实际场景（instruct model）中不可用，即使可用也没有实际用途（depth 信息不改善训练质量）。
- 为什么影响接收：如果论文的主要价值是 empirical contribution（DDR 三分），但该发现既不能应用于实际场景也不能指导数据策略，那对 NLP 社区的实际影响极为有限。
- 建议：(a) 将论文更明确地定位为 scientific contribution（理解递归生成的本质），弱化 data governance/provenance 动机；(b) 或者提供至少一个 positive downstream application（例如 recursive generation 检测用于 training data audit、contamination detection）；(c) 考虑添加 at least 一个 instruct model 的成功案例（哪怕是受限条件下）来证明方向可行。

---

#### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Table 1 vs Table 2 binary F1 不一致，评估协议差异解释不清**
- 具体位置：Table 1 (binary F1=0.694), Table 2 (7-feature binary F1=0.705)
- 问题：同一个方法在两张表中 binary F1 相差 1.1pp。Table 2 caption 说 "pooled evaluation; slightly higher than per-generator macro average in Table 1"，但这意味着 Table 2 的 LOGO 是将所有 fold 的 predictions 拼接后计算一个 F1，而 Table 1 是先算每个 generator 的 F1 再 macro-average。对于想要 reproduce 的读者，这个区别非常关键但没有在方法论中明确说明。
- 建议：在 §3.4 的 metrics 段落中明确定义 "pooled LOGO F1" vs "macro-averaged LOGO F1" 的区别，并在所有表格中统一标注使用的是哪一种。

**W2 [warning] TTR 和 hapax_ratio 高度冗余（r=0.97），膨胀了 DDR 的 drifting 组计数**
- 具体位置：Appendix O (Feature Correlation), §4.2
- 问题：TTR 和 hapax_ratio 的 Pearson 相关 r=0.97，本质上是同一个信号。论文承认 "reducing effective dimensionality to ≈5"（§4.2 L79），但仍将它们计为两个独立的 drifting features。这使得 DDR 的 "3 drifting / 1 intermediate / 3 near-stationary" 叙事在技术上应该是 "2 independent drifting / 1 intermediate / 3 near-stationary"（或 2.5/1/3），削弱了三分的对称性和说服力。
- 建议：在报告 DDR 时明确说明有效独立特征数，或在主文中讨论 TTR 和 hapax 的冗余性如何影响 DDR 叙事。

**W3 [warning] Temperature sensitivity 限制了方法的普适性声明**
- 具体位置：§4.2 Temperature sensitivity, Appendix G
- 问题：t=0.9 导致所有 4 个测试的 generator 损失 9.3-26.0pp binary F1。OLMo 在 t=0.9 下降至 0.453，接近随机。这意味着方法只在 t∈[0.5, 0.7] 范围内可靠——但实际应用中温度参数未知且不可控。论文标题和摘要没有提及这个限制。
- 建议：在 abstract 或 introduction 中明确提及温度范围限制，如 "under standard decoding (t≤0.7)" 已在 abstract 中出现但不够醒目。

**W4 [warning] Cross-domain 实验使用了不同的解码参数**
- 具体位置：Appendix I (Cross-Domain)
- 问题：Cross-domain 实验使用 t=1.0, top-p=1.0，而主实验使用 t=0.7, top-p=0.9。这引入了一个 confound：cross-domain 的结果（binary F1>0.73）可能部分归因于高温度产生的更大 distributional divergence（论文自己在 domain×temperature interaction 段落承认了这一点），而非 depth signal 的跨域泛化。
- 建议：在 t=0.7 下重复 cross-domain 实验（或者至少报告两个温度的完整结果），确认深度信号本身的跨域泛化。

**W5 [warning] TOST 等价性阈值选择缺乏 application-specific 论证**
- 具体位置：Appendix Q (TOST), Appendix L (Downstream TOST)
- 问题：TOST 使用 ε=|d|<0.20（"small effect" 惯例值），但没有论证为什么 d=0.20 是 depth classification 场景下的合适等价边界。更关键的是，tail_decay 仅在 4/8 generator 上通过等价性检验，entropy_max 在 6/8 上通过。这意味着 near-stationary 组中只有 entropy_min 是真正跨 generator 稳定的，tail_decay 的 "near-stationary" 标签对 Pythia-2.8B/1B、OLMo、Llama 并不成立。
- 建议：讨论 tail_decay 在 4/8 generator 上不满足等价性的含义。考虑是否应该将 tail_decay 重新分类为 intermediate 或至少标注 "*" 表示有条件的 near-stationary。

**W6 [warning] "entropy" 术语混用**
- 具体位置：§3.3 L42-43
- 问题：论文用 "entropy" 指代 per-token NLL，并承认 "these are point-wise NLL values, not Shannon entropy of the full distribution"。但全文 feature 名字（entropy_mean, entropy_std 等）和大量讨论仍使用 "entropy"。对信息论背景的读者，这会造成持续的认知摩擦。虽然声明了这是 shorthand，但在一篇以统计分析为核心的论文中，术语精确性很重要。
- 建议：考虑在 feature 命名中使用 "NLL" 替代 "entropy"（如 nll_mean, nll_std），或在 feature extraction 部分更突出地标注这一区分。

---

#### 小问题（不影响接收）

- **M1**: Abstract 报告 F1=0.694 但未给置信区间，而正文 Table 1 给出 CI [.688, .700]。
- **M2**: Appendix 实验使用的 generator 子集不一致（6-gen vs 8-gen），虽然每张表都标注了，但导致跨附录的数字难以直接比较。正文应在一处集中说明这个历史原因。
- **M3**: Qualitative example（Appendix S）展示的 gen-2 文本是极端退化的重复（"God of the Sky and the Goddess of the Earth" 反复出现），这可能不是困难案例的代表。建议增加一个更 subtle 的例子。
- **M4**: OLMo temperature 实验使用了不同版本的模型（OLMo-2-0425-1B vs OLMo-2-1B-hf），虽然有脚注说明，但这引入了一个未控制的变量。
- **M5**: 论文正文 6 页，充分利用了 8 页限制的空间；但大量关键分析放在 appendix 中（length control, seed control, TOST, downstream utility），建议考虑将最关键的 1-2 个控制实验提到正文中。

---

### Questions for Authors

**Q1**: 7 个特征是否是从一个更大的候选集中选出的？如果是，初始集有多少特征？淘汰标准是什么？特征选择是在 DDR 分析之前还是之后最终确定的？

**Q2**: DDR 三分是否可以通过无监督方法（如对 7 个特征的 depth-sensitivity metrics 做 clustering）自动 emerge？是否尝试过？

**Q3**: 论文提到 Qwen3-1.7B 和 OLMo-2-1B 在温度敏感性上表现相反（§4.2），推测是 model family effect。是否有进一步的证据排除 tokenizer difference 作为解释？

**Q4**: Cross-model chains（binary F1=0.764）使用 5 个 generator，而 LOGO（binary F1=0.694）使用 8 个 generator。5-generator LOGO average 是 0.734（§4.1 L14）。请确认：cross-model chains 的提升（0.764 vs 0.734）是来自 protocol difference（所有 generator 都在 training 中出现）还是 generator mixing 本身增强了信号？

**Q5**: 对于 instruction-tuned models，entropy_mean 的 ρ 符号反转（+0.48 vs -0.60）。这是否意味着 instruct tuning 产生了一种 "anti-DDR" 模式？如果是，这个发现本身是否有独立的分析价值？

---

### Missing References

无显著遗漏。论文引用覆盖全面。建议考虑以下补充引用（非必须）：
- Mitchell et al. (2023), "DetectGPT" 的后续工作（DNA-GPT 已引用）
- 关于 iterative generation 在 image domain 的 parallel work（如 StableRep 等），可以在 model collapse 段落中提供更广的 context

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有统计支撑（多指标交叉验证 DDR、控制实验排除 confounds），但 DDR 阈值 post-hoc、特征选择透明度不足、tail_decay 在 4/8 generator 上不满足等价性。方法论整体扎实但有局部缺口。 |
| Excitement | 2.5/5 | 任务定义有新意（depth classification vs binary detection），DDR 三分是有趣的 empirical finding。但 base-model-only 限制严重制约实际影响，downstream utility 为负面结果，F1=0.694 的实用性有限。 |
| Reproducibility | 4/5 | 超参数、数据构造、评估协议描述详尽。代码和数据承诺开源。所有统计检验有明确的参数和 correction 方法。OLMo 版本差异是小瑕疵。 |
| Reviewer Confidence | 4/5 | 仔细阅读了正文和全部 20 个 appendix，核实了统计方法和评估协议。对 AI text detection 和统计方法有足够的领域知识。 |

---

## 总体评分

**Overall**: 3.0 / 5 — Findings（可被 Findings 接收）

**一句话总结**: 论文提出了有价值的任务定义（generation depth classification）和有趣的 empirical finding（DDR 三分结构），统计分析扎实且 limitations 诚实，但 base-model-only 限制严重制约实际影响，DDR 阈值的 post-hoc 性质和特征选择透明度不足削弱了 primary contribution 的说服力，downstream utility 的负面结果进一步降低了实用价值。作为 Findings 论文可以贡献知识，但方法论和影响力不足以支撑主会议接收。

---

### 主要优势（总结）

1. 任务定义（depth classification）填补了 binary detection 和 model collapse 之间的空白
2. 控制实验设计出色（seed control, length control, cross-reference validation）
3. 统计方法运用规范（TOST, bootstrap CI, Bonferroni, McNemar）
4. 科学诚实度高，所有重要 limitation 都在正文中讨论
5. 引用体系完整，与 concurrent work 的比较公正

### 改稿优先级

1. **最高**：回应 N1（DDR 阈值论证）和 N2（特征选择透明度）——这两个问题直接影响 primary contribution 的可信度
2. **高**：回应 N3（applicability / downstream utility）——需要重新定位论文的 motivation 或提供正面 application evidence
3. **中**：修复 W1-W6（metrics 一致性、冗余特征讨论、温度限制标注、术语）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1274 · 2026-05-18T23:30:51.341567+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1275 · 2026-05-18T23:30:53.895618+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

报告核心判断：**Overall 3.0/5（Findings）**。

三个 Must-Fix 问题：
1. DDR 三分阈值缺乏先验基础，存在 post-hoc 风险——这是论文 primary contribution，需要更强的存在性论证
2. 特征选择过程不透明，可能存在循环论证
3. Base model 限制 + 负面 downstream 结果组合严重制约实际影响

六个 Should-Fix 问题涉及 metrics 不一致、TTR/hapax 冗余、温度敏感性、cross-domain confound、TOST 阈值选择、entropy 术语混用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1276 · 2026-05-18T23:31:00.409499+00:00_

Reviewer 1 报告已收。等待 Reviewer 2 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 115

## Round 115

6 recorded events


### User

_source line 1277 · 2026-05-18T23:34:29.211915+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall Assessment**: 3.0 / 5 — Findings（可被 Findings 接收）
**Confidence**: 4 / 5

**一句话总结**: 问题定义（generation depth classification）有价值且实验设计严谨，但核心发现（DDR tri-partition）是描述性而非解释性的，加上仅限 base model 的 scope 严重限制实际影响力，贡献厚度不足以支撑主会议长论文。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论严谨（LOGO、bootstrap CI、McNemar、TOST），controls 充分；但部分 claim 相对证据略有 overstate（DDR "novel"、practical motivation vs. negative downstream result） |
| Excitement | 2.5/5 | 问题本身有趣（binary → depth），但 DDR 发现缺乏理论深度，base-model-only scope 限制实用性，downstream utility 实验为负面结果 |
| Reproducibility | 4.0/5 | 模型、数据、超参均明确说明，承诺代码公开，计算预算透明（62 GPU-hours） |
| Overall Assessment | 3.0/5 | Borderline Findings — 实验质量高但贡献偏薄 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR tri-partition 的新颖性不足以支撑核心贡献

- 具体位置：§1 (Introduction, contributions list), §4.2 (Differential Depth Response), §5 (Discussion)
- 问题：DDR 的本质是将 7 个特征按 depth correlation 分为三组。NLL mean 随 recursive generation 下降（文本变得更 "model-like"）和 TTR/hapax 下降（词汇多样性压缩）在 model collapse 文献中已有充分文档 [curse_of_recursion, curious_decline, writing_diversity]。论文声称 "the structured tri-partition and its exploitation for depth classification have not been previously reported"（§1 第14行），但这一 tri-partition 本质上是一个统计分类——测量哪些特征变化、哪些不变——而非一个有理论支撑的发现。intermediate 类别仅有一个成员（entropy_std），进一步削弱了 partition 的结构性。论文自述 "Our contributions are empirical rather than methodological"（§1 第20行），这诚实但也准确指出了核心弱点。
- 为什么影响接收：EMNLP 长论文需要足够的 intellectual contribution。当核心发现是描述性的且无理论解释时，即使实验再充分也难以达到 Conference 标准。
- 建议修改方向：(1) 提供 DDR tri-partition 的理论解释——为什么 location drift 而 shape stable？§5 仅用一句话 gesture at "softmax architecture and fixed sampling parameters"，这需要严格论证。(2) 或者将贡献重新定位为 benchmark/dataset paper，强调 evaluation suite 和 task formulation 的价值。

**N2** [critical] Base-model-only scope 从根本上限制影响力

- 具体位置：§1 第15行, §5 (Discussion) 第7-11行, §Limitations 第1-9行
- 问题：所有 8 个 generator 均为 base (pretrained) models。Instruct 实验显示 DDR 信号在 instruction tuning 下急剧衰减：OLMo-2-1B-Instruct LOGO F1 从 0.763 降至 0.338，entropy_mean 的 ρ 从 −0.6 反转至 +0.48。实际部署的 LLM 文本几乎全部来自 instruction-tuned models。论文将 base model 研究定位为 "isolating the generation mechanism"，但如果 mechanism 在 instruction tuning 下质性改变（6/7 特征方向反转），那么 base model 上的发现可能无法泛化，削弱了 DDR 作为 "recursive generation 的内在属性" 的定位。
- 为什么影响接收：实用相关性是 EMNLP 的重要评判标准。一个仅在 base model 上有效的方法/发现，其受众和影响力非常有限。
- 建议修改方向：(1) 提供至少 2-3 个 instruct model 的系统性实验（不仅是 Limitations 中的初步结果），分析 DDR 在 instruct 下为何失效。(2) 若无法扩展到 instruct，将论文明确定位为面向 pretraining data pipeline 的 quality signal（而非通用 provenance 工具），并在 Introduction 动机中收窄 scope。

**N3** [critical] 贡献列表对长论文过于单薄

- 具体位置：§1 第20-24行（contribution list）
- 问题：仅列出 2 条贡献：(1) task formulation + evaluation suite, (2) DDR characterization。对于一篇 8 页正文 + 16 页附录的长论文，两条贡献不足以支撑篇幅。Task formulation（3-class instead of binary）是直接的扩展；DDR 如 N1 所述是描述性发现。相比之下，QLoRA 实验（Appendix E）显示 3-class F1 从 0.789 跃升至 0.905（+11.6 pp），证明 token-level 表示中存在更丰富的 depth signal，但这个结果被埋在附录中。
- 为什么影响接收：审稿人和 AC 会评估 contribution-to-length ratio。贡献列表过短会导致 "could have been a short paper" 的批评。
- 建议修改方向：(1) 将 QLoRA end-to-end 结果提升到正文作为第三个贡献。(2) 将 cross-model chain 实验或 temperature sensitivity 分析作为独立贡献。(3) 或考虑改投 short paper。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Downstream utility 实验结果为负，削弱 Introduction 的 practical motivation

- 具体位置：Appendix L (Downstream Utility), §1 第7行 ("such text already re-enters training pipelines at scale")
- 问题：Introduction 以 data provenance 和 training pipeline 质量为动机，但 Appendix L 的实验明确显示 depth-aware curation 不优于随机采样（random subsample ppl 2.367 vs. depth 0-1 ppl 2.387）。这一负面结果直接否定了"depth classification 对 data curation 有价值"的隐含承诺。该结果被埋在附录中，正文仅用一句话提及（§4.3 最后一行："Preliminary downstream evaluation finds that depth composition does not determine training utility at fixed sample count"）。
- 建议：(1) 在正文 Discussion 中更显著地讨论这一负面结果及其含义。(2) 调整 Introduction 动机，弱化 data curation 方面的暗示。

**W2** [warning] 实验中 generator subset 不一致造成混乱

- 具体位置：§3.4 第76-77行, Table 1 footnote, Appendix E (QLoRA), main.tex 第40-41行
- 问题：不同实验使用 5/6/8 个 generators：main LOGO 用 8 个，cross-model chains 用 5 个，QLoRA 用 6 个，部分 appendix 用 6 个。main.tex 第40-41行的 appendix note 试图澄清但增加了复杂性。Cross-model binary F1 = 0.764（5-gen）vs. LOGO binary F1 = 0.694（8-gen）的比较因 subset 不同而难以解读。Table 1 (0.694) vs. Table 2 (0.705) 的 7-feature binary F1 差异（pooled vs. macro average）进一步增加困惑。
- 建议：(1) 统一核心实验使用 8-gen subset（或标明这不可能的原因）。(2) 在一个集中的表格中列出每个实验使用的 generator subset。(3) Table 1 和 Table 2 应使用相同的 aggregation 方式。

**W3** [warning] 温度敏感性暗示 DDR 可能是参数依赖而非内在属性

- 具体位置：§4.2 (Temperature sensitivity), Appendix H (Sampling Sensitivity)
- 问题：所有 4 个测试 generator 在 t=0.9 时损失 9.3-26.0 pp binary F1。论文将 DDR 描述为 "consistent with recursive generation shifting the NLL location while distributional shape remains stable"（§3.3 第66行），这暗示 DDR 是 recursive generation 的内在属性。但 t=0.9 时信号大幅衰减说明 DDR 的强度高度依赖 sampling parameters，削弱了 "intrinsic" 的定位。
- 建议：在 Discussion 中明确区分 DDR 作为现象（parameter-dependent）和 DDR 作为 property of recursive generation（intrinsic）。目前措辞倾向后者但证据只支持前者。

**W4** [warning] Paraphrastic chain 结果在附录中缺乏支撑

- 具体位置：§4.2 第88行 ("Paraphrastic chains yield weaker signal (binary F1 = 0.671 vs. 0.749 for continuation)")
- 问题：正文报告了 paraphrastic chain 的 binary F1 = 0.671，但 Appendix C (Prompt Type Generalization) 仅涵盖 continuation、elaboration、rewriting 三种 prompt type，未包含 paraphrastic chain 的详细方法和结果。该数字在正文中无完整的实验支撑。
- 建议：将 paraphrastic chain 实验纳入 Appendix C 并提供完整的实验细节。

**W5** [warning] "Entropy" 术语使用造成持续混淆

- 具体位置：§3.3 第42行 ("We use 'entropy' as shorthand for token-level NLL")
- 问题：所有特征命名（entropy_mean, entropy_std, entropy_max, entropy_min）和全文讨论使用 "entropy" 指代 per-token NLL。尽管有免责声明，但 entropy 在信息论中有明确定义（Shannon entropy of the full output distribution），与 point-wise NLL 不同。This creates persistent confusion，特别是在讨论 "distributional shape" 时——读者可能将 entropy_std 理解为 distribution entropy 的 std，而非 NLL sequence 的 std。
- 建议：考虑全文改用 "NLL" 或 "surprise" 以避免歧义，或至少在 Section 3.3 中更明确地区分。

---

## 小问题（不影响接收）

1. **PDF 格式 bug**：第 24 页 Figure 9 caption 下方有游离的 "chance" 文字，疑似 LaTeX 排版残留。
2. **Appendix 数量过多**（20+ 节，pages 13-29）：建议合并相关分析（如 seed control + TOST + ablation → "Robustness Controls"），减少到 10-12 个核心 appendix。
3. **附录中 generator subset 不一致**（main.tex 第40-41行的 note 试图统一说明但不够清晰）：每个 appendix table 应在 caption 中明确标注使用的 generator subset。
4. **Figure 2 (page 8)** 中 "Binary F1 (gen-1 vs. gen-2+)" 标签字体偏小，打印后可读性受限。
5. **.tex 注释中的 em-dash**（abstract.tex:1, appendix_length.tex:1, main.tex:1）：不影响渲染，但建议清理。
6. **Reference verification**：67 条 bib 引用，无 orphan/missing。OpenAlex 未找到 7 条（含 DetectGPT, XGBoost, Pythia 等知名论文——likely API lookup issues，非引用问题）。5 条 mismatch（字段差异，需人工确认）。引用数量达到 EMNLP 标准。

---

## 缺失引用

1. **Synthetic data detection in training pipelines**: 近期有较多工作关注 pre-training data 中 synthetic content 的检测和过滤 [如 FineWeb filtering pipeline, Dolma curation]，论文 §2.4 仅引用了 DSIR/QuRating/CCNet，缺少更直接的 synthetic data contamination detection 工作。
2. **MTLD/HD-D 在 LLM detection 中的应用**: §2.3 提到 TTR 和 hapax "suffice for depth discrimination" 并引用 MTLD/HD-D，但未讨论这些更高级指标是否可能提供额外信号。考虑到 TTR 和 hapax 高度相关（r=0.97），替代指标可能有价值。
3. **Concurrent work on recursive generation quality**: 除 Broken Telephone 和 Markovian Chains 外，是否有 2025-2026 年的其他相关工作关注 iterative/recursive generation 的分布特性？

---

## 主要优势

1. **实验方法论设计严谨**：LOGO cross-validation、length-matched subsampling、independent-seed control、perturbation robustness、seed-level demeaning——每一个潜在 confound 都有对应的 control experiment。这是该论文最大的亮点。
2. **统计严谨性**：Bootstrap 95% CIs、McNemar tests、TOST equivalence testing、Bonferroni correction、class-balanced subsampling——统计实践远超该领域平均水平。
3. **诚实透明**：明确承认 base-model scope、moderate performance、temperature sensitivity、negative downstream result。不过度宣传。
4. **Task formulation 有价值**：从 binary detection 到 depth classification 的扩展是自然但有意义的，开辟了一个新方向。
5. **QLoRA 实验**（Appendix E）有效验证了 depth signal 的真实性，3-class F1 从 0.789 跳到 0.905。
6. **Related Work 完整且定位准确**：与 Broken Telephone / Markovian Chains 的对比清晰，不 overstate 自身贡献。
7. **写作质量良好**：几乎无 AI 写作痕迹（无 em-dash、无 -ing 分词结尾堆砌、分段自然），文本流畅度明显高于平均投稿。
8. **格式合规**：正文 ≤8 页（Limitations/Ethics 在 page 8-9，不计入限制），匿名、行号、ACL review mode 均正确。Limitations section 详尽。

---

## Framing 一致性评估

- **Abstract → Introduction**：一致，均以 recursive chain 和 depth classification 开篇，scope 限制（base model）在 Abstract 最后一句和 Introduction §1 第15行声明。
- **Introduction → Method**：贡献声明与 Method 实际内容一致。
- **Method → Results**：DDR characterization 在 Method 中定义、Results 中验证，逻辑连贯。
- **Results → Discussion**：Discussion 正确回收 temperature sensitivity 和 instruct degradation 的结果。
- **标题与内容**："Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"——标题准确反映内容，"Base LLM" 明确 scope。

**Framing 张力**：论文在 "empirical study" 和 "method paper" 之间摇摆。Introduction 说 "contributions are empirical"，但 Table 2 的 baseline comparison 和 inference cost 讨论暗示方法竞争力。Discussion 又回到分析性。这种张力不致命，但使论文的 identity 模糊——审稿人可能从方法论角度批评 novelty 不足，也可能从 empirical study 角度批评 insight 不够深入。建议明确选择一个定位并贯穿全文。

---

## 格式合规性检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| ACL template ([review] mode) | ✓ | `\usepackage[review]{acl}` |
| 正文 ≤8 页 | ✓ | 正文至 page 8 底部，Limitations/Ethics 在 pages 8-9（不计入限制）|
| 行号 | ✓ | `\linenumbers` 全文可见 |
| 匿名化 | ✓ | `\author{Anonymous}`，无自识别信息 |
| 附录 double-column | ✓/⚠ | 大部分 double-column，部分 figure pages (21-25) 使用 full-width `figure*`（可接受但需注意 2025 年 7 月新规）|
| Limitations section | ✓ | 详尽（32 行），覆盖所有主要限制 |
| Ethics statement | ✓ | 完整，含 licenses、compute budget、software versions |
| Reference 格式 (natbib) | ✓ | `acl_natbib.bst` |
| Responsible NLP Checklist | — | 未见（ARR 可能在 OpenReview 系统中单独提交）|

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-18T23:35:17.670249+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意，并说明理由\n- **[REBUT]**：反驳，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR tri-partition 的新颖性不足以支撑核心贡献\n- DDR 本质上是将 7 个特征按 depth correlation 分为三组。NLL mean 下降和 TTR/hapax 下降在 model collapse 文献中已有充分文档。\"structured tri-partition and its exploitation for depth classification have not been previously reported\"（§1 第14行），但 tri-partition 本质是统计分类而非有理论支撑的发现。intermediate 仅一个成员（entropy_std），削弱 partition 结构性。\n- 建议：(1) 提供 DDR tri-partition 理论解释——为什么 location drift 而 shape stable？(2) 或定位为 benchmark/dataset paper。\n\n**N2** [critical] Base-model-only scope 从根本上限制影响力\n- 所有 8 个 generator 均为 base models。Instruct 实验：OLMo-2-1B-Instruct LOGO F1 从 0.763 降至 0.338，entropy_mean ρ 从 −0.6 反转至 +0.48。实际部署 LLM 几乎全部 instruction-tuned。如果 mechanism 在 instruction tuning 下质性改变（6/7 特征方向反转），base model 发现可能无法泛化。\n- 建议：(1) 提供 2-3 个 instruct model 系统性实验，(2) 或定位为 pretraining data pipeline quality signal。\n\n**N3** [critical] 贡献列表对长论文过于单薄\n- 仅 2 条贡献：task formulation + DDR characterization。对 8+16 页论文不足。QLoRA 实验（Appendix E）3-class F1 从 0.789 到 0.905（+11.6pp），但埋在附录。\n- 建议：(1) 将 QLoRA 提升到正文作为第三个贡献，(2) 或考虑改投 short paper。\n\n### Should-Fix 问题\n\n**W1** [warning] Downstream utility 负面结果削弱 Introduction practical motivation\n- Appendix L 显示 depth-aware curation 不优于随机采样。但 Introduction 以 data provenance 和 training pipeline 质量为动机。\n- 建议：调整 Introduction 动机，弱化 data curation 暗示。\n\n**W2** [warning] Generator subset 不一致造成混乱（5/6/8-gen）\n- LOGO 用 8 gen，cross-model 用 5，QLoRA 用 6。Table 1 vs Table 2 aggregation 方式不同。\n- 建议：统一或在集中表格中列出每个实验的 subset。\n\n**W3** [warning] 温度敏感性暗示 DDR 是参数依赖而非内在属性\n- t=0.9 时所有 4 个 generator 损失 9.3-26.0pp。DDR 描述倾向 \"intrinsic property\" 但证据只支持 \"parameter-dependent phenomenon\"。\n\n**W4** [warning] Paraphrastic chain 结果在附录中缺乏支撑\n- 正文 §4.2 报告 paraphrastic binary F1=0.671，但 Appendix C 仅覆盖 continuation/elaboration/rewriting，未包含 paraphrastic chain 详细方法和结果。\n\n**W5** [warning] \"Entropy\" 术语使用造成持续混淆\n- 所有特征命名使用 \"entropy\" 但实际是 per-token NLL，与信息论 Shannon entropy 不同。\n\n### 小问题\n1. PDF 格式 bug：第 24 页 Figure 9 caption 下方有游离的 \"chance\" 文字\n2. Appendix 数量过多（20+ 节），建议合并到 10-12 个\n3. Figure 2 标签字体偏小\n4. .tex 注释中的 em-dash\n5. Reference 基本完整，7 条 OpenAlex 未找到（likely API issues）\n\n### 缺失引用\n1. Synthetic data contamination detection 工作（FineWeb filtering, Dolma curation 之外的）\n2. MTLD/HD-D 在 LLM detection 中的应用\n3. 2025-2026 其他 recursive generation 分布特性工作\n\n### Framing 评估\n论文在 \"empirical study\" 和 \"method paper\" 之间摇摆，identity 模糊。\n\n---\n\n请对每个 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT]，附上你的理由和证据。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意，并说明理由\n- **[REBUT]**：反驳，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR tri-partition 的新颖性不足以支撑核心贡献\n- DDR 本质上是将 7 个特征按 depth correlation 分为三组。NLL mean 下降和 TTR/hapax 下降在 model collapse 文献中已有充分文档。\"structured tri-partition and its exploitation for depth classification have not been previously reported\"（§1 第14行），但 tri-partition 本质是统计分类而非有理论支撑的发现。intermediate 仅一个成员（entropy_std），削弱 partition 结构性。\n- 建议：(1) 提供 DDR tri-partition 理论解释——为什么 location drift 而 shape stable？(2) 或定位为 benchmark/dataset paper。\n\n**N2** [critical] Base-model-only scope 从根本上限制影响力\n- 所有 8 个 generator 均为 base models。Instruct 实验：OLMo-2-1B-Instruct LOGO F1 从 0.763 降至 0.338，entropy_mean ρ 从 −0.6 反转至 +0.48。实际部署 LLM 几乎全部 instruction-tuned。如果 mechanism 在 instruction tuning 下质性改变（6/7 特征方向反转），base model 发现可能无法泛化。\n- 建议：(1) 提供 2-3 个 instruct model 系统性实验，(2) 或定位为 pretraining data pipeline quality signal。\n\n**N3** [critical] 贡献列表对长论文过于单薄\n- 仅 2 条贡献：task formulation + DDR characterization。对 8+16 页论文不足。QLoRA 实验（Appendix E）3-class F1 从 0.789 到 0.905（+11.6pp），但埋在附录。\n- 建议：(1) 将 QLoRA 提升到正文作为第三个贡献，(2) 或考虑改投 short paper。\n\n### Should-Fix 问题\n\n**W1** [warning] Downstream utility 负面结果削弱 Introduction practical motivation\n- Appendix L 显示 depth-aware curation 不优于随机采样。但 Introduction 以 data provenance 和 training pipeline 质量为动机。\n- 建议：调整 Introduction 动机，弱化 data curation 暗示。\n\n**W2** [warning] Generator subset 不一致造成混乱（5/6/8-gen）\n- LOGO 用 8 gen，cross-model 用 5，QLoRA 用 6。Table 1 vs Table 2 aggregation 方式不同。\n- 建议：统一或在集中表格中列出每个实验的 subset。\n\n**W3** [warning] 温度敏感性暗示 DDR 是参数依赖而非内在属性\n- t=0.9 时所有 4 个 generator 损失 9.3-26.0pp。DDR 描述倾向 \"intrinsic property\" 但证据只支持 \"parameter-dependent phenomenon\"。\n\n**W4** [warning] Paraphrastic chain 结果在附录中缺乏支撑\n- 正文 §4.2 报告 paraphrastic binary F1=0.671，但 Appendix C 仅覆盖 continuation/elaboration/rewriting，未包含 paraphrastic chain 详细方法和结果。\n\n**W5** [warning] \"Entropy\" 术语使用造成持续混淆\n- 所有特征命名使用 \"entropy\" 但实际是 per-token NLL，与信息论 Shannon entropy 不同。\n\n### 小问题\n1. PDF 格式 bug：第 24 页 Figure 9 caption 下方有游离的 \"chance\" 文字\n2. Appendix 数量过多（20+ 节），建议合并到 10-12 个\n3. Figure 2 标签字体偏小\n4. .tex 注释中的 em-dash\n5. Reference 基本完整，7 条 OpenAlex 未找到（likely API issues）\n\n### 缺失引用\n1. Synthetic data contamination detection 工作（FineWeb filtering, Dolma curation 之外的）\n2. MTLD/HD-D 在 LLM detection 中的应用\n3. 2025-2026 其他 recursive generation 分布特性工作\n\n### Framing 评估\n论文在 \"empirical study\" 和 \"method paper\" 之间摇摆，identity 模糊。\n\n---\n\n请对每个 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT]，附上你的理由和证据。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-18T23:35:53.468359+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 35798
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-18T23:35:54.271827+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意，并说明理由\n- **[REBUT]**：反驳，并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 阈值缺乏先验理论/经验基础，存在 post-hoc 风险\n- Cohen's d 阈值（drifting: d>0.75, near-stationary: d<0.10）和 Spearman ρ 阈值（drifting: |ρ|>0.60, near-stationary: |ρ|<0.10）。切分点无理论推导或先验经验支撑。\"shifting thresholds by ±0.10 does not alter grouping\"（§4.2 L67）仅说明三分对阈值微调稳定，不说明三分是数据中的自然结构。\n- 核心担忧：如果三分是 post-hoc 从数据中\"读出来\"的，DDR 作为 primary contribution 的 novelty 就减弱了。\n- 建议：(a) gap statistics / silhouette analysis / clustering evidence 证明三分自然 emerge，(b) 在 held-out 数据集上预注册阈值验证 replicability，(c) 或将 DDR 定位为 descriptive framework。\n\n**N2** [critical] 特征选择过程不透明，存在循环论证风险\n- 没说明：(a) 是否存在更大初始特征集？(b) 特征选择在 DDR 分析前还是后？(c) 是否有被排除的特征因不符合三分结构被丢弃？\n- entropy_min 特别可疑：LOFO ΔF1=+0.01pp 但保留理由是 \"completes the four-number NLL summary\"。像是为维持 3/1/3 对称性。\n- 建议：明确报告特征选择时间线和过程。\n\n**N3** [critical] 实际应用价值存疑：base model 限制 + 负面 downstream 结果\n- (a) Instruct: OLMo-Instruct F1 从 0.763 降至 0.338。(b) Downstream: depth-aware curation 不优于 random（PPL 2.387 vs 2.367, TOST 确认等价）。(c) 两个结果组合意味着方法在实际场景不可用且无实际用途。\n- 建议：(a) 重定位为 scientific contribution，弱化 data governance 动机，(b) 或提供 positive downstream application，(c) 添加 instruct 成功案例。\n\n### Should-Fix 问题\n\n**W1** [warning] Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705），评估协议差异解释不清\n- 同方法两表相差 1.1pp。pooled vs macro-average 区别对 reproduce 很关键但未在方法论中明确定义。\n\n**W2** [warning] TTR 和 hapax_ratio 高度冗余（r=0.97），膨胀了 DDR drifting 组计数\n- 本质同一个信号。\"reducing effective dimensionality to ≈5\"（§4.2 L79）但仍计为两个独立 drifting features。\n\n**W3** [warning] Temperature sensitivity 限制普适性声明\n- t=0.9 导致所有 4 个 generator 损失 9.3-26.0pp。方法只在 t∈[0.5, 0.7] 可靠，但实际应用中温度未知。\n\n**W4** [warning] Cross-domain 实验使用不同解码参数（t=1.0 vs t=0.7）\n- Cross-domain 使用 t=1.0, top-p=1.0，主实验 t=0.7, top-p=0.9。引入 confound。\n\n**W5** [warning] TOST 等价性阈值选择缺乏 application-specific 论证\n- ε=|d|<0.20 惯例值，未论证为何适合 depth classification。tail_decay 仅 4/8 generator 通过等价性检验。\n\n**W6** [warning] \"entropy\" 术语混用\n- 用 \"entropy\" 指代 per-token NLL，与信息论 Shannon entropy 不同。\n\n### 小问题\n- M1: Abstract F1=0.694 无 CI，正文 Table 1 有 CI [.688, .700]\n- M2: Appendix generator subset 不一致（6-gen vs 8-gen）\n- M3: Qualitative example 过于极端，建议增加 subtle 案例\n- M4: OLMo temperature 实验使用不同版本模型\n- M5: 大量关键分析放在 appendix，建议提升 1-2 个到正文\n\n### Questions\n- Q1: 7 特征是否从更大候选集选出？\n- Q2: DDR 三分可否通过无监督方法自动 emerge？\n- Q3: Qwen/OLMo 温度敏感性差异是否可能是 tokenizer 导致？\n- Q4: Cross-model chains 的提升来自 protocol difference 还是 generator mixing？\n- Q5: Instruct models 的 \"anti-DDR\" 模式是否有独立分析价值？\n\n---\n\n请对每个 N1-N3、W1-W6 逐条给出 [AGREE] 或 [REBUT]，附上你的理由和证据。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意，并说明理由\n- **[REBUT]**：反驳，并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] DDR 阈值缺乏先验理论/经验基础，存在 post-hoc 风险\n- Cohen's d 阈值（drifting: d>0.75, near-stationary: d<0.10）和 Spearman ρ 阈值（drifting: |ρ|>0.60, near-stationary: |ρ|<0.10）。切分点无理论推导或先验经验支撑。\"shifting thresholds by ±0.10 does not alter grouping\"（§4.2 L67）仅说明三分对阈值微调稳定，不说明三分是数据中的自然结构。\n- 核心担忧：如果三分是 post-hoc 从数据中\"读出来\"的，DDR 作为 primary contribution 的 novelty 就减弱了。\n- 建议：(a) gap statistics / silhouette analysis / clustering evidence 证明三分自然 emerge，(b) 在 held-out 数据集上预注册阈值验证 replicability，(c) 或将 DDR 定位为 descriptive framework。\n\n**N2** [critical] 特征选择过程不透明，存在循环论证风险\n- 没说明：(a) 是否存在更大初始特征集？(b) 特征选择在 DDR 分析前还是后？(c) 是否有被排除的特征因不符合三分结构被丢弃？\n- entropy_min 特别可疑：LOFO ΔF1=+0.01pp 但保留理由是 \"completes the four-number NLL summary\"。像是为维持 3/1/3 对称性。\n- 建议：明确报告特征选择时间线和过程。\n\n**N3** [critical] 实际应用价值存疑：base model 限制 + 负面 downstream 结果\n- (a) Instruct: OLMo-Instruct F1 从 0.763 降至 0.338。(b) Downstream: depth-aware curation 不优于 random（PPL 2.387 vs 2.367, TOST 确认等价）。(c) 两个结果组合意味着方法在实际场景不可用且无实际用途。\n- 建议：(a) 重定位为 scientific contribution，弱化 data governance 动机，(b) 或提供 positive downstream application，(c) 添加 instruct 成功案例。\n\n### Should-Fix 问题\n\n**W1** [warning] Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705），评估协议差异解释不清\n- 同方法两表相差 1.1pp。pooled vs macro-average 区别对 reproduce 很关键但未在方法论中明确定义。\n\n**W2** [warning] TTR 和 hapax_ratio 高度冗余（r=0.97），膨胀了 DDR drifting 组计数\n- 本质同一个信号。\"reducing effective dimensionality to ≈5\"（§4.2 L79）但仍计为两个独立 drifting features。\n\n**W3** [warning] Temperature sensitivity 限制普适性声明\n- t=0.9 导致所有 4 个 generator 损失 9.3-26.0pp。方法只在 t∈[0.5, 0.7] 可靠，但实际应用中温度未知。\n\n**W4** [warning] Cross-domain 实验使用不同解码参数（t=1.0 vs t=0.7）\n- Cross-domain 使用 t=1.0, top-p=1.0，主实验 t=0.7, top-p=0.9。引入 confound。\n\n**W5** [warning] TOST 等价性阈值选择缺乏 application-specific 论证\n- ε=|d|<0.20 惯例值，未论证为何适合 depth classification。tail_decay 仅 4/8 generator 通过等价性检验。\n\n**W6** [warning] \"entropy\" 术语混用\n- 用 \"entropy\" 指代 per-token NLL，与信息论 Shannon entropy 不同。\n\n### 小问题\n- M1: Abstract F1=0.694 无 CI，正文 Table 1 有 CI [.688, .700]\n- M2: Appendix generator subset 不一致（6-gen vs 8-gen）\n- M3: Qualitative example 过于极端，建议增加 subtle 案例\n- M4: OLMo temperature 实验使用不同版本模型\n- M5: 大量关键分析放在 appendix，建议提升 1-2 个到正文\n\n### Questions\n- Q1: 7 特征是否从更大候选集选出？\n- Q2: DDR 三分可否通过无监督方法自动 emerge？\n- Q3: Qwen/OLMo 温度敏感性差异是否可能是 tokenizer 导致？\n- Q4: Cross-model chains 的提升来自 protocol difference 还是 generator mixing？\n- Q5: Instruct models 的 \"anti-DDR\" 模式是否有独立分析价值？\n\n---\n\n请对每个 N1-N3、W1-W6 逐条给出 [AGREE] 或 [REBUT]，附上你的理由和证据。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-18T23:35:55.678744+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1406
}
```

</details>

---


### Assistant

_source line 1282 · 2026-05-18T23:35:58.429675+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1283 · 2026-05-18T23:36:00.992842+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿核心结论：Overall 3.0/5（Findings 水平）**

三个 Must-Fix 问题：
1. **DDR 新颖性不足**——tri-partition 本质是描述性分类而非理论性发现，NLL/TTR 随 recursive generation 漂移在 model collapse 文献中已有记录
2. **Base-model-only scope 根本性限制影响力**——instruct model 下信号急剧衰减（OLMo F1: 0.763→0.338），实际 LLM 文本几乎全来自 instruct models
3. **贡献列表单薄**——仅 2 条贡献对 8+16 页长论文不够，QLoRA 的强结果（+11.6pp）被埋在附录中

主要优势：实验方法论严谨（LOGO、bootstrap、TOST 等控制实验），统计实践远超领域平均水平，写作质量高且诚实透明。Task formulation 本身有价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1284 · 2026-05-18T23:36:05.402800+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1285 · 2026-05-18T23:37:39.909696+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 意见

---

### Must-Fix 问题

**[AGREE] R1-N1: DDR 阈值缺乏先验理论/经验基础，存在 post-hoc 风险**

同意核心判断。论文的 robustness argument（"shifting thresholds by ±0.10 does not alter grouping", §4.2 L67）仅证明 partition 对微调稳定，不证明它是数据中的自然结构。我自己的 N1 也从另一角度指出了同一问题：DDR 本质上是描述性分类而非有理论支撑的发现。

补充两点细微差异：

(1) 论文确实使用了多个独立度量的收敛来支撑 partition（ρ、Cohen's d、KS statistic、Levene test、CV shift，§4.2 L73），且 per-generator TOST（Appendix T, Table）显示 entropy_min 在 8/8 generators 通过等价性检验、entropy_max 在 6/8 通过，而所有 drifting features 在 0/8 通过。这比单一阈值的 post-hoc 分类要强，但 R1 的核心论点仍然成立：没有证据表明"三分"优于"两分"或"连续谱"。

(2) R1 建议的 gap statistics / silhouette analysis 非常到位。如果在 7 维特征空间中对 (ρ, d) 对做 clustering，能否自动 recover 三分结构？这是可验证的。若只 recover 两组（drifting vs. stationary），intermediate 类别（仅 entropy_std 一个成员）的存在理由就更薄弱了。

**[AGREE] R1-N2: 特征选择过程不透明，存在循环论证风险**

同意，这个问题我自己审稿时未充分展开。关键疑点：

(a) §3.3 第32-36行解释特征选择动机为 "interpretable distributional statistics rather than learned representations so that the DDR tri-partition remains transparent"。这隐含地承认特征选择服务于 DDR 叙事。如果 DDR 是 primary contribution，而特征是为了展示 DDR 而选择的，那确实存在循环论证风险。

(b) R1 对 entropy_min 的观察非常敏感。§3.3 第49-50行的保留理由（"LOFO ΔF1=+0.01pp, within bootstrap noise" + "completes the four-number NLL summary"）读起来确实像 post-hoc rationalization。一个对分类无贡献的特征被保留，最合理的解释是它在 DDR 叙事中有位置价值（充实 near-stationary 组），这正是 R1 指出的 3/1/3 对称性问题。

(c) 论文未说明是否测试过其他候选特征（如 MTLD、HD-D、n-gram entropy、repetition rate）。§2.3 提到 "more sophisticated alternatives exist (MTLD, HD-D; MATTR) but TTR and hapax ratio suffice for depth discrimination"，但 "suffice" 是事后判断，不是先验选择。

建议与 R1 一致：需要明确的特征选择时间线和完整候选集报告。

**[AGREE] R1-N3: 实际应用价值存疑**

完全同意。这与我自己的 N2（base-model scope）和 W1（negative downstream result）高度一致。

补充一个 R1 未展开的角度：即使将论文重定位为 scientific contribution（R1 建议 a），DDR 作为 scientific finding 的深度也不足——因为没有理论解释为什么 location drift 而 shape stable（我的 N1）。所以论文同时面临两个方向的困境：作为方法论文缺乏实用性，作为科学发现缺乏理论深度。

R1 建议 (c)（添加 instruct 成功案例）是最有建设性的方向。如果能找到 instruct model 上 DDR 的变体形式（即使 pattern 不同但仍可分类），可以同时解决 applicability 和 novelty 问题。§5 第10行提到 "consistent with instruction tuning shifting the generation attractor rather than destroying the iterative dynamics"，这暗示 instruct 下可能存在不同的但可利用的 depth signal。

---

### Should-Fix 问题

**[AGREE] R1-W1: Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705）**

同意，我也独立提出了这个问题（我的 W2）。Table 1 的 0.694 是 per-generator binary F1 的 macro average（8 个 generator 各自的 binary F1 取平均），Table 2 的 0.705 是 pooled evaluation（所有 generator 的预测合并后计算 binary F1）。Table 1 caption 注释了 "binary F1 is leak-free"，Table 2 caption 注释了 "pooled evaluation; slightly higher than per-generator macro average in Table 1"，但这一关键方法论差异应在 §3.4 (Evaluation Protocol) 中正式定义，而非依赖 caption 注释。同一方法在同一论文中的两个 primary metric 不一致，会严重影响可信度。

**[AGREE] R1-W2: TTR 和 hapax_ratio 高度冗余（r=0.97）**

同意。r=0.97 意味着二者携带本质相同的信号。§4.2 L79 承认 "reducing effective dimensionality to ≈5"，但仍在 DDR partition 中将二者计为两个独立 drifting features，使 drifting 组从 2 个膨胀到 3 个（entropy_mean + TTR/hapax 实质上只有 2 个独立信号）。如果 drifting 组实际只有 2 个独立特征，partition 变成 2/1/3，"三分" 的结构对称性就不那么compelling了。

论文的辩护（"both are retained for marginal LOFO gains", §4.2 L79）是分类器性能的理由，不是 DDR 结构的理由。分类器中保留冗余特征是合理的，但在 DDR 叙事中将冗余特征计为独立成员是 misleading。

**[AGREE] R1-W3: Temperature sensitivity 限制普适性声明**

完全同意，我也独立提出（我的 W3）。补充：不仅 t=0.9 时信号衰减，温度敏感性还是 model-dependent 的（Pythia/OLMo 在 t=0.5 获益 +7-9pp，Qwen 几乎不变），这进一步说明 DDR 不是 universal property of recursive generation，而是 parameter × model family 的交互效应。

**[AGREE] R1-W4: Cross-domain 实验使用不同解码参数**

同意。Appendix J 明确说明 cross-domain 使用 "t=1.0, top-p=1.0"（第24行），与主实验的 t=0.7, top-p=0.9 不同。论文将此解释为 "domain × temperature interaction"（第25-27行），但更准确的说法是：cross-domain 结果和 main 结果在不同解码设置下获得，因此不能直接比较。特别是 cross-domain binary F1 > 0.73 的结论是在 t=1.0 下获得的，而 W3 已经指出主实验在 t=0.9 时大幅衰减。这两个结果放在一起是矛盾的：为什么 main experiment 在 t=0.9 崩溃，但 cross-domain 在 t=1.0 却表现良好？论文给出的解释（reference model calibration）合理但未经验证。

**[REBUT] R1-W5: TOST 等价性阈值选择缺乏 application-specific 论证**

部分反驳。ε=|d|<0.20 并非任意选择，而是 Cohen (1988) 定义的 "small effect" 标准阈值，Lakens (2017) 推荐用于等价性检验。在没有 domain-specific 先验时使用该惯例值是方法论上可接受的。论文也在 Appendix L (downstream) 中展示了 margin sensitivity analysis（Table, testing ±1%/2%/3%/5%），证明结论对阈值选择不敏感。

但 R1 指出的 tail_decay 仅 4/8 generator 通过这一点是有效的。Appendix T Table 显示 tail_decay 的 |d| 范围为 0.07-0.22，其中 4 个 generator 超过 0.15，说明 tail_decay 的 near-stationary 分类并不稳健。这削弱了 DDR partition 的一致性，与 R1-N1 的 post-hoc 风险呼应。

综合判断：阈值选择本身可辩护，但 tail_decay 的不一致性是实质问题。

**[AGREE] R1-W6: "entropy" 术语混用**

完全同意，我也独立提出（我的 W5）。特别在讨论 "distributional shape" 时，entropy_std 容易被误解为 distribution entropy 的标准差（衡量 output distribution 的离散程度如何波动），而实际是 per-token NLL sequence 的标准差（衡量 token-level surprise 的变异性）。这两者含义差异大。

---

### 对 R1 小问题的简要回应

- **M1 (Abstract 无 CI)**：同意，Abstract 空间有限但可加 "±0.006" 或在 Introduction 首次引用时附 CI。
- **M2 (Appendix generator subset 不一致)**：同意，我也独立提出。
- **M3 (Qualitative examples 过于极端)**：合理建议，但优先级低。
- **M4 (OLMo temperature 版本差异)**：注意到 Appendix H footnote 已标注 "OLMo-2-0425-1B (April 2025 release)"，但确实引入了不可控变量。
- **M5 (关键分析放 appendix)**：强烈同意。QLoRA 结果（3-class F1: 0.789→0.905）和 negative downstream result 都应在正文 Discussion 中更显著地讨论。这与我的 N3（贡献列表过薄）和 W1（negative downstream 被埋）一致。

---

### 综合评估

R1 和我（R2）的审稿意见高度一致：

| 议题 | R1 | R2 | 判断 |
|------|----|----|------|
| DDR 新颖性/理论深度 | N1 (post-hoc 风险) | N1 (描述性非解释性) | 同一问题不同角度 |
| 实际应用限制 | N3 (base + downstream) | N2 + W1 | 完全一致 |
| 贡献厚度 | 隐含在 N1-N3 | N3 (explicit) | 一致 |
| Table 1/2 不一致 | W1 | W2 | 完全一致 |
| Temperature sensitivity | W3 | W3 | 完全一致 |
| Entropy 术语 | W6 | W5 | 完全一致 |
| 特征选择透明度 | N2 | 未充分展开 | 补充同意 |
| TTR/hapax 冗余 | W2 | 未明确提出 | 补充同意 |
| Cross-domain 参数差异 | W4 | 未明确提出 | 补充同意 |

两位 reviewer 独立给出 Overall 3.0 (Findings)、Confidence 4/5，且核心问题几乎完全重叠，这增强了评估的可靠性。主要分歧仅在 TOST 阈值问题上（我认为阈值本身可辩护，但 tail_decay 的不一致性是实质问题）。

**修改优先级建议（若作者 revise）**：
1. 最高优先：解决 base-model scope（至少 2-3 个 instruct model 的系统实验）
2. 高优先：明确特征选择时间线，报告是否有被排除的候选特征
3. 高优先：为 DDR 提供理论解释或重定位为 descriptive framework
4. 中优先：统一评估协议（消除 Table 1/2 差异，统一 generator subset）
5. 中优先：将 QLoRA 和 negative downstream 结果提升到正文

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1286 · 2026-05-18T23:37:46.212697+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1287 · 2026-05-18T23:37:48.831686+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和 R2 的审稿意见高度一致（Overall 均为 3.0/Findings，6 个主要问题完全重叠），仅在 TOST 阈值问题上有轻微分歧（我认为阈值可辩护但 tail_decay 不一致性是实质问题）。R1 提出的特征选择透明度（N2）和 TTR/hapax 冗余（W2）是我未充分展开的有效补充，我对这两点均表示同意并补充了证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1288 · 2026-05-18T23:37:55.276699+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 119

## Round 119

12 recorded events


### User

_source line 1289 · 2026-05-18T23:38:50.214359+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE with qualification] R2-N1: DDR tri-partition 新颖性不足**

同意 R2 关于 DDR 阈值缺乏理论支撑的判断，这与我的 R1-N1（post-hoc 阈值风险）和 R1-N2（特征选择透明度）一致。但 R2 的论证中有一处需要纠正：

R2 说 "NLL mean 下降和 TTR/hapax 下降在 model collapse 文献中已有充分文档"，但这混淆了两个不同的现象。Model collapse 文献研究的是**训练时**在合成数据上迭代训练导致的退化，而 DDR 描述的是**推理时**递归生成的分布漂移。论文在 §5 L15 明确区分了二者："DDR is distinct from model collapse: inference-chain drift is fully reversible under fixed parameters and leaves distributional shape near-stationary (d < 0.10; variance ratios 0.98--1.12)"。Model collapse 会永久改变模型权重和输出分布的 shape，而 DDR 仅影响 location 且可逆——这是一个有意义的实证区分。

即便如此，我同意 R2 的核心关切：tri-partition 更像是对观测数据的 **descriptive taxonomy**，而非有理论预测力的发现。intermediate 组仅一个成员（entropy_std）确实削弱了结构性。论文需要以下之一：(a) 提供为什么 location drift 而 shape stable 的理论机制，(b) 通过 clustering/gap statistics 证明三分是数据中的自然结构，(c) 或降低 novelty claim 的强度。

**[AGREE] R2-N2: Base-model-only scope 限制影响力**

完全同意，与我的 R1-N3 一致。补充一个 R2 未展开的细节：instruction tuning 不仅削弱信号（OLMo-Instruct LOGO F1 从 0.763→0.338），而且使 6/7 特征方向反转（§5 L10），entropy_mean ρ 从 -0.6 变为 +0.48。这意味着 instruct model 下的 DDR 不是"变弱的版本"，而是**质性不同的现象**——R2 正确识别了这一点。这进一步说明 base model DDR 发现不能外推到实际部署场景。

**[REBUT] R2-N3: 贡献列表对长论文过于单薄**

不同意这是 Must-Fix 级别的问题，理由如下：

1. **论文正文仅 6 页**（PDF 视觉确认），而非 R2 暗示的充分使用 8 页限制。2 条聚焦贡献对 6 页正文是合理的。

2. **QLoRA 实验存在方法论限制，不宜提升为核心贡献。** 我阅读了 appendix_qlora.tex（R2 引用为 Appendix E）：QLoRA fine-tunes Qwen3-0.6B-Base，在 6-generator LOGO 上 3-class F1=0.905。但 (a) 它使用 Qwen3-0.6B-Base 作为 backbone，而 Qwen3-0.6B 本身就是 8 个 generator 之一——存在 within-model affinity 的风险，尽管在 LOGO 协议下 Qwen3-0.6B 被 held out；(b) 它仅在 6-generator 子集上评估（脚注明确说"Evaluated on the original 6-generator subset"），尚未在 full 8-gen 设置下验证；(c) 如果提升为核心贡献，论文的定位会从"empirical characterization of DDR"转向"method paper"，这与论文自身定位（"our contributions are empirical"）矛盾，且方法性能（binary F1 ≈ 0.7）不够支撑 method paper 的标准。

3. **贡献数量不应是评判标准；贡献的深度和可靠性才是。** 2 条贡献如果有充分支撑，强于 4 条注水贡献。真正的问题不是贡献太少，而是 R1-N1 和 R1-N3 指出的：DDR 论证不够严谨，且应用价值有限。

建议在 Minor Revision 中考虑将 QLoRA 结果在正文中简要提及（一句话），但不必重构论文贡献列表。

---

### Should-Fix 问题

**[AGREE] R2-W1: Downstream utility 负面结果削弱 Introduction 动机**

完全同意。Appendix L 明确显示 depth-aware curation 在等量数据下与随机采样统计等价（TOST p = 1.1×10⁻⁴），且 full dataset (12,299 samples, PPL=2.335) vs depth-filtered (3,951 samples, PPL=2.387) 的 TOST 在 ±2% margin 下 rejects equivalence——数据量主导训练质量，depth 信息无附加价值。

Introduction 的 data provenance 动机需要重新校准。建议定位为 "scientific understanding of recursive generation dynamics"，弱化 "practical data governance pipeline" 的叙事。

**[AGREE] R2-W2: Generator subset 不一致**

同意，与我的 R1-M2 一致。论文使用了 5/6/8-gen 三种子集：5-gen（cross-model chains, §4.1 L13）、6-gen（QLoRA, LOFO, confusion matrix, 5-class）、8-gen（主要 LOGO）。虽然每张表都标注了子集，但缺少一个集中说明：为什么存在三种子集、每种用于哪些实验、以及结果的可比性。建议在 §3 末尾增加一个段落或脚注统一交代。

**[REBUT] R2-W3: 温度敏感性暗示 DDR 是参数依赖而非内在属性**

不同意 R2 的推论方向。论文在 §5 L4 明确将 DDR 定位为 "under fixed sampling parameters"——DDR 从未被描述为不依赖任何条件的 universal law。关键证据：

1. **§4.2 L85 的措辞是审慎的**："The method operates reliably within t ∈ [0.5, 0.7]"——论文给出了明确的有效域，没有过度泛化。

2. **温度敏感性的物理解释是合理的**：高温度注入更多随机性，flatten 了 depth-accumulated distributional drift（§5 L5 "temperature and prompt-type ablations support this as a tendency rather than a guarantee"）。这类似于说信号在高噪声下不可检测——不意味着信号不存在，而是 SNR 不足。

3. **t=0.7 是标准解码温度**：大多数 base model 默认或推荐的解码温度在 0.5-0.8 范围内。DDR 在此范围内可靠（Appendix G, Table sampling-ablation），这覆盖了主要实际场景。

R2 的合理关切是论文是否过度暗示 DDR 是 intrinsic property——但通读正文，我认为措辞已经足够谨慎。如果有具体的句子 overclaim "intrinsic"，R2 应 cite 具体位置。我建议论文在 abstract 或 introduction 中更显著地标注温度范围（与我的 R1-W3 一致），但不同意将其升级为 DDR 本身可信度的问题。

**[AGREE] R2-W4: Paraphrastic chain 结果缺乏附录支撑**

同意。§4.2 L88 报告 "Paraphrastic chains yield weaker signal (binary F1 = 0.671 vs. 0.749 for continuation)"，但 Appendix C（appendix_prompt_type.tex）仅覆盖 continuation/elaboration/rewriting 三种 prompt type，**未包含 paraphrastic chains 的方法描述和详细结果**。0.671 这个数字在正文中出现但无法从任何附录中验证。

Limitations §L15 也引用了这个数字。论文需要：(a) 在 Appendix C 中补充 paraphrastic chain 的完整实验设置和结果，或 (b) 如果 paraphrastic 实验不够完整，删除正文中的数字引用，仅在 Limitations 中定性讨论。

**[AGREE] R2-W5: "Entropy" 术语混用**

完全同意，与我的 R1-W6 一致。论文在 §3.3 L42-43 明确声明 "these are point-wise NLL values, not Shannon entropy"，但全文 feature 名（entropy_mean 等）和讨论一直使用 "entropy"。对统计分析为核心的论文，术语精确性是基本要求。建议至少在 §3.3 feature extraction 部分更突出地标注这一区分，或在 feature 命名中使用 NLL。

---

### 小问题和缺失引用

R2 的 5 个小问题（PDF 格式 bug、appendix 数量、Figure 2 字体、em-dash、reference API issues）属于 editorial 层面，不影响审稿判断，无需逐条回应。

R2 关于缺失引用的 3 条建议（synthetic data contamination detection、MTLD/HD-D in LLM detection、2025-2026 recursive generation 工作）与论文的核心叙事关联度有限。论文已引用 MTLD/HD-D 的原始文献（McCarthy 2010, Covington 2010），以及 iterative generation 领域的最新工作（broken_telephone, markovian_chains）。

---

### R2 Framing 评估的回应

R2 指出 "论文在 empirical study 和 method paper 之间摇摆，identity 模糊"。

**[AGREE]** 这是一个精准的诊断。论文的 Introduction 用 data provenance/governance 动机暗示实用方法，但 Conclusion（§6）和自我定位（"our contributions are empirical"）又退回到纯经验研究。建议作者明确选择一个身份：如果是 empirical study，弱化实用动机、强化科学发现叙事；如果是 method paper，需要更强的性能结果和 instruct model 支持。当前的模糊定位对两种读者都不够有说服力。

---

### R1 与 R2 共识总结

两位 reviewer 在以下核心问题上完全一致：
1. **Base-model-only 限制**是最严重的影响力瓶颈（R1-N3, R2-N2）
2. **DDR 三分缺乏先验理论支撑**，更像 descriptive taxonomy（R1-N1, R2-N1）
3. **Downstream utility 负面结果**与 Introduction 动机不匹配（R1-N3, R2-W1）
4. **Entropy 术语混用**需修正（R1-W6, R2-W5）
5. **Generator subset 不一致**需集中说明（R1-M2, R2-W2）

主要分歧：
- R2-N3（贡献数量）：R1 认为不应是 Must-Fix，问题不在贡献数量而在贡献深度
- R2-W3（DDR 是否 parameter-dependent）：R1 认为论文措辞已足够审慎，温度敏感性是边界条件而非否定 DDR

**两位 reviewer 均给出 Overall 3.0 (Findings)，Confidence 4/5。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-18T23:39:13.561639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-18T23:39:13.562072+00:00_

1	# Round 18 review — Review Director consolidated 2026-05-18
2	# R18 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)
3	# Both reviewers: 3.0 (Findings). Cross-responses completed.
4	
5	# === New issues raised in R18 review ===
6	
7	- id: "R18-N1"
8	  summary: "DDR 'framework' overclaim — 阈值论证不足, N=7 不足以建立 framework"
9	  category: method
10	  severity: critical
11	  status: open
12	  first_raised_round: 18
13	  last_seen_round: 18
14	  mentions:
15	    - {round: 18, reviewers: "R1,R2", note: "R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；Cohen d benchmarks 针对效应量非 Spearman ρ；N=7 特征分 3/1/3 不具统计说服力；Levene test 拒绝等方差但用 CV shift 辩护需 equivalence testing。R2 AGREE，补充 Appendix M TOST 存在但未直接用于 near-stationary 分类判定。两位共识：DDR 应定位为 empirical observation 非 general framework。"}
16	  action_items:
17	    - {round: 18, action: "对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'", assigned_to: "", status: "open"}
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R18-N2"
22	  summary: "'Fingerprinting' 标题与 3-class 实际能力不匹配 (binary F1=0.694, 5-class F1=0.50)"
23	  category: framing
24	  severity: critical
25	  status: open
26	  first_raised_round: 18
27	  last_seen_round: 18
28	  mentions:
29	    - {round: 18, reviewers: "R1,R2", note: "R1-N3：fingerprinting 在安全/取证领域意味着高可靠性，F1=0.694 约 30% 错分率不匹配。R2 AGREE，补充 per-generator F1 跨度 0.633-0.724，5-class F1=0.50 gen-2/3 仅 0.259。Conclusion 'three classes = practical ceiling' 与标题矛盾。建议改为 Depth Profiling/Classification。"}
30	  action_items:
31	    - {round: 18, action: "将标题中 'Fingerprinting' 改为更准确的措辞（Depth Classification/Profiling/Detection）；在 Abstract 明确 3-class 粒度限制", assigned_to: "", status: "open"}
32	  resolution: ""
33	  resolution_round: null
34	
35	- id: "R18-N3"
36	  summary: "方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost"
37	  category: method
38	  severity: critical
39	  status: open
40	  first_raised_round: 18
41	  last_seen_round: 18
42	  ment
…[truncated 2963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-18T23:39:16.624929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-18T23:39:16.675970+00:00_

100	  action_items:
101	    - {round: 18, action: "将 'DDR is a property of recursive generation' 改为 'feature computation is robust to reference model choice'；intrinsic property 声明需独立论证", assigned_to: "", status: "open"}
102	  resolution: ""
103	  resolution_round: null
104	
105	- id: "R18-W5"
106	  summary: "Stylometry 引用覆盖不足 + data contamination/provenance 文献线缺失"
107	  category: writing
108	  severity: warning
109	  status: open
110	  first_raised_round: 18
111	  last_seen_round: 18
112	  mentions:
113	    - {round: 18, reviewers: "R1,R2", note: "R2-W4：TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体讨论。R2-W5：以 data provenance 为动机但缺 contamination detection 文献（Oren 2024, Golchin 2024 等）。R1 均 AGREE。"}
114	  action_items:
115	    - {round: 18, action: "§2.3 增加 TTR 变体文献（McCarthy & Jarvis 2010, Covington & McFall 2010）；§2.4 增加 data provenance/contamination paragraph", assigned_to: "", status: "open"}
116	  resolution: ""
117	  resolution_round: null
118	
119	# === Existing issues updated with R18 review mentions ===
120	
121	- id: "R7-W5"
122	  summary: "Base-model-only scope vs title/abstract generality"
123	  category: framing
124	  severity: critical
125	  status: in_progress
126	  first_raised_round: 7
127	  last_seen_round: 18
128	  mentions:
129	    - {round: 16, reviewers: "R1,R2", note: "Intro still opens with instruct-model evidence."}
130	    - {round: 17, reviewers: "R1,R2", note: "Introduction 动机与方法适用范围脱节。"}
131	    - {round: 18, reviewers: "Director", note: "MF3: Intro restructured. 7-17% moved from position 2 to supporting evidence after binary detection critique. Dynamical system framing leads. Base-model restriction at L15 with explicit justification."}
132	    - {round: 18, reviewers: "R1,R2", note: "R18 review: 两位 Reviewer 均再次标记。R1-W2 + R2-N2（升为 critical）。OLMo-Instruct F1=0.338 接近 random。Intro restructure 有改善但核心 gap 仍存在：Abstract 未提及 base-model restriction，读者可能误以为方法适用于所有 LLM。需在 Abstract 和 Intro 更早声明 scope。"}
133	  action_items:
134	    - {ro
…[truncated 5186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-18T23:39:35.506180+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-18T23:39:35.556721+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-18T23:42:11.837765+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# Round 19 (fresh) review — Review Director consolidated 2026-05-18\n# R19 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)\n# Both reviewers: 3.0 (Findings). Cross-responses completed. High consensus.\n\n# === Issues active in R19 review ===\n\n- id: \"R18-N1\"\n  summary: \"DDR tri-partition 缺乏先验理论基础，存在 post-hoc 风险，更像 descriptive taxonomy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；R2 AGREE。两位共识：DDR 应定位为 empirical observation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19-R1-N1: Cohen's d>0.75/d<0.10 和 ρ 阈值无先验支撑，robustness ±0.10 仅证明稳定性非自然结构。建议 gap statistics/silhouette/clustering 验证。R19-R2-N1: DDR 本质是描述性分类非理论发现，intermediate 仅 entropy_std 一个成员削弱结构性，NLL/TTR drift 在 model collapse 文献已有记录（R1 纠正：inference-time DDR 与 training-time model collapse 机制不同，但核心判断不变）。两位共识：需理论解释或降级为 descriptive framework。\"}\n  action_items:\n    - {round: 18, action: \"对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'\", assigned_to: \"\", status: \"open\"}\n    - {round: 19, action: \"提供 gap statistics/silhouette analysis 证明三分自然 emerge，或在 held-out 数据集预注册阈值验证 replicability，或明确降级为 descriptive framework\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-N2\"\n  summary: \"特征选择过程不透明，存在循环论证风险——特征可能为维持 DDR 3/1/3 叙事而选择\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-N2 提出：(a) 是否存在更大初始特征集？(b) 特征选择在 DDR 分析前还是后？(c) 是否有被排除特征因不符合三分结构而丢弃？entropy_min LOFO ΔF1=+0.01pp 但保留理由是 'completes four-number NLL summary'，像为维持 3/1/3 对称性。R2 AGREE 补充：§3.3 L32-36 承认特征选择服务于 DDR 叙事；§2.3 'suffice' 是事后判断非先验选择；未报告 MTLD/HD-D 等候选特征测试结果。\"}\n  action_items:\n    - {round: 19, action: \"明确报告特征选择时间线：初始候选集大小、淘汰标准、选择在 DDR 分析前/后确定；报告被排除特征及原因\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Intro still opens with instruct-model evidence.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Introduction 动机与方法适用范围脱节。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"Intro restructured 有改善但 Abstract 未提及 base-model restriction。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 fresh review 再次独立标记。R1-N3+R2-N2: OLMo-Instruct F1 0.763→0.338，6/7 特征方向反转，instruct 下 DDR 不是减弱版而是质性不同现象。Abstract 最后一句提及 base-model restriction（'The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models'），但两位 Reviewer 认为不够醒目。结合 downstream negative result，论文在实际场景中既不可用（instruct）也无实际用途（depth 信息不改善训练质量）。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"MF3: move 7-17% to supporting evidence position\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 18, action: \"Abstract 中明确 base-model restriction\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"提供 2-3 个 instruct model 系统性实验分析 DDR 为何失效；或将论文定位收窄为 pretraining data pipeline quality signal；或将论文重定位为 scientific contribution（弱化 data governance 动机）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' — downstream negative result 进一步弱化动机\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-W3 指出 downstream utility 实验反而弱化动机。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19-R2-W1: Appendix L 显示 depth-aware curation 不优于 random（PPL 2.387 vs 2.367, TOST 确认等价），full dataset PPL=2.335 vs depth-filtered PPL=2.387 在 ±2% margin 下 rejects equivalence——数据量主导训练质量，depth 无附加价值。R1 AGREE。Introduction 以 data provenance/training pipeline 为动机但 downstream 结果否定该承诺。\"}\n  action_items:\n    - {round: 17, action: \"Intro 补充 depth 信息价值论证\", assigned_to: \"Director\", status: \"in_progress\"}\n    - {round: 18, action: \"调整动机叙事：从 data curation/quality 转为 provenance transparency/audit\", assigned_to: \"\", status: \"open\"}\n    - {round: 19, action: \"在 Discussion 中更显著讨论 downstream negative result 及含义；调整 Introduction 弱化 data curation 暗示\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N2\"\n  summary: \"'Fingerprinting' 标题与实际能力不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"fingerprinting 意味着高可靠性，F1=0.694 约 30% 错分率不匹配。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 标题已改为 'Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains'——'Fingerprinting' 已替换为 'Depth Profiling'，'Base LLM' 明确 scope。R2 Framing 评估确认标题准确。此问题在 R18→R19 修改中已解决。\"}\n  action_items:\n    - {round: 18, action: \"标题改为 Depth Profiling\", assigned_to: \"\", status: \"done\"}\n  resolution: \"标题已改为 'Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains'，R19 R2 确认标题准确。\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"贡献定位应为 empirical discovery 非 method innovation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S1 确认 'empirical rather than methodological' 定位清晰，避免了 overclaim。但 R2-N1 指出 DDR 本质是 descriptive 非 explanatory。R1 cross-response 纠正 DDR vs model collapse 机制确有区别（inference-time reversible drift vs training-time irreversible degradation），但同意 analytical contribution 有限。两位共识：当前定位（empirical study）合理但贡献深度仍不足以支撑主会议。\"}\n  action_items:\n    - {round: 18, action: \"明确定位为 empirical study / phenomenon paper\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"为 DDR 提供理论解释（为什么 location drift 而 shape stable），或提供 clustering evidence 证明三分结构的自然性，增加贡献深度\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705），pooled vs macro-average 未在方法论中定义\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W1 提出，R2 独立提出（R2-W2）。Table 1 macro-averaged LOGO F1=0.694, Table 2 pooled LOGO F1=0.705。差异依赖 caption 注释而非方法论正式定义。同一方法两个 primary metric 不一致影响可信度。\"}\n  action_items:\n    - {round: 19, action: \"在 §3.4 metrics 段落正式定义 pooled vs macro-averaged LOGO F1，所有表格统一标注使用的聚合方式\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"TTR 和 hapax_ratio 高度冗余（r=0.97），膨胀 DDR drifting 组计数\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W2 提出，R2 AGREE。r=0.97 本质同一信号，DDR partition 实际为 2/1/3 非 3/1/3。论文承认 effective dimensionality ≈5 但仍将二者计为独立 drifting features，在分类器中保留冗余特征合理但在 DDR 叙事中将冗余特征计为独立成员是 misleading。\"}\n  action_items:\n    - {round: 19, action: \"在报告 DDR 时明确有效独立特征数，讨论 TTR/hapax 冗余对 partition 叙事的影响\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Temperature sensitivity 未充分限定 DDR 普遍性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"t=0.9 时大幅衰减，DDR 声明需限定 temperature 条件。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-W3 + R2-W3 再次独立标记。t=0.9 导致 9.3-26.0pp 损失，OLMo 降至 0.453 接近随机。R2 认为暗示 DDR 是 parameter-dependent 非 intrinsic。R1 REBUT：论文措辞已审慎（'under fixed sampling parameters'），t=0.7 是标准解码温度，温度敏感性是边界条件非否定 DDR。但 R1 同意应在 Abstract/Introduction 更显著标注温度范围。R2 补充温度敏感性还是 model-dependent（Pythia/OLMo 在 t=0.5 获益，Qwen 几乎不变），说明 DDR 是 parameter × model family 交互效应。\"}\n  action_items:\n    - {round: 18, action: \"在 Abstract 和 DDR 普遍性处加温度限定\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"在 Discussion 中明确区分 DDR 作为 phenomenon (parameter-dependent) 和 property of recursive generation (intrinsic)；Abstract 中 'under standard decoding (t≤0.7)' 需更醒目\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W3\"\n  summary: \"Cross-domain 实验使用不同解码参数（t=1.0 vs t=0.7），引入 confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W4 提出，R2 AGREE 补充矛盾：main experiment t=0.9 崩溃但 cross-domain t=1.0 表现良好（binary F1>0.73），论文解释（reference model calibration）合理但未验证。结果不能直接比较。\"}\n  action_items:\n    - {round: 19, action: \"在 t=0.7 下重复 cross-domain 实验，或明确标注结果不可与主实验直接比较，讨论 domain×temperature confound\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W4\"\n  summary: \"TOST tail_decay 仅 4/8 generator 通过等价性检验，near-stationary 标签不稳健\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W5 提出 tail_decay |d| 范围 0.07-0.22，4/8 超过 0.15。R2 REBUT ε=0.20 惯例值可辩护（Cohen 1988, Lakens 2017），但 AGREE tail_decay 不一致性是实质问题。综合：阈值选择本身可接受，但 tail_decay 的 near-stationary 分类跨 generator 不稳健，削弱 DDR partition 一致性。\"}\n  action_items:\n    - {round: 19, action: \"讨论 tail_decay 在 4/8 generator 上不满足等价性的含义，考虑重分类为 intermediate 或标注有条件的 near-stationary\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W5\"\n  summary: \"'Entropy' 术语指代 per-token NLL，与 Shannon entropy 混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W6 + R2-W5 独立提出。§3.3 L42-43 声明 'shorthand for token-level NLL' 但全文 feature 名和讨论持续使用 entropy。entropy_std 尤其易误解为 distribution entropy 的 std 而非 NLL sequence 的 std。在统计分析为核心的论文中术语精确性很重要。\"}\n  action_items:\n    - {round: 19, action: \"考虑 feature 命名改用 NLL（nll_mean 等）或在 §3.3 更突出标注区分\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W6\"\n  summary: \"Paraphrastic chain binary F1=0.671 在正文引用但附录无完整支撑\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R2-W4 提出，R1 AGREE。§4.2 L88 报告 paraphrastic F1=0.671 但 Appendix C 仅覆盖 continuation/elaboration/rewriting，不含 paraphrastic chains。正文数字无法从附录验证。\"}\n  action_items:\n    - {round: 19, action: \"在 Appendix C 补充 paraphrastic chain 完整实验设置和结果，或删除正文数字引用仅定性讨论\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W7\"\n  summary: \"Generator subset 不一致（5/6/8-gen），缺少集中说明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-M2 + R2-W2。LOGO 用 8-gen，cross-model 用 5-gen，QLoRA 用 6-gen，部分 appendix 用 6-gen。每张表有标注但缺集中说明为什么存在三种子集及结果可比性。\"}\n  action_items:\n    - {round: 19, action: \"在 §3 末尾增加段落或脚注统一交代三种 generator subset 的原因和可比性\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Baseline 4-det ensemble 在 3-class F1 上优于所提方法\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"论文应更直接承认 4-det ensemble 在准确性上更优。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 未被 Reviewer 独立标记为新问题，但 R1-S1 确认论文已用 'contextualize not claim advantage' 定位，R2 Framing 评估亦认可。此前修改有效但仍需监控。\"}\n  action_items:\n    - {round: 18, action: \"§4.3 更直接承认 4-det ensemble 优于 7-feature\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W4\"\n  summary: \"Cross-reference model 实验声明过强\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"spread ≤0.013 仅说明 features 对 reference model 选择鲁棒，不支持 DDR 是内在属性。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 Reviewer 未独立重提，但 R1 cross-response 中关于 DDR intrinsic vs parameter-dependent 的讨论与此相关。\"}\n  action_items:\n    - {round: 18, action: \"将 'DDR is a property of recursive generation' 改为 'feature computation is robust to reference model choice'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升 Must-Fix，R1 REBUT。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"部分改善，DDR 整体需降级为 empirical observation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S6 确认引用体系完整，与 concurrent work 比较公正。R2-S6 同样确认 Related Work 定位准确。此问题在 R18→R19 修改中已显著改善，§2.2 区分有效。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Strengthen §2.2 positioning\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Discussion 需扩展。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"§2.2 contrast strengthened。改善但未完全解决。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1 cross-response 明确肯定机制区别（inference-time reversible drift vs training-time irreversible degradation），§5 L15 的区分有效。R2 接受机制区别但认为 analytical contribution 有限。区分论证本身已 adequate，核心问题转为 DDR 的理论深度（R18-N1）。\"}\n  action_items:\n    - {round: 17, action: \"Discussion DDR vs model collapse 区分加强\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Various minor fixes needed.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"写作质量中等偏上，格式基本合规。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R2 确认写作质量良好，几乎无 AI 痕迹。R1 minor: Abstract NLL 未展开, Appendix 过多(20+节)建议合并到 10-12 个。R2 minor: PDF p.24 有游离 'chance' 文字, Figure 2 标签字体偏小。\"}\n  action_items:\n    - {round: 16, action: \"Various minor fixes\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 19, action: \"合并 Appendix 到 10-12 个核心节；修复 p.24 排版残留；检查 Figure 2 字体大小\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W3\"\n  summary: \"XGBoost 超参数选择未说明来源\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"est=200, depth=6, lr=0.1 来源不明。Appendix H classifier sensitivity 部分缓解。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 未被独立标记。R1 在 S4 中确认 classifier sensitivity 分析全面（3 替代分类器 + 3 ordinal 方法），部分缓解此问题。\"}\n  action_items:\n    - {round: 18, action: \"报告超参数选择来源\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W5\"\n  summary: \"Stylometry 引用覆盖 + data contamination/provenance 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"TTR 变体文献和 contamination detection 文献缺失。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S6 确认 67 篇引用覆盖全面，含 2025-2026 最新工作。R2 minor 3 建议补充引用但标注为非必须。R1 cross-response 指出论文已引用 MTLD/HD-D 原始文献（McCarthy 2010, Covington 2010）和最新 concurrent work。此问题在 R18→R19 修改中已改善。\"}\n  action_items:\n    - {round: 18, action: \"§2.3 增加 TTR 变体文献\", assigned_to: \"\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Previously resolved issues (unchanged, truncated for brevity) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R2 格式检查确认正文 ≤8 页，Limitations/Ethics 在 pages 8-9 不计入限制。\"}\n  resolution: \"正文 ≤8 页，多轮确认。\"\n  resolution_round: 18\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"§4.3 contextualization framing applied.\"\n  resolution_round: 18\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"DDR tri-partition (3/1/3) consistently applied.\"\n  resolution_round: 18\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Abstract trimmed from ~8 to 4 essential numbers.\"\n  resolution_round: 18\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Feature selection rationale added in §3.3.\"\n  resolution_round: 18\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Acknowledged in Limitations. Compute constraints.\"\n  resolution_round: 18\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Fingerprinting defined in Intro. Terminology consistent.\"\n  resolution_round: 18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# Round 19 (fresh) review — Review Director consolidated 2026-05-18\n# R19 submission reviewed by R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)\n# Both reviewers: 3.0 (Findings). Cross-responses completed. High consensus.\n\n# === Issues active in R19 review ===\n\n- id: \"R18-N1\"\n  summary: \"DDR tri-partition 缺乏先验理论基础，存在 post-hoc 风险，更像 descriptive taxonomy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"R1-N1 提出：|ρ|>0.60/|ρ|<0.10 阈值缺理论依据；R2 AGREE。两位共识：DDR 应定位为 empirical observation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19-R1-N1: Cohen's d>0.75/d<0.10 和 ρ 阈值无先验支撑，robustness ±0.10 仅证明稳定性非自然结构。建议 gap statistics/silhouette/clustering 验证。R19-R2-N1: DDR 本质是描述性分类非理论发现，intermediate 仅 entropy_std 一个成员削弱结构性，NLL/TTR drift 在 model collapse 文献已有记录（R1 纠正：inference-time DDR 与 training-time model collapse 机制不同，但核心判断不变）。两位共识：需理论解释或降级为 descriptive framework。\"}\n  action_items:\n    - {round: 18, action: \"对 ρ 阈值做 sensitivity analysis (±0.10)；对 near-stationary 特征用 TOST equivalence testing；将 DDR 从 'framework' 降级为 'empirical pattern/observation'\", assigned_to: \"\", status: \"open\"}\n    - {round: 19, action: \"提供 gap statistics/silhouette analysis 证明三分自然 emerge，或在 held-out 数据集预注册阈值验证 replicability，或明确降级为 descriptive framework\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-N2\"\n  summary: \"特征选择过程不透明，存在循环论证风险——特征可能为维持 DDR 3/1/3 叙事而选择\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-N2 提出：(a) 是否存在更大初始特征集？(b) 特征选择在 DDR 分析前还是后？(c) 是否有被排除特征因不符合三分结构而丢弃？entropy_min LOFO ΔF1=+0.01pp 但保留理由是 'completes four-number NLL summary'，像为维持 3/1/3 对称性。R2 AGREE 补充：§3.3 L32-36 承认特征选择服务于 DDR 叙事；§2.3 'suffice' 是事后判断非先验选择；未报告 MTLD/HD-D 等候选特征测试结果。\"}\n  action_items:\n    - {round: 19, action: \"明确报告特征选择时间线：初始候选集大小、淘汰标准、选择在 DDR 分析前/后确定；报告被排除特征及原因\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs title/abstract generality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Intro still opens with instruct-model evidence.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"Introduction 动机与方法适用范围脱节。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"Intro restructured 有改善但 Abstract 未提及 base-model restriction。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 fresh review 再次独立标记。R1-N3+R2-N2: OLMo-Instruct F1 0.763→0.338，6/7 特征方向反转，instruct 下 DDR 不是减弱版而是质性不同现象。Abstract 最后一句提及 base-model restriction（'The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models'），但两位 Reviewer 认为不够醒目。结合 downstream negative result，论文在实际场景中既不可用（instruct）也无实际用途（depth 信息不改善训练质量）。\"}\n  action_items:\n    - {round: 16, action: \"Intro structural rewrite: dynamical system framing.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 17, action: \"MF3: move 7-17% to supporting evidence position\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 18, action: \"Abstract 中明确 base-model restriction\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"提供 2-3 个 instruct model 系统性实验分析 DDR 为何失效；或将论文定位收窄为 pretraining data pipeline quality signal；或将论文重定位为 scientific contribution（弱化 data governance 动机）\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"Introduction 缺少 'why depth matters' — downstream negative result 进一步弱化动机\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"从 binary detection 到 depth classification 的跳跃缺少动机。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"R2-W3 指出 downstream utility 实验反而弱化动机。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19-R2-W1: Appendix L 显示 depth-aware curation 不优于 random（PPL 2.387 vs 2.367, TOST 确认等价），full dataset PPL=2.335 vs depth-filtered PPL=2.387 在 ±2% margin 下 rejects equivalence——数据量主导训练质量，depth 无附加价值。R1 AGREE。Introduction 以 data provenance/training pipeline 为动机但 downstream 结果否定该承诺。\"}\n  action_items:\n    - {round: 17, action: \"Intro 补充 depth 信息价值论证\", assigned_to: \"Director\", status: \"in_progress\"}\n    - {round: 18, action: \"调整动机叙事：从 data curation/quality 转为 provenance transparency/audit\", assigned_to: \"\", status: \"open\"}\n    - {round: 19, action: \"在 Discussion 中更显著讨论 downstream negative result 及含义；调整 Introduction 弱化 data curation 暗示\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-N2\"\n  summary: \"'Fingerprinting' 标题与实际能力不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"fingerprinting 意味着高可靠性，F1=0.694 约 30% 错分率不匹配。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 标题已改为 'Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains'——'Fingerprinting' 已替换为 'Depth Profiling'，'Base LLM' 明确 scope。R2 Framing 评估确认标题准确。此问题在 R18→R19 修改中已解决。\"}\n  action_items:\n    - {round: 18, action: \"标题改为 Depth Profiling\", assigned_to: \"\", status: \"done\"}\n  resolution: \"标题已改为 'Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains'，R19 R2 确认标题准确。\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"方法论新颖性不足 — 7 个标准特征 + off-the-shelf XGBoost\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"贡献定位应为 empirical discovery 非 method innovation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S1 确认 'empirical rather than methodological' 定位清晰，避免了 overclaim。但 R2-N1 指出 DDR 本质是 descriptive 非 explanatory。R1 cross-response 纠正 DDR vs model collapse 机制确有区别（inference-time reversible drift vs training-time irreversible degradation），但同意 analytical contribution 有限。两位共识：当前定位（empirical study）合理但贡献深度仍不足以支撑主会议。\"}\n  action_items:\n    - {round: 18, action: \"明确定位为 empirical study / phenomenon paper\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"为 DDR 提供理论解释（为什么 location drift 而 shape stable），或提供 clustering evidence 证明三分结构的自然性，增加贡献深度\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705），pooled vs macro-average 未在方法论中定义\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W1 提出，R2 独立提出（R2-W2）。Table 1 macro-averaged LOGO F1=0.694, Table 2 pooled LOGO F1=0.705。差异依赖 caption 注释而非方法论正式定义。同一方法两个 primary metric 不一致影响可信度。\"}\n  action_items:\n    - {round: 19, action: \"在 §3.4 metrics 段落正式定义 pooled vs macro-averaged LOGO F1，所有表格统一标注使用的聚合方式\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"TTR 和 hapax_ratio 高度冗余（r=0.97），膨胀 DDR drifting 组计数\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W2 提出，R2 AGREE。r=0.97 本质同一信号，DDR partition 实际为 2/1/3 非 3/1/3。论文承认 effective dimensionality ≈5 但仍将二者计为独立 drifting features，在分类器中保留冗余特征合理但在 DDR 叙事中将冗余特征计为独立成员是 misleading。\"}\n  action_items:\n    - {round: 19, action: \"在报告 DDR 时明确有效独立特征数，讨论 TTR/hapax 冗余对 partition 叙事的影响\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W2\"\n  summary: \"Temperature sensitivity 未充分限定 DDR 普遍性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"t=0.9 时大幅衰减，DDR 声明需限定 temperature 条件。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-W3 + R2-W3 再次独立标记。t=0.9 导致 9.3-26.0pp 损失，OLMo 降至 0.453 接近随机。R2 认为暗示 DDR 是 parameter-dependent 非 intrinsic。R1 REBUT：论文措辞已审慎（'under fixed sampling parameters'），t=0.7 是标准解码温度，温度敏感性是边界条件非否定 DDR。但 R1 同意应在 Abstract/Introduction 更显著标注温度范围。R2 补充温度敏感性还是 model-dependent（Pythia/OLMo 在 t=0.5 获益，Qwen 几乎不变），说明 DDR 是 parameter × model family 交互效应。\"}\n  action_items:\n    - {round: 18, action: \"在 Abstract 和 DDR 普遍性处加温度限定\", assigned_to: \"\", status: \"done\"}\n    - {round: 19, action: \"在 Discussion 中明确区分 DDR 作为 phenomenon (parameter-dependent) 和 property of recursive generation (intrinsic)；Abstract 中 'under standard decoding (t≤0.7)' 需更醒目\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W3\"\n  summary: \"Cross-domain 实验使用不同解码参数（t=1.0 vs t=0.7），引入 confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W4 提出，R2 AGREE 补充矛盾：main experiment t=0.9 崩溃但 cross-domain t=1.0 表现良好（binary F1>0.73），论文解释（reference model calibration）合理但未验证。结果不能直接比较。\"}\n  action_items:\n    - {round: 19, action: \"在 t=0.7 下重复 cross-domain 实验，或明确标注结果不可与主实验直接比较，讨论 domain×temperature confound\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W4\"\n  summary: \"TOST tail_decay 仅 4/8 generator 通过等价性检验，near-stationary 标签不稳健\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W5 提出 tail_decay |d| 范围 0.07-0.22，4/8 超过 0.15。R2 REBUT ε=0.20 惯例值可辩护（Cohen 1988, Lakens 2017），但 AGREE tail_decay 不一致性是实质问题。综合：阈值选择本身可接受，但 tail_decay 的 near-stationary 分类跨 generator 不稳健，削弱 DDR partition 一致性。\"}\n  action_items:\n    - {round: 19, action: \"讨论 tail_decay 在 4/8 generator 上不满足等价性的含义，考虑重分类为 intermediate 或标注有条件的 near-stationary\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W5\"\n  summary: \"'Entropy' 术语指代 per-token NLL，与 Shannon entropy 混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-W6 + R2-W5 独立提出。§3.3 L42-43 声明 'shorthand for token-level NLL' 但全文 feature 名和讨论持续使用 entropy。entropy_std 尤其易误解为 distribution entropy 的 std 而非 NLL sequence 的 std。在统计分析为核心的论文中术语精确性很重要。\"}\n  action_items:\n    - {round: 19, action: \"考虑 feature 命名改用 NLL（nll_mean 等）或在 §3.3 更突出标注区分\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W6\"\n  summary: \"Paraphrastic chain binary F1=0.671 在正文引用但附录无完整支撑\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R2-W4 提出，R1 AGREE。§4.2 L88 报告 paraphrastic F1=0.671 但 Appendix C 仅覆盖 continuation/elaboration/rewriting，不含 paraphrastic chains。正文数字无法从附录验证。\"}\n  action_items:\n    - {round: 19, action: \"在 Appendix C 补充 paraphrastic chain 完整实验设置和结果，或删除正文数字引用仅定性讨论\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W7\"\n  summary: \"Generator subset 不一致（5/6/8-gen），缺少集中说明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R1-M2 + R2-W2。LOGO 用 8-gen，cross-model 用 5-gen，QLoRA 用 6-gen，部分 appendix 用 6-gen。每张表有标注但缺集中说明为什么存在三种子集及结果可比性。\"}\n  action_items:\n    - {round: 19, action: \"在 §3 末尾增加段落或脚注统一交代三种 generator subset 的原因和可比性\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Baseline 4-det ensemble 在 3-class F1 上优于所提方法\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"论文应更直接承认 4-det ensemble 在准确性上更优。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 未被 Reviewer 独立标记为新问题，但 R1-S1 确认论文已用 'contextualize not claim advantage' 定位，R2 Framing 评估亦认可。此前修改有效但仍需监控。\"}\n  action_items:\n    - {round: 18, action: \"§4.3 更直接承认 4-det ensemble 优于 7-feature\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W4\"\n  summary: \"Cross-reference model 实验声明过强\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"spread ≤0.013 仅说明 features 对 reference model 选择鲁棒，不支持 DDR 是内在属性。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 Reviewer 未独立重提，但 R1 cross-response 中关于 DDR intrinsic vs parameter-dependent 的讨论与此相关。\"}\n  action_items:\n    - {round: 18, action: \"将 'DDR is a property of recursive generation' 改为 'feature computation is robust to reference model choice'\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-N2\"\n  summary: \"Concurrent work distinction — Broken Telephone + Markovian Chains\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"§2.2 needs expanded comparison.\"}\n    - {round: 17, reviewers: \"R1,R2\", note: \"R2 升 Must-Fix，R1 REBUT。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"部分改善，DDR 整体需降级为 empirical observation。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S6 确认引用体系完整，与 concurrent work 比较公正。R2-S6 同样确认 Related Work 定位准确。此问题在 R18→R19 修改中已显著改善，§2.2 区分有效。\"}\n  action_items:\n    - {round: 16, action: \"§2.2 expanded\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 17, action: \"Strengthen §2.2 positioning\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W5\"\n  summary: \"DDR vs model collapse 区分论证\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: \"R1,R2\", note: \"Discussion 需扩展。\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"§2.2 contrast strengthened。改善但未完全解决。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1 cross-response 明确肯定机制区别（inference-time reversible drift vs training-time irreversible degradation），§5 L15 的区分有效。R2 接受机制区别但认为 analytical contribution 有限。区分论证本身已 adequate，核心问题转为 DDR 的理论深度（R18-N1）。\"}\n  action_items:\n    - {round: 17, action: \"Discussion DDR vs model collapse 区分加强\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"Minor writing and figure issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 16, reviewers: \"R1,R2\", note: \"Various minor fixes needed.\"}\n    - {round: 18, reviewers: \"R1,R2\", note: \"写作质量中等偏上，格式基本合规。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R2 确认写作质量良好，几乎无 AI 痕迹。R1 minor: Abstract NLL 未展开, Appendix 过多(20+节)建议合并到 10-12 个。R2 minor: PDF p.24 有游离 'chance' 文字, Figure 2 标签字体偏小。\"}\n  action_items:\n    - {round: 16, action: \"Various minor fixes\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 19, action: \"合并 Appendix 到 10-12 个核心节；修复 p.24 排版残留；检查 Figure 2 字体大小\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W3\"\n  summary: \"XGBoost 超参数选择未说明来源\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"est=200, depth=6, lr=0.1 来源不明。Appendix H classifier sensitivity 部分缓解。\"}\n    - {round: 19, reviewers: \"Director\", note: \"R19 未被独立标记。R1 在 S4 中确认 classifier sensitivity 分析全面（3 替代分类器 + 3 ordinal 方法），部分缓解此问题。\"}\n  action_items:\n    - {round: 18, action: \"报告超参数选择来源\", assigned_to: \"\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W5\"\n  summary: \"Stylometry 引用覆盖 + data contamination/provenance 文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: \"R1,R2\", note: \"TTR 变体文献和 contamination detection 文献缺失。\"}\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R1-S6 确认 67 篇引用覆盖全面，含 2025-2026 最新工作。R2 minor 3 建议补充引用但标注为非必须。R1 cross-response 指出论文已引用 MTLD/HD-D 原始文献（McCarthy 2010, Covington 2010）和最新 concurrent work。此问题在 R18→R19 修改中已改善。\"}\n  action_items:\n    - {round: 18, action: \"§2.3 增加 TTR 变体文献\", assigned_to: \"\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === Previously resolved issues (unchanged, truncated for brevity) ===\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: \"R1,R2\", note: \"R19 R2 格式检查确认正文 ≤8 页，Limitations/Ethics 在 pages 8-9 不计入限制。\"}\n  resolution: \"正文 ≤8 页，多轮确认。\"\n  resolution_round: 18\n\n- id: \"R14-W4\"\n  summary: \"Baseline comparison fairness\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"§4.3 contextualization framing applied.\"\n  resolution_round: 18\n\n- id: \"R17-N1\"\n  summary: \"DDR 二分框架内部不一致\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"DDR tri-partition (3/1/3) consistently applied.\"\n  resolution_round: 18\n\n- id: \"R17-W1\"\n  summary: \"Abstract 数据密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Abstract trimmed from ~8 to 4 essential numbers.\"\n  resolution_round: 18\n\n- id: \"R17-W2\"\n  summary: \"Feature selection 缺少系统化方法论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Feature selection rationale added in §3.3.\"\n  resolution_round: 18\n\n- id: \"R17-W3\"\n  summary: \"模型规模覆盖不足 — 无 >8B\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Acknowledged in Limitations. Compute constraints.\"\n  resolution_round: 18\n\n- id: \"R17-M1\"\n  summary: \"术语不一致 + fingerprinting 可能误导\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Fingerprinting defined in Intro. Terminology consistent.\"\n  resolution_round: 18"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-18T23:42:11.938866+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 18178}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---
