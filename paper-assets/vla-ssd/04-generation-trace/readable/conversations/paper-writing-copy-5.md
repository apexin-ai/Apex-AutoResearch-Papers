# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_writing_20260516T024157.jsonl`
- **Structured JSON:** [`b95457439b675f3ab9f0.json`](../../sessions/b9/b95457439b675f3ab9f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-16T02:43:34.034865+00:00_

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
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:43:34.035480+00:00_

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
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:43:34.035669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:43:34.035985+00:00_

1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:43:34.036162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:43:34.036381+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ betwee
…[truncated 13545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:43:34.036560+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:43:34.036685+00:00_

docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:43:34.036823+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:43:34.036958+00:00_

docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:43:34.037079+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:43:34.037191+00:00_

experiments.tex
references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:43:34.037350+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.\nThis section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} (0.80B parameters, frozen during fine-tuning), an MLP projector that maps vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).\n\n\\paragraph{Fine-tuning data.}\nWe use a checkpoint fine-tuned on the LIBERO-10 split~\\cite{liu2023_libero}, which provides 10 tabletop manipulation tasks with 50 human demonstrations per task.\n\n\\paragraph{Evaluation benchmark.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, which shares initial states with LIBERO-10 but pairs them with different language-specified goals.\nThis separation ensures that the evaluation tasks test generalization to novel goals rather than memorization of training trajectories.\n\n\\paragraph{Untrained control.}\nTo isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \\texttt{from\\_config()}, yielding 6.74B random weights while preserving the frozen SigLIP encoder (0.80B pretrained weights) and the MLP projector architecture.\nAny difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from five sources that span the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),leftmargin=*,nosep]\n  \\item \\textbf{SigLIP+Projector}: the output of the MLP projector applied to SigLIP vision features, i.e., the representation immediately before LLM processing.\n  \\item \\textbf{LLM image\\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.\n  \\item \\textbf{LLM last\\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.\n  \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2}: the \\texttt{cls\\_token} from a vision-only self-supervised encoder, serving as a baseline without language grounding.\n  \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip}: the mean of patch token activations (\\texttt{patch\\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.\n\\end{enumerate}\n\n\\paragraph{Experimental conditions.}\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nSources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.\nFor the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.\n\n\\paragraph{RDM construction.}\nFor a set of $N$ observations, we compute the $N \\times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances.\nAn analogous RDM is computed for the 7-dimensional action vectors.\n\n\\paragraph{RSA statistic.}\nWe measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ over the upper-triangular entries of each matrix.\nHigher $\\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.\n\n\\paragraph{Task-level analysis.}\nWe compute RSA separately for each of the 10 LIBERO-Goal tasks, then aggregate across tasks.\nThis per-task procedure avoids conflating within-task structure with between-task variation.\n\n\\paragraph{Statistical inference.}\nWe construct 95\\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.\nPairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA captures geometric alignment but does not assess whether action-relevant information is linearly decodable.\nWe complement RSA with functional probes following~\\cite{alain2017}.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear; $d_\\text{in} \\to 256 \\to 7$) to predict 7-D action vectors from frozen representations.\nAll representation weights are fixed; only the probe parameters are optimized.\n\n\\paragraph{Training protocol.}\nProbes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).\nEach task's data is split into training and validation sets.\n\n\\paragraph{Evaluation metric.}\nWe report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\\% confidence intervals for all pairwise contrasts.\n\n%------------------------------------------------------------------\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nAs a complementary perspective, we employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\n\\paragraph{Two CKA variants.}\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\n\\paragraph{Dimension mismatch caveat.}\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.\nThis section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} (0.80B parameters, frozen during fine-tuning), an MLP projector that maps vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).\n\n\\paragraph{Fine-tuning data.}\nWe use a checkpoint fine-tuned on the LIBERO-10 split~\\cite{liu2023_libero}, which provides 10 tabletop manipulation tasks with 50 human demonstrations per task.\n\n\\paragraph{Evaluation benchmark.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, which shares initial states with LIBERO-10 but pairs them with different language-specified goals.\nThis separation ensures that the evaluation tasks test generalization to novel goals rather than memorization of training trajectories.\n\n\\paragraph{Untrained control.}\nTo isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \\texttt{from\\_config()}, yielding 6.74B random weights while preserving the frozen SigLIP encoder (0.80B pretrained weights) and the MLP projector architecture.\nAny difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from five sources that span the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),leftmargin=*,nosep]\n  \\item \\textbf{SigLIP+Projector}: the output of the MLP projector applied to SigLIP vision features, i.e., the representation immediately before LLM processing.\n  \\item \\textbf{LLM image\\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.\n  \\item \\textbf{LLM last\\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.\n  \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2}: the \\texttt{cls\\_token} from a vision-only self-supervised encoder, serving as a baseline without language grounding.\n  \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip}: the mean of patch token activations (\\texttt{patch\\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.\n\\end{enumerate}\n\n\\paragraph{Experimental conditions.}\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nSources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.\nFor the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.\n\n\\paragraph{RDM construction.}\nFor a set of $N$ observations, we compute the $N \\times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances.\nAn analogous RDM is computed for the 7-dimensional action vectors.\n\n\\paragraph{RSA statistic.}\nWe measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ over the upper-triangular entries of each matrix.\nHigher $\\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.\n\n\\paragraph{Task-level analysis.}\nWe compute RSA separately for each of the 10 LIBERO-Goal tasks, then aggregate across tasks.\nThis per-task procedure avoids conflating within-task structure with between-task variation.\n\n\\paragraph{Statistical inference.}\nWe construct 95\\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.\nPairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA captures geometric alignment but does not assess whether action-relevant information is linearly decodable.\nWe complement RSA with functional probes following~\\cite{alain2017}.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear; $d_\\text{in} \\to 256 \\to 7$) to predict 7-D action vectors from frozen representations.\nAll representation weights are fixed; only the probe parameters are optimized.\n\n\\paragraph{Training protocol.}\nProbes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).\nEach task's data is split into training and validation sets.\n\n\\paragraph{Evaluation metric.}\nWe report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\\% confidence intervals for all pairwise contrasts.\n\n%------------------------------------------------------------------\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nAs a complementary perspective, we employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\n\\paragraph{Two CKA variants.}\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\n\\paragraph{Dimension mismatch caveat.}\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:43:34.037599+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:43:34.037858+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:43:34.038021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:43:34.038145+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method.tex",
  "type": "paper",
  "description": "Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "tags": "['paper', 'method', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method.tex",
    "type": "paper",
    "description": "Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.",
    "project": "vla-ssd",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "tags": "['paper', 'method', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:43:34.038285+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a6c062\", \"name\": \"method.tex\", \"type\": \"paper\", \"description\": \"Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:43:25.266418+00:00\", \"tags\": [\"paper\", \"method\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T024157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T02:43:34.038450+00:00_

Method 章节已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex`。

内容概要：
- **2.1 Model and Data**: OpenVLA-7B 架构（SigLIP → Projector → Llama-2 7B → action head）、LIBERO-10 微调、LIBERO-Goal 评估、untrained control 设计
- **2.2 Representation Extraction**: 五个表征来源 (a)-(e) 的定义，$2\times2$ factorial design（trained/untrained × with/without instruction）
- **2.3 RSA**: RDM 构建、Spearman $\rho$、per-task 分析、bootstrap CI (10,000 resamples)
- **2.4 Functional Action Probes**: MLP probe 架构（$d_\text{in} \to 256 \to 7$）、训练协议（Adam, lr=$10^{-3}$, batch 256, 50 epochs, patience 5）、mean $R^2$ 指标、bootstrap paired comparison
- **2.5 CKA Analysis**: Linear CKA 与 RDM kernel CKA 两种变体，dimension mismatch caveat

所有术语、符号、数字与 experiments.tex 保持一致。仅使用指定的 bibtex keys。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260516T024157"
}
```

</details>

---
