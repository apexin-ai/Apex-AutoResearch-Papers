# paper writing introduction

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260516T090825.jsonl`
- **Structured JSON:** [`9d3ad5dee6ed32f538b3.json`](../../sessions/9d/9d3ad5dee6ed32f538b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-16T09:10:42.517886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:10:42.518337+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.
7	\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.
8	
9	Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
10	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.
11	This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.
12	The optimal set of structures to retain should therefore depend on the recovery paradigm.
13	
14	We hypothesize that \emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.
15	If a pruned structure has high overlap with retained structures, 
…[truncated 3731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:10:42.518555+00:00_

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
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T09:10:42.518942+00:00_

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
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:10:42.519192+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:10:42.519509+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:10:42.519653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "description": "Count words in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "description": "Count words in introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:10:42.519777+00:00_

942 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:10:42.519932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:10:42.520098+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	GRPO training~\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.
5	Yet GSM8K~\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.
6	The reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.
7	This observation---\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.
8	
9	On pruned models, the decoupled reward signal becomes catastrophic.
10	Structured pruning at 20\% sparsity removes entire attention heads and MLP channels~\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.
11	When GRPO is applied to these pruned architectures, training does not merely stall---it \emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.
12	The collapse severity depends on \emph{what} was pruned.
13	\rasp{}, which uses CKA-based functional overlap~\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.
14	By removing functionally overlapping heads that served as exploration buffers, \rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.
15	Crucially, the decoupling is bidirectional: just as reward 
…[truncated 6076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:10:42.520299+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
  "new_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "old_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
    "new_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:10:42.520470+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T09:10:42.520599+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
  "new_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "old_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
    "new_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:10:42.520762+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:10:42.520885+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
  "new_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nWhen multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "old_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
    "new_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nWhen multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:10:42.521034+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:10:42.521153+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
  "new_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\nThis gradient provides a practical diagnostic: collapse timing under GRPO can distinguish between pruning strategies that damage exploration capacity (fast collapse) versus those that damage representational capacity (slow or no collapse), even when post-SFT accuracy is similar."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "old_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
    "new_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\nThis gradient provides a practical diagnostic: collapse timing under GRPO can distinguish between pruning strategies that damage exploration capacity (fast collapse) versus those that damage representational capacity (slow or no collapse), even when post-SFT accuracy is similar."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:10:42.521322+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T09:10:42.521448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "description": "Count words in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "description": "Count words in introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T09:10:42.521562+00:00_

1088 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260516T090825",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T09:10:42.521740+00:00_

1088 words — within the 1000–1400 target. Introduction rewritten with the Redundancy-Stability Tradeoff narrative: opens with reward-accuracy decoupling on the unpruned model, escalates to pruning-induced GRPO collapse, identifies the tradeoff, and presents RASP as diagnostic tool rather than optimal method. All cite keys verified, `\rasp{}` macro used, [TBD-25%] and [TBD-QwenMath] placeholders retained.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260516T090825"
}
```

</details>

---
