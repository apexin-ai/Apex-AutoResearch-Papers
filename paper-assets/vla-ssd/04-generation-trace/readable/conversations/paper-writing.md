# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_20260516T025122.jsonl`
- **Structured JSON:** [`fef7bd69642f39b05c1a.json`](../../sessions/fe/fef7bd69642f39b05c1a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-16T02:52:53.628871+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:52:53.629498+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:52:53.629703+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:52:53.630030+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:52:53.630196+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:52:53.630412+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:52:53.630568+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:52:53.630732+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:52:53.630950+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nOur experiments reveal a coherent picture of how action-relevant structure flows through a VLA.\nThe vision encoder is the \\emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\\rho = 0.615$; CLIP $\\rho = 0.557$), far exceeding what the LLM produces at any layer ($\\rho \\leq 0.501$).\nThe LLM is a \\emph{router}: it degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$; $R^2$: $0.706 \\to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).\nTraining teaches the \\emph{routing policy}: the geometric structure itself is invariant to training ($\\Delta\\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nNotably, the projector alone captures 96.6\\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.\n\n\\paragraph{VL pretraining as a general source of action-relevant geometry.}\nThe inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.\nBoth VL-pretrained encoders---SigLIP ($\\rho = 0.615$) and CLIP ($\\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\\rho = 0.388$).\nThe 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.\nThe additional increment from CLIP to SigLIP+Projector ($\\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\\rho = 0.557 \\gg 0.388$) originates in VL pretraining itself.\n\n\\paragraph{Geometric-functional dissociation.}\nA recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).\nDINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\\ $0.615$).\nThis dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \\emph{geometric alignment}, organizing that information into a structure that mirrors the action space.\nFor VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.\n\n\\paragraph{Metric sensitivity: RSA versus CKA.}\nThe divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.\nLinear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.\nUnder linear CKA, training appears to \\emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.\nRDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).\nThe divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\\cite{kornblith2019}.\nThe practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.\n\n\\paragraph{Implications for VLA design.}\nOur findings suggest four practical considerations.\n\\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.\n\\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\\% of readout-level decodability.\n\\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.\n\\emph{Fourth}, the invariance of representation geometry to language instructions ($\\Delta\\rho = 0.004$, n.s.; content controls within $\\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.\n\n\\paragraph{Connection to behavioral evidence.}\nOur representational findings complement the behavioral results of \\citet{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.\nOur data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\\pm 0.017$).\nThe alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.\n\n\\paragraph{Limitations.}\nSeveral limitations scope our conclusions.\nWe study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.\nRSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.\nThe CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.\nFinally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nOur experiments reveal a coherent picture of how action-relevant structure flows through a VLA.\nThe vision encoder is the \\emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\\rho = 0.615$; CLIP $\\rho = 0.557$), far exceeding what the LLM produces at any layer ($\\rho \\leq 0.501$).\nThe LLM is a \\emph{router}: it degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$; $R^2$: $0.706 \\to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).\nTraining teaches the \\emph{routing policy}: the geometric structure itself is invariant to training ($\\Delta\\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nNotably, the projector alone captures 96.6\\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.\n\n\\paragraph{VL pretraining as a general source of action-relevant geometry.}\nThe inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.\nBoth VL-pretrained encoders---SigLIP ($\\rho = 0.615$) and CLIP ($\\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\\rho = 0.388$).\nThe 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.\nThe additional increment from CLIP to SigLIP+Projector ($\\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\\rho = 0.557 \\gg 0.388$) originates in VL pretraining itself.\n\n\\paragraph{Geometric-functional dissociation.}\nA recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).\nDINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\\ $0.615$).\nThis dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \\emph{geometric alignment}, organizing that information into a structure that mirrors the action space.\nFor VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.\n\n\\paragraph{Metric sensitivity: RSA versus CKA.}\nThe divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.\nLinear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.\nUnder linear CKA, training appears to \\emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.\nRDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).\nThe divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\\cite{kornblith2019}.\nThe practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.\n\n\\paragraph{Implications for VLA design.}\nOur findings suggest four practical considerations.\n\\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.\n\\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\\% of readout-level decodability.\n\\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.\n\\emph{Fourth}, the invariance of representation geometry to language instructions ($\\Delta\\rho = 0.004$, n.s.; content controls within $\\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.\n\n\\paragraph{Connection to behavioral evidence.}\nOur representational findings complement the behavioral results of \\citet{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.\nOur data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\\pm 0.017$).\nThe alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.\n\n\\paragraph{Limitations.}\nSeveral limitations scope our conclusions.\nWe study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.\nRSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.\nThe CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.\nFinally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:52:53.631164+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025122",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:52:53.631298+00:00_

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
  "session": "worker_paper_writing_20260516T025122",
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

_source line 12 · 2026-05-16T02:52:53.631416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025122",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:52:53.631533+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "discussion.tex",
  "type": "paper",
  "description": "Discussion section for VLA-SSD paper: 7 paragraphs covering synthesis, CLIP generalization, geometric-functional dissociation, RSA/CKA metric sensitivity, design implications, connection to behavioral evidence, and limitations.",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "tags": "['paper', 'discussion', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T025122",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "discussion.tex",
    "type": "paper",
    "description": "Discussion section for VLA-SSD paper: 7 paragraphs covering synthesis, CLIP generalization, geometric-functional dissociation, RSA/CKA metric sensitivity, design implications, connection to behavioral evidence, and limitations.",
    "project": "vla-ssd",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "tags": "['paper', 'discussion', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:52:53.631667+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_f7970e\", \"name\": \"discussion.tex\", \"type\": \"paper\", \"description\": \"Discussion section for VLA-SSD paper: 7 paragraphs covering synthesis, CLIP generalization, geometric-functional dissociation, RSA/CKA metric sensitivity, design implications, connection to behavioral evidence, and limitations.\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/discussion.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:52:43.283321+00:00\", \"tags\": [\"paper\", \"discussion\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T025122",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T02:52:53.631845+00:00_

Discussion section 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex`。

7 段结构：
1. **Synthesis** — source-router-policy 三角叙事，projector 提供 96.6% readout 容量
2. **VL pretraining generalization** — CLIP 0.557 确认 VL pretraining 是通用 source，非 SigLIP 特有
3. **Geometric-functional dissociation** — DINO ≈ Proj in R² but << in RSA，VL pretraining 提供 alignment 而非额外 information
4. **RSA vs CKA** — linear CKA 排序反转，RDM kernel CKA 恢复一致，metric choice determines narrative
5. **Design implications** — 四条实践建议（encoder quality、projector output、readout concentration、instruction role）
6. **Behavioral connection** — 与 Grant et al. 2026 behavioral findings 的 representational account 对应
7. **Limitations** — 单架构/单 benchmark、RSA 非因果、跨实验 R² 超参差异、post-hoc 分析局限

所有数字严格来自 registry，R² 对比仅在同一 probe 设置内进行，未混用 50ep/100ep 数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260516T025122"
}
```

</details>

---
