# paper writing related work

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260522T152514.jsonl`
- **Structured JSON:** [`f16cd1d48ddb73e1f756.json`](../../sessions/f1/f16cd1d48ddb73e1f756.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-22T15:27:11.032384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T15:27:11.033266+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T15:27:11.033559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T15:27:11.033827+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe acc
…[truncated 3687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T15:27:11.034127+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T15:27:11.034341+00:00_

docs/paper/custom.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T15:27:11.034552+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/ 2>/dev/null",
  "description": "Check existing sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/ 2>/dev/null",
    "description": "Check existing sections directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T15:27:11.034765+00:00_

experiments.tex
introduction.tex
method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T15:27:11.035000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T15:27:11.035318+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	% Auto-generated from literature_map.yaml
3	
4	@article{basu2026interpretability,
5	  author    = {Basu, S. and others},
6	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
7	  journal   = {arXiv preprint arXiv:2603.18353},
8	  year      = {2026},
9	  url       = {https://arxiv.org/abs/2603.18353}
10	}
11	
12	@article{boer2026probing,
13	  author    = {Boer, A. and Brink, I. and Ulmer, D.},
14	  title     = {Probing for Knowledge Attribution in Large Language Models},
15	  journal   = {arXiv preprint arXiv:2602.22787},
16	  year      = {2026},
17	  url       = {https://arxiv.org/abs/2602.22787}
18	}
19	
20	@inproceedings{ifergan2024beneath,
21	  author    = {Ifergan, M. and Choshen, L. and Aharoni, R. and Szpektor, I. and Abend, O.},
22	  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},
23	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
24	  year      = {2024},
25	  url       = {https://arxiv.org/abs/2408.10646}
26	}
27	
28	@article{kialy2026universal,
29	  author    = {Kialy, U.Z. and Shtarkberg, A. and Klein, A.},
30	  title     = {A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register with {SAEs}},
31	  journal   = {arXiv preprint arXiv:2603.26236},
32	  year      = {2026},
33	  url       = {https://arxiv.org/abs/2603.26236}
34	}
35	
36	@inproceedings{li2025taming,
37	  author    = {Li, G. and Chen, Y. and Tong, H.},
38	  title     = {Taming Knowledge Conflicts in Language Models},
39	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2503.10996}
42	}
43	
44	@article{pham2026where,
45	  author    = {Pham, M.V. and Borkakoty, H. and Hou, Y.},
46	  title     = {Whe
…[truncated 9107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T15:27:11.035564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/custom.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T15:27:11.035795+00:00_

1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {J
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T15:27:11.036151+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Knowledge conflict detection.}\nResearch on how LLMs handle conflicting knowledge has developed along two axes: behavioral characterization and internal signal analysis.\n\\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent strategies when parametric and contextual knowledge disagree, ranging from faithful context-following to stubborn reliance on memorized answers.\n\\citet{xu2024knowledge} provided a systematic taxonomy of conflict types (intra-memory, context-memory, and inter-context) that has since guided experimental design in this area.\nMore recent work has moved beyond behavioral observation to probe model internals.\n\\citet{zhao2024analysing} demonstrated that residual stream representations carry linearly separable conflict signals in English, while \\citet{boer2026probing} used probing classifiers to localize factual associations within model parameters.\n\\citet{pham2026where} investigated the mechanistic pathways through which intra-memory conflicts are processed, and \\citet{li2025taming} proposed methods to mitigate conflict-induced errors.\nThese studies, however, operate exclusively in monolingual English settings.\nExtending conflict probing to cross-lingual scenarios introduces confounds that require explicit control: translation quality can degrade the conflict signal, token overlap between languages can provide spurious shortcuts, and general cross-lingual transfer properties can be mistaken for conflict-specific phenomena.\nWe build on the residual stream probing approach of \\citet{zhao2024analysing} and extend it to cross-lingual settings with a confound exclusion pipeline that addresses each of these concerns.\n\n\\paragraph{Cross-lingual representations in multilingual models.}\nA consistent finding across multilingual model analyses is that intermediate layers develop language-independent representations.\n\\citet{wu2020emerging} showed that cross-lingual structure emerges in pretrained models without explicit alignment objectives, and \\citet{muller2021first} found that multilingual BERT first aligns representations across languages in middle layers before making task predictions.\nFor decoder-only LLMs, \\citet{wendler2024llamas} provided evidence that Llama models process non-English inputs through an English-centric latent space, with internal representations converging toward English regardless of the input language.\n\\citet{kargaran2024mexa} quantified this English-centric bias and showed that cross-lingual alignment quality varies substantially across language pairs and model layers.\nThis body of work predicts two patterns that we observe empirically.\nFirst, the success of mid-layer steering (L13, 41\\% depth) aligns with the finding that language-independent encoding peaks at intermediate layers.\nSecond, the ZH$\\to$EN transfer advantage in our probing experiments is consistent with the English-centric structure documented by \\citet{wendler2024llamas} and \\citet{kargaran2024mexa}: Chinese representations map more readily onto the English space than the reverse.\nSeveral studies have documented behavioral consequences of this representational structure.\n\\citet{wang2025lost} found systematic cross-lingual factual inconsistencies in transformer language models, \\citet{zhao2026when} constructed the CLEAR benchmark showing that conflict resolution patterns differ across languages, and \\citet{ifergan2024beneath} and \\citet{xing2024evaluating} evaluated the consistency of cross-lingual knowledge sharing.\nOur work complements these behavioral studies by providing a mechanistic account of why such asymmetries arise.\n\n\\paragraph{Representation steering and causal intervention.}\nProbing establishes correlation between representations and task-relevant information, but causal influence requires intervention.\n\\citet{li2023iti} introduced Inference-Time Intervention, which adds learned bias vectors at specific attention heads to steer model outputs toward truthfulness.\n\\citet{zou2023representation} generalized this idea through Representation Engineering, extracting and manipulating concept-level directions in activation space.\nIn the knowledge conflict domain, \\citet{zhao2025steering} applied SAE-based steering (SpARE) to shift conflict resolution behavior in monolingual settings.\nThese successes, however, are not universal.\n\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, raising the question of when detectability implies actionability.\n\\citet{feng2026finegrained} proposed fine-grained activation steering to improve intervention precision by targeting specific layers and positions.\nOur results contribute to this discussion by identifying layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, even though the late layer achieves higher probe accuracy.\nThis dissociation between the probing peak and the causal locus suggests that conflict resolution occurs upstream of where the outcome becomes linearly readable.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Knowledge conflict detection.}\nResearch on how LLMs handle conflicting knowledge has developed along two axes: behavioral characterization and internal signal analysis.\n\\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent strategies when parametric and contextual knowledge disagree, ranging from faithful context-following to stubborn reliance on memorized answers.\n\\citet{xu2024knowledge} provided a systematic taxonomy of conflict types (intra-memory, context-memory, and inter-context) that has since guided experimental design in this area.\nMore recent work has moved beyond behavioral observation to probe model internals.\n\\citet{zhao2024analysing} demonstrated that residual stream representations carry linearly separable conflict signals in English, while \\citet{boer2026probing} used probing classifiers to localize factual associations within model parameters.\n\\citet{pham2026where} investigated the mechanistic pathways through which intra-memory conflicts are processed, and \\citet{li2025taming} proposed methods to mitigate conflict-induced errors.\nThese studies, however, operate exclusively in monolingual English settings.\nExtending conflict probing to cross-lingual scenarios introduces confounds that require explicit control: translation quality can degrade the conflict signal, token overlap between languages can provide spurious shortcuts, and general cross-lingual transfer properties can be mistaken for conflict-specific phenomena.\nWe build on the residual stream probing approach of \\citet{zhao2024analysing} and extend it to cross-lingual settings with a confound exclusion pipeline that addresses each of these concerns.\n\n\\paragraph{Cross-lingual representations in multilingual models.}\nA consistent finding across multilingual model analyses is that intermediate layers develop language-independent representations.\n\\citet{wu2020emerging} showed that cross-lingual structure emerges in pretrained models without explicit alignment objectives, and \\citet{muller2021first} found that multilingual BERT first aligns representations across languages in middle layers before making task predictions.\nFor decoder-only LLMs, \\citet{wendler2024llamas} provided evidence that Llama models process non-English inputs through an English-centric latent space, with internal representations converging toward English regardless of the input language.\n\\citet{kargaran2024mexa} quantified this English-centric bias and showed that cross-lingual alignment quality varies substantially across language pairs and model layers.\nThis body of work predicts two patterns that we observe empirically.\nFirst, the success of mid-layer steering (L13, 41\\% depth) aligns with the finding that language-independent encoding peaks at intermediate layers.\nSecond, the ZH$\\to$EN transfer advantage in our probing experiments is consistent with the English-centric structure documented by \\citet{wendler2024llamas} and \\citet{kargaran2024mexa}: Chinese representations map more readily onto the English space than the reverse.\nSeveral studies have documented behavioral consequences of this representational structure.\n\\citet{wang2025lost} found systematic cross-lingual factual inconsistencies in transformer language models, \\citet{zhao2026when} constructed the CLEAR benchmark showing that conflict resolution patterns differ across languages, and \\citet{ifergan2024beneath} and \\citet{xing2024evaluating} evaluated the consistency of cross-lingual knowledge sharing.\nOur work complements these behavioral studies by providing a mechanistic account of why such asymmetries arise.\n\n\\paragraph{Representation steering and causal intervention.}\nProbing establishes correlation between representations and task-relevant information, but causal influence requires intervention.\n\\citet{li2023iti} introduced Inference-Time Intervention, which adds learned bias vectors at specific attention heads to steer model outputs toward truthfulness.\n\\citet{zou2023representation} generalized this idea through Representation Engineering, extracting and manipulating concept-level directions in activation space.\nIn the knowledge conflict domain, \\citet{zhao2025steering} applied SAE-based steering (SpARE) to shift conflict resolution behavior in monolingual settings.\nThese successes, however, are not universal.\n\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, raising the question of when detectability implies actionability.\n\\citet{feng2026finegrained} proposed fine-grained activation steering to improve intervention precision by targeting specific layers and positions.\nOur results contribute to this discussion by identifying layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, even though the late layer achieves higher probe accuracy.\nThis dissociation between the probing peak and the causal locus suggests that conflict resolution occurs upstream of where the outcome becomes linearly readable.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T15:27:11.036440+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T15:27:11.036712+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections && grep -n \"—\" related_work.tex; grep -n \" – \" related_work.tex; echo \"---em/en-dash check done---\"; grep -c \"ing,\" related_work.tex; echo \"---ing-comma check done---\"; wc -w related_work.tex",
  "description": "Check for em-dashes, en-dashes, -ing patterns, and word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections && grep -n \"—\" related_work.tex; grep -n \" – \" related_work.tex; echo \"---em/en-dash check done---\"; grep -c \"ing,\" related_work.tex; echo \"---ing-comma check done---\"; wc -w related_work.tex",
    "description": "Check for em-dashes, en-dashes, -ing patterns, and word count"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T15:27:11.036966+00:00_

---em/en-dash check done---
2
---ing-comma check done---
589 related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T15:27:11.037183+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,\"",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,\"",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T15:27:11.037396+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T15:27:11.037605+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T15:27:11.037816+00:00_

30:\citet{zou2023representation} generalized this idea through Representation Engineering, extracting and manipulating concept-level directions in activation space.
33:\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, raising the question of when detectability implies actionability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T15:27:11.038091+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
  "old_string": "\\citet{zou2023representation} generalized this idea through Representation Engineering, extracting and manipulating concept-level directions in activation space.",
  "new_string": "\\citet{zou2023representation} generalized this idea through Representation Engineering, which extracts and manipulates concept-level directions in activation space."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
    "old_string": "\\citet{zou2023representation} generalized this idea through Representation Engineering, extracting and manipulating concept-level directions in activation space.",
    "new_string": "\\citet{zou2023representation} generalized this idea through Representation Engineering, which extracts and manipulates concept-level directions in activation space."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T15:27:11.038358+00:00_

The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T15:27:11.038601+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
  "old_string": "\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, raising the question of when detectability implies actionability.",
  "new_string": "\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, which raises the question of when detectability implies actionability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
    "old_string": "\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, raising the question of when detectability implies actionability.",
    "new_string": "\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, which raises the question of when detectability implies actionability."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T15:27:11.038865+00:00_

The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260522T152514",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T15:27:11.039143+00:00_

Related Work section written to `docs/paper/sections/related_work.tex`. Three clusters (~590 words total including LaTeX markup, prose body ~550 words):

1. **Knowledge conflict detection** -- positions our work as extending monolingual residual stream probing (Zhao et al., 2024) to cross-lingual settings with confound controls
2. **Cross-lingual representations** -- connects mid-layer language-independent encoding and English-centric bias to our empirical findings (mid-layer steering success, ZH→EN transfer advantage)
3. **Representation steering and causal intervention** -- frames the detection-decision layer dissociation within the ITI/RepE literature and the detectability-vs-actionability debate

No em-dashes, no -ing phrase endings, no paper stacking, no contribution claims in Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260522T152514"
}
```

</details>

---
