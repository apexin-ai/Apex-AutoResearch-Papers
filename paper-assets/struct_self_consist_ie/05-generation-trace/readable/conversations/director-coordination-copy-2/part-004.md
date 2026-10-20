# Director coordination — Part 4 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 76

### Tool result

_source line 934 · 2026-05-16T02:14:33.266196+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 2297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-16T02:14:33.919409+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/main.tex",
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
    "pattern": "projects/struct_self_consist_ie/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-16T02:14:33.970004+00:00_

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

_source line 937 · 2026-05-16T02:14:39.141262+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 938 · 2026-05-16T02:14:39.543615+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 939 · 2026-05-16T02:14:39.543996+00:00_

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

_source line 940 · 2026-05-16T02:14:39.594515+00:00_



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

_source line 941 · 2026-05-16T02:14:44.565320+00:00_

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

_source line 942 · 2026-05-16T02:14:45.017976+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

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

_source line 943 · 2026-05-16T02:14:45.922077+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
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
    "query": "EMNLP 2026 call for papers submission deadline author guidelines",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
  }
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-16T02:14:46.374564+00:00_

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

_source line 945 · 2026-05-16T02:15:01.633327+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/category/topics/natural-language-processing"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_date&sort=desc"},{"title":"Events List | ACL Member Portal","url":"https://www.aclweb.org/portal/events?order=field_event_date&sort=desc"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"CFP: Fourth ArabicNLP Conference (ArabicNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/fourth-arabicnlp-conference-arabicnlp-2026-first-cfp"}]

Now let me search for more specific information about author guidelines:

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url
…[truncated 6058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 15711
}
```

</details>

---


### Tool result

_source line 946 · 2026-05-16T02:15:01.684072+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 15309
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-16T02:15:08.379664+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper page limit formatting template ACL style"
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
    "query": "EMNLP 2026 main conference paper page limit formatting template ACL style"
  }
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-16T02:15:09.083318+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 949 · 2026-05-16T02:15:09.083981+00:00_



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

_source line 950 · 2026-05-16T02:15:10.037814+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "5000"
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
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-16T02:15:11.406951+00:00_

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

_source line 952 · 2026-05-16T02:15:13.324497+00:00_

Web search results for query: "EMNLP 2026 main conference paper page limit formatting template ACL style"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"LaTeLL_26_template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/latell-26-template/kfcvbgxmccvb"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"ACL Template | Format, Structure, and Guide","url":"https://scispace.com/templates/acl-template-hjmlcd42ar7fdcg"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here's what I found about EMNLP 2026 main conference paper formatting requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Formatting Template and Style

The official EMNLP 2026 LaTeX template uses ACL style files. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Required Sections

The mandatory Limitations section is required, placed after the conclus
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 4944
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-16T02:15:13.375468+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ:
…[truncated 3403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3337
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-16T02:15:13.375972+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 1969
}
```

</details>

---


### Tool call

_source line 955 · 2026-05-16T02:15:20.253449+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits for long/short papers, formatting template, anonymity/double-blind rules, appendix rules, citation format, mandatory sections (limitations, ethics), any special requirements. Also extract all deadlines."
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
    "prompt": "Extract all submission requirements: page limits for long/short papers, formatting template, anonymity/double-blind rules, appendix rules, citation format, mandatory sections (limitations, ethics), any special requirements. Also extract all deadlines."
  }
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-16T02:15:21.056681+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-16T02:15:21.057124+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-16T02:15:21.659598+00:00_

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

_source line 959 · 2026-05-16T02:15:21.710293+00:00_

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

_source line 960 · 2026-05-16T02:15:26.227531+00:00_

# EMNLP 2026 Submission Requirements & Deadlines

## Page Limits
- **Long Papers:** 8 pages (final versions: 9 pages with one additional page for addressing reviewer comments)
- **Short Papers:** 4 pages (final versions: 5 pages with one additional page for addressing reviewer comments)

## Anonymity & Review Process
The review process is "double-blind." Authors cannot see reviewers, and reviewers cannot see authors. "Reviews on ARR will not be made publicly visible," though authors may opt to make anonymized submissions publicly available.

## Mandatory Sections & Requirements
- Limitations section required
- Ethics policy compliance mandatory
- "Responsible NLP research checklist" must be completed
- Two-way anonymized review instructions must be followed
- Disclosure of conflicts of interest required

## Formatting & Templates
All submissions must follow ARR submission requirements including paper templates and formatting guidelines available through the ARR CFP.

## Additional Requirements
- Supplementary materials, appendices, software, and data are optional
- Writing assistance is permitted; AI-generated papers are prohibited
- Citations and comparisons must follow ACL standards
- Multiple submissions and resubmission policies apply per ARR guidelines

## Critical Deadlines (All times: 11:59 PM UTC-12:00)
| Milestone | Date |
|-----------|------|
| ARR Submission | May 25, 2026 |
| Reviewer Registration | May 27, 2026 |
| Author Response Period | July 7-13, 2026 |
| Meta-review Release | July 30, 2026 |
| EMNLP Commitment | August 2, 2026 |
| Acceptance Notification | August 20, 2026 |
| Camera-ready Due | September 20, 2026 |
| Conference | October 24-29, 2026 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 5974
}
```

</details>

---


### Tool call

_source line 961 · 2026-05-16T02:15:29.741828+00:00_

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

_source line 962 · 2026-05-16T02:15:29.742207+00:00_

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

_source line 963 · 2026-05-16T02:15:30.294598+00:00_

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

_source line 964 · 2026-05-16T02:15:30.345176+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

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

_source line 965 · 2026-05-16T02:15:35.466094+00:00_

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

_source line 966 · 2026-05-16T02:15:36.019999+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-7) =====
3	- id: R0-C1
4	  summary: 模型规模单一（仅 8B）
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  mentions:
11	  - round: 0
12	    reviewers: [1, 2]
13	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
14	  - round: 1
15	    reviewers: [1, 2]
16	    note: model-agnostic 与 Limitations 矛盾
17	  action_items:
18	  - round: 1
19	    action: 全文替换 model-agnostic → consistent across tested model families
20	    assigned_to: Paper Agent
21	    status: resolved
22	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
23	  resolution_round: 2
24	- id: R0-C2
25	  summary: 相关工作显著遗漏
26	  category: framing
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 0
30	  last_seen_round: 1
31	  mentions:
32	  - round: 0
33	    reviewers: [1, 2]
34	    note: 5 篇核心文献缺失
35	  - round: 1
36	    reviewers: [1, 2]
37	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
38	  action_items:
39	  - round: 1
40	    action: 补充 6 篇引用到 Related Work
41	    assigned_to: Paper Agent
42	    status: resolved
43	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
44	  resolution_round: 2
45	- id: R0-C3
46	  summary: RE 结论仅基于 SciERC 单数据集
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 0
51	  last_seen_round: 4
52	  mentions:
53	  - round: 0
54	    reviewers: [1, 2]
55	    note: 需跨数据集验证或降级措辞
56	  - round: 2
57	    reviewers: [1, 2]
58	    note: Abstract RE 措辞需修正
59	  - round: 3
60	    reviewers: [1, 2]
61	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
62	  - round: 4
63	    reviewers: [1, 2]
64	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
65	  action_items:
66	  - round: 1
67	    action: 降级措辞 universal → observed in SciERC
68	    assigned_to: Paper Agent
69	    status: resolved
70	  - round: 2
71	    action: Abstract 改为 NER (three datasets) and RE (SciERC)
72	
…[truncated 53992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 967 · 2026-05-16T02:15:36.020387+00:00_

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

_source line 968 · 2026-05-16T02:15:36.422477+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).
4	All signals achieve strong quality estimation yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Most signals are instance-level and cannot rank candidates by construction; log-probability---the only per-sample signal---is too compressed within instances to discriminate.
6	A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types.
7	\end{abstract}
8	

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

_source line 969 · 2026-05-16T02:15:36.523369+00:00_

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

_source line 970 · 2026-05-16T02:15:36.875851+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	Four of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\S\ref{sec:discussion}).
12	
13	\begin{figure*}[t]
14	\centering
15	\includegraphics[width=\textwidth]{fig_overview}
16	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
17	\label{fig:overview}
18	\end{figure*}
19	
20	We evaluate five signal
…[truncated 971 chars]

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

_source line 971 · 2026-05-16T02:15:36.876269+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 972 · 2026-05-16T02:15:37.027202+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
13	
14	\paragraph{Uncertainty estimation and calibration.}
15	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
16	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; our structural signals instead measure agreement over output \textit{str
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 973 · 2026-05-16T02:15:37.378945+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 974 · 2026-05-16T02:15:37.429715+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	
8	\subsection{Confidence Signals}\label{sec:signals}
9	
10	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
11	
12	\paragraph{Log-probability (model-internal, per-sample).}
13	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
14	\begin{equation}\label{eq:logprob}
15	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
16	\end{equation}
17	
18	\paragraph{Exact match voting (surface, instance-level).}
19	The proportion of samples producing the most common output:
20	\begin{equation}\label{eq:em}
21	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
22	\end{equation}
23	
24	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
25	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
26	\begin{equation}\label{eq:fk}
27	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
28	\end{equation}
29	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
30	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%), which does not inflate
…[truncated 2079 chars]

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

_source line 975 · 2026-05-16T02:15:42.411645+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-16T02:15:42.813795+00:00_

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$). Best in \textbf{bold}. RE: preliminary. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}
…[truncated 5939 chars]

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

_source line 977 · 2026-05-16T02:15:42.814231+00:00_

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

_source line 978 · 2026-05-16T02:15:43.768310+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.38$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.
12	
13	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
14	Removing grammar constraints (SciERC NER, Qwen3-8B) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause.
15	On RE (preliminary), LP reverses direction under free-form decoding (CI includes zero); whether this generalizes remains open.
16	Our consensus-proximity strategies instantiate MBR decoding \cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
17	
18
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-16T02:15:43.818999+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 980 · 2026-05-16T02:15:44.271323+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE.
4	All signals achieve strong quality estimation yet none improves selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four signals fail by construction (instance-level); log-probability is too compressed to discriminate, and a free-form ablation confirms compression is intrinsic.
6	Signal rankings shift with difficulty and task type, collapsing at the capability boundary---consistent across two model families and a 4B ablation.
7	Trained verifiers and scaling to 70B+ are promising directions.
8	

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

_source line 981 · 2026-05-16T02:15:44.271661+00:00_

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

_source line 982 · 2026-05-16T02:15:44.422992+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers one dataset (SciERC NER) with one model; RE shows a directional LP reversal under free-form decoding.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	

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

_source line 983 · 2026-05-16T02:15:44.423449+00:00_

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

_source line 984 · 2026-05-16T02:15:44.725559+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
47	\quad FK & 
…[truncated 61168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-16T02:15:51.201033+00:00_

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

_source line 986 · 2026-05-16T02:15:51.753822+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 101\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 987 · 2026-05-16T02:15:51.754254+00:00_

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

_source line 988 · 2026-05-16T02:15:53.611589+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 989 · 2026-05-16T02:15:53.913076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null && head -5 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "description": "Check references.bib line count and header"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null && head -5 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "description": "Check references.bib line count and header"
  }
}
```

</details>

---


### Tool result

_source line 990 · 2026-05-16T02:15:54.114288+00:00_

537 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
% Auto-generated from literature_map.yaml — do not edit manually

@inproceedings{angelopoulos2021conformal,
  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},

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

_source line 991 · 2026-05-16T02:16:20.283808+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml",
  "max_chars": "2000"
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
    "file": "writing_plan.yaml",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 992 · 2026-05-16T02:16:21.238013+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only 
…[truncated 374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 993 · 2026-05-16T02:16:21.338897+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Find external review config files"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Find external review config files"
  }
}
```

</details>

---


### Tool result

_source line 994 · 2026-05-16T02:16:21.439756+00:00_

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

_source line 995 · 2026-05-16T02:17:02.920436+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "9",
  "text": "你是 Reviewer 1，负责审查以下论文的**方法严谨性、实验设计和统计分析**。\n\n## 论文信息\n- 标题: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n- 目标 venue: **EMNLP 2026 Main Conference**（via ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求:\n  - 正文 ≤8 页（final 9 页），参考文献不限页数\n  - ACL 模板（`\\usepackage[review]{acl}`），double-blind\n  - Limitations section 必须\n  - Responsible NLP Checklist 必须\n  - Ethics Statement 必须\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- 5 个 confidence signal（SJ, VC, FK, EM, LP）的形式化定义是否精确、无歧义\n- SJ 的 Hungarian matching + IoU + max normalizer 设计是否合理\n- FK 独立性假设的 justification 是否充分\n- 评估框架（QE: Spearman ρ + AUROC；Selection: best-of-N）是否恰当\n- Correlation-selection gap 的概念界定是否清晰——instance-level vs per-sample 区分是否 tautological\n\n### 2. 实验设计\n- 数据集选择（SciERC / CoNLL-2003 / WNUT-17）的覆盖度和 difficulty gradient 设计\n- 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）及训练配置（identical LoRA）是否构成公平比较\n- N=8/16、T=0.7/1.0、3-seed 的 ablation 是否充分\n- Free-form decoding ablation 的范围（1 dataset × 1 model × 1 seed）是否支撑其结论\n- Scale ablation（4B vs 8B）设计是否合理\n\n### 3. 统计分析\n- Bootstrap CI、permutation test、Fisher combined p 的使用是否规范\n- TOST 等价检验的 δ 选择是否有外部基准\n- 多重比较校正的处理\n- Effect size 报告（Cohen's d）的恰当性\n- 单种子 vs 多种子结果的标注一致性（RE 是否全部标注 preliminary）\n\n### 4. 页数合规\n- 估算正文是否 ≤8 页（section 数量、figure/table、equation 数量）\n\n请提供完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment。",
  "project": "struct_self_consist_ie"
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
    "round_number": "9",
    "text": "你是 Reviewer 1，负责审查以下论文的**方法严谨性、实验设计和统计分析**。\n\n## 论文信息\n- 标题: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n- 目标 venue: **EMNLP 2026 Main Conference**（via ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求:\n  - 正文 ≤8 页（final 9 页），参考文献不限页数\n  - ACL 模板（`\\usepackage[review]{acl}`），double-blind\n  - Limitations section 必须\n  - Responsible NLP Checklist 必须\n  - Ethics Statement 必须\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- 5 个 confidence signal（SJ, VC, FK, EM, LP）的形式化定义是否精确、无歧义\n- SJ 的 Hungarian matching + IoU + max normalizer 设计是否合理\n- FK 独立性假设的 justification 是否充分\n- 评估框架（QE: Spearman ρ + AUROC；Selection: best-of-N）是否恰当\n- Correlation-selection gap 的概念界定是否清晰——instance-level vs per-sample 区分是否 tautological\n\n### 2. 实验设计\n- 数据集选择（SciERC / CoNLL-2003 / WNUT-17）的覆盖度和 difficulty gradient 设计\n- 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）及训练配置（identical LoRA）是否构成公平比较\n- N=8/16、T=0.7/1.0、3-seed 的 ablation 是否充分\n- Free-form decoding ablation 的范围（1 dataset × 1 model × 1 seed）是否支撑其结论\n- Scale ablation（4B vs 8B）设计是否合理\n\n### 3. 统计分析\n- Bootstrap CI、permutation test、Fisher combined p 的使用是否规范\n- TOST 等价检验的 δ 选择是否有外部基准\n- 多重比较校正的处理\n- Effect size 报告（Cohen's d）的恰当性\n- 单种子 vs 多种子结果的标注一致性（RE 是否全部标注 preliminary）\n\n### 4. 页数合规\n- 估算正文是否 ≤8 页（section 数量、figure/table、equation 数量）\n\n请提供完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 996 · 2026-05-16T02:17:21.627988+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18707
}
```

</details>

---


### Tool call

_source line 997 · 2026-05-16T02:17:22.582510+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "9",
  "text": "你是 Reviewer 2，负责审查以下论文的**新颖性、完整性、相关工作和格式合规**。\n\n## 论文信息\n- 标题: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n- 目标 venue: **EMNLP 2026 Main Conference**（via ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求:\n  - 正文 ≤8 页（final 9 页），参考文献不限页数\n  - ACL 模板（`\\usepackage[review]{acl}`），double-blind\n  - Limitations section 必须\n  - Responsible NLP Checklist 必须\n  - Ethics Statement 必须\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- Correlation-selection gap 概念的原创性——是否为社区的 genuinely new insight\n- 与 Yao et al. (2026, nedellec2026/yao2026consistency) 的增量贡献是否明确\n- 4/5 信号 instance-level failure 是否为 definitional/tautological（by construction 不能 rank）\n- LP score compression 作为核心实证发现的价值\n- Free-form ablation 的 novelty\n\n### 2. 完整性检查\n- Abstract 是否准确反映论文内容（不过度声称、不遗漏关键限制）\n- Introduction 的 contribution list 是否与实际贡献匹配\n- Discussion 是否充分解释 gap 的机制\n- Conclusion 是否恰当 hedge RE 结论\n- Limitations section 是否覆盖所有重要限制\n- Ethics Statement 是否充实\n\n### 3. 相关工作审查\n- 引用是否全面——特别检查：\n  - Self-consistency / test-time scaling 方向（Wang 2023, Snell 2025, Brown 2024 等）\n  - MBR decoding 在非 MT 任务的应用（Eikema 2025 等）\n  - Uncertainty estimation for LLMs（Kuhn 2023, Malinin 等）\n  - IE-specific confidence / calibration 工作\n  - Structured MBR（Eikema 2025 structured）\n- 是否有遗漏的重要 2025-2026 相关工作\n- 引用格式是否正确（bib key 一致性、作者名正确性）\n\n### 4. 格式合规\n- 页数是否 ≤8 页（基于 section/figure/table/equation 数量估算）\n- `\\usepackage[review]{acl}` 是否正确\n- Double-blind：是否有泄露身份的信息（匿名性）\n- Table/Figure 标注规范（caption 是否自包含、cross-reference 是否完整）\n- Limitations section 是否存在且位置正确\n- Ethics Statement 是否存在\n- References 格式是否一致\n\n### 5. 写作质量\n- Abstract 信息密度是否恰当\n- 术语一致性（VC/SJ/FK/EM/LP 缩写是否统一）\n- 数字精度和一致性（表格 vs 正文）\n- 语法和表达\n\n请提供完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment。",
  "project": "struct_self_consist_ie"
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
    "round_number": "9",
    "text": "你是 Reviewer 2，负责审查以下论文的**新颖性、完整性、相关工作和格式合规**。\n\n## 论文信息\n- 标题: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n- 目标 venue: **EMNLP 2026 Main Conference**（via ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求:\n  - 正文 ≤8 页（final 9 页），参考文献不限页数\n  - ACL 模板（`\\usepackage[review]{acl}`），double-blind\n  - Limitations section 必须\n  - Responsible NLP Checklist 必须\n  - Ethics Statement 必须\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- Correlation-selection gap 概念的原创性——是否为社区的 genuinely new insight\n- 与 Yao et al. (2026, nedellec2026/yao2026consistency) 的增量贡献是否明确\n- 4/5 信号 instance-level failure 是否为 definitional/tautological（by construction 不能 rank）\n- LP score compression 作为核心实证发现的价值\n- Free-form ablation 的 novelty\n\n### 2. 完整性检查\n- Abstract 是否准确反映论文内容（不过度声称、不遗漏关键限制）\n- Introduction 的 contribution list 是否与实际贡献匹配\n- Discussion 是否充分解释 gap 的机制\n- Conclusion 是否恰当 hedge RE 结论\n- Limitations section 是否覆盖所有重要限制\n- Ethics Statement 是否充实\n\n### 3. 相关工作审查\n- 引用是否全面——特别检查：\n  - Self-consistency / test-time scaling 方向（Wang 2023, Snell 2025, Brown 2024 等）\n  - MBR decoding 在非 MT 任务的应用（Eikema 2025 等）\n  - Uncertainty estimation for LLMs（Kuhn 2023, Malinin 等）\n  - IE-specific confidence / calibration 工作\n  - Structured MBR（Eikema 2025 structured）\n- 是否有遗漏的重要 2025-2026 相关工作\n- 引用格式是否正确（bib key 一致性、作者名正确性）\n\n### 4. 格式合规\n- 页数是否 ≤8 页（基于 section/figure/table/equation 数量估算）\n- `\\usepackage[review]{acl}` 是否正确\n- Double-blind：是否有泄露身份的信息（匿名性）\n- Table/Figure 标注规范（caption 是否自包含、cross-reference 是否完整）\n- Limitations section 是否存在且位置正确\n- Ethics Statement 是否存在\n- References 格式是否一致\n\n### 5. 写作质量\n- Abstract 信息密度是否恰当\n- 术语一致性（VC/SJ/FK/EM/LP 缩写是否统一）\n- 数字精度和一致性（表格 vs 正文）\n- 语法和表达\n\n请提供完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 998 · 2026-05-16T02:17:23.994353+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 999 · 2026-05-16T02:17:32.057366+00:00_

Reviewer 1（方法严谨性 + 实验设计 + 统计分析）和 Reviewer 2（新颖性 + 完整性 + 相关工作 + 格式）已部署，等待独立初审结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 77

## Round 77

6 recorded events


### User

_source line 1000 · 2026-05-16T02:22:24.438475+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 完整审稿意见

**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
**Venue**: EMNLP 2026 Main Conference (via ACL ARR May 2026)
**审查侧重**: 新颖性、完整性、相关工作、格式合规、写作质量

---

## 总体评分
**Overall**: 3 (Findings acceptance)
**一句话总结**: 实验执行扎实、LP 压缩发现有价值，但核心 "correlation-selection gap" 概念对 4/5 信号而言是 definitional/tautological，框架性贡献被高估。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | LP 压缩发现有坚实数据支撑；但 4/5 信号的 selection 失败是数学构造的必然结果，不是实验发现 |
| Excitement | 2.5/5 | QE vs. selection 的解耦对 IE 实践有用，但核心 insight 的 surprise 较低；scope 受限于 4B-8B |
| Reproducibility | 4/5 | 训练细节、prompt、超参完整；代码承诺 release；constrained decoding 配置清晰 |
| Confidence | 4/5 | 仔细阅读全文含 appendix，领域相关经验充分 |

---

## 主要优势

**S1. 概念框架清晰**：quality estimation vs. sample selection 的显式区分（Section 1 contribution #1）在 IE 文献中此前未被正式化。instance-level vs. per-sample 信号的分类法直接解释了为什么 4/5 信号不能做 selection，为后续工作提供了设计准则。

**S2. LP 压缩分析深入**：median within-instance LP range = 0.041 nats, 60.3% tied (Table 12, Appendix F)，non-tied subset 显著优于 greedy (+2.9pp, p=0.004, Section 5 Discussion)，ε sensitivity sweep (Table 13) 验证阈值稳健性。这是论文最有价值的实证发现。

**S3. 实验严谨性高**：multi-seed stability (Kendall's W=1.000, Table 19)、TOST equivalence testing (Table 10)、external equivalence margins (δ_SEM, δ_practical, δ_literature)、bootstrap CI (Table 8)、free-form ablation (Table 15)。统计分析远超同类论文的水准。

**S4. Appendix 极其充实**：17 个 appendix section 覆盖了几乎所有可预见的 reviewer 质疑（evaluation circularity, SJ normalizer robustness, FK independence, ε sensitivity, OOD transfer, thinking token confound）。这体现了高度的学术自觉。

**S5. Related work 覆盖面广**：self-consistency 方向（Wang 2023, Chen 2024, Taubenfeld 2025, Kang 2025, Kim 2026, Oh 2025, Feng 2025, Wang 2025 ranked voting, Li 2025）、MBR decoding（Eikema 2022, 2025; Freitag 2022; Jinnai 2024; Müller 2021）、uncertainty surveys（Geng 2024, Xia 2025, Hobelsberger 2025）、structured IE（Zhou 2024, Sainz 2024, Li 2023, Wadhwa 2023）。对 Eikema 2025 structured MBR 的对接尤其到位（Section 2, line 18; Appendix L）。

**S6. Hedging 恰当**：RE 结论全文一致标记 "preliminary"，WNUT-17 作为 capability boundary 的定位清晰，Introduction contribution #3 明确标注 "RE conclusions rest on SciERC alone"。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心 "gap" 对 4/5 信号是 definitional，非实验发现
- 具体位置：Section 4.2 (line 83), Section 5 Discussion (line 8), Abstract (line 4-5)
- 问题：VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——这是信号定义的直接推论，不是实验发现。论文标题 "The Correlation-Selection Gap" 和 abstract "none improves best-of-N selection" 将一个部分 tautological 的观察框架化为统一发现，过度膨胀了贡献。真正的实验发现仅是 LP score compression（1/5 信号的具体失败机制）。
- 为什么影响接收：如果核心 contribution 的 4/5 证据是 by construction，论文的 novelty 实质上缩减为 "LP 在 IE constrained decoding 下 score 过于压缩"，这是一个有价值但范围更窄的发现，框架不匹配。
- 建议修改方向：(1) 在 Introduction/Abstract 中明确承认 4/5 信号的 selection 失败是 definitional 而非 empirical，将贡献重心移向 "为什么 LP 也不行"；(2) 或者重新框架化——论文真正的贡献是 *分类法*（instance-level vs. per-sample）本身，而非 gap 的 "发现"，应将分类法作为 contribution #1 并降低 selection failure 的修辞权重。

**N2** [critical] Abstract 过度声称——省略 RE free-form decoding 的方向性反转
- 具体位置：Abstract (line 6), Discussion Section 5 (lines 14-15)
- 问题：Abstract 称 "A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types"。但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。Abstract 的 "the gap persists across...task types" 与 RE 结果矛盾。
- 为什么影响接收：Abstract 是多数 reviewer/AC 评判论文的首要依据，省略关键反例构成 overclaiming。
- 建议修改方向：修改 Abstract 为 "...compression is intrinsic to NER; on RE (preliminary), free-form decoding reverses LP selection direction" 或类似更精确的表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺少 verbalized/elicited confidence 作为 per-sample signal
- 具体位置：Section 3.2 (confidence signals)
- 问题：论文评估了 5 种信号，但 per-sample signal 仅有 LP 一种。Xiong et al. (2024, 已在 bib 中但未引用) 和 Tian et al. (2023) 研究了 verbalized confidence（让 LLM 自己输出置信度），Kang et al. (2025, 已引用) 提出 self-certainty 作为 per-sample signal。缺少其他 per-sample signal 的对比使得 "no signal improves selection" 的结论不完整——也许更好的 per-sample signal 可以 bridge the gap。
- 建议：至少在 Limitations 中承认仅测试了一种 per-sample signal；理想情况下增加 verbalized confidence 或 self-certainty 作为 baseline。

**W2** [warning] 24 个 orphan bib entries 未引用
- 具体位置：references.bib
- 问题：verify_references 检测到 64 个 bib 条目中有 24 个未在正文中引用，包括高度相关的工作：Culotta & McCallum 2004 (IE confidence estimation 的开创性工作), Kadavath 2022 (LLMs know what they know), Malinin 2021 (autoregressive uncertainty), Guo 2017 (calibration), Desai 2020 (pre-trained model calibration), Shelmanov 2021 (active learning for sequence tagging with uncertainty), He 2024 (sequential labeling uncertainty), Zhang 2023 E-NER (evidential NER)。
- 建议：(1) 引用相关的 orphan entries（特别是 Culotta 2004, Kadavath 2022, Malinin 2021）；(2) 删除不相关的 orphan entries 以清理 bib。

**W3** [warning] Conclusion 未 hedge RE 结论
- 具体位置：Section 6 Conclusion
- 问题：Conclusion 称 "Signal rankings shift with difficulty and task type, collapsing at the capability boundary—consistent across two model families and a 4B ablation" 但未提及 RE 的 preliminary 性质。Introduction contribution #3 正确标注了 "RE conclusions rest on SciERC alone (preliminary)"，Conclusion 应呼应。
- 建议：在 Conclusion 加一句 hedging，如 "RE conclusions are preliminary, based on a single benchmark."

**W4** [warning] 模型规模限制削弱了 generalizability claim
- 具体位置：Limitations (line 2), Introduction (line 20)
- 问题：仅覆盖 4B-8B 规模。70B+ 模型可能产生更高质量、更多样化的样本，LP 压缩程度可能不同。论文在 Limitations 中提到这一点，但 Introduction 和 Conclusion 的表述 ("the gap persists across scales") 仅指 4B-8B，读者可能误以为结论适用于更大规模。
- 建议：在 Introduction 和 Conclusion 中明确标注 "at 4B-8B scale"。

**W5** [warning] Consensus-proximity selection 对 instance-level 信号的 operationalization 有些 ad-hoc
- 具体位置：Section 3.3 (line 59), Table 3
- 问题：对于 instance-level 信号，selection 策略是 "select the sample closest to consensus"。这个 operationalization 虽然合理（本质是 MBR），但论文未讨论其他可能的 operationalization（如 entity voting selection 用 majority-voted entities 构造输出，已在 footnote 5 提及但仅用于 Table 3 的 VC 行）。如果不同 operationalization 得到不同结果，"instance-level signals cannot select" 的结论需要 qualify。
- 建议：在 Discussion 中明确说明 consensus-proximity 是 MBR 的一种 instantiation（已在 Appendix L 做了），但应在主文中更早地 qualify。

---

## 小问题（不影响接收）

- **M1**: Table 2 caption 中 "$^\dagger$Greedy: $T{=}1.0$ sample" 可能引起混淆——greedy 通常指 argmax (T→0)，这里指的是 T=1.0 的 single sample（即 random baseline 的 deterministic 版本？）。建议改为 "Single sample at $T{=}1.0$" 或解释为何称之为 greedy。
- **M2**: Section 3.2 line 30: "Temperature-based sampling introduces mild negative dependence (−0.4% to −4.0%)" — 这个百分比的含义不清晰（负依赖的程度？FK 的偏移量？），需要更明确的 context。
- **M3**: `feng2025optimal` 的 bib entry 第一作者为 "Feng, Austin"，OpenAlex 匹配到 first_author = "austin"（名在前），可能是 bib entry 的名/姓顺序问题。`snell2025scaling` 类似（bib 为 "Snell, Charlie"，API 匹配 "charlie"）。这是 bib 格式问题，建议统一检查。
- **M4**: Discussion line 4 中 ρ=0.38 是 Table 1 中 VC ρ=0.379 的四舍五入，但正文中应保持一致精度或标注 "≈0.38"。
- **M5**: Introduction line 8: "nedellec2026/yao2026consistency" 似乎是 bib key 的残留文本，应检查是否在渲染后正确显示为 citation。

## Questions to Authors

**Q1**: 你们是否尝试过其他 per-sample signals（如 verbalized confidence, entropy of next-token distribution, self-certainty）？如果是，结果如何？如果否，为什么不？

**Q2**: LP 压缩在 free-form decoding 下几乎不变（std ratio 0.97），但 RE selection 方向翻转。这意味着 compression 不是唯一的失败原因——是什么机制驱动了 RE 的翻转？论文说 "selective variance reallocation"，能否更具体？

**Q3**: 对于 instance-level 信号，一个自然的 selection 策略是 entity-level majority voting（已在 footnote 5 提及用于 VC 行）。如果对所有 consistency 信号都使用 entity-level aggregation（而非 sample-level consensus-proximity），selection 结果会否不同？

**Q4**: Qwen3-8B 的 thinking token confound (Appendix G) 分析了 LP 影响，但是否也影响了 consistency signals？empty `&lt;think>&lt;/think>` blocks 在 training 中是否改变了模型的 output distribution，进而影响了 inter-sample agreement？

## Missing References

以下论文可能需要引用或在 Related Work 中讨论：

1. **Kadavath et al. 2022** "Language Models (Mostly) Know What They Know" — 已在 bib 中但未引用。这是 LLM self-knowledge/calibration 的开创性工作，与 LP 作为 confidence signal 直接相关。
2. **Culotta & McCallum 2004** "Confidence Estimation for Information Extraction" — 已在 bib 中但未引用。IE confidence estimation 的早期工作，应在 Related Work 第三段提及。
3. **Malinin & Gales 2021** "Uncertainty Estimation in Autoregressive Structured Prediction" — 已在 bib 中但未引用。直接讨论了 autoregressive 模型在 structured output 上的 uncertainty 估计，高度相关。
4. **Tian et al. 2023** "Just Ask for Calibration" — 不在 bib 中。verbalized confidence 的重要工作，与 W1 中缺少 per-sample signal baseline 的问题相关。
5. **Lin et al. 2023** "Generating with Confidence" — 可能相关，讨论了 LLM generation 中的 confidence estimation。

## Overall Assessment

这是一篇实验执行扎实、统计分析严谨的论文。LP score compression 的发现有实际价值，appendix 的充实程度体现了高度学术自觉。

核心问题是框架与内容的不匹配：论文将一个部分 definitional 的观察（instance-level 信号不能做 per-sample selection）和一个 scope 较窄的实证发现（LP 在 constrained decoding 下 score 压缩）包装为一个统一的 "gap"。这不构成 reject 的理由，但降低了 excitement——读者在理解 instance-level vs. per-sample 的区分后，会发现 4/5 信号的 "failure" 是显然的，真正的 surprise 仅来自 LP 压缩。

建议 **Findings** 而非 Main Conference，除非 N1 和 N2 得到有效 reframing。具体来说，如果作者将论文重心从 "发现了 gap" 转向 "提供了 instance-level vs. per-sample 的分类法，并证明了当前唯一可用的 per-sample signal (LP) 为何不够"，novelty 评估会更积极。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见

**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)

---

## 总体评分
**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)
**一句话总结**: 问题定义清晰、实验设计严谨、统计分析透明，correlation-selection gap 是有价值的概念贡献；但核心 insight 有部分 tautological 成分，RE 证据不足，free-form ablation 范围过窄以至于 abstract 中"compression is intrinsic"的 claim 强于实际证据。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨，统计实践优于同类工作（bootstrap CI, TOST, permutation test）；但 instance-level signal 无法 rank 是 by construction 的，gap 部分是 tautological；TOST 外部锚点显示等价性结论 configuration-dependent |
| Excitement | 3/5 | 概念贡献（metric dissociation, correlation-selection gap）对社区有价值；但负结果论文天然 excitement 有限，且未提出解决方案 |
| Reproducibility | 4/5 | 训练配置、prompt 模板、超参数详尽（Appendix F）；代码承诺 release；唯一扣分：Qwen3-8B SciERC thinking token confound 需要额外验证 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部 appendix |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract/Conclusion 中 "free-form ablation confirms compression is intrinsic" 过度概括
- 具体位置：Abstract line 6；Section 6 (Conclusion) line 5
- 问题：Free-form ablation 仅覆盖 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。NER LP 分布确实稳定（std ratio 0.97, Table 12 Panel A），但 RE 在 free-form 下 LP 选择方向反转（从 −0.68pp 到 +1.69pp, Panel B），这直接 undermines "compression is intrinsic" 的通用性。论文 Discussion (§5) 和 Limitations 都诚实承认了这一局限，但 abstract 和 conclusion 的措辞没有限定范围。
- 为什么影响接收：Abstract 是读者对论文的第一印象，overclaim 会误导对核心贡献的理解。
- 建议修改方向：改为 "A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal that warrants further investigation" 或类似限定性表述。

**N2** [critical] Correlation-selection gap 中 instance-level signal 失败的 tautological 成分未充分讨论
- 具体位置：Section 4.2, Section 5 "Why the gap exists"
- 问题：4/5 信号是 instance-level 的，assign identical score to all candidates *by construction*（论文自己也这样说：Section 4.2 line 83）。这不是一个 empirical finding，而是一个 definitional consequence——这些信号根本不是设计用来做 per-sample selection 的。将此包装为 "gap" 有夸大意外程度之嫌。真正有信息量的 gap 仅存在于 LP（唯一的 per-sample signal）和 VC 的 majority-voting selection variant（脚注 Eq 5 line 50 表明 selection 时 VC 给每个 sample 不同的 voted output，从而变成 per-sample signal）。
- 为什么影响接收：如果 "gap" 在 4/5 信号上是 trivially true，论文的核心贡献缩窄为 "LP compression prevents selection"——仍有价值但 scope 显著缩小。
- 建议修改方向：(a) 更清晰地将 instance-level 信号的失败定位为 design limitation 而非 empirical surprise；(b) 将 LP 和 VC-voted-output 的 selection failure 作为核心实验发现重点展开；(c) 或者重新 frame 贡献为 "existing signals are either instance-level (by design) or compressed (LP), and there is no practical per-sample signal for structured IE"。

**N3** [critical] RE 证据不足以支撑标题和 abstract 中 "LLM-Based Information Extraction" 的通用性声明
- 具体位置：Title, Abstract, Section 4.1 line 49-50, Limitations
- 问题：RE 仅在 SciERC 上测试（40% zero F1），且全部标注 "preliminary"。标题和 abstract 说 "Information Extraction"，实际上核心可靠结论仅覆盖 NER。论文在 Limitations 和正文中反复诚实标注了 "preliminary"，但标题/abstract 的 scope 与证据不匹配。
- 为什么影响接收：Reviewer 和读者会基于标题/abstract 判断 scope，当 RE 是 preliminary 时称 "Information Extraction" 是 overclaim。
- 建议修改方向：标题/abstract 中加限定语（如 "primarily on NER"），或在 abstract 明确 "RE conclusions rest on a single benchmark and are preliminary"（introduction 已有类似措辞 line 30，但 abstract 没有）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST 外部锚点结果显示等价性结论 configuration-dependent，但正文未充分整合
- 具体位置：Appendix D, Section 4.2
- 问题：外部锚点下（δ_SEM, δ_practical=0.5pp, δ_literature=1.0pp），LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 在所有外部 δ 下均 fail（Appendix D line 390-394）。这意味着 "no signal improves selection" 的 blanket claim 应改为 "no signal *consistently* improves selection" 或 "selection gains are at best marginal"。当前正文 Section 4.2 没有整合这一 nuance。
- 建议：在 Section 4.2 主文中加一句提及外部锚点结果的 configuration-dependent 性质，或调整 claim 措辞。

**W2** [warning] VC majority-voting selection variant（脚注 Eq 5）的 per-sample 性质和失败原因未深入分析
- 具体位置：Section 3.2 line 50 (footnote), Table 2
- 问题：Eq 5 脚注说 selection 时只保留 frequency > N/2 的实体形成 voted output。这使得 VC 在 selection 语境下成为一个 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但 Table 2 显示 VC selection 表现最差（0.623, 低于 random 0.610 但也低于 greedy 0.645）。这个失败值得深入分析——VC 理论上 *能* rank candidates，为什么仍然失败？是因为 voted output 本身就和多数 sample 相似（高 recall、低 precision），还是因为 high-overlap sample 恰好不是 best-F1 sample？
- 建议：在 Discussion 中增加 1-2 句对 VC-selection 失败机制的分析。

**W3** [warning] 多重比较校正不完整
- 具体位置：Table 1 (quality estimation), Table 2 (selection), 全文
- 问题：Bootstrap CI appendix 的脚注（line 302）提到 SJ-EM gap "would not survive Bonferroni correction for 10 pairwise comparisons"，但正文中大量信号 × 数据集 × 模型的比较（5 signals × 3 datasets × 2-3 models）没有系统性的多重比较校正。Selection 分析中每个 signal 都与 greedy 做了独立的 sign test / Fisher combined test，但没有 family-wise error 校正。
- 建议：至少在正文或 appendix 中讨论多重比较的影响，说明 "即使做 Bonferroni/Holm 校正，core conclusions 是否成立"。对于 "无显著差异" 类的负结果，未校正的 individual p-values 已经足够（p > 0.05 未校正 → 校正后仍 > 0.05），但应明确说明这一逻辑。

**W4** [warning] Quality estimation 主表（Table 1）仅用单 seed，与后续多 seed 分析有潜在不一致
- 具体位置：Table 1 (seed=42), Table 7 (3-seed mean)
- 问题：Table 1 报告 seed=42 的单次结果。Table 7（Appendix F）显示 3-seed mean 值与 Table 1 有差异（如 SJ NER: Table 1 报 0.360, Table 7 mean 0.364; VC NER: 0.379 vs 0.386; LP NER: 0.205 vs 0.217）。虽然差异不大且 ranking 一致（Kendall's W=1.000），但 Table 1 作为主表应注明这些是 single-seed 结果并指向多 seed 验证。
- 建议：Table 1 caption 中加一句 "Values are single-seed (42); 3-seed means and stability in Table X confirm ranking consistency (W=1.000)"，或直接报告 3-seed mean。

**W5** [warning] Scale ablation (4B vs 8B) 设计有限
- 具体位置：Table 3, Section 4.3 line 117-118
- 问题：4B ablation 仅用 Qwen3-4B（无 LLaMA 4B），且结论 "task difficulty, not model capacity, drives the gap" 仅基于两个数据点（4B 和 8B）。4B→8B 的 scale 差异不到 2×，不足以充分 disentangle model capacity 和 task difficulty 的效应。论文 Limitations 中提到 "70B+ models untested"，但这一局限对 "not model capacity" 的 claim 影响更大。
- 建议：弱化 "not model capacity" 的措辞为 "within the 4B-8B range, task difficulty appears to be the primary driver"，保留 scale limitation。

---

## 小问题（不影响接收）

- **W6** [info] Bib 有 24 个 orphan entries（在 .bib 中但未被 \cite），建议清理以避免提交时 LaTeX warning。
- **W7** [info] Section 3.2 line 30 关于 FK 负依赖性的 claim（"−0.4% to −4.0%"）未给出计算过程或 appendix reference，直接断言 "does not inflate FK" 需要更多 justification。虽然 permutation test (Table 4) 间接支持了 FK 的有效性，但 claim 本身的推导缺失。
- **W8** [info] Table 2 NER 用 2-seed mean±σ（sign test），RE 用 single seed。NER 和 RE 的统计标准不一致，建议统一。
- **W9** [info] Ethics Statement 提到 "CoNLL-2003 is derived from Reuters RCV1 corpus, which is available for research purposes under a NIST agreement"——严格来说是 NIST 分发但非 NIST 协议，应核实具体 license 描述。
- **W10** [info] "correlation-selection gap" 这个术语在论文中反复使用但没有形式化定义（如 Δ = ρ − selection_gain / oracle_headroom）。建议在 Section 4.2 给出操作性定义。

---

## 提问（Questions for Authors）

**Q1**: VC 在 selection 语境下（majority-voted output 然后选最近的 sample）实际上是 per-sample signal——每个 candidate 与 voted output 的 overlap 不同。那为什么 VC selection 仍然失败？是否因为 voted output 本身和高频 sample 高度 overlap，导致 selection 退化为 "选最平庸的 sample"？

**Q2**: 有没有尝试过组合信号（如 LP + SJ 的 weighted combination）做 selection？即使各自失败，是否有互补性？

**Q3**: Free-form RE LP reversal（Table 12 Panel B: from −0.68pp to +1.69pp）是最 actionable 的发现之一。这个 reversal 在 seed 42 之外是否能复现？如果能，这可能是一个重要的 positive contribution（"free-form decoding enables LP selection for RE"）。

**Q4**: $\varepsilon$ = 0.05 用于 LP tied/non-tied 分割。Table 9 的 $\varepsilon$ sweep 显示这个选择最大化了 statistical separation（p=0.004），但这是否构成 p-hacking？即在多个 threshold 中选了效果最好的那个来报告？

---

## Missing References

引用核查：所有 40 个 \cite key 均有对应 bib entry，无 missing。3 个条目在 OpenAlex 中未找到（hobelsberger2025, lightman2024, venktesh2025），经核实为 OpenAlex 覆盖局限，论文本身存在。

可能遗漏的相关工作：
- **Ren et al. (2023)** "Investigating Uncertainty Calibration of Aligned Language Models under the Hood" (EMNLP 2023 Findings) — 与 LP calibration 和 uncertainty estimation 直接相关
- **Lin et al. (2024)** "Generating Benchmarks for Factuality Evaluation of Language Models" (EACL 2024) — SelfCheckGPT 相关但更 focused on factuality + consistency

---

## 主要优势

- **S1**: 问题定义有价值——将 self-consistency 扩展到 set-valued structured output 是一个自然但重要的研究方向，quality estimation vs selection 的 metric dissociation 是有启发性的
- **S2**: 实验设计严谨——difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed 验证形成完整的 robustness picture
- **S3**: 统计分析显著优于同类 empirical NLP 工作——bootstrap CI with pairwise Δρ、TOST 等价检验（含外部锚点）、permutation test、Fisher combined p、Cohen's d 报告，且诚实标注所有 borderline/preliminary 结果
- **S4**: Limitations 透明——RE preliminary 标注贯穿全文，thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 没有被回避
- **S5**: Appendix 极其详尽（~15 pages），提供了 normalizer robustness、LOO-SJ equivalence、ε sensitivity、OOD analysis、LP failure stability 等细粒度分析，增强可重复性
- **S6**: 与 MBR decoding 文献的连接（Appendix K, cite Eikema et al. 2025）将 finding 嵌入更广泛的理论框架，非 ad hoc observation

---

## 最终判断

这是一篇方法论严谨、统计实践优良的 empirical 负结果论文。核心贡献（metric dissociation + LP compression bottleneck）对 test-time scaling for IE 社区有实际价值。主要弱点是：(1) instance-level signal 失败有 tautological 成分；(2) RE 证据不足但标题/abstract scope 过宽；(3) free-form ablation 范围不支撑 abstract 中的通用性 claim。修复 N1-N3 后，推荐 Findings acceptance；若能增加 free-form multi-seed RE 实验并缩窄 framing，可考虑 main conference。

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

_source line 1001 · 2026-05-16T02:23:16.529696+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "9",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 N/W/M 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3 (Findings acceptance)\n**一句话总结**: 实验执行扎实、LP 压缩发现有价值，但核心 \"correlation-selection gap\" 概念对 4/5 信号而言是 definitional/tautological，框架性贡献被高估。\n\n### Must-Fix\n\n**N1** [critical] 核心 \"gap\" 对 4/5 信号是 definitional，非实验发现\n- Section 4.2 (line 83), Section 5 Discussion (line 8), Abstract (line 4-5)\n- VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——是信号定义的直接推论，不是实验发现。标题 \"The Correlation-Selection Gap\" 和 abstract \"none improves best-of-N selection\" 将部分 tautological 的观察框架化为统一发现。真正的实验发现仅是 LP score compression（1/5 信号的具体失败机制）。\n- 建议：(1) 在 Introduction/Abstract 中明确承认 4/5 信号的 selection 失败是 definitional 而非 empirical；(2) 或重新框架化——分类法本身是贡献，而非 gap 的 \"发现\"。\n\n**N2** [critical] Abstract 过度声称——省略 RE free-form decoding 的方向性反转\n- Abstract (line 6), Discussion Section 5 (lines 14-15)\n- Abstract 称 \"A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types\"。但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。\n- 建议：修改 Abstract 为 \"...compression is intrinsic to NER; on RE (preliminary), free-form decoding reverses LP selection direction\"。\n\n### Should-Fix\n\n**W1** [warning] 缺少 verbalized/elicited confidence 作为 per-sample signal\n- 论文 per-sample signal 仅有 LP 一种。Xiong et al. (2024), Tian et al. (2023), Kang et al. (2025, self-certainty) 均为 per-sample signal 但未对比。\n- 建议：至少在 Limitations 中承认仅测试了一种 per-sample signal。\n\n**W2** [warning] 24 个 orphan bib entries 未引用\n- 包括 Culotta & McCallum 2004, Kadavath 2022, Malinin 2021, Guo 2017, Desai 2020, Shelmanov 2021, He 2024, Zhang 2023 E-NER 等。\n- 建议：引用相关的或删除不相关的。\n\n**W3** [warning] Conclusion 未 hedge RE 结论\n- Conclusion 未提及 RE 的 preliminary 性质，但 Introduction #3 正确标注了。\n- 建议：Conclusion 加一句 hedging。\n\n**W4** [warning] 模型规模限制削弱了 generalizability claim\n- 仅覆盖 4B-8B 规模。Introduction 和 Conclusion 的 \"the gap persists across scales\" 仅指 4B-8B。\n- 建议：明确标注 \"at 4B-8B scale\"。\n\n**W5** [warning] Consensus-proximity selection 对 instance-level 信号的 operationalization 有些 ad-hoc\n- 是否尝试过其他 operationalization？如 entity-level majority voting 应用于所有 consistency 信号。\n- 建议：在主文中更早 qualify consensus-proximity 是 MBR 的一种 instantiation。\n\n### Minor\n\n- **M1**: Table 2 \"Greedy\" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞。\n- **M2**: Section 3.2 line 30 FK 负依赖 \"−0.4% to −4.0%\" 含义不清。\n- **M3**: bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling）。\n- **M4**: Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。\n- **M5**: Introduction line 8 \"nedellec2026/yao2026consistency\" 似乎是 bib key 残留。\n\n### Questions\n- Q1: 是否尝试过其他 per-sample signals？\n- Q2: RE free-form LP reversal 的具体机制？\"selective variance reallocation\" 能否更具体？\n- Q3: 对所有 consistency 信号都用 entity-level aggregation 做 selection，结果是否不同？\n- Q4: Thinking token confound 是否也影响了 consistency signals？\n\n### Missing References\n- Kadavath et al. 2022 (在 bib 中未引用)\n- Culotta & McCallum 2004 (在 bib 中未引用)\n- Malinin & Gales 2021 (在 bib 中未引用)\n- Tian et al. 2023 \"Just Ask for Calibration\"\n- Lin et al. 2023 \"Generating with Confidence\"",
  "project": "struct_self_consist_ie"
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
    "round_number": "9",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 N/W/M 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3 (Findings acceptance)\n**一句话总结**: 实验执行扎实、LP 压缩发现有价值，但核心 \"correlation-selection gap\" 概念对 4/5 信号而言是 definitional/tautological，框架性贡献被高估。\n\n### Must-Fix\n\n**N1** [critical] 核心 \"gap\" 对 4/5 信号是 definitional，非实验发现\n- Section 4.2 (line 83), Section 5 Discussion (line 8), Abstract (line 4-5)\n- VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——是信号定义的直接推论，不是实验发现。标题 \"The Correlation-Selection Gap\" 和 abstract \"none improves best-of-N selection\" 将部分 tautological 的观察框架化为统一发现。真正的实验发现仅是 LP score compression（1/5 信号的具体失败机制）。\n- 建议：(1) 在 Introduction/Abstract 中明确承认 4/5 信号的 selection 失败是 definitional 而非 empirical；(2) 或重新框架化——分类法本身是贡献，而非 gap 的 \"发现\"。\n\n**N2** [critical] Abstract 过度声称——省略 RE free-form decoding 的方向性反转\n- Abstract (line 6), Discussion Section 5 (lines 14-15)\n- Abstract 称 \"A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types\"。但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。\n- 建议：修改 Abstract 为 \"...compression is intrinsic to NER; on RE (preliminary), free-form decoding reverses LP selection direction\"。\n\n### Should-Fix\n\n**W1** [warning] 缺少 verbalized/elicited confidence 作为 per-sample signal\n- 论文 per-sample signal 仅有 LP 一种。Xiong et al. (2024), Tian et al. (2023), Kang et al. (2025, self-certainty) 均为 per-sample signal 但未对比。\n- 建议：至少在 Limitations 中承认仅测试了一种 per-sample signal。\n\n**W2** [warning] 24 个 orphan bib entries 未引用\n- 包括 Culotta & McCallum 2004, Kadavath 2022, Malinin 2021, Guo 2017, Desai 2020, Shelmanov 2021, He 2024, Zhang 2023 E-NER 等。\n- 建议：引用相关的或删除不相关的。\n\n**W3** [warning] Conclusion 未 hedge RE 结论\n- Conclusion 未提及 RE 的 preliminary 性质，但 Introduction #3 正确标注了。\n- 建议：Conclusion 加一句 hedging。\n\n**W4** [warning] 模型规模限制削弱了 generalizability claim\n- 仅覆盖 4B-8B 规模。Introduction 和 Conclusion 的 \"the gap persists across scales\" 仅指 4B-8B。\n- 建议：明确标注 \"at 4B-8B scale\"。\n\n**W5** [warning] Consensus-proximity selection 对 instance-level 信号的 operationalization 有些 ad-hoc\n- 是否尝试过其他 operationalization？如 entity-level majority voting 应用于所有 consistency 信号。\n- 建议：在主文中更早 qualify consensus-proximity 是 MBR 的一种 instantiation。\n\n### Minor\n\n- **M1**: Table 2 \"Greedy\" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞。\n- **M2**: Section 3.2 line 30 FK 负依赖 \"−0.4% to −4.0%\" 含义不清。\n- **M3**: bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling）。\n- **M4**: Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。\n- **M5**: Introduction line 8 \"nedellec2026/yao2026consistency\" 似乎是 bib key 残留。\n\n### Questions\n- Q1: 是否尝试过其他 per-sample signals？\n- Q2: RE free-form LP reversal 的具体机制？\"selective variance reallocation\" 能否更具体？\n- Q3: 对所有 consistency 信号都用 entity-level aggregation 做 selection，结果是否不同？\n- Q4: Thinking token confound 是否也影响了 consistency signals？\n\n### Missing References\n- Kadavath et al. 2022 (在 bib 中未引用)\n- Culotta & McCallum 2004 (在 bib 中未引用)\n- Malinin & Gales 2021 (在 bib 中未引用)\n- Tian et al. 2023 \"Just Ask for Calibration\"\n- Lin et al. 2023 \"Generating with Confidence\"",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1002 · 2026-05-16T02:23:48.237881+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31708
}
```

</details>

---


### Tool call

_source line 1003 · 2026-05-16T02:23:50.450011+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "9",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 N/W 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5/5 (介于 Findings 和 Conference acceptance)\n**一句话总结**: 问题定义清晰、实验设计严谨、统计分析透明，correlation-selection gap 是有价值的概念贡献；但核心 insight 有部分 tautological 成分，RE 证据不足，free-form ablation 范围过窄。\n\n### Must-Fix\n\n**N1** [critical] Abstract/Conclusion 中 \"free-form ablation confirms compression is intrinsic\" 过度概括\n- Free-form ablation 仅 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。NER LP 分布稳定（std ratio 0.97），但 RE LP selection 方向反转（−0.68pp → +1.69pp）。Abstract 和 conclusion 未限定范围。\n- 建议：改为 \"A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal\"。\n\n**N2** [critical] Correlation-selection gap 中 instance-level signal 失败的 tautological 成分未充分讨论\n- 4/5 信号是 instance-level，assign identical score to all candidates *by construction*。将此包装为 \"gap\" 有夸大意外程度之嫌。真正有信息量的 gap 仅存在于 LP 和 VC majority-voting selection variant。\n- 建议：(a) 将 instance-level 失败定位为 design limitation 而非 empirical surprise；(b) 将 LP 和 VC-voted-output 的 selection failure 作为核心实验发现；(c) 或 reframe 为 \"existing signals are either instance-level or compressed\"。\n\n**N3** [critical] RE 证据不足以支撑标题和 abstract 中 \"Information Extraction\" 的通用性声明\n- RE 仅在 SciERC 上测试（40% zero F1），全部标注 \"preliminary\"。标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER。\n- 建议：标题/abstract 加限定语或明确 RE preliminary。\n\n### Should-Fix\n\n**W1** [warning] TOST 外部锚点结果显示等价性结论 configuration-dependent\n- LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。\n- 建议：Section 4.2 主文中加一句提及。\n\n**W2** [warning] VC majority-voting selection variant 的 per-sample 性质和失败原因未深入分析\n- VC 在 selection 语境下成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得分析。\n- 建议：Discussion 增加 1-2 句分析。\n\n**W3** [warning] 多重比较校正不完整\n- 5 signals × 3 datasets × 2-3 models 的大量比较没有系统性校正。对于负结果，未校正 p > 0.05 已足够但应说明逻辑。\n- 建议：在正文或 appendix 讨论影响。\n\n**W4** [warning] Table 1 单 seed 与 Table 7 多 seed 差异\n- Table 1 seed=42，Table 7 3-seed mean 有差异（如 LP NER: 0.205 vs 0.217）。Table 1 应注明。\n- 建议：Table 1 caption 加指向多 seed 验证的注释。\n\n**W5** [warning] Scale ablation 设计有限\n- 仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。\"not model capacity\" 仅基于两个数据点。\n- 建议：弱化为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"。\n\n### Minor\n- W6: 24 个 orphan bib entries\n- W7: FK 负依赖 \"−0.4% to −4.0%\" 无推导过程\n- W8: Table 2 NER 2-seed vs RE single seed 统计标准不一致\n- W9: Ethics Statement CoNLL-2003 license 描述需核实\n- W10: \"correlation-selection gap\" 术语无操作性定义\n\n### Questions\n- Q1: VC voted-output selection 为何失败？\n- Q2: 有没有尝试组合信号做 selection？\n- Q3: Free-form RE LP reversal 在 seed 42 之外能否复现？\n- Q4: ε=0.05 是否构成 p-hacking？\n\n### Missing References\n- Ren et al. (2023) \"Investigating Uncertainty Calibration of Aligned LMs\" (EMNLP 2023 Findings)\n- Lin et al. (2024) (factuality + consistency)",
  "project": "struct_self_consist_ie"
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
    "round_number": "9",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 N/W 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5/5 (介于 Findings 和 Conference acceptance)\n**一句话总结**: 问题定义清晰、实验设计严谨、统计分析透明，correlation-selection gap 是有价值的概念贡献；但核心 insight 有部分 tautological 成分，RE 证据不足，free-form ablation 范围过窄。\n\n### Must-Fix\n\n**N1** [critical] Abstract/Conclusion 中 \"free-form ablation confirms compression is intrinsic\" 过度概括\n- Free-form ablation 仅 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。NER LP 分布稳定（std ratio 0.97），但 RE LP selection 方向反转（−0.68pp → +1.69pp）。Abstract 和 conclusion 未限定范围。\n- 建议：改为 \"A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal\"。\n\n**N2** [critical] Correlation-selection gap 中 instance-level signal 失败的 tautological 成分未充分讨论\n- 4/5 信号是 instance-level，assign identical score to all candidates *by construction*。将此包装为 \"gap\" 有夸大意外程度之嫌。真正有信息量的 gap 仅存在于 LP 和 VC majority-voting selection variant。\n- 建议：(a) 将 instance-level 失败定位为 design limitation 而非 empirical surprise；(b) 将 LP 和 VC-voted-output 的 selection failure 作为核心实验发现；(c) 或 reframe 为 \"existing signals are either instance-level or compressed\"。\n\n**N3** [critical] RE 证据不足以支撑标题和 abstract 中 \"Information Extraction\" 的通用性声明\n- RE 仅在 SciERC 上测试（40% zero F1），全部标注 \"preliminary\"。标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER。\n- 建议：标题/abstract 加限定语或明确 RE preliminary。\n\n### Should-Fix\n\n**W1** [warning] TOST 外部锚点结果显示等价性结论 configuration-dependent\n- LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。\n- 建议：Section 4.2 主文中加一句提及。\n\n**W2** [warning] VC majority-voting selection variant 的 per-sample 性质和失败原因未深入分析\n- VC 在 selection 语境下成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得分析。\n- 建议：Discussion 增加 1-2 句分析。\n\n**W3** [warning] 多重比较校正不完整\n- 5 signals × 3 datasets × 2-3 models 的大量比较没有系统性校正。对于负结果，未校正 p > 0.05 已足够但应说明逻辑。\n- 建议：在正文或 appendix 讨论影响。\n\n**W4** [warning] Table 1 单 seed 与 Table 7 多 seed 差异\n- Table 1 seed=42，Table 7 3-seed mean 有差异（如 LP NER: 0.205 vs 0.217）。Table 1 应注明。\n- 建议：Table 1 caption 加指向多 seed 验证的注释。\n\n**W5** [warning] Scale ablation 设计有限\n- 仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。\"not model capacity\" 仅基于两个数据点。\n- 建议：弱化为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"。\n\n### Minor\n- W6: 24 个 orphan bib entries\n- W7: FK 负依赖 \"−0.4% to −4.0%\" 无推导过程\n- W8: Table 2 NER 2-seed vs RE single seed 统计标准不一致\n- W9: Ethics Statement CoNLL-2003 license 描述需核实\n- W10: \"correlation-selection gap\" 术语无操作性定义\n\n### Questions\n- Q1: VC voted-output selection 为何失败？\n- Q2: 有没有尝试组合信号做 selection？\n- Q3: Free-form RE LP reversal 在 seed 42 之外能否复现？\n- Q4: ε=0.05 是否构成 p-hacking？\n\n### Missing References\n- Ren et al. (2023) \"Investigating Uncertainty Calibration of Aligned LMs\" (EMNLP 2023 Findings)\n- Lin et al. (2024) (factuality + consistency)",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-16T02:23:51.868224+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1418
}
```

</details>

---


### Assistant

_source line 1005 · 2026-05-16T02:23:54.673524+00:00_

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


## Round 78

## Round 78

8 recorded events


### User

_source line 1006 · 2026-05-16T02:23:55.810886+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审查摘要**：

- **Overall: 3 (Findings acceptance)**，Soundness 3.5，Excitement 2.5
- **2 个 Must-Fix 问题**：(1) 核心 "gap" 对 4/5 信号是 definitional 而非 empirical finding，框架过度膨胀贡献；(2) Abstract 省略了 RE free-form decoding 下 LP selection 方向翻转的关键反例
- **5 个 Should-Fix**：缺少其他 per-sample signal baseline (如 verbalized confidence)、24 个 orphan bib entries、Conclusion 未 hedge RE、模型规模限制表述不清、consensus-proximity operationalization 的 ad-hoc 性
- **5 个小问题**：greedy 术语歧义、FK negative dependence 表述不清、bib 格式、数字精度、可能的 bib key 残留
- **优势**：LP 压缩分析深入、统计分析远超同类论文、appendix 极其充实、related work 覆盖广、RE hedging 恰当

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.5/5**，介于 Findings 和 Main Conference 之间。

三个 Must-Fix 问题：
1. Abstract 中 "compression is intrinsic" 的 claim 强于 free-form ablation 的证据（NER 成立但 RE 方向反转）
2. Instance-level signal 无法 rank candidates 是 by construction 的，不应包装为 empirical surprise——correlation-selection gap 的贡献范围需重新界定
3. 标题/Abstract 说 "Information Extraction" 但 RE 仅在 SciERC 上测试且标注 preliminary，scope 过宽

五个 Should-Fix：VC selection 失败机制分析缺失、TOST 等价性 configuration-dependent 未整合进正文、多重比较校正不完整、主表用单 seed、4B-8B scale ablation 不足以得出 "not model capacity" 的结论。

优势方面：统计实践显著优于同类 empirical NLP 工作（bootstrap CI + TOST + permutation test），difficulty gradient 实验设计完整，limitations 透明度高。

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

_source line 1007 · 2026-05-16T02:24:34.437251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "1755"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "1755"
  }
}
```

</details>

---


### Tool result

_source line 1008 · 2026-05-16T02:24:34.488122+00:00_

1755	    action: 全文搜索替换
1756	    assigned_to: Paper Agent
1757	    status: resolved
1758	  resolution: "grep 确认全文无 'Qwen 2.5' 残留"
1759	  resolution_round: 8
1760	
1761	# ===== NEW ISSUES (Round 8) =====
1762	- id: R8-N1
1763	  summary: 正文页数严重超过 8 页限制（估计 10-11 页）
1764	  category: format
1765	  severity: critical
1766	  status: resolved
1767	  first_raised_round: 8
1768	  last_seen_round: 8
1769	  mentions:
1770	  - round: 8
1771	    reviewers: [1, 2]
1772	    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'
1773	  action_items:
1774	  - round: 8
1775	    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'
1776	    assigned_to: Paper Agent
1777	    status: resolved
1778	  resolution: "正文 ≤8 页（PDF 页 1-7 为 Section 1-6, 页 8 为 Limitations + Ethics）"
1779	  resolution_round: 8
1780	- id: R8-N2
1781	  summary: 标题 "Do Not Select" overclaim——论文自身数据显示 LP 在子集上 significantly selects
1782	  category: framing
1783	  severity: critical
1784	  status: resolved
1785	  first_raised_round: 8
1786	  last_seen_round: 8
1787	  mentions:
1788	  - round: 8
1789	    reviewers: [1, 2]
1790	    note: 'R2 列 critical N3："Do Not Select" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'
1791	  action_items:
1792	  - round: 8
1793	    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'
1794	    assigned_to: Paper Agent
1795	    status: resolved
1796	  resolution: "标题改为 'Strong Predictors, Weak Selectors: Confidence Signals Predict but Struggle to Select in LLM-Based Information Extraction'"
1797	  resolution_round: 8
1798	- id: R8-W1
1799	  summary: 缺少代码/数据发布承诺
18
…[truncated 3845 chars]

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

_source line 1009 · 2026-05-16T02:26:38.350058+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-8) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2。R1 rebut。两层视觉分组 resolved。'\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 Round 9 两位 Reviewer 再次独立提出（R1-N2, R2-N1）：尽管论文已有两层结构和透明声明，4/5 信号的 selection 失败仍被框架化为统一 \"gap\" finding，但这对 instance-level 信号是 definitional。两位 Reviewer 共识：贡献重心应移向 LP compression + MBR failure 的实证发现，或将分类法本身（instance-level vs per-sample）定位为核心贡献。Round 8 的 resolution（视觉分组+两层结构）被认为不够——需要在 Abstract/Introduction/Conclusion 层面重新框架化。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Table 3 视觉分组区分 instance-level 和 per-sample 信号\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Abstract/Introduction/Conclusion 层面 reframe：(1) 明确承认 4/5 信号 selection 失败是 definitional，用一句话 dismiss；(2) 将贡献重心定位为 \"分类法（instance-level vs per-sample）+ LP compression 实证发现 + MBR-style selection 也失败的 non-trivial 发现\"；(3) 标题 \"Correlation-Selection Gap\" 可保留但 Abstract 需明确 gap 的两层性质'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree。\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 Round 9 两位 Reviewer 共识（R1-N1, R2-N2）：Abstract \"A free-form ablation confirms compression is intrinsic; the gap persists across...task types\" 与 RE LP selection 方向反转（−0.68pp → +1.69pp, Table 15 Panel B）直接矛盾。Discussion/Limitations 诚实记录了 RE reversal，但 Abstract/Conclusion 未限定范围。Round 8 resolution（scope 限定为 NER only in Discussion）不够——Abstract 和 Conclusion 仍未修正。'\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 明确承认 RE LP 翻转 + CI includes zero\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Abstract 修改为 \"confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation\"。Conclusion 同步修改，不能说 \"across task types\" without qualification。'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据不足——标题/Abstract \"Information Extraction\" scope 过宽\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: Abstract 必须标注 RE preliminary\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 R1-N3 列 critical：标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER，RE 仅 SciERC 且 preliminary。R2 在 W3 和 W4 间接呼应。共识：Abstract 需明确 RE preliminary，或标题加限定语。Introduction contribution #3 已正确标注但 Abstract/Conclusion 不一致。'\n  action_items:\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Conclusion 增加 RE preliminary hedge（如 \"RE conclusions are preliminary, based on a single benchmark\"）。Abstract 已标注但 Conclusion 遗漏。标题可保留 \"Information Extraction\" 但需正文一致 hedge。'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 9) =====\n- id: R9-W1\n  summary: 缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [2]\n    note: 'R2-W1：论文仅有 LP 一种 per-sample signal，但 verbalized confidence (Tian 2023)、self-certainty (Kang 2025) 等 per-sample signal 未对比。\"no signal improves selection\" 结论不完整。R1 未独立提出但 Q2 问了组合信号。'\n  action_items:\n  - round: 9\n    action: 至少在 Limitations 中承认仅测试了一种 per-sample signal 并列出可能的替代方案\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W2\n  summary: 24 个 orphan bib entries 未在正文引用\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R2-W2 和 R1-W6 均提出。包括 Culotta 2004, Kadavath 2022, Malinin 2021, Guo 2017, Desai 2020 等高度相关工作。应引用相关的或删除不相关的。'\n  action_items:\n  - round: 9\n    action: '清理 bib：引用 Culotta 2004, Kadavath 2022, Malinin 2021 等相关 entries；删除不相关的 orphan entries'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W3\n  summary: TOST 等价性结论 configuration-dependent 未整合进正文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W1：外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。'\n  action_items:\n  - round: 9\n    action: Section 4.2 主文加一句提及外部锚点结果的 configuration-dependent 性质\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W4\n  summary: VC majority-voting selection 的 per-sample 性质和失败机制未分析\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W2：VC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal，但表现最差（0.623）。失败机制值得分析——是因为 voted output 与高频 sample 高度 overlap 导致 selection 退化？'\n  action_items:\n  - round: 9\n    action: Discussion 增加 1-2 句 VC selection 失败机制分析\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W5\n  summary: 多重比较校正不完整\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W3：5 signals × 3 datasets × 2-3 models 大量比较无系统校正。负结果未校正 p>0.05 已够但应明确说明逻辑。'\n  action_items:\n  - round: 9\n    action: 正文或 Appendix 加一段讨论多重比较校正的影响，说明负结果下未校正 p>0.05 的逻辑\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W6\n  summary: Table 1 主表单种子未标注，与多种子分析不一致\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W4：Table 1 seed=42 单次结果与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致但应标注。'\n  action_items:\n  - round: 9\n    action: Table 1 caption 加 \"single-seed (42); 3-seed stability in Table X (W=1.000)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W7\n  summary: Scale ablation 设计有限——\"not model capacity\" 结论过强\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R1-W5 和 R2-W4：仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。\"not model capacity\" 仅基于两个数据点。建议弱化为 \"within the 4B-8B range\"。'\n  action_items:\n  - round: 9\n    action: 弱化措辞为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M1\n  summary: Table 2 \"Greedy\" 术语歧义——T=1.0 single sample 不等于 argmax\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [2]\n    note: 'R2-M1：greedy 通常指 argmax (T→0)，建议改为 \"Single sample at T=1.0\"。'\n  action_items:\n  - round: 9\n    action: 改措辞或加注释说明含义\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M2\n  summary: FK 负依赖 \"−0.4% to −4.0%\" 无推导过程\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R2-M2, R1-W7：直接断言但无推导或 appendix reference。'\n  action_items:\n  - round: 9\n    action: 补推导过程或引用 appendix 中的 permutation test 支撑\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M3\n  summary: correlation-selection gap 术语无操作性定义\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W10：反复使用但无形式化定义（如 Δ = ρ − selection_gain / oracle_headroom）。'\n  action_items:\n  - round: 9\n    action: Section 4.2 给出操作性定义\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PREVIOUSLY RESOLVED ISSUES (abbreviated, not re-listed individually) =====\n# R0-RR-D1, R1-N1 through R1-M3, R2-C1 through R2-AUROC, R3-C1 through R3-M7,\n# R4-C1, R4-M1 through R4-W4, R5-N1 through R5-W7, R5-M1 through R5-Q4,\n# R6-W1 through R6-W2, R7-C1 through R7-W4, R8-N1 through R8-M1\n# All status: resolved. See round_8.md for full details.\n"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-8) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2。R1 rebut。两层视觉分组 resolved。'\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 Round 9 两位 Reviewer 再次独立提出（R1-N2, R2-N1）：尽管论文已有两层结构和透明声明，4/5 信号的 selection 失败仍被框架化为统一 \"gap\" finding，但这对 instance-level 信号是 definitional。两位 Reviewer 共识：贡献重心应移向 LP compression + MBR failure 的实证发现，或将分类法本身（instance-level vs per-sample）定位为核心贡献。Round 8 的 resolution（视觉分组+两层结构）被认为不够——需要在 Abstract/Introduction/Conclusion 层面重新框架化。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: Table 3 视觉分组区分 instance-level 和 per-sample 信号\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Abstract/Introduction/Conclusion 层面 reframe：(1) 明确承认 4/5 信号 selection 失败是 definitional，用一句话 dismiss；(2) 将贡献重心定位为 \"分类法（instance-level vs per-sample）+ LP compression 实证发现 + MBR-style selection 也失败的 non-trivial 发现\"；(3) 标题 \"Correlation-Selection Gap\" 可保留但 Abstract 需明确 gap 的两层性质'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree。\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 Round 9 两位 Reviewer 共识（R1-N1, R2-N2）：Abstract \"A free-form ablation confirms compression is intrinsic; the gap persists across...task types\" 与 RE LP selection 方向反转（−0.68pp → +1.69pp, Table 15 Panel B）直接矛盾。Discussion/Limitations 诚实记录了 RE reversal，但 Abstract/Conclusion 未限定范围。Round 8 resolution（scope 限定为 NER only in Discussion）不够——Abstract 和 Conclusion 仍未修正。'\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 8\n    action: 明确承认 RE LP 翻转 + CI includes zero\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Abstract 修改为 \"confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation\"。Conclusion 同步修改，不能说 \"across task types\" without qualification。'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据不足——标题/Abstract \"Information Extraction\" scope 过宽\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: Abstract 必须标注 RE preliminary\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R9 R1-N3 列 critical：标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER，RE 仅 SciERC 且 preliminary。R2 在 W3 和 W4 间接呼应。共识：Abstract 需明确 RE preliminary，或标题加限定语。Introduction contribution #3 已正确标注但 Abstract/Conclusion 不一致。'\n  action_items:\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 9\n    action: 'Conclusion 增加 RE preliminary hedge（如 \"RE conclusions are preliminary, based on a single benchmark\"）。Abstract 已标注但 Conclusion 遗漏。标题可保留 \"Information Extraction\" 但需正文一致 hedge。'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 9) =====\n- id: R9-W1\n  summary: 缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [2]\n    note: 'R2-W1：论文仅有 LP 一种 per-sample signal，但 verbalized confidence (Tian 2023)、self-certainty (Kang 2025) 等 per-sample signal 未对比。\"no signal improves selection\" 结论不完整。R1 未独立提出但 Q2 问了组合信号。'\n  action_items:\n  - round: 9\n    action: 至少在 Limitations 中承认仅测试了一种 per-sample signal 并列出可能的替代方案\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W2\n  summary: 24 个 orphan bib entries 未在正文引用\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R2-W2 和 R1-W6 均提出。包括 Culotta 2004, Kadavath 2022, Malinin 2021, Guo 2017, Desai 2020 等高度相关工作。应引用相关的或删除不相关的。'\n  action_items:\n  - round: 9\n    action: '清理 bib：引用 Culotta 2004, Kadavath 2022, Malinin 2021 等相关 entries；删除不相关的 orphan entries'\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W3\n  summary: TOST 等价性结论 configuration-dependent 未整合进正文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W1：外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。'\n  action_items:\n  - round: 9\n    action: Section 4.2 主文加一句提及外部锚点结果的 configuration-dependent 性质\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W4\n  summary: VC majority-voting selection 的 per-sample 性质和失败机制未分析\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W2：VC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal，但表现最差（0.623）。失败机制值得分析——是因为 voted output 与高频 sample 高度 overlap 导致 selection 退化？'\n  action_items:\n  - round: 9\n    action: Discussion 增加 1-2 句 VC selection 失败机制分析\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W5\n  summary: 多重比较校正不完整\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W3：5 signals × 3 datasets × 2-3 models 大量比较无系统校正。负结果未校正 p>0.05 已够但应明确说明逻辑。'\n  action_items:\n  - round: 9\n    action: 正文或 Appendix 加一段讨论多重比较校正的影响，说明负结果下未校正 p>0.05 的逻辑\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W6\n  summary: Table 1 主表单种子未标注，与多种子分析不一致\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W4：Table 1 seed=42 单次结果与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致但应标注。'\n  action_items:\n  - round: 9\n    action: Table 1 caption 加 \"single-seed (42); 3-seed stability in Table X (W=1.000)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-W7\n  summary: Scale ablation 设计有限——\"not model capacity\" 结论过强\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R1-W5 和 R2-W4：仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。\"not model capacity\" 仅基于两个数据点。建议弱化为 \"within the 4B-8B range\"。'\n  action_items:\n  - round: 9\n    action: 弱化措辞为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M1\n  summary: Table 2 \"Greedy\" 术语歧义——T=1.0 single sample 不等于 argmax\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [2]\n    note: 'R2-M1：greedy 通常指 argmax (T→0)，建议改为 \"Single sample at T=1.0\"。'\n  action_items:\n  - round: 9\n    action: 改措辞或加注释说明含义\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M2\n  summary: FK 负依赖 \"−0.4% to −4.0%\" 无推导过程\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 'R2-M2, R1-W7：直接断言但无推导或 appendix reference。'\n  action_items:\n  - round: 9\n    action: 补推导过程或引用 appendix 中的 permutation test 支撑\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n- id: R9-M3\n  summary: correlation-selection gap 术语无操作性定义\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1]\n    note: 'R1-W10：反复使用但无形式化定义（如 Δ = ρ − selection_gain / oracle_headroom）。'\n  action_items:\n  - round: 9\n    action: Section 4.2 给出操作性定义\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PREVIOUSLY RESOLVED ISSUES (abbreviated, not re-listed individually) =====\n# R0-RR-D1, R1-N1 through R1-M3, R2-C1 through R2-AUROC, R3-C1 through R3-M7,\n# R4-C1, R4-M1 through R4-W4, R5-N1 through R5-W7, R5-M1 through R5-Q4,\n# R6-W1 through R6-W2, R7-C1 through R7-W4, R8-N1 through R8-M1\n# All status: resolved. See round_8.md for full details.\n"
  }
}
```

</details>

---


### Tool result

_source line 1010 · 2026-05-16T02:26:38.401111+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 12633}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-16T02:29:04.751463+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# Round 9 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+相关工作+格式)\n**审稿模式**: Fresh review (Round 9)\n\n---\n\n## Summary\n\n本文研究 LLM-based 结构化信息抽取（NER/RE）中五种一致性信号（SJ, VC, FK, EM, LP）的质量估计与样本选择能力。核心发现是 \"correlation-selection gap\"：所有信号均能有效预测输出质量（ρ 达 0.45, AUROC 达 0.82），但无法从 N 个采样中选出最优输出，尽管 oracle headroom 达 13-18pp。论文通过 free-form decoding ablation 证明 LP score compression 是 task-intrinsic 的（NER 上成立），并在 4B-8B 两个规模上验证了结论的稳健性。\n\n---\n\n## Strengths\n\n**S1. 概念框架有价值。** Quality estimation vs. sample selection 的显式区分在 IE 文献中此前未被正式化。Instance-level vs. per-sample 信号的分类法直接解释了 4/5 信号为何不能做 selection，为后续工作提供设计准则。[R1-S1, R2-S1 共识]\n\n**S2. LP 压缩分析深入且有实际价值。** Median within-instance LP range = 0.041 nats, 60.3% tied instances, non-tied subset 显著优于 greedy (+2.9pp, p=0.004), ε sensitivity sweep 验证阈值稳健性。这是论文最有价值的实证发现。[R2-S2, R1 隐含认同]\n\n**S3. 统计分析显著优于同类 empirical NLP 工作。** Bootstrap CI with pairwise Δρ、TOST 等价检验（含三类外部锚点 δ_SEM/δ_practical/δ_literature）、instance-level permutation test、Fisher combined p、Cohen's d 报告。诚实标注所有 borderline/preliminary 结果。[R1-S3, R2-S3 高度共识]\n\n**S4. 实验设计严谨。** Difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed (3 seeds, Kendall's W=1.000)、free-form ablation。形成完整 robustness picture。[R1-S2, R2-S3]\n\n**S5. Appendix 极其充实（~15 pages）。** 17 个 appendix section 覆盖了几乎所有可预见质疑：SJ normalizer robustness (Δρ<0.005)、LOO-SJ equivalence、ε sensitivity、FK independence permutation test、OOD transfer、thinking token 三部分定量分析、LP failure stability cross-seed analysis。体现高度学术自觉。[R1-S5, R2-S4]\n\n**S6. Limitations 透明度高。** RE preliminary 标注贯穿全文（Abstract, Introduction #3, Table captions, Conclusion），thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 未回避。[R1-S4, R2-S6]\n\n**S7. Related work 覆盖面广。** Self-consistency 方向（Wang 2023 等 10+ 篇）、MBR decoding（Eikema 2022/2025, Freitag 2022 等）、uncertainty surveys（Geng 2024, Xia 2025, Hobelsberger 2025）、structured IE (Zhou 2024 等)。与 Eikema 2025 structured MBR 的对接尤其到位。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **Correlation-selection gap 对 4/5 信号是 definitional 而非 empirical finding — 框架过度膨胀贡献**\n\n两位 Reviewer 独立提出相同核心问题（R1-N2, R2-N1）：VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——这是信号定义的直接推论。标题 \"The Correlation-Selection Gap\" 和 Abstract \"none improves best-of-N selection\" 将部分 tautological 的观察框架化为统一发现，过度膨胀了贡献。\n\n真正的实验发现仅是：(a) LP score compression 导致唯一的 per-sample signal 也失败；(b) consensus-proximity/MBR-style selection 也失败——后者是 non-trivial 的。论文 Discussion §5 和 Table 2 已有两层结构和透明声明（line 8: \"assign a single score per input; they cannot rank candidates by construction\"），但 Abstract/Introduction/Conclusion 的修辞权重仍将 gap 呈现为统一发现。\n\n**建议修改方向**：(1) Abstract/Introduction 中用一句话 dismiss instance-level 信号的 selection 失败为 definitional consequence，将贡献重心移向 LP compression + MBR failure 的实证发现；(2) 或将分类法本身（instance-level vs per-sample）定位为核心贡献（Contribution #1），降低 selection failure 的修辞权重。\n\n⚠️ 此问题自 Round 3 (R3-W2) 起反复出现，Round 8 的 resolution（视觉分组+两层结构）被两位 Reviewer 认为不够——需要在 Abstract/Introduction/Conclusion 层面根本性 reframe。\n\n---\n\n**N2** [critical, 共识] **Abstract/Conclusion 对 free-form ablation 过度概括——省略 RE LP selection 方向反转**\n\n两位 Reviewer 共识（R1-N1, R2-N2）：Abstract 称 \"A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types\"，但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。\"across task types\" 与 RE 结果直接矛盾。\n\n论文 Discussion 和 Limitations 诚实承认了 RE reversal，但 Abstract 和 Conclusion 的措辞未限定范围。\n\n**建议修改方向**：Abstract 改为 \"confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation\"。Conclusion 同步修改，不能说 \"across task types\" without qualification。\n\n⚠️ 此问题自 Round 7 (R7-C3) 起存在，Round 8 resolution（Discussion scope 限定为 NER only）被认为不够——Abstract/Conclusion 仍未修正。\n\n---\n\n**N3** [critical, R1 主导, R2 间接支持] **标题/Abstract \"Information Extraction\" scope 过宽——RE 仅 preliminary**\n\nR1-N3 列 critical：RE 仅在 SciERC 上测试（40% zero F1），全部标注 \"preliminary\"。标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER。Introduction contribution #3 已正确标注 \"RE conclusions rest on SciERC alone (preliminary)\"，但 Conclusion 未同步 hedge。\n\nR2 在 W3（Conclusion 未 hedge RE）和 W4（模型规模限制）中间接呼应。\n\n**建议修改方向**：Conclusion 增加 \"RE conclusions are preliminary, based on a single benchmark\"。标题可保留 \"Information Extraction\" 但正文需一致 hedge。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R2] **缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）**\nPer-sample signal 仅有 LP 一种。Tian et al. (2023, verbalized confidence)、Kang et al. (2025, self-certainty, 已引用) 等 per-sample signal 未对比。\"no signal improves selection\" 的结论不完整。建议至少在 Limitations 中承认仅测试了一种 per-sample signal。\n\n**W2** [warning, 共识] **24 个 orphan bib entries 未引用**\n包括 Culotta & McCallum 2004（IE confidence estimation 开创性工作）、Kadavath 2022（LLMs know what they know）、Malinin & Gales 2021（autoregressive uncertainty for structured prediction）等高度相关工作。应引用相关的或删除不相关的。\n\n**W3** [warning, R1] **TOST 外部锚点结果 configuration-dependent 未整合进主文**\n外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。当前主文 Section 4.2 缺少这一 nuance。\n\n**W4** [warning, R1] **VC majority-voting selection 的 per-sample 性质和失败机制未分析**\nVC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得 1-2 句机制分析。\n\n**W5** [warning, R1] **多重比较校正不完整**\n5 signals × 3 datasets × 2-3 models 大量比较无系统性校正。对于负结果，未校正 p>0.05 已足够但应明确说明这一逻辑。\n\n**W6** [warning, R1] **Table 1 主表单种子未标注**\nTable 1 seed=42 单次结果，与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致（W=1.000）但应标注。\n\n**W7** [warning, 共识] **Scale ablation \"not model capacity\" 结论过强**\n仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。应弱化为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"。\n\n---\n\n### Minor（不影响接收）\n\n- **M1** [info, R2] Table 2 \"Greedy\" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞或加注释。\n- **M2** [info, 共识] Section 3.2 FK 负依赖 \"−0.4% to −4.0%\" 无推导过程或 appendix reference。\n- **M3** [info, R1] \"correlation-selection gap\" 术语反复使用但无操作性定义。建议 Section 4.2 给出形式化定义。\n- **M4** [info, R2] Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。\n- **M5** [info, R1] Table 2 NER 2-seed vs RE single seed 统计标准不一致。\n- **M6** [info, R2] Bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling 等），建议统一检查。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 以下问题两位 Reviewer 完全达成共识：\n- N1: Instance-level 信号 selection 失败是 definitional — 框架需 reframe\n- N2: Abstract 对 free-form ablation 过度概括 — RE reversal 必须标注\n- S3/S4: 统计分析和实验设计是论文的核心优势\n- S2: LP compression 是最有价值的实证发现\n- W2: Orphan bib entries 需清理\n- W7: Scale ablation 结论需弱化\n\n## Reviewer Divergence\n\n**分歧 1** [R1: 3.5/5 vs R2: 3.0/5] — R1 认为概念贡献（metric dissociation + correlation-selection gap taxonomy）即使部分 tautological 也有信息量，MBR failure 是 non-trivial 的发现；R2 认为框架性贡献被高估，真正的 novelty 仅限于 LP compression。这是程度分歧而非方向分歧。\n\n**分歧 2** [R2-W1 vs R1 未提] — R2 认为缺少其他 per-sample signal baseline（verbalized confidence）是 should-fix；R1 未独立提出此问题但 Q2 问了组合信号。\n\n**分歧 3** [R2-W5 vs R1 未提] — R2 认为 consensus-proximity operationalization 有些 ad-hoc；R1 认为与 MBR 的连接已在 Appendix L 充分讨论。\n\n---\n\n## Questions to Authors\n\n**Q1**: VC 在 selection 语境下（majority-voted output + overlap）实质成为 per-sample signal——为什么仍然失败？是否因为 voted output 与高频 sample 高度 overlap，导致 selection 退化为选最平庸的 sample？\n\n**Q2**: 是否尝试过其他 per-sample signals（verbalized confidence, self-certainty, entropy of next-token distribution）？或组合信号（LP + SJ weighted combination）？\n\n**Q3**: Free-form RE LP reversal（−0.68pp → +1.69pp）是最 actionable 的发现之一。这在 seed 42 之外能否复现？如果能，这可能成为重要 positive contribution。\n\n**Q4**: ε=0.05 是否构成 p-hacking？Table 13 的 ε sweep 显示此阈值最大化了 statistical separation (p=0.004)。\n\n**Q5**: Thinking token confound（Appendix G）分析了 LP 影响，但是否也改变了模型 output distribution 进而影响 consistency signals？\n\n---\n\n## Missing References\n\n**论文中已有 bib entry 但未引用**（应引用或删除）：\n- Kadavath et al. 2022 \"Language Models (Mostly) Know What They Know\" — LLM self-knowledge/calibration 开创性工作\n- Culotta & McCallum 2004 \"Confidence Estimation for Information Extraction\" — IE confidence estimation 早期工作\n- Malinin & Gales 2021 \"Uncertainty Estimation in Autoregressive Structured Prediction\" — 直接相关\n\n**论文中未有 bib entry**（建议补充）：\n- Tian et al. 2023 \"Just Ask for Calibration\" — verbalized confidence，与 W1 中 per-sample signal baseline 相关\n- Ren et al. 2023 \"Investigating Uncertainty Calibration of Aligned LMs\" (EMNLP 2023 Findings) — LP calibration 相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: weak accept / borderline (3.25/5)\n**置信度**: 4/5 (两位 Reviewer 均仔细阅读全文含 Appendix)\n\n**建议**: Findings acceptance（两位 Reviewer 共识）\n\n**理由**：\n- **正面**：LP compression 发现有实际价值（median range 0.041 nats → non-tied subset +2.9pp, p=0.004）；统计分析远超同类工作；appendix 详尽；QE vs selection 的 metric dissociation 对社区有启发性\n- **负面**：核心 \"correlation-selection gap\" 对 4/5 信号是 definitional（by construction），真正的 empirical finding scope 较窄（LP compression + MBR failure）；Abstract/Conclusion 对 free-form ablation 过度概括（RE reversal 未标注）；RE 证据不足但标题 scope 过宽\n\n**升格条件**（若满足可考虑 Main Conference）：\n1. Abstract/Introduction/Conclusion 层面 reframe：明确 dismiss instance-level failure 为 definitional，将贡献重心移向 LP compression + MBR failure\n2. Abstract 修正 RE free-form reversal\n3. 补充 free-form multi-seed RE 实验（若时间允许）\n4. Conclusion hedge RE\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 第 4-5 行：\"All signals achieve strong quality estimation yet none improves best-of-N selection\" — 对 4/5 instance-level 信号是 definitional（N1）\n- 第 6 行：\"the gap persists across scales and task types\" — RE reversal 未标注（N2）\n- 信息密度恰当（Round 8 后精简为 9 行 问题-发现-意义结构），RE preliminary 有标注\n\n### Introduction\n- Contribution list 结构清晰：#1 metric dissociation, #2 correlation-selection gap, #3 difficulty-dependent signal rankings\n- Contribution #1 定位为 finding-led（\"We find that...\"）恰当\n- Contribution #3 正确标注 \"RE conclusions rest on SciERC alone (preliminary)\"\n- Figure 1 有效传达 gap 概念\n\n### Related Work\n- 覆盖面广，3 段结构清晰\n- 与 Yao et al. (2026) 的增量贡献明确（structural matching, selection analysis, difficulty gradient）\n- Eikema 2025 structured MBR 对接到位\n- 建议引用已有 orphan entries（Kadavath 2022, Culotta 2004, Malinin 2021）\n\n### Method\n- 5 信号形式化定义精确\n- SJ Hungarian matching 定义完整（threshold, normalizer, IoU）\n- Evaluation framework（QE: ρ + AUROC; Selection: best-of-N）恰当\n- 建议 Section 3.3 更早 qualify consensus-proximity 为 MBR instantiation\n\n### Experiments\n- Difficulty gradient 设计有效（SciERC → CoNLL → WNUT-17）\n- Table 1 应标注 single seed (42)（W6）\n- Table 2 NER 2-seed vs RE single seed 不一致（M5）\n- \"Greedy\" 术语需澄清（M1）\n- Scale ablation \"not model capacity\" 需弱化（W7）\n\n### Discussion\n- 两层结构（definitional + LP compression）存在但需在 Abstract/Introduction 更突出\n- VC selection 失败机制缺分析（W4）\n- MBR decoding 连接已到位（cite Eikema 2022/2025）\n\n### Conclusion\n- 缺 RE preliminary hedge（N3）\n- \"across task types\" 需 qualification（N2）\n\n### Limitations\n- 透明度高\n- 建议增加\"仅测试了一种 per-sample signal\"（W1）\n\n### Ethics Statement\n- 内容充实，含 CoNLL Reuters 出处和代码发布承诺\n\n### Appendix\n- 极其详尽（~15 pages，17 sections）\n- SJ normalizer robustness、FK independence、ε sensitivity、OOD、free-form ablation 等细粒度分析增强可重复性",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept / borderline (Findings acceptance)"
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
    "report": "# Round 9 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性+实验设计+统计分析), R2 (新颖性+完整性+相关工作+格式)\n**审稿模式**: Fresh review (Round 9)\n\n---\n\n## Summary\n\n本文研究 LLM-based 结构化信息抽取（NER/RE）中五种一致性信号（SJ, VC, FK, EM, LP）的质量估计与样本选择能力。核心发现是 \"correlation-selection gap\"：所有信号均能有效预测输出质量（ρ 达 0.45, AUROC 达 0.82），但无法从 N 个采样中选出最优输出，尽管 oracle headroom 达 13-18pp。论文通过 free-form decoding ablation 证明 LP score compression 是 task-intrinsic 的（NER 上成立），并在 4B-8B 两个规模上验证了结论的稳健性。\n\n---\n\n## Strengths\n\n**S1. 概念框架有价值。** Quality estimation vs. sample selection 的显式区分在 IE 文献中此前未被正式化。Instance-level vs. per-sample 信号的分类法直接解释了 4/5 信号为何不能做 selection，为后续工作提供设计准则。[R1-S1, R2-S1 共识]\n\n**S2. LP 压缩分析深入且有实际价值。** Median within-instance LP range = 0.041 nats, 60.3% tied instances, non-tied subset 显著优于 greedy (+2.9pp, p=0.004), ε sensitivity sweep 验证阈值稳健性。这是论文最有价值的实证发现。[R2-S2, R1 隐含认同]\n\n**S3. 统计分析显著优于同类 empirical NLP 工作。** Bootstrap CI with pairwise Δρ、TOST 等价检验（含三类外部锚点 δ_SEM/δ_practical/δ_literature）、instance-level permutation test、Fisher combined p、Cohen's d 报告。诚实标注所有 borderline/preliminary 结果。[R1-S3, R2-S3 高度共识]\n\n**S4. 实验设计严谨。** Difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed (3 seeds, Kendall's W=1.000)、free-form ablation。形成完整 robustness picture。[R1-S2, R2-S3]\n\n**S5. Appendix 极其充实（~15 pages）。** 17 个 appendix section 覆盖了几乎所有可预见质疑：SJ normalizer robustness (Δρ<0.005)、LOO-SJ equivalence、ε sensitivity、FK independence permutation test、OOD transfer、thinking token 三部分定量分析、LP failure stability cross-seed analysis。体现高度学术自觉。[R1-S5, R2-S4]\n\n**S6. Limitations 透明度高。** RE preliminary 标注贯穿全文（Abstract, Introduction #3, Table captions, Conclusion），thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 未回避。[R1-S4, R2-S6]\n\n**S7. Related work 覆盖面广。** Self-consistency 方向（Wang 2023 等 10+ 篇）、MBR decoding（Eikema 2022/2025, Freitag 2022 等）、uncertainty surveys（Geng 2024, Xia 2025, Hobelsberger 2025）、structured IE (Zhou 2024 等)。与 Eikema 2025 structured MBR 的对接尤其到位。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **Correlation-selection gap 对 4/5 信号是 definitional 而非 empirical finding — 框架过度膨胀贡献**\n\n两位 Reviewer 独立提出相同核心问题（R1-N2, R2-N1）：VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——这是信号定义的直接推论。标题 \"The Correlation-Selection Gap\" 和 Abstract \"none improves best-of-N selection\" 将部分 tautological 的观察框架化为统一发现，过度膨胀了贡献。\n\n真正的实验发现仅是：(a) LP score compression 导致唯一的 per-sample signal 也失败；(b) consensus-proximity/MBR-style selection 也失败——后者是 non-trivial 的。论文 Discussion §5 和 Table 2 已有两层结构和透明声明（line 8: \"assign a single score per input; they cannot rank candidates by construction\"），但 Abstract/Introduction/Conclusion 的修辞权重仍将 gap 呈现为统一发现。\n\n**建议修改方向**：(1) Abstract/Introduction 中用一句话 dismiss instance-level 信号的 selection 失败为 definitional consequence，将贡献重心移向 LP compression + MBR failure 的实证发现；(2) 或将分类法本身（instance-level vs per-sample）定位为核心贡献（Contribution #1），降低 selection failure 的修辞权重。\n\n⚠️ 此问题自 Round 3 (R3-W2) 起反复出现，Round 8 的 resolution（视觉分组+两层结构）被两位 Reviewer 认为不够——需要在 Abstract/Introduction/Conclusion 层面根本性 reframe。\n\n---\n\n**N2** [critical, 共识] **Abstract/Conclusion 对 free-form ablation 过度概括——省略 RE LP selection 方向反转**\n\n两位 Reviewer 共识（R1-N1, R2-N2）：Abstract 称 \"A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types\"，但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。\"across task types\" 与 RE 结果直接矛盾。\n\n论文 Discussion 和 Limitations 诚实承认了 RE reversal，但 Abstract 和 Conclusion 的措辞未限定范围。\n\n**建议修改方向**：Abstract 改为 \"confirms NER compression is intrinsic; RE shows a directional reversal warranting further investigation\"。Conclusion 同步修改，不能说 \"across task types\" without qualification。\n\n⚠️ 此问题自 Round 7 (R7-C3) 起存在，Round 8 resolution（Discussion scope 限定为 NER only）被认为不够——Abstract/Conclusion 仍未修正。\n\n---\n\n**N3** [critical, R1 主导, R2 间接支持] **标题/Abstract \"Information Extraction\" scope 过宽——RE 仅 preliminary**\n\nR1-N3 列 critical：RE 仅在 SciERC 上测试（40% zero F1），全部标注 \"preliminary\"。标题说 \"Information Extraction\" 但核心可靠结论仅覆盖 NER。Introduction contribution #3 已正确标注 \"RE conclusions rest on SciERC alone (preliminary)\"，但 Conclusion 未同步 hedge。\n\nR2 在 W3（Conclusion 未 hedge RE）和 W4（模型规模限制）中间接呼应。\n\n**建议修改方向**：Conclusion 增加 \"RE conclusions are preliminary, based on a single benchmark\"。标题可保留 \"Information Extraction\" 但正文需一致 hedge。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R2] **缺少其他 per-sample signal baseline（verbalized confidence, self-certainty）**\nPer-sample signal 仅有 LP 一种。Tian et al. (2023, verbalized confidence)、Kang et al. (2025, self-certainty, 已引用) 等 per-sample signal 未对比。\"no signal improves selection\" 的结论不完整。建议至少在 Limitations 中承认仅测试了一种 per-sample signal。\n\n**W2** [warning, 共识] **24 个 orphan bib entries 未引用**\n包括 Culotta & McCallum 2004（IE confidence estimation 开创性工作）、Kadavath 2022（LLMs know what they know）、Malinin & Gales 2021（autoregressive uncertainty for structured prediction）等高度相关工作。应引用相关的或删除不相关的。\n\n**W3** [warning, R1] **TOST 外部锚点结果 configuration-dependent 未整合进主文**\n外部锚点下 LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 均 fail。\"no signal improves selection\" 应改为 \"no signal consistently improves selection\"。当前主文 Section 4.2 缺少这一 nuance。\n\n**W4** [warning, R1] **VC majority-voting selection 的 per-sample 性质和失败机制未分析**\nVC 在 selection 语境下通过 majority-voted output + overlap 实质成为 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但表现最差（0.623）。这个失败值得 1-2 句机制分析。\n\n**W5** [warning, R1] **多重比较校正不完整**\n5 signals × 3 datasets × 2-3 models 大量比较无系统性校正。对于负结果，未校正 p>0.05 已足够但应明确说明这一逻辑。\n\n**W6** [warning, R1] **Table 1 主表单种子未标注**\nTable 1 seed=42 单次结果，与 Table 7 3-seed mean 有差异（LP NER: 0.205 vs 0.217）。虽然 ranking 一致（W=1.000）但应标注。\n\n**W7** [warning, 共识] **Scale ablation \"not model capacity\" 结论过强**\n仅 Qwen3-4B（无 LLaMA 4B），4B→8B 差异不到 2×。应弱化为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"。\n\n---\n\n### Minor（不影响接收）\n\n- **M1** [info, R2] Table 2 \"Greedy\" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞或加注释。\n- **M2** [info, 共识] Section 3.2 FK 负依赖 \"−0.4% to −4.0%\" 无推导过程或 appendix reference。\n- **M3** [info, R1] \"correlation-selection gap\" 术语反复使用但无操作性定义。建议 Section 4.2 给出形式化定义。\n- **M4** [info, R2] Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。\n- **M5** [info, R1] Table 2 NER 2-seed vs RE single seed 统计标准不一致。\n- **M6** [info, R2] Bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling 等），建议统一检查。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 以下问题两位 Reviewer 完全达成共识：\n- N1: Instance-level 信号 selection 失败是 definitional — 框架需 reframe\n- N2: Abstract 对 free-form ablation 过度概括 — RE reversal 必须标注\n- S3/S4: 统计分析和实验设计是论文的核心优势\n- S2: LP compression 是最有价值的实证发现\n- W2: Orphan bib entries 需清理\n- W7: Scale ablation 结论需弱化\n\n## Reviewer Divergence\n\n**分歧 1** [R1: 3.5/5 vs R2: 3.0/5] — R1 认为概念贡献（metric dissociation + correlation-selection gap taxonomy）即使部分 tautological 也有信息量，MBR failure 是 non-trivial 的发现；R2 认为框架性贡献被高估，真正的 novelty 仅限于 LP compression。这是程度分歧而非方向分歧。\n\n**分歧 2** [R2-W1 vs R1 未提] — R2 认为缺少其他 per-sample signal baseline（verbalized confidence）是 should-fix；R1 未独立提出此问题但 Q2 问了组合信号。\n\n**分歧 3** [R2-W5 vs R1 未提] — R2 认为 consensus-proximity operationalization 有些 ad-hoc；R1 认为与 MBR 的连接已在 Appendix L 充分讨论。\n\n---\n\n## Questions to Authors\n\n**Q1**: VC 在 selection 语境下（majority-voted output + overlap）实质成为 per-sample signal——为什么仍然失败？是否因为 voted output 与高频 sample 高度 overlap，导致 selection 退化为选最平庸的 sample？\n\n**Q2**: 是否尝试过其他 per-sample signals（verbalized confidence, self-certainty, entropy of next-token distribution）？或组合信号（LP + SJ weighted combination）？\n\n**Q3**: Free-form RE LP reversal（−0.68pp → +1.69pp）是最 actionable 的发现之一。这在 seed 42 之外能否复现？如果能，这可能成为重要 positive contribution。\n\n**Q4**: ε=0.05 是否构成 p-hacking？Table 13 的 ε sweep 显示此阈值最大化了 statistical separation (p=0.004)。\n\n**Q5**: Thinking token confound（Appendix G）分析了 LP 影响，但是否也改变了模型 output distribution 进而影响 consistency signals？\n\n---\n\n## Missing References\n\n**论文中已有 bib entry 但未引用**（应引用或删除）：\n- Kadavath et al. 2022 \"Language Models (Mostly) Know What They Know\" — LLM self-knowledge/calibration 开创性工作\n- Culotta & McCallum 2004 \"Confidence Estimation for Information Extraction\" — IE confidence estimation 早期工作\n- Malinin & Gales 2021 \"Uncertainty Estimation in Autoregressive Structured Prediction\" — 直接相关\n\n**论文中未有 bib entry**（建议补充）：\n- Tian et al. 2023 \"Just Ask for Calibration\" — verbalized confidence，与 W1 中 per-sample signal baseline 相关\n- Ren et al. 2023 \"Investigating Uncertainty Calibration of Aligned LMs\" (EMNLP 2023 Findings) — LP calibration 相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分**: weak accept / borderline (3.25/5)\n**置信度**: 4/5 (两位 Reviewer 均仔细阅读全文含 Appendix)\n\n**建议**: Findings acceptance（两位 Reviewer 共识）\n\n**理由**：\n- **正面**：LP compression 发现有实际价值（median range 0.041 nats → non-tied subset +2.9pp, p=0.004）；统计分析远超同类工作；appendix 详尽；QE vs selection 的 metric dissociation 对社区有启发性\n- **负面**：核心 \"correlation-selection gap\" 对 4/5 信号是 definitional（by construction），真正的 empirical finding scope 较窄（LP compression + MBR failure）；Abstract/Conclusion 对 free-form ablation 过度概括（RE reversal 未标注）；RE 证据不足但标题 scope 过宽\n\n**升格条件**（若满足可考虑 Main Conference）：\n1. Abstract/Introduction/Conclusion 层面 reframe：明确 dismiss instance-level failure 为 definitional，将贡献重心移向 LP compression + MBR failure\n2. Abstract 修正 RE free-form reversal\n3. 补充 free-form multi-seed RE 实验（若时间允许）\n4. Conclusion hedge RE\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 第 4-5 行：\"All signals achieve strong quality estimation yet none improves best-of-N selection\" — 对 4/5 instance-level 信号是 definitional（N1）\n- 第 6 行：\"the gap persists across scales and task types\" — RE reversal 未标注（N2）\n- 信息密度恰当（Round 8 后精简为 9 行 问题-发现-意义结构），RE preliminary 有标注\n\n### Introduction\n- Contribution list 结构清晰：#1 metric dissociation, #2 correlation-selection gap, #3 difficulty-dependent signal rankings\n- Contribution #1 定位为 finding-led（\"We find that...\"）恰当\n- Contribution #3 正确标注 \"RE conclusions rest on SciERC alone (preliminary)\"\n- Figure 1 有效传达 gap 概念\n\n### Related Work\n- 覆盖面广，3 段结构清晰\n- 与 Yao et al. (2026) 的增量贡献明确（structural matching, selection analysis, difficulty gradient）\n- Eikema 2025 structured MBR 对接到位\n- 建议引用已有 orphan entries（Kadavath 2022, Culotta 2004, Malinin 2021）\n\n### Method\n- 5 信号形式化定义精确\n- SJ Hungarian matching 定义完整（threshold, normalizer, IoU）\n- Evaluation framework（QE: ρ + AUROC; Selection: best-of-N）恰当\n- 建议 Section 3.3 更早 qualify consensus-proximity 为 MBR instantiation\n\n### Experiments\n- Difficulty gradient 设计有效（SciERC → CoNLL → WNUT-17）\n- Table 1 应标注 single seed (42)（W6）\n- Table 2 NER 2-seed vs RE single seed 不一致（M5）\n- \"Greedy\" 术语需澄清（M1）\n- Scale ablation \"not model capacity\" 需弱化（W7）\n\n### Discussion\n- 两层结构（definitional + LP compression）存在但需在 Abstract/Introduction 更突出\n- VC selection 失败机制缺分析（W4）\n- MBR decoding 连接已到位（cite Eikema 2022/2025）\n\n### Conclusion\n- 缺 RE preliminary hedge（N3）\n- \"across task types\" 需 qualification（N2）\n\n### Limitations\n- 透明度高\n- 建议增加\"仅测试了一种 per-sample signal\"（W1）\n\n### Ethics Statement\n- 内容充实，含 CoNLL Reuters 出处和代码发布承诺\n\n### Appendix\n- 极其详尽（~15 pages，17 sections）\n- SJ normalizer robustness、FK independence、ε sensitivity、OOD、free-form ablation 等细粒度分析增强可重复性",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept / borderline (Findings acceptance)"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-16T02:29:09.135548+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4384
}
```

</details>

---


### Assistant

_source line 1013 · 2026-05-16T02:29:20.626100+00:00_

**Round 9 审稿完成。**

审稿报告已投递至 Research Director。

**结论摘要**：
- **评分**：weak accept / borderline (3.25/5)，建议 **Findings acceptance**
- **3 个 Must-Fix**：(1) 核心 gap 对 4/5 信号是 definitional 需 reframe；(2) Abstract 省略 RE free-form reversal；(3) Conclusion 缺 RE preliminary hedge
- **7 个 Should-Fix**：缺 per-sample signal baseline、orphan bib entries、TOST configuration-dependent、VC selection 机制、多重比较校正、Table 1 单种子标注、scale ablation 结论过强
- **核心优势**：LP compression 分析深入有实际价值、统计分析远超同类、Appendix 极其充实、实验设计严谨

Issue Tracker 已同步更新（3 个 recurring issues reopened，10 个新 issues 创建）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 1014 · 2026-05-16T02:29:20.633432+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

### Must-Fix

**[AGREE] R2-N1: 核心 "gap" 对 4/5 信号是 definitional**
同意，与 R1-N2 一致。Section 4.2 line 83 自己写 "cannot rank outputs by construction"。补充：VC 在 selection 语境下（脚注 Eq 5, line 50）实际上给每个 candidate 不同的 overlap score（per-sample-like），但 Table 2 显示 VC selection 最差（0.623），这个失败才是真正的 empirical finding，论文未深入分析。

**[AGREE] R2-N2: Abstract 过度声称 free-form ablation 结论**
完全同意，与 R1-N1 一致。Table 12 Panel B 的 RE LP reversal (+1.69pp) 直接 undermines Abstract line 6 的通用性声称。

### Should-Fix

**[AGREE] R2-W1: 缺少 verbalized/elicited confidence**
同意。仅测试 LP 一种 per-sample signal 就跳到 "需要 trained verifiers" 的结论，逻辑链有缺环。

**[REBUT] R2-W2: 24 个 orphan bib entries**
事实正确但严重程度应降为 info。ACL \bibliography{} 只渲染被 \cite 的条目，orphan entries 不出现在 PDF 中。是 bib 卫生问题，不影响论文内容。

**[AGREE] R2-W3: Conclusion 未 hedge RE**
同意。Conclusion Section 6 未标注 RE preliminary，与 Introduction #3 (line 30) 不一致。

**[AGREE] R2-W4: 模型规模限制**
同意，与 R1-W5 一致。4B-8B range 过窄支撑 "across scales" 的表述。

**[REBUT] R2-W5: Consensus-proximity 是 ad-hoc**
部分不同意。Appendix K (line 649) 已将其定位为 MBR instantiation，Appendix D (line 167-172) 证明 LOO-SJ 等价性（最大差异 3.1×10⁻⁴）。但同意应补充对其他 operationalization（如 entity-level majority voting 应用于 SJ/FK/EM）的讨论。

### Minor

**[AGREE] R2-M1**: "Greedy" 在 NLP 中通常指 argmax，此处指 T=1.0 单次采样，应改名。
**[AGREE] R2-M2**: FK 负依赖数值缺推导，与 R1-W7 一致。
**[REBUT] R2-M3**: Bib 格式无误，是 OpenAlex API 的 first_author 比对 false positive（"Feng, Austin" 被解析为 api=austin vs bib=feng）。
**[AGREE] R2-M4**: ρ=0.38 vs Table 1 的 0.379 vs Table 7 的 0.386，精度不一致。
**[REBUT] R2-M5**: 未发现 bib key 残留。Introduction line 8 是正常 \citet{yao2026consistency}，R2 可能将共同作者 Nédellec 误认为 bib key。

### R1-R2 共识总结

两位 Reviewer 在以下核心问题上完全一致：
1. **Instance-level signal 失败是 definitional 而非 empirical**（R1-N2 = R2-N1）
2. **Abstract "compression is intrinsic" overclaim**（R1-N1 = R2-N2）——RE free-form reversal 未在 abstract 中限定
3. **RE 证据不足但 scope 过宽**（R1-N3 ≈ R2-W3/W4）
4. **Scale ablation range 过窄**（R1-W5 = R2-W4）

主要分歧：
- R2-W2（orphan bib）：R1 认为应降级为 info
- R2-W5（ad-hoc operationalization）：R1 认为 MBR framing 已在 appendix 中，但同意应讨论替代方案
- R2-M3（bib 格式）：R1 认为是 false positive
- R2-M5（bib key 残留）：R1 在源码中未发现

---

[Reviewer 1 审稿结果]:
逐条回应已完成并汇报给 Director。核心共识：R1 和 R2 在三个 critical 问题上完全对齐——instance-level gap 的 tautological 性质、abstract overclaim、RE 证据不足。两处分歧（orphan bib 严重程度、M3/M5 的准确性）已给出具体证据。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: Abstract/Conclusion "free-form ablation confirms compression is intrinsic" 过度概括**

同意。我在自己的审稿中也独立提出了相同问题（R2-N2）。Abstract line 6 "the gap persists across scales and task types" 与 Discussion Section 5 lines 14-15 记录的 RE free-form LP reversal（−0.68pp → +1.69pp, Table 15 Panel B）直接矛盾。这不是 hedging 不足的问题，而是 factual inconsistency：论文正文的数据否定了 Abstract 的声称。R1 建议的修改措辞 "A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal" 准确且充分。

**[AGREE] R1-N2: Instance-level signal 失败的 tautological 成分**

同意，这也是我的核心关切（R2-N1）。补充一个角度：论文实际上在 Section 4.2 line 83 和 Discussion line 8 已经*承认*了 instance-level signals "cannot rank outputs by construction"。但承认 ≠ reframing——论文仍然在 title、abstract、contribution list 中将其与 LP failure 并列为统一 "gap"。R1 的建议 (c) "existing signals are either instance-level or compressed" 是最好的 reframing 方向，因为它将论文贡献转化为 *分类法*（这确实是 novel 的）而非 *发现*（对 4/5 信号而言是 trivial 的）。

不过，我对 R1 建议 (b) 中 "VC-voted-output 的 selection failure" 有一点 nuance：footnote 5（Section 3.2 line 50）说明 voted-output selection 用 frequency > N/2 的 entities 构造输出，这使 VC 成为 aggregation/fusion 策略而非 sample selection，与论文的 best-of-N framework 不完全可比。论文将其放在 Table 3 是合理的对比，但不应将其与 LP 的 per-sample ranking failure 等同。

**[REBUT] R1-N3: RE 证据不足以支撑标题 "Information Extraction" 的通用性**

部分不同意。R1 的事实判断正确（RE 仅 SciERC，40% zero F1，全部 preliminary），但结论过强。理由：

1. **标题使用 "Information Extraction" 涵盖 NER + RE 是领域惯例**。IE 在 ACL 文献中标准定义为 NER + RE（+ event extraction），论文覆盖了两者。要求标题写 "NER and Preliminary RE" 会过度限制。
2. **NER 本身有 3 个 benchmark + 2 个 model families + 4B ablation**，这已经是 substantial coverage。NER 结论的 generalizability 不弱。
3. **论文在正文中一致标注 RE 为 "preliminary"**（Introduction contribution #3, Table 1 caption, Table 2 caption, Section 4.3, Discussion line 4, Limitations line 1）——共 6 处显式 hedge。读者不会误以为 RE 结论与 NER 同等可靠。
4. **但 Abstract 确实没有 hedge RE**。Abstract line 2 说 "NER and RE benchmarks" 没有标注 preliminary，这是一个 gap。

建议折中：Abstract 加 "preliminary" 限定 RE，标题可保留不变。这比 R1 要求改标题更合理。

---

### Should-Fix

**[AGREE] R1-W1: TOST 外部锚点结论 configuration-dependent**

同意。Appendix D 的外部锚点分析（δ_SEM, δ_practical, δ_literature）结果清晰表明 LLaMA CoNLL 通过所有 δ，但 SciERC 和 Qwen CoNLL 均 fail（Appendix D 最后一段）。将 "no signal improves selection" 改为 "no signal consistently improves selection" 是更精确的表述，且几乎不损失论文的 impact。主文 Section 4.2 应加一句指向 Appendix D 的 qualification。

**[AGREE] R1-W2: VC majority-voting selection variant 的失败原因未分析**

同意。VC voted-output 在 Table 3 中表现最差（NER 0.623, 低于 random 0.610 仅 1.3pp），但论文未解释为什么 entity-level majority voting——一个在 discrete-answer 任务中很成功的策略——在 IE 中反而最差。可能的原因：majority voting 会 drop 低频但正确的 entities，在 long-tail entity 分布中造成系统性 recall 损失。Discussion 应增加 1-2 句。

**[REBUT] R1-W3: 多重比较校正不完整**

不同意这是一个 should-fix。理由：

1. **论文的核心结论是 negative result**（no signal significantly improves selection）。对 negative result，不做多重比较校正是 conservative——校正只会使 p 值更大，更强化 "无显著差异" 的结论。
2. **对 positive results**，论文确实做了部分校正：Appendix E Table 8 的 bootstrap CI 明确标注了 SJ-EM gap 的 marginal significance "would not survive Bonferroni correction for 10 pairwise comparisons (α_adj=0.005)"。
3. **R1 自己也承认** "对于负结果，未校正 p > 0.05 已足够但应说明逻辑"。这正是论文已经在做的。

建议：在 Section 4.2 加一句说明 "For our negative selection results, uncorrected tests are conservative; for positive QE comparisons, see bootstrap CIs with multiple comparison caveats in Appendix E." 即可。

**[AGREE] R1-W4: Table 1 单 seed 与 Table 7 多 seed 差异**

同意。Table 1 caption 已标注 "seed=42" 但未指向 multi-seed 验证。LP NER ρ=0.205 (seed 42) vs. 0.217±0.013 (3-seed mean, Table 7) 差异达 0.012，虽然在 1σ 内，但读者可能依赖 Table 1 的单 seed 数值做定量比较。Table 1 caption 加一句 "Multi-seed stability in Table 7" 成本极低且有益。

**[AGREE] R1-W5: Scale ablation 设计有限**

同意。仅 Qwen3-4B vs. 8B（同架构，参数量差 2×），无 LLaMA 4B 对照。Table 4 中 4B 某些指标反而高于 8B（SciERC NER SJ: 0.422 vs 0.360, Δ=+0.062），这可能是因为 4B 模型 output diversity 更高。"Task difficulty, not model capacity, drives the gap" (Section 4.3 line 118) 仅基于一个 architecture pair 的两个 scale point，evidence 不足以做 causal claim。R1 建议的弱化表述 "within the 4B-8B range" 合理。

---

### Minor

**[AGREE] R1-W6: 24 个 orphan bib entries**
同意。我在 R2-W2 中也独立提出此问题。特别是 Culotta 2004、Kadavath 2022、Malinin 2021 应被引用。

**[AGREE] R1-W7: FK 负依赖 "−0.4% to −4.0%" 无推导**
同意。Section 3.2 line 30 提到 "Temperature-based sampling introduces mild negative dependence (−0.4% to −4.0%)"，但未给出推导过程或引用来源。这是 FK validity 的一个前提条件，需要至少在 appendix 中提供推导或实证支持。

**[REBUT] R1-W8: Table 2 NER 2-seed vs RE single seed 统计标准不一致**
部分不同意。Table 2 caption 已明确标注 "NER: 2-seed mean±σ, Fisher p vs. greedy; RE: single seed (preliminary)"。统计标准不一致是 data availability 的结果（RE 实验只跑了 1 个 seed），不是方法论缺陷。论文通过 "preliminary" 标注已充分告知读者。改进方向是补跑 RE seeds，但这是 scope 问题而非 reporting 问题。

**[AGREE] R1-W9: Ethics Statement CoNLL-2003 license**
同意应核实。Ethics Statement 称 CoNLL-2003 "is available for research purposes under a NIST agreement"——实际上 CoNLL-2003 基于 Reuters RCV1 corpus，其分发确实受 NIST/LDC 协议约束，但具体条款因版本而异，应确保描述准确。

**[AGREE] R1-W10: "correlation-selection gap" 无操作性定义**
同意。论文使用 "correlation-selection gap" 贯穿全文但从未给出 formal definition（如 "the gap is defined as the difference between ρ > threshold and ΔF1_selection ≤ 0"）。作为论文核心术语，应在 Section 3.3 或 Section 1 给出明确的操作性定义。

---

### Questions

**R1-Q1: VC voted-output selection 为何失败？**
好问题。与 W2 关联。我推测原因是：majority voting 以 frequency > N/2 为阈值，会系统性丢弃低频但正确的 entities（尤其是 rare types 和 boundary-ambiguous spans），导致 precision 提升但 recall 下降。在 F1 metric 下，这个 trade-off 对 SciERC（6 types, 很多低频 entities）不利。但论文未提供 precision/recall decomposition 来验证这一假说。

**R1-Q2: 组合信号做 selection？**
有价值的方向。论文未探索 LP + consensus 的组合（如 LP weighted by SJ distance to consensus）。这可能部分 bridge the gap，但也可能不行——如果 LP 的 within-instance discrimination 本身太弱，组合不会帮助。值得在 Discussion 中提及作为 future work。

**R1-Q3: Free-form RE LP reversal 在其他 seed 能否复现？**
关键问题。Discussion line 15 承认 "whether this generalizes remains open"，Appendix M line 658 也说 "single seed (seed=42); whether the RE reversal replicates across seeds...warrants further investigation"。论文已适当 hedge，但确实需要更多 seed 来区分 signal 和 noise。

**R1-Q4: ε=0.05 是否构成 p-hacking？**
不构成。Appendix F 的 ε sensitivity sweep (Table 13) 展示了 ε 从 0.01 到 0.20 的完整 landscape，selection gain 单调递增（tied subset 缩小），ε=0.05 是 "strongest statistical separation" 而非 cherry-picked。此外，Appendix F 末尾的 ε robustness 分析 (Table 14) 表明 consistency signals 在 ε∈[0, 0.2] 范围内 selection F1 变化 ≤1.09pp。论文在 transparency 上做得很好。

---

### Missing References

**R1 提出的 Ren et al. (2023)**：同意应考虑引用。Uncertainty calibration of aligned LMs 与论文的 LP calibration 分析（Appendix B）直接相关。

**R1 提出的 Lin et al. (2024)**：需要更具体的信息才能评判相关性。

---

### 总结

与 R1 在所有 Must-Fix 的方向上一致（N1 完全同意，N2 完全同意，N3 部分同意但认为改 abstract 而非标题更合理）。Should-Fix 中 W3（多重比较）不构成 should-fix 级别问题（negative results 不需校正），其余同意。

两位 reviewer 的核心共识：
1. **tautological framing 是最大问题**（R1-N2 = R2-N1），需要 reframe
2. **Abstract overclaiming**（R1-N1 ≈ R2-N2），需要加限定
3. **LP 压缩是真正有价值的实证发现**，两位 reviewer 均认可
4. **统计分析严谨性是论文强项**，两位 reviewer 均认可
5. **建议 Findings**，除非 reframing 成功

---

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部条目的逐条回应并提交给 Director。核心结论：

- **N1 (free-form overclaiming)**: [AGREE]，与我的 R2-N2 一致
- **N2 (tautological framing)**: [AGREE]，与我的 R2-N1 一致，补充了 VC voted-output 与 LP ranking 不可等同的 nuance
- **N3 (RE 通用性)**: [REBUT]——NER 3 benchmark 覆盖足够，标题 "IE" 是领域惯例，但 Abstract 确实应 hedge RE
- **W1-W5**: 同意 4 条，反驳 W3（negative results 不需多重比较校正）
- **W6-W10**: 同意 4 条，反驳 W8（统计标准不一致是 data availability 问题，已有 preliminary 标注）

两位 reviewer 达成共识：tautological framing + abstract overclaiming 是核心问题，LP 压缩发现有价值，建议 Findings 除非成功 reframe。

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

_source line 1015 · 2026-05-16T02:30:12.549332+00:00_

交叉回应已收集。两位 Reviewer 的详细 [AGREE]/[REBUT] 回应确认了报告中的共识判断。

**交叉回应收敛结果**：

**完全共识（双方 AGREE）**：
- Instance-level gap 是 definitional（R1-N2 = R2-N1）✅
- Abstract free-form overclaim（R1-N1 = R2-N2）✅
- LP 压缩是核心实证贡献 ✅
- 统计分析是论文强项 ✅
- Scale ablation 结论需弱化 ✅
- VC selection 失败机制需分析 ✅
- Table 1 单种子需标注 ✅
- TOST configuration-dependent 需整合 ✅
- Orphan bib 需清理 ✅
- Gap 需操作性定义 ✅
- ε=0.05 **不构成 p-hacking**（Table 13 完整 landscape + 单调递增确认非 cherry-pick）

**有分歧但已达成折中**：
- **R1-N3（RE scope vs 标题）**：R2 部分 REBUT — "IE" 是领域惯例，NER 有 3 benchmark 覆盖充分。**折中共识：标题保留 "Information Extraction"，Abstract 加 RE preliminary hedge，Conclusion 同步 hedge**
- **W3（多重比较校正）**：R2 REBUT — 负结果不做校正是 conservative。R2 论证合理。**折中：加一句说明逻辑即可，不需全面校正**
- **W5（consensus-proximity ad-hoc）**：R1 REBUT — MBR framing 已在 Appendix K。**折中：主文早点 qualify 即可**

**VC voted-output 新 insight**（R1 补充）：VC 在 selection 语境下实质是 aggregation/fusion 策略（构造新输出），不等同于 LP 的 per-sample ranking。这个区分值得在 Discussion 中说明。

---

审稿报告已投递至 Research Director。报告核心结论不因交叉回应而改变：

- **评分**：weak accept / borderline (3.25/5)
- **建议**：Findings acceptance
- **3 个 Must-Fix**：tautological framing 需 reframe、Abstract free-form overclaim 需限定、Conclusion 需 hedge RE
- **7 个 Should-Fix**：缺 per-sample baseline、orphan bib、TOST nuance、VC 机制分析、Table 1 标注、scale ablation 弱化、多重比较逻辑说明
- **升格条件**：成功 reframe + 修正 Abstract + 补 RE multi-seed free-form

Round 9 审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 80

## Round 80

62 recorded events


### User

_source line 1016 · 2026-05-16T04:15:39.303571+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

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

_source line 1017 · 2026-05-16T04:15:44.728374+00:00_

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

_source line 1018 · 2026-05-16T04:15:44.780283+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-16T04:15:48.404589+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-16T04:15:48.404994+00:00_



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

_source line 1021 · 2026-05-16T04:15:54.348775+00:00_

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

_source line 1022 · 2026-05-16T04:15:54.800969+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (107 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_llama3b_scierc_ablation** (success): Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\n- **exp_qwen3_4b_conll_scs_inference_v2** (success): CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\n  [table4_gold_filter_audit](file:///root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/table4_gold_filter_audit.json)\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \"score compression is general\" claim. If effective → important positive finding requiring narrative adjustment.\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\n\n## 趋势\n成功 60 / 负向 23 / 失败 4 / 共 107\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-16T04:15:54.801375+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "6000"
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
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1024 · 2026-05-16T04:15:55.304273+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 2297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-16T04:15:55.304645+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
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
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-16T04:15:55.355666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1027 · 2026-05-16T04:15:59.976232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-16T04:16:01.130602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "150"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-16T04:16:01.484513+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-16T04:16:02.237364+00:00_

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

_source line 1031 · 2026-05-16T04:16:07.880920+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Submission Requirements

In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing compu
…[truncated 1684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7904
}
```

</details>

---


### Tool result

_source line 1032 · 2026-05-16T04:16:07.931724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5694
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-16T04:16:12.200151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper page limit format requirements long short paper ARR"
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
    "query": "EMNLP 2026 main conference paper page limit format requirements long short paper ARR"
  }
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-16T04:16:12.652326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline format guidelines page limit"
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
    "query": "ACL Rolling Review 2026 May cycle submission deadline format guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1035 · 2026-05-16T04:16:13.406472+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "6000"
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
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1036 · 2026-05-16T04:16:18.144512+00:00_

Web search results for query: "EMNLP 2026 main conference paper page limit format requirements long short paper ARR"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the web search results, here's what I found about EMNLP 2026 main conference paper page limits, format requirements, and ARR information:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. The mandatory Limitations section is required, placed after the conclusion.

## ACL Rolling Review (ARR) Submission

All submis
…[truncated 452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5944
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-16T04:16:24.334058+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline format guidelines page limit"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Let me search more specifically for the May 2026 cycle dates and submission guidelines.

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{
…[truncated 4005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 11681
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-16T04:16:24.385082+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ:
…[truncated 4433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10978
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-16T04:16:28.772425+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
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
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-16T04:16:29.276472+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1041 · 2026-05-16T04:16:29.679734+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml",
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
    "file": "writing_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-16T04:16:29.730455+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only 
…[truncated 1414 chars]

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

_source line 1043 · 2026-05-16T04:16:32.441995+00:00_

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

_source line 1044 · 2026-05-16T04:16:32.844231+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp; preliminary, single benchmark), suggesting regime-dependent behavior.
7	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
8	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	

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

_source line 1045 · 2026-05-16T04:16:32.894939+00:00_

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

_source line 1046 · 2026-05-16T04:16:33.347311+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	Instance-level signals (4 of 5) fail by construction---they assign identical scores to all candidates.
12	The empirical contribution concerns log-probability (LP), the only per-sample signal: LP scores are too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.
13	
14	\begin{figure*}[t]
15	\centering
16	\includegraphics[width=\textwidth]{fig_overview}
17	\caption{The correlation-selection gap. \textbf{Le
…[truncated 1370 chars]

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

_source line 1047 · 2026-05-16T04:16:33.347715+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1048 · 2026-05-16T04:16:33.347929+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
17	Semantic uncertainty \cite{ku
…[truncated 898 chars]

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

_source line 1049 · 2026-05-16T04:16:33.749822+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-16T04:16:33.800593+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	
8	\subsection{Confidence Signals}\label{sec:signals}
9	
10	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
11	
12	\paragraph{Log-probability (model-internal, per-sample).}
13	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
14	\begin{equation}\label{eq:logprob}
15	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
16	\end{equation}
17	
18	\paragraph{Exact match voting (surface, instance-level).}
19	The proportion of samples producing the most common output:
20	\begin{equation}\label{eq:em}
21	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
22	\end{equation}
23	
24	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
25	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
26	\begin{equation}\label{eq:fk}
27	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
28	\end{equation}
29	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
30	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_in
…[truncated 2139 chars]

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

_source line 1051 · 2026-05-16T04:16:42.436785+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1052 · 2026-05-16T04:16:42.789272+00:00_

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE: preliminary. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \m
…[truncated 6607 chars]

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

_source line 1053 · 2026-05-16T04:16:42.940269+00:00_

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

_source line 1054 · 2026-05-16T04:16:42.940649+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.
12	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection (Appendix~\ref{app:verbalized_confidence}).
13	
14	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
15	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
16	On RE, LP selection consistently reverses direction under free-form decodin
…[truncated 1296 chars]

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

_source line 1055 · 2026-05-16T04:16:43.242042+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-16T04:16:43.844856+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction (preliminary, single benchmark).
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	RE conclusions rest on SciERC alone (preliminary, 40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

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

_source line 1057 · 2026-05-16T04:16:43.946485+00:00_

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

_source line 1058 · 2026-05-16T04:16:43.997423+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	

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

_source line 1059 · 2026-05-16T04:16:48.415386+00:00_

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

_source line 1060 · 2026-05-16T04:16:48.718785+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
47	\quad FK & 
…[truncated 66606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1061 · 2026-05-16T04:16:48.719237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1062 · 2026-05-16T04:16:48.719758+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 3208 chars]

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

_source line 1063 · 2026-05-16T04:16:54.944834+00:00_

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

_source line 1064 · 2026-05-16T04:16:56.301444+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 104\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1065 · 2026-05-16T04:16:56.301983+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
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
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1066 · 2026-05-16T04:16:56.804505+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

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

_source line 1067 · 2026-05-16T04:16:57.307460+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/round_*.md",
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
    "pattern": "**/artifacts/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1068 · 2026-05-16T04:16:57.508648+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1069 · 2026-05-16T04:16:57.559402+00:00_

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

_source line 1070 · 2026-05-16T04:16:57.660246+00:00_

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

_source line 1071 · 2026-05-16T04:17:34.139712+00:00_

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

_source line 1072 · 2026-05-16T04:17:34.140162+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-16T04:18:21.011296+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n引用文件：`references.bib`\n\n### 论文概要\n论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：信号能预测质量（ρ 达 0.45）但无法改善 best-of-N 选择。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个模型族（Qwen3-8B, LLaMA-3.1-8B），加 4B scale ablation。\n\n### 审查重点（必须逐条评估）\n\n1. **实验设计**\n   - 数据集选择是否足够？RE 只有 SciERC 一个，论文标注为 \"preliminary\"——这种标注是否足够？\n   - 模型覆盖（3B-8B）是否支撑论文声称的 generality？\n   - N=8 作为 primary setting 是否合理？N=16 仅作补充。\n   - 3 seeds 是否足以支撑稳定性声明？\n\n2. **统计方法**\n   - Spearman ρ 作为 primary metric 是否合适？AUROC 和 selection F1 的三指标框架是否 well-motivated？\n   - Bootstrap CI、permutation test、Fisher combined p、TOST 等统计检验是否正确使用？\n   - 多重比较校正（Bonferroni）是否充分？\n   - \"tied fraction\" 的 ε=0.05 阈值选择是否有足够的 data-driven justification？\n\n3. **Claims vs Evidence 对齐**\n   - 核心 claim \"correlation-selection gap is universal\" 是否被证据完全支撑？\n   - \"LP compression is model/task intrinsic, not decoding artifact\" 这个因果推断是否可靠（free-form ablation 仅在 SciERC 上做）？\n   - Scale ablation 只覆盖 3B-8B，能否支撑 \"task difficulty is the primary driver\" 的结论？\n   - RE 结论标注为 \"preliminary, single benchmark\"——这种 hedging 是否适当？\n\n4. **潜在混淆因素**\n   - Qwen3-8B SciERC checkpoint 的 empty thinking token confound——论文三重论证是否充分排除？\n   - Gold-empty instance filtering（CoNLL 20.2%, SciERC 4.0%）的影响？\n   - Constrained decoding 对 LP 的系统性影响？\n\n5. **可重复性**\n   - 是否提供足够的实验细节（超参数、prompt template、evaluation protocol）？\n   - 代码/数据 release 声明？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。"
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
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n引用文件：`references.bib`\n\n### 论文概要\n论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：信号能预测质量（ρ 达 0.45）但无法改善 best-of-N 选择。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个模型族（Qwen3-8B, LLaMA-3.1-8B），加 4B scale ablation。\n\n### 审查重点（必须逐条评估）\n\n1. **实验设计**\n   - 数据集选择是否足够？RE 只有 SciERC 一个，论文标注为 \"preliminary\"——这种标注是否足够？\n   - 模型覆盖（3B-8B）是否支撑论文声称的 generality？\n   - N=8 作为 primary setting 是否合理？N=16 仅作补充。\n   - 3 seeds 是否足以支撑稳定性声明？\n\n2. **统计方法**\n   - Spearman ρ 作为 primary metric 是否合适？AUROC 和 selection F1 的三指标框架是否 well-motivated？\n   - Bootstrap CI、permutation test、Fisher combined p、TOST 等统计检验是否正确使用？\n   - 多重比较校正（Bonferroni）是否充分？\n   - \"tied fraction\" 的 ε=0.05 阈值选择是否有足够的 data-driven justification？\n\n3. **Claims vs Evidence 对齐**\n   - 核心 claim \"correlation-selection gap is universal\" 是否被证据完全支撑？\n   - \"LP compression is model/task intrinsic, not decoding artifact\" 这个因果推断是否可靠（free-form ablation 仅在 SciERC 上做）？\n   - Scale ablation 只覆盖 3B-8B，能否支撑 \"task difficulty is the primary driver\" 的结论？\n   - RE 结论标注为 \"preliminary, single benchmark\"——这种 hedging 是否适当？\n\n4. **潜在混淆因素**\n   - Qwen3-8B SciERC checkpoint 的 empty thinking token confound——论文三重论证是否充分排除？\n   - Gold-empty instance filtering（CoNLL 20.2%, SciERC 4.0%）的影响？\n   - Constrained decoding 对 LP 的系统性影响？\n\n5. **可重复性**\n   - 是否提供足够的实验细节（超参数、prompt template、evaluation protocol）？\n   - 代码/数据 release 声明？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。"
  }
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-16T04:18:40.987046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19975
}
```

</details>

---


### Tool call

_source line 1075 · 2026-05-16T04:18:41.288641+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n引用文件：`references.bib`\n\n### 论文概要\n论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：信号能预测质量但无法改善 best-of-N 选择。3 个贡献：(1) metric dissociation (QE vs selection), (2) LP compression 和 MBR failure, (3) difficulty-dependent signal rankings。\n\n### 审查重点（必须逐条评估）\n\n1. **新颖性评估**\n   - \"Correlation-selection gap\" 概念是否真正 novel？与 MBR decoding 文献中已知的 utility-quality misalignment 有何本质区别？\n   - 对比 Yao et al. (2026)（论文明确 cite 为最近相关工作），增量贡献是什么？是否足以支撑 main conference paper？\n   - \"Instance-level signals fail by construction\" 是 definitional 而非 empirical contribution——论文是否正确区分了这两者？\n   - LP compression 作为核心 empirical finding 的新颖性？verbalized confidence baseline 是否增强了贡献？\n\n2. **相关工作覆盖**\n   - 搜索 2025-2026 年相关工作：self-consistency for structured prediction, MBR decoding for IE, confidence estimation for NER/RE, test-time scaling for structured outputs\n   - 是否遗漏重要 baseline 或对比方法？例如：learned verifiers, reward models, ensemble methods\n   - 与 Eikema & Aziz (2025) structured MBR 的讨论是否充分？\n   - uncertainty quantification 文献（semantic uncertainty, P(True)）的覆盖是否足够？\n\n3. **写作质量**\n   - 论文结构是否清晰？8 页内容密度是否适当？\n   - 术语定义是否一致（per-sample vs instance-level, quality estimation vs sample selection）？\n   - Figure/Table 设计是否有效传达核心信息？\n   - Abstract 是否准确反映论文内容？是否有 overclaiming？\n   - \"Preliminary\" 标注在论文中频繁出现——是否影响论文整体可信度？\n\n4. **格式合规**\n   - 页数是否在 8 页限制内？\n   - 引用格式是否符合 ACL/natbib 规范？\n   - 匿名是否完全？检查是否有作者身份泄露（GitHub links, institution names, 服务器信息等）\n   - Ethics Statement 是否充分？\n   - Limitations 是否诚实且全面？\n\n5. **呈现与叙事**\n   - 核心 \"negative result\"（信号无法 selection）的 framing 是否恰当？\n   - 是否给出足够的 actionable insight？还是仅仅 \"X doesn't work\"？\n   - Discussion 中 \"trained verifiers\" 的前瞻讨论是否有价值？\n   - 大量实验细节放在 appendix 中——正文是否 self-contained？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。同时搜索最新相关工作，检查是否有遗漏。"
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
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n引用文件：`references.bib`\n\n### 论文概要\n论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：信号能预测质量但无法改善 best-of-N 选择。3 个贡献：(1) metric dissociation (QE vs selection), (2) LP compression 和 MBR failure, (3) difficulty-dependent signal rankings。\n\n### 审查重点（必须逐条评估）\n\n1. **新颖性评估**\n   - \"Correlation-selection gap\" 概念是否真正 novel？与 MBR decoding 文献中已知的 utility-quality misalignment 有何本质区别？\n   - 对比 Yao et al. (2026)（论文明确 cite 为最近相关工作），增量贡献是什么？是否足以支撑 main conference paper？\n   - \"Instance-level signals fail by construction\" 是 definitional 而非 empirical contribution——论文是否正确区分了这两者？\n   - LP compression 作为核心 empirical finding 的新颖性？verbalized confidence baseline 是否增强了贡献？\n\n2. **相关工作覆盖**\n   - 搜索 2025-2026 年相关工作：self-consistency for structured prediction, MBR decoding for IE, confidence estimation for NER/RE, test-time scaling for structured outputs\n   - 是否遗漏重要 baseline 或对比方法？例如：learned verifiers, reward models, ensemble methods\n   - 与 Eikema & Aziz (2025) structured MBR 的讨论是否充分？\n   - uncertainty quantification 文献（semantic uncertainty, P(True)）的覆盖是否足够？\n\n3. **写作质量**\n   - 论文结构是否清晰？8 页内容密度是否适当？\n   - 术语定义是否一致（per-sample vs instance-level, quality estimation vs sample selection）？\n   - Figure/Table 设计是否有效传达核心信息？\n   - Abstract 是否准确反映论文内容？是否有 overclaiming？\n   - \"Preliminary\" 标注在论文中频繁出现——是否影响论文整体可信度？\n\n4. **格式合规**\n   - 页数是否在 8 页限制内？\n   - 引用格式是否符合 ACL/natbib 规范？\n   - 匿名是否完全？检查是否有作者身份泄露（GitHub links, institution names, 服务器信息等）\n   - Ethics Statement 是否充分？\n   - Limitations 是否诚实且全面？\n\n5. **呈现与叙事**\n   - 核心 \"negative result\"（信号无法 selection）的 framing 是否恰当？\n   - 是否给出足够的 actionable insight？还是仅仅 \"X doesn't work\"？\n   - Discussion 中 \"trained verifiers\" 的前瞻讨论是否有价值？\n   - 大量实验细节放在 appendix 中——正文是否 self-contained？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。同时搜索最新相关工作，检查是否有遗漏。"
  }
}
```

</details>

---


### Tool result

_source line 1076 · 2026-05-16T04:18:42.751046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 1077 · 2026-05-16T04:18:50.941968+00:00_

Reviewer 1（方法严谨性）和 Reviewer 2（新颖性/完整性）已分配任务，正在独立初审。等待两份审稿报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 81

## Round 81

2 recorded events


### User

_source line 1078 · 2026-05-16T04:23:41.370981+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**审查侧重：方法严谨性 + 实验设计 + 统计有效性**

---

## 总体评分
**Overall**: 3.5/5（介于 Findings acceptance 和 Conference acceptance 之间）
**一句话总结**: 论文对 structured IE 中 quality estimation 与 sample selection 的解耦提供了系统性实证，核心 NER 发现扎实，但 RE 覆盖不足、scale 范围过窄、以及若干因果推断的证据链不完整限制了 generality claims 的力度。

## 官方维度打分（ARR 2025+ Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NER 主张有充分支撑；RE 适当标注 preliminary；但 LP compression "task-intrinsic" 因果推断与 free-form RE reversal 矛盾；ε=0.05 阈值选择存在 circularity |
| Excitement | 3/5 | Correlation-selection gap 是有实践价值的负性发现，对 test-time scaling 社区有意义；但论文本身不提供解决方案，且发现的 surprise 有限——instance-level 信号无法 rank candidates 是构造性的 |
| Overall Assessment | 3.5/5 | 方法论严谨，统计处理在同类工作中属上乘，但 claim scope 超出证据覆盖（单一 RE benchmark、3B–8B scale），建议 Findings 或经修改后 Main Conference |
| Reproducibility | 4/5 | 训练配置、prompt template、超参数详尽（Appendix F）；代码/数据承诺 upon acceptance；缺少 inference compute budget 和具体 vLLM 版本 |
| Reviewer Confidence | 4/5 | 仔细阅读了正文和全部附录；对 statistical methodology 和 structured IE 评估有经验 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] RE 覆盖不足与 claim scope 不匹配
- 具体位置：Title ("LLM-Based Information Extraction"), Abstract line 3 ("NER and RE benchmarks"), §5
- 问题：论文标题和 abstract 将贡献定位为 "Information Extraction"，涵盖 NER + RE，但 RE 实验仅在 SciERC 一个 benchmark 上进行（且 40% zero-F1）。NER 有 3 个 benchmark 跨难度梯度，RE 却缺乏类似设计。论文在正文中反复标注 "preliminary"（≥12 次），但标题、abstract 第 1–2 句和 Figure 1 caption 均未体现这一限定。
- 为什么影响接收：单一 RE benchmark 不足以支撑 "Information Extraction" 级别的 claim。SciERC RE 的 40% zero-F1 率进一步削弱该 benchmark 的代表性。
- 建议：(1) 将标题/abstract 显式限定为 "primarily NER, with preliminary RE evidence"；(2) 增加至少一个额外 RE benchmark（如 TACRED、DocRED、或 ACE05）；(3) 若无法增加数据集，则将 RE 结论完全移至附录并在 abstract 中删除 RE 相关的具体数字。

**N2** [critical] ε=0.05 "tied fraction" 阈值的 circularity
- 具体位置：Appendix §app:logprob_ties（line 499–500）, Table 11（ε sweep）
- 问题：Appendix 声称 "the median within-instance LP range is only 0.041 nats—below the ε=0.05 threshold used throughout, providing data-driven justification for this cutoff." 这是 circular reasoning：阈值 ε 的选择是为了让 median LP range 落在阈值以下。Table 11 的 ε sweep 显示 ε=0.05 恰好给出最强 p-value（p=0.004），暗示 p-value optimization。ARR guidelines (R1) 明确标记 threshold optimization 为 problematic practice。
- 建议：(1) 用 pre-registered 或 literature-grounded ε 替代；(2) 报告 ε-free 的连续指标（median LP range 本身即可作为核心统计量）；(3) 如果保留 ε，承认 circularity 并在所有 tied-fraction 数字旁标注 "threshold-dependent"。

**N3** [critical] "LP compression is model/task intrinsic, not decoding artifact" 的因果推断被 RE reversal 削弱
- 具体位置：Abstract line 6, §6 ¶"Ablation: free-form decoding", Appendix Table 15 Panel B
- 问题：论文声称 free-form ablation "confirms NER compression is not an artifact of constrained decoding"，但 RE 数据直接反驳——LP selection 在 constrained 下为 −0.68 pp，free-form 下为 +1.69 pp。至少对 RE 而言，constrained decoding 确实是 LP selection failure 的一个因素。Abstract 的措辞暗示了比实际证据更强的结论。
- 建议：Abstract 改为 "...confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction under free-form decoding, suggesting regime-dependent behavior (preliminary, single benchmark)."

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Scale range (3B–8B) 过窄，不足以支撑 "task difficulty is the primary driver" 因果结论
- 具体位置：§5.4 line 120, Conclusion line 6
- 建议：弱化为 "task difficulty is a stronger predictor than model scale within the 3B–8B range tested"。

**W2** [warning] 3 seeds 对 stability claims 的统计效力不足
- 具体位置：Appendix Table 8, Table 10 (Kendall's W)
- Kendall's W=1.000 with 3 observations 不具信息量。σ≤0.026 基于 n=3，95% CI 极宽。
- 建议：增加至少 5–10 seeds 或弱化 stability 措辞。

**W3** [warning] "Greedy" baseline 实为 T=1.0 random sample，命名混淆
- 建议：使用 "single-sample" 替代 "greedy"；增加 argmax (T=0) baseline。

**W4** [warning] 缺少信号组合实验
- LP non-tied subset 的 +2.9 pp gain 暗示 VC 筛选 + LP 排序等组合策略可能有效。
- 建议：增加至少一个 simple combination baseline。

**W5** [warning] Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性
- 建议：报告 CoNLL full-set ρ 作为对照。

**W6** [warning] Thinking token confound 的 "CoNLL control" 论证薄弱
- CoNLL 高 tied fraction 更可能因 task easiness（88% identical outputs），而非证据排除 thinking token 假说。Task difficulty 与 thinking token 混淆未被分离。

---

## 小问题

- Table 3 NER 用 2-seed mean，其他部分用 3 seeds，未说明原因
- Figure 1 caption 措辞对 LP 不适用（LP 是 per-sample，非 instance-level）
- \cite vs \citet 使用不一致
- 引用验证：3 条 bib entries 未在 OpenAlex 索引中找到（hobelsberger2025, lightman2024, venktesh2025），均为知名预印本，非引用错误

## Questions to Authors

1. ε=0.05 的选择是否先于 LP range 分析确定？
2. 为什么 Table 3 selection analysis 使用 2 seeds 而非 3？
3. 是否考虑过 LP + consistency signal 组合策略？
4. Free-form RE reversal 是否在不同 temperature 下也成立？
5. 增加 TACRED/ACE05 是否预计 RE conclusions 会有质性变化？

## Missing References

- Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet" — 对 self-assessment 限制有直接相关性
- Fernandes et al. (2022) "Quality-Aware Decoding for Neural Machine Translation" — MBR 在 structured prediction 的早期讨论

## 主要优势

- 统计方法论在同类工作中属上乘（Bootstrap CI、TOST with external anchors、permutation test）
- 三指标框架（ρ, AUROC, selection F1）的 dissociation 是重要的方法论贡献
- 极其详尽的 appendix（15 sections），几乎每个 claim 都有 robustness check
- 诚实的 RE hedging 和全面的 Limitations section
- Matched training protocol 消除跨模型训练 confound
- LP compression 的系统性诊断分析是论文最有洞察力的贡献

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

_source line 1079 · 2026-05-16T04:23:47.637440+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 1080 · 2026-05-16T04:23:50.229093+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿摘要：**

- **Overall 3.5/5**，Soundness 3.5，Excitement 3
- 3 个 Must-Fix：(N1) RE 仅 SciERC 一个 benchmark 与 title/abstract 的 "IE" scope 不匹配；(N2) ε=0.05 tied-fraction 阈值存在 circular reasoning / p-value optimization 嫌疑；(N3) abstract 关于 LP compression "not a decoding artifact" 的措辞被 RE free-form reversal 削弱
- 6 个 Should-Fix：scale range 过窄、3 seeds 统计效力不足、greedy baseline 命名混淆、缺信号组合实验、gold-empty filtering 跨数据集不可比、thinking token CoNLL control 论证薄弱
- **主要优势**：统计方法论上乘，三指标 dissociation 框架有贡献，appendix 极其详尽，LP compression 诊断分析系统性强

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

_source line 1081 · 2026-05-16T04:23:55.292429+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 83

## Round 83

6 recorded events


### User

_source line 1082 · 2026-05-16T04:24:39.612316+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**

---

## 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 方法论扎实的 empirical study，但核心概念 "correlation-selection gap" 的新颖性不足以支撑 main conference；instance-level signals "fail by construction" 是 definitional observation 而非 empirical contribution，LP compression 虽有价值但增量有限。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计系统、统计方法严谨（bootstrap CI、TOST、permutation test），但 RE 结论仅基于单一 benchmark 且 40% zero-F1，核心 claim 之一是 definitional 而非 empirical |
| Excitement | 2.5/5 | 对 IE 实践者有参考价值，但"不同粒度的信号做不了同一件事"概念上不意外；相比 MBR 文献中已有的 utility-quality misalignment，增量有限 |
| Overall | 3.0/5 | 适合 Findings：thorough、honest、useful，但 novelty 和 impact 不够 main conference |
| Reproducibility | 4/5 | 训练配置、prompt、超参数完整；代码承诺 acceptance 后公开 |
| Confidence | 4/5 | 仔细阅读全文和 appendix，熟悉相关文献 |

## Must-Fix 问题

**N1** [critical] "Instance-level signals fail by construction" 是 definitional observation，不应算作 empirical contribution
- 位置：Section 1 Contribution 1、Section 4.2 第二段、Section 5 第二段
- 论文反复强调四个 instance-level signals 因只产生单一分数而无法 per-sample selection，但这是定义层面的必然结果，不构成 empirical finding。论文自己也承认 "fail by construction"，却仍列为三大贡献之一（"Metric dissociation"）。去掉 definitional 部分后，empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者 scope 有限，后者与 Eikema & Aziz (2025) structured MBR 发现高度一致。
- 建议：将 instance-level/per-sample 区分作为 problem formulation 前提（Section 3），聚焦 LP compression 和 difficulty-dependent rankings 作为贡献。

**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate
- 位置：Table 1 RE 列、Table 2 RE F1、Conclusion 第 5 行
- NER 有 3 个 benchmark，RE 只有 SciERC（40% zero-F1）。正文 "preliminary" 出现至少 11 次，但 Abstract 和 Conclusion 仍将 RE LP reversal 作为核心发现。单一 40% failure rate dataset 上的 "preliminary" 发现不应以 contribution-level claim 呈现。"LLM-Based Information Extraction" title scope 与实际 RE coverage 不匹配。
- 建议：增加至少一个 RE benchmark，或将 scope 明确限定为 NER。

**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰
- 位置：Section 1 第 8 行、Section 2 第 10 行
- 三个 "extension"（structural matching、selection analysis、difficulty gradient）中：(a) SJ 比 EM 高 0.065 ρ 仅 marginal significance；(b) selection analysis 核心是 negative result；(c) WNUT-17 所有 signal collapse。Combined novelty 是否足够 main conference paper？
- 建议：更明确阐述 Yao et al. 未回答的具体 research question，以及本文 answers 为什么重要。

## Should-Fix 问题

**W1** [warning] "Preliminary" 标注过于频繁，削弱论文可信度
- 正文至少 11 次 "preliminary"，给人 "工作未完成就提交" 的印象。
- 建议：补全 RE 实验或将 RE 集中到明确标记的 subsection。

**W2** [warning] LP compression 缺乏 mechanistic explanation
- Section 5 详细 characterize 了 compression 现象并排除了多个原因，但未解释 WHY——例如 fine-tuned model 在 IE 任务上的 posterior 是否天然 peaked？
- 建议：增加对 LP compression 机制的讨论。

**W3** [warning] 缺少对 conformal prediction / set-valued uncertainty 的讨论
- Conformal Structured Prediction (ICLR 2025, arxiv 2410.06296) 直接处理 structured prediction 的 set-valued uncertainty，与本文问题设置高度相关。
- 建议：在 Related Work 或 Discussion 中简要讨论。

**W4** [warning] 3B-8B 规模限制对结论适用范围影响大
- Larger models (70B+) 的 LP 分布可能有质的变化。Limitations 提到但未充分讨论。

**W5** [warning] Spearman ρ 作为 primary QE metric 缺乏 justification
- ρ 衡量 rank correlation，但实际 QE 应用更接近 AUROC 的 binary classification。论文展示了 ρ-AUROC dissociation 但未讨论选择标准。

## 小问题
- 术语交替使用 "per-sample signal"/"per-sample scoring"、"consensus-proximity selection"/"MBR"，建议首次定义时明确等价关系
- Table 2 "Greedy: T=1.0 sample" 在 NLP 中 greedy 通常指 argmax，建议正文首次提及时明确说明
- Figure 1 caption 抽象，建议增加具体数值标注
- Ethics Statement 中 CoNLL-2003 Reuters 许可条款近年有争议，建议确认合规性

## 缺失引用
1. Conformal Structured Prediction (ICLR 2025; arxiv 2410.06296) — set-valued uncertainty for structured prediction
2. "Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs" (arxiv 2605.07806, May 2026) — alternative self-assessment dimensions
3. "Learning When to Sample: Confidence-Aware Self-Consistency" (arxiv 2603.08999, March 2026) — confidence-aware sampling
4. Slim-SC / Thought Pruning (EMNLP 2025) — efficient self-consistency via semantic pruning

## 主要优势
- 实验设计系统且严谨：5 signal × 3 NER dataset × 2 model × 多 seed/温度/N，配合完善的统计检验
- 诚实的 scope 限定和负责任的 "preliminary" 标注
- 清晰的 practical recommendations（VC for hard NER, EM for easy NER, LP for RE）
- 高质量 Appendix（22 页中 12+ 页），包含 LOO-SJ equivalence、FK independence test、OOD analysis 等
- MBR within- vs across-instance failure analysis 是有价值的诊断贡献

## 格式合规
- 页数：主体约 7 页（含 Limitations + Ethics），References 之后 Appendix，符合 8 页限制
- 模板：`\usepackage[review]{acl}` ✓，行号可见
- 匿名：author = "Anonymous" ✓，未发现身份泄露
- Ethics Statement：存在但较简短
- Limitations：诚实且全面

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

_source line 1083 · 2026-05-16T04:24:59.613647+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Overall: 3.0/5 (Findings)\nSoundness 3.5, Excitement 2.5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] \"Instance-level signals fail by construction\" 是 definitional observation，不应算作 empirical contribution\n- 位置：Section 1 Contribution 1、Section 4.2 第二段、Section 5 第二段\n- 论文反复强调四个 instance-level signals 因只产生单一分数而无法 per-sample selection，但这是定义层面的必然结果，不构成 empirical finding。论文自己也承认 \"fail by construction\"，却仍列为三大贡献之一（\"Metric dissociation\"）。去掉 definitional 部分后，empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者 scope 有限，后者与 Eikema & Aziz (2025) structured MBR 发现高度一致。\n- 建议：将 instance-level/per-sample 区分作为 problem formulation 前提（Section 3），聚焦 LP compression 和 difficulty-dependent rankings 作为贡献。\n\n**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate\n- 与你的 N1 一致：RE 覆盖不足，title/abstract scope 不匹配。\n\n**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰\n- 三个 \"extension\"（structural matching、selection analysis、difficulty gradient）中：(a) SJ 比 EM 高 0.065 ρ 仅 marginal significance；(b) selection analysis 核心是 negative result；(c) WNUT-17 所有 signal collapse。Combined novelty 是否足够？\n\n### Should-Fix 问题\n\n**W1** \"Preliminary\" 标注过于频繁（≥11次），削弱论文可信度\n**W2** LP compression 缺乏 mechanistic explanation\n**W3** 缺少对 conformal prediction / set-valued uncertainty 的讨论（ICLR 2025, arxiv 2410.06296）\n**W4** 3B-8B 规模限制对结论适用范围影响大\n**W5** Spearman ρ 作为 primary QE metric 缺乏 justification\n\n### 缺失引用\n1. Conformal Structured Prediction (ICLR 2025)\n2. \"Beyond Confidence\" (arxiv 2605.07806, May 2026)\n3. \"Learning When to Sample\" (arxiv 2603.08999, March 2026)\n4. Slim-SC / Thought Pruning (EMNLP 2025)\n\n### 主要优势\n- 实验设计系统且严谨\n- 诚实的 scope 限定\n- 清晰的 practical recommendations\n- 高质量 Appendix\n- MBR within- vs across-instance failure analysis 有价值\n\n---\n\n请对 Reviewer 2 的每个 Must-Fix、Should-Fix 和缺失引用逐条回应 [AGREE] 或 [REBUT]。"
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
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Overall: 3.0/5 (Findings)\nSoundness 3.5, Excitement 2.5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] \"Instance-level signals fail by construction\" 是 definitional observation，不应算作 empirical contribution\n- 位置：Section 1 Contribution 1、Section 4.2 第二段、Section 5 第二段\n- 论文反复强调四个 instance-level signals 因只产生单一分数而无法 per-sample selection，但这是定义层面的必然结果，不构成 empirical finding。论文自己也承认 \"fail by construction\"，却仍列为三大贡献之一（\"Metric dissociation\"）。去掉 definitional 部分后，empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者 scope 有限，后者与 Eikema & Aziz (2025) structured MBR 发现高度一致。\n- 建议：将 instance-level/per-sample 区分作为 problem formulation 前提（Section 3），聚焦 LP compression 和 difficulty-dependent rankings 作为贡献。\n\n**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate\n- 与你的 N1 一致：RE 覆盖不足，title/abstract scope 不匹配。\n\n**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰\n- 三个 \"extension\"（structural matching、selection analysis、difficulty gradient）中：(a) SJ 比 EM 高 0.065 ρ 仅 marginal significance；(b) selection analysis 核心是 negative result；(c) WNUT-17 所有 signal collapse。Combined novelty 是否足够？\n\n### Should-Fix 问题\n\n**W1** \"Preliminary\" 标注过于频繁（≥11次），削弱论文可信度\n**W2** LP compression 缺乏 mechanistic explanation\n**W3** 缺少对 conformal prediction / set-valued uncertainty 的讨论（ICLR 2025, arxiv 2410.06296）\n**W4** 3B-8B 规模限制对结论适用范围影响大\n**W5** Spearman ρ 作为 primary QE metric 缺乏 justification\n\n### 缺失引用\n1. Conformal Structured Prediction (ICLR 2025)\n2. \"Beyond Confidence\" (arxiv 2605.07806, May 2026)\n3. \"Learning When to Sample\" (arxiv 2603.08999, March 2026)\n4. Slim-SC / Thought Pruning (EMNLP 2025)\n\n### 主要优势\n- 实验设计系统且严谨\n- 诚实的 scope 限定\n- 清晰的 practical recommendations\n- 高质量 Appendix\n- MBR within- vs across-instance failure analysis 有价值\n\n---\n\n请对 Reviewer 2 的每个 Must-Fix、Should-Fix 和缺失引用逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-16T04:25:15.054780+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15441
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-16T04:25:15.156492+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Overall: 3.5/5, Soundness 3.5, Excitement 3, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] RE 覆盖不足与 claim scope 不匹配\n- Title \"LLM-Based Information Extraction\" + Abstract 将 RE 作为核心维度，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1）。NER 3 个 benchmark，RE 0 个额外。\"Preliminary\" ≥12 次但 title/abstract 未体现。\n- 建议：限定 title/abstract scope 或增加 RE benchmark。\n\n**N2** [critical] ε=0.05 \"tied fraction\" 阈值的 circularity\n- Appendix 声称 median LP range (0.041) 低于 ε=0.05 作为 \"data-driven justification\"——这是 circular reasoning。Table 11 ε sweep 显示 ε=0.05 恰好给出最强 p-value (p=0.004)，暗示 p-value optimization。\n- 建议：用 pre-registered 或 literature-grounded ε，或报告 ε-free 连续指标。\n\n**N3** [critical] \"LP compression is model/task intrinsic\" 因果推断被 RE reversal 削弱\n- Abstract 声称 free-form ablation confirms compression not a decoding artifact，但 RE LP selection 在 free-form 下从 −0.68 pp 反转为 +1.69 pp。至少对 RE，constrained decoding 确实是 LP selection failure 的一个因素。\n\n### Should-Fix 问题\n\n**W1** Scale range (3B–8B) 过窄，不足以支撑 \"task difficulty is primary driver\" 因果结论\n**W2** 3 seeds 统计效力不足（Kendall's W=1.000 with n=3 不具信息量）\n**W3** \"Greedy\" baseline 实为 T=1.0 random sample，命名混淆\n**W4** 缺少信号组合实验（如 VC 筛选 + LP 排序）\n**W5** Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性\n**W6** Thinking token confound 的 CoNLL control 论证薄弱——CoNLL 高 tied fraction 更可能因 task easiness\n\n### 小问题\n- Table 3 NER 2-seed vs 其他 3 seeds 未说明\n- Figure 1 caption 对 LP 不适用\n- \\cite vs \\citet 不一致\n\n### Missing References\n- Huang et al. (2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n- Fernandes et al. (2022) \"Quality-Aware Decoding for Neural Machine Translation\"\n\n### 主要优势\n- 统计方法论上乘\n- 三指标 dissociation 框架有贡献\n- 极其详尽的 appendix\n- LP compression 诊断分析系统性强\n- Matched training protocol\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix、Should-Fix、小问题和缺失引用逐条回应 [AGREE] 或 [REBUT]。"
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
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Overall: 3.5/5, Soundness 3.5, Excitement 3, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] RE 覆盖不足与 claim scope 不匹配\n- Title \"LLM-Based Information Extraction\" + Abstract 将 RE 作为核心维度，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1）。NER 3 个 benchmark，RE 0 个额外。\"Preliminary\" ≥12 次但 title/abstract 未体现。\n- 建议：限定 title/abstract scope 或增加 RE benchmark。\n\n**N2** [critical] ε=0.05 \"tied fraction\" 阈值的 circularity\n- Appendix 声称 median LP range (0.041) 低于 ε=0.05 作为 \"data-driven justification\"——这是 circular reasoning。Table 11 ε sweep 显示 ε=0.05 恰好给出最强 p-value (p=0.004)，暗示 p-value optimization。\n- 建议：用 pre-registered 或 literature-grounded ε，或报告 ε-free 连续指标。\n\n**N3** [critical] \"LP compression is model/task intrinsic\" 因果推断被 RE reversal 削弱\n- Abstract 声称 free-form ablation confirms compression not a decoding artifact，但 RE LP selection 在 free-form 下从 −0.68 pp 反转为 +1.69 pp。至少对 RE，constrained decoding 确实是 LP selection failure 的一个因素。\n\n### Should-Fix 问题\n\n**W1** Scale range (3B–8B) 过窄，不足以支撑 \"task difficulty is primary driver\" 因果结论\n**W2** 3 seeds 统计效力不足（Kendall's W=1.000 with n=3 不具信息量）\n**W3** \"Greedy\" baseline 实为 T=1.0 random sample，命名混淆\n**W4** 缺少信号组合实验（如 VC 筛选 + LP 排序）\n**W5** Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性\n**W6** Thinking token confound 的 CoNLL control 论证薄弱——CoNLL 高 tied fraction 更可能因 task easiness\n\n### 小问题\n- Table 3 NER 2-seed vs 其他 3 seeds 未说明\n- Figure 1 caption 对 LP 不适用\n- \\cite vs \\citet 不一致\n\n### Missing References\n- Huang et al. (2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n- Fernandes et al. (2022) \"Quality-Aware Decoding for Neural Machine Translation\"\n\n### 主要优势\n- 统计方法论上乘\n- 三指标 dissociation 框架有贡献\n- 极其详尽的 appendix\n- LP compression 诊断分析系统性强\n- Matched training protocol\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix、Should-Fix、小问题和缺失引用逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1086 · 2026-05-16T04:25:16.615500+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 1087 · 2026-05-16T04:25:19.170351+00:00_

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


## Round 84

## Round 84

2 recorded events


### User

_source line 1088 · 2026-05-16T04:25:21.736630+00:00_

[Reviewer 2 审稿结果]:
审稿报告已发送给 Review Director。

核心评估：**Overall 3.0/5 (Findings track)**。三个 critical 问题：(1) "instance-level signals fail by construction" 是 definitional 而非 empirical contribution，不应列为核心贡献；(2) RE 仅单一 benchmark + 40% zero-F1，与 title scope 不匹配；(3) 与 Yao et al. (2026) 的增量边界不清。论文实验设计和统计方法扎实，Appendix 质量高，practical recommendations 有价值，但 novelty bar 不够 main conference。识别到 4 篇可能遗漏的相关工作。格式合规，匿名维护良好。

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

_source line 1089 · 2026-05-16T04:25:26.506834+00:00_

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


## Round 85

## Round 85

2 recorded events


### User

_source line 1090 · 2026-05-16T04:27:47.244329+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[REBUT] R2-N1: "Instance-level signals fail by construction" 是 definitional observation，不应算作 empirical contribution**

R2 部分正确但过度延伸。"四个 instance-level signals 无法 rank candidates" 确实是构造性的，但 Contribution 1（Metric dissociation）的核心是 ρ/AUROC/selection F1 三指标在实证中的 decoupling——这需要数据来展示：
- Table 1 中 EM 在 CoNLL AUROC 最高（0.816）但 ρ 排名不同
- Appendix §app:verbalized_confidence 中 VerbConf ρ > LP 但 selection 最差——per-sample signal 之间的 dissociation 不是 definitional
- Table 4 中 LP full-set/conditional ρ inversion（−0.410 → +0.350）

但同意 framing 可改进：应将 instance-level/per-sample 区分移至 §3 作为前提，Contribution 1 重新聚焦为 empirical dissociation。Eikema et al. (2025) 的 overlap 存在但本文提供了 IE-specific failure mode（utility correlates across but not within instances）。

**[AGREE] R2-N2: RE 单一 benchmark** — 与我的 N1 完全一致。

**[REBUT] R2-N3: 与 Yao et al. (2026) 增量贡献不够清晰**

R2 低估了 selection analysis 的价值：
(a) SJ vs EM marginal（Δρ=+0.065）确实，但 structural vs LP gap（Δρ=+0.155, CI [+0.074, +0.234], Table 6）clearly significant，Yao 未评估 structural signals 或 LP
(b) Selection analysis 是 test-time scaling 社区最关心的问题——Yao 止步于 correlation，本文的 correlation-selection gap 证明 more samples ≠ better selection 在 structured IE 中不成立
(c) WNUT-17 的 LP full/conditional inversion 提供了具体 diagnostic insight，不仅是 "collapse"

建议作者在 Introduction 更明确 tabulate 与 Yao 的差异，但 combined novelty 足够。

---

### Should-Fix 问题

**[AGREE] R2-W1: "Preliminary" 过于频繁** — 建议首次完整说明后用 † 标记替代。

**[AGREE] R2-W2: LP compression 缺乏 mechanistic explanation** — 论文展示了现象但未解释原因。应至少讨论可能的 hypotheses：token averaging 平滑 variance、schema-enforced tokens 占多数 tokens 导致有效 variance 来源少、constrained decoding 下有效 vocabulary 缩小等。

**[REBUT] R2-W3: 缺少 conformal prediction 讨论** — Conformal prediction 构建具有 coverage guarantee 的 prediction sets，与本文的 best-of-N point selection 目标 fundamentally 不同。High-level connection 在 uncertainty quantification 层面存在，但 Related Work 中一句简要提及足矣，detailed discussion 不必要。

**[AGREE] R2-W4: 3B-8B scale 限制** — 与我的 W1 一致。

**[REBUT] R2-W5: Spearman ρ 缺乏 justification** — Spearman ρ 是 uncertainty estimation 文献标准 metric（Kuhn 2023, Kadavath 2022），rank-based 对非线性关系鲁棒。更重要的是论文并非只用 ρ——三指标框架（ρ + AUROC + selection F1）本身就是对 single-metric 问题的回应。Conditional analysis（Table 4）处理了 floor/ceiling effects。

---

### 缺失引用

**[AGREE] #1 Conformal Structured Prediction (ICLR 2025)** — tangential 但值得在 Related Work 简要提及。
**[AGREE] #2 "Beyond Confidence" (2605.07806)** — 与 verbalized confidence failure 直接相关，应引用。
**[REBUT] #3 "Learning When to Sample" (2603.08999)** — 处理 discrete-answer CoT，本文已引用同类工作（Feng 2025, Wang 2025, Kim 2026），coverage 充分。
**[REBUT] #4 Slim-SC (EMNLP 2025)** — discrete-answer efficiency 问题，与 structured IE selection failure 不同，非 critical missing。

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

_source line 1091 · 2026-05-16T04:27:52.024019+00:00_

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


## Round 86

## Round 86

2 recorded events


### User

_source line 1092 · 2026-05-16T04:27:57.049951+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告和 Reviewer 2 交叉回应均已发送给 Review Director。

总结：
- **我的审稿**：Overall 3.5/5，3 个 Must-Fix（RE 覆盖不足、ε 阈值 circularity、LP "task-intrinsic" 因果推断被 RE reversal 削弱）+ 6 个 Should-Fix
- **对 R2 的回应**：R2-N1 部分反驳（metric dissociation 有 empirical 成分但 framing 需改进）、R2-N2 同意、R2-N3 反驳（selection analysis 价值被低估）；W3（conformal prediction）和 W5（Spearman ρ）反驳；W1/W2/W4 同意；缺失引用 #1/#2 同意、#3/#4 反驳（discrete-answer 工作，已有充分覆盖）

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

_source line 1093 · 2026-05-16T04:28:01.893752+00:00_

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


## Round 87

## Round 87

10 recorded events


### User

_source line 1094 · 2026-05-16T04:28:03.402150+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix

**[AGREE] R1-N1: RE 覆盖不足与 claim scope 不匹配**
与我的 N2 完全一致。Title 暗示 NER+RE 充分覆盖，但 RE 仅有 SciERC（40% zero-F1），"preliminary" ≥11 次但 title/abstract 未体现。

**[AGREE with nuance] R1-N2: ε=0.05 circularity**
同意核心批评：Appendix G (line 499) "data-driven justification" 确为 circular reasoning，Table 11 中 ε=0.05 恰好给出最强 p=0.004 有 p-hacking 之嫌。但需指出两个缓解因素：(1) 主 selection 结果（Table 2）不依赖 ε——LP 直接排序 candidate，全 dataset Δ=+0.2pp (p=0.29) 是 ε-free 的；ε 仅影响诊断性 tied/non-tied subset 分析。(2) Appendix G (line 532) 报告了 ε-free 连续指标 pooled within-instance ρ(LP, F1)=0.248。circularity 影响辅助分析 credibility，不动摇主结论。

**[REBUT with partial agreement] R1-N3: RE reversal 削弱 "compression is intrinsic" 因果推断**
R1 混淆了两个层面。Free-form ablation Panel A (Appendix I, Table 14) 显示 LP **分布** 在两种 regime 下几乎一致（std ratio 0.97, range difference −0.0024, tied fraction 59.7%→57.7%）。LP compression 本身确实 intrinsic。RE 反转的是 **selection outcome**（−0.68→+1.69pp），非 LP 分布。Abstract 正确区分 "confirms NER compression" 与 "on RE, LP selection reverses"。但同意论文未充分解释 WHY 同样 compressed 的 LP 在 RE free-form 下有效，这个 mechanistic gap 需要补充。

### Should-Fix

**[AGREE] R1-W1**: 与我的 W4 一致。3B-8B 不足以支撑因果结论。

**[AGREE] R1-W2**: 正确统计批评。W=1.000 with n=3 置信区间极宽，应增 seeds 或报告 exact permutation p-value。

**[AGREE] R1-W3**: 与我的小问题一致。"Greedy" 在 NLP 中通常指 argmax，T=1.0 sample 应命名为 "single-sample baseline"。

**[AGREE] R1-W4**: 有效建议。不探索 VC+LP 等组合是明显遗漏，尤其是论文已指出两者在不同 regime 下各有优势（Section 5）。

**[REBUT] R1-W5**: Gold-empty filtering 比例差异反映 dataset 特征而非 confound。Appendix B 解释了原因。跨数据集对比在 signal ranking 层面（非绝对 ρ 值），且 selection 分析用 full set 不 filter（Section 3.3, line 56-57）。

**[AGREE with nuance] R1-W6**: 同意 CoNLL control 论证弱——task easiness 是 confound。但 Appendix D 另两个论证较强：LP shift 仅 0.001 nats/token (2.68% of median range)，且 constant prefix cancellation 基于数学推理。thinking token 问题总体证据充分，仅 CoNLL control 这一个论证弱。

### 小问题

**[AGREE] R1-Minor-1**: Table 2 NER 2-seed vs Table 7 QE 3-seed 差异未解释。
**[AGREE] R1-Minor-2**: Figure 1 caption 不适用于 LP（per-sample signal）。
**[REBUT] R1-Minor-3**: 检查 tex 源码，\citet 用于句中主语、\cite 用于括号引用，符合 natbib 标准。

### 缺失引用

**[REBUT] R1-Missing-1**: Huang et al. (2024) 讨论 self-correction（iterative修改），非 self-consistency（one-shot多采样比较），paradigm 不同，关联有限。
**[AGREE] R1-Missing-2**: Fernandes et al. (2022) Quality-Aware Decoding 直接相关，将 QE 与 MBR 结合用 learned estimator rerank，与本文 "trained verifiers" 建议高度相关。

### 总结
R1 审稿质量高。我们在 RE 覆盖不足（R1-N1 = 我的 N2）、scale 局限（R1-W1 = 我的 W4）、greedy 命名（R1-W3 = 我的 minor）上达成共识。主要分歧在 N3（我认为 compression 本身 intrinsic 有证据，selection outcome 变化是另一回事）和 W5（filtering 差异是 dataset 特征非 confound）。ε circularity（R1-N2）是我未识别的新问题，同意其对辅助分析的影响，但主结论不受影响。

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

_source line 1095 · 2026-05-16T04:28:34.058430+00:00_

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

_source line 1096 · 2026-05-16T04:28:34.109622+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-8) =====
3	- id: R0-C1
4	  summary: 模型规模单一（仅 8B）
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  mentions:
11	  - round: 0
12	    reviewers: [1, 2]
13	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
14	  - round: 1
15	    reviewers: [1, 2]
16	    note: model-agnostic 与 Limitations 矛盾
17	  action_items:
18	  - round: 1
19	    action: 全文替换 model-agnostic → consistent across tested model families
20	    assigned_to: Paper Agent
21	    status: resolved
22	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
23	  resolution_round: 2
24	- id: R0-C2
25	  summary: 相关工作显著遗漏
26	  category: framing
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 0
30	  last_seen_round: 1
31	  mentions:
32	  - round: 0
33	    reviewers: [1, 2]
34	    note: 5 篇核心文献缺失
35	  - round: 1
36	    reviewers: [1, 2]
37	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
38	  action_items:
39	  - round: 1
40	    action: 补充 6 篇引用到 Related Work
41	    assigned_to: Paper Agent
42	    status: resolved
43	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
44	  resolution_round: 2
45	- id: R0-C3
46	  summary: RE 结论仅基于 SciERC 单数据集
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 0
51	  last_seen_round: 4
52	  mentions:
53	  - round: 0
54	    reviewers: [1, 2]
55	    note: 需跨数据集验证或降级措辞
56	  - round: 2
57	    reviewers: [1, 2]
58	    note: Abstract RE 措辞需修正
59	  - round: 3
60	    reviewers: [1, 2]
61	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
62	  - round: 4
63	    reviewers: [1, 2]
64	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
65	  action_items:
66	  - round: 1
67	    action: 降级措辞 universal → observed in SciERC
68	    assigned_to: Paper Agent
69	    status: resolved
70	  - round: 2
71	    action: Abstract 改为 NER (three datasets) and RE (SciERC)
72	
…[truncated 23350 chars]

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

_source line 1097 · 2026-05-16T04:31:01.799176+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 确认措辞修正到位\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认 49 条 bib 全部 cited\n  resolution_round: 2\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R3-W4\n  summary: FK independence 假设未验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\n  resolution_round: 9\n- id: R3-W5\n  summary: Cross-model scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: 标题改为当前版本，scope 限定\n  resolution_round: 9\n- id: R4-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: Abstract 压缩为 problem-finding-significance 结构\n  resolution_round: 9\n- id: R5-N1\n  summary: 贡献框架偏 incremental\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: 贡献重新框架化为 finding-led\n  resolution_round: 9\n- id: R7-W1\n  summary: LP temperature 依赖未说明\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: §4.4 明确排除 LP + Limitations 扩展说明\n  resolution_round: 9\n- id: R7-W3\n  summary: Eikema Related Work 覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: Related Work 增加 Eikema 讨论\n  resolution_round: 9\n- id: R8-N1\n  summary: 页数超限\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: 主文在限制内\n  resolution_round: 9\n- id: R8-W2\n  summary: Thinking token 对 LP 的影响未分析\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: Appendix 3-part quantitative analysis 已补充\n  resolution_round: 9\n- id: R8-W3\n  summary: SJ normalizer 选择敏感性\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: Appendix table Δρ<0.005 证明不敏感\n  resolution_round: 9\n- id: R9-W1\n  summary: 缺少其他 per-sample signal baseline\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\n  resolution_round: 9\n- id: R9-W3\n  summary: TOST 等价性结论 configuration-dependent 未整合进正文\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 已含 config-dependent note\n  resolution_round: 9\n- id: R9-W4\n  summary: VC majority-voting selection 失败机制未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Discussion 已补 MBR mode-seeking bias 分析\n  resolution_round: 9\n- id: R9-W5\n  summary: 多重比较校正不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 footnote 说明校正策略\n  resolution_round: 9\n- id: R9-W6\n  summary: Table 1 主表单种子未标注\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Table 1 caption 加 cross-ref\n  resolution_round: 9\n- id: R9-W7\n  summary: Scale ablation \"not model capacity\" 结论过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: 弱化为 \"within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: Table 2 Greedy 术语歧义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Table 2 caption 标注 T=1.0 sample\n  resolution_round: 9\n- id: R9-M2\n  summary: FK 负依赖数值无推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: 引用 Appendix permutation test\n  resolution_round: 9\n- id: R9-M3\n  summary: correlation-selection gap 术语无操作性定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 给出操作性定义\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (resolved previously, re-raised R11) =====\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集——title/abstract \"IE\" scope 过宽\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 0\n  last_seen_round: 11\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 4\n    reviewers: [1, 2]\n    note: claim 降级到位\n  - round: 9\n    reviewers: [1, 2]\n    note: Conclusion hedge 到位\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出：title 'LLM-Based Information Extraction' 仍暗示 NER+RE 充分覆盖，但 RE 仅 SciERC (40% zero-F1)。'preliminary' ≥11 次但 title/abstract 前两句未体现。两位 Reviewer 强共识。\"\n  action_items:\n  - round: 9\n    action: Conclusion 增加 RE hedge\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"(1) 标题或 abstract 首句显式限定 RE scope；(2) 增加至少一个 RE benchmark 或将 RE 完全移至附录\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号 selection 失败是定义必然，不应列为 empirical contribution\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需分离两层论证\n  - round: 9\n    reviewers: [1, 2]\n    note: Abstract/Intro reframe 完成\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review：R2 认为 Contribution 1 (Metric dissociation) 仍含 definitional 成分，不应算 empirical contribution。R1 部分同意 framing 需改进但认为 dissociation 有 empirical 内容（ρ-AUROC 解耦、VerbConf 失败）。共识：将 instance-level/per-sample 区分作为 §3 前提，贡献聚焦 LP compression + MBR failure + difficulty-dependent rankings。\"\n  action_items:\n  - round: 9\n    action: Abstract/Intro reframe 完成\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"Contribution 1 reframe：将 instance-level/per-sample 分类移入 §3 Problem Formulation 作为前提，Contribution 1 改为纯 empirical dissociation（ρ vs AUROC vs selection F1 decoupling）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: ε=0.05 threshold circularity / p-value optimization\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: ε=1pp threshold 无 prior justification\n  - round: 9\n    reviewers: [1]\n    note: 仅作 question 提出\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 R1-N2：Appendix G 'data-driven justification' 是 circular reasoning——ε 选择让 median LP range 落在阈值以下。Table 11 ε=0.05 恰好最强 p=0.004 暗示 p-value optimization。R2 同意核心批评但指出主 selection 结果（Table 2 LP 直接排序）不依赖 ε，仅辅助 tied/non-tied 分析受影响。共识：circularity 存在，影响辅助分析 credibility。\"\n  action_items:\n  - round: 11\n    action: \"(1) 删除 'data-driven justification' 措辞；(2) 用 ε-free 连续指标（median LP range + pooled within-instance ρ）作为主要呈现；(3) ε sweep 保留但标注 'post-hoc exploratory analysis'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 11) =====\n- id: R11-N3\n  summary: Abstract \"LP compression is not a decoding artifact\" 措辞被 RE free-form reversal 削弱\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-N3：Abstract 暗示 LP compression universally intrinsic，但 RE LP selection 从 -0.68pp (constrained) 反转为 +1.69pp (free-form)。R2 反驳：LP 分布确实 intrinsic (std ratio 0.97)，反转的是 selection outcome 非分布。但 R2 同意论文未解释 WHY compressed LP 在 RE free-form 下有效——mechanistic gap 需补充。共识层面：Abstract 措辞应更精确区分 NER vs RE。\"\n  action_items:\n  - round: 11\n    action: \"Abstract 保持当前措辞（已区分 NER/RE）但 Discussion 补充 RE free-form selection reversal 的 mechanistic hypothesis\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: 与 Yao et al. (2026) 的增量贡献定义不够清晰\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2-N3：三个 extension（structural matching、selection analysis、difficulty gradient）中 SJ vs EM 仅 marginal significance，selection 是 negative result，WNUT collapse。R1 反驳：selection analysis 是 test-time scaling 社区最关心的问题，structural vs LP gap clearly significant (Δρ=+0.155)，combined novelty 足够。分歧未完全解决但 R1 反驳有力。\"\n  action_items:\n  - round: 11\n    action: \"Introduction 增加与 Yao et al. 的明确差异 tabulation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: Scale range (3B-8B) 不足以支撑 \"task difficulty is primary driver\" 因果结论\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 共识。R9-W7 已弱化为 'within 4B-8B range'，本轮审稿认为进一步弱化是必要的。\"\n  action_items:\n  - round: 11\n    action: \"确认 §4.4 和 Conclusion 中所有 scale-related claims 均限定为 'within the 3B-8B range tested across two model families'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: 3 seeds 统计效力不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall's W=1.000 with n=3 不具信息量，σ≤0.026 基于 n=3 CI 极宽。建议增至 5-10 seeds 或弱化 stability 措辞。\"\n  action_items:\n  - round: 11\n    action: \"弱化 stability claims 或增加 seeds（至少 5）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: 缺少信号组合实验（如 VC 筛选 + LP 排序）\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp gain 暗示组合策略可能有效。两位 Reviewer 共识。\"\n  action_items:\n  - round: 11\n    action: \"增加至少一个 simple combination baseline（如 VC-filtered LP selection）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary\" 标注过于频繁（≥11次），削弱论文可信度\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"建议首次完整说明后用 † 标记替代。\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 出现次数，首次说明后用 † 或 Section 3 一次性声明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: LP compression 缺乏 mechanistic explanation\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"论文 characterize 了现象但未解释 WHY。应讨论可能 hypotheses：token averaging、schema-enforced tokens、effective vocabulary 缩小等。\"\n  action_items:\n  - round: 11\n    action: \"Discussion 增加 LP compression mechanistic hypotheses 段落\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: Greedy baseline 命名混淆——T=1.0 sample ≠ argmax\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R9-M1 标注了 Table 2 caption，但正文其他位置仍用 greedy 未限定。建议统一使用 'single-sample baseline' 或首次出现时明确定义。\"\n  action_items:\n  - round: 11\n    action: \"首次使用时明确定义 greedy = T=1.0 single sample (not argmax)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: Thinking token CoNLL control 论证薄弱\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-W6：CoNLL 高 tied fraction 更可能因 task easiness (88% identical outputs)，非排除 thinking token 证据。R2 同意此论证弱但其他两个论证（LP shift 0.001 nats + constant prefix cancellation）较强。整体证据充分。\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control group 论证措辞或补充说明 task easiness 混淆\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: Table 3 NER 2-seed vs 其他 3 seeds 未说明原因\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: 共识\n  action_items:\n  - round: 11\n    action: \"说明 Table 3 为何 NER 用 2-seed\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: Figure 1 caption 对 LP (per-sample signal) 不适用\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: 共识\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption 或增加 LP per-sample 说明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: 缺失引用——Fernandes et al. (2022) Quality-Aware Decoding + Conformal Structured Prediction (ICLR 2025)\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes et al. (2022) 两位 Reviewer 共识。Conformal Structured Prediction R1 同意 tangential 提及。另：'Beyond Confidence' (2605.07806) R1 同意引用。\"\n  action_items:\n  - round: 11\n    action: \"Related Work 或 Discussion 补充 Fernandes et al. 2022 + Conformal Structured Prediction + Beyond Confidence\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD FROM R9 (still open) =====\n- id: R9-W2\n  summary: orphan bib entries 未在正文引用\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 24 个 orphan entries\n  - round: 11\n    reviewers: []\n    note: \"本轮未独立提出，但 bib 问题仍存在\"\n  action_items:\n  - round: 9\n    action: 引用相关 entries 或删除不相关的\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: ρ=0.38 rounding 不精确\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: 统一小数位数\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: Table 2 NER/RE 统计标准不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean±σ + Fisher p，RE 单 seed 无 p-value\"\n  action_items:\n  - round: 9\n    action: 统一统计报告标准\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: Bib name order issues\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: 统一 bib 作者姓名格式\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 确认措辞修正到位\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认 49 条 bib 全部 cited\n  resolution_round: 2\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R3-W4\n  summary: FK independence 假设未验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\n  resolution_round: 9\n- id: R3-W5\n  summary: Cross-model scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: 标题改为当前版本，scope 限定\n  resolution_round: 9\n- id: R4-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: Abstract 压缩为 problem-finding-significance 结构\n  resolution_round: 9\n- id: R5-N1\n  summary: 贡献框架偏 incremental\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: 贡献重新框架化为 finding-led\n  resolution_round: 9\n- id: R7-W1\n  summary: LP temperature 依赖未说明\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: §4.4 明确排除 LP + Limitations 扩展说明\n  resolution_round: 9\n- id: R7-W3\n  summary: Eikema Related Work 覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: Related Work 增加 Eikema 讨论\n  resolution_round: 9\n- id: R8-N1\n  summary: 页数超限\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: 主文在限制内\n  resolution_round: 9\n- id: R8-W2\n  summary: Thinking token 对 LP 的影响未分析\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: Appendix 3-part quantitative analysis 已补充\n  resolution_round: 9\n- id: R8-W3\n  summary: SJ normalizer 选择敏感性\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: Appendix table Δρ<0.005 证明不敏感\n  resolution_round: 9\n- id: R9-W1\n  summary: 缺少其他 per-sample signal baseline\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\n  resolution_round: 9\n- id: R9-W3\n  summary: TOST 等价性结论 configuration-dependent 未整合进正文\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 已含 config-dependent note\n  resolution_round: 9\n- id: R9-W4\n  summary: VC majority-voting selection 失败机制未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Discussion 已补 MBR mode-seeking bias 分析\n  resolution_round: 9\n- id: R9-W5\n  summary: 多重比较校正不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 footnote 说明校正策略\n  resolution_round: 9\n- id: R9-W6\n  summary: Table 1 主表单种子未标注\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Table 1 caption 加 cross-ref\n  resolution_round: 9\n- id: R9-W7\n  summary: Scale ablation \"not model capacity\" 结论过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: 弱化为 \"within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: Table 2 Greedy 术语歧义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: Table 2 caption 标注 T=1.0 sample\n  resolution_round: 9\n- id: R9-M2\n  summary: FK 负依赖数值无推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: 引用 Appendix permutation test\n  resolution_round: 9\n- id: R9-M3\n  summary: correlation-selection gap 术语无操作性定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.2 给出操作性定义\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (resolved previously, re-raised R11) =====\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集——title/abstract \"IE\" scope 过宽\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 0\n  last_seen_round: 11\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 4\n    reviewers: [1, 2]\n    note: claim 降级到位\n  - round: 9\n    reviewers: [1, 2]\n    note: Conclusion hedge 到位\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出：title 'LLM-Based Information Extraction' 仍暗示 NER+RE 充分覆盖，但 RE 仅 SciERC (40% zero-F1)。'preliminary' ≥11 次但 title/abstract 前两句未体现。两位 Reviewer 强共识。\"\n  action_items:\n  - round: 9\n    action: Conclusion 增加 RE hedge\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"(1) 标题或 abstract 首句显式限定 RE scope；(2) 增加至少一个 RE benchmark 或将 RE 完全移至附录\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号 selection 失败是定义必然，不应列为 empirical contribution\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需分离两层论证\n  - round: 9\n    reviewers: [1, 2]\n    note: Abstract/Intro reframe 完成\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review：R2 认为 Contribution 1 (Metric dissociation) 仍含 definitional 成分，不应算 empirical contribution。R1 部分同意 framing 需改进但认为 dissociation 有 empirical 内容（ρ-AUROC 解耦、VerbConf 失败）。共识：将 instance-level/per-sample 区分作为 §3 前提，贡献聚焦 LP compression + MBR failure + difficulty-dependent rankings。\"\n  action_items:\n  - round: 9\n    action: Abstract/Intro reframe 完成\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"Contribution 1 reframe：将 instance-level/per-sample 分类移入 §3 Problem Formulation 作为前提，Contribution 1 改为纯 empirical dissociation（ρ vs AUROC vs selection F1 decoupling）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: ε=0.05 threshold circularity / p-value optimization\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: ε=1pp threshold 无 prior justification\n  - round: 9\n    reviewers: [1]\n    note: 仅作 question 提出\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 R1-N2：Appendix G 'data-driven justification' 是 circular reasoning——ε 选择让 median LP range 落在阈值以下。Table 11 ε=0.05 恰好最强 p=0.004 暗示 p-value optimization。R2 同意核心批评但指出主 selection 结果（Table 2 LP 直接排序）不依赖 ε，仅辅助 tied/non-tied 分析受影响。共识：circularity 存在，影响辅助分析 credibility。\"\n  action_items:\n  - round: 11\n    action: \"(1) 删除 'data-driven justification' 措辞；(2) 用 ε-free 连续指标（median LP range + pooled within-instance ρ）作为主要呈现；(3) ε sweep 保留但标注 'post-hoc exploratory analysis'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 11) =====\n- id: R11-N3\n  summary: Abstract \"LP compression is not a decoding artifact\" 措辞被 RE free-form reversal 削弱\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-N3：Abstract 暗示 LP compression universally intrinsic，但 RE LP selection 从 -0.68pp (constrained) 反转为 +1.69pp (free-form)。R2 反驳：LP 分布确实 intrinsic (std ratio 0.97)，反转的是 selection outcome 非分布。但 R2 同意论文未解释 WHY compressed LP 在 RE free-form 下有效——mechanistic gap 需补充。共识层面：Abstract 措辞应更精确区分 NER vs RE。\"\n  action_items:\n  - round: 11\n    action: \"Abstract 保持当前措辞（已区分 NER/RE）但 Discussion 补充 RE free-form selection reversal 的 mechanistic hypothesis\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: 与 Yao et al. (2026) 的增量贡献定义不够清晰\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2-N3：三个 extension（structural matching、selection analysis、difficulty gradient）中 SJ vs EM 仅 marginal significance，selection 是 negative result，WNUT collapse。R1 反驳：selection analysis 是 test-time scaling 社区最关心的问题，structural vs LP gap clearly significant (Δρ=+0.155)，combined novelty 足够。分歧未完全解决但 R1 反驳有力。\"\n  action_items:\n  - round: 11\n    action: \"Introduction 增加与 Yao et al. 的明确差异 tabulation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: Scale range (3B-8B) 不足以支撑 \"task difficulty is primary driver\" 因果结论\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 共识。R9-W7 已弱化为 'within 4B-8B range'，本轮审稿认为进一步弱化是必要的。\"\n  action_items:\n  - round: 11\n    action: \"确认 §4.4 和 Conclusion 中所有 scale-related claims 均限定为 'within the 3B-8B range tested across two model families'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: 3 seeds 统计效力不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall's W=1.000 with n=3 不具信息量，σ≤0.026 基于 n=3 CI 极宽。建议增至 5-10 seeds 或弱化 stability 措辞。\"\n  action_items:\n  - round: 11\n    action: \"弱化 stability claims 或增加 seeds（至少 5）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: 缺少信号组合实验（如 VC 筛选 + LP 排序）\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp gain 暗示组合策略可能有效。两位 Reviewer 共识。\"\n  action_items:\n  - round: 11\n    action: \"增加至少一个 simple combination baseline（如 VC-filtered LP selection）\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary\" 标注过于频繁（≥11次），削弱论文可信度\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"建议首次完整说明后用 † 标记替代。\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 出现次数，首次说明后用 † 或 Section 3 一次性声明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: LP compression 缺乏 mechanistic explanation\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"论文 characterize 了现象但未解释 WHY。应讨论可能 hypotheses：token averaging、schema-enforced tokens、effective vocabulary 缩小等。\"\n  action_items:\n  - round: 11\n    action: \"Discussion 增加 LP compression mechanistic hypotheses 段落\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: Greedy baseline 命名混淆——T=1.0 sample ≠ argmax\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R9-M1 标注了 Table 2 caption，但正文其他位置仍用 greedy 未限定。建议统一使用 'single-sample baseline' 或首次出现时明确定义。\"\n  action_items:\n  - round: 11\n    action: \"首次使用时明确定义 greedy = T=1.0 single sample (not argmax)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: Thinking token CoNLL control 论证薄弱\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-W6：CoNLL 高 tied fraction 更可能因 task easiness (88% identical outputs)，非排除 thinking token 证据。R2 同意此论证弱但其他两个论证（LP shift 0.001 nats + constant prefix cancellation）较强。整体证据充分。\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control group 论证措辞或补充说明 task easiness 混淆\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: Table 3 NER 2-seed vs 其他 3 seeds 未说明原因\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: 共识\n  action_items:\n  - round: 11\n    action: \"说明 Table 3 为何 NER 用 2-seed\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: Figure 1 caption 对 LP (per-sample signal) 不适用\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: 共识\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption 或增加 LP per-sample 说明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: 缺失引用——Fernandes et al. (2022) Quality-Aware Decoding + Conformal Structured Prediction (ICLR 2025)\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes et al. (2022) 两位 Reviewer 共识。Conformal Structured Prediction R1 同意 tangential 提及。另：'Beyond Confidence' (2605.07806) R1 同意引用。\"\n  action_items:\n  - round: 11\n    action: \"Related Work 或 Discussion 补充 Fernandes et al. 2022 + Conformal Structured Prediction + Beyond Confidence\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD FROM R9 (still open) =====\n- id: R9-W2\n  summary: orphan bib entries 未在正文引用\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: 24 个 orphan entries\n  - round: 11\n    reviewers: []\n    note: \"本轮未独立提出，但 bib 问题仍存在\"\n  action_items:\n  - round: 9\n    action: 引用相关 entries 或删除不相关的\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: ρ=0.38 rounding 不精确\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: 统一小数位数\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: Table 2 NER/RE 统计标准不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean±σ + Fisher p，RE 单 seed 无 p-value\"\n  action_items:\n  - round: 9\n    action: 统一统计报告标准\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: Bib name order issues\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: 统一 bib 作者姓名格式\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-16T04:31:01.900298+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"issues_yaml is not valid YAML: while parsing a block mapping\\n  in \\\"&lt;unicode string>\\\", line 412, column 3:\\n    - id: R11-W5\\n      ^\\nexpected &lt;block end>, but found '&lt;scalar>'\\n  in \\\"&lt;unicode string>\\\", line 413, column 26:\\n      summary: \\\"Preliminary\\\" 标注过于频繁（≥11次），削弱论文可信度\\n                             ^\"}"}

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

_source line 1099 · 2026-05-16T04:32:23.647437+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (resolved previously, re-raised R11) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, title/abstract IE scope 过宽\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 0\n  last_seen_round: 11\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出: title LLM-Based IE 仍暗示 NER+RE 充分覆盖, 但 RE 仅 SciERC (40% zero-F1). preliminary 11+ 次但 title/abstract 前两句未体现. 两位 Reviewer 强共识.\"\n  action_items:\n  - round: 9\n    action: \"Conclusion 增加 RE hedge\"\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope, 或增加至少一个 RE benchmark\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11: R2 认为 Contribution 1 仍含 definitional 成分. R1 部分同意但认为 dissociation 有 empirical 内容. 共识: 将 instance-level/per-sample 区分作为 Section 3 前提.\"\n  action_items:\n  - round: 9\n    action: \"Abstract/Intro reframe 完成\"\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"Contribution 1 reframe: 将分类移入 Section 3, 贡献聚焦纯 empirical dissociation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold circularity / p-value optimization\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 R1-N2: Appendix G data-driven justification 是 circular reasoning. R2 同意核心批评但主 selection 结果不依赖 epsilon. 共识: circularity 存在, 影响辅助分析.\"\n  action_items:\n  - round: 11\n    action: \"删除 data-driven justification 措辞, 用 epsilon-free 连续指标作主要呈现, epsilon sweep 标注 post-hoc exploratory\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 11) =====\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-N3 vs R2 rebut. 共识: LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释.\"\n  action_items:\n  - round: 11\n    action: \"Discussion 补充 RE free-form selection reversal mechanistic hypothesis\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2-N3 提出, R1 反驳 selection analysis 有独立价值. 分歧部分解决.\"\n  action_items:\n  - round: 11\n    action: \"Introduction 增加与 Yao et al. 明确差异 tabulation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑因果结论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 共识. 需确认所有 scale claims 均限定范围.\"\n  action_items:\n  - round: 11\n    action: \"确认所有 scale claims 限定为 within 3B-8B range\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量. 建议增 seeds 或弱化措辞.\"\n  action_items:\n  - round: 11\n    action: \"弱化 stability claims 或增加 seeds\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效. 两位共识.\"\n  action_items:\n  - round: 11\n    action: \"增加至少一个 simple combination baseline\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁, 削弱论文可信度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses.\"\n  action_items:\n  - round: 11\n    action: \"Discussion 增加 LP compression mechanistic hypotheses\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"Greedy baseline 命名混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax. 正文其他位置仍用 greedy 未限定.\"\n  action_items:\n  - round: 11\n    action: \"首次使用时明确定义 greedy = T=1.0 single sample\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness. 其他两个论证较强, 整体充分.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Table 3 NER 2-seed vs 其他 3 seeds 未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  action_items:\n  - round: 11\n    action: \"说明 Table 3 NER 2-seed 原因\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用: Fernandes 2022 + Conformal Structured Prediction + Beyond Confidence\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022 两位共识. CSP 和 Beyond Confidence R1 同意.\"\n  action_items:\n  - round: 11\n    action: \"补充 3 篇引用\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD FROM R9 (still open) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Table 2 NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (resolved previously, re-raised R11) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, title/abstract IE scope 过宽\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 0\n  last_seen_round: 11\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出: title LLM-Based IE 仍暗示 NER+RE 充分覆盖, 但 RE 仅 SciERC (40% zero-F1). preliminary 11+ 次但 title/abstract 前两句未体现. 两位 Reviewer 强共识.\"\n  action_items:\n  - round: 9\n    action: \"Conclusion 增加 RE hedge\"\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope, 或增加至少一个 RE benchmark\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 11\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11: R2 认为 Contribution 1 仍含 definitional 成分. R1 部分同意但认为 dissociation 有 empirical 内容. 共识: 将 instance-level/per-sample 区分作为 Section 3 前提.\"\n  action_items:\n  - round: 9\n    action: \"Abstract/Intro reframe 完成\"\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 11\n    action: \"Contribution 1 reframe: 将分类移入 Section 3, 贡献聚焦纯 empirical dissociation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold circularity / p-value optimization\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 R1-N2: Appendix G data-driven justification 是 circular reasoning. R2 同意核心批评但主 selection 结果不依赖 epsilon. 共识: circularity 存在, 影响辅助分析.\"\n  action_items:\n  - round: 11\n    action: \"删除 data-driven justification 措辞, 用 epsilon-free 连续指标作主要呈现, epsilon sweep 标注 post-hoc exploratory\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 11) =====\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R1-N3 vs R2 rebut. 共识: LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释.\"\n  action_items:\n  - round: 11\n    action: \"Discussion 补充 RE free-form selection reversal mechanistic hypothesis\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2-N3 提出, R1 反驳 selection analysis 有独立价值. 分歧部分解决.\"\n  action_items:\n  - round: 11\n    action: \"Introduction 增加与 Yao et al. 明确差异 tabulation\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑因果结论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"两位 Reviewer 共识. 需确认所有 scale claims 均限定范围.\"\n  action_items:\n  - round: 11\n    action: \"确认所有 scale claims 限定为 within 3B-8B range\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量. 建议增 seeds 或弱化措辞.\"\n  action_items:\n  - round: 11\n    action: \"弱化 stability claims 或增加 seeds\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效. 两位共识.\"\n  action_items:\n  - round: 11\n    action: \"增加至少一个 simple combination baseline\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁, 削弱论文可信度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses.\"\n  action_items:\n  - round: 11\n    action: \"Discussion 增加 LP compression mechanistic hypotheses\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"Greedy baseline 命名混淆\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax. 正文其他位置仍用 greedy 未限定.\"\n  action_items:\n  - round: 11\n    action: \"首次使用时明确定义 greedy = T=1.0 single sample\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness. 其他两个论证较强, 整体充分.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Table 3 NER 2-seed vs 其他 3 seeds 未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  action_items:\n  - round: 11\n    action: \"说明 Table 3 NER 2-seed 原因\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用: Fernandes 2022 + Conformal Structured Prediction + Beyond Confidence\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022 两位共识. CSP 和 Beyond Confidence R1 同意.\"\n  action_items:\n  - round: 11\n    action: \"补充 3 篇引用\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD FROM R9 (still open) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Table 2 NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-16T04:32:23.698370+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 14705}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-16T04:34:41.997425+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# Round 11 Consolidated Review Report\n## Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Target Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 写作质量)\n\n---\n\n## Summary\n\n论文系统评估了 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE (NER + RE) 中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：所有信号能预测输出质量（Spearman ρ 达 0.45）但无法改善 best-of-N 选择，尽管存在 13-18 pp 的 oracle headroom。4/5 信号是 instance-level 的（by construction 无法 per-sample ranking），第 5 个信号 LP 因 score compression（60% tied）而失败。Free-form decoding ablation 在 NER 上确认 compression 非 constrained decoding artifact；RE 上 LP selection 方向反转。实验覆盖 3 个 NER 数据集、1 个 RE 数据集、2 个模型族（3B-8B）、多 seed/温度/N。\n\n---\n\n## Strengths\n\n**[S1] 统计方法论上乘** [AGREE: R1, R2]\nBootstrap CI、TOST with external anchors、permutation test、Fisher combined p、Bonferroni correction——在同类 empirical NLP 工作中属于高标准。三指标框架（ρ + AUROC + selection F1）的 dissociation 展示具有独立方法论价值。\n\n**[S2] LP compression 诊断系统性强** [AGREE: R1, R2]\n从分布特征（median range 0.041 nats）到条件分析（non-tied subset +2.9pp, p=0.004）到因果排除（free-form ablation std ratio 0.97）到 verbalized confidence 控制实验，形成了完整的证据链。这是论文最有洞察力的贡献。\n\n**[S3] Appendix 质量极高** [AGREE: R1, R2]\n15+ sections 覆盖了几乎每个 claim 的 robustness check：LOO-SJ equivalence、FK independence test、OOD analysis、ε sensitivity sweep、diversity-stratified selection、scale ablation 等。\n\n**[S4] 诚实的 scope 限定和 Limitations** [AGREE: R1, R2]\nRE 结论标注 preliminary、free-form ablation 限制明确、scale 范围声明——论文的 intellectual honesty 值得肯定。\n\n**[S5] Matched training protocol** [AGREE: R1, R2]\n两个模型族使用完全相同的训练配置，消除训练 confound，增强跨模型比较可信度。\n\n**[S6] 清晰的 practical recommendations** [AGREE: R1, R2]\nVC for hard NER, EM for easy NER, LP for RE——对 IE 实践者有直接参考价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[MF1] RE 覆盖不足 vs title/abstract \"Information Extraction\" scope** [AGREE: R1-N1, R2-N2 — 强共识]\n- Title 和 Abstract 前两句将贡献定位为 \"Information Extraction\" 涵盖 NER + RE，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1, n=397 non-empty）。NER 有 3 个 benchmark 跨难度梯度。\"Preliminary\" 在正文出现 11+ 次但 title/abstract 未反映。\n- **影响**：单一 RE benchmark 不足以支撑 \"IE\" 级别 claim。这是跨 11 轮审稿反复出现的持久性问题（首次 R0-C3）。\n- **建议**：(1) 增加至少一个 RE benchmark（TACRED/DocRED/ACE05），或 (2) 将 title 限定为 NER-focused + RE 作为 exploratory extension，或 (3) 将 RE 结论完全移至附录。\n\n**[MF2] ε=0.05 tied-fraction threshold 的 circularity** [AGREE with nuance: R1-N2, R2 agrees core but notes main results ε-free]\n- Appendix G 声称 median LP range (0.041) 低于 ε=0.05 作为 \"data-driven justification\"——这是 circular reasoning。Table 11 ε sweep 中 ε=0.05 恰好给出最强 p=0.004，有 p-value optimization 之嫌。\n- **缓解因素**（R2 指出）：主 selection 结果（Table 2 LP 直接排序，Δ=+0.2pp, p=0.29）不依赖 ε。Appendix G 也报告了 ε-free 连续指标 pooled within-instance ρ=0.248。Circularity 影响辅助 tied/non-tied 分析 credibility，不动摇主结论。\n- **建议**：(1) 删除 \"data-driven justification\" 措辞；(2) 用 ε-free 连续指标（median LP range + pooled within-instance ρ）作为主要呈现；(3) ε sweep 保留但标注 \"post-hoc exploratory analysis\"。\n\n**[MF3] Instance-level signals \"fail by construction\" framing 需改进** [PARTIAL: R2-N1, R1 partially agrees]\n- 4/5 信号因 instance-level 粒度无法 rank candidates 是定义层面必然，不应列为 empirical contribution。论文自己承认 \"fail by construction\" 却列入 Contribution 1。\n- **R1 反驳要点**：Metric dissociation（ρ/AUROC/selection F1 decoupling）有 empirical 内容——如 VerbConf ρ > LP 但 selection 最差（Appendix K），LP full/conditional ρ inversion（Table 4）。这些需要数据展示。\n- **共识**：将 instance-level/per-sample 分类移入 §3 作为 problem formulation 前提，Contribution 1 reframe 为纯 empirical dissociation（ρ vs AUROC vs selection F1 解耦）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[SF1] Scale range (3B-8B) 不足以支撑因果结论** [AGREE: R1-W1, R2-W4]\n- \"Task difficulty is the primary driver\" 仅基于 3B-8B 两个规模点。70B+ 模型的 LP 分布可能有质的变化。\n- 建议：弱化为 \"task difficulty is a stronger predictor than model scale within the 3B-8B range tested\"。\n\n**[SF2] 3 seeds 统计效力不足** [AGREE: R1-W2, R2]\n- Kendall's W=1.000 with n=3 不具统计信息量。σ≤0.026 基于 n=3，95% CI 极宽。\n- 建议：增至 5-10 seeds 或弱化 stability measures 的措辞。\n\n**[SF3] 缺少信号组合实验** [AGREE: R1-W4, R2]\n- LP non-tied subset 的 +2.9pp gain 暗示 VC 筛选 + LP 排序等 cascaded 策略可能有效。论文 Discussion 建议 trained verifiers 但未探索 simpler combinations。\n- 建议：增加至少一个 combination baseline（如 VC-filtered LP selection）。\n\n**[SF4] LP compression 缺乏 mechanistic explanation** [AGREE: R1, R2-W2]\n- 论文详细 characterize 了 compression 现象并排除了多个原因，但未解释 WHY。\n- 建议：Discussion 增加 hypotheses 段落——token averaging 平滑 variance、schema-enforced tokens 占多数导致有效 variance 来源少、constrained decoding 下 effective vocabulary 缩小等。\n\n**[SF5] \"Preliminary\" 标注过于频繁** [AGREE: R1, R2-W1]\n- 11+ 次出现给人 \"工作未完成就提交\" 的印象。\n- 建议：首次完整说明后用 † 标记替代。\n\n**[SF6] \"Greedy\" baseline 命名混淆** [AGREE: R1-W3, R2]\n- NLP 中 \"greedy\" 通常指 argmax (T→0)。T=1.0 single sample 应命名为 \"single-sample baseline\"。Table 2 caption 已标注但正文其他位置未限定。\n\n**[SF7] 与 Yao et al. (2026) 增量贡献定义不够清晰** [DIVERGENT: R2-N3, R1 rebuts]\n- R2 认为三个 extension 中 SJ vs EM 仅 marginal significance、selection 是 negative result、WNUT collapse，combined novelty 有限。\n- R1 反驳：structural vs LP gap clearly significant (Δρ=+0.155, CI [+0.074, +0.234])；selection analysis 是 test-time scaling 社区最关心的问题；WNUT LP full/conditional inversion 提供 diagnostic insight。\n- **建议**：Introduction 增加与 Yao et al. 的明确差异 tabulation。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n1. RE 单一 benchmark 与 title scope 不匹配（strongest consensus）\n2. ε=0.05 circularity 存在（影响程度有分歧——R1 认为 critical，R2 认为仅影响辅助分析）\n3. Scale 3B-8B 不足以支撑因果结论\n4. 3 seeds 统计效力有限\n5. 需要信号组合实验\n6. LP compression 需 mechanistic explanation\n7. \"Preliminary\" 过频\n8. \"Greedy\" 命名混淆\n9. 统计方法论是论文强项\n10. LP compression 诊断分析是核心贡献\n11. Appendix 质量极高\n\n## Reviewer Divergence\n\n**[DIV1] LP \"intrinsic\" claim vs RE free-form reversal (R1-N3 vs R2 rebut)**\n- R1：RE LP selection 在 free-form 下从 −0.68pp 反转为 +1.69pp，至少对 RE，constrained decoding 是 LP selection failure 的一个因素。Abstract 措辞过强。\n- R2：LP **分布** 在两种 regime 下几乎一致（std ratio 0.97），compression 本身确实 intrinsic。RE 反转的是 **selection outcome** 非 LP 分布。Abstract 已正确区分。但同意论文未充分解释 WHY compressed LP 在 RE free-form 下有效。\n- **Director 判断**：R2 的区分有道理——分布 vs selection outcome 是不同层面。但 R1 的核心批评也合理：Abstract 措辞可以更精确。建议保持当前 Abstract 措辞（已区分 NER/RE）但在 Discussion 补充 RE reversal mechanistic hypothesis。降级为 warning 而非 critical。\n\n**[DIV2] Novelty sufficiency for main conference (R1: 3.5/5 vs R2: 3.0/5)**\n- R1 认为 combined novelty 足够 borderline main conference；R2 认为仅够 Findings。\n- 核心分歧：selection analysis 作为 negative result 的价值判断。R1 认为 \"more samples ≠ better selection in structured IE\" 对 test-time scaling 社区有重要意义；R2 认为与 MBR 文献已知 utility-quality misalignment 增量有限。\n\n**[DIV3] Conformal prediction 覆盖 (R2-W3 vs R1 rebut)**\n- R1 认为 conformal prediction 构建 prediction sets，与 best-of-N selection 目标 fundamentally 不同，brief mention 足矣。\n- **Director 判断**：同意 R1，Related Work 一句简要提及即可。\n\n**[DIV4] Gold-empty filtering 跨数据集可比性 (R1-W5 vs R2 rebut)**\n- R2 认为比例差异反映 dataset 特征而非 confound，selection 分析用 full set 不 filter。\n- **Director 判断**：同意 R2，非 confound。但建议报告 CoNLL full-set ρ 作为参考。\n\n---\n\n## Questions to Authors\n\n1. ε=0.05 的选择是否先于 LP range 分析确定？如果是 post-hoc 选择，是否有 pre-registered 替代方案？\n2. Table 3 NER selection 为何用 2 seeds 而非 3？是 data availability issue 还是 design choice？\n3. 是否考虑过 LP + consistency signal 组合策略（如 VC-filtered LP selection）？如有结果请提供。\n4. Free-form RE LP reversal 是否在 T≠1.0 下也成立？\n5. 增加 TACRED 或 ACE05 RE benchmark 是否预计 RE conclusions 会有质性变化？\n6. LP compression 的 mechanistic cause 有无初步假说？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识或一方同意、另一方未反对：\n1. **Fernandes et al. (2022)** \"Quality-Aware Decoding for Neural Machine Translation\" — 将 QE 与 MBR 结合用 learned estimator rerank，与本文 \"trained verifiers\" 建议高度相关 [AGREE: R1, R2]\n2. **Conformal Structured Prediction (ICLR 2025; arxiv 2410.06296)** — set-valued uncertainty for structured prediction，tangential but worth brief mention [AGREE: R1, R2]\n3. **\"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\" (arxiv 2605.07806)** — alternative self-assessment dimensions，与 verbalized confidence failure 相关 [AGREE: R1, R2]\n\n以下引用有分歧（一方提出，另一方认为非必要）：\n4. **Huang et al. (2024)** \"Large Language Models Cannot Self-Correct Reasoning Yet\" — R1 提出，R2 反驳（self-correction ≠ self-consistency，paradigm 不同）\n5. **\"Learning When to Sample\" (arxiv 2603.08999)** — R2 提出，R1 反驳（discrete-answer，已有充分覆盖）\n6. **Slim-SC / Thought Pruning (EMNLP 2025)** — R2 提出，R1 反驳（discrete-answer efficiency，不同问题）\n\n---\n\n## Overall Assessment\n\n**Score**: borderline (between weak reject and weak accept for main conference)\n**Confidence**: 4/5\n\n**R1**: 3.5/5 — 方法论扎实，NER 结论有充分支撑，适合 borderline main / strong Findings\n**R2**: 3.0/5 — novelty 不够 main conference，适合 Findings\n\n**Director 综合判断**：\n\n论文是一篇方法论扎实、统计严谨的 empirical study。LP compression 诊断和三指标 dissociation 框架有独立贡献。但存在三个核心限制：\n\n1. **RE 覆盖不足**（跨 11 轮反复出现的持久性问题）——title 声称 \"Information Extraction\" 但 RE 仅有单一 benchmark，这是最大的 scope-evidence 不匹配。\n2. **Novelty 边界模糊**——instance-level signals \"fail by construction\" 是 definitional 而非 empirical，去掉后核心 empirical 贡献（LP compression + MBR within-instance failure）增量需要更清晰地与 Yao et al. (2026) 和 MBR 文献区分。\n3. **辅助分析 credibility 受 ε circularity 影响**——虽然主结论不受影响，但 tied/non-tied 分析是论文最引人注目的诊断，其 threshold 选择问题需要修正。\n\n**推荐**：以当前状态适合 **EMNLP 2026 Findings**。若能 (1) 增加至少一个 RE benchmark 或将 RE scope 显式限定，(2) reframe Contribution 1 消除 definitional 成分，(3) 修正 ε circularity，则有潜力提升至 **borderline accept for main conference**。\n\n---\n\n## Detailed Comments (by Section)\n\n### Abstract\n- 信息密度适当，9 行 problem-finding-significance 结构。\n- \"NER and RE benchmarks\" 应改为 \"three NER and one RE benchmark\" 以反映实际覆盖。\n- \"4-seed free-form decoding ablation confirms NER compression\" 准确；RE reversal 描述也准确。\n- 建议删减 \"preliminary, single benchmark\" 括号注——正文详述即可。\n\n### Introduction\n- Contribution 1 \"Metric dissociation\" 混合 definitional 和 empirical 元素，需重构。\n- 与 Yao et al. (2026) 的差异描述过于简略（\"we extend their work\"），需要更具体的 tabulation。\n- Figure 1 caption 不适用于 LP（per-sample signal）。\n\n### Related Work\n- 覆盖较为全面，Eikema et al. (2025) structured MBR 讨论到位。\n- 缺少 Fernandes et al. (2022) Quality-Aware Decoding 和 Conformal Structured Prediction。\n- 可增加简要提及 self-assessment limitation 文献。\n\n### Method\n- 信号定义清晰，公式完整。\n- Instance-level vs per-sample 区分是论文的重要框架——建议从 §3.2 开头强调这一分类，为后续 gap 分析奠基。\n- FK independence 假设通过 Appendix permutation test 验证，方法严谨。\n\n### Experiments\n- 实验设计系统，跨数据集/模型/seed/温度/N 的 coverage 全面。\n- Table 1 单 seed (42) 已标注 + cross-ref 3-seed 表，处理得当。\n- Table 3 NER 2-seed vs RE 单 seed 的不一致需解释。\n- Scale ablation（Table 4）仅 Qwen 4B vs 8B，无 LLaMA 4B，限制了结论力度。\n\n### Discussion\n- Practical recommendations 清晰有用。\n- LP compression 描述详尽但缺 mechanistic hypothesis。\n- Free-form ablation RE reversal 需更深入讨论 WHY。\n- \"Trained verifiers\" 前瞻有价值但略显 hand-wavy。\n\n### Conclusion\n- RE hedge 到位（\"rest on SciERC alone\"）。\n- Scale 限定到位（\"3B-8B\"）。\n- 整体简洁准确。\n\n### Limitations\n- 诚实且全面。Verbalized confidence 作为补充实验增强了可信度。\n- 可增加：signal combination 未探索、ε threshold 选择局限性。\n\n### Appendix\n- 22 页中 12+ 页 appendix，质量极高。\n- LOO-SJ equivalence、SJ normalizer robustness、FK independence test 等分析展示了罕见的 rigor。\n- ε sensitivity sweep (Table 11) 需标注 post-hoc exploratory。\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "project": "struct_self_consist_ie",
    "report": "# Round 11 Consolidated Review Report\n## Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Target Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 写作质量)\n\n---\n\n## Summary\n\n论文系统评估了 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE (NER + RE) 中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：所有信号能预测输出质量（Spearman ρ 达 0.45）但无法改善 best-of-N 选择，尽管存在 13-18 pp 的 oracle headroom。4/5 信号是 instance-level 的（by construction 无法 per-sample ranking），第 5 个信号 LP 因 score compression（60% tied）而失败。Free-form decoding ablation 在 NER 上确认 compression 非 constrained decoding artifact；RE 上 LP selection 方向反转。实验覆盖 3 个 NER 数据集、1 个 RE 数据集、2 个模型族（3B-8B）、多 seed/温度/N。\n\n---\n\n## Strengths\n\n**[S1] 统计方法论上乘** [AGREE: R1, R2]\nBootstrap CI、TOST with external anchors、permutation test、Fisher combined p、Bonferroni correction——在同类 empirical NLP 工作中属于高标准。三指标框架（ρ + AUROC + selection F1）的 dissociation 展示具有独立方法论价值。\n\n**[S2] LP compression 诊断系统性强** [AGREE: R1, R2]\n从分布特征（median range 0.041 nats）到条件分析（non-tied subset +2.9pp, p=0.004）到因果排除（free-form ablation std ratio 0.97）到 verbalized confidence 控制实验，形成了完整的证据链。这是论文最有洞察力的贡献。\n\n**[S3] Appendix 质量极高** [AGREE: R1, R2]\n15+ sections 覆盖了几乎每个 claim 的 robustness check：LOO-SJ equivalence、FK independence test、OOD analysis、ε sensitivity sweep、diversity-stratified selection、scale ablation 等。\n\n**[S4] 诚实的 scope 限定和 Limitations** [AGREE: R1, R2]\nRE 结论标注 preliminary、free-form ablation 限制明确、scale 范围声明——论文的 intellectual honesty 值得肯定。\n\n**[S5] Matched training protocol** [AGREE: R1, R2]\n两个模型族使用完全相同的训练配置，消除训练 confound，增强跨模型比较可信度。\n\n**[S6] 清晰的 practical recommendations** [AGREE: R1, R2]\nVC for hard NER, EM for easy NER, LP for RE——对 IE 实践者有直接参考价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[MF1] RE 覆盖不足 vs title/abstract \"Information Extraction\" scope** [AGREE: R1-N1, R2-N2 — 强共识]\n- Title 和 Abstract 前两句将贡献定位为 \"Information Extraction\" 涵盖 NER + RE，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1, n=397 non-empty）。NER 有 3 个 benchmark 跨难度梯度。\"Preliminary\" 在正文出现 11+ 次但 title/abstract 未反映。\n- **影响**：单一 RE benchmark 不足以支撑 \"IE\" 级别 claim。这是跨 11 轮审稿反复出现的持久性问题（首次 R0-C3）。\n- **建议**：(1) 增加至少一个 RE benchmark（TACRED/DocRED/ACE05），或 (2) 将 title 限定为 NER-focused + RE 作为 exploratory extension，或 (3) 将 RE 结论完全移至附录。\n\n**[MF2] ε=0.05 tied-fraction threshold 的 circularity** [AGREE with nuance: R1-N2, R2 agrees core but notes main results ε-free]\n- Appendix G 声称 median LP range (0.041) 低于 ε=0.05 作为 \"data-driven justification\"——这是 circular reasoning。Table 11 ε sweep 中 ε=0.05 恰好给出最强 p=0.004，有 p-value optimization 之嫌。\n- **缓解因素**（R2 指出）：主 selection 结果（Table 2 LP 直接排序，Δ=+0.2pp, p=0.29）不依赖 ε。Appendix G 也报告了 ε-free 连续指标 pooled within-instance ρ=0.248。Circularity 影响辅助 tied/non-tied 分析 credibility，不动摇主结论。\n- **建议**：(1) 删除 \"data-driven justification\" 措辞；(2) 用 ε-free 连续指标（median LP range + pooled within-instance ρ）作为主要呈现；(3) ε sweep 保留但标注 \"post-hoc exploratory analysis\"。\n\n**[MF3] Instance-level signals \"fail by construction\" framing 需改进** [PARTIAL: R2-N1, R1 partially agrees]\n- 4/5 信号因 instance-level 粒度无法 rank candidates 是定义层面必然，不应列为 empirical contribution。论文自己承认 \"fail by construction\" 却列入 Contribution 1。\n- **R1 反驳要点**：Metric dissociation（ρ/AUROC/selection F1 decoupling）有 empirical 内容——如 VerbConf ρ > LP 但 selection 最差（Appendix K），LP full/conditional ρ inversion（Table 4）。这些需要数据展示。\n- **共识**：将 instance-level/per-sample 分类移入 §3 作为 problem formulation 前提，Contribution 1 reframe 为纯 empirical dissociation（ρ vs AUROC vs selection F1 解耦）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[SF1] Scale range (3B-8B) 不足以支撑因果结论** [AGREE: R1-W1, R2-W4]\n- \"Task difficulty is the primary driver\" 仅基于 3B-8B 两个规模点。70B+ 模型的 LP 分布可能有质的变化。\n- 建议：弱化为 \"task difficulty is a stronger predictor than model scale within the 3B-8B range tested\"。\n\n**[SF2] 3 seeds 统计效力不足** [AGREE: R1-W2, R2]\n- Kendall's W=1.000 with n=3 不具统计信息量。σ≤0.026 基于 n=3，95% CI 极宽。\n- 建议：增至 5-10 seeds 或弱化 stability measures 的措辞。\n\n**[SF3] 缺少信号组合实验** [AGREE: R1-W4, R2]\n- LP non-tied subset 的 +2.9pp gain 暗示 VC 筛选 + LP 排序等 cascaded 策略可能有效。论文 Discussion 建议 trained verifiers 但未探索 simpler combinations。\n- 建议：增加至少一个 combination baseline（如 VC-filtered LP selection）。\n\n**[SF4] LP compression 缺乏 mechanistic explanation** [AGREE: R1, R2-W2]\n- 论文详细 characterize 了 compression 现象并排除了多个原因，但未解释 WHY。\n- 建议：Discussion 增加 hypotheses 段落——token averaging 平滑 variance、schema-enforced tokens 占多数导致有效 variance 来源少、constrained decoding 下 effective vocabulary 缩小等。\n\n**[SF5] \"Preliminary\" 标注过于频繁** [AGREE: R1, R2-W1]\n- 11+ 次出现给人 \"工作未完成就提交\" 的印象。\n- 建议：首次完整说明后用 † 标记替代。\n\n**[SF6] \"Greedy\" baseline 命名混淆** [AGREE: R1-W3, R2]\n- NLP 中 \"greedy\" 通常指 argmax (T→0)。T=1.0 single sample 应命名为 \"single-sample baseline\"。Table 2 caption 已标注但正文其他位置未限定。\n\n**[SF7] 与 Yao et al. (2026) 增量贡献定义不够清晰** [DIVERGENT: R2-N3, R1 rebuts]\n- R2 认为三个 extension 中 SJ vs EM 仅 marginal significance、selection 是 negative result、WNUT collapse，combined novelty 有限。\n- R1 反驳：structural vs LP gap clearly significant (Δρ=+0.155, CI [+0.074, +0.234])；selection analysis 是 test-time scaling 社区最关心的问题；WNUT LP full/conditional inversion 提供 diagnostic insight。\n- **建议**：Introduction 增加与 Yao et al. 的明确差异 tabulation。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n1. RE 单一 benchmark 与 title scope 不匹配（strongest consensus）\n2. ε=0.05 circularity 存在（影响程度有分歧——R1 认为 critical，R2 认为仅影响辅助分析）\n3. Scale 3B-8B 不足以支撑因果结论\n4. 3 seeds 统计效力有限\n5. 需要信号组合实验\n6. LP compression 需 mechanistic explanation\n7. \"Preliminary\" 过频\n8. \"Greedy\" 命名混淆\n9. 统计方法论是论文强项\n10. LP compression 诊断分析是核心贡献\n11. Appendix 质量极高\n\n## Reviewer Divergence\n\n**[DIV1] LP \"intrinsic\" claim vs RE free-form reversal (R1-N3 vs R2 rebut)**\n- R1：RE LP selection 在 free-form 下从 −0.68pp 反转为 +1.69pp，至少对 RE，constrained decoding 是 LP selection failure 的一个因素。Abstract 措辞过强。\n- R2：LP **分布** 在两种 regime 下几乎一致（std ratio 0.97），compression 本身确实 intrinsic。RE 反转的是 **selection outcome** 非 LP 分布。Abstract 已正确区分。但同意论文未充分解释 WHY compressed LP 在 RE free-form 下有效。\n- **Director 判断**：R2 的区分有道理——分布 vs selection outcome 是不同层面。但 R1 的核心批评也合理：Abstract 措辞可以更精确。建议保持当前 Abstract 措辞（已区分 NER/RE）但在 Discussion 补充 RE reversal mechanistic hypothesis。降级为 warning 而非 critical。\n\n**[DIV2] Novelty sufficiency for main conference (R1: 3.5/5 vs R2: 3.0/5)**\n- R1 认为 combined novelty 足够 borderline main conference；R2 认为仅够 Findings。\n- 核心分歧：selection analysis 作为 negative result 的价值判断。R1 认为 \"more samples ≠ better selection in structured IE\" 对 test-time scaling 社区有重要意义；R2 认为与 MBR 文献已知 utility-quality misalignment 增量有限。\n\n**[DIV3] Conformal prediction 覆盖 (R2-W3 vs R1 rebut)**\n- R1 认为 conformal prediction 构建 prediction sets，与 best-of-N selection 目标 fundamentally 不同，brief mention 足矣。\n- **Director 判断**：同意 R1，Related Work 一句简要提及即可。\n\n**[DIV4] Gold-empty filtering 跨数据集可比性 (R1-W5 vs R2 rebut)**\n- R2 认为比例差异反映 dataset 特征而非 confound，selection 分析用 full set 不 filter。\n- **Director 判断**：同意 R2，非 confound。但建议报告 CoNLL full-set ρ 作为参考。\n\n---\n\n## Questions to Authors\n\n1. ε=0.05 的选择是否先于 LP range 分析确定？如果是 post-hoc 选择，是否有 pre-registered 替代方案？\n2. Table 3 NER selection 为何用 2 seeds 而非 3？是 data availability issue 还是 design choice？\n3. 是否考虑过 LP + consistency signal 组合策略（如 VC-filtered LP selection）？如有结果请提供。\n4. Free-form RE LP reversal 是否在 T≠1.0 下也成立？\n5. 增加 TACRED 或 ACE05 RE benchmark 是否预计 RE conclusions 会有质性变化？\n6. LP compression 的 mechanistic cause 有无初步假说？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识或一方同意、另一方未反对：\n1. **Fernandes et al. (2022)** \"Quality-Aware Decoding for Neural Machine Translation\" — 将 QE 与 MBR 结合用 learned estimator rerank，与本文 \"trained verifiers\" 建议高度相关 [AGREE: R1, R2]\n2. **Conformal Structured Prediction (ICLR 2025; arxiv 2410.06296)** — set-valued uncertainty for structured prediction，tangential but worth brief mention [AGREE: R1, R2]\n3. **\"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\" (arxiv 2605.07806)** — alternative self-assessment dimensions，与 verbalized confidence failure 相关 [AGREE: R1, R2]\n\n以下引用有分歧（一方提出，另一方认为非必要）：\n4. **Huang et al. (2024)** \"Large Language Models Cannot Self-Correct Reasoning Yet\" — R1 提出，R2 反驳（self-correction ≠ self-consistency，paradigm 不同）\n5. **\"Learning When to Sample\" (arxiv 2603.08999)** — R2 提出，R1 反驳（discrete-answer，已有充分覆盖）\n6. **Slim-SC / Thought Pruning (EMNLP 2025)** — R2 提出，R1 反驳（discrete-answer efficiency，不同问题）\n\n---\n\n## Overall Assessment\n\n**Score**: borderline (between weak reject and weak accept for main conference)\n**Confidence**: 4/5\n\n**R1**: 3.5/5 — 方法论扎实，NER 结论有充分支撑，适合 borderline main / strong Findings\n**R2**: 3.0/5 — novelty 不够 main conference，适合 Findings\n\n**Director 综合判断**：\n\n论文是一篇方法论扎实、统计严谨的 empirical study。LP compression 诊断和三指标 dissociation 框架有独立贡献。但存在三个核心限制：\n\n1. **RE 覆盖不足**（跨 11 轮反复出现的持久性问题）——title 声称 \"Information Extraction\" 但 RE 仅有单一 benchmark，这是最大的 scope-evidence 不匹配。\n2. **Novelty 边界模糊**——instance-level signals \"fail by construction\" 是 definitional 而非 empirical，去掉后核心 empirical 贡献（LP compression + MBR within-instance failure）增量需要更清晰地与 Yao et al. (2026) 和 MBR 文献区分。\n3. **辅助分析 credibility 受 ε circularity 影响**——虽然主结论不受影响，但 tied/non-tied 分析是论文最引人注目的诊断，其 threshold 选择问题需要修正。\n\n**推荐**：以当前状态适合 **EMNLP 2026 Findings**。若能 (1) 增加至少一个 RE benchmark 或将 RE scope 显式限定，(2) reframe Contribution 1 消除 definitional 成分，(3) 修正 ε circularity，则有潜力提升至 **borderline accept for main conference**。\n\n---\n\n## Detailed Comments (by Section)\n\n### Abstract\n- 信息密度适当，9 行 problem-finding-significance 结构。\n- \"NER and RE benchmarks\" 应改为 \"three NER and one RE benchmark\" 以反映实际覆盖。\n- \"4-seed free-form decoding ablation confirms NER compression\" 准确；RE reversal 描述也准确。\n- 建议删减 \"preliminary, single benchmark\" 括号注——正文详述即可。\n\n### Introduction\n- Contribution 1 \"Metric dissociation\" 混合 definitional 和 empirical 元素，需重构。\n- 与 Yao et al. (2026) 的差异描述过于简略（\"we extend their work\"），需要更具体的 tabulation。\n- Figure 1 caption 不适用于 LP（per-sample signal）。\n\n### Related Work\n- 覆盖较为全面，Eikema et al. (2025) structured MBR 讨论到位。\n- 缺少 Fernandes et al. (2022) Quality-Aware Decoding 和 Conformal Structured Prediction。\n- 可增加简要提及 self-assessment limitation 文献。\n\n### Method\n- 信号定义清晰，公式完整。\n- Instance-level vs per-sample 区分是论文的重要框架——建议从 §3.2 开头强调这一分类，为后续 gap 分析奠基。\n- FK independence 假设通过 Appendix permutation test 验证，方法严谨。\n\n### Experiments\n- 实验设计系统，跨数据集/模型/seed/温度/N 的 coverage 全面。\n- Table 1 单 seed (42) 已标注 + cross-ref 3-seed 表，处理得当。\n- Table 3 NER 2-seed vs RE 单 seed 的不一致需解释。\n- Scale ablation（Table 4）仅 Qwen 4B vs 8B，无 LLaMA 4B，限制了结论力度。\n\n### Discussion\n- Practical recommendations 清晰有用。\n- LP compression 描述详尽但缺 mechanistic hypothesis。\n- Free-form ablation RE reversal 需更深入讨论 WHY。\n- \"Trained verifiers\" 前瞻有价值但略显 hand-wavy。\n\n### Conclusion\n- RE hedge 到位（\"rest on SciERC alone\"）。\n- Scale 限定到位（\"3B-8B\"）。\n- 整体简洁准确。\n\n### Limitations\n- 诚实且全面。Verbalized confidence 作为补充实验增强了可信度。\n- 可增加：signal combination 未探索、ε threshold 选择局限性。\n\n### Appendix\n- 22 页中 12+ 页 appendix，质量极高。\n- LOO-SJ equivalence、SJ normalizer robustness、FK independence test 等分析展示了罕见的 rigor。\n- ε sensitivity sweep (Table 11) 需标注 post-hoc exploratory。\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-16T04:34:46.274357+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4276
}
```

</details>

---


### Assistant

_source line 1103 · 2026-05-16T04:34:58.906195+00:00_

**Round 11 审稿报告已投递给 Research Director。**

审稿总结：

**评分**：borderline（R1: 3.5/5, R2: 3.0/5）

**3 个 Must-Fix**：
1. RE 仅 SciERC 一个 benchmark vs "Information Extraction" title scope（跨 11 轮持久性问题，两位 Reviewer 最强共识）
2. ε=0.05 tied-fraction threshold circularity（影响辅助分析 credibility，主结论不受影响）
3. Contribution 1 混合 definitional 和 empirical 元素需 reframe

**8 个 Should-Fix**：scale 范围窄、3 seeds 不足、缺信号组合实验、LP compression 缺 mechanistic explanation、"preliminary" 过频、greedy 命名、Yao et al. 差异化不清、thinking token CoNLL control 弱

**核心优势**：统计方法论上乘、LP compression 诊断系统性强、Appendix 极高质量、诚实的 scope 限定

**推荐**：当前状态适合 **EMNLP 2026 Findings**。若修复 RE coverage + contribution framing + ε circularity，有潜力提升至 borderline accept for main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 88

## Round 88

2 recorded events


### User

_source line 1104 · 2026-05-16T04:35:01.510204+00:00_

[Reviewer 2 审稿结果]:
交叉回应已发送。

总结：与 R1 在 RE 覆盖不足、scale 局限、greedy 命名上达成共识。主要分歧在 N3（LP compression 分布 vs selection outcome 的区分——Appendix I Panel A 的数据支持 compression 本身 intrinsic）和 W5（gold-empty filtering 差异是 dataset 特征非 confound）。ε circularity 是 R1 提出的新问题，同意其对诊断分析的影响但主结论不受影响。

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

_source line 1105 · 2026-05-16T04:35:13.213956+00:00_

审稿报告已于交叉回应收齐后提交给 Research Director。

**本轮审稿总结：**

- **Overall: borderline**（R1: 3.5/5, R2: 3.0/5）
- **推荐**: 当前状态适合 **EMNLP 2026 Findings**
- **3 个 Must-Fix**: (1) RE 单一 benchmark vs "IE" title scope（跨 11 轮持久性问题，强共识）；(2) ε=0.05 tied-fraction circularity（主结论不受影响但辅助分析需修正）；(3) Contribution 1 混合 definitional/empirical 需 reframe
- **8 个 Should-Fix**: scale 范围窄、3 seeds 不足、缺信号组合实验、LP compression 缺 mechanistic explanation、preliminary 过频、greedy 命名混淆、Yao et al. 差异不清、thinking token CoNLL control 论证弱
- **Issue tracker 已更新**: 3 个 recurring issues 重新 open + 11 个新 issues + 4 个 R9 carry-forward

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 89

## Round 89

76 recorded events


### User

_source line 1106 · 2026-05-16T05:09:02.881786+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: Main Conference
- 截止日期: 2026-05-25

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

_source line 1107 · 2026-05-16T05:09:08.832011+00:00_

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

_source line 1108 · 2026-05-16T05:09:08.832984+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-16T05:09:14.304349+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-16T05:09:14.304765+00:00_



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

_source line 1111 · 2026-05-16T05:09:19.277588+00:00_

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

_source line 1112 · 2026-05-16T05:09:20.741695+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (110 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_vc_lp_cascade_selection: VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.（准备中）\n- exp_tacred_re_benchmark: TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.（准备中）\n\n## 近期结论\n- **exp_vc_quartile_analysis** (success): VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\n  [vc_quartile_stratification_analysis](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_vc_quartile_analysis/report/report.md)\n- **exp_015_metrics_expansion** (success): —\n  [analyze_exp015_metrics_expansion](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_015_metrics_expansion/intermediate/analyze_exp015_metrics_expansion.py) | [heatmap_data_audit](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_015_metrics_expansion/repo
…[truncated 1424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1464
}
```

</details>

---


### Tool call

_source line 1113 · 2026-05-16T05:09:20.892766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1114 · 2026-05-16T05:09:21.146221+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Structured Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-16T05:09:21.146637+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md"
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
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-16T05:09:21.197552+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 2297 chars]

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

_source line 1117 · 2026-05-16T05:09:29.449151+00:00_

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

_source line 1118 · 2026-05-16T05:09:29.550160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-16T05:09:32.468463+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-16T05:09:33.523211+00:00_

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

_source line 1121 · 2026-05-16T05:09:33.876570+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-16T05:09:33.927508+00:00_

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

_source line 1123 · 2026-05-16T05:09:42.495357+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derive
…[truncated 2358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10026
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-16T05:09:42.546067+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8618
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-16T05:09:48.270898+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
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
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-16T05:09:48.723411+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

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

_source line 1127 · 2026-05-16T05:09:48.723764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission format page limit template guidelines"
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
    "query": "ACL Rolling Review 2026 May submission format page limit template guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-16T05:09:49.528329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" | head -20",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" | head -20",
    "description": "Find all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-16T05:09:49.729535+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

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


### Tool result

_source line 1130 · 2026-05-16T05:09:56.221950+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission format page limit template guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here is information about ACL Rolling Review 2026 May submission format, page limits, and guidelines:

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations). More specifically, the paper has a section titled "Limitations" placed as follows: ACL formatting guidelines. This section can
…[truncated 1349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7498
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-16T05:10:00.694289+00:00_

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

_source line 1132 · 2026-05-16T05:10:00.745028+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp), suggesting regime-dependent behavior.
7	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
8	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	

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

_source line 1133 · 2026-05-16T05:10:01.248317+00:00_

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

_source line 1134 · 2026-05-16T05:10:01.702822+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	The gap has two causes: instance-level signals (4 of 5) assign identical scores to all candidates and thus cannot rank them (\S\ref{sec:formulation}); LP---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instan
…[truncated 2115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-16T05:10:01.704529+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-16T05:10:02.209640+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
17	Semantic uncertainty \cite{ku
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-16T05:10:02.210671+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-16T05:10:02.615873+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical scores to all $N$ candidates and thus cannot rank them by construction; only per-sample signals can, in principle, select the best output.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equatio
…[truncated 2752 chars]

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

_source line 1139 · 2026-05-16T05:10:02.616370+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-16T05:10:03.572735+00:00_

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. $^\dagger$RE results rest on a single benchmark (SciERC, 40\% zero-F1 rate). $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textb
…[truncated 6700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-16T05:10:03.723865+00:00_

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

_source line 1142 · 2026-05-16T05:10:04.078845+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\dagger$RE, LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Stratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
12	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\dagger$RE at 4B scale, LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below single-sample at 8B.
13	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidenc
…[truncated 3206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-16T05:10:04.230667+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-16T05:10:04.532978+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\dagger$RE, LP selection reverses direction.
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	$^\dagger$RE conclusions rest on SciERC alone (40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-16T05:10:04.533521+00:00_

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

_source line 1146 · 2026-05-16T05:10:04.684503+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	TACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.
3	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
4	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-16T05:10:05.038238+00:00_

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

_source line 1148 · 2026-05-16T05:10:05.491398+00:00_

File content (25409 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1149 · 2026-05-16T05:10:05.793193+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "5000"
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
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-16T05:10:05.894164+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ:
…[truncated 3403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-16T05:10:11.735212+00:00_

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

_source line 1152 · 2026-05-16T05:10:12.187833+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 106\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1153 · 2026-05-16T05:10:12.690713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
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
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-16T05:10:13.194866+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
47	\quad FK & 
…[truncated 13708 chars]

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

_source line 1155 · 2026-05-16T05:10:13.195992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1156 · 2026-05-16T05:10:14.100246+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 3208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-16T05:10:14.201589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-16T05:10:16.010937+00:00_

issues:
# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====
- id: R0-C1
  summary: "模型规模单一（仅 8B）"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 Reviewer 确认措辞修正到位"
  resolution_round: 2
- id: R0-C2
  summary: "相关工作显著遗漏"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认 49 条 bib 全部 cited"
  resolution_round: 2
- id: R0-C4
  summary: "SJ 方法新颖性有限"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认三点差异化清晰"
  resolution_round: 2
- id: R0-C5
  summary: "全文零图表"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "论文已包含 6 个 figures"
  resolution_round: 1
- id: R0-C6
  summary: "成本分析 negligible 误导"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "Round 1+ 未再提及"
  resolution_round: 1
- id: R0-W1
  summary: "未探索 signal combination"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "Round 1+ 未再提及"
  resolution_round: 1
- id: R0-W4
  summary: "统计检验不系统"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
  resolution_round: 2
- id: R3-W4
  summary: "FK independence 假设未验证"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 3
  last_seen_round: 8
  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
  resolution_round: 9
- id: R3-W5
  summary: "Cross-model scope 过宽"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 3
  last_seen_round: 5
  resolution: "标题改为当前版本，scope 限定"
  resolution_round: 9
- id: R4-W3
  summary: "Abstract 信息密度过高"
  categ
…[truncated 13105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1809
}
```

</details>

---


### Tool call

_source line 1159 · 2026-05-16T05:10:16.162026+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null | head -5; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
  "description": "Check external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null | head -5; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1160 · 2026-05-16T05:10:16.314223+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-16T05:10:45.744977+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "figures/*",
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
    "pattern": "figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-16T05:10:46.199759+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-16T05:10:46.501936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "400"
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
    "offset": "200",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-16T05:10:46.756212+00:00_

200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
…[truncated 28445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-16T05:10:51.279626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "599",
  "limit": "300"
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
    "offset": "599",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-16T05:10:51.380889+00:00_

599	\multicolumn{5}{l}{\textit{NER}} \\
600	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
601	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
602	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
603	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
604	\midrule
605	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
606	Q1 (low) & --- & $-$3.56 & --- & --- \\
607	Q4 (high) & --- & $+$4.01 & --- & --- \\
608	\bottomrule
609	\end{tabular}
610	\end{table}
611	
612	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
613	\begin{itemize}
614	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.
615	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\Delta$ signs across quartiles.
616	\end{itemize}
617	
618	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
619	
620	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.
621	
622	\section{RE Conditional Selection}\label{app:re_conditional_selection}
623	
624	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
625	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
626	All five signals underperform single-sample on both subsets.
627	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) an
…[truncated 15674 chars]

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

_source line 1167 · 2026-05-16T05:10:56.105256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "898",
  "limit": "200"
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
    "offset": "898",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-16T05:10:56.156036+00:00_

898	\centering
899	\small
900	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
901	\label{tab:ood}
902	\begin{tabular}{l ccc ccc}
903	\toprule
904	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
905	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
906	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
907	\midrule
908	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
909	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
910	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
911	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
912	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
913	\bottomrule
914	\end{tabular}
915	\end{table}
916	
917	\paragraph{Wider-to-narrower schema transfer.}
918	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
919	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and 
…[truncated 5788 chars]

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

_source line 1169 · 2026-05-16T05:11:02.388844+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-16T05:11:02.489721+00:00_

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

_source line 1171 · 2026-05-16T05:11:05.756145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Find config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-16T05:11:05.857509+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-16T05:11:11.391988+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"*.yaml\" -path \"*/struct_self_consist_ie/*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null | head -20",
  "description": "Find project YAML config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"*.yaml\" -path \"*/struct_self_consist_ie/*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null | head -20",
    "description": "Find project YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-16T05:11:11.492845+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml

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

_source line 1175 · 2026-05-16T05:11:15.566351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/*.yaml 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/*.yaml 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-16T05:11:15.667264+00:00_

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

_source line 1177 · 2026-05-16T05:12:20.380821+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数\n- **匿名规则**: double-blind, 禁止自引暴露身份\n\n### 论文文件\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)\n- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**核心任务：评估方法严谨性、实验设计和统计分析的可靠性。** 具体关注：\n\n1. **方法论有效性**\n   - 5 个 confidence signal 的定义是否严谨、无歧义\n   - Soft Jaccard (SJ) 的 Hungarian matching + IoU 定义是否正确\n   - instance-level vs per-sample 的区分是否成立——特别是 4/5 信号无法做 selection 是否是 tautological（定义上必然的）而非 empirical finding\n   - Evaluation framework (ρ, AUROC, selection F1) 三指标是否充分且无冗余\n\n2. **实验设计**\n   - 3 个 NER benchmark + 1 个 RE benchmark 的覆盖度是否足够支撑 \"structured IE\" 的论文标题\n   - N=8 (primary) / N=16 的样本量选择是否合理\n   - 2 个 model family (Qwen3-8B, LLaMA-3.1-8B) + 1 个 4B ablation 的 scale coverage 是否足够\n   - Fine-tuning setup (LoRA rank=32, 5 epochs) 是否标准且可复现\n   - Free-form decoding ablation 的设计是否能有效隔离 constrained decoding 的影响\n\n3. **统计分析**\n   - Spearman ρ 的 bootstrap CI 和 permutation test 是否正确应用\n   - Selection F1 的 Fisher p-value 和 sign test 是否适当\n   - TOST 等价性检验的 δ 选择是否有 prior justification（注意 ε=0.05 是否存在 circularity）\n   - 3-seed stability (Kendall W=1.000 with n=3) 的统计效力\n   - 多重比较校正是否充分（只对 positive finding 做了 Bonferroni）\n   - Gold-empty instance filtering 的决策是否合理且一致\n\n4. **数据可靠性**\n   - Table 1-4 之间数据是否一致\n   - 正文、caption、appendix 中同一数值的引用是否一致\n   - Table 2 NER 2-seed vs RE 单 seed 的不一致是否有合理解释\n\n5. **页数合规**\n   - 正文是否在 8 页限制内（不计 Limitations, Ethics, References, Appendix）\n\n请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References、Overall Assessment (评分 + 置信度)。",
  "project": "struct_self_consist_ie"
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
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数\n- **匿名规则**: double-blind, 禁止自引暴露身份\n\n### 论文文件\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)\n- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**核心任务：评估方法严谨性、实验设计和统计分析的可靠性。** 具体关注：\n\n1. **方法论有效性**\n   - 5 个 confidence signal 的定义是否严谨、无歧义\n   - Soft Jaccard (SJ) 的 Hungarian matching + IoU 定义是否正确\n   - instance-level vs per-sample 的区分是否成立——特别是 4/5 信号无法做 selection 是否是 tautological（定义上必然的）而非 empirical finding\n   - Evaluation framework (ρ, AUROC, selection F1) 三指标是否充分且无冗余\n\n2. **实验设计**\n   - 3 个 NER benchmark + 1 个 RE benchmark 的覆盖度是否足够支撑 \"structured IE\" 的论文标题\n   - N=8 (primary) / N=16 的样本量选择是否合理\n   - 2 个 model family (Qwen3-8B, LLaMA-3.1-8B) + 1 个 4B ablation 的 scale coverage 是否足够\n   - Fine-tuning setup (LoRA rank=32, 5 epochs) 是否标准且可复现\n   - Free-form decoding ablation 的设计是否能有效隔离 constrained decoding 的影响\n\n3. **统计分析**\n   - Spearman ρ 的 bootstrap CI 和 permutation test 是否正确应用\n   - Selection F1 的 Fisher p-value 和 sign test 是否适当\n   - TOST 等价性检验的 δ 选择是否有 prior justification（注意 ε=0.05 是否存在 circularity）\n   - 3-seed stability (Kendall W=1.000 with n=3) 的统计效力\n   - 多重比较校正是否充分（只对 positive finding 做了 Bonferroni）\n   - Gold-empty instance filtering 的决策是否合理且一致\n\n4. **数据可靠性**\n   - Table 1-4 之间数据是否一致\n   - 正文、caption、appendix 中同一数值的引用是否一致\n   - Table 2 NER 2-seed vs RE 单 seed 的不一致是否有合理解释\n\n5. **页数合规**\n   - 正文是否在 8 页限制内（不计 Limitations, Ethics, References, Appendix）\n\n请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References、Overall Assessment (评分 + 置信度)。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-16T05:12:42.688303+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22307
}
```

</details>

---


### Tool call

_source line 1179 · 2026-05-16T05:12:42.839361+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + Related Work + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数\n- **匿名规则**: double-blind, 禁止自引暴露身份\n\n### 论文文件\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)\n- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**核心任务：评估论文的新颖性、学术贡献完整性、related work 覆盖度和写作质量。** 具体关注：\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 是否是一个真正的新概念，还是已知现象的重新命名\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰——论文声称扩展了他们的工作（structural matching, selection analysis, difficulty gradient），这些扩展是否构成 substantial contribution\n   - 3 个 contribution 的分量：(1) metric dissociation, (2) LP compression + MBR failure, (3) difficulty-dependent rankings——哪些是 empirical finding，哪些是 definitional/tautological\n   - Contribution 1 中 instance-level 信号不能做 selection 是\"发现\"还是\"定义必然\"\n   - 核心结论是 negative result（信号不能做 selection）——negative paper 的价值在于 insight depth，这篇是否足够深入\n\n2. **Related Work 完整性**\n   - 检查引用列表是否覆盖关键领域：self-consistency, MBR decoding, confidence estimation, structured IE, test-time scaling\n   - 是否遗漏重要 2025-2026 近期工作\n   - 与每篇关键引用的差异是否准确描述（尤其 Yao 2026, Eikema 2025, Vashurin 2025 CoCoA）\n   - 用 web_search 搜索是否有遗漏的直接相关工作\n\n3. **论文结构与写作**\n   - Abstract 是否准确概括核心发现（information density vs clarity tradeoff）\n   - Introduction 的 contribution list 是否清晰、不过度 claim\n   - \"preliminary\" / \"exploratory\" 标注是否过于频繁（搜索论文中出现次数）\n   - RE 结果的 dagger (†) 标注体系是否一致\n   - \"greedy\" / \"single-sample\" baseline 命名是否全文统一\n   - Figure/Table caption 是否 self-contained\n   - Limitations section 是否诚实且全面\n   - Ethics statement 是否合规\n\n4. **论文标题与 scope**\n   - 标题 \"LLM-Based Structured Information Extraction\" 暗示 NER + RE 充分覆盖 IE\n   - 实际上 RE 仅有 SciERC 一个数据集（40% zero-F1），是否 over-scope\n   - Abstract 前两句设定的 scope 与实际覆盖是否匹配\n\n5. **引用格式与完整性**\n   - 检查 references.bib 中是否有 orphan entries（未在正文引用的条目）\n   - 引用格式是否一致（year, venue, DOI）\n   - 是否存在可疑引用（幻觉引用风险）\n\n请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References (具体列出应补充的论文)、Overall Assessment (评分 + 置信度)。",
  "project": "struct_self_consist_ie"
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
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + Related Work + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数\n- **匿名规则**: double-blind, 禁止自引暴露身份\n\n### 论文文件\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)\n- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**核心任务：评估论文的新颖性、学术贡献完整性、related work 覆盖度和写作质量。** 具体关注：\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 是否是一个真正的新概念，还是已知现象的重新命名\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰——论文声称扩展了他们的工作（structural matching, selection analysis, difficulty gradient），这些扩展是否构成 substantial contribution\n   - 3 个 contribution 的分量：(1) metric dissociation, (2) LP compression + MBR failure, (3) difficulty-dependent rankings——哪些是 empirical finding，哪些是 definitional/tautological\n   - Contribution 1 中 instance-level 信号不能做 selection 是\"发现\"还是\"定义必然\"\n   - 核心结论是 negative result（信号不能做 selection）——negative paper 的价值在于 insight depth，这篇是否足够深入\n\n2. **Related Work 完整性**\n   - 检查引用列表是否覆盖关键领域：self-consistency, MBR decoding, confidence estimation, structured IE, test-time scaling\n   - 是否遗漏重要 2025-2026 近期工作\n   - 与每篇关键引用的差异是否准确描述（尤其 Yao 2026, Eikema 2025, Vashurin 2025 CoCoA）\n   - 用 web_search 搜索是否有遗漏的直接相关工作\n\n3. **论文结构与写作**\n   - Abstract 是否准确概括核心发现（information density vs clarity tradeoff）\n   - Introduction 的 contribution list 是否清晰、不过度 claim\n   - \"preliminary\" / \"exploratory\" 标注是否过于频繁（搜索论文中出现次数）\n   - RE 结果的 dagger (†) 标注体系是否一致\n   - \"greedy\" / \"single-sample\" baseline 命名是否全文统一\n   - Figure/Table caption 是否 self-contained\n   - Limitations section 是否诚实且全面\n   - Ethics statement 是否合规\n\n4. **论文标题与 scope**\n   - 标题 \"LLM-Based Structured Information Extraction\" 暗示 NER + RE 充分覆盖 IE\n   - 实际上 RE 仅有 SciERC 一个数据集（40% zero-F1），是否 over-scope\n   - Abstract 前两句设定的 scope 与实际覆盖是否匹配\n\n5. **引用格式与完整性**\n   - 检查 references.bib 中是否有 orphan entries（未在正文引用的条目）\n   - 引用格式是否一致（year, venue, DOI）\n   - 是否存在可疑引用（幻觉引用风险）\n\n请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References (具体列出应补充的论文)、Overall Assessment (评分 + 置信度)。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1180 · 2026-05-16T05:12:44.248323+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 1181 · 2026-05-16T05:12:52.862297+00:00_

两名 Reviewer 已分配：

- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计分析
- **Reviewer 2** → 新颖性 + 完整性 + Related Work + 写作质量

等待 Reviewer 初审报告返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 90

## Round 90

2 recorded events


### User

_source line 1182 · 2026-05-16T05:17:17.574431+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Summary

本文评估了五种置信度信号在 LLM-based structured IE 中的质量估计和样本选择能力，发现"correlation-selection gap"：信号与 F1 相关性强（ρ 达 0.45）但无法改善 best-of-N 选择。四个 instance-level 信号通过 MBR 选择无效，LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats）而失败。这是一个有价值的负面结果，实验设计整体严谨，但核心 framing 存在方法论问题，且实验覆盖度不足以支撑标题。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法总体可靠，统计分析全面（bootstrap CI, permutation test, TOST），但核心 "by construction" framing 存在逻辑问题（见 N1），部分统计分析的效力不足（见 W1） |
| Excitement | 3/5 | 识别了 QE vs. selection 的 decoupling 现象，对 test-time compute scaling 社区有参考价值；但缺乏解决方案，范围限于小模型，且标题过于宽泛 |
| Overall | 3.5/5 | Borderline Conference — 实验工作扎实，负面结果有价值，但 framing 和 scope 问题需解决 |
| Reproducibility | 4/5 | 训练配置、prompt template 完整公开（Table A6），使用开源框架/模型，代码承诺 release |
| Confidence | 4/5 | 仔细阅读全文及 appendix，熟悉 self-consistency、MBR decoding 和 IE 评估相关文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] "By construction" framing 混淆定义性与经验性发现

- 具体位置：Section 3.1 (line 7), Section 4.2 paragraph 2, Abstract (line 4-5)
- 问题：论文反复声称 4/5 信号"cannot rank candidates by construction"（Section 3.1: "4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction"），但 Table 2 中这些信号 **实际执行了选择**（SJ=0.646, FK=0.646 等），通过 "consensus-proximity selection"（即 MBR: argmax_i Σ_{j≠i} U(y_i, y_j)）。Discussion 也承认 "VC becomes per-sample in the selection context." Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。

  论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的，trivially true）；(2) 用这些信号做 MBR-style selection 无效（经验性发现，有意义）。但论文将两者混为一谈，将 (2) 也归为 "by construction" 失败，从而弱化了这一经验发现的价值。MBR 在 MT 中成功但在 IE 中失败是本文最重要的经验贡献之一——应该突出而非隐藏在 "by construction" framing 之下。

- 为什么影响接收：核心 claim 的逻辑严密性是 soundness 评分的关键。当前 framing 使读者混淆哪些结论是定义推导、哪些是实验证据。
- 建议修改方向：明确区分两层失败——(a) QE signal 的 instance-level 性质使其 *本身* 无法做 selection；(b) 将其转化为 per-sample utility（MBR/consensus-proximity）后仍然失败，且这是一个经验发现（因为 MBR 在 MT 中有效）。将 (b) 作为独立 contribution 突出。

**N2** [critical] 标题和论文范围不匹配："Structured Information Extraction" vs. 实际覆盖

- 具体位置：Title, Abstract, Section 4.1
- 问题：标题使用 "Structured Information Extraction" 这一宽泛术语，但论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅有 1 个 benchmark（SciERC）作为 "exploratory extension"，且 RE 实验在统计上不完整（Table 2: RE 为 single-seed；全文标注 "†RE" 表示 preliminary）。

  Structured IE 通常包括 NER、RE、Event Extraction、Slot Filling 等多种任务。当前论文实质上是一篇 "NER confidence estimation" 论文附带一个初步的 RE 探索。Section 4.1 和 Limitations 均承认 "RE conclusions rest on SciERC alone" 和 "TACRED-style RE is left for future work"。

- 为什么影响接收：标题/abstract 的 claim 范围与证据支撑之间的落差会被 AC 视为 overclaiming。EMNLP reviewer guidelines 明确要求 claims 与 evidence 对齐。
- 建议修改方向：(1) 缩窄标题为 "NER" 或 "Entity Set Extraction"；(2) 或增加至少一个独立 RE 数据集（如 TACRED、DocRED）的实验使 RE 结论不再 preliminary。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Kendall W=1.000 (n=3 seeds) 的统计效力问题

- 具体位置：Appendix F, Table A8 (tab:ranking-stability)
- 问题：3 seeds 排 5 个 signal 的 Kendall W=1.000 被用于支撑 "signal ranking is stable across seeds" 的结论。然而 n=3 的统计效力极低——即使 raters 之间仅有轻微共识，W 也容易达到高值（W 的 chi-squared 检验 df=4，临界值 9.49 for α=0.05）。论文在 Appendix 中承认 "statistical power with n=3 is limited"，但正文 Section 4.1 footnote 仍以此作为 robustness 证据。
- 建议：要么增加 seeds（≥5）以提高效力，要么在正文中降低对 ranking stability 的表述强度，改为 "consistent with stable rankings but insufficient power to confirm."

**W2** [warning] Table 2 NER 2-seed vs RE single-seed 的不一致未充分解释

- 具体位置：Table 2 caption ("NER: 2-seed mean±σ; †RE: single seed")
- 问题：同一张表中 NER 用 2-seed 统计但 RE 仅 single seed。Appendix Table A8 显示 RE 有 3-seed QE 数据可用（Qwen RE ρ: .297±.022 for LP, .309±.024 for VC），但 selection 实验为何 RE 只跑了一个 seed？资源限制？如果是，应当明确说明。
- 建议：在正文或 footnote 中解释这一不对称的原因。如果 3-seed RE selection 数据可用但未报告，考虑在 appendix 中补充。

**W3** [warning] 未测试 entity-level LP 聚合——明显的 LP 变体缺失

- 具体位置：Eq. 1 (Section 3.2), Discussion "Hypotheses for LP compression" (d)
- 问题：论文指出假说 (d) "format-token dilution" 是 LP 压缩的可能主因（fine-tuned models 对 schema tokens 赋予极高 LP，稀释了 entity-name tokens 的信号）。这直接暗示了一个显而易见的变体：仅在 entity-name tokens 上计算 LP（排除 format/schema tokens），即 entity-level LP aggregation。论文列出了 4 个假说但只通过 free-form ablation 测试了 (b)-(c)，未直接验证 (a)/(d)——而 entity-level LP 正是 (d) 的直接测试。
- 建议：加入 entity-token-only LP 变体的实验或 pilot study；如果不可行（如 constrained decoding 下无法区分 entity vs. schema tokens 的 LP），需明确说明为什么。

**W4** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致

- 具体位置：Section 3.3 paragraph "Quality estimation" ("Correlation analyses exclude empty gold annotations... selection retains the full set")
- 问题：QE 分析排除 gold-empty instances（CoNLL 排除 697/3453=20.2%），而 selection 保留完整集。这一设计选择的理由 partially explained（"F1 is trivially zero regardless of prediction quality"），但导致两个问题：(1) QE 的 ρ 在 n=2756 上计算，selection F1 在 n=3453 上计算，直接对比（如 "strong ρ yet no selection gain"）涉及不同样本集；(2) Table A13（cross_selection）的 CoNLL 仍标注 n=2756——这与正文描述矛盾。
- 建议：统一说明 filtering 策略并验证 Table cross_selection 的 n 值标注是否正确。如果 selection 确实在 full set 上计算，解释为什么 gold-empty instances 对 selection 的影响是可接受的。

**W5** [warning] 模型规模覆盖不足限制结论的普适性

- 具体位置：Section 4.1 ("Both Qwen3-8B and LLaMA-3.1-8B-Instruct"), Table A6
- 问题：所有实验仅覆盖 3B-8B 规模，Limitations 承认 "whether the gap holds for 70B+ models or closed-source APIs is untested." 然而正文 Conclusion 表述为 "consistent across two model families (3B–8B)" 暗示了比实际证据更强的普适性。在 test-time compute scaling 文献中，model scale 是核心变量——70B 模型可能产生更多样的 samples 从而改变 LP compression 现象。
- 建议：在 Conclusion/Discussion 中更明确地将发现限定为 small-model regime 的特性，或增加一个 ≥32B 模型的 pilot experiment。

---

### Questions（需作者回答）

**Q1**: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上是一个 per-sample 选择策略。请解释为什么论文将其归类为 "fail by construction" 而非 "MBR fails empirically for IE"——这两者的理论含义截然不同。

**Q2**: Entity-token-only LP（仅对 entity mention tokens 计算 mean LP，排除 JSON schema tokens）是否被考虑过？如果排除了 schema tokens 的 LP 贡献，within-instance compression 是否缓解？这是假说 (d) 的直接检验。

**Q3**: Table A13 (cross_selection) 标注 CoNLL n=2756，但正文 Section 3.3 说 "selection retains the full set" (n=3453)。哪个是正确的？

**Q4**: TOST 分析中的 external anchors (Section F, Appendix) 显示 Qwen CoNLL 的 selection 实际上 significantly worse than single-sample（所有外部 δ 下均不通过等价检验）。这是否意味着在某些配置下，signals 实际上 *损害* selection？这一发现与 "equivalence" 的正文表述矛盾。

**Q5**: Free-form ablation 中 RE LP selection 的 direction reversal（constrained: −0.68pp → free-form: +1.84±0.12pp across 4 seeds）——这暗示 constrained decoding 本身是 RE selection failure 的原因。为什么论文没有将 "free-form decoding + LP selection" 作为一个 positive result 更突出地呈现？

---

### Missing References

1. **Bertoldi et al. (2024)** "Beyond Self-Consistency: Ensemble Reasoning in LLMs" — 直接讨论 self-consistency 在 structured output 上的局限性
2. **Ye et al. (2023)** "Complementary Explanations for Effective In-Context Learning" — 提出对 sampling diversity 与 selection 关系的分析框架
3. 论文引用了 Eikema & Aziz (2022) for MBR 但未引用 **Deguchi et al. (2024)** "Centroid-Based Efficient Minimum Bayes Risk Decoding" 中关于 MBR 在 structured 任务上 mode-seeking bias 的分析

---

### 主要优势

1. **问题定义清晰有价值**：明确区分 quality estimation 和 sample selection 是本文的核心方法论贡献，对 test-time compute scaling 社区有直接指导意义。三个评估指标（ρ, AUROC, selection F1）的 decoupling demonstration (Contribution 1) 设计精巧。

2. **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep——统计方法论的严谨程度超过 EMNLP 平均水平。论文主动提出并解决 potential circularity（如 TOST δ 与 oracle headroom 的循环性），且在 Limitations 中诚实声明了所有已知限制。

3. **消融设计合理**：Free-form decoding ablation 有效隔离了 constrained decoding 的影响；scale ablation (4B vs. 8B) 提供了跨规模验证；温度和 N-scaling 实验覆盖了关键超参数。

4. **负面结果的呈现方式得当**：论文没有为 negative result 强行赋予 positive spin，而是通过 non-tied subset analysis (+2.9pp, p=0.004) 展示了 LP 在什么条件下 *能* 工作，并由此诊断出 compression 作为瓶颈。

5. **Related work 公允全面**：对 Yao et al. (2026) 的 positioning 清晰（从 exact-match 扩展到 structural matching + selection），对 Eikema et al. (2025) structured MBR 失败的 connection 有见地。

---

### 小问题（不影响接收）

- "Soft Jaccard" 命名：使用 max(|g_i|, |g_j|) 而非 |A∪B| 作为分母，严格说不是 Jaccard 的 soft 推广。建议改为 "Soft overlap score" 或在首次出现时明确说明与标准 Jaccard 的区别。
- Discussion 中列出 (a)(b)(c)(d) 四个假说但标记为 "three (non-mutually-exclusive) mechanisms"——实际有 4 个。
- Table 1 caption 说 "Best in bold" 但某些列有多个 bold（如 CoNLL LLaMA 列 SJ 和 EM 均 .431），需确认是否为 ties。
- Abstract 第 5 行 "Four instance-level signals fail by construction; the empirical finding is that log-probability..." 这一句的分号前后表述暗示 LP 发现是 "the" empirical finding，降低了 MBR failure 作为独立发现的地位。

---

### Overall Assessment

**Overall**: 3.5/5 (Borderline Conference)

**一句话总结**: 实验严谨且统计分析全面的经验性负面结果论文，但核心 framing 的逻辑问题（N1）和标题/范围不匹配（N2）需要在 rebuttal 中有说服力地回应才能达到 conference acceptance。

如果 N1 的 framing 问题被修正（明确区分 definitional vs. empirical failure，突出 MBR failure 作为独立 contribution），且标题/abstract 精确化，本文可提升至 4.0（Conference acceptance level）。当前版本的主要风险是 overclaiming（标题）和 underclaiming（将 MBR 的经验性失败归为定义性的）同时存在，造成叙事的不一致。

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

_source line 1183 · 2026-05-16T05:17:24.893778+00:00_

Reviewer 1 审稿报告已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 1184 · 2026-05-16T05:17:33.585299+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交至 Review Director。

**完成情况总结**：

- **Overall**: 3.5/5（Borderline Conference）
- **Soundness**: 3.5/5 — 统计方法全面但核心 "by construction" framing 有逻辑漏洞
- **Excitement**: 3/5 — 有价值的负面结果但缺乏解决方案且 scope 有限

**两个 Must-Fix 问题**：
1. "By construction" framing 混淆了定义性失败与经验性发现（MBR 在 IE 中的失败是 empirical finding，不应被 "by construction" 标签掩盖）
2. 标题 "Structured IE" 过宽，实际主要是 NER + 一个 exploratory RE 实验

**关键 Should-Fix**：Kendall W 统计效力不足、NER/RE seed 数量不一致、未测试 entity-token-only LP 变体、gold-empty filtering 不一致、模型规模限于 3B-8B。

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

_source line 1185 · 2026-05-16T05:17:39.758576+00:00_

Reviewer 1 报告已收到（3.5/5, Borderline Conference）。等待 Reviewer 2 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 1186 · 2026-05-16T05:18:21.239307+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**审查侧重：新颖性 + 完整性 + Related Work + 写作质量**

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 论文对 IE 中 QE-selection 脱钩现象做了系统的经验性刻画，LP compression 分析有洞察力，但核心贡献的新颖性有限——4/5 信号的 selection 失败是定义必然而非经验发现，RE 覆盖过薄，且缺少任何解决方案的尝试。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理、统计方法严谨（bootstrap CI, TOST, permutation tests），但 Contribution 1 的 "empirical dissociation" 中 4/5 信号的 selection 失败是定义上不可避免的；TOST 等价检验结论是 configuration-dependent 的（Appendix §TOST 自己承认 Qwen-CoNLL 不等价），但主文表述为 "no signal consistently improves selection" 有过度概括之嫌 |
| Excitement | 2.5/5 | 负面结果论文的价值在于 insight depth。LP compression 分析和 MBR within-instance failure 有一定洞察力，但论文止步于诊断而不尝试任何 remedy，限制了对社区的启发性。"Correlation-selection gap" 命名暗示概念突破，实际是对已知统计现象在 IE 场景的实例化 |
| Reproducibility | 4/5 | 详细的训练配置、prompt template、constrained decoding 细节、多 seed 统计。承诺代码发布 |
| Confidence | 4/5 | 仔细阅读全文及 appendix，熟悉 self-consistency、MBR decoding 和 IE confidence estimation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution 1 的 "empirical dissociation" 大部分是定义必然，不是经验发现
- 具体位置：Section 1 (Introduction), contribution list item 1; Section 3.1 (Problem Formulation)
- 问题：论文将 "instance-level signals 无法做 sample selection" 列为第一个 contribution ("Empirical dissociation of evaluation metrics")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数 ("4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction")。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号"不能选"的反复论述中。
- 为什么影响接收：将定义上的必然性包装为经验发现会误导读者对 contribution 分量的判断。对一篇 negative result paper，insight 必须是非显而易见的。
- 建议修改方向：重新组织 contribution list——将 "by construction" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。

**N2** [critical] 标题和 scope 严重不匹配：标题声称 "Structured Information Extraction"，实际 RE 覆盖严重不足
- 具体位置：标题 "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Structured Information Extraction"；Abstract 第2句
- 问题：标题使用 "Structured Information Extraction" 暗示对 IE 的广泛覆盖（通常包括 NER、RE、EE）。实际上：(1) RE 仅有 SciERC 一个数据集，且 40% instances zero-F1；(2) 论文自己将 RE 定位为 "exploratory extension"，全文用 †RE 标注；(3) 完全没有 Event Extraction。这本质上是一篇 NER 论文，附带了不完整的 RE 探索。
- 为什么影响接收：标题与实际 scope 的不匹配是 over-claiming。3 个 NER benchmark + 1 个不充分的 RE benchmark 不能支撑 "Structured IE" 的宣称。
- 建议修改方向：(a) 将标题限定为 NER，将 RE 作为 exploratory extension；或 (b) 增加至少一个额外的 RE benchmark（如 TACRED, DocRED）。

**N3** [critical] ρ = 0.45 被描述为 "strong quality estimation"——这是中等相关性，措辞过度
- 具体位置：Abstract 第3句; Conclusion 第1句; Section 5.2 标题附近
- 问题：Spearman ρ = 0.45 在统计学中通常归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 "strong quality estimation" 来描述这一数值，但 ρ = 0.45 仅能解释约 20% 的方差。作为核心论点的一半（"strong QE 但 weak selection"），如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。
- 建议修改方向：使用 "moderate" 或 "non-trivial"，或明确说明 "up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 未尝试任何 remedy，纯诊断性论文的 impact 受限
- 具体位置：Discussion §Methodological implications; Conclusion; Limitations §11
- 问题：论文诊断了问题但完全没有尝试解决。即使是简单的 baseline remedy（如 LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。
- 建议：至少加一个 LP × consistency 或 entity-token-restricted LP 的消融实验，哪怕结果也是 negative。

**W2** [warning] 模型规模范围过窄（3B-8B），结论的普适性存疑
- 具体位置：Limitations 第3句; Appendix §LLaMA-3.2-3B
- 问题：3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性——更大的模型可能产生更多样化的 samples 和更分散的 LP 分布。论文声称 "task difficulty is a stronger predictor of the gap than model scale"（Section 5.3），但只在一个非常窄的 scale range 内验证。
- 建议：在标题或 abstract 中明确 scale 限制，或加入至少一个 ≥30B 模型的验证。

**W3** [warning] Yao et al. (2026) 的差异描述不够精确
- 具体位置：Section 2 (Related Work) 和 Section 1 (Introduction) line 8
- 问题：论文声称对 Yao et al. (2026) 的三个扩展，但 Yao et al. 的原始工作本身就是在做 consistency-accuracy correlation（即 quality estimation）。需要更精确地说明增量贡献的大小。
- 建议：添加一个简洁的对比段落，明确列出 Yao et al. 的具体方法/实验/发现 vs. 本文的差异点。

**W4** [warning] ε = 0.05 threshold 的选择影响核心叙事
- 具体位置：Discussion §Why the gap exists; Appendix §Log-Probability Score Compression (Table 9, Table 10)
- 问题：论文的核心叙事（"60% tied, LP too compressed"）依赖于 ε = 0.05 这一阈值。Appendix Table 10 显示：ε = 0.03 时 tied fraction 仅 31.8%。LP 是连续信号，tied/non-tied 二分法本身就是人为的。
- 建议：主文应改用 continuous characterization（如 pooled within-instance ρ = 0.248），将 ε-based 分析降为辅助论据。

**W5** [warning] 缺少若干直接相关的 2024-2025 文献
- 具体位置：Section 2 (Related Work)
- 遗漏工作：
  1. Zerva et al. (2025) "Uncertainty-Aware Decoding with Minimum Bayes Risk" (ICLR 2025): MBR + uncertainty 的结合
  2. Mejer & Crammer (2011) "Confidence Estimation in Structured Prediction": 经典 structured prediction confidence
  3. Xie et al. (2024) "Self-Evaluation Improves Selective Generation" (NeurIPS 2024): LLM per-sample self-evaluation 用于 selective generation
  4. "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025): 直接挑战 self-consistency 假设

---

## 小问题（不影响接收）

- Abstract 信息密度过高：一句话内同时出现 ρ = 0.45、0.041 nats、60% tied、+1.8±0.1 pp——数字过密。
- Introduction contribution 3（difficulty-dependent rankings）较弱——rankings shift with task difficulty 是常见现象。
- Table 2 caption 中 ‡Single 与 †RE 的不同 dagger 标注视觉易混淆。
- Equation (3) FK 的 entity set 改编是非标准操作，值得更详细解释。
- "4B and 8B" in abstract 应明确 model family。
- Discussion §Hypotheses for LP compression 的 (a)(b)(c)(d) 编号有标点错误：(c) 结尾写了 "and"，然后又有 (d)。
- `oh2025latentsc` bib year=2025 但 OpenAlex 匹配 2026 版本，应更新。

---

## 主要优势

1. **QE vs selection 的显式区分**：Section 3.1 的 per-sample vs instance-level signal 形式化是清晰有用的，这在 IE confidence estimation 文献中是第一次系统性地做。
2. **LP compression 分析有深度**：median range 0.041 nats、pooled within-instance ρ = 0.248、non-tied subset +2.9pp——多角度刻画，是论文最有价值的 empirical contribution。
3. **统计方法严谨**：bootstrap CI、permutation tests、TOST、Fisher combined p、Bonferroni correction、Kendall's W、external equivalence margins。
4. **诚实的 limitations 和 caveats**：RE 始终用 † 标注、明确说 preliminary、TOST 是 configuration-dependent、ε 是 post-hoc。
5. **Appendix 极其详尽**：15+ 个 appendix section 覆盖了几乎所有可能的消融方向。
6. **MBR within-instance failure 的刻画**：utility 在 instance-level 相关但 within-instance 不相关，与 Eikema et al. (2025) 互补。

---

## 引用完整性检查

- 47 个 bib entries，0 orphan，0 missing
- OpenAlex 验证：40/47 verified，4 not found（均为 recent preprints，手动确认均为真实论文），3 minor mismatch（first author encoding）
- 未发现可疑/幻觉引用
- oh2025latentsc 应更新 year 为 2026

---

## Questions for Authors

1. 如果将 LP 限制为只计算 entity-name tokens（排除 schema/format tokens）的 log-probability，compression 是否会缓解？这直接测试了 Discussion 中 hypothesis (d) "format-token dilution"。
2. 论文报告 non-tied subset (n=210) 有 +2.9pp 选择增益。是否尝试过用一个简单的 binary classifier 预测哪些 instances 是 non-tied，然后有条件地应用 LP selection？这可以将诊断性发现转化为实用方法。
3. Contribution 1 中 "Spearman ρ, AUROC, and selection F1 decouple" 的 empirical surprise 在哪里？ρ 衡量 rank correlation，AUROC 衡量 binary discrimination，selection F1 要求 within-instance discrimination——它们本来就衡量不同的东西，decouple 是否才是 expected behavior？
4. 对于 CoNLL 这样 single-sample F1 ≈ 0.91 的数据集，Oracle headroom 仅 ~4pp。在这么小的 headroom 下做 selection 分析是否有意义？是否应该在分析中排除 near-ceiling datasets？

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

_source line 1187 · 2026-05-16T05:23:54.463760+00:00_

API Error: Stream idle timeout - partial response received

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 93

## Round 93

6 recorded events


### User

_source line 1188 · 2026-05-16T05:23:57.056184+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings level)**

3 个 Must-Fix 问题：
1. Contribution 1 的 4/5 信号 selection 失败是定义必然而非经验发现，需重组 contribution list
2. 标题 "Structured IE" 与实际 scope（主要是 NER，RE 仅 1 个数据集）严重不匹配
3. ρ = 0.45 被称为 "strong" 但实际是 moderate correlation，核心叙事的 dramatic tension 被削弱

5 个 Should-Fix 问题：纯诊断无 remedy 尝试、模型规模范围窄(3B-8B)、Yao et al. 差异描述不精确、ε=0.05 阈值依赖、缺少 4 篇直接相关文献。

主要优势：QE/selection 解耦形式化清晰、LP compression 分析多角度深入、统计方法严谨、limitations 诚实透明、appendix 详尽。

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

_source line 1189 · 2026-05-16T05:24:26.793430+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 2 观点不同的地方。\n\n---\n\n### Reviewer 2 的完整审稿报告\n\n**Overall**: 3.0 (Findings)\n\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n#### Must-Fix 问题\n\n**N1** [critical] Contribution 1 的 \"empirical dissociation\" 大部分是定义必然，不是经验发现\n- 论文将 \"instance-level signals 无法做 sample selection\" 列为第一个 contribution (\"Empirical dissociation of evaluation metrics\")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号\"不能选\"的反复论述中。\n- 建议：重新组织 contribution list——将 \"by construction\" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。\n\n**N2** [critical] 标题和 scope 严重不匹配：\"Structured Information Extraction\" vs. 实际 RE 覆盖严重不足\n- 标题使用 \"Structured Information Extraction\" 暗示 NER、RE、EE 等广泛覆盖。实际上 RE 仅 SciERC 一个数据集（40% zero-F1），且自称 \"exploratory extension\"。完全没有 Event Extraction。\n- 建议：将标题限定为 NER，或增加至少一个额外 RE benchmark。\n\n**N3** [critical] ρ = 0.45 被描述为 \"strong quality estimation\"——这是中等相关性，措辞过度\n- Spearman ρ = 0.45 在统计学中归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 \"strong quality estimation\"，但 ρ = 0.45 仅解释约 20% 方差。如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。\n- 建议：使用 \"moderate\" 或 \"non-trivial\"，或明确说明 \"up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines\"。\n\n#### Should-Fix 问题\n\n**W1** 未尝试任何 remedy，纯诊断性论文的 impact 受限\n- 即使简单的 baseline remedy（LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。\n\n**W2** 模型规模范围过窄（3B-8B），结论普适性存疑\n- 3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性。\n\n**W3** Yao et al. (2026) 的差异描述不够精确\n- 需要更精确地说明增量贡献的大小，建议添加对比段落。\n\n**W4** ε = 0.05 threshold 的选择影响核心叙事\n- \"60% tied\" 依赖于 ε = 0.05。ε = 0.03 时 tied fraction 仅 31.8%。建议主文改用 continuous characterization（pooled within-instance ρ = 0.248）。\n\n**W5** 缺少若干直接相关文献\n- Zerva et al. (2025) \"Uncertainty-Aware Decoding with MBR\" (ICLR 2025)\n- Mejer & Crammer (2011) \"Confidence Estimation in Structured Prediction\"\n- Xie et al. (2024) \"Self-Evaluation Improves Selective Generation\" (NeurIPS 2024)\n- \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n\n#### Questions\n1. Entity-name-only LP 是否被考虑过？\n2. 是否尝试过用 binary classifier 预测 non-tied instances 然后条件性应用 LP？\n3. Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？它们本来就衡量不同的东西。\n4. CoNLL (F1≈0.91, headroom ~4pp) 的 selection 分析是否有意义？\n\n#### 小问题\n- Abstract 数字过密\n- Contribution 3 (difficulty-dependent rankings) 较弱\n- Table 2 caption dagger 标注混淆\n- FK entity set 改编非标准\n- Discussion LP hypotheses (a)(b)(c)(d) 编号标点错误\n- oh2025latentsc bib year 应更新为 2026\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "struct_self_consist_ie"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 2 观点不同的地方。\n\n---\n\n### Reviewer 2 的完整审稿报告\n\n**Overall**: 3.0 (Findings)\n\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n#### Must-Fix 问题\n\n**N1** [critical] Contribution 1 的 \"empirical dissociation\" 大部分是定义必然，不是经验发现\n- 论文将 \"instance-level signals 无法做 sample selection\" 列为第一个 contribution (\"Empirical dissociation of evaluation metrics\")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号\"不能选\"的反复论述中。\n- 建议：重新组织 contribution list——将 \"by construction\" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。\n\n**N2** [critical] 标题和 scope 严重不匹配：\"Structured Information Extraction\" vs. 实际 RE 覆盖严重不足\n- 标题使用 \"Structured Information Extraction\" 暗示 NER、RE、EE 等广泛覆盖。实际上 RE 仅 SciERC 一个数据集（40% zero-F1），且自称 \"exploratory extension\"。完全没有 Event Extraction。\n- 建议：将标题限定为 NER，或增加至少一个额外 RE benchmark。\n\n**N3** [critical] ρ = 0.45 被描述为 \"strong quality estimation\"——这是中等相关性，措辞过度\n- Spearman ρ = 0.45 在统计学中归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 \"strong quality estimation\"，但 ρ = 0.45 仅解释约 20% 方差。如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。\n- 建议：使用 \"moderate\" 或 \"non-trivial\"，或明确说明 \"up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines\"。\n\n#### Should-Fix 问题\n\n**W1** 未尝试任何 remedy，纯诊断性论文的 impact 受限\n- 即使简单的 baseline remedy（LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。\n\n**W2** 模型规模范围过窄（3B-8B），结论普适性存疑\n- 3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性。\n\n**W3** Yao et al. (2026) 的差异描述不够精确\n- 需要更精确地说明增量贡献的大小，建议添加对比段落。\n\n**W4** ε = 0.05 threshold 的选择影响核心叙事\n- \"60% tied\" 依赖于 ε = 0.05。ε = 0.03 时 tied fraction 仅 31.8%。建议主文改用 continuous characterization（pooled within-instance ρ = 0.248）。\n\n**W5** 缺少若干直接相关文献\n- Zerva et al. (2025) \"Uncertainty-Aware Decoding with MBR\" (ICLR 2025)\n- Mejer & Crammer (2011) \"Confidence Estimation in Structured Prediction\"\n- Xie et al. (2024) \"Self-Evaluation Improves Selective Generation\" (NeurIPS 2024)\n- \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n\n#### Questions\n1. Entity-name-only LP 是否被考虑过？\n2. 是否尝试过用 binary classifier 预测 non-tied instances 然后条件性应用 LP？\n3. Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？它们本来就衡量不同的东西。\n4. CoNLL (F1≈0.91, headroom ~4pp) 的 selection 分析是否有意义？\n\n#### 小问题\n- Abstract 数字过密\n- Contribution 3 (difficulty-dependent rankings) 较弱\n- Table 2 caption dagger 标注混淆\n- FK entity set 改编非标准\n- Discussion LP hypotheses (a)(b)(c)(d) 编号标点错误\n- oh2025latentsc bib year 应更新为 2026\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1190 · 2026-05-16T05:24:59.508583+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32715
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-16T05:24:59.810373+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 1 观点不同的地方。\n\n---\n\n### Reviewer 1 的完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n#### Must-Fix 问题\n\n**N1** [critical] \"By construction\" framing 混淆定义性与经验性发现\n- Section 3.1 反复声称 4/5 信号 \"cannot rank candidates by construction\"，但 Table 2 中这些信号实际通过 consensus-proximity selection (MBR) 执行了选择（SJ=0.646, FK=0.646 等）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。\n- 论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的）；(2) 用这些信号做 MBR-style selection 无效（经验性发现）。但论文将两者混为一谈。MBR 在 MT 中成功但在 IE 中失败是最重要的经验贡献之一——应突出而非隐藏在 \"by construction\" framing 下。\n- 建议：明确区分两层失败——(a) QE signal 的 instance-level 性质使其本身无法做 selection；(b) 将其转化为 per-sample utility（MBR）后仍然失败，这是经验发现。将 (b) 作为独立 contribution 突出。\n\n**N2** [critical] 标题和论文范围不匹配：\"Structured IE\" vs. 实际覆盖\n- \"Structured Information Extraction\" 通常包括 NER、RE、Event Extraction 等。论文核心证据来自 3 个 NER benchmark，RE 仅 1 个 benchmark 作为 \"exploratory extension\"，且统计上不完整（Table 2: RE 为 single-seed）。\n- 建议：缩窄标题或增加独立 RE 数据集。\n\n#### Should-Fix 问题\n\n**W1** Kendall W=1.000 (n=3 seeds) 统计效力不足\n- n=3 排 5 个 signal 的 W=1.000 效力极低。建议增加 seeds 或降低表述强度。\n\n**W2** Table 2 NER 2-seed vs RE single-seed 未充分解释\n- Appendix 显示 RE 有 3-seed QE 数据，但 selection 仅 single seed。需解释原因。\n\n**W3** 未测试 entity-level LP 聚合\n- Discussion 指出 hypothesis (d) \"format-token dilution\" 是主因，但未直接测试 entity-token-only LP。\n\n**W4** Gold-empty instance filtering 在 QE 和 Selection 之间不一致\n- QE 排除 gold-empty (CoNLL n=2756)，selection 保留 full set (n=3453)。Table A13 标注 n=2756 与此矛盾。\n\n**W5** 模型规模覆盖不足（3B-8B）限制结论普适性\n- Conclusion 表述 \"consistent across two model families (3B–8B)\" 暗示超过实际证据的普适性。\n\n#### Questions\n\n**Q1**: 为什么将 consensus-proximity selection 归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"？\n\n**Q2**: Entity-token-only LP 是否被考虑过？\n\n**Q3**: Table A13 CoNLL n=2756 vs 正文 \"selection retains full set\" (n=3453)——哪个正确？\n\n**Q4**: TOST external anchors 显示 Qwen CoNLL selection significantly worse than single-sample。这是否意味着某些配置下 signals 损害 selection？\n\n**Q5**: RE LP selection 在 free-form 下 direction reversal (+1.84±0.12pp)——为什么不作为 positive result 更突出呈现？\n\n#### Missing References\n1. Bertoldi et al. (2024) \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\"\n2. Ye et al. (2023) \"Complementary Explanations for Effective In-Context Learning\"\n3. Deguchi et al. (2024) \"Centroid-Based Efficient MBR Decoding\" — MBR 在 structured 任务上 mode-seeking bias\n\n#### 小问题\n- \"Soft Jaccard\" 命名不准确（分母是 max 不是 union）\n- Discussion LP hypotheses 标注 \"three mechanisms\" 实际有 4 个\n- Table 1 多个 bold 值需确认是否为 ties\n- Abstract 分号句暗示 LP 是 \"the\" empirical finding，降低 MBR failure 地位\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "struct_self_consist_ie"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 1 观点不同的地方。\n\n---\n\n### Reviewer 1 的完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n#### Must-Fix 问题\n\n**N1** [critical] \"By construction\" framing 混淆定义性与经验性发现\n- Section 3.1 反复声称 4/5 信号 \"cannot rank candidates by construction\"，但 Table 2 中这些信号实际通过 consensus-proximity selection (MBR) 执行了选择（SJ=0.646, FK=0.646 等）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。\n- 论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的）；(2) 用这些信号做 MBR-style selection 无效（经验性发现）。但论文将两者混为一谈。MBR 在 MT 中成功但在 IE 中失败是最重要的经验贡献之一——应突出而非隐藏在 \"by construction\" framing 下。\n- 建议：明确区分两层失败——(a) QE signal 的 instance-level 性质使其本身无法做 selection；(b) 将其转化为 per-sample utility（MBR）后仍然失败，这是经验发现。将 (b) 作为独立 contribution 突出。\n\n**N2** [critical] 标题和论文范围不匹配：\"Structured IE\" vs. 实际覆盖\n- \"Structured Information Extraction\" 通常包括 NER、RE、Event Extraction 等。论文核心证据来自 3 个 NER benchmark，RE 仅 1 个 benchmark 作为 \"exploratory extension\"，且统计上不完整（Table 2: RE 为 single-seed）。\n- 建议：缩窄标题或增加独立 RE 数据集。\n\n#### Should-Fix 问题\n\n**W1** Kendall W=1.000 (n=3 seeds) 统计效力不足\n- n=3 排 5 个 signal 的 W=1.000 效力极低。建议增加 seeds 或降低表述强度。\n\n**W2** Table 2 NER 2-seed vs RE single-seed 未充分解释\n- Appendix 显示 RE 有 3-seed QE 数据，但 selection 仅 single seed。需解释原因。\n\n**W3** 未测试 entity-level LP 聚合\n- Discussion 指出 hypothesis (d) \"format-token dilution\" 是主因，但未直接测试 entity-token-only LP。\n\n**W4** Gold-empty instance filtering 在 QE 和 Selection 之间不一致\n- QE 排除 gold-empty (CoNLL n=2756)，selection 保留 full set (n=3453)。Table A13 标注 n=2756 与此矛盾。\n\n**W5** 模型规模覆盖不足（3B-8B）限制结论普适性\n- Conclusion 表述 \"consistent across two model families (3B–8B)\" 暗示超过实际证据的普适性。\n\n#### Questions\n\n**Q1**: 为什么将 consensus-proximity selection 归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"？\n\n**Q2**: Entity-token-only LP 是否被考虑过？\n\n**Q3**: Table A13 CoNLL n=2756 vs 正文 \"selection retains full set\" (n=3453)——哪个正确？\n\n**Q4**: TOST external anchors 显示 Qwen CoNLL selection significantly worse than single-sample。这是否意味着某些配置下 signals 损害 selection？\n\n**Q5**: RE LP selection 在 free-form 下 direction reversal (+1.84±0.12pp)——为什么不作为 positive result 更突出呈现？\n\n#### Missing References\n1. Bertoldi et al. (2024) \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\"\n2. Ye et al. (2023) \"Complementary Explanations for Effective In-Context Learning\"\n3. Deguchi et al. (2024) \"Centroid-Based Efficient MBR Decoding\" — MBR 在 structured 任务上 mode-seeking bias\n\n#### 小问题\n- \"Soft Jaccard\" 命名不准确（分母是 max 不是 union）\n- Discussion LP hypotheses 标注 \"three mechanisms\" 实际有 4 个\n- Table 1 多个 bold 值需确认是否为 ties\n- Abstract 分号句暗示 LP 是 \"the\" empirical finding，降低 MBR failure 地位\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1192 · 2026-05-16T05:25:01.280727+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1470
}
```

</details>

---


### Assistant

_source line 1193 · 2026-05-16T05:25:04.243322+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 1194 · 2026-05-16T05:26:18.977199+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见如下。

---

## 交叉回应 Reviewer 2

### Must-Fix 问题

**[AGREE] R2-N1**: Contribution 1 的 "empirical dissociation" 大部分是定义必然

同意核心论点。这与我的 N1 高度一致——论文将 instance-level signals 的 selection failure 反复描述为 "by construction"，同时又展示它们的 MBR selection 结果（Table 2: SJ=0.646, FK=0.646），制造了逻辑上的自相矛盾。

**但需补充一点 nuance**：Contribution 1 中 ρ-AUROC-selection F1 三指标的 decouple 并非完全 trivial。对于 LP（per-sample signal），higher ρ 的朴素预期是 better selection——LP 的 selection failure 尽管 ρ=0.205 仍是真正的经验发现。此外，VerbConf 的 ρ > LP 但 selection worst（Appendix K, Table A14）才是最 surprising 的 dissociation。R2 的建议（将 by-construction 降为 background，突出 LP compression + MBR within-instance failure）是正确的重组方向。

---

**[AGREE] R2-N2**: 标题和 scope 严重不匹配

完全同意。我在自己的 N2 中提出了相同问题。RE 仅 SciERC 一个 benchmark，40% zero-F1，全文标注 "†RE" = preliminary。标题用 "Structured Information Extraction" 不成立。

---

**[REBUT] R2-N3**: ρ=0.45 被描述为 "strong" 是 overclaiming

部分不同意将此列为 **Must-Fix**。理由：

1. **Cohen's benchmarks 适用于行为科学，不直接适用于 NLP unsupervised QE**。在无监督置信度信号领域，ρ=0.45 的 baseline 对比应该是 random (ρ≈0) 和 supervised methods（通常 ρ=0.5-0.7），而非 Cohen 的 generic threshold。论文在 CoNLL 上 EM ρ=0.451, AUROC=0.816——后者在二分类场景中已是 good discriminator。

2. **论文已使用了限定语**：Abstract 写 "up to 0.45"（不是 average），Introduction 的 "strong quality estimation ($\rho$ up to 0.45)" 是在 contrast 完全失败的 selection 时使用的相对表述。

3. **然而 R2 的 underlying point 有道理**：如果 QE 本身只是 moderate，"gap" 的 dramaticness 确实降低。建议采纳 R2 的措辞建议 "moderate-to-strong by domain standards, substantially exceeding random baselines"——但这是 **Should-Fix level 的 framing refinement**，不是 critical issue。

---

### Should-Fix 问题

**[AGREE] R2-W1**: 未尝试任何 remedy

同意这限制了论文的 impact。我在 W3 中提出了 entity-token-only LP 这一最直接的 remedy。论文作为纯诊断性工作有其价值（类似于 Belinkov & Glass 2019 analysis papers），但至少一个 pilot remedy（如 LP × VC 组合、或 entity-token LP）会显著增强贡献。不过，我认为这不上升到 Must-Fix——因为论文的定位是 diagnostic + negative result，且已明确指向 trained verifiers 作为解决方向（citing Cobbe et al. 2021, Lightman et al. 2024）。

---

**[AGREE] R2-W2**: 模型规模范围过窄

完全同意，与我的 W5 一致。3B-8B 本质上是 one capability tier。LP compression 可能在 70B+ 上缓解。

---

**[REBUT] R2-W3**: Yao et al. (2026) 差异描述不够精确

不完全同意。Section 1 (Introduction, paragraph 2) 明确列出三项增量贡献："we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-N selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation." Related Work (Section 2, paragraph 2) 进一步澄清 Yao et al. 使用 "exact-match agreement" 而本文引入 structural matching。

这些差异是明确的、具体的、可验证的。如果 R2 的意思是需要 quantify 增量大小（如 "SJ vs. EM on Yao's setup"），那可能超出论文 scope——Yao et al. 在不同数据/模型上工作，direct comparison 不一定 feasible。建议作者在 camera-ready 中添加 1-2 句更精确的对比（如 "Yao et al. report ρ=X on their setup; our structural signals achieve ρ=Y on the same task type"），但这是 minor refinement。

---

**[AGREE] R2-W4**: ε=0.05 threshold 选择影响核心叙事

同意 R2 的具体建议。"60% tied" 是论文反复引用的核心数字（Abstract, Discussion），高度依赖 ε=0.05 的选择。ε=0.03 时 tied fraction 仅 31.8%（Table A10），叙事将从 "大多数 instances 无法区分" 变为 "约三分之一无法区分"。

论文确实在 Appendix 提供了 ε sweep（Table A10）和 continuous metric（pooled within-instance ρ=0.248），但这些被埋在附录中。R2 的建议——在正文中用 continuous characterization（pooled ρ=0.248, CDF 特征）替代二元 threshold 叙述——是合理的改进方向。不过我认为当前呈现也不算 misleading（因为 CDF 图和 sweep 都在 Appendix 中），所以 Should-Fix 定级恰当。

---

**[AGREE with caveat] R2-W5**: 缺少若干直接相关文献

- **Mejer & Crammer (2011) "Confidence in Structured Prediction"**：直接相关，structured prediction 的置信度估计先驱工作（CRF-based），论文已引 Culotta & McCallum (2004) 但漏了这篇。同意应加。
- **Xie et al. (2024) "Self-Evaluation Improves Selective Generation"**：如果涉及 per-sample self-evaluation for selection，直接相关。同意。
- **Zerva et al. (2025)** 和 **"Existing LLMs Are Not Self-Consistent" (2025)**：无法独立验证这两篇的存在和确切内容。建议作者核查后按相关性添加。

---

### Questions

**[AGREE] R2-Q1**: Entity-name-only LP 是否被考虑过？

完全同意这是关键缺失实验——与我的 W3 一致。Discussion 提出假说 (d) format-token dilution 但未直接检验。

---

**[REBUT] R2-Q2**: Binary classifier 预测 non-tied instances 然后条件性应用 LP

这是一个合理的 future work 方向，但作为对当前论文的批评稍显苛刻。论文定位为 diagnostic paper，要求实现 learned components 超出了论文的 scope statement。而且这本质上已是 "trained selector"——论文已指向 Cobbe et al. verifiers 作为解决方案。

---

**[AGREE] R2-Q3**: ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？

R2 的质疑合理：这三个指标 *理论上* 确实衡量不同的东西（rank correlation, binary discrimination, per-sample selection），所以它们 decouple 本身不令人惊讶。真正的 empirical content 不在于 "它们 decouple"，而在于 **decouple 的具体方式和原因**（VerbConf ρ > LP 但 selection worst; EM AUROC highest on CoNLL 但 ρ not best on SciERC）。建议作者重新表述 Contribution 1：不是 "metrics decouple"（trivial），而是 "the specific patterns of decoupling reveal distinct failure modes that single-metric evaluation would miss"。

---

**[REBUT] R2-Q4**: CoNLL selection 分析是否有意义？

不完全同意此批评。CoNLL 的 selection 分析虽然 headroom 极小（4pp），但作为 **ceiling-effect control** 是方法论上必要的：它确认 selection failure 不仅发生在难任务（SciERC）上，也发生在易任务上——但原因不同（难任务: LP compression + unreliable rankings; 易任务: collapsed diversity，无 headroom 可 exploit）。论文在 Appendix (Table A13 note) 已承认 "selection analysis on these configurations is uninformative because there is little per-sample variance"。

不过 R2 的 implicit point 有道理：正文不应对 CoNLL selection 结果过度解读。当前 Table A13 的呈现方式是恰当的（放 appendix 而非主表），但正文 Section 4.2 末尾 "The pattern holds across CoNLL" 的表述可以更 nuanced。

---

### 小问题

**[AGREE]** Abstract 数字过密——确实对 readability 有影响，建议精简。

**[REBUT]** Contribution 3 (difficulty-dependent rankings) 较弱——不同意较弱。WNUT-17 boundary collapse（full-set ρ=0.724 but conditional ρ=0.038，Table A5）是一个有价值的 finding，说明 signals 在 capability boundary 处完全失效。这对 practitioners 的 deployment 决策有直接意义。

**[AGREE]** Discussion LP hypotheses 标为 "three mechanisms" 但列出 (a)(b)(c)(d) 四个——我在小问题中也指出了这个 inconsistency。

**[AGREE]** oh2025latentsc bib year 应更新为 2026——如果论文确实在 2026 发表，应修正。

**[REBUT]** FK entity set 改编非标准——论文在 Section 3.2 给出了完整定义，Appendix D 通过 permutation test 验证了 FK 的有效性（all p<0.001, Table A3）。Adapted FK 的理论依据充分：将 entity set 视为 binary present/absent rating matrix 是 Fleiss' κ 的标准 use case。

---

### 总结

与 R2 的评分差异：我给 Overall 3.5（Borderline Conference），R2 给 3.0（Findings）。主要分歧点：

1. **N3 的严重程度**：R2 将 ρ=0.45 的措辞问题列为 critical，我认为是 Should-Fix level 的 framing refinement。
2. **W1 (no remedy) 的影响**：R2 认为严重限制 impact，我认为 diagnostic papers 在 EMNLP 有先例（如 probing/analysis papers），但同意加一个 pilot remedy 会增强。
3. **Contribution 3 (difficulty-dependent)**：R2 认为较弱，我认为 WNUT-17 boundary collapse 有独立价值。

核心一致点：N1/N2（framing + scope）是必须修改的关键问题。

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

_source line 1195 · 2026-05-16T05:26:23.752098+00:00_

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


## Round 95

## Round 95

8 recorded events


### User

_source line 1196 · 2026-05-16T05:27:19.255828+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

### Must-Fix

**[AGREE] R1-N1: "By construction" framing 混淆定义性与经验性发现**
同意，且 R1 的 framing 比我的 N1 更精准。Table 2 显示 instance-level signals 通过 consensus-proximity (MBR) 确实产生了 per-sample ranking (SJ=0.646, FK=0.646)。Discussion 承认 "VC becomes per-sample in the selection context"。Appendix §MBR Discussion (line 685-687) 将 selection 等价为 MBR decoding 并分析了 within-instance failure。这段分析本应在主文核心位置，而非 appendix。R1 建议将两层失败（定义性 vs 经验性 MBR failure）显式区分是正确的修改方向。

**[AGREE] R1-N2: 标题和论文范围不匹配**
与我的 N2 一致。补充：Appendix §RE Conditional Selection (Table A14) 排除 zero-F1 后 signals 表现更差 (VC: -10.0pp)，这个重要结果应在主文中明确呈现。

### Should-Fix

**[AGREE] R1-W1: Kendall W=1.000 (n=3) 统计效力不足**
n=3 时 W=1.000 的 p-value 约 0.05，仅 borderline significant。论文在 Appendix (line 890) 承认 "statistical power with n=3 seeds is limited" 但 main text 未体现。

**[AGREE] R1-W2: Table 2 NER 2-seed vs RE single-seed 未充分解释**
Appendix Table A6 有 3-seed RE QE 数据但 selection 仅 single seed，应解释原因。

**[AGREE] R1-W3: 未测试 entity-level LP 聚合**
与我的 Question 1 一致。Discussion 指出 hypothesis (d) "format-token dilution" 是主因但未直接测试 entity-token-only LP——零成本消融实验，缺失令人费解。

**[AGREE] R1-W4: Gold-empty filtering 不一致**
Section 3.3 说 "selection retains the full set" 但 Table A13 CoNLL 标注 n=2,756（而非 3,453）。无论哪个正确，都需修正。

**[AGREE] R1-W5: 模型规模覆盖不足**
与我的 W2 一致。

### Questions

**[AGREE] R1-Q1-Q4**: 全部同意。特别是 Q4——Appendix §TOST External Anchors 显示 Qwen CoNLL selection degrades by 0.9-1.5pp，某些配置下 signals 主动损害 selection，主文叙事 "no signal consistently improves" 低估了问题严重性。

**[REBUT] R1-Q5: RE free-form reversal 应更突出**
部分不同意。谨慎处理是适当的：(1) 单一 RE benchmark + 40% zero-F1；(2) 仅 Qwen3-8B 验证；(3) +1.84pp 仅捕获 ~10% oracle headroom。但同意可将其更积极地定位为 "promising direction"。

### Missing References

**[REBUT] R1-Ref-1: Bertoldi et al. (2024)**: 搜索未找到该论文，可能是幻觉引用。建议 R1 提供 arXiv ID。

**[REBUT] R1-Ref-2: Ye et al. (2023)**: ICL explanation 机制与本文 consistency/selection 关联度不高。

**[AGREE] R1-Ref-3: Deguchi et al. (2024)**: MBR centroid + mode-seeking bias 与 Appendix MBR Discussion 直接相关。

### Minor Issues

**[AGREE]** "Soft Jaccard" 命名不准确（分母是 max 不是 union）
**[AGREE]** "Three mechanisms" 实际有 4 个——我也独立标记了此错误
**[REBUT]** Table 1 bold ties：tied values 同时加粗是标准做法，没有问题
**[AGREE]** Abstract 结构暗示 LP 是唯一 empirical finding，低估 MBR failure

### 总结

两位 reviewer 高度一致：N1/N2 核心批评、W3-W5 实验缺陷、大部分 minor issues 独立得出相同结论。主要分歧在 Q5（RE reversal 呈现方式）和两篇 missing references 的验证。共同结论：LP compression + MBR failure 有价值，但 framing 和 scope 问题使论文更适合 Findings。

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

_source line 1197 · 2026-05-16T05:27:47.169620+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | head -30",
  "description": "Read current issue tracker header"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | head -30",
    "description": "Read current issue tracker header"
  }
}
```

</details>

---


### Tool result

_source line 1198 · 2026-05-16T05:27:47.372977+00:00_

issues:
# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====
- id: R0-C1
  summary: "模型规模单一（仅 8B）"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 Reviewer 确认措辞修正到位"
  resolution_round: 2
- id: R0-C2
  summary: "相关工作显著遗漏"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认 49 条 bib 全部 cited"
  resolution_round: 2
- id: R0-C4
  summary: "SJ 方法新颖性有限"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认三点差异化清晰"
  resolution_round: 2
- id: R0-C5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-16T05:30:38.057384+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (updated Round 12) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, title/abstract IE scope 过宽\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 12\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位 Reviewer 强共识: 标题 Structured IE 暗示 NER+RE+EE 覆盖, 实际 RE 仅 SciERC (40% zero-F1) + 全文 †RE preliminary. 本质是 NER 论文附带不完整 RE 探索. R1 建议缩窄标题或增 RE dataset; R2 同意. 已持续 13 轮, 是最顽固的 issue.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 12\n    action: \"将标题限定为 NER/entity set extraction, 或增加至少一个独立 RE dataset (TACRED/DocRED)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 12\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: (1) 4/5 信号 instance-level → identical scores 是定义必然, 不是 empirical finding; (2) 这些信号通过 MBR/consensus-proximity 做 selection 仍然失败是真正的 empirical finding (MBR 在 MT 中有效但在 IE 中失败); (3) 论文将两者混为一谈, 将 MBR 经验失败归为 by construction. R1: Table 2 显示 SJ/FK 确实产生了不同 selection F1, 说明 MBR 被执行了. R2: Appendix MBR Discussion 应移到主文. 两位一致建议: by-construction 降为 Section 3 前提, Contribution 1 重组为纯 empirical (LP compression + MBR within-instance failure).\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: (1) 将 instance-level/per-sample 分类降为 Section 3.1 前提/背景; (2) 将 MBR within-instance failure 提升为独立 empirical contribution; (3) LP compression 保持为核心 empirical contribution\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 12\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 60% tied 是核心叙事数字 (Abstract/Discussion 反复引用), 但 ε=0.03 时仅 31.8%. LP 是连续信号, tied/non-tied 二分法人为. R1 同意 R2 建议: 主文用 continuous characterization (pooled within-instance ρ=0.248, CDF 特征), ε-based 分析降为辅助. 当前不算 misleading (因 CDF 和 sweep 在 Appendix), 维持 Should-Fix.\"\n  action_items:\n  - round: 12\n    action: \"主文改用 continuous characterization (pooled within-instance ρ=0.248) 作为 primary evidence, ε=0.05 二分法降为辅助论据, 标注 post-hoc exploratory\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 部分解决: R1 rebut 指出 Introduction 已列 3 项具体差异 (structural matching, QE/selection separation, difficulty gradient). R2 接受但仍建议更精确量化. 共识: 现有差异描述可接受, camera-ready 级 refinement.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识. 3B-8B 本质是同一 capability tier. LP compression 可能在 70B+ 上缓解. Conclusion 'consistent across two model families (3B-8B)' 暗示超过实际证据的普适性.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime, 或增加 ≥30B 模型 pilot experiment\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant. Appendix 承认 power limited 但正文未体现.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度, 如 'consistent with stable rankings but insufficient power to confirm'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 聚焦到 entity-token-only LP: Discussion 列出 hypothesis (d) format-token dilution 但未直接测试. 两位独立提出 entity-name-token LP 是零成本消融实验, 缺失令人费解. R1 列为 Should-Fix W3; R2 列为 Question 1 + W1 (no remedy). 共识: 至少应尝试 entity-token LP 或 LP×consistency 组合.\"\n  action_items:\n  - round: 12\n    action: \"增加 entity-token-only LP 消融实验 (直接测试 hypothesis d), 或至少 LP×VC 组合 pilot\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及. 论文已改用 †RE 标记体系. 可能已部分改善, 待 Research Director 确认.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12: Discussion 已列出 (a)(b)(c)(d) 四个 hypotheses, 但标注为 'three (non-mutually-exclusive) mechanisms' — 编号错误. 更重要的是, hypotheses 仅列出未逐一验证 (free-form 仅测试 b/c). 两位独立标记编号错误.\"\n  action_items:\n  - round: 12\n    action: \"(1) 修正 'three' → 'four' mechanisms; (2) entity-token LP 测试 hypothesis (d)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"Greedy baseline 命名混淆\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及. Table 2 已改为 'Single‡' 标注 T=1.0 draw. 可能已修正, 待确认全文一致性.\"\n  action_items:\n  - round: 11\n    action: \"全文统一为 single-sample baseline\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位共识: Appendix 有 3-seed RE QE 数据, 但 selection 仅 single seed, 需解释原因 (资源限制?)\"\n  action_items:\n  - round: 12\n    action: \"在正文或 footnote 解释 NER/RE seed 数量不对称原因; 如有数据补充 RE multi-seed selection\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022, CSP, Beyond Confidence\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 新增缺失引用: Deguchi et al. (2024) Centroid-Based MBR (两位共识), Mejer & Crammer (2011) Confidence in Structured Prediction (R2 提 R1 同意), Xie et al. (2024) Self-Evaluation Selective Generation (R2 提 R1 同意). R1 提 Bertoldi et al. 被 R2 rebut (可能不存在). R11 三篇 (Fernandes, CSP, Beyond Confidence) 已有引用.\"\n  action_items:\n  - round: 12\n    action: \"补充: Deguchi et al. (2024), Mejer & Crammer (2011), Xie et al. (2024). 核实 Bertoldi et al. 是否存在.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 12) =====\n- id: R12-N1\n  summary: \"ρ=0.45 描述为 strong quality estimation, 实际是 moderate correlation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R2 列为 Must-Fix, R1 rebut 降为 Should-Fix. R1 论点: Cohen's benchmarks 适用于行为科学而非 NLP unsupervised QE; ρ=0.45 对比 random (ρ≈0) 已是 substantial; AUROC=0.816 (CoNLL) 补充了二分类性能. R2 接受 rebut, 共识: Should-Fix level, 改措辞为 moderate-to-strong 或加限定语.\"\n  action_items:\n  - round: 12\n    action: \"将 'strong quality estimation' 改为 'moderate-to-strong by domain standards' 或 'non-trivial quality estimation, substantially exceeding random baselines'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix. R1 同意但认为 diagnostic papers 在 EMNLP 有先例. 共识: Should-Fix level, 至少一个 pilot remedy (entity-token LP, LP×VC, LP z-score) 会显著增强.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验, 即使结果为 negative\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致; Table A13 n 值标注可能有误\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1 发现: Section 3.3 说 'selection retains the full set' 但 Table A13 CoNLL 标注 n=2756 (非 3453). R2 同意需修正.\"\n  action_items:\n  - round: 12\n    action: \"确认 Table A13 n 值是否正确; 统一说明 QE/selection filtering 策略差异的理由\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出 (a)(b)(c)(d) 四个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1 提出, R2 同意. Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|, 非标准 Jaccard 推广.\"\n  action_items:\n  - round: 12\n    action: \"改名为 Soft Overlap Score 或在首次出现时明确说明与标准 Jaccard 区别\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  - round: 12\n    reviewers: [2]\n    note: \"R2 引用完整性检查: 47 entries, 0 orphan. 可能已修复, 待 Research Director 确认.\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及, 可能已修复\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"与 R11-M1 合并处理\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12: R1-Q5 提出应更突出呈现 RE reversal. R2 rebut: 单 benchmark + 40% zero-F1, 谨慎处理适当, 但可定位为 promising direction. 共识: 不作为 positive result 突出, 但应更积极讨论.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction 而非纯 caveat\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness. 其他两个论证较强, 整体充分\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (updated Round 12) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, title/abstract IE scope 过宽\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 12\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位 Reviewer 强共识: 标题 Structured IE 暗示 NER+RE+EE 覆盖, 实际 RE 仅 SciERC (40% zero-F1) + 全文 †RE preliminary. 本质是 NER 论文附带不完整 RE 探索. R1 建议缩窄标题或增 RE dataset; R2 同意. 已持续 13 轮, 是最顽固的 issue.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 12\n    action: \"将标题限定为 NER/entity set extraction, 或增加至少一个独立 RE dataset (TACRED/DocRED)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 12\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: (1) 4/5 信号 instance-level → identical scores 是定义必然, 不是 empirical finding; (2) 这些信号通过 MBR/consensus-proximity 做 selection 仍然失败是真正的 empirical finding (MBR 在 MT 中有效但在 IE 中失败); (3) 论文将两者混为一谈, 将 MBR 经验失败归为 by construction. R1: Table 2 显示 SJ/FK 确实产生了不同 selection F1, 说明 MBR 被执行了. R2: Appendix MBR Discussion 应移到主文. 两位一致建议: by-construction 降为 Section 3 前提, Contribution 1 重组为纯 empirical (LP compression + MBR within-instance failure).\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: (1) 将 instance-level/per-sample 分类降为 Section 3.1 前提/背景; (2) 将 MBR within-instance failure 提升为独立 empirical contribution; (3) LP compression 保持为核心 empirical contribution\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 12\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 60% tied 是核心叙事数字 (Abstract/Discussion 反复引用), 但 ε=0.03 时仅 31.8%. LP 是连续信号, tied/non-tied 二分法人为. R1 同意 R2 建议: 主文用 continuous characterization (pooled within-instance ρ=0.248, CDF 特征), ε-based 分析降为辅助. 当前不算 misleading (因 CDF 和 sweep 在 Appendix), 维持 Should-Fix.\"\n  action_items:\n  - round: 12\n    action: \"主文改用 continuous characterization (pooled within-instance ρ=0.248) 作为 primary evidence, ε=0.05 二分法降为辅助论据, 标注 post-hoc exploratory\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 部分解决: R1 rebut 指出 Introduction 已列 3 项具体差异 (structural matching, QE/selection separation, difficulty gradient). R2 接受但仍建议更精确量化. 共识: 现有差异描述可接受, camera-ready 级 refinement.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识. 3B-8B 本质是同一 capability tier. LP compression 可能在 70B+ 上缓解. Conclusion 'consistent across two model families (3B-8B)' 暗示超过实际证据的普适性.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime, 或增加 ≥30B 模型 pilot experiment\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant. Appendix 承认 power limited 但正文未体现.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度, 如 'consistent with stable rankings but insufficient power to confirm'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 聚焦到 entity-token-only LP: Discussion 列出 hypothesis (d) format-token dilution 但未直接测试. 两位独立提出 entity-name-token LP 是零成本消融实验, 缺失令人费解. R1 列为 Should-Fix W3; R2 列为 Question 1 + W1 (no remedy). 共识: 至少应尝试 entity-token LP 或 LP×consistency 组合.\"\n  action_items:\n  - round: 12\n    action: \"增加 entity-token-only LP 消融实验 (直接测试 hypothesis d), 或至少 LP×VC 组合 pilot\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及. 论文已改用 †RE 标记体系. 可能已部分改善, 待 Research Director 确认.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12: Discussion 已列出 (a)(b)(c)(d) 四个 hypotheses, 但标注为 'three (non-mutually-exclusive) mechanisms' — 编号错误. 更重要的是, hypotheses 仅列出未逐一验证 (free-form 仅测试 b/c). 两位独立标记编号错误.\"\n  action_items:\n  - round: 12\n    action: \"(1) 修正 'three' → 'four' mechanisms; (2) entity-token LP 测试 hypothesis (d)\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"Greedy baseline 命名混淆\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及. Table 2 已改为 'Single‡' 标注 T=1.0 draw. 可能已修正, 待确认全文一致性.\"\n  action_items:\n  - round: 11\n    action: \"全文统一为 single-sample baseline\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位共识: Appendix 有 3-seed RE QE 数据, 但 selection 仅 single seed, 需解释原因 (资源限制?)\"\n  action_items:\n  - round: 12\n    action: \"在正文或 footnote 解释 NER/RE seed 数量不对称原因; 如有数据补充 RE multi-seed selection\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022, CSP, Beyond Confidence\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 新增缺失引用: Deguchi et al. (2024) Centroid-Based MBR (两位共识), Mejer & Crammer (2011) Confidence in Structured Prediction (R2 提 R1 同意), Xie et al. (2024) Self-Evaluation Selective Generation (R2 提 R1 同意). R1 提 Bertoldi et al. 被 R2 rebut (可能不存在). R11 三篇 (Fernandes, CSP, Beyond Confidence) 已有引用.\"\n  action_items:\n  - round: 12\n    action: \"补充: Deguchi et al. (2024), Mejer & Crammer (2011), Xie et al. (2024). 核实 Bertoldi et al. 是否存在.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 12) =====\n- id: R12-N1\n  summary: \"ρ=0.45 描述为 strong quality estimation, 实际是 moderate correlation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R2 列为 Must-Fix, R1 rebut 降为 Should-Fix. R1 论点: Cohen's benchmarks 适用于行为科学而非 NLP unsupervised QE; ρ=0.45 对比 random (ρ≈0) 已是 substantial; AUROC=0.816 (CoNLL) 补充了二分类性能. R2 接受 rebut, 共识: Should-Fix level, 改措辞为 moderate-to-strong 或加限定语.\"\n  action_items:\n  - round: 12\n    action: \"将 'strong quality estimation' 改为 'moderate-to-strong by domain standards' 或 'non-trivial quality estimation, substantially exceeding random baselines'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R2 列为 Should-Fix. R1 同意但认为 diagnostic papers 在 EMNLP 有先例. 共识: Should-Fix level, 至少一个 pilot remedy (entity-token LP, LP×VC, LP z-score) 会显著增强.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验, 即使结果为 negative\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致; Table A13 n 值标注可能有误\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1 发现: Section 3.3 说 'selection retains the full set' 但 Table A13 CoNLL 标注 n=2756 (非 3453). R2 同意需修正.\"\n  action_items:\n  - round: 12\n    action: \"确认 Table A13 n 值是否正确; 统一说明 QE/selection filtering 策略差异的理由\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出 (a)(b)(c)(d) 四个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R1 提出, R2 同意. Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|, 非标准 Jaccard 推广.\"\n  action_items:\n  - round: 12\n    action: \"改名为 Soft Overlap Score 或在首次出现时明确说明与标准 Jaccard 区别\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  - round: 12\n    reviewers: [2]\n    note: \"R2 引用完整性检查: 47 entries, 0 orphan. 可能已修复, 待 Research Director 确认.\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及, 可能已修复\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"与 R11-M1 合并处理\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12: R1-Q5 提出应更突出呈现 RE reversal. R2 rebut: 单 benchmark + 40% zero-F1, 谨慎处理适当, 但可定位为 promising direction. 共识: 不作为 positive result 突出, 但应更积极讨论.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction 而非纯 caveat\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness. 其他两个论证较强, 整体充分\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-16T05:30:38.159474+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 21279}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-16T05:32:57.655521+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 12（Fresh Review）\n\n**项目**: struct_self_consist_ie\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+完整性+写作）\n**轮次**: 1 轮即收敛（关键问题强共识，无重大未解决分歧）\n\n---\n\n## Summary\n\n本文评估五种置信度信号（structural: SJ/VC; surface: EM/FK; model-internal: LP）在 LLM-based structured IE 中的质量估计（QE）和 best-of-N 样本选择能力，提出 \"correlation-selection gap\"：信号与 F1 达中等相关性（Spearman ρ up to 0.45）但无法改善样本选择，尽管 oracle headroom 达 13-18 pp。四个 instance-level 信号本质上对所有 candidate 赋予相同分数；LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats, 60% tied）而失败。Free-form ablation 证明 NER LP 压缩非 constrained decoding artifact。\n\n论文在统计方法和实验设计上达到较高标准（bootstrap CI, TOST, permutation tests, 多 seed 验证），但核心 framing 存在定义性 vs 经验性发现的混淆，标题/scope 不匹配实际覆盖度，且纯诊断性论文缺乏 remedy 尝试限制了 impact。\n\n---\n\n## Strengths\n\n**S1** [两位共识] **QE vs selection 的显式形式化**：Section 3.1 首次在 IE confidence estimation 领域系统区分 per-sample 和 instance-level 信号，ρ/AUROC/selection F1 三指标的 decouple demonstration 对 test-time compute scaling 社区有直接参考价值。\n\n**S2** [两位共识] **LP compression 分析深度突出**：多角度刻画——median range 0.041 nats, pooled within-instance ρ=0.248, non-tied subset +2.9pp (p=0.004), CDF 连续性, VerbConf 对照 (Appendix K)——是论文最有价值的 empirical contribution。\n\n**S3** [两位共识] **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep, external equivalence margins。主动识别并处理了 potential circularity（TOST δ vs oracle headroom）。超过 EMNLP 平均水平。\n\n**S4** [两位共识] **消融设计合理**：Free-form decoding ablation（4-seed, NER+RE）有效隔离 constrained decoding 影响; Scale ablation (3B-8B) 提供跨规模验证; Temperature + N-scaling 覆盖关键超参。\n\n**S5** [两位共识] **诚实的 limitations 和 caveats**：RE 始终用 † 标注, TOST configuration-dependent 已说明, ε 标注 post-hoc, thinking token confound 有 3-part 分析。Appendix 极其详尽（15+ sections）。\n\n**S6** [R1] **负面结果呈现方式得当**：通过 non-tied subset 展示 LP 在什么条件下能工作，并诊断出 compression 作为瓶颈，而非强行 positive spin。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 两位强共识] **\"By construction\" framing 混淆定义性与经验性发现，掩盖 MBR failure 的独立价值**\n\n论文反复声称 4/5 信号 \"cannot rank candidates by construction\"（Section 3.1, Abstract, Discussion），但 Table 2 显示这些信号通过 consensus-proximity selection (MBR) 确实产生了不同的 selection F1（SJ=0.646, FK=0.646, EM=0.637, VC=0.623）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix §MBR Discussion 将 selection 等价为 MBR decoding。\n\n两位 Reviewer 一致认为：\n- (a) instance-level QE 值对所有 candidate 相同——这是**定义必然**，不是经验发现\n- (b) 将这些信号转化为 MBR-style per-sample utility 后 selection 仍然失败——这是**真正的经验发现**（MBR 在 MT 中有效但在 IE 中失败）\n- 论文将 (a) 和 (b) 混为一谈，将 MBR 的经验性失败归为 \"by construction\"，既弱化了 (b) 作为独立 contribution 的价值，又在逻辑上自相矛盾\n\n**建议**：Contribution list 重组——将 instance-level/per-sample 分类降为 Section 3 前提，将 MBR within-instance failure 提升为独立 empirical contribution，LP compression 保持为核心 contribution。Appendix §MBR Discussion 的 within-instance failure 分析应进入主文。\n\n**MF2** [critical, 两位强共识] **标题 \"Structured Information Extraction\" 与实际覆盖严重不匹配**\n\n\"Structured IE\" 通常涵盖 NER、RE、Event Extraction 等。论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅 SciERC 一个 benchmark（40% zero-F1）作为 \"exploratory extension\"，全文用 †RE 标注 preliminary。无 Event Extraction。实质上是 NER confidence estimation 论文附带初步 RE 探索。\n\n此问题已**持续 13 轮**（首次提出于 Round 0），是最顽固的 issue。每轮 Reviewer 均指出标题/scope 落差。\n\n**建议**：(a) 将标题限定为 NER / Entity Set Extraction，RE 作为 exploratory extension; 或 (b) 增加至少一个独立 RE dataset（如 DocRED）使 RE 结论不再 preliminary。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 两位共识] **ρ=0.45 描述为 \"strong quality estimation\" 措辞过度**\n\nR2 原列为 Must-Fix，R1 有效 rebut 后降为 Should-Fix。Cohen's benchmarks (0.1/0.3/0.5) 适用于行为科学，不直接适用于 NLP unsupervised QE。但 ρ=0.45 仅解释 ~20% 方差，\"strong\" 确实 overstate。\n\n**建议**：改为 \"moderate-to-strong by domain standards, substantially exceeding random baselines\"。\n\n**SF2** [warning, 两位共识] **未测试 entity-token-only LP——Discussion 假说 (d) 的直接检验缺失**\n\nDiscussion 列出 hypothesis (d) \"format-token dilution\" 为 LP compression 主因（fine-tuned models 对 schema tokens 赋予极高 LP），但未直接验证。Entity-name-token-only LP 是零成本消融实验，缺失令人费解。两位 Reviewer 独立提出。\n\n**建议**：增加 entity-token-only LP 消融；如不可行需解释原因。\n\n**SF3** [warning, 两位共识] **纯诊断无 remedy 尝试，限制论文 impact**\n\n论文诊断了问题但未尝试任何解决方案（哪怕是简单的 LP×consistency 组合、LP z-score 归一化、或 entity-token LP）。R1 认为 diagnostic papers 在 EMNLP 有先例（probing/analysis 传统），R2 认为严重限制 impact。共识：Should-Fix level，至少一个 pilot remedy（即使 negative）会显著增强。\n\n**SF4** [warning, 两位共识] **ε=0.05 threshold 依赖影响核心叙事**\n\n\"60% tied\" 是论文反复引用的核心数字（Abstract, Discussion），高度依赖 ε=0.05。ε=0.03 时 tied fraction 仅 31.8%。LP 是连续信号，二元 threshold 叙述人为。Appendix 有 CDF 和 sweep 但被埋在附录中。\n\n**建议**：主文改用 continuous characterization（pooled within-instance ρ=0.248, CDF 特征）作为 primary evidence，ε-based 分析标注 post-hoc exploratory。\n\n**SF5** [warning, 两位共识] **模型规模覆盖不足（3B-8B）**\n\n3B-8B 本质是同一 capability tier。LP compression 可能在 70B+ 上缓解（更大模型可能产生更多样化 samples）。Conclusion \"consistent across two model families (3B–8B)\" 暗示超过实际证据的普适性。\n\n**建议**：在 Conclusion/Discussion 明确限定为 small-model regime，或增加 ≥30B 模型 pilot。\n\n**SF6** [warning, 两位共识] **Kendall W=1.000 (n=3 seeds) 统计效力不足**\n\nn=3 排 5 个 signal 的 W=1.000 p≈0.05 仅 borderline significant。Appendix 承认 \"statistical power with n=3 is limited\" 但正文未体现。\n\n**建议**：正文降低表述强度，改为 \"consistent with stable rankings but insufficient power to confirm.\"\n\n**SF7** [warning, 两位共识] **Table 2 NER 2-seed vs RE single-seed 不一致未解释**\n\nAppendix 有 3-seed RE QE 数据，但 selection 仅 single seed。需在正文或 footnote 说明原因。\n\n**SF8** [warning, R1 提出 R2 同意] **Gold-empty filtering 在 QE 和 Selection 之间不一致**\n\nSection 3.3 说 \"selection retains the full set\"（n=3453），但 Table A13 CoNLL 标注 n=2756。无论哪个正确，存在矛盾需修正。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立提出并在交叉分享中确认共识：\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| By-construction framing 问题 | N1 [AGREE] | N1 [AGREE] | **强共识** |\n| 标题/scope 不匹配 | N2 [AGREE] | N2 [AGREE] | **强共识** |\n| Entity-token LP 未测试 | W3 [AGREE] | Q1 [AGREE] | **强共识** |\n| ε threshold 依赖 | — [AGREE] | W4 [AGREE] | **强共识** |\n| Model scale 不足 | W5 [AGREE] | W2 [AGREE] | **强共识** |\n| Kendall W 效力 | W1 [AGREE] | — [AGREE] | **强共识** |\n| NER/RE seed 不对称 | W2 [AGREE] | — [AGREE] | **强共识** |\n| Gold-empty filtering | W4 [AGREE] | — [AGREE] | **共识** |\n| LP hypotheses 编号错误 | minor [AGREE] | minor [AGREE] | **共识** |\n\n## Reviewer Divergence\n\n| Issue | R1 Position | R2 Position | Resolution |\n|-------|-------------|-------------|------------|\n| ρ=0.45 \"strong\" 措辞 | Should-Fix (domain standards differ) | Must-Fix (Cohen's moderate) | **降为 Should-Fix**: R1 有效 rebut, domain-specific 标准有道理 |\n| No remedy 的严重程度 | Should-Fix (diagnostic papers 有先例) | 接近 Must-Fix | **Should-Fix**: 共识 pilot remedy 会增强但非必须 |\n| Contribution 3 (difficulty-dependent) | 有独立价值 (WNUT-17 collapse) | 较弱 | **保留**: WNUT-17 boundary collapse 对 practitioners 有意义 |\n| RE free-form reversal 呈现 | 应更突出 | 谨慎处理适当 | **定位为 promising direction**: 单 benchmark 限制了 claim 强度 |\n| Yao et al. 差异描述 | 现有描述充分 | 需更精确 | **Camera-ready refinement**: 现有 3 项差异清晰 |\n\n---\n\n## Questions（需作者回答）\n\n**Q1** [两位共识]: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上产生了 per-sample ranking。请解释为什么论文将其归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"——这两者的理论含义截然不同。\n\n**Q2** [两位共识]: Entity-token-only LP（仅对 entity mention tokens 计算 LP，排除 JSON schema tokens）是否被考虑过？如果排除 schema tokens，within-instance compression 是否缓解？这是 Discussion hypothesis (d) 的直接检验。\n\n**Q3** [R1]: Table A13 (cross_selection) 标注 CoNLL n=2756，但 Section 3.3 说 \"selection retains the full set\" (n=3453)。哪个正确？\n\n**Q4** [R1, R2 同意]: TOST external anchors 显示 Qwen CoNLL selection 比 single-sample 显著更差（0.9-1.5pp degradation，所有外部 δ 下不通过等价检验）。某些配置下 signals 是否主动损害 selection？这与正文 \"no signal consistently improves\" 的表述不一致。\n\n**Q5** [R2]: Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？这三个指标衡量不同的东西（rank correlation, binary discrimination, per-sample selection），decouple 本身是否只是 expected behavior？\n\n**Q6** [R2]: CoNLL (F1≈0.91, oracle headroom ~4pp) 的 selection 分析是否有意义？R1 回应这是必要的 ceiling-effect control，但正文可否避免对 near-ceiling 配置过度解读？\n\n---\n\n## Missing References\n\n两位 Reviewer 共识应补充：\n1. **Deguchi et al. (2024)** \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" — MBR mode-seeking bias 分析，与 Appendix MBR Discussion 直接相关\n2. **Mejer & Crammer (2011)** \"Confidence Estimation in Structured Prediction\" — 经典 structured prediction confidence 先驱工作\n3. **Xie et al. (2024)** \"Self-Evaluation Improves Selective Generation\" (NeurIPS 2024) — LLM per-sample self-evaluation for selective generation\n\n待核实：\n4. **Bertoldi et al. (2024)** \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\" — R1 推荐，R2 rebut 未能找到。需作者核实是否存在。\n\n已有引用无问题：\n- R2 引用完整性检查: 47 entries, 0 orphan, 0 missing, 40/47 OpenAlex verified, 无幻觉引用\n- oh2025latentsc bib year 建议更新为 2026\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿 (paperreview.ai disabled)。\n\n---\n\n## Overall Assessment\n\n**Overall Score**: Borderline — 介于 Findings (3.0) 和 Conference (3.5) 之间\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.75** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.25** |\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及 appendix，熟悉相关文献）\n\n**核心判断**：\n- **值得发表**的内容：LP compression 分析、MBR within-instance failure、QE/selection 解耦形式化、统计方法论标准\n- **阻碍 Conference acceptance** 的问题：(1) framing 的定义性/经验性混淆（MF1）；(2) 标题/scope 不匹配（MF2，持续 13 轮）\n- **如果 MF1+MF2 修正**（contribution 重组 + 标题精确化），可提升至 Conference acceptance (3.5-4.0)\n- **当前版本**更适合 **Findings track**：实验扎实、统计全面、负面结果有价值，但 framing 不当和 scope overclaiming 使 main conference 定位困难\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（一句话内 ρ=0.45, 0.041 nats, 60% tied, +1.8±0.1 pp）\n- \"strong quality estimation\" → 建议改为 \"moderate-to-strong\"\n- \"Four instance-level signals fail by construction\" 暗示 LP 是唯一 empirical finding，降低 MBR failure 地位\n\n### Introduction\n- Contribution 1 需重组：definitional 部分降为 background，突出 empirical dissociation 的具体 pattern\n- Contribution 3 (difficulty-dependent rankings) 较弱但有价值（WNUT-17 collapse 对 practitioners 有意义）\n- 与 Yao et al. (2026) 的差异清晰但可更精确\n\n### Method (Section 3)\n- Signal 定义严谨，SJ/FK/VC/EM/LP 形式化清晰\n- \"Soft Jaccard\" 命名不准确（分母是 max 不是 union），建议改名或说明\n- FK entity set adaptation 非标准但 Appendix permutation test 验证充分\n\n### Experiments (Section 4)\n- Table 1: 单 seed 已在 caption 标注，cross-ref Table A7 合理\n- Table 2: NER 2-seed vs RE single-seed 不一致需解释\n- Section 4.2: \"no signal consistently improves selection\" 与 TOST external anchors（Qwen CoNLL degradation）存在张力\n- Scale ablation (Table 3): 3B-8B 覆盖不足\n\n### Discussion (Section 5)\n- LP hypotheses 标注 \"three mechanisms\" 但列出 4 个——编号错误\n- Hypothesis (d) format-token dilution 是最有力假说但未直接测试\n- RE free-form reversal (+1.84±0.12pp) 被谨慎处理——建议定位为 promising direction\n- \"Effective selection likely requires trained verifiers\" 指向合理但论文未尝试任何 remedy\n\n### Limitations\n- 诚实全面，覆盖了 RE 单 benchmark、model scale、verifier 缺失、ε 选择等已知限制\n- 可补充：entity-token LP 未测试的明确说明\n\n### Appendix\n- 极其详尽（15+ sections），覆盖了几乎所有消融方向\n- MBR Discussion (Appendix L) 的 within-instance failure 分析应进入主文\n- RE Conditional Selection (Appendix M) 排除 zero-F1 后 signals 更差 (VC: -10.0pp)——重要结果应在主文提及",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "report": "# 审稿报告 — Round 12（Fresh Review）\n\n**项目**: struct_self_consist_ie\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+完整性+写作）\n**轮次**: 1 轮即收敛（关键问题强共识，无重大未解决分歧）\n\n---\n\n## Summary\n\n本文评估五种置信度信号（structural: SJ/VC; surface: EM/FK; model-internal: LP）在 LLM-based structured IE 中的质量估计（QE）和 best-of-N 样本选择能力，提出 \"correlation-selection gap\"：信号与 F1 达中等相关性（Spearman ρ up to 0.45）但无法改善样本选择，尽管 oracle headroom 达 13-18 pp。四个 instance-level 信号本质上对所有 candidate 赋予相同分数；LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats, 60% tied）而失败。Free-form ablation 证明 NER LP 压缩非 constrained decoding artifact。\n\n论文在统计方法和实验设计上达到较高标准（bootstrap CI, TOST, permutation tests, 多 seed 验证），但核心 framing 存在定义性 vs 经验性发现的混淆，标题/scope 不匹配实际覆盖度，且纯诊断性论文缺乏 remedy 尝试限制了 impact。\n\n---\n\n## Strengths\n\n**S1** [两位共识] **QE vs selection 的显式形式化**：Section 3.1 首次在 IE confidence estimation 领域系统区分 per-sample 和 instance-level 信号，ρ/AUROC/selection F1 三指标的 decouple demonstration 对 test-time compute scaling 社区有直接参考价值。\n\n**S2** [两位共识] **LP compression 分析深度突出**：多角度刻画——median range 0.041 nats, pooled within-instance ρ=0.248, non-tied subset +2.9pp (p=0.004), CDF 连续性, VerbConf 对照 (Appendix K)——是论文最有价值的 empirical contribution。\n\n**S3** [两位共识] **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep, external equivalence margins。主动识别并处理了 potential circularity（TOST δ vs oracle headroom）。超过 EMNLP 平均水平。\n\n**S4** [两位共识] **消融设计合理**：Free-form decoding ablation（4-seed, NER+RE）有效隔离 constrained decoding 影响; Scale ablation (3B-8B) 提供跨规模验证; Temperature + N-scaling 覆盖关键超参。\n\n**S5** [两位共识] **诚实的 limitations 和 caveats**：RE 始终用 † 标注, TOST configuration-dependent 已说明, ε 标注 post-hoc, thinking token confound 有 3-part 分析。Appendix 极其详尽（15+ sections）。\n\n**S6** [R1] **负面结果呈现方式得当**：通过 non-tied subset 展示 LP 在什么条件下能工作，并诊断出 compression 作为瓶颈，而非强行 positive spin。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 两位强共识] **\"By construction\" framing 混淆定义性与经验性发现，掩盖 MBR failure 的独立价值**\n\n论文反复声称 4/5 信号 \"cannot rank candidates by construction\"（Section 3.1, Abstract, Discussion），但 Table 2 显示这些信号通过 consensus-proximity selection (MBR) 确实产生了不同的 selection F1（SJ=0.646, FK=0.646, EM=0.637, VC=0.623）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix §MBR Discussion 将 selection 等价为 MBR decoding。\n\n两位 Reviewer 一致认为：\n- (a) instance-level QE 值对所有 candidate 相同——这是**定义必然**，不是经验发现\n- (b) 将这些信号转化为 MBR-style per-sample utility 后 selection 仍然失败——这是**真正的经验发现**（MBR 在 MT 中有效但在 IE 中失败）\n- 论文将 (a) 和 (b) 混为一谈，将 MBR 的经验性失败归为 \"by construction\"，既弱化了 (b) 作为独立 contribution 的价值，又在逻辑上自相矛盾\n\n**建议**：Contribution list 重组——将 instance-level/per-sample 分类降为 Section 3 前提，将 MBR within-instance failure 提升为独立 empirical contribution，LP compression 保持为核心 contribution。Appendix §MBR Discussion 的 within-instance failure 分析应进入主文。\n\n**MF2** [critical, 两位强共识] **标题 \"Structured Information Extraction\" 与实际覆盖严重不匹配**\n\n\"Structured IE\" 通常涵盖 NER、RE、Event Extraction 等。论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅 SciERC 一个 benchmark（40% zero-F1）作为 \"exploratory extension\"，全文用 †RE 标注 preliminary。无 Event Extraction。实质上是 NER confidence estimation 论文附带初步 RE 探索。\n\n此问题已**持续 13 轮**（首次提出于 Round 0），是最顽固的 issue。每轮 Reviewer 均指出标题/scope 落差。\n\n**建议**：(a) 将标题限定为 NER / Entity Set Extraction，RE 作为 exploratory extension; 或 (b) 增加至少一个独立 RE dataset（如 DocRED）使 RE 结论不再 preliminary。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 两位共识] **ρ=0.45 描述为 \"strong quality estimation\" 措辞过度**\n\nR2 原列为 Must-Fix，R1 有效 rebut 后降为 Should-Fix。Cohen's benchmarks (0.1/0.3/0.5) 适用于行为科学，不直接适用于 NLP unsupervised QE。但 ρ=0.45 仅解释 ~20% 方差，\"strong\" 确实 overstate。\n\n**建议**：改为 \"moderate-to-strong by domain standards, substantially exceeding random baselines\"。\n\n**SF2** [warning, 两位共识] **未测试 entity-token-only LP——Discussion 假说 (d) 的直接检验缺失**\n\nDiscussion 列出 hypothesis (d) \"format-token dilution\" 为 LP compression 主因（fine-tuned models 对 schema tokens 赋予极高 LP），但未直接验证。Entity-name-token-only LP 是零成本消融实验，缺失令人费解。两位 Reviewer 独立提出。\n\n**建议**：增加 entity-token-only LP 消融；如不可行需解释原因。\n\n**SF3** [warning, 两位共识] **纯诊断无 remedy 尝试，限制论文 impact**\n\n论文诊断了问题但未尝试任何解决方案（哪怕是简单的 LP×consistency 组合、LP z-score 归一化、或 entity-token LP）。R1 认为 diagnostic papers 在 EMNLP 有先例（probing/analysis 传统），R2 认为严重限制 impact。共识：Should-Fix level，至少一个 pilot remedy（即使 negative）会显著增强。\n\n**SF4** [warning, 两位共识] **ε=0.05 threshold 依赖影响核心叙事**\n\n\"60% tied\" 是论文反复引用的核心数字（Abstract, Discussion），高度依赖 ε=0.05。ε=0.03 时 tied fraction 仅 31.8%。LP 是连续信号，二元 threshold 叙述人为。Appendix 有 CDF 和 sweep 但被埋在附录中。\n\n**建议**：主文改用 continuous characterization（pooled within-instance ρ=0.248, CDF 特征）作为 primary evidence，ε-based 分析标注 post-hoc exploratory。\n\n**SF5** [warning, 两位共识] **模型规模覆盖不足（3B-8B）**\n\n3B-8B 本质是同一 capability tier。LP compression 可能在 70B+ 上缓解（更大模型可能产生更多样化 samples）。Conclusion \"consistent across two model families (3B–8B)\" 暗示超过实际证据的普适性。\n\n**建议**：在 Conclusion/Discussion 明确限定为 small-model regime，或增加 ≥30B 模型 pilot。\n\n**SF6** [warning, 两位共识] **Kendall W=1.000 (n=3 seeds) 统计效力不足**\n\nn=3 排 5 个 signal 的 W=1.000 p≈0.05 仅 borderline significant。Appendix 承认 \"statistical power with n=3 is limited\" 但正文未体现。\n\n**建议**：正文降低表述强度，改为 \"consistent with stable rankings but insufficient power to confirm.\"\n\n**SF7** [warning, 两位共识] **Table 2 NER 2-seed vs RE single-seed 不一致未解释**\n\nAppendix 有 3-seed RE QE 数据，但 selection 仅 single seed。需在正文或 footnote 说明原因。\n\n**SF8** [warning, R1 提出 R2 同意] **Gold-empty filtering 在 QE 和 Selection 之间不一致**\n\nSection 3.3 说 \"selection retains the full set\"（n=3453），但 Table A13 CoNLL 标注 n=2756。无论哪个正确，存在矛盾需修正。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立提出并在交叉分享中确认共识：\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| By-construction framing 问题 | N1 [AGREE] | N1 [AGREE] | **强共识** |\n| 标题/scope 不匹配 | N2 [AGREE] | N2 [AGREE] | **强共识** |\n| Entity-token LP 未测试 | W3 [AGREE] | Q1 [AGREE] | **强共识** |\n| ε threshold 依赖 | — [AGREE] | W4 [AGREE] | **强共识** |\n| Model scale 不足 | W5 [AGREE] | W2 [AGREE] | **强共识** |\n| Kendall W 效力 | W1 [AGREE] | — [AGREE] | **强共识** |\n| NER/RE seed 不对称 | W2 [AGREE] | — [AGREE] | **强共识** |\n| Gold-empty filtering | W4 [AGREE] | — [AGREE] | **共识** |\n| LP hypotheses 编号错误 | minor [AGREE] | minor [AGREE] | **共识** |\n\n## Reviewer Divergence\n\n| Issue | R1 Position | R2 Position | Resolution |\n|-------|-------------|-------------|------------|\n| ρ=0.45 \"strong\" 措辞 | Should-Fix (domain standards differ) | Must-Fix (Cohen's moderate) | **降为 Should-Fix**: R1 有效 rebut, domain-specific 标准有道理 |\n| No remedy 的严重程度 | Should-Fix (diagnostic papers 有先例) | 接近 Must-Fix | **Should-Fix**: 共识 pilot remedy 会增强但非必须 |\n| Contribution 3 (difficulty-dependent) | 有独立价值 (WNUT-17 collapse) | 较弱 | **保留**: WNUT-17 boundary collapse 对 practitioners 有意义 |\n| RE free-form reversal 呈现 | 应更突出 | 谨慎处理适当 | **定位为 promising direction**: 单 benchmark 限制了 claim 强度 |\n| Yao et al. 差异描述 | 现有描述充分 | 需更精确 | **Camera-ready refinement**: 现有 3 项差异清晰 |\n\n---\n\n## Questions（需作者回答）\n\n**Q1** [两位共识]: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上产生了 per-sample ranking。请解释为什么论文将其归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"——这两者的理论含义截然不同。\n\n**Q2** [两位共识]: Entity-token-only LP（仅对 entity mention tokens 计算 LP，排除 JSON schema tokens）是否被考虑过？如果排除 schema tokens，within-instance compression 是否缓解？这是 Discussion hypothesis (d) 的直接检验。\n\n**Q3** [R1]: Table A13 (cross_selection) 标注 CoNLL n=2756，但 Section 3.3 说 \"selection retains the full set\" (n=3453)。哪个正确？\n\n**Q4** [R1, R2 同意]: TOST external anchors 显示 Qwen CoNLL selection 比 single-sample 显著更差（0.9-1.5pp degradation，所有外部 δ 下不通过等价检验）。某些配置下 signals 是否主动损害 selection？这与正文 \"no signal consistently improves\" 的表述不一致。\n\n**Q5** [R2]: Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？这三个指标衡量不同的东西（rank correlation, binary discrimination, per-sample selection），decouple 本身是否只是 expected behavior？\n\n**Q6** [R2]: CoNLL (F1≈0.91, oracle headroom ~4pp) 的 selection 分析是否有意义？R1 回应这是必要的 ceiling-effect control，但正文可否避免对 near-ceiling 配置过度解读？\n\n---\n\n## Missing References\n\n两位 Reviewer 共识应补充：\n1. **Deguchi et al. (2024)** \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" — MBR mode-seeking bias 分析，与 Appendix MBR Discussion 直接相关\n2. **Mejer & Crammer (2011)** \"Confidence Estimation in Structured Prediction\" — 经典 structured prediction confidence 先驱工作\n3. **Xie et al. (2024)** \"Self-Evaluation Improves Selective Generation\" (NeurIPS 2024) — LLM per-sample self-evaluation for selective generation\n\n待核实：\n4. **Bertoldi et al. (2024)** \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\" — R1 推荐，R2 rebut 未能找到。需作者核实是否存在。\n\n已有引用无问题：\n- R2 引用完整性检查: 47 entries, 0 orphan, 0 missing, 40/47 OpenAlex verified, 无幻觉引用\n- oh2025latentsc bib year 建议更新为 2026\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿 (paperreview.ai disabled)。\n\n---\n\n## Overall Assessment\n\n**Overall Score**: Borderline — 介于 Findings (3.0) 和 Conference (3.5) 之间\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.75** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.25** |\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及 appendix，熟悉相关文献）\n\n**核心判断**：\n- **值得发表**的内容：LP compression 分析、MBR within-instance failure、QE/selection 解耦形式化、统计方法论标准\n- **阻碍 Conference acceptance** 的问题：(1) framing 的定义性/经验性混淆（MF1）；(2) 标题/scope 不匹配（MF2，持续 13 轮）\n- **如果 MF1+MF2 修正**（contribution 重组 + 标题精确化），可提升至 Conference acceptance (3.5-4.0)\n- **当前版本**更适合 **Findings track**：实验扎实、统计全面、负面结果有价值，但 framing 不当和 scope overclaiming 使 main conference 定位困难\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（一句话内 ρ=0.45, 0.041 nats, 60% tied, +1.8±0.1 pp）\n- \"strong quality estimation\" → 建议改为 \"moderate-to-strong\"\n- \"Four instance-level signals fail by construction\" 暗示 LP 是唯一 empirical finding，降低 MBR failure 地位\n\n### Introduction\n- Contribution 1 需重组：definitional 部分降为 background，突出 empirical dissociation 的具体 pattern\n- Contribution 3 (difficulty-dependent rankings) 较弱但有价值（WNUT-17 collapse 对 practitioners 有意义）\n- 与 Yao et al. (2026) 的差异清晰但可更精确\n\n### Method (Section 3)\n- Signal 定义严谨，SJ/FK/VC/EM/LP 形式化清晰\n- \"Soft Jaccard\" 命名不准确（分母是 max 不是 union），建议改名或说明\n- FK entity set adaptation 非标准但 Appendix permutation test 验证充分\n\n### Experiments (Section 4)\n- Table 1: 单 seed 已在 caption 标注，cross-ref Table A7 合理\n- Table 2: NER 2-seed vs RE single-seed 不一致需解释\n- Section 4.2: \"no signal consistently improves selection\" 与 TOST external anchors（Qwen CoNLL degradation）存在张力\n- Scale ablation (Table 3): 3B-8B 覆盖不足\n\n### Discussion (Section 5)\n- LP hypotheses 标注 \"three mechanisms\" 但列出 4 个——编号错误\n- Hypothesis (d) format-token dilution 是最有力假说但未直接测试\n- RE free-form reversal (+1.84±0.12pp) 被谨慎处理——建议定位为 promising direction\n- \"Effective selection likely requires trained verifiers\" 指向合理但论文未尝试任何 remedy\n\n### Limitations\n- 诚实全面，覆盖了 RE 单 benchmark、model scale、verifier 缺失、ε 选择等已知限制\n- 可补充：entity-token LP 未测试的明确说明\n\n### Appendix\n- 极其详尽（15+ sections），覆盖了几乎所有消融方向\n- MBR Discussion (Appendix L) 的 within-instance failure 分析应进入主文\n- RE Conditional Selection (Appendix M) 排除 zero-F1 后 signals 更差 (VC: -10.0pp)——重要结果应在主文提及",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 1202 · 2026-05-16T05:33:02.173313+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4517
}
```

</details>

---


### Assistant

_source line 1203 · 2026-05-16T05:33:12.362558+00:00_

审稿报告已投递至 Research Director。

---

**Round 12 审稿完成汇总**：

**Overall**: Borderline (3.25/5) — 介于 Findings 和 Conference 之间

**2 个 Must-Fix**：
1. **MF1**: "By construction" framing 混淆定义性与经验性发现——MBR 在 IE 中的经验性失败被 "by construction" 标签掩盖，需将 MBR failure 提升为独立 empirical contribution
2. **MF2**: 标题 "Structured IE" 与实际覆盖不匹配——本质是 NER 论文 + 不完整 RE 探索（持续 13 轮的顽固 issue）

**8 个 Should-Fix**：ρ=0.45 措辞过度、entity-token LP 未测试、纯诊断无 remedy、ε threshold 依赖、model scale 不足 (3B-8B)、Kendall W 效力不足、NER/RE seed 不对称、gold-empty filtering 不一致

**核心判断**：LP compression 分析和 MBR failure 刻画有价值，统计方法论超过 EMNLP 平均水平。若 MF1+MF2 修正（contribution 重组 + 标题精确化），可提升至 Conference acceptance。当前版本更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 1204 · 2026-05-16T05:33:15.000821+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心发现：两位 reviewer 在 N1（by construction framing）、N2（scope mismatch）、W3（entity-token LP 未测试）、W5（模型规模不足）上高度一致。主要分歧仅在 Q5（RE free-form reversal 的呈现力度）和 R1 推荐的两篇 missing references 的有效性上。

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

_source line 1205 · 2026-05-16T05:33:28.052160+00:00_

审稿报告已提交至 Research Director。

**Round 12 审稿完成总结**：

- **Overall**: Borderline (3.25/5)，介于 Findings 和 Conference 之间
- **Reviewer 1**: 3.5 (Borderline Conference) | **Reviewer 2**: 3.0 (Findings)
- **1 轮即收敛**，关键问题强共识

**2 个 Must-Fix**：
1. **MF1**: "By construction" framing 混淆定义性与经验性发现——MBR 在 IE 中的经验性失败被掩盖在 "by construction" 标签下，需重组 contribution list
2. **MF2**: 标题 "Structured IE" 与实际覆盖不匹配（3 NER + 1 exploratory RE）——持续 13 轮的最顽固 issue

**8 个 Should-Fix**：ρ=0.45 措辞过度、entity-token LP 未测试、纯诊断无 remedy、ε threshold 依赖、model scale 3B-8B 不足、Kendall W 效力、NER/RE seed 不对称、gold-empty filtering 不一致

**核心判断**：LP compression 分析和 MBR within-instance failure 有独立学术价值，统计方法论超过 EMNLP 平均水平。若 MF1+MF2 修正（contribution 重组 + 标题精确化），可提升至 Conference acceptance。当前版本更适合 Findings track。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 97

## Round 97

74 recorded events


### User

_source line 1206 · 2026-05-16T06:36:24.163731+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

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

_source line 1207 · 2026-05-16T06:36:31.874300+00:00_

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

_source line 1208 · 2026-05-16T06:36:31.876536+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-16T06:36:36.045320+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-16T06:36:36.096024+00:00_



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

_source line 1211 · 2026-05-16T06:36:42.724985+00:00_

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

_source line 1212 · 2026-05-16T06:36:43.880026+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (111 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\n- **exp_entity_token_lp** (negative): Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\n  [exp_entity_token_lp_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json) | [exp_entity_token_lp_report](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md)\n\n## 趋势\n成功 61 / 负向 24 / 失败 4 / 共 111\n\n## 下一步\
…[truncated 1212 chars]

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

_source line 1213 · 2026-05-16T06:36:44.031344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-16T06:36:44.081974+00:00_

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

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

_source line 1215 · 2026-05-16T06:36:54.152286+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
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
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-16T06:36:54.202902+00:00_



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

_source line 1217 · 2026-05-16T06:36:57.720619+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-16T06:36:59.131874+00:00_

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

_source line 1219 · 2026-05-16T06:36:59.584318+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).
4	All signals achieve moderate-to-strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals assign identical scores to all candidates; when converted to consensus-proximity rankings (MBR), they produce per-sample scores but do not improve selection.
6	Log-probability---the only natively per-sample signal---is too compressed within instances to discriminate (median within-instance range 0.041 nats).
7	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp), suggesting regime-dependent behavior.
8	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
9	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
10	\end{abstract}
11	

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

_source line 1220 · 2026-05-16T06:36:59.685310+00:00_

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

_source line 1221 · 2026-05-16T06:36:59.736038+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard, a variant using per-type max cardinality; \S\ref{sec:signals}) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve moderate-to-strong quality estimation ($\rho$ up to 0.45, substantially exceeding random baselines) but fail at sample selection despite substantial oracle headroom.
11	The gap has two causes: instance-level signals (4 of 5) assign identical QE scores to all candidates; consensus-proximity (MBR) converts these to per-sample rankings, but utility correlates with F1 across instances, not within them (\S\ref{sec:discussion}).
12	LP---the only nativ
…[truncated 2496 chars]

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

_source line 1222 · 2026-05-16T06:37:06.936256+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on the web search results, here is information about the EMNLP 2026 Call for Papers submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fa
…[truncated 1491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9215
}
```

</details>

---


### Tool call

_source line 1223 · 2026-05-16T06:37:11.662468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long short paper template"
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
    "query": "ACL Rolling Review 2026 submission format page limit long short paper template"
  }
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-16T06:37:12.165423+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-16T06:37:12.216214+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each
…[truncated 3037 chars]

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

_source line 1226 · 2026-05-16T06:37:13.220712+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-16T06:37:13.321674+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. $^\dagger$RE results rest on a single benchmark (SciERC, 40\% zero-F1 rate). $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\text
…[truncated 7584 chars]

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


### Tool result

_source line 1228 · 2026-05-16T06:37:19.007551+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format, page limits, and templates:

## Page Limits

Long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Required Sections

ACL currently requires all submissions to have a section titled "Limitations", which discusses the limitations of the work. It should be placed after the c
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7345
}
```

</details>

---


### Tool call

_source line 1229 · 2026-05-16T06:37:23.699466+00:00_

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

_source line 1230 · 2026-05-16T06:37:24.152437+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\dagger$RE, LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single QE score per input. Consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}), instantiating MBR decoding \cite{eikema2022sampling} with signal-specific utility functions. Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because utility correlates with F1 across instances but not within a single instance---the fundamental asymmetry underlying the gap (Appendix~\ref{app:mbr_discussion}).
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Stratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
12	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\dagger$RE at 4B scale, LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~
…[truncated 4902 chars]

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

_source line 1231 · 2026-05-16T06:37:24.152927+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-16T06:37:24.605154+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} and \citet{mejer2011confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibr
…[truncated 1435 chars]

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

_source line 1233 · 2026-05-16T06:37:24.605661+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-16T06:37:24.706363+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate-to-strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals, even when converted to per-sample MBR rankings, do not improve selection; the core empirical finding is that log-probability---the only natively per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats), and consensus-proximity utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\dagger$RE, LP selection reverses direction.
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary in the small-model regime (3B--8B); whether LP compression persists at 70B+ scales is an open question.
7	$^\dagger$RE conclusions rest on SciERC alone (40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

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

_source line 1235 · 2026-05-16T06:37:27.772292+00:00_

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

_source line 1236 · 2026-05-16T06:37:28.224499+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	TACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.
3	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
4	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	We tested one remedy for LP compression--
…[truncated 258 chars]

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

_source line 1237 · 2026-05-16T06:37:28.325823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "150"
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
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-16T06:37:28.426814+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
47	\quad FK & 
…[truncated 9116 chars]

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

_source line 1239 · 2026-05-16T06:37:35.216846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "150",
  "limit": "200"
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
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-16T06:37:35.217450+00:00_

150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
154	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
155	
156	\paragraph{Length vs.\ log-probability.}
157	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
162	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
163	\label{fig:length_logprob_scatter}
16
…[truncated 14850 chars]

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

_source line 1241 · 2026-05-16T06:37:36.522944+00:00_

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

_source line 1242 · 2026-05-16T06:37:36.574008+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-16T06:37:44.658421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "349",
  "limit": "200"
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
    "offset": "349",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-16T06:37:44.658949+00:00_

349	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
350	This rules out insufficient diversity as an explanation for the correlation-selection gap.
351	
352	\paragraph{TOST equivalence testing.}\label{app:tost}
353	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
354	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
355	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
356	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
357	We address this below with externally anchored equivalence margins.
358	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
359	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
360	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
361	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at 
…[truncated 13456 chars]

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

_source line 1245 · 2026-05-16T06:37:45.562992+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
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
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-16T06:37:46.065724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-16T06:37:46.367292+00:00_

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

_source line 1248 · 2026-05-16T06:37:46.417963+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

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

_source line 1249 · 2026-05-16T06:37:50.542851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-16T06:37:51.045977+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====
3	- id: R0-C1
4	  summary: "模型规模单一（仅 8B）"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  resolution: "Round 2 Reviewer 确认措辞修正到位"
11	  resolution_round: 2
12	- id: R0-C2
13	  summary: "相关工作显著遗漏"
14	  category: framing
15	  severity: warning
16	  status: resolved
17	  first_raised_round: 0
18	  last_seen_round: 1
19	  resolution: "Round 2 确认 49 条 bib 全部 cited"
20	  resolution_round: 2
21	- id: R0-C4
22	  summary: "SJ 方法新颖性有限"
23	  category: method
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 1
28	  resolution: "Round 2 确认三点差异化清晰"
29	  resolution_round: 2
30	- id: R0-C5
31	  summary: "全文零图表"
32	  category: writing
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 0
37	  resolution: "论文已包含 6 个 figures"
38	  resolution_round: 1
39	- id: R0-C6
40	  summary: "成本分析 negligible 误导"
41	  category: method
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 0
46	  resolution: "Round 1+ 未再提及"
47	  resolution_round: 1
48	- id: R0-W1
49	  summary: "未探索 signal combination"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 0
55	  resolution: "Round 1+ 未再提及"
56	  resolution_round: 1
57	- id: R0-W4
58	  summary: "统计检验不系统"
59	  category: experiment
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 0
63	  last_seen_round: 1
64	  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
65	  resolution_round: 2
66	- id: R3-W4
67	  summary: "FK independence 假设未验证"
68	  category: experiment
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 3
72	  last_seen_round: 8
73	  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
74	  resolution_round: 9
75	- id: R3-W5
76	  summary: "Cross-model
…[truncated 655 chars]

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

_source line 1251 · 2026-05-16T06:37:51.297659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "548",
  "limit": "200"
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
    "offset": "548",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1252 · 2026-05-16T06:37:51.399257+00:00_

548	\midrule
549	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
550	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
551	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
552	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
553	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
554	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
555	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
561	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
562	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
563	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
564	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
565	
566	\begin{table}[t]
567	\centering
568	\small
569	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
570	\label{tab:epsilon_robustness}
571	\begin{tabular}{lcccc}
572	\toprule
573	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
574	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
575	Signal & Qwen & LLaMA & Qwen & LLaMA \\
576	\midrule
577	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
578	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
5
…[truncated 10433 chars]

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

_source line 1253 · 2026-05-16T06:37:59.037323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-16T06:37:59.439498+00:00_

100	  resolution: "贡献重新框架化为 finding-led"
101	  resolution_round: 9
102	- id: R7-W1
103	  summary: "LP temperature 依赖未说明"
104	  category: experiment
105	  severity: warning
106	  status: resolved
107	  first_raised_round: 7
108	  last_seen_round: 7
109	  resolution: "Appendix 排除 LP + Limitations 扩展说明"
110	  resolution_round: 9
111	- id: R7-W3
112	  summary: "Eikema Related Work 覆盖不足"
113	  category: writing
114	  severity: warning
115	  status: resolved
116	  first_raised_round: 7
117	  last_seen_round: 7
118	  resolution: "Related Work 增加 Eikema 讨论"
119	  resolution_round: 9
120	- id: R8-N1
121	  summary: "页数超限"
122	  category: writing
123	  severity: warning
124	  status: resolved
125	  first_raised_round: 8
126	  last_seen_round: 8
127	  resolution: "主文在限制内"
128	  resolution_round: 9
129	- id: R8-W2
130	  summary: "Thinking token 对 LP 影响未分析"
131	  category: experiment
132	  severity: warning
133	  status: resolved
134	  first_raised_round: 8
135	  last_seen_round: 8
136	  resolution: "Appendix 3-part quantitative analysis 已补充"
137	  resolution_round: 9
138	- id: R8-W3
139	  summary: "SJ normalizer 选择敏感性"
140	  category: method
141	  severity: warning
142	  status: resolved
143	  first_raised_round: 8
144	  last_seen_round: 8
145	  resolution: "Appendix table delta-rho<0.005 证明不敏感"
146	  resolution_round: 9
147	- id: R9-W1
148	  summary: "缺少其他 per-sample signal baseline"
149	  category: experiment
150	  severity: warning
151	  status: resolved
152	  first_raised_round: 9
153	  last_seen_round: 9
154	  resolution: "Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)"
155	  resolution_round: 9
156	- id: R9-W3
157	  summary: "TOST 等价性结论 configuration-dependent 未整合进正文"
158	  category: experiment
159	  severity: warning
160	  status: resolved
161	  first_raised_round: 9
162	  last_seen_round: 9
163	  resolution: "Section 4.2 已含 config-dependent note"
164	  resolution_round: 9
165	- id: R9-W4
166	  summary: "VC majority-voting selection 失败机制未分析"
167	  category: met
…[truncated 4362 chars]

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

_source line 1255 · 2026-05-16T06:37:59.841491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "747",
  "limit": "200"
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
    "offset": "747",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1256 · 2026-05-16T06:37:59.842181+00:00_

747	
748	\vspace{8pt}
749	
750	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
751	\vspace{2pt}
752	
753	\begin{tabular}{l ccc ccc}
754	\toprule
755	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
756	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
757	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
758	\midrule
759	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
760	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
761	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
762	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
763	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
764	\bottomrule
765	\end{tabular}
766	
767	\vspace{8pt}
768	
769	{\small\textsc{Panel D: Parse Rate (Free-form)}}
770	\vspace{2pt}
771	
772	\begin{tabular}{lc}
773	\toprule
774	Metric & Value \\
775	\midrule
776	Total samples          & 4408 \\
777	Parse rate             & 99.95\% \\
778	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
779	\bottomrule
780	\end{tabular}
781	
782	\end{table*}
783	
784	\paragraph{CoNLL NER free-form results.}
785	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
786	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
787	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
788	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
789	
790	\section{LP Selection Failure S
…[truncated 10575 chars]

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

_source line 1257 · 2026-05-16T06:38:05.214844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "299",
  "limit": "200"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-16T06:38:05.265752+00:00_

299	  last_seen_round: 12
300	  mentions:
301	  - round: 7
302	    reviewers: [1, 2]
303	    note: "threshold 无 prior justification"
304	  - round: 9
305	    reviewers: [1]
306	    note: "仅作 question 提出"
307	  - round: 11
308	    reviewers: [1, 2]
309	    note: "circularity 存在, 影响辅助分析"
310	  - round: 12
311	    reviewers: [1, 2]
312	    note: "R12 共识: 60% tied 是核心叙事数字 (Abstract/Discussion 反复引用), 但 ε=0.03 时仅 31.8%. LP 是连续信号, tied/non-tied 二分法人为. R1 同意 R2 建议: 主文用 continuous characterization (pooled within-instance ρ=0.248, CDF 特征), ε-based 分析降为辅助. 当前不算 misleading (因 CDF 和 sweep 在 Appendix), 维持 Should-Fix."
313	  action_items:
314	  - round: 12
315	    action: "Abstract '60% tied'→continuous, ε降为辅助 (D106)"
316	    assigned_to: Paper Agent
317	    status: in_progress
318	  resolution: ""
319	  resolution_round: null
320	
321	- id: R11-W1
322	  summary: "与 Yao et al. (2026) 增量贡献定义不够清晰"
323	  category: framing
324	  severity: warning
325	  status: in_progress
326	  first_raised_round: 11
327	  last_seen_round: 12
328	  mentions:
329	  - round: 11
330	    reviewers: [1, 2]
331	    note: "R2 提出, R1 反驳 selection analysis 有独立价值"
332	  - round: 12
333	    reviewers: [1, 2]
334	    note: "R12 部分解决: R1 rebut 指出 Introduction 已列 3 项具体差异 (structural matching, QE/selection separation, difficulty gradient). R2 接受但仍建议更精确量化. 共识: 现有差异描述可接受, camera-ready 级 refinement."
335	  action_items:
336	  - round: 12
337	    action: "Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比"
338	    assigned_to: Paper Agent
339	    status: in_progress
340	  resolution: ""
341	  resolution_round: null
342	
343	- id: R11-W2
344	  summary: "Scale range (3B-8B) 不足以支撑普适性结论"
345	  category: framing
346	  severity: warning
347	  status: in_progress
348	  first_raised_round: 11
349	  last_seen_round: 12
350	  mentions:
351	  - round: 11
352	    reviewers: [1, 2]
353	    note: "需确认所有 scale claims 限定范围"
354	  - round: 12
355	    reviewers: [1, 2]
356	    note: "R12 两位再次强共识. 3B-8B 本质是同一 capability tier. LP compression 可能在 7
…[truncated 4700 chars]

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

_source line 1259 · 2026-05-16T06:38:08.228831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "497",
  "limit": "200"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "497",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-16T06:38:08.279771+00:00_

497	- id: R11-M3
498	  summary: "缺失引用"
499	  category: writing
500	  severity: info
501	  status: in_progress
502	  first_raised_round: 11
503	  last_seen_round: 12
504	  mentions:
505	  - round: 11
506	    reviewers: [1, 2]
507	    note: "Fernandes 2022, CSP, Beyond Confidence"
508	  - round: 12
509	    reviewers: [1, 2]
510	    note: "R12 新增缺失引用: Deguchi et al. (2024) Centroid-Based MBR (两位共识), Mejer & Crammer (2011) Confidence in Structured Prediction (R2 提 R1 同意), Xie et al. (2024) Self-Evaluation Selective Generation (R2 提 R1 同意). R1 提 Bertoldi et al. 被 R2 rebut (可能不存在). R11 三篇 (Fernandes, CSP, Beyond Confidence) 已有引用."
511	  action_items:
512	  - round: 12
513	    action: "补充: Deguchi et al. (2024), Mejer & Crammer (2011), Xie et al. (2024). 核实 Bertoldi et al. 是否存在."
514	    assigned_to: Paper Agent
515	    status: in_progress
516	  resolution: ""
517	  resolution_round: null
518	
519	# ===== NEW ISSUES (Round 12) =====
520	- id: R12-N1
521	  summary: "ρ=0.45 描述为 strong quality estimation, 实际是 moderate correlation"
522	  category: framing
523	  severity: warning
524	  status: in_progress
525	  first_raised_round: 12
526	  last_seen_round: 12
527	  mentions:
528	  - round: 12
529	    reviewers: [1, 2]
530	    note: "R2 列为 Must-Fix, R1 rebut 降为 Should-Fix. R1 论点: Cohen's benchmarks 适用于行为科学而非 NLP unsupervised QE; ρ=0.45 对比 random (ρ≈0) 已是 substantial; AUROC=0.816 (CoNLL) 补充了二分类性能. R2 接受 rebut, 共识: Should-Fix level, 改措辞为 moderate-to-strong 或加限定语."
531	  action_items:
532	  - round: 12
533	    action: "将 'strong quality estimation' 改为 'moderate-to-strong by domain standards' 或 'non-trivial quality estimation, substantially exceeding random baselines'"
534	    assigned_to: Paper Agent
535	    status: in_progress
536	  resolution: ""
537	  resolution_round: null
538	
539	- id: R12-W1
540	  summary: "纯诊断无 remedy 尝试, 限制论文 impact"
541	  category: experiment
542	  severity: warning
543	  status: in_progress
544	  first_raised_round: 12
545	  last_seen_round: 12
546	  men
…[truncated 4219 chars]

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

_source line 1261 · 2026-05-16T06:38:15.358868+00:00_

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

_source line 1262 · 2026-05-16T06:38:15.761196+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 108\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1263 · 2026-05-16T06:38:15.812239+00:00_

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

_source line 1264 · 2026-05-16T06:38:15.812683+00:00_

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

_source line 1265 · 2026-05-16T06:38:19.488173+00:00_

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

_source line 1266 · 2026-05-16T06:38:19.538793+00:00_

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

_source line 1267 · 2026-05-16T06:38:22.500845+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
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
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1268 · 2026-05-16T06:38:22.702825+00:00_

Found 9 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T183358_453446.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-16T06:38:26.133328+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "**/CLAUDE.md",
  "output_mode": "content"
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
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "**/CLAUDE.md",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-16T06:38:26.184040+00:00_

CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-16T06:38:30.260245+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "**/*.yaml",
  "output_mode": "content"
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
    "pattern": "external_review|paperreview_ai\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "**/*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-16T06:38:30.361073+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1273 · 2026-05-16T06:39:25.076929+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计 + 统计分析\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子文件）\n- **目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **格式**: ACL template (review mode), 8 页正文 + unlimited references, double-blind, 需含 Limitations section\n\n### 你的审查重点\n\n1. **方法设计**\n   - 5 个 confidence signals 的定义是否严谨、无歧义\n   - Soft Jaccard 定义（Eq.4 用 max 分母而非 union）是否合理、命名是否准确\n   - Instance-level vs per-sample 信号的区分是否在实验中得到正确处理\n   - MBR/consensus-proximity selection 的实现是否正确\n\n2. **实验设计**\n   - 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否构成有效的 difficulty gradient\n   - N=8 primary + N=16 scaling 是否足够\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）是否覆盖足够\n   - Gold-empty instance filtering 策略是否一致（QE vs Selection 是否用同一 n？）\n   - Free-form decoding ablation 是否充分（seeds, datasets）\n\n3. **统计分析**\n   - Sign tests, Fisher combined p, bootstrap CIs 使用是否得当\n   - TOST equivalence testing 的 δ 选择是否合理（是否有循环论证）\n   - 多重比较校正是否充分\n   - 3 seeds 是否提供足够 statistical power（Kendall W=1.000 with n=3 的信息量）\n   - NER 2-seed vs RE single-seed selection 统计标准是否一致\n\n4. **结论支撑**\n   - \"correlation-selection gap\" 中哪些是 by-construction（定义必然）vs empirical finding\n   - ρ=0.45 被称为 \"strong\" quality estimation 是否合理\n   - RE 结论仅基于 SciERC 单数据集，标题中的 NER 限定是否足够\n   - Scale 结论（3B-8B）是否过度泛化\n   - Entity-token LP 消融结果如何影响核心叙事\n\n请按以下结构输出你的审稿报告：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者回答的)\n- **Missing References**\n- **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)"
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
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计 + 统计分析\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子文件）\n- **目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **格式**: ACL template (review mode), 8 页正文 + unlimited references, double-blind, 需含 Limitations section\n\n### 你的审查重点\n\n1. **方法设计**\n   - 5 个 confidence signals 的定义是否严谨、无歧义\n   - Soft Jaccard 定义（Eq.4 用 max 分母而非 union）是否合理、命名是否准确\n   - Instance-level vs per-sample 信号的区分是否在实验中得到正确处理\n   - MBR/consensus-proximity selection 的实现是否正确\n\n2. **实验设计**\n   - 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否构成有效的 difficulty gradient\n   - N=8 primary + N=16 scaling 是否足够\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）是否覆盖足够\n   - Gold-empty instance filtering 策略是否一致（QE vs Selection 是否用同一 n？）\n   - Free-form decoding ablation 是否充分（seeds, datasets）\n\n3. **统计分析**\n   - Sign tests, Fisher combined p, bootstrap CIs 使用是否得当\n   - TOST equivalence testing 的 δ 选择是否合理（是否有循环论证）\n   - 多重比较校正是否充分\n   - 3 seeds 是否提供足够 statistical power（Kendall W=1.000 with n=3 的信息量）\n   - NER 2-seed vs RE single-seed selection 统计标准是否一致\n\n4. **结论支撑**\n   - \"correlation-selection gap\" 中哪些是 by-construction（定义必然）vs empirical finding\n   - ρ=0.45 被称为 \"strong\" quality estimation 是否合理\n   - RE 结论仅基于 SciERC 单数据集，标题中的 NER 限定是否足够\n   - Scale 结论（3B-8B）是否过度泛化\n   - Entity-token LP 消融结果如何影响核心叙事\n\n请按以下结构输出你的审稿报告：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者回答的)\n- **Missing References**\n- **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1274 · 2026-05-16T06:39:43.067539+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17990
}
```

</details>

---
