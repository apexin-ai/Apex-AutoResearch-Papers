# paper writing method section

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_method_section_20260513T033854.jsonl`
- **Structured JSON:** [`042ad4218f6bad4b0344.json`](../../sessions/04/042ad4218f6bad4b0344.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-13T03:41:47.201445+00:00_

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
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T03:41:47.202207+00:00_

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
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T03:41:47.202689+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex",
  "content": "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 3 -- Motivating Experiment\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Motivating Experiment}\n\\label{sec:motivating}\n\nBefore committing to the full \\textbf{ACR-VLA} pipeline, we ask a targeted question: \\emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.\n\n\\paragraph{Setup.}\nA synthetic policy outputs actions $a\\in\\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\\sigma_x{=}0.5,\\;\\sigma_y{=}0.1,\\;\\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.\n\nWe train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:\n\\begin{itemize}[nosep]\n  \\item \\textbf{Model A} (scalar): conditioned on the average standard deviation $\\bar{\\sigma}=\\tfrac{1}{3}\\sum_j\\sigma_j$.\n  \\item \\textbf{Model B} (per-DOF): conditioned on the full vector $[\\sigma_x,\\sigma_y,\\sigma_z]$.\n  \\item \\textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.\n\\end{itemize}\nTo match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \\emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \\textbf{ACR-VLA}).\n\n\\paragraph{Results.}\nTable~\\ref{tab:motivating} reports per-axis MSE over 1{,}000 test episodes at a 5:1 anisotropy ratio ($\\sigma_x/\\sigma_y$) with $K{=}10$ estimated uncertainty.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-axis MSE ($\\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{=}10$ estimated uncertainty). Model~B, which receives per-DOF uncertainty, preserves accuracy on the low-uncertainty axes ($y,z$) where Model~A and~C over-correct.}\n\\label{tab:motivating}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Conditioning & MSE$_x$ & MSE$_y$ & MSE$_z$ & Total MSE \\\\\n\\midrule\nA & scalar $\\bar\\sigma$ & 0.1874 & 0.0247 & 0.0243 & 0.0788 \\\\\n\\textbf{B} & \\textbf{per-DOF} $[\\sigma_x,\\sigma_y,\\sigma_z]$ & \\textbf{0.1829} & \\textbf{0.0191} & \\textbf{0.0185} & \\textbf{0.0735} \\\\\nC & none & 0.2151 & 0.0250 & 0.0246 & 0.0882 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel~B reduces total MSE by 6.7\\% relative to~A and by 16.7\\% relative to~C.  The gains concentrate on the non-perturbed axes: $y$- and $z$-axis MSE drop by 22.7\\% and 23.9\\% versus~A, indicating that Model~B learns to leave low-uncertainty dimensions largely untouched while directing correction effort toward the high-uncertainty $x$-axis.  Model~A, receiving only a scalar average, lacks the information to make this distinction and applies a uniform correction that degrades the already-accurate axes.\n\nWith oracle (ground-truth) variances, the ranking $\\text{B}>\\text{A}>\\text{C}$ is preserved with larger margins (non-perturbed axis improvements of 22--38\\% over~A).  Moving from oracle to $K{=}10$ estimation reduces relative gains by roughly 15 percentage points, reflecting finite-sample noise, but does not alter the ordering.  The pattern also holds at weaker anisotropy ratios (2:1 and 1.5:1): across all six conditions tested, Model~B consistently outperforms both baselines.\n\n\\paragraph{Takeaway.}\nEven a simple MLP can exploit per-DOF uncertainty structure for dimension-selective correction---a capability that scalar summaries cannot provide.  This motivates the design of \\textbf{ACR-VLA}, which extracts rich per-DOF features from a flow-matching VLA and feeds them into a learned correction module (Section~\\ref{sec:method}).\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 4 -- Method\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA) is an inference-time, post-hoc module that attaches to any flow-matching VLA without modifying its weights.  It comprises three components (Figure~\\ref{fig:pipeline}):\n\\begin{enumerate}[nosep]\n  \\item \\textbf{Conformalized Gaussian Scoring} (CGS, \\S\\ref{sec:cgs}): draws $K{=}10$ action samples per step, fits a shrinkage-regularized Gaussian, and extracts a 40-dimensional structured uncertainty feature.\n  \\item \\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency} (ACI+COC, \\S\\ref{sec:aci}): maintains an online conformal threshold that adapts to distribution shift using a self-referential coverage signal from overlapping action chunks.\n  \\item \\textbf{Conformal Refinement Module} (CRM, \\S\\ref{sec:crm}): a lightweight MLP that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\n\\end{enumerate}\n\nWe instantiate \\textbf{ACR-VLA} on SmolVLA~\\cite{smolvla2025}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).\n\n\n%%% 4.1 CGS %%%\n\\subsection{Conformalized Gaussian Scoring}\n\\label{sec:cgs}\n\nCGS converts a set of stochastic action samples from the base VLA into a compact uncertainty descriptor that captures \\emph{which} degrees of freedom are uncertain and \\emph{how} they co-vary---information that a scalar nonconformity score discards.\n\n\\paragraph{Sampling and truncation.}\nAt each control step, we draw $K{=}10$ action chunks from the frozen base VLA via independent flow-matching rollouts.  Although SmolVLA predicts 50-step chunks, under receding-horizon execution only the first few steps influence the robot before re-planning.  We therefore retain only the first $H{=}5$ steps, yielding $K$ samples $\\{a_h^{(k)}\\}_{k=1}^{K}$ with $a_h^{(k)}\\in\\mathbb{R}^{d}$ for each horizon step $h=1,\\dots,H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1-\\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity.  With a dimension-to-sample ratio $p/n = d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error due to the Marchenko--Pastur effect; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nWe define a joint multivariate nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis single score captures cross-DOF covariance structure.  In contrast, treating each DOF independently and applying Bonferroni correction across all $d{\\times}H = 30$ marginals yields intervals that are substantially wider than necessary.  Our joint formulation requires Bonferroni correction only across $H{=}5$ horizon steps (target level $\\alpha/H$ per step), preserving tight per-step regions~\\cite{braun2025cgs}.\n\n\\paragraph{CGS feature vector.}\nWe assemble a 40-dimensional feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ that is passed to the refinement module:\n\\begin{equation}\n  \\boldsymbol{\\varphi}_{\\mathrm{CGS}} = \\bigl[\\,\\underbrace{\\sigma_{j,h}}_{j=1..d,\\;h=1..H}\\;;\\;\\underbrace{q_h}_{h=1..H}\\;;\\;\\underbrace{v_h}_{h=1..H}\\,\\bigr] \\;\\in\\;\\mathbb{R}^{40},\n  \\label{eq:cgs_feat}\n\\end{equation}\nwhere $\\sigma_{j,h} = \\sqrt{(\\boldsymbol{\\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \\S\\ref{sec:aci}), and $v_h = \\tfrac{1}{2}\\log\\det(\\boldsymbol{\\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \\emph{which dimensions are uncertain} (per-DOF std), the \\emph{overall calibrated confidence level} (conformal radius), and the \\emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\\cite{reconvla2026}, this representation is strictly more informative.\n\n\\paragraph{Epistemic vs.\\ aleatoric positioning.}\nRecent work~\\cite{diu2026} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates epistemic uncertainty via multi-sample covariance: it rises when the model is uncertain about the correct action (e.g., out-of-distribution observations), rather than reflecting irreducible task ambiguity.  For action correction, epistemic uncertainty is the more relevant signal---it identifies \\emph{where the model needs help}.  We validate this distinction empirically in ablation~A7.\n\n\n%%% 4.2 ACI + COC %%%\n\\subsection{Adaptive Conformal Inference via Chunk Overlap Consistency}\n\\label{sec:aci}\n\nCGS requires a conformal threshold $q_h$ to convert Mahalanobis scores into calibrated prediction regions.  Static calibration on a held-out set, as in conformal quantile regression~\\cite{romano2019cqr}, assumes exchangeability between calibration and deployment data---an assumption that breaks under the distribution shifts common in real-world manipulation.  We instead adopt Adaptive Conformal Inference (ACI)~\\cite{gibbs2021aci}, which provides long-run coverage guarantees under arbitrary distribution shift, and equip it with a novel self-referential coverage signal.\n\n\\paragraph{The coverage signal problem.}\nACI updates the miscoverage level $\\alpha_t$ at each step based on whether the true action falls inside the conformal region.  In robotics, the most direct signal would check whether the \\emph{executed} action lies within the predicted region.  However, contact dynamics cause the achieved end-effector displacement to differ from the commanded action, corrupting this signal.\n\n\\paragraph{Chunk Overlap Consistency (COC).}\nWe exploit the temporal overlap inherent in receding-horizon action chunking.  At control step $t$, the VLA predicts a chunk $[a_t^1,\\dots,a_t^H]$ with associated conformal ellipsoids $\\{C_t^h\\}_{h=1}^H$ derived from the Mahalanobis score (\\ref{eq:mahal}) and threshold $q_h$.  After executing $a_t^1$ and observing the new state $s_{t+1}$, we draw $K{=}10$ fresh samples and compute the new first-step mean $\\boldsymbol{\\mu}_{t+1}^1$.  The COC coverage indicator is:\n\\begin{equation}\n  \\mathrm{err}_t = \\mathbb{1}\\bigl[\\boldsymbol{\\mu}_{t+1}^1 \\notin C_t^2\\bigr],\n  \\label{eq:coc}\n\\end{equation}\ni.e., we check whether the next step's predicted action falls within the \\emph{previous} step's conformal region for the overlapping horizon position.\n\nCOC has four properties that make it well-suited for online calibration:\n(i)~it is self-referential, requiring no external supervisor or trained reward model;\n(ii)~it compares prediction-to-prediction rather than prediction-to-execution, making it robust to contact dynamics;\n(iii)~it directly measures calibration quality---whether the conformal regions are appropriately sized;\n(iv)~it produces a signal at every control step, not only at episode boundaries.\n\n\\paragraph{Online update rule.}\nThe ACI update follows \\cite{gibbs2021aci}:\n\\begin{equation}\n  \\alpha_{t+1} = \\alpha_t + \\gamma\\bigl(\\alpha_{\\mathrm{target}} - \\mathrm{err}_t\\bigr),\n  \\label{eq:aci_update}\n\\end{equation}\nwhere $\\gamma$ is the learning rate and $\\alpha_{\\mathrm{target}}$ is the desired miscoverage rate.  When $\\mathrm{err}_t{=}1$ (the region failed to cover), $\\alpha_{t+1}$ decreases, widening the next region; when $\\mathrm{err}_t{=}0$, $\\alpha_{t+1}$ increases, tightening it.  Within each episode, we apply exponentially weighted conformal prediction~\\cite{barber2023conformal} with decay parameter $\\rho$ to down-weight stale calibration data.  Across episodes, the fraction of intra-episode COC hits serves as $\\mathrm{err}_t$ for a cross-episode ACI update, enabling the threshold to adapt over the course of deployment.\n\n\n%%% 4.3 CRM %%%\n\\subsection{Conformal Refinement Module}\n\\label{sec:crm}\n\nThe Conformal Refinement Module (CRM) is a lightweight network that performs dimension-selective action correction, conditioned on the structured uncertainty features from CGS.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$250K parameters).  Its input concatenates three sources:\n(i)~the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the base VLA encoder,\n(ii)~the 40D CGS feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$, and\n(iii)~the mean action $\\boldsymbol{\\mu} \\in \\mathbb{R}^{30}$ ($d{\\times}H = 6{\\times}5$).\nThe output is a residual correction $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the refined action is:\n\\begin{equation}\n  \\mathbf{a}^* = \\boldsymbol{\\mu} + \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}},\\;\\boldsymbol{\\varphi}_{\\mathrm{CGS}},\\;\\boldsymbol{\\mu}).\n  \\label{eq:crm}\n\\end{equation}\n\n\\paragraph{Training.}\nCRM is trained with a single objective:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:crm_loss}\n\\end{equation}\non demonstration trajectories from LIBERO~\\cite{liberoplus2025} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.\n\nACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\\cite{cploop2025}.\n\n\\paragraph{Why per-DOF conditioning enables selective correction.}\nTo build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \\cite{reconvla2026}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ instead reveals that $\\sigma_{x},\\sigma_{y} \\gg \\sigma_{z},\\sigma_{\\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\\ref{sec:experiments} demonstrates it on real VLA tasks.\n\n\\paragraph{Inference protocol.}\nEach control step proceeds as: draw $K{=}10$ samples $\\to$ compute CGS $\\to$ apply CRM $\\to$ execute the first action of the refined chunk $\\to$ observe new state $\\to$ draw $K{=}10$ fresh samples $\\to$ compute COC (\\ref{eq:coc}) $\\to$ ACI update (\\ref{eq:aci_update}).  The entire module adds ${\\sim}$250K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex",
    "content": "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 3 -- Motivating Experiment\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Motivating Experiment}\n\\label{sec:motivating}\n\nBefore committing to the full \\textbf{ACR-VLA} pipeline, we ask a targeted question: \\emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.\n\n\\paragraph{Setup.}\nA synthetic policy outputs actions $a\\in\\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\\sigma_x{=}0.5,\\;\\sigma_y{=}0.1,\\;\\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.\n\nWe train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:\n\\begin{itemize}[nosep]\n  \\item \\textbf{Model A} (scalar): conditioned on the average standard deviation $\\bar{\\sigma}=\\tfrac{1}{3}\\sum_j\\sigma_j$.\n  \\item \\textbf{Model B} (per-DOF): conditioned on the full vector $[\\sigma_x,\\sigma_y,\\sigma_z]$.\n  \\item \\textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.\n\\end{itemize}\nTo match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \\emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \\textbf{ACR-VLA}).\n\n\\paragraph{Results.}\nTable~\\ref{tab:motivating} reports per-axis MSE over 1{,}000 test episodes at a 5:1 anisotropy ratio ($\\sigma_x/\\sigma_y$) with $K{=}10$ estimated uncertainty.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-axis MSE ($\\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{=}10$ estimated uncertainty). Model~B, which receives per-DOF uncertainty, preserves accuracy on the low-uncertainty axes ($y,z$) where Model~A and~C over-correct.}\n\\label{tab:motivating}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Conditioning & MSE$_x$ & MSE$_y$ & MSE$_z$ & Total MSE \\\\\n\\midrule\nA & scalar $\\bar\\sigma$ & 0.1874 & 0.0247 & 0.0243 & 0.0788 \\\\\n\\textbf{B} & \\textbf{per-DOF} $[\\sigma_x,\\sigma_y,\\sigma_z]$ & \\textbf{0.1829} & \\textbf{0.0191} & \\textbf{0.0185} & \\textbf{0.0735} \\\\\nC & none & 0.2151 & 0.0250 & 0.0246 & 0.0882 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel~B reduces total MSE by 6.7\\% relative to~A and by 16.7\\% relative to~C.  The gains concentrate on the non-perturbed axes: $y$- and $z$-axis MSE drop by 22.7\\% and 23.9\\% versus~A, indicating that Model~B learns to leave low-uncertainty dimensions largely untouched while directing correction effort toward the high-uncertainty $x$-axis.  Model~A, receiving only a scalar average, lacks the information to make this distinction and applies a uniform correction that degrades the already-accurate axes.\n\nWith oracle (ground-truth) variances, the ranking $\\text{B}>\\text{A}>\\text{C}$ is preserved with larger margins (non-perturbed axis improvements of 22--38\\% over~A).  Moving from oracle to $K{=}10$ estimation reduces relative gains by roughly 15 percentage points, reflecting finite-sample noise, but does not alter the ordering.  The pattern also holds at weaker anisotropy ratios (2:1 and 1.5:1): across all six conditions tested, Model~B consistently outperforms both baselines.\n\n\\paragraph{Takeaway.}\nEven a simple MLP can exploit per-DOF uncertainty structure for dimension-selective correction---a capability that scalar summaries cannot provide.  This motivates the design of \\textbf{ACR-VLA}, which extracts rich per-DOF features from a flow-matching VLA and feeds them into a learned correction module (Section~\\ref{sec:method}).\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 4 -- Method\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA) is an inference-time, post-hoc module that attaches to any flow-matching VLA without modifying its weights.  It comprises three components (Figure~\\ref{fig:pipeline}):\n\\begin{enumerate}[nosep]\n  \\item \\textbf{Conformalized Gaussian Scoring} (CGS, \\S\\ref{sec:cgs}): draws $K{=}10$ action samples per step, fits a shrinkage-regularized Gaussian, and extracts a 40-dimensional structured uncertainty feature.\n  \\item \\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency} (ACI+COC, \\S\\ref{sec:aci}): maintains an online conformal threshold that adapts to distribution shift using a self-referential coverage signal from overlapping action chunks.\n  \\item \\textbf{Conformal Refinement Module} (CRM, \\S\\ref{sec:crm}): a lightweight MLP that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\n\\end{enumerate}\n\nWe instantiate \\textbf{ACR-VLA} on SmolVLA~\\cite{smolvla2025}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).\n\n\n%%% 4.1 CGS %%%\n\\subsection{Conformalized Gaussian Scoring}\n\\label{sec:cgs}\n\nCGS converts a set of stochastic action samples from the base VLA into a compact uncertainty descriptor that captures \\emph{which} degrees of freedom are uncertain and \\emph{how} they co-vary---information that a scalar nonconformity score discards.\n\n\\paragraph{Sampling and truncation.}\nAt each control step, we draw $K{=}10$ action chunks from the frozen base VLA via independent flow-matching rollouts.  Although SmolVLA predicts 50-step chunks, under receding-horizon execution only the first few steps influence the robot before re-planning.  We therefore retain only the first $H{=}5$ steps, yielding $K$ samples $\\{a_h^{(k)}\\}_{k=1}^{K}$ with $a_h^{(k)}\\in\\mathbb{R}^{d}$ for each horizon step $h=1,\\dots,H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1-\\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity.  With a dimension-to-sample ratio $p/n = d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error due to the Marchenko--Pastur effect; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nWe define a joint multivariate nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis single score captures cross-DOF covariance structure.  In contrast, treating each DOF independently and applying Bonferroni correction across all $d{\\times}H = 30$ marginals yields intervals that are substantially wider than necessary.  Our joint formulation requires Bonferroni correction only across $H{=}5$ horizon steps (target level $\\alpha/H$ per step), preserving tight per-step regions~\\cite{braun2025cgs}.\n\n\\paragraph{CGS feature vector.}\nWe assemble a 40-dimensional feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ that is passed to the refinement module:\n\\begin{equation}\n  \\boldsymbol{\\varphi}_{\\mathrm{CGS}} = \\bigl[\\,\\underbrace{\\sigma_{j,h}}_{j=1..d,\\;h=1..H}\\;;\\;\\underbrace{q_h}_{h=1..H}\\;;\\;\\underbrace{v_h}_{h=1..H}\\,\\bigr] \\;\\in\\;\\mathbb{R}^{40},\n  \\label{eq:cgs_feat}\n\\end{equation}\nwhere $\\sigma_{j,h} = \\sqrt{(\\boldsymbol{\\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \\S\\ref{sec:aci}), and $v_h = \\tfrac{1}{2}\\log\\det(\\boldsymbol{\\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \\emph{which dimensions are uncertain} (per-DOF std), the \\emph{overall calibrated confidence level} (conformal radius), and the \\emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\\cite{reconvla2026}, this representation is strictly more informative.\n\n\\paragraph{Epistemic vs.\\ aleatoric positioning.}\nRecent work~\\cite{diu2026} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates epistemic uncertainty via multi-sample covariance: it rises when the model is uncertain about the correct action (e.g., out-of-distribution observations), rather than reflecting irreducible task ambiguity.  For action correction, epistemic uncertainty is the more relevant signal---it identifies \\emph{where the model needs help}.  We validate this distinction empirically in ablation~A7.\n\n\n%%% 4.2 ACI + COC %%%\n\\subsection{Adaptive Conformal Inference via Chunk Overlap Consistency}\n\\label{sec:aci}\n\nCGS requires a conformal threshold $q_h$ to convert Mahalanobis scores into calibrated prediction regions.  Static calibration on a held-out set, as in conformal quantile regression~\\cite{romano2019cqr}, assumes exchangeability between calibration and deployment data---an assumption that breaks under the distribution shifts common in real-world manipulation.  We instead adopt Adaptive Conformal Inference (ACI)~\\cite{gibbs2021aci}, which provides long-run coverage guarantees under arbitrary distribution shift, and equip it with a novel self-referential coverage signal.\n\n\\paragraph{The coverage signal problem.}\nACI updates the miscoverage level $\\alpha_t$ at each step based on whether the true action falls inside the conformal region.  In robotics, the most direct signal would check whether the \\emph{executed} action lies within the predicted region.  However, contact dynamics cause the achieved end-effector displacement to differ from the commanded action, corrupting this signal.\n\n\\paragraph{Chunk Overlap Consistency (COC).}\nWe exploit the temporal overlap inherent in receding-horizon action chunking.  At control step $t$, the VLA predicts a chunk $[a_t^1,\\dots,a_t^H]$ with associated conformal ellipsoids $\\{C_t^h\\}_{h=1}^H$ derived from the Mahalanobis score (\\ref{eq:mahal}) and threshold $q_h$.  After executing $a_t^1$ and observing the new state $s_{t+1}$, we draw $K{=}10$ fresh samples and compute the new first-step mean $\\boldsymbol{\\mu}_{t+1}^1$.  The COC coverage indicator is:\n\\begin{equation}\n  \\mathrm{err}_t = \\mathbb{1}\\bigl[\\boldsymbol{\\mu}_{t+1}^1 \\notin C_t^2\\bigr],\n  \\label{eq:coc}\n\\end{equation}\ni.e., we check whether the next step's predicted action falls within the \\emph{previous} step's conformal region for the overlapping horizon position.\n\nCOC has four properties that make it well-suited for online calibration:\n(i)~it is self-referential, requiring no external supervisor or trained reward model;\n(ii)~it compares prediction-to-prediction rather than prediction-to-execution, making it robust to contact dynamics;\n(iii)~it directly measures calibration quality---whether the conformal regions are appropriately sized;\n(iv)~it produces a signal at every control step, not only at episode boundaries.\n\n\\paragraph{Online update rule.}\nThe ACI update follows \\cite{gibbs2021aci}:\n\\begin{equation}\n  \\alpha_{t+1} = \\alpha_t + \\gamma\\bigl(\\alpha_{\\mathrm{target}} - \\mathrm{err}_t\\bigr),\n  \\label{eq:aci_update}\n\\end{equation}\nwhere $\\gamma$ is the learning rate and $\\alpha_{\\mathrm{target}}$ is the desired miscoverage rate.  When $\\mathrm{err}_t{=}1$ (the region failed to cover), $\\alpha_{t+1}$ decreases, widening the next region; when $\\mathrm{err}_t{=}0$, $\\alpha_{t+1}$ increases, tightening it.  Within each episode, we apply exponentially weighted conformal prediction~\\cite{barber2023conformal} with decay parameter $\\rho$ to down-weight stale calibration data.  Across episodes, the fraction of intra-episode COC hits serves as $\\mathrm{err}_t$ for a cross-episode ACI update, enabling the threshold to adapt over the course of deployment.\n\n\n%%% 4.3 CRM %%%\n\\subsection{Conformal Refinement Module}\n\\label{sec:crm}\n\nThe Conformal Refinement Module (CRM) is a lightweight network that performs dimension-selective action correction, conditioned on the structured uncertainty features from CGS.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$250K parameters).  Its input concatenates three sources:\n(i)~the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the base VLA encoder,\n(ii)~the 40D CGS feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$, and\n(iii)~the mean action $\\boldsymbol{\\mu} \\in \\mathbb{R}^{30}$ ($d{\\times}H = 6{\\times}5$).\nThe output is a residual correction $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the refined action is:\n\\begin{equation}\n  \\mathbf{a}^* = \\boldsymbol{\\mu} + \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}},\\;\\boldsymbol{\\varphi}_{\\mathrm{CGS}},\\;\\boldsymbol{\\mu}).\n  \\label{eq:crm}\n\\end{equation}\n\n\\paragraph{Training.}\nCRM is trained with a single objective:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:crm_loss}\n\\end{equation}\non demonstration trajectories from LIBERO~\\cite{liberoplus2025} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.\n\nACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\\cite{cploop2025}.\n\n\\paragraph{Why per-DOF conditioning enables selective correction.}\nTo build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \\cite{reconvla2026}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ instead reveals that $\\sigma_{x},\\sigma_{y} \\gg \\sigma_{z},\\sigma_{\\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\\ref{sec:experiments} demonstrates it on real VLA tasks.\n\n\\paragraph{Inference protocol.}\nEach control step proceeds as: draw $K{=}10$ samples $\\to$ compute CGS $\\to$ apply CRM $\\to$ execute the first action of the refined chunk $\\to$ observe new state $\\to$ draw $K{=}10$ fresh samples $\\to$ compute COC (\\ref{eq:coc}) $\\to$ ACI update (\\ref{eq:aci_update}).  The entire module adds ${\\sim}$250K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T03:41:47.203170+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T03:41:47.203423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T03:41:47.203755+00:00_

1	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
2	%% Section 3 -- Motivating Experiment
3	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
4	
5	\section{Motivating Experiment}
6	\label{sec:motivating}
7	
8	Before committing to the full \textbf{ACR-VLA} pipeline, we ask a targeted question: \emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.
9	
10	\paragraph{Setup.}
11	A synthetic policy outputs actions $a\in\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\sigma_x{=}0.5,\;\sigma_y{=}0.1,\;\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.
12	
13	We train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:
14	\begin{itemize}[nosep]
15	  \item \textbf{Model A} (scalar): conditioned on the average standard deviation $\bar{\sigma}=\tfrac{1}{3}\sum_j\sigma_j$.
16	  \item \textbf{Model B} (per-DOF): conditioned on the full vector $[\sigma_x,\sigma_y,\sigma_z]$.
17	  \item \textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.
18	\end{itemize}
19	To match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \textbf{ACR-VLA}).
20	
21	\paragraph{Results.}
22	Table~\ref{tab:motivating} reports per-axis MSE over 1{,}000 test episodes at a 5:1 anisotropy ratio ($\sigma_x/\sigma_y$) with $K{=}10$ estimated uncertainty.
23	
24	\begin{table}[t]
25	\centering
26	\caption{Per-axis MSE ($\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{
…[truncated 14419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T03:41:47.204168+00:00_

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
  "session": "worker_paper_writing_method_section_20260513T033854",
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

_source line 8 · 2026-05-13T03:41:47.204521+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T03:41:47.204731+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Method Section Draft (Section 3 + 4)",
  "type": "paper",
  "description": "LaTeX draft of Section 3 (Motivating Experiment) and Section 4 (Method: CGS, ACI+COC, CRM) for ACR-VLA paper. Pure section content, no preamble.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex",
  "tags": "['paper', 'method', 'latex', 'section3', 'section4']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Method Section Draft (Section 3 + 4)",
    "type": "paper",
    "description": "LaTeX draft of Section 3 (Motivating Experiment) and Section 4 (Method: CGS, ACI+COC, CRM) for ACR-VLA paper. Pure section content, no preamble.",
    "project": "acr-vla-conformal-refinement",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex",
    "tags": "['paper', 'method', 'latex', 'section3', 'section4']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T03:41:47.204962+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_0a67e7\", \"name\": \"Method Section Draft (Section 3 + 4)\", \"type\": \"paper\", \"description\": \"LaTeX draft of Section 3 (Motivating Experiment) and Section 4 (Method: CGS, ACI+COC, CRM) for ACR-VLA paper. Pure section content, no preamble.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T03:41:35.063669+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"section3\", \"section4\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_section_20260513T033854",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-13T03:41:47.205232+00:00_

文件已保存并注册。

**产出**: `artifacts/method_section_draft.tex` (art_20260513_0a67e7)

**结构概览**:
- **Section 3** (~350 words + 1 table): 合成 3D point-reaching 实验，Table 1 报告 K=10 estimated 的 Group 4 数据，文字覆盖 oracle 和弱各向异性条件
- **Section 4.1 CGS** (~400 words, Eq. 1–4): 采样截断 → Ledoit-Wolf 收缩 → Mahalanobis score → 40D 特征向量 → epistemic vs aleatoric 定位
- **Section 4.2 ACI+COC** (~350 words, Eq. 5–6): coverage signal 问题 → COC 定义 → 四个优势 → ACI update rule + 跨 episode 聚合
- **Section 4.3 CRM** (~300 words, Eq. 7–8): 架构 → MSE 训练 → 训练/calibration 解耦 → per-DOF 直觉 → inference protocol

6 个公式有 label，1 个 table 用 booktabs，13 处引用均来自提供的 verified list。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_section_20260513T033854"
}
```

</details>

---
