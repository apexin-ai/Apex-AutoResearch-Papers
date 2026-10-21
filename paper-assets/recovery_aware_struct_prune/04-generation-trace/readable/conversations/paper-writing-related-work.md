# paper writing related work

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_related-work_20260515T045854.jsonl`
- **Structured JSON:** [`1ecaa6f8eb3e1a0f53c5.json`](../../sessions/1e/1ecaa6f8eb3e1a0f53c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-15T05:01:24.110246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/literature_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/literature_notes.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T05:01:24.110875+00:00_

1	# Related Work Literature Notes
2	
3	> Generated 2026-05-15. Verified via WebSearch + WebFetch.
4	
5	## Core Comparisons
6	
7	### 1. Self-Healing (2025)
8	- **Full Title**: Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning
9	- **Authors**: Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang
10	- **Venue/Year**: ICLR 2026 (submitted Sep 2025, modified Feb 2026)
11	- **arXiv**: Not found on arXiv; OpenReview ID: Cy8Qa4gAst
12	- **Core Method**: First work applying RLVR (reinforcement learning with verifiable reward) to recover pruned large reasoning models. Shows that structured pruning degrades math reasoning but doesn't destroy it — leaving room for RL-based recovery. RLVR treats recovery as active exploration rather than passive imitation (SFT).
13	- **Key Results**: At 25% compression, RLVR recovery achieves >95% accuracy vs ~80% with SFT across 5 LRMs on 6 math benchmarks, nearly matching unpruned performance.
14	- **vs RASP**: Self-Healing tests RLVR recovery with standard importance-based pruning at a single sparsity ratio. RASP optimizes the pruning decision itself FOR recovery by predicting recoverability via CKA, yielding better accuracy at the same sparsity+recovery budget.
15	
16	### 2. GRASPrune (ACL 2026)
17	- **Full Title**: GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models
18	- **Authors**: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, Jianbin Qin
19	- **Venue/Year**: ACL 2026 Main
20	- **arXiv**: 2604.19398 (Apr 2026)
21	- **Core Method**: Jointly prunes FFN channels and KV head groups under a single global budget. Learns lightweight gate scores with a projected straight-through estimator enforcing a hard mask at every step, backbone weights frozen. Post-mask calibration of scaling factors mitigates scale mismatch.
22	- **Key Results**: LLaMA-2-7B at 50% params → 12.18 PPL on WikiText-2 with competitive zero-shot accuracy. At 0.4 retention
…[truncated 12024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T05:01:24.111152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T05:01:24.111412+00:00_

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
…[truncated 7344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T05:01:24.111604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T05:01:24.111816+00:00_

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
…[truncated 10077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T05:01:24.111964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/_project/paper/figure_plan.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/_project/paper/figure_plan.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T05:01:24.112149+00:00_

1	# Figure Plan — Recovery-Aware Structured Pruning (RASP)
2	
3	---
4	
5	## Fig 1: RASP Pipeline Overview
6	
7	**类型**: 流程/架构图（method figure）
8	
9	**内容**:
10	```
11	Pre-trained Reasoning LLM (DeepSeek-R1-Distill-Qwen-7B)
12	        │
13	        ├──────────────────────────┐
14	        ▼                          ▼
15	  Importance I(h)           CKA Overlap F(h)
16	  (Taylor gradient)        (intra-layer pairwise)
17	        │                          │
18	        └──────────┬───────────────┘
19	                   ▼
20	        RASP Score: S(h) = I(h) × (1 - F(h))^α
21	                   │
22	                   ▼
23	        Structured Pruning (remove lowest S(h))
24	                   │
25	                   ▼
26	        ┌──────────┴──────────┐
27	        ▼                     ▼
28	  SFT Warmup              [对比: Standard Pruning]
29	  (fix generation)         只用 I(h), 无 F(h) 修正
30	        │
31	        ▼
32	  GRPO RLVR Recovery
33	  (restore reasoning)
34	        │
35	        ▼
36	  Recovered Compact Model
37	```
38	
39	**关键设计要素**:
40	- 左侧主 pipeline 用蓝色系，右侧 Standard 对比用灰色/红色
41	- I(h) 和 F(h) 分支用不同颜色区分（如蓝 vs 橙），在合并处突出 RASP scoring 公式
42	- Standard pruning 旁路用虚线表示，标注 "importance-only"
43	- Recovery 阶段标注 "SFT Warmup → GRPO" 两步
44	- 在 CKA Overlap 框旁加小示意：同层 head 间 pairwise CKA matrix
45	
46	**数据可用性**: 无需实验数据，纯方法示意图
47	
48	**建议工具**: TikZ（最佳）或 matplotlib + patches + FancyArrowPatch
49	
50	**论文位置**: Section 3 (Method) 开头，首次引用
51	
52	**尺寸**: 双栏宽度（full width），高度约 6-8cm
53	
54	---
55	
56	## Fig 2: CKA Overlap vs Recoverability Scatter Plot
57	
58	**类型**: 散点图
59	
60	**内容**:
61	- **X 轴**: F(g) — per-structure CKA functional overlap（pruned structure 与其最相似 retained structure 的 CKA）
62	- **Y 轴**: Recoverability — retained structure 在 pruned model vs GRPO-recovered model 之间的 activation shift（1 - cosine similarity）
63	- 每个点 = 一个被剪掉的 structure（attention GQA group 或 MLP channel group）
64	- 按 structure type 着色：蓝色 = attention，橙色 = MLP
65	- 或按 layer index 着色（viridis colormap）+ colorbar
66	- 回归线
…[truncated 6109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T05:01:24.112407+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T05:01:24.112564+00:00_

paper/introduction.tex
paper/related_work.tex
paper/experiments.tex
paper/backup/experiments.tex
paper/backup/introduction.tex
paper/backup/method.tex
paper/backup/related_work.tex
paper/main.tex
paper/abstract.tex
paper/conclusion.tex
paper/limitations.tex
paper/appendix.tex
paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T05:01:24.112690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T05:01:24.112846+00:00_

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
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T05:01:24.113048+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
  "old_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
  "new_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
    "old_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
    "new_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T05:01:24.113212+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T05:01:24.113403+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
  "old_string": "@article{doingmore2026,",
  "new_string": "@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
    "old_string": "@article{doingmore2026,",
    "new_string": "@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T05:01:24.113573+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T05:01:24.113767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T05:01:24.113938+00:00_

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
…[truncated 4099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T05:01:24.114085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[pt]?\\{([^}]+)\\}' paper/related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | while read key; do if grep -q \"^@.*{${key},\" paper/references.bib; then echo \"✓ $key\"; else echo \"✗ MISSING: $key\"; fi; done",
  "description": "Verify all citation keys from related_work.tex exist in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[pt]?\\{([^}]+)\\}' paper/related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | while read key; do if grep -q \"^@.*{${key},\" paper/references.bib; then echo \"✓ $key\"; else echo \"✗ MISSING: $key\"; fi; done",
    "description": "Verify all citation keys from related_work.tex exist in references.bib"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T05:01:24.114214+00:00_

✓ bonsai2025
✓ doingmore2026
✓ frankle2019lth
✓ graspprune2026
✓ kornblith2019cka
✓ lachance2024cka
✓ llmpruner2023
✓ llms2lrms2026
✓ mpruner2024
✓ opsd2026
✓ p2law2025
✓ paser2025
✓ pat2025
✓ rac2025
✓ resp2025
✓ rlsqueezes2026
✓ selfhealing2025
✓ shortgpt2024
✓ slicegpt2024
✓ ssgr2025
✓ wanda2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related-work_20260515T045854",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T05:01:24.114395+00:00_

全部 21 个 citation key 均在 `references.bib` 中存在。

完成内容：
- `paper/related_work.tex` — 3 个小节（Structured Pruning / Pruning-Aware Recovery / RLVR Training Dynamics + CKA），引用 21 篇文献，约 600 词
- `paper/references.bib` — 新增 `ssgr2025` 条目
- 原有文件已覆盖 `literature_notes.md` 中 5 篇核心 + 5 篇补充文献（ThinkPrune 和 Think-Prune-Train-Improve 是 reasoning trace 压缩，与 model pruning 正交，未纳入）
- Gap 明确突出：现有工作未用 CKA functional overlap 指导剪枝决策来优化 RLVR recovery

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related-work_20260515T045854"
}
```

</details>

---
