# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_20260516T025433.jsonl`
- **Structured JSON:** [`55a9784ad60041289e9f.json`](../../sessions/55/55a9784ad60041289e9f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T02:56:34.629774+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:56:34.630601+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:56:34.630865+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:56:34.631297+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:56:34.631519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:56:34.631773+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.
5	This section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.
6	
7	%------------------------------------------------------------------
8	\subsection{Model and Data}
9	\label{sec:model_data}
10	
11	\paragraph{Architecture.}
12	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip} (0.80B parameters, frozen during fine-tuning), an MLP projector that maps vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).
13	
14	\paragraph{Fine-tuning data.}
15	We use a checkpoint fine-tuned on the LIBERO-10 split~\cite{liu2023_libero}, which provides 10 tabletop manipulation tasks with 50 human demonstrations per task.
16	
17	\paragraph{Evaluation benchmark.}
18	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, which shares initial states with LIBERO-10 but pairs them with different language-specified goals.
19	This separation ensures that the evaluation tasks test generalization to novel goals rather than memorization of training trajectories.
20	
21	\paragraph{Untrained control.}
22	To isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \texttt{from\_config()}, yielding 6.74B random weights while preserving the frozen SigLIP encoder (0.80B pretrained weights) and the MLP projector architecture.
23	Any difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.
24	
25	%-----------------------
…[truncated 5922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:56:34.632024+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:56:34.632361+00:00_

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
…[truncated 13600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:56:34.632592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:56:34.632864+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of how action-relevant structure flows through a VLA.
6	The vision encoder is the \emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\rho = 0.615$; CLIP $\rho = 0.557$), far exceeding what the LLM produces at any layer ($\rho \leq 0.501$).
7	The LLM is a \emph{router}: it degrades distributed geometric structure ($\rho$: $0.615 \to 0.501$; $R^2$: $0.706 \to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).
8	Training teaches the \emph{routing policy}: the geometric structure itself is invariant to training ($\Delta\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\Delta R^2 = 0.045$, $p < 0.0001$).
9	Notably, the projector alone captures 96.6\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.
10	
11	\paragraph{VL pretraining as a general source of action-relevant geometry.}
12	The inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.
13	Both VL-pretrained encoders---SigLIP ($\rho = 0.615$) and CLIP ($\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\rho = 0.388$).
14	The 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.
15	The additional increment from CLIP to SigLIP+Projector ($\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\rho = 0.557 \gg 0.388$) originates in VL pretraining itself.
16	
17	\paragraph{Geo
…[truncated 5220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:56:34.633260+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve strong manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe prevailing architectural assumption is that LLM fine-tuning injects action-relevant representational knowledge into the system---that the language backbone learns to transform visual input into representations suited for action prediction.\nYet this assumption has not been tested at the representational level.\nWhere do the representations that drive action prediction actually originate?\nThe answer has direct consequences for VLA design: if the LLM backbone is the primary source of action structure, scaling and training the LLM is the critical lever; if instead the pretrained vision encoder already supplies this structure, investment should prioritize visual representation quality.\n\nRecent work has begun to probe this question from complementary angles.\nAt the behavioral level, \\cite{grant2026} demonstrated that VLA policies are disproportionately driven by visual input, with language instructions having limited influence on action selection.\nRepresentational analyses of VLA internals further suggest that language instructions are largely ignored by the action generation pathway~\\cite{haon2025}.\nHowever, these studies operate at the behavioral or single-component level---none has performed a systematic \\emph{representational decomposition} that quantifies how each architectural component (vision encoder, projector, LLM layers) independently contributes to action-relevant structure.\nWithout such a decomposition, it remains unclear whether VLA fine-tuning creates new action knowledge or merely reconfigures structure inherited from pretrained components.\n\nWe address this gap by decomposing OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA that chains a frozen SigLIP vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone fine-tuned on LIBERO-10~\\cite{liu2023_libero}.\nWe extract representations from the projector output, each of the 32 LLM layers at both distributed image-token and readout-token positions, and two external baselines---CLIP ViT-L/14~\\cite{radford2021_clip} and DINOv2 ViT-L/14~\\cite{oquab2024_dinov2}---that isolate the effect of pretraining objective (vision-language vs.\\ vision-only).\nTo disentangle training from architecture, we cross two factors in a $2 \\times 2$ factorial design: LLM training status (trained vs.\\ untrained, with the untrained control reinitializing all 6.74B LLM parameters) and instruction presence (with vs.\\ without language instruction).\nWe quantify action-relevant structure using Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, which measures geometric alignment between representations and the action space, and functional MLP probes~\\cite{alain2017}, which measure decodability of action vectors from frozen representations.\n\nThree findings emerge from this decomposition.\n\\emph{First}, the frozen vision-language encoder provides the dominant source of action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$); CLIP, an independent VL-pretrained encoder with no VLA training signal, achieves $\\rho = 0.557$---both far exceeding vision-only DINOv2 ($\\rho = 0.388$).\nThis 0.169-point gap between CLIP and DINOv2, two ViT-L/14 architectures differing primarily in pretraining objective, isolates VL pretraining as the operative factor.\nThe LLM never exceeds $\\rho = 0.501$ at any layer.\n\\emph{Second}, the LLM degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$) but concentrates a functionally superior representation at the readout token (probe $R^2 = 0.731$ vs.\\ $0.706$ for the projector, $p = 0.001$), characterizing the LLM as an information \\emph{router} rather than a knowledge source.\n\\emph{Third}, the geometric structure is invariant to LLM training ($\\Delta\\rho = 0.021$, $p = 0.20$, n.s.), while functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nTraining teaches routing, not representation creation.\n\nThese findings make three contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item We provide the first representational decomposition of a VLA, separately quantifying the action-relevant structure contributed by the vision encoder, projector, and LLM layers using both geometric (RSA) and functional (probe $R^2$) metrics.\n  \\item We demonstrate that VL-pretrained vision encoders---not LLM fine-tuning---are the primary source of action-relevant geometric structure, with two independent VL encoders (SigLIP, CLIP) both substantially exceeding vision-only DINOv2.\n  \\item We characterize the LLM as an information router that concentrates pre-existing vision-encoder geometry at the readout token for action decoding, with training teaching the routing policy rather than creating new representations.\n\\end{itemize}\nThese results suggest that vision encoder pretraining quality---specifically, vision-language alignment---is the primary lever for action representations in current VLA architectures, and that the LLM backbone's role is information routing rather than knowledge injection (\\S\\ref{sec:discussion}).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve strong manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe prevailing architectural assumption is that LLM fine-tuning injects action-relevant representational knowledge into the system---that the language backbone learns to transform visual input into representations suited for action prediction.\nYet this assumption has not been tested at the representational level.\nWhere do the representations that drive action prediction actually originate?\nThe answer has direct consequences for VLA design: if the LLM backbone is the primary source of action structure, scaling and training the LLM is the critical lever; if instead the pretrained vision encoder already supplies this structure, investment should prioritize visual representation quality.\n\nRecent work has begun to probe this question from complementary angles.\nAt the behavioral level, \\cite{grant2026} demonstrated that VLA policies are disproportionately driven by visual input, with language instructions having limited influence on action selection.\nRepresentational analyses of VLA internals further suggest that language instructions are largely ignored by the action generation pathway~\\cite{haon2025}.\nHowever, these studies operate at the behavioral or single-component level---none has performed a systematic \\emph{representational decomposition} that quantifies how each architectural component (vision encoder, projector, LLM layers) independently contributes to action-relevant structure.\nWithout such a decomposition, it remains unclear whether VLA fine-tuning creates new action knowledge or merely reconfigures structure inherited from pretrained components.\n\nWe address this gap by decomposing OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA that chains a frozen SigLIP vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone fine-tuned on LIBERO-10~\\cite{liu2023_libero}.\nWe extract representations from the projector output, each of the 32 LLM layers at both distributed image-token and readout-token positions, and two external baselines---CLIP ViT-L/14~\\cite{radford2021_clip} and DINOv2 ViT-L/14~\\cite{oquab2024_dinov2}---that isolate the effect of pretraining objective (vision-language vs.\\ vision-only).\nTo disentangle training from architecture, we cross two factors in a $2 \\times 2$ factorial design: LLM training status (trained vs.\\ untrained, with the untrained control reinitializing all 6.74B LLM parameters) and instruction presence (with vs.\\ without language instruction).\nWe quantify action-relevant structure using Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, which measures geometric alignment between representations and the action space, and functional MLP probes~\\cite{alain2017}, which measure decodability of action vectors from frozen representations.\n\nThree findings emerge from this decomposition.\n\\emph{First}, the frozen vision-language encoder provides the dominant source of action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$); CLIP, an independent VL-pretrained encoder with no VLA training signal, achieves $\\rho = 0.557$---both far exceeding vision-only DINOv2 ($\\rho = 0.388$).\nThis 0.169-point gap between CLIP and DINOv2, two ViT-L/14 architectures differing primarily in pretraining objective, isolates VL pretraining as the operative factor.\nThe LLM never exceeds $\\rho = 0.501$ at any layer.\n\\emph{Second}, the LLM degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$) but concentrates a functionally superior representation at the readout token (probe $R^2 = 0.731$ vs.\\ $0.706$ for the projector, $p = 0.001$), characterizing the LLM as an information \\emph{router} rather than a knowledge source.\n\\emph{Third}, the geometric structure is invariant to LLM training ($\\Delta\\rho = 0.021$, $p = 0.20$, n.s.), while functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nTraining teaches routing, not representation creation.\n\nThese findings make three contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item We provide the first representational decomposition of a VLA, separately quantifying the action-relevant structure contributed by the vision encoder, projector, and LLM layers using both geometric (RSA) and functional (probe $R^2$) metrics.\n  \\item We demonstrate that VL-pretrained vision encoders---not LLM fine-tuning---are the primary source of action-relevant geometric structure, with two independent VL encoders (SigLIP, CLIP) both substantially exceeding vision-only DINOv2.\n  \\item We characterize the LLM as an information router that concentrates pre-existing vision-encoder geometry at the readout token for action decoding, with training teaching the routing policy rather than creating new representations.\n\\end{itemize}\nThese results suggest that vision encoder pretraining quality---specifically, vision-language alignment---is the primary lever for action representations in current VLA architectures, and that the LLM backbone's role is information routing rather than knowledge injection (\\S\\ref{sec:discussion}).\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:56:34.633610+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:56:34.633832+00:00_

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
  "session": "worker_paper_writing_20260516T025433",
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

_source line 14 · 2026-05-16T02:56:34.634047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:56:34.634224+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "introduction.tex",
  "type": "paper",
  "description": "Introduction section for the VLA-SSD paper: 5-paragraph structure covering problem, gap, approach, findings, and contributions.",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "tags": "['paper', 'introduction', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "introduction.tex",
    "type": "paper",
    "description": "Introduction section for the VLA-SSD paper: 5-paragraph structure covering problem, gap, approach, findings, and contributions.",
    "project": "vla-ssd",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
    "tags": "['paper', 'introduction', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:56:34.634435+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_fccb56\", \"name\": \"introduction.tex\", \"type\": \"paper\", \"description\": \"Introduction section for the VLA-SSD paper: 5-paragraph structure covering problem, gap, approach, findings, and contributions.\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/introduction_fccb56.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:56:22.820879+00:00\", \"tags\": [\"paper\", \"introduction\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025433",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T02:56:34.634679+00:00_

Introduction 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex`。

**结构**：5 段，按 writing_plan.yaml 的 para_1–para_5 组织：
1. **Problem** — VLA 的隐含假设：LLM fine-tuning 注入 action knowledge
2. **Gap** — 现有工作停留在 behavioral 层面，无 representational decomposition（引用 grant2026, haon2025）
3. **Approach** — 2×2 factorial design + RSA + probes，分解 OpenVLA 各组件
4. **Findings** — 三个核心发现，所有数字均来自同一 probe set（50ep），RSA 数字全部安全
5. **Contributions** — 3-item itemize + 一句 implications 指向 Discussion

**合规检查**：
- R² 数字仅引用 Proj/LLM 系列（0.706, 0.731, 0.686），未混入 CLIP/DINO 100ep 数字
- 未使用 "consistently"（单 benchmark）
- "significantly" 未出现（统计检验用 p 值直接报告）
- 所有引用均限于允许的 bibtex keys
- 术语与 experiments.tex / method.tex / discussion.tex 一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260516T025433"
}
```

</details>

---
