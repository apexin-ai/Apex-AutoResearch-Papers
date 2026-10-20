# paper writing experiments d041

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_experiments_d041_20260516T043441.jsonl`
- **Structured JSON:** [`222b6468b9d6439d9087.json`](../../sessions/22/222b6468b9d6439d9087.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T04:36:54.453456+00:00_

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
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:36:54.454093+00:00_

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
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:36:54.454298+00:00_

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
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:36:54.454488+00:00_

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
12	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M, frozen during training), an MLP projector that maps fused vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).
13	
14	\paragraph{Model checkpoint.}
15	We use the base OpenVLA-7B checkpoint, pretrained on the Open X-Embodiment dataset.
16	No task-specific fine-tuning is applied; the ``trained'' condition refers to the standard OpenVLA weights, while the ``untrained'' condition reinitializes the LLM parameters (\S\ref{sec:setup}).
17	
18	\paragraph{Evaluation benchmark.}
19	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
20	
21	\paragraph{Untrained control.}
22	To isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \texttt{from\_config()}, yielding 6.74B random weights while preserving the frozen DinoSigLIP encoder and the MLP projector architecture.
23	Any difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.
24	
25	%------------------------------------------------
…[truncated 6531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:36:54.454659+00:00_

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
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:36:54.454873+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{DinoSigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We 
…[truncated 13994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:36:54.455129+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from six sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the fused vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} and \\texttt{patch\\_mean};\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}; and\n(f)~\\textbf{Branch-split}---the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) extracted separately before fusion, plus the fused 2{,}176-D representation before projection.\nSources (d)--(f) serve as external or ablation baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder and the projector architecture, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{RSA.}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) using Euclidean distance for each representation source and for the 7-dimensional action space, with within-task pairing across 50 demonstrations per task.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples (\\S\\ref{sec:rsa}).\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions (\\S\\ref{sec:probes}).\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest action-relevant geometric structure.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe standalone DINOv2 \\texttt{cls\\_token} achieves the highest alignment of any representation source ($\\rho = 0.692$), followed by the fused DinoSigLIP 2{,}176-D representation before projection ($\\rho = 0.634$) and the DINOv2 \\texttt{patch\\_mean} ($\\rho = 0.631$).\nCLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment among pretrained encoders ($\\rho = 0.557$; Figure~\\ref{fig:rsa_bar}).\n\n\\paragraph{Self-supervised pretraining dominates.}\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.692$---exceeding not only CLIP ($\\rho = 0.557$) but also the VLA's own internal representations at their peaks (trained image\\_mean: $0.628$; trained readout: $0.643$).\nThis ordering---self-supervised $>$ VL-pretrained---is consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\nFunctional probes corroborate the ranking: DINOv2 \\texttt{cls\\_token} achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP yields the lowest probe $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\n\n\\paragraph{Branch-split analysis.}\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone, indicating that concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\nThe projector thus maps features into LLM-compatible dimensionality at the cost of modest geometric degradation.\n\n\\paragraph{Metric sensitivity.}\nThe choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties~\\cite{kornblith2019} and underscores the importance of multi-metric evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 \\texttt{cls\\_token} achieves the highest geometric alignment ($0.692$). Fusion of both branches ($0.634$) exceeds either branch alone; the projector introduces modest compression loss ($0.634 \\to 0.615$). VLA peaks refer to the best layer for each token type. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & Notes \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.692 & Standalone, highest \\\\\nFused DinoSigLIP & 2{,}176-D & 0.634 & Before projection \\\\\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & Standalone \\\\\nVLA Trained & image\\_mean (L12) & 0.628 & Peak layer \\\\\nVLA Untrained & last\\_preaction (L1) & 0.626 & Peak layer \\\\\nSigLIP branch & 1{,}088-D & 0.621 & Branch-split \\\\\nDINOv2 branch & 1{,}088-D & 0.619 & Branch-split \\\\\nDinoSigLIP+Projector & --- & 0.615 & After MLP \\\\\nVLA Untrained & image\\_mean (L0) & 0.612 & Peak layer \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & VL-pretrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment, followed by fused DinoSigLIP ($0.634$) and the VLA trained image\\_mean peak ($0.628$). CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic LLM Transformation}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder across its 32 layers.\n\n\\paragraph{Inverted-U pattern.}\nFigure~\\ref{fig:layer_curves} reveals a non-monotonic trajectory for trained image\\_mean RSA: $\\rho$ begins at $0.612$ (L0, equal to the projector input), rises to a peak of $0.628$ at L12---\\emph{above} the DinoSigLIP+Projector baseline ($0.615$)---then declines monotonically to $0.422$ at L32.\nThe first 12 layers thus \\emph{enhance} geometric alignment with the action space beyond the vision encoder input, while the remaining 20 layers progressively degrade it below the initial level.\nThis non-monotonic profile contrasts sharply with the untrained control, which peaks at L0 ($\\rho = 0.612$) and decays monotonically to $0.545$ at L32.\n\n\\paragraph{Peak above projector.}\nThe trained image\\_mean peak at L12 ($\\rho = 0.628$) exceeds the DinoSigLIP+Projector ($0.615$) by $\\Delta = 0.013$.\nThe LLM's middle layers contain representations more geometrically aligned with actions than the raw vision encoder output---refining, not merely preserving, the inherited structure.\n\n\\paragraph{RSA--CKA dissociation.}\nLinear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens follow the inverted-U trajectory, the readout token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves peak RSA $\\rho = 0.643$ at L12 and probe $R^2 = 0.671$ (L19), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Table~\\ref{tab:probes}, Figure~\\ref{fig:probe_bars}).\n\n\\paragraph{Late-layer degradation.}\nThe decline from L12 to L32 ($\\rho$: $0.628 \\to 0.422$, $\\Delta = -0.206$) represents distributed degradation as the LLM repurposes image token representations for language modeling objectives.\nThis degradation exceeds the untrained decay ($0.612 \\to 0.545$, $\\Delta = -0.067$), suggesting that training actively redirects later layers away from action geometry preservation.\n\nTogether, these results characterize LLM processing as a three-phase transformation: early-layer geometric refinement, mid-layer peak, and late-layer degradation with concurrent concentration at the readout position~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The trained readout concentrates action information ($0.671$) beyond the projector ($0.630$), while distributed image\\_mean loses information ($0.599$). $^\\dagger$Untrained readout uses internally consistent probe hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\midrule\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers. Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $= 0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2 cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The trained readout ($R^2{=}0.671$) exceeds the projector baseline ($0.630$) and all external encoders, while trained image\\_mean ($0.599$) falls below the projector. DINOv2 cls ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Redistributes, Does Not Create}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant structure or redistributes pre-existing geometry inherited from the vision encoder.\nFigure~\\ref{fig:factorial} shows the $2 \\times 2$ factorial analysis; Table~\\ref{tab:training_effects} reports bootstrap comparisons.\n\n\\paragraph{Peak shift without peak gain.}\nTraining moves the image\\_mean RSA peak from L0 to L12.\nThe trained model peaks at L12 ($\\rho = 0.628$); the untrained model peaks at L0 ($\\rho = 0.612$).\nComparing best-versus-best: $\\Delta = +0.017$, 95\\% CI includes zero, not statistically significant.\nTraining does not create geometric structure that exceeds what the vision encoder already provides---it relocates the peak deeper into the network.\n\n\\paragraph{Same-layer effect.}\nAt the same layer (L12), training produces a large effect: $\\Delta = +0.079$, $p < 0.0001$.\nThe trained model at L12 ($0.628$) far exceeds the untrained model at L12 ($0.549$).\nTraining thus has a dramatic effect on \\emph{where} action geometry peaks, but a negligible effect on \\emph{how high} it peaks.\n\n\\paragraph{Interpretation.}\nThese two results together support a routing interpretation: training teaches the LLM \\emph{where to concentrate} action-relevant structure (moving the peak from L0 to L12), not \\emph{what structure to create} (the peak value does not increase beyond the untrained best).\nThe vision encoder provides the ceiling; training determines the depth profile.\n\n\\paragraph{Instruction invariance.}\nLanguage instructions do not modulate geometric structure.\nAcross all conditions, instruction presence produces a maximum $|\\Delta| = 0.006$ in RSA, well within noise.\nThis confirms that the action geometry is visually grounded and instruction-independent~\\cite{grant2026}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training effects on action-relevant structure (bootstrap, 10{,}000 resamples). Best-vs-best comparison shows training does not create new geometry ($\\Delta{=}+0.017$, n.s.), while the same-layer comparison reveals training's large routing effect ($\\Delta{=}+0.079$, $p{<}0.0001$).}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$) without increasing the peak value beyond the untrained maximum (best-vs-best $\\Delta{=}+0.017$, n.s.). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$, confirming visually grounded action geometry.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from six sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the fused vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} and \\texttt{patch\\_mean};\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}; and\n(f)~\\textbf{Branch-split}---the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) extracted separately before fusion, plus the fused 2{,}176-D representation before projection.\nSources (d)--(f) serve as external or ablation baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder and the projector architecture, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{RSA.}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) using Euclidean distance for each representation source and for the 7-dimensional action space, with within-task pairing across 50 demonstrations per task.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples (\\S\\ref{sec:rsa}).\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions (\\S\\ref{sec:probes}).\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest action-relevant geometric structure.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe standalone DINOv2 \\texttt{cls\\_token} achieves the highest alignment of any representation source ($\\rho = 0.692$), followed by the fused DinoSigLIP 2{,}176-D representation before projection ($\\rho = 0.634$) and the DINOv2 \\texttt{patch\\_mean} ($\\rho = 0.631$).\nCLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment among pretrained encoders ($\\rho = 0.557$; Figure~\\ref{fig:rsa_bar}).\n\n\\paragraph{Self-supervised pretraining dominates.}\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.692$---exceeding not only CLIP ($\\rho = 0.557$) but also the VLA's own internal representations at their peaks (trained image\\_mean: $0.628$; trained readout: $0.643$).\nThis ordering---self-supervised $>$ VL-pretrained---is consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\nFunctional probes corroborate the ranking: DINOv2 \\texttt{cls\\_token} achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP yields the lowest probe $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\n\n\\paragraph{Branch-split analysis.}\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone, indicating that concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\nThe projector thus maps features into LLM-compatible dimensionality at the cost of modest geometric degradation.\n\n\\paragraph{Metric sensitivity.}\nThe choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties~\\cite{kornblith2019} and underscores the importance of multi-metric evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 \\texttt{cls\\_token} achieves the highest geometric alignment ($0.692$). Fusion of both branches ($0.634$) exceeds either branch alone; the projector introduces modest compression loss ($0.634 \\to 0.615$). VLA peaks refer to the best layer for each token type. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & Notes \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.692 & Standalone, highest \\\\\nFused DinoSigLIP & 2{,}176-D & 0.634 & Before projection \\\\\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & Standalone \\\\\nVLA Trained & image\\_mean (L12) & 0.628 & Peak layer \\\\\nVLA Untrained & last\\_preaction (L1) & 0.626 & Peak layer \\\\\nSigLIP branch & 1{,}088-D & 0.621 & Branch-split \\\\\nDINOv2 branch & 1{,}088-D & 0.619 & Branch-split \\\\\nDinoSigLIP+Projector & --- & 0.615 & After MLP \\\\\nVLA Untrained & image\\_mean (L0) & 0.612 & Peak layer \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & VL-pretrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment, followed by fused DinoSigLIP ($0.634$) and the VLA trained image\\_mean peak ($0.628$). CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic LLM Transformation}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder across its 32 layers.\n\n\\paragraph{Inverted-U pattern.}\nFigure~\\ref{fig:layer_curves} reveals a non-monotonic trajectory for trained image\\_mean RSA: $\\rho$ begins at $0.612$ (L0, equal to the projector input), rises to a peak of $0.628$ at L12---\\emph{above} the DinoSigLIP+Projector baseline ($0.615$)---then declines monotonically to $0.422$ at L32.\nThe first 12 layers thus \\emph{enhance} geometric alignment with the action space beyond the vision encoder input, while the remaining 20 layers progressively degrade it below the initial level.\nThis non-monotonic profile contrasts sharply with the untrained control, which peaks at L0 ($\\rho = 0.612$) and decays monotonically to $0.545$ at L32.\n\n\\paragraph{Peak above projector.}\nThe trained image\\_mean peak at L12 ($\\rho = 0.628$) exceeds the DinoSigLIP+Projector ($0.615$) by $\\Delta = 0.013$.\nThe LLM's middle layers contain representations more geometrically aligned with actions than the raw vision encoder output---refining, not merely preserving, the inherited structure.\n\n\\paragraph{RSA--CKA dissociation.}\nLinear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens follow the inverted-U trajectory, the readout token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves peak RSA $\\rho = 0.643$ at L12 and probe $R^2 = 0.671$ (L19), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Table~\\ref{tab:probes}, Figure~\\ref{fig:probe_bars}).\n\n\\paragraph{Late-layer degradation.}\nThe decline from L12 to L32 ($\\rho$: $0.628 \\to 0.422$, $\\Delta = -0.206$) represents distributed degradation as the LLM repurposes image token representations for language modeling objectives.\nThis degradation exceeds the untrained decay ($0.612 \\to 0.545$, $\\Delta = -0.067$), suggesting that training actively redirects later layers away from action geometry preservation.\n\nTogether, these results characterize LLM processing as a three-phase transformation: early-layer geometric refinement, mid-layer peak, and late-layer degradation with concurrent concentration at the readout position~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The trained readout concentrates action information ($0.671$) beyond the projector ($0.630$), while distributed image\\_mean loses information ($0.599$). $^\\dagger$Untrained readout uses internally consistent probe hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\midrule\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers. Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $= 0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2 cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The trained readout ($R^2{=}0.671$) exceeds the projector baseline ($0.630$) and all external encoders, while trained image\\_mean ($0.599$) falls below the projector. DINOv2 cls ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Redistributes, Does Not Create}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant structure or redistributes pre-existing geometry inherited from the vision encoder.\nFigure~\\ref{fig:factorial} shows the $2 \\times 2$ factorial analysis; Table~\\ref{tab:training_effects} reports bootstrap comparisons.\n\n\\paragraph{Peak shift without peak gain.}\nTraining moves the image\\_mean RSA peak from L0 to L12.\nThe trained model peaks at L12 ($\\rho = 0.628$); the untrained model peaks at L0 ($\\rho = 0.612$).\nComparing best-versus-best: $\\Delta = +0.017$, 95\\% CI includes zero, not statistically significant.\nTraining does not create geometric structure that exceeds what the vision encoder already provides---it relocates the peak deeper into the network.\n\n\\paragraph{Same-layer effect.}\nAt the same layer (L12), training produces a large effect: $\\Delta = +0.079$, $p < 0.0001$.\nThe trained model at L12 ($0.628$) far exceeds the untrained model at L12 ($0.549$).\nTraining thus has a dramatic effect on \\emph{where} action geometry peaks, but a negligible effect on \\emph{how high} it peaks.\n\n\\paragraph{Interpretation.}\nThese two results together support a routing interpretation: training teaches the LLM \\emph{where to concentrate} action-relevant structure (moving the peak from L0 to L12), not \\emph{what structure to create} (the peak value does not increase beyond the untrained best).\nThe vision encoder provides the ceiling; training determines the depth profile.\n\n\\paragraph{Instruction invariance.}\nLanguage instructions do not modulate geometric structure.\nAcross all conditions, instruction presence produces a maximum $|\\Delta| = 0.006$ in RSA, well within noise.\nThis confirms that the action geometry is visually grounded and instruction-independent~\\cite{grant2026}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training effects on action-relevant structure (bootstrap, 10{,}000 resamples). Best-vs-best comparison shows training does not create new geometry ($\\Delta{=}+0.017$, n.s.), while the same-layer comparison reveals training's large routing effect ($\\Delta{=}+0.079$, $p{<}0.0001$).}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$) without increasing the peak value beyond the untrained maximum (best-vs-best $\\Delta{=}+0.017$, n.s.). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$, confirming visually grounded action geometry.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:36:54.455597+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_d041_20260516T043441",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T04:36:54.455794+00:00_

experiments.tex 已全量重写。主要变更：

- **§4.1**: 新增 source (f) branch-split，其余保持简洁
- **§4.2**: DINO cls_token 0.692 领先；新增 branch-split 段落（DINOv2=0.619 ≈ SigLIP=0.621，fusion=0.634 > 两者，projector 压缩 0.634→0.615）；CKA 反转讨论保留
- **§4.3**: 标题改为 "Non-Monotonic LLM Transformation"；核心叙事：inverted-U（L0=0.612→L12=0.628 peak ABOVE projector 0.615→L32=0.422）；RSA-CKA dissociation；readout concentration 保留
- **§4.4**: 标题改为 "Training Redistributes, Does Not Create"；best-vs-best Δ=+0.017 n.s.；same-layer L12 Δ=+0.079 p<0.0001；instruction invariance |Δ|<0.006

所有 \label 与旧版一致，数字均来自权威数据表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_d041_20260516T043441"
}
```

</details>

---
