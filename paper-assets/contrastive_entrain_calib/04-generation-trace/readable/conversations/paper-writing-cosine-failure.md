# paper writing cosine failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_cosine_failure_20260520T074932.jsonl`
- **Structured JSON:** [`58038b6d372adc84e197.json`](../../sessions/58/58038b6d372adc84e197.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T07:51:03.215590+00:00_

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
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T07:51:03.216221+00:00_

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
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T07:51:03.216430+00:00_

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
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T07:51:03.216808+00:00_

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
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T07:51:03.217070+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T07:51:03.217269+00:00_

docs/paper/sections/framework.tex
docs/paper/sections/direction_quality.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T07:51:03.217460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T07:51:03.217652+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	This section establishes the notation, experimental components, and evaluation protocol used throughout the paper.
5	We first describe how the contrastive sycophancy direction $\dsyc$ is extracted (\S\ref{ssec:extraction}), then define three reward formulations that incorporate $\dsyc$ into GRPO training (\S\ref{ssec:reward}), explain the online recalibration procedure (\S\ref{ssec:recalib}), and finally specify the evaluation metrics (\S\ref{ssec:eval}).
6	
7	\subsection{Direction Extraction}
8	\label{ssec:extraction}
9	
10	We extract a linear sycophancy direction $\dsyc$ from the residual stream of a target model using contrastive activation pairs.
11	Each pair consists of two model responses to the same user challenge: a \emph{valid correction}, in which the model appropriately revises its earlier answer upon receiving well-supported counter-evidence, and a \emph{sycophantic capitulation}, in which the model abandons a correct answer under social pressure without adequate evidential warrant.
12	
13	To isolate the cognitive signal from surface-level linguistic variation, we apply style control: both responses in each pair are generated with matched hedging patterns, politeness markers, and response length, so that $\dsyc$ reflects the distinction between warranted and unwarranted belief change rather than stylistic differences.
14	Concretely, we construct 362 style-controlled contrastive activations from 181 paired examples stratified across three evidence-strength levels (weak, medium, strong).
15	
16	Given a target layer $\ell$, let $\mathbf{h}^{+}_i$ denote the residual-stream activation for the $i$-th valid correction and $\mathbf{h}^{-}_i$ for the corresponding sycophantic capitulation.
17	The sycophancy direction is the mean difference:
18	\begin{equation}
19	\label{eq:dsyc}
20	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
21	\end{equation}
22	where $N{=}181$ 
…[truncated 4916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T07:51:03.217802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T07:51:03.218035+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827 \pm 0.028$ at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
21	Llama-3-8B achi
…[truncated 2874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T07:51:03.218259+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex",
  "content": "\\section{Cosine \\texorpdfstring{$\\rone$}{R1}: Structural Failure}\n\\label{sec:cosine_failure}\n\nSection~\\ref{sec:direction_quality} established that $\\dsyc$ achieves AUROC 0.827 on Qwen3-8B and generalizes across models.\nWe now test whether this discriminability translates into a viable GRPO reward signal.\nThis section reports four configurations (F1a--F1d) that form a systematic diagnostic chain: each configuration resolves the failure mode of its predecessor but exposes a deeper structural limitation.\nTable~\\ref{tab:cosine_chain} summarizes the chain; Figure~\\ref{fig:cosine_failure} visualizes the training dynamics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cosine $\\rone$ failure chain. Each configuration addresses the preceding failure but reveals a more fundamental limitation. All experiments use Qwen3-8B with LoRA (rank$=$64) and GRPO with $R = w_1 \\cdot \\rone + w_3 \\cdot \\rthree$.}\n\\label{tab:cosine_chain}\n\\begin{tabular}{lllll}\n\\toprule\nConfig & $\\rone$ Formula & $w_1$ & Outcome & Root Cause \\\\\n\\midrule\nF1a & $\\tanh(\\mathbf{h}\\cdot\\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\\\\nF1b & $\\cos(\\mathbf{h},\\, \\dsyc)$ & 0.25 & $\\rone \\approx 0$ & Gap too small \\\\\nF1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\\\\nF1d & $5\\cos(\\mathbf{h},\\, \\dsyc)$ & 0.40 & Mode collapse & $\\rthree$ saturation + noise \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{F1a: Tanh gate saturation (exp-002).}\nThe initial configuration defines $\\rone = \\tanh(\\mathbf{h} \\cdot \\dsyc / 20)$ with $w_1{=}0.25$, $w_3{=}0.75$.\nThe dot product formulation preserves directional sensitivity but is not scale-invariant: activation norms in the residual stream range from $100{\\times}$ to $1{,}200{\\times}$ the direction norm across layers.\nThis norm mismatch drives the pre-activation into the saturated tails of tanh, where the gradient vanishes.\nBy step 955, $\\rone$ contributes effectively zero gradient to the combined reward, and training was terminated.\nSubsequent weight adjustments ($w_1{=}0.15$, $w_3{=}0.65$) did not resolve the saturation because the pre-activation magnitude, not the weight, controls the gate.\nThe diagnostic conclusion is clear: any formulation that passes raw dot products through a bounded nonlinearity will saturate in high-norm activation spaces.\nCosine similarity, which normalizes by both norms, is the natural alternative.\n\n\\paragraph{F1b: Raw cosine signal too weak (exp-002v2).}\nReplacing the dot product with cosine similarity ($\\rone = \\cos(\\mathbf{h},\\, \\dsyc)$) eliminates the norm dependence.\nHowever, the cosine gap between valid corrections and sycophantic capitulations is only 0.098 when averaged across the seven highest-AUROC layers.\nWith $w_1{=}0.25$, this yields an effective $\\rone$ contribution of approximately $0.025$ per token, a signal that is negligible relative to $\\rthree$ variance.\nThroughout training, $\\rone \\approx 0$, and the combined reward $R$ is functionally equivalent to $w_3 \\cdot \\rthree$ alone.\nTraining was terminated after confirming that the sycophancy component exerts no measurable influence on policy updates.\nThe failure isolates a quantitative limitation: the cosine projection of $\\dsyc$ onto individual activations produces a gap too narrow to generate meaningful reward contrast between sycophantic and non-sycophantic completions.\n\n\\paragraph{F1c: Recalibration induces mode collapse (exp002v2-recalib).}\nOne hypothesis for the weak signal in F1b is that $\\dsyc$ drifts during LoRA training, eroding the already-small gap.\nTo test this, we resume from the exp-002v2 checkpoint at step 500 and enable the online recalibration procedure described in \\S\\ref{ssec:recalib}, re-extracting $\\dsyc$ every 500 steps.\nRecalibration increases the offline AUROC from 0.82 to 0.91, confirming that the refreshed direction better separates the updated activations.\nTraining collapses nonetheless.\nWithin 300 steps of the first recalibration event, the policy degenerates into a low-entropy mode: generation entropy drops to 0.069, and mean response length contracts to 62 tokens.\nThe mechanism is a reward discontinuity at the recalibration boundary.\nWhen $\\dsyc$ is replaced by a fresh direction, the cosine projection of every cached rollout shifts abruptly.\nCompletions that were mildly rewarded under the stale direction may become penalized under the fresh one, and vice versa.\nThis discontinuity destabilizes the GRPO advantage estimates and drives the policy toward a narrow region of activation space that remains low-risk under both the old and new directions.\nThe result is a degenerate policy that produces short, hedged responses regardless of the input.\nImproving direction quality via recalibration, paradoxically, makes the reward landscape less stable.\n\n\\paragraph{F1d: Scaling amplifies noise (exp-002v3).}\nConfiguration F1d addresses the magnitude problem directly: $\\rone = 5 \\cdot \\cos(\\mathbf{h},\\, \\dsyc)$ with $w_1{=}0.4$, $w_3{=}0.6$.\nThe $5{\\times}$ scaling lifts the $\\rone$ contribution above the $\\rthree$ noise floor, but it simultaneously amplifies the noise in the cosine projection.\nTraining proceeds in three phases.\nIn the first phase (steps 100--300), $\\rthree$ saturates at 0.9998 as the policy rapidly learns to produce NLI-consistent answers; mean response length drops from 247 to 80 tokens and entropy falls from 0.45 to 0.10.\nIn the second phase (steps 300--2150), the combined reward degenerates to $R \\approx w_1 \\cdot \\rone + \\text{const}$ because the saturated $\\rthree$ provides no gradient.\n$\\rone$ is now the sole learning signal, but its mean oscillates between $-0.46$ and $+0.41$ with no sustained positive trend, because the cosine projection conflates warranted belief revision with unwarranted capitulation (both shift activations toward the user's position along $\\dsyc$).\nIn the third phase (step 2160), the policy collapses terminally: entropy drops from 0.056 to 0.026, and the fraction of completions with zero reward standard deviation rises from 0.125 to 0.419, indicating that the policy has converged to a near-deterministic mode.\n\n\\paragraph{Unified diagnosis.}\nThe four configurations converge on a single structural limitation.\nThe cosine gap between valid and sycophantic activations (0.098 across layers) is too narrow to serve as a reward signal, and this narrowness is not a calibration artifact.\nRecalibration raises offline AUROC to 0.91 yet rewards still fail (F1c), confirming that direction quality is not the bottleneck.\nThe root cause is semantic: $\\dsyc$ encodes the \\emph{direction} of belief change (toward or away from the user's position) but does not encode whether that change is \\emph{warranted}.\nA model that appropriately revises an incorrect answer in response to strong evidence and a model that capitulates under social pressure both shift their activations toward the user's position along $\\dsyc$.\nThe cosine projection assigns similar scores to both behaviors.\nScaling the projection (F1d) amplifies this conflation rather than resolving it.\nAny reward formulation that uses $\\dsyc$ as a continuous scalar will inherit this ambiguity.\nSection~\\ref{sec:probe_trap} examines whether discretizing the signal via a binary probe can escape this limitation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex",
    "content": "\\section{Cosine \\texorpdfstring{$\\rone$}{R1}: Structural Failure}\n\\label{sec:cosine_failure}\n\nSection~\\ref{sec:direction_quality} established that $\\dsyc$ achieves AUROC 0.827 on Qwen3-8B and generalizes across models.\nWe now test whether this discriminability translates into a viable GRPO reward signal.\nThis section reports four configurations (F1a--F1d) that form a systematic diagnostic chain: each configuration resolves the failure mode of its predecessor but exposes a deeper structural limitation.\nTable~\\ref{tab:cosine_chain} summarizes the chain; Figure~\\ref{fig:cosine_failure} visualizes the training dynamics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cosine $\\rone$ failure chain. Each configuration addresses the preceding failure but reveals a more fundamental limitation. All experiments use Qwen3-8B with LoRA (rank$=$64) and GRPO with $R = w_1 \\cdot \\rone + w_3 \\cdot \\rthree$.}\n\\label{tab:cosine_chain}\n\\begin{tabular}{lllll}\n\\toprule\nConfig & $\\rone$ Formula & $w_1$ & Outcome & Root Cause \\\\\n\\midrule\nF1a & $\\tanh(\\mathbf{h}\\cdot\\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\\\\nF1b & $\\cos(\\mathbf{h},\\, \\dsyc)$ & 0.25 & $\\rone \\approx 0$ & Gap too small \\\\\nF1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\\\\nF1d & $5\\cos(\\mathbf{h},\\, \\dsyc)$ & 0.40 & Mode collapse & $\\rthree$ saturation + noise \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{F1a: Tanh gate saturation (exp-002).}\nThe initial configuration defines $\\rone = \\tanh(\\mathbf{h} \\cdot \\dsyc / 20)$ with $w_1{=}0.25$, $w_3{=}0.75$.\nThe dot product formulation preserves directional sensitivity but is not scale-invariant: activation norms in the residual stream range from $100{\\times}$ to $1{,}200{\\times}$ the direction norm across layers.\nThis norm mismatch drives the pre-activation into the saturated tails of tanh, where the gradient vanishes.\nBy step 955, $\\rone$ contributes effectively zero gradient to the combined reward, and training was terminated.\nSubsequent weight adjustments ($w_1{=}0.15$, $w_3{=}0.65$) did not resolve the saturation because the pre-activation magnitude, not the weight, controls the gate.\nThe diagnostic conclusion is clear: any formulation that passes raw dot products through a bounded nonlinearity will saturate in high-norm activation spaces.\nCosine similarity, which normalizes by both norms, is the natural alternative.\n\n\\paragraph{F1b: Raw cosine signal too weak (exp-002v2).}\nReplacing the dot product with cosine similarity ($\\rone = \\cos(\\mathbf{h},\\, \\dsyc)$) eliminates the norm dependence.\nHowever, the cosine gap between valid corrections and sycophantic capitulations is only 0.098 when averaged across the seven highest-AUROC layers.\nWith $w_1{=}0.25$, this yields an effective $\\rone$ contribution of approximately $0.025$ per token, a signal that is negligible relative to $\\rthree$ variance.\nThroughout training, $\\rone \\approx 0$, and the combined reward $R$ is functionally equivalent to $w_3 \\cdot \\rthree$ alone.\nTraining was terminated after confirming that the sycophancy component exerts no measurable influence on policy updates.\nThe failure isolates a quantitative limitation: the cosine projection of $\\dsyc$ onto individual activations produces a gap too narrow to generate meaningful reward contrast between sycophantic and non-sycophantic completions.\n\n\\paragraph{F1c: Recalibration induces mode collapse (exp002v2-recalib).}\nOne hypothesis for the weak signal in F1b is that $\\dsyc$ drifts during LoRA training, eroding the already-small gap.\nTo test this, we resume from the exp-002v2 checkpoint at step 500 and enable the online recalibration procedure described in \\S\\ref{ssec:recalib}, re-extracting $\\dsyc$ every 500 steps.\nRecalibration increases the offline AUROC from 0.82 to 0.91, confirming that the refreshed direction better separates the updated activations.\nTraining collapses nonetheless.\nWithin 300 steps of the first recalibration event, the policy degenerates into a low-entropy mode: generation entropy drops to 0.069, and mean response length contracts to 62 tokens.\nThe mechanism is a reward discontinuity at the recalibration boundary.\nWhen $\\dsyc$ is replaced by a fresh direction, the cosine projection of every cached rollout shifts abruptly.\nCompletions that were mildly rewarded under the stale direction may become penalized under the fresh one, and vice versa.\nThis discontinuity destabilizes the GRPO advantage estimates and drives the policy toward a narrow region of activation space that remains low-risk under both the old and new directions.\nThe result is a degenerate policy that produces short, hedged responses regardless of the input.\nImproving direction quality via recalibration, paradoxically, makes the reward landscape less stable.\n\n\\paragraph{F1d: Scaling amplifies noise (exp-002v3).}\nConfiguration F1d addresses the magnitude problem directly: $\\rone = 5 \\cdot \\cos(\\mathbf{h},\\, \\dsyc)$ with $w_1{=}0.4$, $w_3{=}0.6$.\nThe $5{\\times}$ scaling lifts the $\\rone$ contribution above the $\\rthree$ noise floor, but it simultaneously amplifies the noise in the cosine projection.\nTraining proceeds in three phases.\nIn the first phase (steps 100--300), $\\rthree$ saturates at 0.9998 as the policy rapidly learns to produce NLI-consistent answers; mean response length drops from 247 to 80 tokens and entropy falls from 0.45 to 0.10.\nIn the second phase (steps 300--2150), the combined reward degenerates to $R \\approx w_1 \\cdot \\rone + \\text{const}$ because the saturated $\\rthree$ provides no gradient.\n$\\rone$ is now the sole learning signal, but its mean oscillates between $-0.46$ and $+0.41$ with no sustained positive trend, because the cosine projection conflates warranted belief revision with unwarranted capitulation (both shift activations toward the user's position along $\\dsyc$).\nIn the third phase (step 2160), the policy collapses terminally: entropy drops from 0.056 to 0.026, and the fraction of completions with zero reward standard deviation rises from 0.125 to 0.419, indicating that the policy has converged to a near-deterministic mode.\n\n\\paragraph{Unified diagnosis.}\nThe four configurations converge on a single structural limitation.\nThe cosine gap between valid and sycophantic activations (0.098 across layers) is too narrow to serve as a reward signal, and this narrowness is not a calibration artifact.\nRecalibration raises offline AUROC to 0.91 yet rewards still fail (F1c), confirming that direction quality is not the bottleneck.\nThe root cause is semantic: $\\dsyc$ encodes the \\emph{direction} of belief change (toward or away from the user's position) but does not encode whether that change is \\emph{warranted}.\nA model that appropriately revises an incorrect answer in response to strong evidence and a model that capitulates under social pressure both shift their activations toward the user's position along $\\dsyc$.\nThe cosine projection assigns similar scores to both behaviors.\nScaling the projection (F1d) amplifies this conflation rather than resolving it.\nAny reward formulation that uses $\\dsyc$ as a continuous scalar will inherit this ambiguity.\nSection~\\ref{sec:probe_trap} examines whether discretizing the signal via a binary probe can escape this limitation.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T07:51:03.218477+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T07:51:03.218617+00:00_

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
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
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

_source line 14 · 2026-05-20T07:51:03.218740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T07:51:03.218861+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "cosine_failure_section",
  "type": "paper",
  "description": "§4 Cosine R1: Structural Failure - complete LaTeX section covering 4-experiment failure chain (F1a-F1d) with diagnostic table and unified root cause analysis",
  "project": "contrastive_entrain_calib",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex",
  "tags": "['paper', 'section4', 'cosine-failure', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "cosine_failure_section",
    "type": "paper",
    "description": "§4 Cosine R1: Structural Failure - complete LaTeX section covering 4-experiment failure chain (F1a-F1d) with diagnostic table and unified root cause analysis",
    "project": "contrastive_entrain_calib",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex",
    "tags": "['paper', 'section4', 'cosine-failure', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T07:51:03.219039+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_7e9360\", \"name\": \"cosine_failure_section\", \"type\": \"paper\", \"description\": \"§4 Cosine R1: Structural Failure - complete LaTeX section covering 4-experiment failure chain (F1a-F1d) with diagnostic table and unified root cause analysis\", \"path\": \"projects/contrastive_entrain_calib/artifacts/_project/paper/cosine_failure.tex\", \"url\": null, \"project\": \"contrastive_entrain_calib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T07:50:50.856319+00:00\", \"tags\": [\"paper\", \"section4\", \"cosine-failure\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_cosine_failure_20260520T074932",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T07:51:03.219205+00:00_

§4 已写入 `docs/paper/sections/cosine_failure.tex`，约 700 words。

结构：
- **开头**：从 §3 的 discriminability 结果过渡，预告 4-experiment diagnostic chain
- **Table 1** (`tab:cosine_chain`)：4 行总结 F1a--F1d 的配置、公式、outcome、root cause
- **F1a**：tanh gate saturation，norm mismatch 导致梯度消失
- **F1b**：raw cosine gap 仅 0.098，信号被 R3 方差淹没
- **F1c**：recalibration 把 AUROC 提到 0.91 但引入 reward discontinuity，导致 mode collapse
- **F1d**：5x scaling 放大 noise，R3 step 100 饱和后 R1 独撑但 oscillate，终端 collapse
- **Unified diagnosis**：cosine projection 把 warranted revision 和 unwarranted capitulation 混为一谈，方向编码 belief change direction 但不编码 warrant；过渡到 §5 binary probe

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_cosine_failure_20260520T074932"
}
```

</details>

---
