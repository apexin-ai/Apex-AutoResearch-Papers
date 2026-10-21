# paper writing related work

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260515T051223.jsonl`
- **Structured JSON:** [`80cea496213c6be712e3.json`](../../sessions/80/80cea496213c6be712e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T05:15:47.794167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T05:15:47.794768+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T05:15:47.794961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T05:15:47.795138+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
15	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
16	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
17	
18	RASP differs from all the above in that it optimizes the pruning decision for post-RLV
…[truncated 3917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T05:15:47.795316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T05:15:47.795599+00:00_

1	papers:
2	  # === Direct Competitors ===
3	  - id: self_healing_2025
4	    title: "Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning"
5	    authors: "未确认完整作者列表（OpenReview: Cy8Qa4gAst）"
6	    year: 2025
7	    venue: "under review (OpenReview Oct 2025)"
8	    category: direct-competitor
9	    role: "RLVR recovery baseline"
10	    relevance: 9
11	    key_finding: "RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%"
12	    our_relation: "We extend beyond single sparsity ratio and add CKA-guided pruning selection"
13	    arxiv_id: ""
14	
15	  - id: resp_2025
16	    title: "RESP: Self-Reflective Structured Pruning for Reasoning LLMs"
17	    authors: ""
18	    year: 2025
19	    venue: "arXiv Dec 2025"
20	    category: direct-competitor
21	    role: "Structured pruning for reasoning without recovery"
22	    relevance: 8
23	    key_finding: "GSM8K 81.3% at 40% sparsity via self-reflective importance"
24	    our_relation: "No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity"
25	    arxiv_id: "2512.02185"
26	
27	  - id: grasprune_2026
28	    title: "GRASPrune: Global Gating-based Structural Pruning for LLMs"
29	    authors: ""
30	    year: 2026
31	    venue: "ACL 2026 Main"
32	    category: direct-competitor
33	    role: "SOTA budgeted structural pruning"
34	    relevance: 8
35	    key_finding: "Global gating achieves best structured pruning under budget constraints"
36	    our_relation: "GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top"
37	    arxiv_id: ""
38	
39	  - id: opsd_2026
40	    title: "OPSD: One-shot Post-RL Structured Distillation"
41	    authors: ""
42	    year: 2026
43	    venue: "arXiv May 2026"
44	    category: direct-competitor
45	    role: "Post-RL compression via distillation"
46	    relevance: 7
47	    key_finding: "Compress post-RL model in one shot via structured distillation"
48	    our_relation: "Distillation-based vs our pruning+recovery approach; complementar
…[truncated 20265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T05:15:47.795766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T05:15:47.795955+00:00_

1	@article{deepseek2025r1,
2	  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
3	  author={{DeepSeek-AI}},
4	  journal={arXiv preprint arXiv:2501.12948},
5	  year={2025},
6	  url={https://arxiv.org/abs/2501.12948}
7	}
8	
9	@article{qwen2.5,
10	  title={Qwen2.5 Technical Report},
11	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},
12	  journal={arXiv preprint arXiv:2412.15115},
13	  year={2024},
14	  url={https://arxiv.org/abs/2412.15115}
15	}
16	
17	@article{cobbe2021gsm8k,
18	  title={Training Verifiers to Solve Math Word Problems},
19	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
20	  journal={arXiv preprint arXiv:2110.14168},
21	  year={2021},
22	  url={https://arxiv.org/abs/2110.14168}
23	}
24	
25	@article{shao2024grpo,
26	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
27	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
28	  journal={arXiv preprint arXiv:2402.03300},
29	  year={2024},
30	  url={https://arxiv.org/abs/2402.03300}
31	}
32	
33	@inproceedings{llmpruner2023,
34	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
35	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
36	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
37	  year={2023},
38	  url={https://arxiv.org/abs/2305.11627}
39	}
40	
41	@inproceedings{graspprune2026,
42	  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},
43	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
44	  booktitle
…[truncated 9720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T05:15:47.796098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T05:15:47.796343+00:00_

1	\section{Method: Recovery-Aware Structured Pruning}
2	\label{sec:method}
3	
4	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.
5	The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.
17	We treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm, following~\citet{selfhealing2025}.
22	
23	\subsection{Stage 1: Reasoning-Trace Structural Analysis}
24	\label{sec:stage1}
25	
26	\rasp{} computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's
…[truncated 10638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T05:15:47.796611+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/",
  "description": "List paper output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/",
    "description": "List paper output directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T05:15:47.796752+00:00_

abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
limitations.tex
main.tex
method.tex
references.bib
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T05:15:47.796897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T05:15:47.797062+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	SSGR~\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.
15	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
16	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
17	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, s
…[truncated 5984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T05:15:47.797315+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning for LLMs}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both orthogonal to the width-level structural pruning we study.\n\nFor reasoning models, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction improves unstructured and semi-structured pruning but does not extend to full structural pruning.\n\\rasp{} differs from all the above in optimizing the pruning decision for post-RLVR recoverability rather than immediate accuracy preservation.\n\n\\subsection{Pruning-Aware Recovery}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects recoverability.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-pruning recovery but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold-based budget allocation---complementary to \\rasp{}, which optimizes which \\emph{structures} to prune.\nPAT~\\citep{pat2025} jointly considers pruning and fine-tuning objectives, outperforming the sequential prune-then-finetune pipeline.\n\\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models through incremental SFT recovery.\nRestoreLCC~\\citep{restorelcc_2025} takes a complementary approach, recovering pruned models through activation-level lost component compensation without retraining.\n\nAll these methods treat pruning as a black box and optimize recovery independently.\n\\rasp{} closes this gap by making the pruning decision itself recovery-aware.\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from scratch; \\rasp{} extends this to \\emph{paradigm-conditioned trainability}: the optimal subnetwork depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for \\rasp{}---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization.\nGRPO~\\citep{shao2024grpo}, as instantiated in DeepSeek-R1~\\citep{deepseek2025r1}, serves as both the foundational RL algorithm and the recovery paradigm in our framework.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been applied to pruning, but at a fundamentally different granularity.\nAmong representation similarity measures, \\citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\\% layer identification accuracy versus 45.4\\% for SVCCA, owing to its invariance to invertible linear transforms---properties critical for comparing heterogeneous structures within the same layer.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning, removing entire layers whose representations resemble adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning.\nBoth operate at the layer level; in contrast, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth) optimizing for a different objective (post-recovery reasoning vs.\\ immediate accuracy).\n\n\\paragraph{Function-aware pruning.}\nFANG~\\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss.\nFuncNet~\\citep{funcnet_2025} applies Independent Component Analysis from neuroimaging to decompose LLMs into functional networks and preserves key neurons within each.\nBoth share \\rasp{}'s motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning for LLMs}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both orthogonal to the width-level structural pruning we study.\n\nFor reasoning models, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction improves unstructured and semi-structured pruning but does not extend to full structural pruning.\n\\rasp{} differs from all the above in optimizing the pruning decision for post-RLVR recoverability rather than immediate accuracy preservation.\n\n\\subsection{Pruning-Aware Recovery}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects recoverability.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-pruning recovery but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold-based budget allocation---complementary to \\rasp{}, which optimizes which \\emph{structures} to prune.\nPAT~\\citep{pat2025} jointly considers pruning and fine-tuning objectives, outperforming the sequential prune-then-finetune pipeline.\n\\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models through incremental SFT recovery.\nRestoreLCC~\\citep{restorelcc_2025} takes a complementary approach, recovering pruned models through activation-level lost component compensation without retraining.\n\nAll these methods treat pruning as a black box and optimize recovery independently.\n\\rasp{} closes this gap by making the pruning decision itself recovery-aware.\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from scratch; \\rasp{} extends this to \\emph{paradigm-conditioned trainability}: the optimal subnetwork depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for \\rasp{}---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization.\nGRPO~\\citep{shao2024grpo}, as instantiated in DeepSeek-R1~\\citep{deepseek2025r1}, serves as both the foundational RL algorithm and the recovery paradigm in our framework.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been applied to pruning, but at a fundamentally different granularity.\nAmong representation similarity measures, \\citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\\% layer identification accuracy versus 45.4\\% for SVCCA, owing to its invariance to invertible linear transforms---properties critical for comparing heterogeneous structures within the same layer.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning, removing entire layers whose representations resemble adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning.\nBoth operate at the layer level; in contrast, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth) optimizing for a different objective (post-recovery reasoning vs.\\ immediate accuracy).\n\n\\paragraph{Function-aware pruning.}\nFANG~\\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss.\nFuncNet~\\citep{funcnet_2025} applies Independent Component Analysis from neuroimaging to decompose LLMs into functional networks and preserves key neurons within each.\nBoth share \\rasp{}'s motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T05:15:47.797600+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T05:15:47.797781+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper && grep -oP '\\\\cite[tp]*\\{[^}]+\\}' related_work.tex | grep -oP '[a-zA-Z0-9_]+' | grep -v 'citep\\|citet\\|citealp\\|cite' | sort -u",
  "description": "Extract all citation keys from related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper && grep -oP '\\\\cite[tp]*\\{[^}]+\\}' related_work.tex | grep -oP '[a-zA-Z0-9_]+' | grep -v 'citep\\|citet\\|citealp\\|cite' | sort -u",
    "description": "Extract all citation keys from related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T05:15:47.797923+00:00_

boiling_frog_2026
bonsai2025
deepseek2025r1
doingmore2026
fang_2025
frankle2019lth
funcnet_2025
graspprune2026
klabunde_similarity_survey_2025
kornblith2019cka
lachance2024cka
llmpruner2023
llms2lrms2026
mpruner2024
opsd2026
p2law2025
paser2025
pat2025
rac2025
resp2025
restorelcc_2025
rlsqueezes2026
selfhealing2025
shao2024grpo
shortgpt2024
slicegpt2024
wanda2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T05:15:47.798047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~]//g; s/%.*//; s/---/ /g; s/--/ /g; s/\\\\\\\\//g' | wc -w",
  "description": "Estimate word count excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "tool_args": {
    "command": "cat related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~]//g; s/%.*//; s/---/ /g; s/--/ /g; s/\\\\\\\\//g' | wc -w",
    "description": "Estimate word count excluding LaTeX commands"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T05:15:47.798161+00:00_

658

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T05:15:47.798319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat related_work.tex | sed 's/\\\\citep{[^}]*}/(citation)/g; s/\\\\citet{[^}]*}/(citation)/g; s/\\\\citealp{[^}]*}/(citation)/g; s/\\\\rasp{}/ RASP /g; s/\\\\emph{/ /g; s/\\\\textbf{/ /g; s/\\\\textsuperscript{[^}]*}/ /g; s/\\\\label{[^}]*}//g; s/\\\\section{[^}]*}//g; s/\\\\subsection{[^}]*}//g; s/\\\\paragraph{[^}]*}//g' | sed 's/[{}~]/ /g; s/\\\\\\\\/ /g; s/---/ /g; s/--/ /g; s/%.*//; s/\\\\[a-z]*//g' | wc -w",
  "description": "Better word count estimate for rendered text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "tool_args": {
    "command": "cat related_work.tex | sed 's/\\\\citep{[^}]*}/(citation)/g; s/\\\\citet{[^}]*}/(citation)/g; s/\\\\citealp{[^}]*}/(citation)/g; s/\\\\rasp{}/ RASP /g; s/\\\\emph{/ /g; s/\\\\textbf{/ /g; s/\\\\textsuperscript{[^}]*}/ /g; s/\\\\label{[^}]*}//g; s/\\\\section{[^}]*}//g; s/\\\\subsection{[^}]*}//g; s/\\\\paragraph{[^}]*}//g' | sed 's/[{}~]/ /g; s/\\\\\\\\/ /g; s/---/ /g; s/--/ /g; s/%.*//; s/\\\\[a-z]*//g' | wc -w",
    "description": "Better word count estimate for rendered text"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T05:15:47.798449+00:00_

702

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260515T051223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T05:15:47.798624+00:00_

Verification complete:

1. **All 27 citation keys exist in references.bib** -- no CITATION NEEDED placeholders required
2. **5 clusters covered**: Structured Pruning (\subsection), Pruning-Aware Recovery (\subsection), RLVR Training Dynamics (\subsection), CKA-based pruning (\paragraph), Function-aware pruning (\paragraph)
3. **~700-800 rendered words** -- within the ~800 budget, well under 1000
4. **Each cluster has a \rasp{} positioning statement**
5. **No 35% sparsity references**

Changes from the previous version:
- `RASP` → `\rasp{}` for macro consistency with method.tex
- Added GRPO and DeepSeek-R1 citations to Cluster 3 (was missing)
- Removed `ssgr2025` citation (not in the required outline)
- Tightened prose throughout (removed redundant detail like venue notes, specific numbers from cited papers)
- Reorganized Function-Aware Pruning as a standalone `\paragraph` per the outline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260515T051223"
}
```

</details>

---
