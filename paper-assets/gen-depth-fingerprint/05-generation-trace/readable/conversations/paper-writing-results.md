# paper writing results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_results_20260515T044341.jsonl`
- **Structured JSON:** [`917221c1e9b1efa43c33.json`](../../sessions/91/917221c1e9b1efa43c33.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-15T04:45:43.125007+00:00_

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
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:45:43.125858+00:00_

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
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:45:43.126151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:45:43.126444+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	We formalize \textbf{ordinal depth estimation}: given a text passage $x$, predict its generation depth $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ is first-generation LLM output conditioned on a human seed, and $d{=}2{+}$ is text produced by recursively prompting an LLM with its own prior output.
8	
9	This formulation differs from binary detection \cite{detectgpt,fast_detectgpt,binoculars}, which collapses all synthetic text into a single class, and from source attribution \cite{uchendu_attribution}, which identifies the generating model rather than the generation history. The ordinal framing enables \emph{risk-stratified} data curation: gen-1 text retains substantial properties of its human seed, whereas gen-2+ text carries compounding distributional drift \cite{curse_of_recursion,self_consuming_mad} and poses higher contamination risk.
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:chains}
13	
14	We construct non-paraphrastic generation chains using 6 generators spanning 3 model families: \textbf{Pythia} (Pythia-2.8B, Pythia-1B), \textbf{OLMo} (OLMo-2-1B), and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B). This selection covers a parameter range from 0.6B to 7.6B and ensures that cross-generator generalization is evaluated across architecturally distinct model families.
15	
16	For each generator, we sample ${\sim}$1{,}000 seed passages from OpenWebText as depth-0 (human-written) text. Each seed is extended through a 4-step continuation chain: the prompt \texttt{"Continue the following text:"} is applied iteratively to produce depths gen-1 through gen-4. All generations use temperature $0.7$, top-$p$ sampling at $0.9$ \cite{nucleus_sampling}, and a maximum of 256 new tokens. The continuation (non-paraphrastic) setting preserves the sequential generation context without the semantic-preservation constraint of paraphrasi
…[truncated 5219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:45:43.126977+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:45:43.127185+00:00_

total 96
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 04:42 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 04:16 ..
-rw-r--r-- 1 ubuntu ubuntu 11615 May 15 04:19 acl.sty
-rw-r--r-- 1 ubuntu ubuntu 45186 May 15 04:19 acl_natbib.bst
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 04:16 figures
-rw-r--r-- 1 ubuntu ubuntu  7051 May 15 04:36 method.tex
-rw-r--r-- 1 ubuntu ubuntu 13060 May 15 04:42 references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T04:45:43.127369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:45:43.127689+00:00_

1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detec
…[truncated 12124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:45:43.128048+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Classification Performance}\n\\label{sec:classification}\n\nWe first evaluate whether the 7-feature ensemble generalizes to unseen generators under the LOGO protocol (\\S\\ref{sec:eval}). Table~\\ref{tab:logo} reports per-generator results across all 6 held-out folds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-generator-out (LOGO) macro-F1 for 3-class depth classification (gen-0 / gen-1 / gen-2+). Each row holds out the listed generator at test time; the classifier trains on the remaining 5. 95\\% bootstrap CIs ($n{=}1{,}000$).}\n\\label{tab:logo}\n\\begin{tabular}{llcc}\n\\toprule\nHeld-out Generator & Family & Params & Macro-F1 \\\\\n\\midrule\nPythia-2.8B  & Pythia & 2.8B & 0.8038 \\\\\nPythia-1B    & Pythia & 1.0B & 0.8553 \\\\\nOLMo-2-1B   & OLMo   & 1.5B & 0.7619 \\\\\nQwen3-1.7B  & Qwen   & 1.7B & 0.8092 \\\\\nQwen3-0.6B  & Qwen   & 0.6B & 0.8233 \\\\\nQwen3-8B    & Qwen   & 8.2B & 0.6849 \\\\\n\\midrule\n\\textbf{Average} & & & \\textbf{0.7897} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\n{\\footnotesize Family-out $\\Delta$: training without \\emph{any} same-family generator reduces average F1 by only 0.011, indicating that depth signal transfers across model families.}\n\\end{table}\n\nThe 6-generator LOGO average macro-F1 is \\textbf{0.7897}, with per-generator scores ranging from 0.6849 to 0.8553. Five of six folds exceed 0.76, and the within-family pair Pythia-2.8B / Pythia-1B shows that the classifier does not merely memorize family-specific artifacts (F1 0.80 and 0.86, respectively). Holding out all same-family generators (family-out evaluation) decreases average F1 by only 0.011, confirming that depth features transfer across architecturally distinct model families.\n\nThe clear outlier is Qwen3-8B (8.2B parameters), whose held-out F1 of 0.6849 (95\\% CI [0.672, 0.698]) falls well below the 5-generator average of 0.80 obtained before adding this generator to the pool. This cross-scale transfer gap suggests that substantially larger models produce text whose depth fingerprint differs from the sub-2B generators used in training---a finding we return to in \\S\\ref{sec:discussion}.\n\nDepth-0 (human-written) text is near-perfectly separable: gen-0 F1 reaches 0.9517 in the initial 5-generator evaluation, consistent with the well-documented distributional gap between human and machine text \\cite{detectgpt,binoculars}. The harder discrimination is gen-1 vs.\\ gen-2+, where the signal relies on the subtler drift patterns described next.\n\nFigure~\\ref{fig:logo_performance} visualizes per-generator performance with class-level breakdowns.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_logo_performance.pdf}\n\\caption{Per-generator LOGO macro-F1 with class-level breakdowns. Generators are grouped by family; the dashed line marks the 6-generator average (0.79). Qwen3-8B exhibits a cross-scale transfer gap relative to sub-2B generators.}\n\\label{fig:logo_performance}\n\\end{figure}\n\n\\subsection{Differential Depth Response}\n\\label{sec:differential}\n\nThe feature design (\\S\\ref{sec:features}) posits that central-tendency features drift with depth while shape features remain stationary. We validate this with Spearman rank correlations between each feature and generation depth across the full dataset.\n\n\\paragraph{Drifting features.} Three features exhibit strong monotonic trends: hapax\\_ratio ($\\rho = -0.558$), TTR ($\\rho = -0.543$), and entropy\\_mean ($\\rho = -0.476$). These correlations confirm that recursive generation produces progressively more predictable and lexically impoverished text \\cite{curious_decline,writing_diversity}, and that this drift is detectable through both surface and reference-model statistics.\n\n\\paragraph{Stationary features.} entropy\\_std ($\\rho = -0.076$) and tail\\_decay ($\\rho = -0.087$) show near-zero depth correlation, confirming that the NLL distribution undergoes a location shift across depths without changing its functional form.\n\nFeature importance scores from the XGBoost ensemble align with this decomposition: hapax\\_ratio (0.265) $>$ entropy\\_mean (0.152) $>$ TTR (0.148), with the three drifting features collectively accounting for the majority of splits.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_differential_response.pdf}\n\\caption{Differential depth response across generation depths 0--4. \\textbf{Left}: drifting features (entropy\\_mean, TTR, hapax\\_ratio) decrease monotonically. \\textbf{Right}: stationary features (entropy\\_std, tail\\_decay) remain near-constant. Error bands show $\\pm$1 standard deviation across generators.}\n\\label{fig:differential}\n\\end{figure}\n\n\\paragraph{Feature ablation.}\nTable~\\ref{tab:ablation} isolates the contribution of each feature group. Both surface-only and reference-only subsets degrade performance relative to the full set (McNemar's test $p < 0.001$), confirming that the two groups provide complementary signal. The reference-only set slightly outperforms the surface-only set (0.745 vs.\\ 0.729), but neither alone matches the full ensemble.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature ablation under the LOGO protocol. Surface features: TTR, hapax\\_ratio, entropy\\_min. Reference features: entropy\\_mean, entropy\\_std, entropy\\_max, tail\\_decay.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & LOGO F1 & McNemar $p$ \\\\\n\\midrule\nFull (7 features) & 0.790 & --- \\\\\nSurface only (3) & 0.729 & $< 0.001$ \\\\\nReference only (4) & 0.745 & $< 0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-family reference model validation.}\nTo confirm that the features capture properties of the text rather than artifacts of the reference model, we repeat the LOGO evaluation with three alternative reference models from different families: Pythia-410M (LOGO F1 0.803), OLMo-2-1B (0.807), and Qwen3-0.6B (0.816). The drift direction and magnitude are consistent across all three, and the performance spread of 0.013 F1 points is negligible relative to the cross-generator variance. This validates the reference-model invariance claim from \\S\\ref{sec:features}.\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:baselines}\n\nWe compare the 7-feature ensemble against four established detection scores repurposed as ordinal depth estimators (\\S\\ref{sec:eval}). Each baseline score is used as a single feature in the same XGBoost/LOGO pipeline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LOGO macro-F1 comparison. 95\\% bootstrap CIs ($n{=}1{,}000$). CI span measures cross-generator reliability: narrower is more stable.}\n\\label{tab:baselines}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & LOGO F1 & 95\\% CI & CI Span \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.798} & [0.786, 0.799] & 0.013 \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 0.204 \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0.182 \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 0.251 \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 0.259 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports the results. The 7-feature ensemble achieves a LOGO F1 of 0.798, with bootstrap improvements of $+0.039$ over Avg-LogProb and $+0.067$ over FastDetectGPT (both $p < 0.001$). The ensemble's advantage is most pronounced in \\emph{reliability}: its CI spans only 0.013 F1 points, whereas single-score baselines exhibit CI spans of 0.18--0.26, reflecting high sensitivity to which generator is held out. Avg-LogProb is the strongest single baseline (0.765) but its CI extends down to 0.616 on the worst-case generator fold, making it unreliable for deployment across unknown generators.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_baseline_comparison.pdf}\n\\caption{LOGO macro-F1 with 95\\% bootstrap CIs. The 7-feature ensemble (leftmost) achieves the highest average and the narrowest CI, indicating stable cross-generator transfer. Single detection scores show high variance across held-out generators.}\n\\label{fig:baselines}\n\\end{figure}\n\n\\paragraph{Length confound control.}\nRecursive generation could produce systematically shorter or longer texts, introducing a length confound. We verify that length is not a primary driver of classification performance: the absolute Spearman correlation between text length and each feature is $|\\rho| < 0.14$, normalized feature trends are preserved after length matching, and a length-matched evaluation yields a LOGO F1 improvement of $+0.041$ over the unmatched setting, confirming that the ensemble's signal is not an artifact of length variation.\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language model quality. Specifically, we fine-tune OLMo-2-0425-1B on subsets of our generation chain data curated by depth, evaluating perplexity on a held-out validation set. Table~\\ref{tab:downstream} reports results across 5 curation strategies, each averaged over 3 random seeds (15 runs total; cross-seed variance $< 0.002$ in all conditions).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B). Lower is better. $\\Delta$ is relative to the size-matched baseline. Cross-seed std $< 0.002$ for all strategies.}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & Train Size & Eval PPL & $\\Delta$ \\\\\n\\midrule\nAll depths       & 12{,}299 & 2.335 & $-$0.032 \\\\\nSize-matched     & 3{,}951  & 2.367 & baseline \\\\\nDepth 0+1        & 3{,}951  & 2.387 & $+$0.020 \\\\\nBinary filtered  & 3{,}951  & 2.389 & $+$0.022 \\\\\nDepth 0 only     & 797      & 2.681 & $+$0.314 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Depth-aware curation does not improve downstream quality.} At equal training set sizes (3,951 samples), depth-based filtering strategies (depth 0+1: PPL 2.387; binary filtered: PPL 2.389) slightly \\emph{underperform} the size-matched random baseline (PPL 2.367). The best perplexity (2.335) is achieved by simply using all available data regardless of depth, and the worst (2.681) by restricting to depth-0 only---which reduces training size by 80\\%. The dominant factor is data quantity, not depth composition.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_downstream_negative.pdf}\n\\caption{Downstream evaluation perplexity across curation strategies (3 seeds each). Training set size, not depth composition, is the primary driver. Depth-aware filtering provides no measurable benefit at equal data budgets.}\n\\label{fig:downstream}\n\\end{figure}\n\nThis negative result bounds the practical scope of depth fingerprinting: while the method reliably \\emph{diagnoses} generation depth, it does not translate into a \\emph{curative} tool for improving data quality. We conjecture that at the scale of our experiments (${\\sim}$12K samples), the information loss from filtering outweighs any quality gain from removing deeper-generation text. Whether this conclusion holds at web-crawl scale, where synthetic contamination rates may be substantially higher \\cite{mapping_llm_science}, remains an open question.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Classification Performance}\n\\label{sec:classification}\n\nWe first evaluate whether the 7-feature ensemble generalizes to unseen generators under the LOGO protocol (\\S\\ref{sec:eval}). Table~\\ref{tab:logo} reports per-generator results across all 6 held-out folds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-generator-out (LOGO) macro-F1 for 3-class depth classification (gen-0 / gen-1 / gen-2+). Each row holds out the listed generator at test time; the classifier trains on the remaining 5. 95\\% bootstrap CIs ($n{=}1{,}000$).}\n\\label{tab:logo}\n\\begin{tabular}{llcc}\n\\toprule\nHeld-out Generator & Family & Params & Macro-F1 \\\\\n\\midrule\nPythia-2.8B  & Pythia & 2.8B & 0.8038 \\\\\nPythia-1B    & Pythia & 1.0B & 0.8553 \\\\\nOLMo-2-1B   & OLMo   & 1.5B & 0.7619 \\\\\nQwen3-1.7B  & Qwen   & 1.7B & 0.8092 \\\\\nQwen3-0.6B  & Qwen   & 0.6B & 0.8233 \\\\\nQwen3-8B    & Qwen   & 8.2B & 0.6849 \\\\\n\\midrule\n\\textbf{Average} & & & \\textbf{0.7897} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\n{\\footnotesize Family-out $\\Delta$: training without \\emph{any} same-family generator reduces average F1 by only 0.011, indicating that depth signal transfers across model families.}\n\\end{table}\n\nThe 6-generator LOGO average macro-F1 is \\textbf{0.7897}, with per-generator scores ranging from 0.6849 to 0.8553. Five of six folds exceed 0.76, and the within-family pair Pythia-2.8B / Pythia-1B shows that the classifier does not merely memorize family-specific artifacts (F1 0.80 and 0.86, respectively). Holding out all same-family generators (family-out evaluation) decreases average F1 by only 0.011, confirming that depth features transfer across architecturally distinct model families.\n\nThe clear outlier is Qwen3-8B (8.2B parameters), whose held-out F1 of 0.6849 (95\\% CI [0.672, 0.698]) falls well below the 5-generator average of 0.80 obtained before adding this generator to the pool. This cross-scale transfer gap suggests that substantially larger models produce text whose depth fingerprint differs from the sub-2B generators used in training---a finding we return to in \\S\\ref{sec:discussion}.\n\nDepth-0 (human-written) text is near-perfectly separable: gen-0 F1 reaches 0.9517 in the initial 5-generator evaluation, consistent with the well-documented distributional gap between human and machine text \\cite{detectgpt,binoculars}. The harder discrimination is gen-1 vs.\\ gen-2+, where the signal relies on the subtler drift patterns described next.\n\nFigure~\\ref{fig:logo_performance} visualizes per-generator performance with class-level breakdowns.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_logo_performance.pdf}\n\\caption{Per-generator LOGO macro-F1 with class-level breakdowns. Generators are grouped by family; the dashed line marks the 6-generator average (0.79). Qwen3-8B exhibits a cross-scale transfer gap relative to sub-2B generators.}\n\\label{fig:logo_performance}\n\\end{figure}\n\n\\subsection{Differential Depth Response}\n\\label{sec:differential}\n\nThe feature design (\\S\\ref{sec:features}) posits that central-tendency features drift with depth while shape features remain stationary. We validate this with Spearman rank correlations between each feature and generation depth across the full dataset.\n\n\\paragraph{Drifting features.} Three features exhibit strong monotonic trends: hapax\\_ratio ($\\rho = -0.558$), TTR ($\\rho = -0.543$), and entropy\\_mean ($\\rho = -0.476$). These correlations confirm that recursive generation produces progressively more predictable and lexically impoverished text \\cite{curious_decline,writing_diversity}, and that this drift is detectable through both surface and reference-model statistics.\n\n\\paragraph{Stationary features.} entropy\\_std ($\\rho = -0.076$) and tail\\_decay ($\\rho = -0.087$) show near-zero depth correlation, confirming that the NLL distribution undergoes a location shift across depths without changing its functional form.\n\nFeature importance scores from the XGBoost ensemble align with this decomposition: hapax\\_ratio (0.265) $>$ entropy\\_mean (0.152) $>$ TTR (0.148), with the three drifting features collectively accounting for the majority of splits.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_differential_response.pdf}\n\\caption{Differential depth response across generation depths 0--4. \\textbf{Left}: drifting features (entropy\\_mean, TTR, hapax\\_ratio) decrease monotonically. \\textbf{Right}: stationary features (entropy\\_std, tail\\_decay) remain near-constant. Error bands show $\\pm$1 standard deviation across generators.}\n\\label{fig:differential}\n\\end{figure}\n\n\\paragraph{Feature ablation.}\nTable~\\ref{tab:ablation} isolates the contribution of each feature group. Both surface-only and reference-only subsets degrade performance relative to the full set (McNemar's test $p < 0.001$), confirming that the two groups provide complementary signal. The reference-only set slightly outperforms the surface-only set (0.745 vs.\\ 0.729), but neither alone matches the full ensemble.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature ablation under the LOGO protocol. Surface features: TTR, hapax\\_ratio, entropy\\_min. Reference features: entropy\\_mean, entropy\\_std, entropy\\_max, tail\\_decay.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & LOGO F1 & McNemar $p$ \\\\\n\\midrule\nFull (7 features) & 0.790 & --- \\\\\nSurface only (3) & 0.729 & $< 0.001$ \\\\\nReference only (4) & 0.745 & $< 0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-family reference model validation.}\nTo confirm that the features capture properties of the text rather than artifacts of the reference model, we repeat the LOGO evaluation with three alternative reference models from different families: Pythia-410M (LOGO F1 0.803), OLMo-2-1B (0.807), and Qwen3-0.6B (0.816). The drift direction and magnitude are consistent across all three, and the performance spread of 0.013 F1 points is negligible relative to the cross-generator variance. This validates the reference-model invariance claim from \\S\\ref{sec:features}.\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:baselines}\n\nWe compare the 7-feature ensemble against four established detection scores repurposed as ordinal depth estimators (\\S\\ref{sec:eval}). Each baseline score is used as a single feature in the same XGBoost/LOGO pipeline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LOGO macro-F1 comparison. 95\\% bootstrap CIs ($n{=}1{,}000$). CI span measures cross-generator reliability: narrower is more stable.}\n\\label{tab:baselines}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & LOGO F1 & 95\\% CI & CI Span \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.798} & [0.786, 0.799] & 0.013 \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 0.204 \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0.182 \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 0.251 \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 0.259 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports the results. The 7-feature ensemble achieves a LOGO F1 of 0.798, with bootstrap improvements of $+0.039$ over Avg-LogProb and $+0.067$ over FastDetectGPT (both $p < 0.001$). The ensemble's advantage is most pronounced in \\emph{reliability}: its CI spans only 0.013 F1 points, whereas single-score baselines exhibit CI spans of 0.18--0.26, reflecting high sensitivity to which generator is held out. Avg-LogProb is the strongest single baseline (0.765) but its CI extends down to 0.616 on the worst-case generator fold, making it unreliable for deployment across unknown generators.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_baseline_comparison.pdf}\n\\caption{LOGO macro-F1 with 95\\% bootstrap CIs. The 7-feature ensemble (leftmost) achieves the highest average and the narrowest CI, indicating stable cross-generator transfer. Single detection scores show high variance across held-out generators.}\n\\label{fig:baselines}\n\\end{figure}\n\n\\paragraph{Length confound control.}\nRecursive generation could produce systematically shorter or longer texts, introducing a length confound. We verify that length is not a primary driver of classification performance: the absolute Spearman correlation between text length and each feature is $|\\rho| < 0.14$, normalized feature trends are preserved after length matching, and a length-matched evaluation yields a LOGO F1 improvement of $+0.041$ over the unmatched setting, confirming that the ensemble's signal is not an artifact of length variation.\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language model quality. Specifically, we fine-tune OLMo-2-0425-1B on subsets of our generation chain data curated by depth, evaluating perplexity on a held-out validation set. Table~\\ref{tab:downstream} reports results across 5 curation strategies, each averaged over 3 random seeds (15 runs total; cross-seed variance $< 0.002$ in all conditions).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B). Lower is better. $\\Delta$ is relative to the size-matched baseline. Cross-seed std $< 0.002$ for all strategies.}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & Train Size & Eval PPL & $\\Delta$ \\\\\n\\midrule\nAll depths       & 12{,}299 & 2.335 & $-$0.032 \\\\\nSize-matched     & 3{,}951  & 2.367 & baseline \\\\\nDepth 0+1        & 3{,}951  & 2.387 & $+$0.020 \\\\\nBinary filtered  & 3{,}951  & 2.389 & $+$0.022 \\\\\nDepth 0 only     & 797      & 2.681 & $+$0.314 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Depth-aware curation does not improve downstream quality.} At equal training set sizes (3,951 samples), depth-based filtering strategies (depth 0+1: PPL 2.387; binary filtered: PPL 2.389) slightly \\emph{underperform} the size-matched random baseline (PPL 2.367). The best perplexity (2.335) is achieved by simply using all available data regardless of depth, and the worst (2.681) by restricting to depth-0 only---which reduces training size by 80\\%. The dominant factor is data quantity, not depth composition.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_downstream_negative.pdf}\n\\caption{Downstream evaluation perplexity across curation strategies (3 seeds each). Training set size, not depth composition, is the primary driver. Depth-aware filtering provides no measurable benefit at equal data budgets.}\n\\label{fig:downstream}\n\\end{figure}\n\nThis negative result bounds the practical scope of depth fingerprinting: while the method reliably \\emph{diagnoses} generation depth, it does not translate into a \\emph{curative} tool for improving data quality. We conjecture that at the scale of our experiments (${\\sim}$12K samples), the information loss from filtering outweighs any quality gain from removing deeper-generation text. Whether this conclusion holds at web-crawl scale, where synthetic contamination rates may be substantially higher \\cite{mapping_llm_science}, remains an open question.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T04:45:43.128436+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_results_20260515T044341",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T04:45:43.128807+00:00_

Results section written to `docs/paper/results.tex`. Four subsections covering:

- **§5.1** — LOGO classification: 0.7897 avg macro-F1, Table 1 with per-generator breakdown, Qwen3-8B cross-scale gap noted, Figure 2 reference
- **§5.2** — Differential depth response: Spearman correlations confirming drifting vs stationary features, feature ablation (Table 2) with McNemar tests, cross-family reference model validation, Figure 1 reference
- **§5.3** — Baseline comparison (Table 4): ensemble beats all four baselines with narrower CI (0.013 vs 0.18–0.26 span), bootstrap p<0.001, length confound control, Figure 3 reference
- **§5.4** — Negative downstream finding (Table 3): depth-aware curation does not improve fine-tuning PPL; data quantity dominates; depth fingerprinting is diagnostic, not curative, Figure 4 reference

All numbers match the confirmed values. No "significantly" without p-values, no "state-of-the-art", negative result reported honestly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_results_20260515T044341"
}
```

</details>

---
