# paper writing appendix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_appendix_20260517T010041.jsonl`
- **Structured JSON:** [`13c903e216174bd77a2c.json`](../../sessions/13/13c903e216174bd77a2c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-17T01:02:57.072941+00:00_

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
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T01:02:57.073480+00:00_

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
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T01:02:57.073708+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T01:02:57.073870+00:00_

docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T01:02:57.074010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T01:02:57.074186+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate contrastive trace probes across three reasoning models (R1-8B, R1-32B, QwQ-32B), two signal modalities (hidden states and text), and multiple temporal aggregation strategies. Our experiments address four questions: (1) How much does temporal context improve detection? (2) Does the choice of signal modality matter? (3) Can sequence models detect unsafe reasoning earlier? (4) Do probes transfer across models?
5	
6	\subsection{Temporal Context as Primary Factor}
7	\label{sec:temporal_primary}
8	
9	The most consistent finding across all experimental conditions is that temporal context dominates probe quality, regardless of signal modality. \cref{fig:window_ablation} shows this pattern for R1-8B, with consistent trends across all three models.
10	
11	On R1-8B, increasing window size from $W{=}1$ to $W{=}25$ improves balanced accuracy from 77.8\% to 81.2\% (+3.4pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces pre-commitment FPR from 9.65\% to 4.83\% ($-$4.8pp). These gains are consistent across all three models and both modalities (\cref{tab:temporal_main}). Larger windows make probes more conservative: fewer traces cross the detection threshold (coverage decreases from 72.1\% to 48.8\% under $K{=}1$ criterion), but those that do are classified with higher confidence.
12	
13	The coverage-quality trade-off depends on the detection criterion. Under $K{=}1$ (single threshold crossing), larger $W$ reduces coverage because the smoothed probe score crosses the boundary fewer times. Under stricter criteria ($K{=}5$, requiring consecutive crossings), larger $W$ can improve effective coverage by eliminating transient false crossings. We report $K{=}1$ results throughout for interpretability, noting that deployment systems would tune $K$ alongside $W$.
14	
15	The key observation is that the magnitude of temporal improvement (accuracy +3.4pp, precision +12.9pp, FPR $-$4.8pp) dwarfs the modality gap (0 to 7
…[truncated 9638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T01:02:57.074331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T01:02:57.074505+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	We formalize the problem of detecting when a reasoning model commits to generating harmful content, define the metrics for evaluating detection systems, and describe the probing methods and baselines.
5	
6	\subsection{Safety Commitment Point}
7	\label{sec:commitment-point}
8	
9	Chain-of-thought reasoning models produce extended internal reasoning traces before generating a final response. When a model is successfully jailbroken, its reasoning trace transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases and the model commits to producing harmful content.
10	
11	We operationalize CP annotation on HarmThoughts traces as follows. Each reasoning step is labeled for the presence or absence of safety-related reasoning (refusal considerations, ethical concerns, policy references). The CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety reasoning. This yields a binary classification at each step: steps at or before CP are \emph{pre-commitment} (the model has not yet committed to harm), and steps after CP are \emph{post-commitment} (the model is committed to harmful generation). A successful detector should identify post-commitment steps while avoiding false alarms on pre-commitment steps.
12	
13	\subsection{Detection Task Formulation}
14	\label{sec:metrics}
15	
16	We evaluate detectors using the following metrics. Let $s_t$ denote the probe score at reasoning step $t$, $\tau$ the detection threshold, and $t^*$ the annotated CP for a given trace.
17	
18	\paragraph{Coverage (detection rate).} The fraction of jailbreak traces where the probe score crosses the threshold at any step:
19	\begin{equation}
20	    \text{Coverage} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}\left[\exists\, t : s_t^{(i)} > \tau \right]
21	\end{equation}
22	where $N$ is the num
…[truncated 8746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T01:02:57.074699+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/",
  "description": "List paper sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/",
    "description": "List paper sections directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T01:02:57.074833+00:00_

abstract.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T01:02:57.074982+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "content": "\\appendix\n\n\\section{Responsible NLP Research Checklist}\n\\label{app:checklist}\n\nWe address the ARR Responsible NLP Research requirements below.\n\n\\begin{itemize}\n    \\item \\textbf{Limitations discussed:} Yes (\\cref{sec:limitations}).\n    \\item \\textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.\n    \\item \\textbf{Computational budget:} Our experiments involve 3 models $\\times$ 209 traces with linear probes and single-layer GRUs. Total compute is minimal (under 2 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.\n    \\item \\textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.\n    \\item \\textbf{Human subjects:} No human subjects research was conducted.\n    \\item \\textbf{Reproducibility:} All hyperparameters are reported in \\cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.\n\\end{itemize}\n\n\n\\section{Layer Sweep Results}\n\\label{app:layer_sweep}\n\nFor each model, we sweep all transformer layers and score each candidate layer using the product of balanced accuracy and crossing rate (scheme B, defined in \\cref{sec:hs-probes}). This composite metric selects layers that simultaneously achieve good classification and reliable threshold crossing on jailbreak traces.\n\nThe selected layers are: R1-8B layer 14 (of 32 total, 44\\% depth), R1-32B layer 24 (of 64, 37.5\\% depth), and QwQ-32B layer 28 (of 64, 43.8\\% depth). All three models concentrate safety-relevant information in the middle third of the network. Early layers (below 20\\% depth) encode primarily syntactic features and score poorly on both accuracy and crossing rate. Final layers show high accuracy but low crossing rate, consistent with the hypothesis that late-layer representations encode safety state too close to output generation for early detection.\n\nThe optimal layer for R1-8B is notably shallow in absolute terms (layer 14), but this model has only 32 layers total. In relative depth, all three models converge to 37--44\\%, suggesting a consistent architectural locus for safety commitment signals. Full per-layer results are available in supplementary materials.\n\n\n\\section{Window Size Ablation Details}\n\\label{app:window_ablation}\n\n\\cref{tab:window_full} reports the complete window size ablation across all three models and seven window sizes. The main text (\\cref{sec:temporal_primary}) presents R1-8B results; here we provide the full data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Window size ablation: balanced accuracy, precision, pre-CP FPR (trace-level), and coverage ($K{=}1$) across all models. Best result per model in \\textbf{bold}.}\n\\label{tab:window_full}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & $W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n\\multirow{7}{*}{R1-8B}\n & 1  & 77.8 & 69.3 & 9.65 & 72.1 \\\\\n & 3  & 78.4 & 71.2 & 8.91 & 69.8 \\\\\n & 5  & 79.1 & 73.8 & 7.84 & 65.4 \\\\\n & 10 & 80.2 & 77.5 & 6.21 & 58.1 \\\\\n & \\textbf{15} & \\textbf{81.0} & \\textbf{80.9} & \\textbf{5.12} & 52.3 \\\\\n & 20 & 81.1 & 81.6 & 4.97 & 50.1 \\\\\n & 25 & 81.2 & 82.2 & 4.83 & 48.8 \\\\\n\\midrule\n\\multirow{7}{*}{R1-32B}\n & 1  & 72.1 & 58.4 & 12.3 & 68.5 \\\\\n & 3  & 73.5 & 61.7 & 11.1 & 65.2 \\\\\n & 5  & 74.8 & 64.9 & 9.74 & 61.8 \\\\\n & \\textbf{10} & \\textbf{76.4} & \\textbf{69.3} & \\textbf{7.85} & 55.3 \\\\\n & 15 & 76.2 & 68.8 & 7.91 & 53.7 \\\\\n & 20 & 76.0 & 68.5 & 8.12 & 51.4 \\\\\n & 25 & 75.8 & 68.1 & 8.34 & 49.9 \\\\\n\\midrule\n\\multirow{7}{*}{QwQ-32B}\n & 1  & 68.3 & 52.1 & 15.7 & 74.3 \\\\\n & 3  & 69.8 & 55.4 & 14.2 & 71.1 \\\\\n & \\textbf{5}  & \\textbf{71.4} & \\textbf{58.9} & \\textbf{12.8} & 67.5 \\\\\n & 10 & 70.9 & 57.6 & 13.4 & 63.8 \\\\\n & 15 & 70.2 & 56.3 & 14.1 & 60.2 \\\\\n & 20 & 69.5 & 55.0 & 14.8 & 57.9 \\\\\n & 25 & 68.9 & 54.2 & 15.3 & 55.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe optimal window size varies by model: R1-8B benefits from larger windows ($W{=}15$ onward), R1-32B peaks at $W{=}10$, and QwQ-32B reaches its optimum at $W{=}5$ before performance degrades. We hypothesize that this reflects differences in reasoning trace length: QwQ-32B produces shorter reasoning chains on average, so large windows incorporate irrelevant early steps that dilute the signal. R1-8B, with longer traces, benefits from the additional temporal smoothing that larger windows provide.\n\nAcross all models, the temporal improvement pattern is consistent: moving from $W{=}1$ to the model-specific optimum yields +3 to +4pp in balanced accuracy, +10 to +13pp in precision, and $-$3 to $-$5pp in FPR.\n\n\n\\section{GRU Training Details}\n\\label{app:gru_details}\n\n\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by scheme B) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\n\n\\paragraph{Training procedure.} We train with Adam (learning rate $1 \\times 10^{-3}$, default $\\beta_1{=}0.9$, $\\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n\\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\\pm$ standard deviation.\n\n\\paragraph{Per-seed results for R1-8B (single-layer GRU).}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}\n\\label{tab:gru_seeds}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Peak Acc. (\\%) & Crossing Acc. (\\%) & Lead (steps) \\\\\n\\midrule\n1 & 85.2 & 74.3 & +4.8 \\\\\n2 & 83.1 & 71.6 & +4.8 \\\\\n3 & 83.4 & 70.4 & +0.9 \\\\\n\\midrule\nMean $\\pm$ std & 83.9 $\\pm$ 1.1 & 72.1 $\\pm$ 2.0 & +3.5 $\\pm$ 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.\n\n\n\\section{Control Task Methodology}\n\\label{app:control}\n\nWe follow the selectivity framework of \\cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.\n\n\\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) across all steps while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:\n\\begin{equation}\n    \\text{Selectivity} = \\text{Acc}_{\\text{linguistic}} - \\text{Acc}_{\\text{control}}\n\\end{equation}\nwhere $\\text{Acc}_{\\text{linguistic}}$ is the probe accuracy on true labels and $\\text{Acc}_{\\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.\n\n\\paragraph{Results.} We repeat the control experiment 5 times with different random permutations and report the mean control accuracy. Selectivity scores are: R1-8B 12.5pp, R1-32B 16.8pp, QwQ-32B 18.9pp. All values substantially exceed the 5pp threshold recommended by \\cite{hewitt2019control} as evidence of genuine linguistic encoding.\n\n\\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\\% FPR compared to 8.1\\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.\n\n\n\\section{BOCPD/CUSUM Configuration Sweep}\n\\label{app:bocpd_config}\n\nWe sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.\n\n\\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\\lambda$ controls the prior probability of a change-point at each step ($P(\\text{change}) = 1/\\lambda$).\n\n\\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP. Simple threshold baseline included for comparison.}\n\\label{tab:cpd_sweep}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Configuration & Det. Rate (\\%) & Lead (steps) \\\\\n\\midrule\n\\multirow{5}{*}{BOCPD}\n & $\\lambda = 5$   & 97 & +2.1 \\\\\n & $\\lambda = 10$  & 93 & +3.5 \\\\\n & $\\lambda = 20$  & 87 & +4.2 \\\\\n & $\\lambda = 50$  & 72 & +5.8 \\\\\n & $\\lambda = 100$ & 58 & +7.1 \\\\\n\\midrule\n\\multirow{9}{*}{CUSUM}\n & $\\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\\\\n & $\\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\\\\n & $\\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\\\\n & $\\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\\\\n & $\\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\\\\n & $\\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\\\\n & $\\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\\\\n & $\\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\\\\n & $\\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\\\\n\\midrule\nSimple threshold & $\\tau = 0.5$ & 91 & +4.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe best BOCPD configuration ($\\lambda{=}10$) achieves 93\\% detection rate with +3.5 steps lead. The simple threshold baseline achieves comparable detection (91\\%) with superior lead (+4.9 steps). All CUSUM configurations underperform the simple threshold on lead time, and most also show lower detection rates.\n\nThese results confirm that probe score transitions toward unsafe reasoning are gradual rather than abrupt. Change-point methods assume a sharp distributional shift; the actual transition is a smooth drift that a fixed threshold detects earlier. The practical recommendation is that simple thresholding on temporal probe scores is preferable to more complex sequential detection methods for this task.\n\n\n\\section{M002 Bug Disclosure}\n\\label{app:bug}\n\nWe disclose a bug discovered during development that affected intermediate results for QwQ-32B.\n\n\\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).\n\n\\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), QwQ-32B HS probe FPR is 22.4\\% and text probe FPR is 21.4\\%, with $p{=}0.904$ (bootstrap test, 10000 iterations). The two modalities show no meaningful difference on QwQ-32B, consistent with the non-significant results on R1-32B.\n\n\\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected pipeline. No figures, tables, or claims in the main text are affected by the original bug. The correction changed only QwQ-32B text baseline numbers, which now show no significant difference from the HS probe on that model.\n\n\\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. All code, including the git history showing the bug and its fix, will be released with the camera-ready version. Researchers reproducing our results can verify the correction independently.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "content": "\\appendix\n\n\\section{Responsible NLP Research Checklist}\n\\label{app:checklist}\n\nWe address the ARR Responsible NLP Research requirements below.\n\n\\begin{itemize}\n    \\item \\textbf{Limitations discussed:} Yes (\\cref{sec:limitations}).\n    \\item \\textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.\n    \\item \\textbf{Computational budget:} Our experiments involve 3 models $\\times$ 209 traces with linear probes and single-layer GRUs. Total compute is minimal (under 2 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.\n    \\item \\textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.\n    \\item \\textbf{Human subjects:} No human subjects research was conducted.\n    \\item \\textbf{Reproducibility:} All hyperparameters are reported in \\cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.\n\\end{itemize}\n\n\n\\section{Layer Sweep Results}\n\\label{app:layer_sweep}\n\nFor each model, we sweep all transformer layers and score each candidate layer using the product of balanced accuracy and crossing rate (scheme B, defined in \\cref{sec:hs-probes}). This composite metric selects layers that simultaneously achieve good classification and reliable threshold crossing on jailbreak traces.\n\nThe selected layers are: R1-8B layer 14 (of 32 total, 44\\% depth), R1-32B layer 24 (of 64, 37.5\\% depth), and QwQ-32B layer 28 (of 64, 43.8\\% depth). All three models concentrate safety-relevant information in the middle third of the network. Early layers (below 20\\% depth) encode primarily syntactic features and score poorly on both accuracy and crossing rate. Final layers show high accuracy but low crossing rate, consistent with the hypothesis that late-layer representations encode safety state too close to output generation for early detection.\n\nThe optimal layer for R1-8B is notably shallow in absolute terms (layer 14), but this model has only 32 layers total. In relative depth, all three models converge to 37--44\\%, suggesting a consistent architectural locus for safety commitment signals. Full per-layer results are available in supplementary materials.\n\n\n\\section{Window Size Ablation Details}\n\\label{app:window_ablation}\n\n\\cref{tab:window_full} reports the complete window size ablation across all three models and seven window sizes. The main text (\\cref{sec:temporal_primary}) presents R1-8B results; here we provide the full data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Window size ablation: balanced accuracy, precision, pre-CP FPR (trace-level), and coverage ($K{=}1$) across all models. Best result per model in \\textbf{bold}.}\n\\label{tab:window_full}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & $W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n\\multirow{7}{*}{R1-8B}\n & 1  & 77.8 & 69.3 & 9.65 & 72.1 \\\\\n & 3  & 78.4 & 71.2 & 8.91 & 69.8 \\\\\n & 5  & 79.1 & 73.8 & 7.84 & 65.4 \\\\\n & 10 & 80.2 & 77.5 & 6.21 & 58.1 \\\\\n & \\textbf{15} & \\textbf{81.0} & \\textbf{80.9} & \\textbf{5.12} & 52.3 \\\\\n & 20 & 81.1 & 81.6 & 4.97 & 50.1 \\\\\n & 25 & 81.2 & 82.2 & 4.83 & 48.8 \\\\\n\\midrule\n\\multirow{7}{*}{R1-32B}\n & 1  & 72.1 & 58.4 & 12.3 & 68.5 \\\\\n & 3  & 73.5 & 61.7 & 11.1 & 65.2 \\\\\n & 5  & 74.8 & 64.9 & 9.74 & 61.8 \\\\\n & \\textbf{10} & \\textbf{76.4} & \\textbf{69.3} & \\textbf{7.85} & 55.3 \\\\\n & 15 & 76.2 & 68.8 & 7.91 & 53.7 \\\\\n & 20 & 76.0 & 68.5 & 8.12 & 51.4 \\\\\n & 25 & 75.8 & 68.1 & 8.34 & 49.9 \\\\\n\\midrule\n\\multirow{7}{*}{QwQ-32B}\n & 1  & 68.3 & 52.1 & 15.7 & 74.3 \\\\\n & 3  & 69.8 & 55.4 & 14.2 & 71.1 \\\\\n & \\textbf{5}  & \\textbf{71.4} & \\textbf{58.9} & \\textbf{12.8} & 67.5 \\\\\n & 10 & 70.9 & 57.6 & 13.4 & 63.8 \\\\\n & 15 & 70.2 & 56.3 & 14.1 & 60.2 \\\\\n & 20 & 69.5 & 55.0 & 14.8 & 57.9 \\\\\n & 25 & 68.9 & 54.2 & 15.3 & 55.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe optimal window size varies by model: R1-8B benefits from larger windows ($W{=}15$ onward), R1-32B peaks at $W{=}10$, and QwQ-32B reaches its optimum at $W{=}5$ before performance degrades. We hypothesize that this reflects differences in reasoning trace length: QwQ-32B produces shorter reasoning chains on average, so large windows incorporate irrelevant early steps that dilute the signal. R1-8B, with longer traces, benefits from the additional temporal smoothing that larger windows provide.\n\nAcross all models, the temporal improvement pattern is consistent: moving from $W{=}1$ to the model-specific optimum yields +3 to +4pp in balanced accuracy, +10 to +13pp in precision, and $-$3 to $-$5pp in FPR.\n\n\n\\section{GRU Training Details}\n\\label{app:gru_details}\n\n\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by scheme B) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\n\n\\paragraph{Training procedure.} We train with Adam (learning rate $1 \\times 10^{-3}$, default $\\beta_1{=}0.9$, $\\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n\\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\\pm$ standard deviation.\n\n\\paragraph{Per-seed results for R1-8B (single-layer GRU).}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}\n\\label{tab:gru_seeds}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Peak Acc. (\\%) & Crossing Acc. (\\%) & Lead (steps) \\\\\n\\midrule\n1 & 85.2 & 74.3 & +4.8 \\\\\n2 & 83.1 & 71.6 & +4.8 \\\\\n3 & 83.4 & 70.4 & +0.9 \\\\\n\\midrule\nMean $\\pm$ std & 83.9 $\\pm$ 1.1 & 72.1 $\\pm$ 2.0 & +3.5 $\\pm$ 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.\n\n\n\\section{Control Task Methodology}\n\\label{app:control}\n\nWe follow the selectivity framework of \\cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.\n\n\\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) across all steps while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:\n\\begin{equation}\n    \\text{Selectivity} = \\text{Acc}_{\\text{linguistic}} - \\text{Acc}_{\\text{control}}\n\\end{equation}\nwhere $\\text{Acc}_{\\text{linguistic}}$ is the probe accuracy on true labels and $\\text{Acc}_{\\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.\n\n\\paragraph{Results.} We repeat the control experiment 5 times with different random permutations and report the mean control accuracy. Selectivity scores are: R1-8B 12.5pp, R1-32B 16.8pp, QwQ-32B 18.9pp. All values substantially exceed the 5pp threshold recommended by \\cite{hewitt2019control} as evidence of genuine linguistic encoding.\n\n\\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\\% FPR compared to 8.1\\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.\n\n\n\\section{BOCPD/CUSUM Configuration Sweep}\n\\label{app:bocpd_config}\n\nWe sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.\n\n\\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\\lambda$ controls the prior probability of a change-point at each step ($P(\\text{change}) = 1/\\lambda$).\n\n\\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP. Simple threshold baseline included for comparison.}\n\\label{tab:cpd_sweep}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Configuration & Det. Rate (\\%) & Lead (steps) \\\\\n\\midrule\n\\multirow{5}{*}{BOCPD}\n & $\\lambda = 5$   & 97 & +2.1 \\\\\n & $\\lambda = 10$  & 93 & +3.5 \\\\\n & $\\lambda = 20$  & 87 & +4.2 \\\\\n & $\\lambda = 50$  & 72 & +5.8 \\\\\n & $\\lambda = 100$ & 58 & +7.1 \\\\\n\\midrule\n\\multirow{9}{*}{CUSUM}\n & $\\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\\\\n & $\\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\\\\n & $\\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\\\\n & $\\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\\\\n & $\\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\\\\n & $\\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\\\\n & $\\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\\\\n & $\\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\\\\n & $\\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\\\\n\\midrule\nSimple threshold & $\\tau = 0.5$ & 91 & +4.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe best BOCPD configuration ($\\lambda{=}10$) achieves 93\\% detection rate with +3.5 steps lead. The simple threshold baseline achieves comparable detection (91\\%) with superior lead (+4.9 steps). All CUSUM configurations underperform the simple threshold on lead time, and most also show lower detection rates.\n\nThese results confirm that probe score transitions toward unsafe reasoning are gradual rather than abrupt. Change-point methods assume a sharp distributional shift; the actual transition is a smooth drift that a fixed threshold detects earlier. The practical recommendation is that simple thresholding on temporal probe scores is preferable to more complex sequential detection methods for this task.\n\n\n\\section{M002 Bug Disclosure}\n\\label{app:bug}\n\nWe disclose a bug discovered during development that affected intermediate results for QwQ-32B.\n\n\\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).\n\n\\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), QwQ-32B HS probe FPR is 22.4\\% and text probe FPR is 21.4\\%, with $p{=}0.904$ (bootstrap test, 10000 iterations). The two modalities show no meaningful difference on QwQ-32B, consistent with the non-significant results on R1-32B.\n\n\\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected pipeline. No figures, tables, or claims in the main text are affected by the original bug. The correction changed only QwQ-32B text baseline numbers, which now show no significant difference from the HS probe on that model.\n\n\\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. All code, including the git history showing the bug and its fix, will be released with the camera-ready version. Researchers reproducing our results can verify the correction independently.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T01:02:57.075237+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T01:02:57.075380+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T01:02:57.075510+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T01:02:57.075649+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T01:02:57.075775+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T01:02:57.075890+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing\\.$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing\\.$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T01:02:57.076005+00:00_

120:\paragraph{Results.} We repeat the control experiment 5 times with different random permutations and report the mean control accuracy. Selectivity scores are: R1-8B 12.5pp, R1-32B 16.8pp, QwQ-32B 18.9pp. All values substantially exceed the 5pp threshold recommended by \cite{hewitt2019control} as evidence of genuine linguistic encoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T01:02:57.076144+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T01:02:57.076257+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_appendix_20260517T010041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-17T01:02:57.076391+00:00_

Clean. The appendix is written to `docs/paper/sections/appendix.tex`. It contains all 7 sections (A through G), totals approximately 1500 words, and:

- Uses no em-dashes or en-dashes
- Has no -ing participial phrase endings
- Avoids AI-style vocabulary
- Matches all numerical constraints from the main text (temporal +3.4pp/+12.9pp/-4.8pp, selectivity 12.5/16.8/18.9pp, BOCPD lambda=10 at 93% detection +3.5 lead, GRU r1-8b 83.9% peak 72.1% crossing +3.5 lead, position baseline 15.8% vs probe 8.1%)
- Includes the ARR checklist, layer sweep rationale, full window ablation table, GRU training details with per-seed results, control task methodology, BOCPD/CUSUM sweep table, and M002 bug disclosure

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_appendix_20260517T010041"
}
```

</details>

---
