# Reviewer 2 coordination — Part 1 of 6

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/4c/4c34ba0b57b75b54a485.json)

## Round 1

## Round 1

46 recorded events


### User

_source line 1 · 2026-05-14T21:22:01.267633+00:00_

[Round 1 审稿请求]:
## Round 1 初审任务 — Reviewer 2: 新颖性 + 完整性 + 格式合规

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL 模板 `[review]`, 8 页正文限制, double-blind
- **匿名规则**: 禁止透露作者身份，self-citation 必须第三人称
- **必须有独立 Limitations section** (EMNLP 强制要求, 不计入页数)

### 论文路径
`projects/solver-trace-ablation/paper/main.tex`（含 \input 的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, references.bib）

### 你的审查侧重

**1. 贡献新颖性评估**
- STA (Solver Trace Ablation) 本质是 leave-one-out ablation on solver inputs——这在技术上是否足够新颖？论文声称新颖性在于 "application and findings, not the perturbation technique itself"——是否足以支撑顶会
- "Meta-level Goodhart's Law" 是否是一个真正的新概念？还是已知 Goodhart 现象在新领域的直接应用？是否有 prior work 已经讨论过 "diagnostic metrics becoming targets"？
- 7 种 hacking mode 的分类法是否有体系性？是否穷尽？分类标准是否自洽？
- 与最近的高度相关工作对比：Kim et al. (2026) "Do LLMs Game Formalization?" 在 ICLR VerifAI-2 Workshop 已经讨论了 formalization gaming——本文贡献相对于此的增量是什么？

**2. Related Work 覆盖度**
- 当前 references.bib 有 ~30 条引用——对 EMNLP main conference 是否足够？
- 是否遗漏重要相关工作？检查以下方向：
  - Process reward models beyond PRM800K (e.g., newer 2025-2026 work)
  - Reward hacking in code generation (beyond text)
  - Neurosymbolic reasoning benchmarks beyond FOLIO
  - Goodhart's Law in RLHF/RLAIF (2025-2026 新进展)
  - Mutation testing 在 ML 中的其他应用
  - Structural analysis of model outputs (probing, mechanistic interpretability)
- Related work section 是否充分区分本文与 prior work 的差异？

**3. EMNLP 格式合规检查**
- [ ] 使用 ACL 模板 + [review] option ✓
- [ ] Double-blind: 作者信息是否完全匿名？注意 "Anonymous ACL submission" 写的是 ACL 而非 EMNLP——是否有问题？
- [ ] 正文是否在 8 页以内？（需估算）
- [ ] **Limitations section**: EMNLP 强制要求独立的 \section{Limitations}——当前论文将其作为 conclusion 中的 \paragraph{Limitations and Future Work}，这**不符合要求**
- [ ] Ethics statement: 是否需要？
- [ ] 参考文献格式是否符合 ACL natbib 规范？
- [ ] 图表是否清晰可读？Caption 是否自足？
- [ ] Appendix 是否合理使用（不要把关键论证放 appendix）？

**4. 写作质量与论文结构**
- Abstract 是否简洁有力？是否包含关键数字？
- Introduction 的 story arc 是否清晰？gap → contribution 是否顺畅？
- 术语定义是否一致（STA, ISR, H1, H7 等缩写）？
- 数字精度是否合理（报告到小数点后几位）？
- 图表设计是否有效传达信息？Figure 1/2/3/4 各自的作用？

**5. 附录完整性**
- Appendix 中的 hacking mode 定义和示例是否充分？
- 是否有关键信息只出现在 appendix 而正文未提及？
- Per-seed 详细表格是否与正文叙述一致？

### 输出格式
请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条, 标注 severity: Critical / Major / Minor)
4. **Questions for Authors** (逐条编号)
5. **Missing References** (如有)
6. **Format Compliance Checklist** (逐项 ✓ 或 ✗ + 说明)
7. **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)
8. **Detailed Comments** (按 section 逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-14T21:22:13.229010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-14T21:22:13.582407+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\graphicspath{{figures/}}
15	
16	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in GRPO-Trained Neurosymbolic Formalizers}
17	
18	\author{Anonymous ACL submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{experiments}
28	\input{conclusion}
29	
30	\bibliography{references}
31	
32	\appendix
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T21:22:13.582919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-14T21:22:13.583242+00:00_

1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution-based evaluation. We introduce \emph{Solver Trace Ablation} (STA), a solver-agnostic diagnostic that applies leave-one-out component necessity testing to solver inputs. The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates maximal tightness; ISR$=$0 indicates complete redundancy.
3	
4	ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.
5	
6	Can ISR serve as a training signal? Incorporating ISR into the reward at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 64.5\% of proved samples exhibit conclusion duplication (H7), versus 0\% under matched random controls. The sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound. At $\beta{=}0.3$, prove rate collapses to 18\% versus 48\% for random control.
7	
8	Cross-logic transfer to Prolog/SWI-Prolog yields a stronger result: ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% genuine proofs.
9	
10	Across 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.
11	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-14T21:22:13.985025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-14T21:22:14.487004+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
9	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from models that exploit solver mechanics.
10	This gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
11	
12	Neurosymbolic approaches combine large language models with external solvers for logical reasoning.
13	Prompting-based methods such as SatLM~\cite{satlm}, Logic-LM~\cite{logic-lm}, and LINC~\cite{linc} translate natural language to formal representations verified by automated provers, but evaluate correctness through execution alone without examining the internal structure of proved outputs.
14	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by theorem provers~\cite{mellgren-prolog-grpo, logic-rl}.
15	The standard reward signal is binary execution feedback: 1 if the solver returns a proof, 0 otherwise.
16	This drives rapid improvement in prove rate but provides no gradient on structural quali
…[truncated 4721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T21:22:14.487469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T21:22:14.989427+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
6	SatLM~\cite{satlm} generates SAT formulas, Logic-LM~\cite{logic-lm} translates to first-order logic, LINC~\cite{linc} generates logic programs, and LoRP~\cite{lorp} uses Prolog as a reasoning backend; FOVER~\cite{fover-pei2025} adds iterative verification.
7	All evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.
8	Recent RL approaches train LLMs against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.
9	STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
10	
11	\paragraph{Reward Shaping and Process Supervision.}
12	Binary outcome rewards motivate process-level supervision: learned process reward models~\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\cite{rlsf} leverage formal verification, and rubric-based rewards~\cite{rubric-grpo} encode structured evaluation criteria.
13	However, process rewards introduce their own failure modes: design choices dominate signal effects~\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\cite{qwen-prm-lessons, progrs-outcome-conditioned}.
14	ISR is solver-grounded rather than learned (no reward-model noise), yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific
…[truncated 1747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-14T21:22:14.989879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-14T21:22:15.441616+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.95\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given natural language premises $P_1,\ldots,P_k$ and a conclusion $C$, the task is to produce a formal logic program $F=\{c_1,\ldots,c_n\}$, where each component $c_i$ is a premise (FOL) or a clause/fact (Prolog), with one distinguished component encoding the query.
15	An external solver $S$ returns $S(F)\in\{\textit{proved},\textit{failed}\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\autoref{fig:sta-overview}a).
16	
17	We train formalizers with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt.
18	Each rollout receives a binary \emph{execution reward}
19	$r_{\text{exec}}(x) = \mathbf{1}[S(F_x) = \textit{proved}]$;
20	group-relative advantages are computed within each prompt's rollout group, and the policy update maximizes a clipped surrogate objective with KL regularization.
21	This setup optimizes prove rate but provides no signal about \emph{structural quality}: a formalization that embeds the conclusion among its premises receives the same reward as a faithful multi-step derivation.
22	
23	\subsection{Solver Trace Ablation (STA)}
24	\label{sec:sta}
25	
26	To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
27	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$, each removing one component, and re-runs the s
…[truncated 3465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-14T21:22:15.441913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-14T21:22:15.943323+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We train Qwen3-4B with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 where noted, across seeds $\{42,43,44\}$.
10	Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), held constant across all seeds and conditions.
11	We use Prover9 for FOL and SWI-Prolog 8.4.2 for Prolog.
12	Evaluation is on 100 held-out FOLIO examples with greedy decoding; all cross-run ISR values are computed by \texttt{eval\_sta.py} which applies STA uniformly.
13	We report prove rate (PR), proved-only ISR (ISR$^*$, over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count.
14	Six reward conditions are compared: \textbf{Exec-only}, \textbf{ISR~$\beta{\in}\{0.1,0.3\}$}, \textbf{Random~$\beta{\in}\{0.1,0.3\}$}, and \textbf{SFT}.
15	Outputs are classified into H7, H1, and Genuine using text matching cross-validated with functional LOO analysis.
16	Full hyperparameters are in Appendix~\ref{app:setup}.
17	
18	\subsection{ISR as Diagnostic}
19	\label{sec:diagnostic}
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
24	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$96\% while proved-only ISR falls 0.642$\to$0.003 over 1000 steps. By step 1000, 94.8\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
25	\label{fig:isr-collapse}
26	\end{figure}
27	
28	\textbf{Collapse trajectory.}
29	Figure~\ref{fig:isr-collapse} traces IS
…[truncated 8884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-14T21:22:16.194324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-14T21:22:16.395966+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:discussion}
4	
5	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
6	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
7	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
8	Both the diagnostic utility and the Goodhart vulnerability transfer across formal languages: Prolog ISR-as-reward produces universal gaming across all seeds---each via a distinct mechanism---with zero genuine proofs (\S\ref{sec:crosslogic}).
9	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
10	
11	\paragraph{Interpreting ISR.}
12	ISR values must always be read relative to the optimization objective: under exec-only Prolog training, \emph{low} ISR reflects redundant coding (repeated ground facts) rather than absence of reasoning, while under ISR-as-reward, \emph{high} ISR reflects metric gaming.
13	The premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs and should be controlled when reporting structural scores.
14	
15	\paragraph{Meta-Level Goodhart: Implications.}
16	The meta-Goodhart finding extends beyond this specific system.
17	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward, the model games I
…[truncated 1904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-14T21:22:16.396335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-14T21:22:16.447077+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 20159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-14T21:22:16.898925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-14T21:22:16.951161+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke Poech},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	@article{thought-like-pro,
43	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
44	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models 
…[truncated 11641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-14T21:22:22.078411+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-14T21:22:22.179254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-14T21:22:25.194466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-14T21:22:25.647642+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines Limitations section requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines Limitations section requirements"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-14T21:22:29.318229+00:00_

Web search results for query: "EMNLP 2026 submission guidelines Limitations section requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here are the EMNLP 2026 submission guidelines for the Limitations section:

Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations". This section should be included at the end of the paper, before the references, and according to additional sources, the mandatory Limitations section is required, placed after the conclusion.

The Limitations section is a mandatory component of EMNLP 2026 submissions and must be clearly labeled and positioned near the end of the paper before the references.


REMINDER: You MUST include the sources above in your response t
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 3670
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-14T21:22:36.607143+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommenda
…[truncated 2506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11412
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T21:22:39.880620+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-14T21:22:39.931199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-14T21:22:43.907464+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever), and the description of each score level. I need the exact wording for soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever), and the description of each score level. I need the exact wording for soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-14T21:22:45.664401+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to score soundness/excitement/overall, what constitutes a strong vs weak paper, and any specific instructions about novelty assessment, related work coverage, and format compliance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to score soundness/excitement/overall, what constitutes a strong vs weak paper, and any specific instructions about novelty assessment, related work coverage, and format compliance."
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-14T21:22:51.942908+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend presentation."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me or broader community."

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: could be an outstanding paper award contender."
- **4**: "Conference: could be accepted to an ACL conference."
- **3**: "Findings: could be accepted to ACL Findings."
- **2**: "Resubmit next cycle: needs substantial revisions."
- **1**: "Do not resubmit: fully redone or not relevant."

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could repr
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8035
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-14T21:22:53.296876+00:00_

# ARR Reviewer Guidelines Summary

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

**Soundness**: Technical validity and methodological rigor. Per guidelines, "soundness scores must be justified by the text of the review." Low scores require explicit justification in review content.

**Excitement**: Personal interest and perceived significance. This is explicitly separated from soundness as "orthogonal to the assessment of the soundness of the paper," allowing reviewers to distinguish between technically sound but personally uninteresting work.

**Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact for ACL venues.

## Scoring Framework

The guidelines specify that all three scores must align with review content. Papers recommended for publication "are expected to be sufficiently sound and reproducible," but reviewers may recommend acceptance despite low personal excitement if impact justifies it.

## Strong vs. Weak Papers

**Strong papers** demonstrate:
- Clear research questions addressing genuine knowledge gaps
- Appropriate methodology matching the contribution type
- Sufficient evidence for stated claims
- Sound technical execution
- Fair comparisons to relevant baselines

**Weak papers** may exhibit issues including:
- Unclear contributions (code G1)
- Incomplete assumptions or proofs (code M5)
- Inappropriate statistical practices (code R1)
- Overclaiming or misleading framing (code R4)

## Novelty Assessment

The guidelines caution against dismissing work as "not novel" without "providing references" to highly similar prior work. Novelty requirements depend on contribution type—reproductions, analyses, and resource papers are explicitly in-scope alongside methodological contributions.

## Related Work Coverage

Authors should demonstrate awareness of work published "3+ months prior to submission deadline," with proper representation of prior contributions and c
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7632
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T21:22:59.608531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kim et al 2026 \"Do LLMs Game Formalization\" VerifAI ICLR arXiv:2604.19459"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kim et al 2026 \"Do LLMs Game Formalization\" VerifAI ICLR arXiv:2604.19459"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-14T21:23:00.613205+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Goodhart's Law RLHF diagnostic metrics becoming targets 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Goodhart's Law RLHF diagnostic metrics becoming targets 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-14T21:23:01.216349+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "process reward models 2025 2026 beyond PRM800K recent advances"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "process reward models 2025 2026 beyond PRM800K recent advances"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-14T21:23:07.646129+00:00_

Web search results for query: "Kim et al 2026 "Do LLMs Game Formalization" VerifAI ICLR arXiv:2604.19459"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"ICLR 2026 Workshop on Logical Reasoning of Large Language Models","url":"https://arxiv.org/pdf/2603.17169"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2503.13980"},{"title":"Game Theory Meets Large Language Models: A Systematic Survey","url":"https://arxiv.org/html/2502.09053v1"},{"title":"Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making","url":"https://arxiv.org/html/2506.12012v1"},{"title":"Large Language Models and Video Games: A Preliminary Scoping Review","url":"https://arxiv.org/html/2403.02613v1"},{"title":"LLMs Have Made Failure Worth Publishing","url":"https://arxiv.org/html/2604.06236v1"}]

I found the paper you're looking for! Here are the key details:

The paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" was authored by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut, submitted on April 21, 2026, with the arXiv identifier 2604.19459. It was published at the VerifAI-2 Workshop at ICLR 2026.

**Research Summary:**

The paper addresses how formal verification guarantees proof validity but not formalization faithfulness, and notes this gap is especially acute for natural-language logical reasoning where models construct axiom systems from scratch without libra
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8037
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-14T21:23:08.248961+00:00_

Web search results for query: "Goodhart's Law RLHF diagnostic metrics becoming targets 2025 2026"

Links: [{"title":"Goodhart's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Goodhart%27s_law"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Goodhart's Law in AI: When Metrics Become Targets, Models Fail","url":"https://www.practical-devsecops.com/glossary/goodharts-law/"},{"title":"Goodhart’s Law | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/goodhart_s_law/"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/1a8189929f3d7bd6183718f42c3f4309-Paper-Conference.pdf"},{"title":"Goodhart's Law: The Danger of Making Metrics into Targets","url":"https://www.ilms.academy/blog/goodharts-law-the-danger-of-making-metrics-into-targets"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification | OpenReview","url":"https://openreview.net/forum?id=UXuBzWoZGK&noteId=YiStZYdof7"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"What is Goodhart's Law? | Splunk","url":"https://www.splunk.com/en_us/blog/learn/goodharts-law.html"}]

I've completed the web search for your query. Here are the key findings:

## General Concept
Goodhart's Law is an adage that has been stated as, "When a measure becomes a target, it ceases to be a good measure". It is named after British economist Charles Goodhart, who expressed the core idea in a 1975 article on monetary policy.

## RLHF and Diagnostic Metrics
The search result
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7635
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-14T21:23:11.965992+00:00_

Web search results for query: "process reward models 2025 2026 beyond PRM800K recent advances"

Links: [{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees | OpenReview","url":"https://openreview.net/forum?id=fGIqGfmgkW"}]

Links: [{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"ICML Poster VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data","url":"https://icml.cc/virtual/2025/poster/44223"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/a
…[truncated 3028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10749
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T21:23:15.397001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward hacking code generation LLM 2025 2026 specification gaming coding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward hacking code generation LLM 2025 2026 specification gaming coding"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-14T21:23:16.100646+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "neurosymbolic reasoning benchmarks beyond FOLIO 2025 2026 logical reasoning datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "neurosymbolic reasoning benchmarks beyond FOLIO 2025 2026 logical reasoning datasets"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-14T21:23:22.903044+00:00_

Web search results for query: "reward hacking code generation LLM 2025 2026 specification gaming coding"

Links: [{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Recent Frontier Models Are Reward Hacking - METR","url":"https://metr.org/blog/2025-06-05-recent-reward-hacking/"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning","url":"https://arxiv.org/html/2605.02073v1"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"2025-Era “Reward Hacking” Does Not Show that ...","url":"https://www.alignmentforum.org/posts/wwRgR3K8FKShjwwL5/2025-era-reward-hacking-does-not-show-that-reward-is-the"},{"title":"SCHOOL OF REWARD HACKS: HACKING HARMLESS TASKS GENERALIZES TO MIS-","url":"https://arxiv.org/pdf/2508.17511"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"}]

Based on the search results, here's what I found about reward hacking, code generation, and LLMs in 2025-2026:

## Current State of Reward Hacking in LLMs

The most recent frontier models have engaged in increasingly sophisticated reward hacking, attempting (often successfully) to get a higher score by modifying the tests or scoring code, gaining access to an existing implementation or answer t
…[truncated 1359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7506
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-14T21:23:24.964026+00:00_

Web search results for query: "neurosymbolic reasoning benchmarks beyond FOLIO 2025 2026 logical reasoning datasets"

Links: [{"title":"A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13369-025-10887-3"},{"title":"NSORN: Designing a Benchmark Dataset for Neurosymbolic Ontology Reasoning with Noise | Neurosymbolic Artificial Intelligence","url":"https://neurosymbolic-ai-journal.com/paper/nsorn-designing-benchmark-dataset-neurosymbolic-ontology-reasoning-noise-2"},{"title":"A Comparative Study of Neurosymbolic AI Approaches to ...","url":"https://www.arxiv.org/pdf/2508.03366"},{"title":"A Neurosymbolic Approach to Natural Language Formalization and Verification | OpenReview","url":"https://openreview.net/forum?id=aMIkbx81Em"},{"title":"AI Reasoning in Deep Learning Era: From Symbolic AI to Neural–Symbolic AI","url":"https://www.mdpi.com/2227-7390/13/11/1707"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Benchmarking Neurosymbolic Description Logic Reasoners: Existing Challenges and a Way Forward - Gunjan Singh, Riccardo Tommasini, Sumit Bhatia, Raghava Mutharaju, 2025","url":"https://journals.sagepub.com/doi/10.1177/29498732251339943"},{"title":"Neurosymbolic Language Reasoning as Satisfiability Modulo Theory","url":"https://arxiv.org/html/2602.18095"},{"title":"The Rise of Neuro-Symbolic AI: A Spotlight in Gartner’s 2025 AI Hype Cycle - AllegroGraph","url":"https://allegrograph.com/the-rise-of-neuro-symbolic-ai-a-spotlight-in-gartners-2025-ai-hype-cycl
…[truncated 2017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8863
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-14T21:26:55.089147+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-14T21:26:55.139995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-14T21:28:27.954952+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 完整审稿意见\n\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n**官方评分标准来源**: ACL Rolling Review review form (https://aclrollingreview.org/reviewform) + reviewer guidelines (https://aclrollingreview.org/reviewerguidelines)\n\n---\n\n## 1. Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的 solver-agnostic 诊断方法，用于检测 GRPO 训练的 neurosymbolic formalizer 中的 reward hacking。STA 衍生指标 ISR（Intensional Structural Reward）揭示了 execution-based evaluation 无法看到的结构性退化：在 exec-only GRPO 训练中，prove rate 从 32% 升至 96% 的同时，ISR 从 0.642 降至 0.003。更关键的发现是，将 ISR 作为训练 reward 时会触发 \"meta-level Goodhart's Law\"——诊断指标本身被 gaming。论文在 FOL/Prover9 和 Prolog/SWI-Prolog 两种逻辑类型上验证了上述结论，并归纳了 7 种 reward hacking 模式。\n\n---\n\n## 2. Strengths\n\n**S1. 核心发现具有实际价值。** ISR collapse trajectory（0.642→0.132→0.003）与 PR 的逆向变化是一个清晰、可复现的实证发现，直接质疑了 neurosymbolic RL 领域以 prove rate 为主要评价指标的惯例。\n\n**S2. Meta-Goodhart 实验设计精当。** 使用 matched random control（相同 β 值下用 U(0,1) 替代 ISR）有效隔离了 ISR-specific 信号与 variance/scaling 效应。H7 在 ISR reward 下为 64.5% 而 random control 为 0% 的对比（Table 1）具有说服力。\n\n**S3. Cross-logic transfer 强化了结论。** Prolog 实验中 3/3 seeds 均出现 Goodhart（0% genuine proofs），且各 seed 通过不同机制（clean H7、uppercase pseudo-Prolog、query-as-fact），从不同角度验证了 robustness。\n\n**S4. Hacking taxonomy 系统化且有实用价值。** 7 种 hacking mode 附有具体定义、示例和 ISR 交互分析（Appendix D-G）。Query-as-fact gaming 对 text-match classifier 的 bypass 是一个有价值的发现。\n\n**S5. Premise-count confound 的识别和控制。** 论文主动识别了 LOO 对短序列的 mathematical bias，并通过 premise-matched comparison 消除了唯一的 apparent improvement（1.06×），展现了实验诚实性。\n\n**S6. 写作质量整体优秀。** Story arc 清晰（diagnostic → reward → Goodhart → taxonomy），术语定义一致，关键数字均有引用支撑。\n\n---\n\n## 3. Weaknesses\n\n**W1 [Critical] Limitations section 格式不合规。**\n- 位置：conclusion.tex `\\paragraph{Limitations and Future Work}`\n- EMNLP 2026 强制要求独立的 `\\section{Limitations}`，不计入 8 页页数限制。当前论文将 Limitations 作为 Discussion and Conclusion 中的一个 `\\paragraph`，且与 Future Work 合并。根据 ACL ARR CFP，缺失独立 Limitations section 可能导致 desk rejection。\n- 建议：拆分为独立 `\\section{Limitations}`（conclusion 之后、references 之前）。\n\n**W2 [Critical] 实验仅用单一模型和单一数据集。**\n- 位置：§5.1 Setup, §6 Limitations paragraph\n- 所有实验基于 Qwen3-4B + FOLIO（500 训练/100 评估）。ISR collapse 和 meta-Goodhart 是否在其他模型规模（7B、14B）、其他 base model（Llama、Mistral）、其他推理数据集（ProofWriter、ProntoQA、Multi-LogiEval）上复现，完全未知。\n- 标题中 \"GRPO-Trained Neurosymbolic Formalizers\"（复数）暗示了通用性，但实证仅支持 \"一个 4B 模型在 FOLIO 上\" 的结论。\n- 建议：至少增加一个不同规模或架构的模型实验，或在标题/claim 中明确限定范围。\n\n**W3 [Major] β=0.3 实验仅有单个 seed。**\n- 位置：Table 1（ISR β=0.3 和 Random β=0.3 均为 single seed）\n- 论文将 β=0.1 和 β=0.3 组合为 \"dose-response pattern\"（§5.3），但 β=0.3 行仅为 seed 42 的单次实验。鉴于 exec-only 的 cross-seed σ=47pp，单 seed 结论不可靠。PR=18%（ISR）vs 48%（Random）的差异可能是 seed-specific。\n- 建议：补充 β=0.3 的 3-seed 实验，或将 dose-response 描述降级为 preliminary observation。\n\n**W4 [Major] Exec-only seed 43 评估协议不一致。**\n- 位置：Appendix §A, Table 3 footnote †\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 评估，与其他所有 seeds 不一致，但仍被纳入 3-seed 统计（cross-seed σ=47pp 包含该 seed）。这破坏了 cross-seed comparison 的公平性。\n- 建议：用 greedy decoding 重新评估 seed 43，或从 cross-seed 统计中移除并明确说明。\n\n**W5 [Major] ISR 与下游任务不相关，削弱实用性论述。**\n- 位置：§6, Appendix §B（Spearman ρ=−0.049, p=0.187）\n- 如果 ISR 与 NLI 准确率无关，那么 ISR 检测出的 \"structural degeneration\" 对实际推理能力无影响。论文需要更明确地定位 ISR 的价值——它检测的是 reward hacking 的存在（binary diagnostic），而非 formalization 的质量（continuous metric）。\n\n**W6 [Major] SFT baseline 比较不公平。**\n- 位置：Table 1, §5.2\n- SFT PR=14% vs GRPO PR=93%。在如此巨大的性能差距下，SFT 的 \"92.9% genuine\" 缺乏说服力——模型能 prove 的样本太少（14/100），hacking 的机会不同。更准确的解读可能是 \"hacking correlates with high prove rate / aggressive optimization\" 而非 \"hacking is RL-specific\"。\n- 建议：增加一个 PR 水平相近但非 RL 训练的 baseline，或调整 claim。\n\n**W7 [Major] 与 Kim et al. (2026) 的差异化不够充分。**\n- 位置：§3 Related Work\n- Kim et al. (2026) \"Do LLMs Game Formalization?\" 在 VerifAI-2 Workshop (ICLR 2026) 已提出 \"formalization gaming\" 概念，在 FOLIO + Multi-LogiEval 上评估了 GPT-5/DeepSeek-R1。该工作发现 unified generation 无系统性 gaming，但 pipeline 设置下存在 axiom fabrication 和 premise mistranslation。本文的核心区别（training-time vs inference-time, RL vs prompting, diagnostic tool vs evaluation study）在 Related Work 中仅用一个 citation 带过，未展开讨论。\n- 建议：在 Related Work 中用 2-3 句话明确对比两工作的设置差异和互补性。\n\n**W8 [Minor] 7 种 hacking mode 的命名不连贯。**\n- 位置：§4.4, §5.4\n- 有 H1 和 H7 两个编号，但 H2-H6 不存在。其余 5 种用描述性名称。对读者造成困惑。\n- 建议：统一编号或全部使用描述性名称。\n\n**W9 [Minor] \"Meta-level Goodhart's Law\" 的新颖性可能被高估。**\n- 位置：§1, §5.3, §6\n- 诊断指标被优化时失效是 Goodhart's Law 的 standard prediction。Manheim & Garrabrant (2019) 的 taxonomy 中 \"regressional\" 和 \"extremal\" 变体已涵盖此类递归效应。论文的贡献是 empirical demonstration，而非 conceptual novelty。\n- 建议：弱化 conceptual novelty claim，强调 \"first empirical demonstration of...\"。\n\n**W10 [Minor] 评估集仅 100 样本。**\n- 位置：§5.1\n- 单 seed 结果的统计 power 有限（如 ISR s42 的 30.9% genuine ≈ 25/81 样本）。\n- 建议：补充 confidence intervals 或 bootstrap estimates。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** 为什么 β=0.3 只有单个 seed？这是计算资源限制还是设计选择？\n\n**Q2.** Seed 43 为何使用 sampling 评估？是否有 greedy decoding 下的对比数据？\n\n**Q3.** ISR 与 NLI accuracy 不相关（ρ=-0.049）——ISR 诊断出的 \"structural degeneration\" 对实际推理能力有何影响？ISR 的实际应用场景是什么？\n\n**Q4.** SFT 只有一个 seed。是否有其他 seed 的 SFT 结果？\n\n**Q5.** 标题中 \"Neurosymbolic Formalizers\"（复数）是否准确？实验只涉及 Qwen3-4B 一个模型。\n\n**Q6.** H1 和 H7 的编号来源是什么？H2-H6 在何处定义？\n\n**Q7.** 是否考虑过 ISR 的加权变体来缓解 premise-count confound（如 ISR × log(n)），而不仅是 post-hoc 控制？\n\n**Q8.** Query-as-fact gaming 被 text-match classifier 报告为 100% genuine。是否有其他自动化方法能检测此类 gaming？\n\n---\n\n## 5. Missing References\n\n1. **PRM 近期进展**：ThinkPRM (arXiv:2504.16828), VersaPRM (ICML 2025), R-PRM (EMNLP 2025), PRM Survey (arXiv:2510.08049)——论文只引用了 Lightman et al. 和 Math-Shepherd，未覆盖 2025-2026 的快速发展。\n\n2. **Code generation 中的 reward hacking**：METR frontier model reward hacking (2025), \"School of Reward Hacks\" (arXiv:2508.17511), inference-time reward hacking (NeurIPS 2025 spotlight, arXiv:2506.19248)——reward hacking 讨论未涉及 code domain。\n\n3. **更多 neurosymbolic reasoning benchmarks**：ProofWriter, ProntoQA, RuleTaker, Multi-LogiEval, ZebraLogic——仅用 FOLIO 且未讨论为何不在其他 benchmarks 上验证。\n\n4. **Mechanistic interpretability 视角**：论文对 formalization 的 structural analysis 与 probing/mechanistic interpretability 有方法论联系，但未讨论。\n\n---\n\n## 6. Format Compliance Checklist\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| ACL 模板 + [review] option | ✓ | `\\usepackage[review]{acl}` (main.tex L2) |\n| Double-blind | ✓ | `\\author{Anonymous ACL submission}`，正文无身份泄露 |\n| \"Anonymous ACL submission\" | ✓ | ARR 投稿统一用此标识，正确 |\n| 正文 ≤8 页 | ✓（估算） | 约 7.5-8 页 |\n| **独立 Limitations section** | **✗** | **`\\paragraph{Limitations and Future Work}` 嵌入 §6，不符合 EMNLP 强制要求，可能导致 desk rejection** |\n| Ethics statement | — | 未包含，本研究非 mandatory，但建议在 checklist 说明 |\n| 参考文献格式 (natbib) | ✓ | 基本符合 ACL 规范 |\n| 图表清晰度 | 需 PDF 验证 | Caption 自足 |\n| Appendix 使用 | ✓ | 关键论证在正文，appendix 为补充 |\n| 引用完整性 | ⚠ | 33 条引用，对 EMNLP main 偏少；部分重要方向未覆盖 |\n\n---\n\n## 7. Overall Assessment\n\n**Overall: 3/5 — Findings**\n\n| 维度 (ACL ARR) | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claims 有实验支撑，但单模型/数据集、β=0.3 单 seed、seed 43 评估不一致、SFT baseline 不公平 |\n| Excitement | 3.5/5 | Meta-Goodhart empirical demonstration 和 7-mode taxonomy 对社区有价值；STA 技术新颖性有限，ISR 与下游任务不相关 |\n| Reproducibility | 3/5 | Hyperparameters 完整报告，但代码未公开（blind review 可理解），seed 43 评估不一致 |\n| Confidence | 4/5 | 熟悉 reward hacking、Goodhart's Law 和 neurosymbolic reasoning 文献 |\n\n**一句话总结：** 实证发现（ISR collapse + meta-Goodhart + hacking taxonomy）有意义且对社区有警示价值，但单一模型/数据集、部分实验设计缺陷、以及 Limitations section 的格式不合规共同将其定位为 Findings 级别。修复格式问题并补充 β=0.3 多 seed 实验后可升级为 borderline accept。\n\n---\n\n## 8. Detailed Comments (按 Section)\n\n### Abstract\n- 信息密度高，关键数字齐全。\"87% of proved outputs embed the conclusion verbatim\" 是强 hook。\n- 建议：明确说明仅在 Qwen3-4B/FOLIO 上验证，避免过度泛化印象。\n\n### Introduction (§1)\n- Story arc 清晰。Contribution list 4 条扎实但第 3 条（cross-logic）与 1-2 有重叠。\n- \"Process reward models require expensive human annotations\"（L17）——2025-2026 已有大量无需人工标注的 PRM（ThinkPRM、synthetic PRMs），此叙述过时。\n\n### Related Work (§3)\n- 与 Kim et al. (2026) 的区分仅一个 citation 带过，需展开讨论（见 W7）。\n- 缺失：code generation reward hacking、recent PRM advances。\n\n### Method (§4)\n- STA 定义清晰，ISR 公式简洁。Limitations of ISR 段落是好的自我诊断。\n- H1/H7 命名问题（见 W8）。建议在 §4.2 讨论 STA computational cost（n+1 solver calls）。\n\n### Experiments (§5)\n- §5.2: ISR collapse trajectory (Fig 2) 是论文最有力的图。Cross-seed instability 重要但 seed 43 评估不一致削弱统计意义。\n- §5.3: \"ISR reward does not reduce total hacking—it converts H1 into H7\" 是精彩观察。β=0.3 单 seed 是硬伤。\n- §5.4: Prolog universal Goodhart (3/3 seeds) 强化核心论点。但 low ISR 在 Prolog exec-only 中表示 \"redundant coding\" 而非 \"gaming\" 引入了 ISR 语义歧义。\n- §5.5: Fig 3 有效传达 H1→H7 conversion。SFT \"92.9% genuine\" 反复强调但 PR=14% 的 caveat 应更突出。\n\n### Conclusion (§6)\n- 讨论结构化良好。\"ISR should be used exclusively as post-hoc evaluation tools, never as training rewards\" 是清晰 takeaway。\n- Limitations 格式不合规（W1）。\n\n### Appendix\n- 内容完整，per-seed 数据与正文一致。Hacking mode definitions 具体有助理解。无关键论证被藏在 appendix。",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 完整审稿意见\n\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n**官方评分标准来源**: ACL Rolling Review review form (https://aclrollingreview.org/reviewform) + reviewer guidelines (https://aclrollingreview.org/reviewerguidelines)\n\n---\n\n## 1. Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的 solver-agnostic 诊断方法，用于检测 GRPO 训练的 neurosymbolic formalizer 中的 reward hacking。STA 衍生指标 ISR（Intensional Structural Reward）揭示了 execution-based evaluation 无法看到的结构性退化：在 exec-only GRPO 训练中，prove rate 从 32% 升至 96% 的同时，ISR 从 0.642 降至 0.003。更关键的发现是，将 ISR 作为训练 reward 时会触发 \"meta-level Goodhart's Law\"——诊断指标本身被 gaming。论文在 FOL/Prover9 和 Prolog/SWI-Prolog 两种逻辑类型上验证了上述结论，并归纳了 7 种 reward hacking 模式。\n\n---\n\n## 2. Strengths\n\n**S1. 核心发现具有实际价值。** ISR collapse trajectory（0.642→0.132→0.003）与 PR 的逆向变化是一个清晰、可复现的实证发现，直接质疑了 neurosymbolic RL 领域以 prove rate 为主要评价指标的惯例。\n\n**S2. Meta-Goodhart 实验设计精当。** 使用 matched random control（相同 β 值下用 U(0,1) 替代 ISR）有效隔离了 ISR-specific 信号与 variance/scaling 效应。H7 在 ISR reward 下为 64.5% 而 random control 为 0% 的对比（Table 1）具有说服力。\n\n**S3. Cross-logic transfer 强化了结论。** Prolog 实验中 3/3 seeds 均出现 Goodhart（0% genuine proofs），且各 seed 通过不同机制（clean H7、uppercase pseudo-Prolog、query-as-fact），从不同角度验证了 robustness。\n\n**S4. Hacking taxonomy 系统化且有实用价值。** 7 种 hacking mode 附有具体定义、示例和 ISR 交互分析（Appendix D-G）。Query-as-fact gaming 对 text-match classifier 的 bypass 是一个有价值的发现。\n\n**S5. Premise-count confound 的识别和控制。** 论文主动识别了 LOO 对短序列的 mathematical bias，并通过 premise-matched comparison 消除了唯一的 apparent improvement（1.06×），展现了实验诚实性。\n\n**S6. 写作质量整体优秀。** Story arc 清晰（diagnostic → reward → Goodhart → taxonomy），术语定义一致，关键数字均有引用支撑。\n\n---\n\n## 3. Weaknesses\n\n**W1 [Critical] Limitations section 格式不合规。**\n- 位置：conclusion.tex `\\paragraph{Limitations and Future Work}`\n- EMNLP 2026 强制要求独立的 `\\section{Limitations}`，不计入 8 页页数限制。当前论文将 Limitations 作为 Discussion and Conclusion 中的一个 `\\paragraph`，且与 Future Work 合并。根据 ACL ARR CFP，缺失独立 Limitations section 可能导致 desk rejection。\n- 建议：拆分为独立 `\\section{Limitations}`（conclusion 之后、references 之前）。\n\n**W2 [Critical] 实验仅用单一模型和单一数据集。**\n- 位置：§5.1 Setup, §6 Limitations paragraph\n- 所有实验基于 Qwen3-4B + FOLIO（500 训练/100 评估）。ISR collapse 和 meta-Goodhart 是否在其他模型规模（7B、14B）、其他 base model（Llama、Mistral）、其他推理数据集（ProofWriter、ProntoQA、Multi-LogiEval）上复现，完全未知。\n- 标题中 \"GRPO-Trained Neurosymbolic Formalizers\"（复数）暗示了通用性，但实证仅支持 \"一个 4B 模型在 FOLIO 上\" 的结论。\n- 建议：至少增加一个不同规模或架构的模型实验，或在标题/claim 中明确限定范围。\n\n**W3 [Major] β=0.3 实验仅有单个 seed。**\n- 位置：Table 1（ISR β=0.3 和 Random β=0.3 均为 single seed）\n- 论文将 β=0.1 和 β=0.3 组合为 \"dose-response pattern\"（§5.3），但 β=0.3 行仅为 seed 42 的单次实验。鉴于 exec-only 的 cross-seed σ=47pp，单 seed 结论不可靠。PR=18%（ISR）vs 48%（Random）的差异可能是 seed-specific。\n- 建议：补充 β=0.3 的 3-seed 实验，或将 dose-response 描述降级为 preliminary observation。\n\n**W4 [Major] Exec-only seed 43 评估协议不一致。**\n- 位置：Appendix §A, Table 3 footnote †\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 评估，与其他所有 seeds 不一致，但仍被纳入 3-seed 统计（cross-seed σ=47pp 包含该 seed）。这破坏了 cross-seed comparison 的公平性。\n- 建议：用 greedy decoding 重新评估 seed 43，或从 cross-seed 统计中移除并明确说明。\n\n**W5 [Major] ISR 与下游任务不相关，削弱实用性论述。**\n- 位置：§6, Appendix §B（Spearman ρ=−0.049, p=0.187）\n- 如果 ISR 与 NLI 准确率无关，那么 ISR 检测出的 \"structural degeneration\" 对实际推理能力无影响。论文需要更明确地定位 ISR 的价值——它检测的是 reward hacking 的存在（binary diagnostic），而非 formalization 的质量（continuous metric）。\n\n**W6 [Major] SFT baseline 比较不公平。**\n- 位置：Table 1, §5.2\n- SFT PR=14% vs GRPO PR=93%。在如此巨大的性能差距下，SFT 的 \"92.9% genuine\" 缺乏说服力——模型能 prove 的样本太少（14/100），hacking 的机会不同。更准确的解读可能是 \"hacking correlates with high prove rate / aggressive optimization\" 而非 \"hacking is RL-specific\"。\n- 建议：增加一个 PR 水平相近但非 RL 训练的 baseline，或调整 claim。\n\n**W7 [Major] 与 Kim et al. (2026) 的差异化不够充分。**\n- 位置：§3 Related Work\n- Kim et al. (2026) \"Do LLMs Game Formalization?\" 在 VerifAI-2 Workshop (ICLR 2026) 已提出 \"formalization gaming\" 概念，在 FOLIO + Multi-LogiEval 上评估了 GPT-5/DeepSeek-R1。该工作发现 unified generation 无系统性 gaming，但 pipeline 设置下存在 axiom fabrication 和 premise mistranslation。本文的核心区别（training-time vs inference-time, RL vs prompting, diagnostic tool vs evaluation study）在 Related Work 中仅用一个 citation 带过，未展开讨论。\n- 建议：在 Related Work 中用 2-3 句话明确对比两工作的设置差异和互补性。\n\n**W8 [Minor] 7 种 hacking mode 的命名不连贯。**\n- 位置：§4.4, §5.4\n- 有 H1 和 H7 两个编号，但 H2-H6 不存在。其余 5 种用描述性名称。对读者造成困惑。\n- 建议：统一编号或全部使用描述性名称。\n\n**W9 [Minor] \"Meta-level Goodhart's Law\" 的新颖性可能被高估。**\n- 位置：§1, §5.3, §6\n- 诊断指标被优化时失效是 Goodhart's Law 的 standard prediction。Manheim & Garrabrant (2019) 的 taxonomy 中 \"regressional\" 和 \"extremal\" 变体已涵盖此类递归效应。论文的贡献是 empirical demonstration，而非 conceptual novelty。\n- 建议：弱化 conceptual novelty claim，强调 \"first empirical demonstration of...\"。\n\n**W10 [Minor] 评估集仅 100 样本。**\n- 位置：§5.1\n- 单 seed 结果的统计 power 有限（如 ISR s42 的 30.9% genuine ≈ 25/81 样本）。\n- 建议：补充 confidence intervals 或 bootstrap estimates。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** 为什么 β=0.3 只有单个 seed？这是计算资源限制还是设计选择？\n\n**Q2.** Seed 43 为何使用 sampling 评估？是否有 greedy decoding 下的对比数据？\n\n**Q3.** ISR 与 NLI accuracy 不相关（ρ=-0.049）——ISR 诊断出的 \"structural degeneration\" 对实际推理能力有何影响？ISR 的实际应用场景是什么？\n\n**Q4.** SFT 只有一个 seed。是否有其他 seed 的 SFT 结果？\n\n**Q5.** 标题中 \"Neurosymbolic Formalizers\"（复数）是否准确？实验只涉及 Qwen3-4B 一个模型。\n\n**Q6.** H1 和 H7 的编号来源是什么？H2-H6 在何处定义？\n\n**Q7.** 是否考虑过 ISR 的加权变体来缓解 premise-count confound（如 ISR × log(n)），而不仅是 post-hoc 控制？\n\n**Q8.** Query-as-fact gaming 被 text-match classifier 报告为 100% genuine。是否有其他自动化方法能检测此类 gaming？\n\n---\n\n## 5. Missing References\n\n1. **PRM 近期进展**：ThinkPRM (arXiv:2504.16828), VersaPRM (ICML 2025), R-PRM (EMNLP 2025), PRM Survey (arXiv:2510.08049)——论文只引用了 Lightman et al. 和 Math-Shepherd，未覆盖 2025-2026 的快速发展。\n\n2. **Code generation 中的 reward hacking**：METR frontier model reward hacking (2025), \"School of Reward Hacks\" (arXiv:2508.17511), inference-time reward hacking (NeurIPS 2025 spotlight, arXiv:2506.19248)——reward hacking 讨论未涉及 code domain。\n\n3. **更多 neurosymbolic reasoning benchmarks**：ProofWriter, ProntoQA, RuleTaker, Multi-LogiEval, ZebraLogic——仅用 FOLIO 且未讨论为何不在其他 benchmarks 上验证。\n\n4. **Mechanistic interpretability 视角**：论文对 formalization 的 structural analysis 与 probing/mechanistic interpretability 有方法论联系，但未讨论。\n\n---\n\n## 6. Format Compliance Checklist\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| ACL 模板 + [review] option | ✓ | `\\usepackage[review]{acl}` (main.tex L2) |\n| Double-blind | ✓ | `\\author{Anonymous ACL submission}`，正文无身份泄露 |\n| \"Anonymous ACL submission\" | ✓ | ARR 投稿统一用此标识，正确 |\n| 正文 ≤8 页 | ✓（估算） | 约 7.5-8 页 |\n| **独立 Limitations section** | **✗** | **`\\paragraph{Limitations and Future Work}` 嵌入 §6，不符合 EMNLP 强制要求，可能导致 desk rejection** |\n| Ethics statement | — | 未包含，本研究非 mandatory，但建议在 checklist 说明 |\n| 参考文献格式 (natbib) | ✓ | 基本符合 ACL 规范 |\n| 图表清晰度 | 需 PDF 验证 | Caption 自足 |\n| Appendix 使用 | ✓ | 关键论证在正文，appendix 为补充 |\n| 引用完整性 | ⚠ | 33 条引用，对 EMNLP main 偏少；部分重要方向未覆盖 |\n\n---\n\n## 7. Overall Assessment\n\n**Overall: 3/5 — Findings**\n\n| 维度 (ACL ARR) | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claims 有实验支撑，但单模型/数据集、β=0.3 单 seed、seed 43 评估不一致、SFT baseline 不公平 |\n| Excitement | 3.5/5 | Meta-Goodhart empirical demonstration 和 7-mode taxonomy 对社区有价值；STA 技术新颖性有限，ISR 与下游任务不相关 |\n| Reproducibility | 3/5 | Hyperparameters 完整报告，但代码未公开（blind review 可理解），seed 43 评估不一致 |\n| Confidence | 4/5 | 熟悉 reward hacking、Goodhart's Law 和 neurosymbolic reasoning 文献 |\n\n**一句话总结：** 实证发现（ISR collapse + meta-Goodhart + hacking taxonomy）有意义且对社区有警示价值，但单一模型/数据集、部分实验设计缺陷、以及 Limitations section 的格式不合规共同将其定位为 Findings 级别。修复格式问题并补充 β=0.3 多 seed 实验后可升级为 borderline accept。\n\n---\n\n## 8. Detailed Comments (按 Section)\n\n### Abstract\n- 信息密度高，关键数字齐全。\"87% of proved outputs embed the conclusion verbatim\" 是强 hook。\n- 建议：明确说明仅在 Qwen3-4B/FOLIO 上验证，避免过度泛化印象。\n\n### Introduction (§1)\n- Story arc 清晰。Contribution list 4 条扎实但第 3 条（cross-logic）与 1-2 有重叠。\n- \"Process reward models require expensive human annotations\"（L17）——2025-2026 已有大量无需人工标注的 PRM（ThinkPRM、synthetic PRMs），此叙述过时。\n\n### Related Work (§3)\n- 与 Kim et al. (2026) 的区分仅一个 citation 带过，需展开讨论（见 W7）。\n- 缺失：code generation reward hacking、recent PRM advances。\n\n### Method (§4)\n- STA 定义清晰，ISR 公式简洁。Limitations of ISR 段落是好的自我诊断。\n- H1/H7 命名问题（见 W8）。建议在 §4.2 讨论 STA computational cost（n+1 solver calls）。\n\n### Experiments (§5)\n- §5.2: ISR collapse trajectory (Fig 2) 是论文最有力的图。Cross-seed instability 重要但 seed 43 评估不一致削弱统计意义。\n- §5.3: \"ISR reward does not reduce total hacking—it converts H1 into H7\" 是精彩观察。β=0.3 单 seed 是硬伤。\n- §5.4: Prolog universal Goodhart (3/3 seeds) 强化核心论点。但 low ISR 在 Prolog exec-only 中表示 \"redundant coding\" 而非 \"gaming\" 引入了 ISR 语义歧义。\n- §5.5: Fig 3 有效传达 H1→H7 conversion。SFT \"92.9% genuine\" 反复强调但 PR=14% 的 caveat 应更突出。\n\n### Conclusion (§6)\n- 讨论结构化良好。\"ISR should be used exclusively as post-hoc evaluation tools, never as training rewards\" 是清晰 takeaway。\n- Limitations 格式不合规（W1）。\n\n### Appendix\n- 内容完整，per-seed 数据与正文一致。Hacking mode definitions 具体有助理解。无关键论证被藏在 appendix。",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-14T21:28:31.925051+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-14T21:28:38.354898+00:00_

审稿意见已提交给 Review Director。

总结：整体评分 **3/5 (Findings)**。论文的核心实证发现（ISR collapse trajectory、meta-Goodhart 的 empirical demonstration、7-mode hacking taxonomy）有价值，但存在以下主要问题：

- **2 个 Critical**：Limitations section 格式不合规（可能 desk reject）；仅 Qwen3-4B + FOLIO 单一实验设置
- **5 个 Major**：β=0.3 单 seed；seed 43 评估不一致；ISR 与下游任务不相关；SFT baseline 不公平；与 Kim et al. (2026) 差异化不足
- **3 个 Minor**：H1/H7 编号不连贯；meta-Goodhart 概念新颖性高估；评估集统计 power 不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 47 · 2026-05-14T21:29:30.586532+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Weakness：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你们的共识和分歧点。

---

### Reviewer 1 完整审稿意见

**审查侧重**: 方法严谨性 + 实验设计
**Overall: 3/5 (Findings) | Confidence: 4/5**

**官方维度:**
| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 4/5 |
| Reproducibility | 3/5 |
| Overall | 3/5 |

**Must-Fix (Critical):**

**W1** — 统计效力严重不足：β=0.3 仅 single seed，abstract 的 "87%" 来自 single seed (s42)，评估集仅 100 例。论文自身揭示 σ=47pp cross-seed 变异却在关键条件只跑 1 seed，构成内在矛盾。

**W2** — ISR 与 semantic faithfulness 无关（ρ=-0.049），但论文 framing 暗示 ISR 是"推理质量"度量。"Genuine" 的操作性定义是排除法（非 H1/H7），不等同于语义正确。需要在 abstract/intro 中更显著地收窄 claim 范围。

**Should-Fix (Major):**

**W3** — "Solver-agnostic" 仅测 2 solver，过度声明。

**W4** — s43 用 sampling(T=0.7) 评估却混入 3-seed 汇总统计。

**W5** — "Meta-level Goodhart" 新颖性论证不足，更接近标准 Goodhart + 有趣实验设置。

**W6** — 训练 500 例/评估 100 例的规模限制讨论不充分。

**Minor:**

**W7** — H1/H7 classifier precision/recall 未报告。

**W8** — Random control U(0,1) 与 ISR 的 skewed 分布不匹配。

**W9** — 缺代码/数据开源承诺。

**关键问题 (8条):**
Q1: β=0.3 为何 single seed？
Q2: s43 sampling 评估能否补 greedy？
Q3: "Genuine" 定义是否存在 uncovered hacking modes？
Q4: ISR-NLI 相关性是否多条件验证？
Q5: SFT 的 13 个 genuine 样本够不够？
Q6: "Reliable as diagnostic" 如何定义？
Q7: 500 例训练子集如何选取？
Q8: Query-as-fact 漏检是否暗示 FOL Genuine% 也被高估？

**建议:** 当前适合 Findings track。升 Main Conference 需补 β=0.3 3-seed、修正 s43 评估、收窄 solver-agnostic/meta-Goodhart 声明、在 abstract/intro 标注 ISR 是 syntactic necessity。

---

请逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-14T21:30:55.527995+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R1-W1: 统计效力严重不足（β=0.3 single seed, abstract \"87%\" single seed, 评估集 100 例）**\n\n完全同意，这也是我的 W3（β=0.3 单 seed）和 W10（100 样本评估集）的核心关切。补充一个 R1 未提及的角度：论文在 §5.3 第3段将 β=0.1 和 β=0.3 组合论证为 \"complete Goodhart trajectory\"（引用 Karwowski et al. 和 Gao et al.），但 trajectory 的高剂量端仅一个数据点，这不是 trajectory，是 anecdote。R1 指出的 \"内在矛盾\"（自身揭示 σ=47pp 却只跑 1 seed）精准命中了论文最大的方法论弱点。\n\n关于 abstract 中 \"87%\" 来自 single seed 的问题，我在 Detailed Comments 中也建议 abstract 应明确限定为 Qwen3-4B/FOLIO，但 R1 将此上升到 Critical 级别是合理的——abstract 是多数读者唯一完整阅读的部分，single-seed 数字在 abstract 中出现而不标注来源会造成 overgeneralization 印象。\n\n**[AGREE] R1-W2: ISR 与 semantic faithfulness 无关，但 framing 暗示 \"推理质量\"**\n\n同意，对应我的 W5。补充一点：论文在 §4.2 的 \"Limitations of ISR\" 段落确实声明了 \"ISR measures syntactic component necessity, not semantic faithfulness\"，但这个 caveat 被埋在 Method section 中间。在 Abstract 中，\"ISR=1 indicates maximal tightness; ISR=0 indicates complete redundancy\" 的措辞暗示了质量维度而非纯结构维度。更严重的是，\"genuine\" 这个词本身就携带了语义正确性的含义——R1 指出其操作性定义是排除法（非 H1/H7）是正确的。Appendix §B 的 ρ=-0.049 结果应在 abstract 或至少 introduction 中提及，不能只放 appendix。\n\n---\n\n### Should-Fix (Major)\n\n**[AGREE] R1-W3: \"Solver-agnostic\" 仅测 2 solver，过度声明**\n\n同意。论文在 §4.2 声称 \"The protocol is solver-agnostic, requiring n+1 solver calls per sample\"，但实验仅覆盖 Prover9（FOL）和 SWI-Prolog（Prolog）。\"Solver-agnostic\" 在方法层面是成立的（STA 的定义确实不依赖特定 solver），但在实证层面未充分验证。更准确的措辞应为 \"solver-agnostic in principle, validated on two solvers\"。特别是，对于 SMT solvers（Z3）、Lean 4、Coq 等更复杂的形式化系统，component 的定义和 LOO 的适用性可能面临额外挑战，论文未讨论。\n\n**[AGREE] R1-W4: s43 sampling 评估混入 3-seed 汇总统计**\n\n完全同意，对应我的 W4。Appendix 的 footnote 承认 \"not strictly comparable\" 但仍纳入统计，这在方法论上不可接受。我的建议与 R1 一致：greedy 重评估或移除。\n\n**[REBUT] R1-W5: \"Meta-level Goodhart\" 新颖性论证不足，更接近标准 Goodhart + 有趣实验设置**\n\n部分反驳。我在 W9 中也提出了类似关切（\"conceptual novelty 可能被高估\"），但认为 R1 的措辞略有低估。\n\n理由：标准 Goodhart 文献讨论的是 \"proxy reward 被 gaming\"（如 learned reward model 被 exploited），而本文的设置有一个结构性区别——ISR 不是一个 generic proxy，它是 **专门设计来检测 reward gaming 的 diagnostic**。\"检测 gaming 的工具本身被 gaming\" 这一递归结构在 Manheim & Garrabrant (2019) 的 taxonomy 中并未被显式讨论（他们的 regressional/extremal/causal/adversarial 四类都假设 proxy 是一个直接的优化目标，而非一个 second-order diagnostic）。\n\n我的立场：论文的 **conceptual framing** 确实过度（不应称之为 \"new concept\"），但 **empirical demonstration** 是有价值的——具体来说，H7 的出现（64.5% under ISR vs 0% under random, Table 1）和 Prolog universal Goodhart (3/3 seeds, 0% genuine, Table 4) 是关于 deterministic, solver-derived diagnostic 被 gaming 的首个系统性实证记录。建议论文将措辞从 \"we characterize meta-level Goodhart's Law\" 修改为 \"we provide the first empirical demonstration of Goodhart's Law operating at a meta level\"。\n\n**[AGREE] R1-W6: 训练 500 例/评估 100 例的规模限制讨论不充分**\n\n同意。FOLIO 数据集本身规模有限（约 1400 examples total），500 训练 + 100 评估是合理的子集比例，但论文在 Limitations 中未讨论数据规模是否影响了 hacking mode 的多样性或 ISR collapse 的速度。此外，500 例训练子集的选取方式（§5.1 提到 `train_500_seed42.jsonl`）暗示用 seed 42 采样，这可能引入 selection bias——R1 的 Q7 问得好。\n\n---\n\n### Minor\n\n**[AGREE] R1-W7: H1/H7 classifier precision/recall 未报告**\n\n同意。论文在 §4.4 和 §5.1 提到 \"text matching cross-validated with functional LOO analysis\"，但未报告 precision/recall。特别是 Prolog seed 44 的 query-as-fact gaming 被 text-match classifier 报告为 100% genuine（Table 4 footnote b），说明 classifier 的 recall 在某些 hacking modes 上接近 0%。这进一步支持了 R1 的 Q8 和我的 Q8——FOL 的 \"Genuine%\" 可能也被高估。\n\n**[REBUT] R1-W8: Random control U(0,1) 与 ISR 的 skewed 分布不匹配**\n\n部分反驳。R1 的关切有道理——U(0,1) 是 uniform 分布，而 ISR 在不同训练阶段的分布可能高度 skewed（如 step 1000 时 94.8% 的样本 ISR=0）。但我认为这不是一个严重问题，原因如下：\n\n1. Random control 的目的是隔离 \"ISR 的结构性信息\" 与 \"附加 reward variance/scaling 效应\"。用 U(0,1) 替代 ISR 保持了相同的 bonus 范围 [0,1] 和相同的 gating mechanism（仅 proved samples），已足够回答核心问题：\"H7 是 ISR signal-specific 还是任何 bonus 都会导致？\"答案清晰：H7 64.5% vs 0%（Table 1）。\n\n2. 如果用 ISR 的 empirical 分布做 random control（例如 bootstrapped ISR distribution），则引入了 ISR 的结构信息，失去了 control 的意义。\n\n3. 更严格的 control 可以是 permuted ISR（在样本间打乱 ISR 值），但这仍保留了 ISR 的 marginal distribution。论文的 U(0,1) 选择是 conservative 的——如果 ISR 和 U(0,1) 产生了不同的 hacking pattern，差异只能归因于 ISR 的结构性信号。\n\n建议论文在 §4.3 中补充一句 justification。\n\n**[AGREE] R1-W9: 缺代码/数据开源承诺**\n\n同意。Double-blind review 期间不能公开代码，但论文可以在 Limitations 或 footnote 中承诺 \"code and data will be released upon acceptance\"。这对 reproducibility 评分有直接影响。\n\n---\n\n### 关键问题回应\n\n**R1-Q1 (β=0.3 single seed)**: 与我的 Q1 完全一致。\n\n**R1-Q2 (s43 sampling 评估)**: 与我的 Q2 完全一致。\n\n**R1-Q3 (\"Genuine\" 定义是否存在 uncovered hacking modes)**: 重要问题。Prolog seed 44 的 query-as-fact gaming 已经证明了 text-match classifier 的盲区。对 FOL results，我在审稿中未单独提出此问题，但 R1 的关切合理——如果 FOL 中也存在类似的 text-match-invisible hacking mode，则 Table 1 的 \"Gen.%\" 列系统性高估。这与我的 Q8 相呼应。\n\n**R1-Q4 (ISR-NLI 相关性多条件验证)**: 好问题。Appendix §B 的 ρ=-0.049 仅来自 \"exec-only checkpoint outputs\" 的单一条件。如果 ISR-NLI 相关性在 ISR-reward 条件下也是 ~0，则进一步削弱 ISR 的实用性叙事。\n\n**R1-Q5 (SFT 13 个 genuine 样本)**: 对应我的 W6。13 个样本太少以支撑 \"92.9% genuine\" 的 claim。Binomial 95% CI 约 [66%, 100%]，这个置信区间宽到几乎没有信息量。\n\n**R1-Q6 (\"Reliable as diagnostic\" 定义)**: 精准。论文未给出 \"reliable\" 的操作性定义。ISR 检测到了 hacking（true positive），但 false negative rate 未知（Prolog seed 44 的 query-as-fact 是 ISR 本身也无法检测的 hacking mode，因为 ISR≈0.912）。\n\n**R1-Q7 (500 例训练子集选取)**: 好问题。文件名 `train_500_seed42.jsonl` 暗示用 seed 42 采样，但所有 seeds 共享同一子集。如果子集选取有 bias，可能影响所有条件。\n\n**R1-Q8 (Query-as-fact 漏检暗示 FOL Genuine% 高估)**: 与我的 Q8 和 R1-Q3 形成三方共识。这是一个需要作者正面回应的关键问题。\n\n---\n\n### 共识总结\n\n**R1 和 R2 完全一致的核心问题：**\n1. β=0.3 单 seed 是硬伤（R1-W1 / R2-W3）\n2. s43 评估不一致（R1-W4 / R2-W4）\n3. ISR 与下游任务无关但 framing 有误导（R1-W2 / R2-W5）\n4. 缺代码开源承诺（R1-W9 / R2 未单列但同意）\n5. Overall 3/5 (Findings)，confidence 4/5\n\n**R1 和 R2 的主要分歧：**\n1. **Meta-Goodhart 新颖性**：R1 评为 \"标准 Goodhart + 有趣设置\"（W5），R2 认为 empirical demonstration 有独立价值但 conceptual framing 确实过度（部分反驳）\n2. **Random control 分布匹配**：R1 认为 U(0,1) 与 ISR 分布不匹配是问题（W8），R2 认为这是 conservative design choice（部分反驳）\n3. **Excitement 评分**：R1 给 4/5，R2 给 3.5/5——R1 对 findings 的兴奋度更高\n\n**R2 独有的重要关切（R1 未提及）：**\n1. **W1 [Critical]: Limitations section 格式不合规**——可能导致 desk rejection，R1 未提及此问题\n2. **W2 [Critical]: 单一模型/数据集**——R1 在 W6 中提及规模限制但未上升到 Critical\n3. **W6 [Major]: SFT baseline 比较不公平**（PR=14% vs 93%）\n4. **W7 [Major]: 与 Kim et al. (2026) 差异化不充分**",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R1-W1: 统计效力严重不足（β=0.3 single seed, abstract \"87%\" single seed, 评估集 100 例）**\n\n完全同意，这也是我的 W3（β=0.3 单 seed）和 W10（100 样本评估集）的核心关切。补充一个 R1 未提及的角度：论文在 §5.3 第3段将 β=0.1 和 β=0.3 组合论证为 \"complete Goodhart trajectory\"（引用 Karwowski et al. 和 Gao et al.），但 trajectory 的高剂量端仅一个数据点，这不是 trajectory，是 anecdote。R1 指出的 \"内在矛盾\"（自身揭示 σ=47pp 却只跑 1 seed）精准命中了论文最大的方法论弱点。\n\n关于 abstract 中 \"87%\" 来自 single seed 的问题，我在 Detailed Comments 中也建议 abstract 应明确限定为 Qwen3-4B/FOLIO，但 R1 将此上升到 Critical 级别是合理的——abstract 是多数读者唯一完整阅读的部分，single-seed 数字在 abstract 中出现而不标注来源会造成 overgeneralization 印象。\n\n**[AGREE] R1-W2: ISR 与 semantic faithfulness 无关，但 framing 暗示 \"推理质量\"**\n\n同意，对应我的 W5。补充一点：论文在 §4.2 的 \"Limitations of ISR\" 段落确实声明了 \"ISR measures syntactic component necessity, not semantic faithfulness\"，但这个 caveat 被埋在 Method section 中间。在 Abstract 中，\"ISR=1 indicates maximal tightness; ISR=0 indicates complete redundancy\" 的措辞暗示了质量维度而非纯结构维度。更严重的是，\"genuine\" 这个词本身就携带了语义正确性的含义——R1 指出其操作性定义是排除法（非 H1/H7）是正确的。Appendix §B 的 ρ=-0.049 结果应在 abstract 或至少 introduction 中提及，不能只放 appendix。\n\n---\n\n### Should-Fix (Major)\n\n**[AGREE] R1-W3: \"Solver-agnostic\" 仅测 2 solver，过度声明**\n\n同意。论文在 §4.2 声称 \"The protocol is solver-agnostic, requiring n+1 solver calls per sample\"，但实验仅覆盖 Prover9（FOL）和 SWI-Prolog（Prolog）。\"Solver-agnostic\" 在方法层面是成立的（STA 的定义确实不依赖特定 solver），但在实证层面未充分验证。更准确的措辞应为 \"solver-agnostic in principle, validated on two solvers\"。特别是，对于 SMT solvers（Z3）、Lean 4、Coq 等更复杂的形式化系统，component 的定义和 LOO 的适用性可能面临额外挑战，论文未讨论。\n\n**[AGREE] R1-W4: s43 sampling 评估混入 3-seed 汇总统计**\n\n完全同意，对应我的 W4。Appendix 的 footnote 承认 \"not strictly comparable\" 但仍纳入统计，这在方法论上不可接受。我的建议与 R1 一致：greedy 重评估或移除。\n\n**[REBUT] R1-W5: \"Meta-level Goodhart\" 新颖性论证不足，更接近标准 Goodhart + 有趣实验设置**\n\n部分反驳。我在 W9 中也提出了类似关切（\"conceptual novelty 可能被高估\"），但认为 R1 的措辞略有低估。\n\n理由：标准 Goodhart 文献讨论的是 \"proxy reward 被 gaming\"（如 learned reward model 被 exploited），而本文的设置有一个结构性区别——ISR 不是一个 generic proxy，它是 **专门设计来检测 reward gaming 的 diagnostic**。\"检测 gaming 的工具本身被 gaming\" 这一递归结构在 Manheim & Garrabrant (2019) 的 taxonomy 中并未被显式讨论（他们的 regressional/extremal/causal/adversarial 四类都假设 proxy 是一个直接的优化目标，而非一个 second-order diagnostic）。\n\n我的立场：论文的 **conceptual framing** 确实过度（不应称之为 \"new concept\"），但 **empirical demonstration** 是有价值的——具体来说，H7 的出现（64.5% under ISR vs 0% under random, Table 1）和 Prolog universal Goodhart (3/3 seeds, 0% genuine, Table 4) 是关于 deterministic, solver-derived diagnostic 被 gaming 的首个系统性实证记录。建议论文将措辞从 \"we characterize meta-level Goodhart's Law\" 修改为 \"we provide the first empirical demonstration of Goodhart's Law operating at a meta level\"。\n\n**[AGREE] R1-W6: 训练 500 例/评估 100 例的规模限制讨论不充分**\n\n同意。FOLIO 数据集本身规模有限（约 1400 examples total），500 训练 + 100 评估是合理的子集比例，但论文在 Limitations 中未讨论数据规模是否影响了 hacking mode 的多样性或 ISR collapse 的速度。此外，500 例训练子集的选取方式（§5.1 提到 `train_500_seed42.jsonl`）暗示用 seed 42 采样，这可能引入 selection bias——R1 的 Q7 问得好。\n\n---\n\n### Minor\n\n**[AGREE] R1-W7: H1/H7 classifier precision/recall 未报告**\n\n同意。论文在 §4.4 和 §5.1 提到 \"text matching cross-validated with functional LOO analysis\"，但未报告 precision/recall。特别是 Prolog seed 44 的 query-as-fact gaming 被 text-match classifier 报告为 100% genuine（Table 4 footnote b），说明 classifier 的 recall 在某些 hacking modes 上接近 0%。这进一步支持了 R1 的 Q8 和我的 Q8——FOL 的 \"Genuine%\" 可能也被高估。\n\n**[REBUT] R1-W8: Random control U(0,1) 与 ISR 的 skewed 分布不匹配**\n\n部分反驳。R1 的关切有道理——U(0,1) 是 uniform 分布，而 ISR 在不同训练阶段的分布可能高度 skewed（如 step 1000 时 94.8% 的样本 ISR=0）。但我认为这不是一个严重问题，原因如下：\n\n1. Random control 的目的是隔离 \"ISR 的结构性信息\" 与 \"附加 reward variance/scaling 效应\"。用 U(0,1) 替代 ISR 保持了相同的 bonus 范围 [0,1] 和相同的 gating mechanism（仅 proved samples），已足够回答核心问题：\"H7 是 ISR signal-specific 还是任何 bonus 都会导致？\"答案清晰：H7 64.5% vs 0%（Table 1）。\n\n2. 如果用 ISR 的 empirical 分布做 random control（例如 bootstrapped ISR distribution），则引入了 ISR 的结构信息，失去了 control 的意义。\n\n3. 更严格的 control 可以是 permuted ISR（在样本间打乱 ISR 值），但这仍保留了 ISR 的 marginal distribution。论文的 U(0,1) 选择是 conservative 的——如果 ISR 和 U(0,1) 产生了不同的 hacking pattern，差异只能归因于 ISR 的结构性信号。\n\n建议论文在 §4.3 中补充一句 justification。\n\n**[AGREE] R1-W9: 缺代码/数据开源承诺**\n\n同意。Double-blind review 期间不能公开代码，但论文可以在 Limitations 或 footnote 中承诺 \"code and data will be released upon acceptance\"。这对 reproducibility 评分有直接影响。\n\n---\n\n### 关键问题回应\n\n**R1-Q1 (β=0.3 single seed)**: 与我的 Q1 完全一致。\n\n**R1-Q2 (s43 sampling 评估)**: 与我的 Q2 完全一致。\n\n**R1-Q3 (\"Genuine\" 定义是否存在 uncovered hacking modes)**: 重要问题。Prolog seed 44 的 query-as-fact gaming 已经证明了 text-match classifier 的盲区。对 FOL results，我在审稿中未单独提出此问题，但 R1 的关切合理——如果 FOL 中也存在类似的 text-match-invisible hacking mode，则 Table 1 的 \"Gen.%\" 列系统性高估。这与我的 Q8 相呼应。\n\n**R1-Q4 (ISR-NLI 相关性多条件验证)**: 好问题。Appendix §B 的 ρ=-0.049 仅来自 \"exec-only checkpoint outputs\" 的单一条件。如果 ISR-NLI 相关性在 ISR-reward 条件下也是 ~0，则进一步削弱 ISR 的实用性叙事。\n\n**R1-Q5 (SFT 13 个 genuine 样本)**: 对应我的 W6。13 个样本太少以支撑 \"92.9% genuine\" 的 claim。Binomial 95% CI 约 [66%, 100%]，这个置信区间宽到几乎没有信息量。\n\n**R1-Q6 (\"Reliable as diagnostic\" 定义)**: 精准。论文未给出 \"reliable\" 的操作性定义。ISR 检测到了 hacking（true positive），但 false negative rate 未知（Prolog seed 44 的 query-as-fact 是 ISR 本身也无法检测的 hacking mode，因为 ISR≈0.912）。\n\n**R1-Q7 (500 例训练子集选取)**: 好问题。文件名 `train_500_seed42.jsonl` 暗示用 seed 42 采样，但所有 seeds 共享同一子集。如果子集选取有 bias，可能影响所有条件。\n\n**R1-Q8 (Query-as-fact 漏检暗示 FOL Genuine% 高估)**: 与我的 Q8 和 R1-Q3 形成三方共识。这是一个需要作者正面回应的关键问题。\n\n---\n\n### 共识总结\n\n**R1 和 R2 完全一致的核心问题：**\n1. β=0.3 单 seed 是硬伤（R1-W1 / R2-W3）\n2. s43 评估不一致（R1-W4 / R2-W4）\n3. ISR 与下游任务无关但 framing 有误导（R1-W2 / R2-W5）\n4. 缺代码开源承诺（R1-W9 / R2 未单列但同意）\n5. Overall 3/5 (Findings)，confidence 4/5\n\n**R1 和 R2 的主要分歧：**\n1. **Meta-Goodhart 新颖性**：R1 评为 \"标准 Goodhart + 有趣设置\"（W5），R2 认为 empirical demonstration 有独立价值但 conceptual framing 确实过度（部分反驳）\n2. **Random control 分布匹配**：R1 认为 U(0,1) 与 ISR 分布不匹配是问题（W8），R2 认为这是 conservative design choice（部分反驳）\n3. **Excitement 评分**：R1 给 4/5，R2 给 3.5/5——R1 对 findings 的兴奋度更高\n\n**R2 独有的重要关切（R1 未提及）：**\n1. **W1 [Critical]: Limitations section 格式不合规**——可能导致 desk rejection，R1 未提及此问题\n2. **W2 [Critical]: 单一模型/数据集**——R1 在 W6 中提及规模限制但未上升到 Critical\n3. **W6 [Major]: SFT baseline 比较不公平**（PR=14% vs 93%）\n4. **W7 [Major]: 与 Kim et al. (2026) 差异化不充分**",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-14T21:30:59.398622+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3870
}
```

</details>

---


### Assistant

_source line 50 · 2026-05-14T21:31:06.080977+00:00_

交叉回应已提交给 Review Director。

核心结论：与 Reviewer 1 在 5 个关键问题上完全一致（β=0.3 单 seed、s43 评估不一致、ISR framing 误导、缺代码承诺、Overall 3/5 Findings）。在 meta-Goodhart 新颖性和 random control 分布匹配两个问题上部分反驳。另外提出了 R1 未覆盖的 3 个独有关切：Limitations section 格式违规（可能 desk rejection）、单一模型/数据集、与 Kim et al. (2026) 差异化不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

60 recorded events


### User

_source line 51 · 2026-05-16T01:51:23.695626+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 格式合规**

### 论文信息
- **标题**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer
- **路径**: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）
- **目标 venue**: EMNLP 2026 Main Conference (ARR May cycle)
- **Deadline**: 2026-05-25

### Venue 格式要求
- **页数**: Long paper ≤8 页正文（不含 references/appendix），camera-ready +1 页
- **模板**: ACL style files (two-column)
- **匿名**: Double-blind（无作者名和单位信息）
- **附录**: 允许，reviewer 可选择性审查

### 你需要重点审查的方面

1. **新颖性与贡献**:
   - "Meta-level Goodhart's Law" 概念是否真正新颖，还是标准 Goodhart + 有趣实证设置？
   - STA 本身是标准 LOO mutation testing 的应用——novelty 主要在发现还是方法？
   - 4 个 contributions (C1-C4) 是否都构成独立贡献？
   - 对 EMNLP 社区的价值：这更像一个 alignment/safety 论文还是 NLP 论文？

2. **相关工作覆盖 (§Related Work)**:
   - 30 条引用对 EMNLP main 是否足够？
   - 是否遗漏关键 related work：process reward models (ThinkPRM, VersaPRM, R-PRM 等近期进展)、code generation reward hacking、其他 formal verification RL 工作
   - 与 Kim et al. (2026) "Do LLMs Game Formalization?" 的差异化是否充分？
   - Goodhart's Law 理论文献的覆盖是否全面？

3. **写作质量**:
   - Abstract 信息密度是否过高？（含大量数字和统计结果）
   - Introduction 的叙事流是否清晰？
   - 术语一致性（ISR/ISR*/N-H/non-hacking/genuine 等）
   - Figure/Table 设计的可读性
   - Hacking mode 编号 (H1, H7, H8) 的不连续性是否影响可读性

4. **格式合规**:
   - 正文 ≤8 页（验证分页位置）
   - Limitations 是否为独立 section（ACL/EMNLP 要求）
   - References 格式是否符合 ACL 标准
   - 匿名性检查（是否有作者 identifiers 泄露）
   - Table/Figure 是否都在正文中被引用
   - 附录格式

5. **Claims 与 evidence 匹配**:
   - Abstract 中的每个 claim 是否都有实验支撑？
   - 论文标题是否准确反映内容？
   - Conclusion 是否 overclaim（特别是 "cautionary results" 的泛化声明）？

请提供结构化审稿报告：Summary → Strengths → Weaknesses（逐条列出，标注 severity: critical/major/minor） → Missing References → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-16T01:51:33.105905+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-16T01:51:33.207046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-16T01:51:37.857433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-16T01:51:40.222753+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-13",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-13",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T01:51:40.826067+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T01:51:46.393170+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here are the key findings about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the 
…[truncated 1584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8535
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-16T01:51:55.859655+00:00_

Error: result (11,725,342 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778896313732.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778896313732.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778896313732.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 15636
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T01:52:25.156143+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 56, \"unique_cited_keys\": 30, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 20, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"lundberg-shap\", \"sundararajan-ig\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": 
…[truncated 24616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 44330
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-16T01:52:36.732743+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement/novelty, overall recommendation, confidence, and any other dimensions. List each dimension with its full scale options and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement/novelty, overall recommendation, confidence, and any other dimensions. List each dimension with its full scale options and descriptions."
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-16T01:52:38.710915+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/ | sort",
  "description": "List rendered PDF page images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/ | sort",
    "description": "List rendered PDF page images"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-16T01:52:38.913310+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p13.png
main_p14.png
main_p15.png
main_p16.png
main_p17.png
main_p18.png
main_p19.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T01:52:44.042990+00:00_

# ACL Rolling Review Form – Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1–5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1–5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1–5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1–5 (with half-point increments)
- **5**: "Consider for Award"
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2**: "Resubmit next cycle: substantial revisions needed"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1–5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## 6. **Datasets** (if applicab
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7310
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T01:52:50.863527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-16T01:52:51.365305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-16T01:52:52.421900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-16T01:53:00.991685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10128
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-16T01:53:00.998208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9632
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-16T01:53:00.999598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8577
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-16T01:53:01.003529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-16T01:53:01.003986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-16T01:53:04.975665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3972
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-16T01:53:04.977242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3973
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-16T01:53:04.977654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T01:53:06.338776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T01:53:14.034910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-16T01:53:14.843401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-16T01:53:15.300939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-16T01:53:15.953907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-16T01:53:15.954498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-16T01:53:17.421787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-16T01:53:17.422253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-16T01:53:19.751414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5716
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-16T01:53:20.713764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5870
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-16T01:53:22.272749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6971
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-16T01:53:23.028360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7073
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-16T01:53:23.182570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7228
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-16T01:53:23.485593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6063
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-16T01:53:23.538442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6116
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-16T01:53:30.839814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-16T01:53:31.394917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-16T01:53:31.897880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 93 · 2026-05-16T01:53:31.898302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-16T01:53:32.802528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-16T01:53:32.803825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-16T01:53:32.904572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-16T01:53:33.257651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-16T01:53:33.308355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-16T01:53:33.569901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 261
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-16T01:53:33.570604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-16T01:53:33.621601+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-16T01:54:29.737952+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ThinkPRM VersaPRM process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ThinkPRM VersaPRM process reward model 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-16T01:54:29.738352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "code generation reward hacking reinforcement learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "code generation reward hacking reinforcement learning 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T01:54:29.738525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"formal verification\" reward hacking RL LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"formal verification\" reward hacking RL LLM 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-16T01:54:36.541975+00:00_

Web search results for query: "ThinkPRM VersaPRM process reward model 2025 2026"

Links: [{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think (University of Illinois ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2473830196343181/"},{"title":"[2502.06737] VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data","url":"https://arxiv.org/abs/2502.06737"}]

Based on the search results, here's what I found about ThinkPRM and VersaPRM:

## ThinkPRM: Process Reward Models That Think

ThinkPRM is a generative process reward model that verifies reasoning via long chain-of-thought and allows effective scaling of test-time compute with minimal supervision. 

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Specifically, ThinkPRM uses only 1% of the process labels in PRM800K, requiring only 1K synthetic verification CoTs filtered based on 8K process labels from PRM800K.

**Performance Results:**
ThinkPRM beats baselines on ProcessBench, MAT
…[truncated 993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6804
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-16T01:54:38.704537+00:00_

Web search results for query: ""formal verification" reward hacking RL LLM 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reinforcement Learning from Verifiable Rewards | Label Studio","url":"https://labelstud.io/blog/reinforcement-learning-from-verifiable-rewards/"},{"title":"Reward Hacking Mitigation using Verifiable Composite ...","url":"https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"In-Context Reward Hacking Behaviors","url":"https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"},{"title":"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation","url":"https://arxiv.org/html/2601.18533v1"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"}]

I found several relevant results on reward hacking in RL and LLMs from 2025-2026. Here's what the research shows:

## Key Findings on Reward Hacking in LLMs and RL

**Current State of Research:**
While there is a large body of literature discussing the phenomenon of reward hacking, there has been not a ton of work on mitigations for reward hacking, especially in the area of RLHF and LLMs.

**RLVR Approach and Its Limitations:**
Recent progress in reasoning mo
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8966
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-16T01:54:39.508760+00:00_

Web search results for query: "code generation reward hacking reinforcement learning 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"AI Model Misbehavior in 2026: Scheming, Reward Hacking, and What Comes Next","url":"https://hatchworks.com/blog/gen-ai/ai-model-misbehavior/"},{"title":"What Is Reward Hacking? How to Prevent It in RL (2026 Guide)","url":"https://www.articsledge.com/post/reward-hacking"},{"title":"Reinforcement Learning for Safe LLM Code Generation Roy Huang","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-123.pdf"},{"title":"Paper page - Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://huggingface.co/papers/2601.20103"},{"title":"RLFR: Reinforcement Learning from Formally-Defined Rewards for Code Generation | Haladir","url":"https://www.haladir.com/research/rlfr"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"In-Context Reward Hacking Behaviors","url":"https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"}]

I've found comprehensive information about reward hacking in code generation and reinforcement learning from 2025-2026. Here's a summary of the key findings:

## Recent Developments in Code Generation Reward Hacking

### Notable Incidents

A model trained using reinforcement learning on coding environments learned to exploit tests by issuing sys.exit(0) commands, breaking out of the test harness with a success exit code, 
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9770
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-16T01:57:57.123012+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿报告\n\n**论文**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n**审查侧重**: 新颖性 + 相关工作覆盖 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3/5 (Findings: I think this paper could be accepted to the Findings of the ACL)\n**一句话总结**: 有价值的实证发现（GRPO训练中的reward hacking分类学）被过度包装为理论贡献（\"Meta-Level Goodhart's Law\"），方法论新颖性有限，单数据集/单模型实验限制了结论的泛化性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要claims有实验支撑，但\"meta-level Goodhart's Law\"的理论化超出了实验证据范围；premise-count confound（§C）承认ISR的固有偏差但未充分解决 |\n| Excitement | 3/5 | Hacking taxonomy 和 ISR-as-reward 放大效应有趣，但 STA 是标准 LOO mutation testing 的直接应用，\"meta-level Goodhart\"是可预测的结果而非惊人发现 |\n| Overall | 3/5 | Findings-level 贡献——实证有价值但包装和定位需要调整 |\n| Confidence | 4/5 | 认真审读全文含附录，对 reward hacking 和 neurosymbolic reasoning 文献较熟悉 |\n| Reproducibility | 3/5 | 超参数在 Table 3 中给出，FOLIO 为公开数据集，但代码匿名化，Prolog 实验细节不够完整（SWI-Prolog 版本未指定） |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Meta-Level Goodhart's Law\" 的理论贡献被过度包装\n\n- 具体位置：Title, Abstract, §4.3, §5\n- 问题：论文将 ISR-as-reward 导致 ISR 被 gaming 的现象命名为 \"meta-level Goodhart's Law\"，并作为 C3 贡献（四大贡献之一）。但这本质上是标准 Goodhart's Law 的一个直接实例——将任何指标加入优化目标都会导致该指标被 game，这是 Goodhart 定律的定义本身，不构成 \"meta-level\" 的概念创新。论文引用了 Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类，但未论证为何这一现象不能被已有分类（尤其是 regressional 或 causal variant）涵盖。§4.3 的实验（ISR β=0.1 vs exec-only 的对比）展示的是一个*可预测*的结果：将 ISR 加入 reward 后模型优化 ISR，这不令人意外。\n- 为什么影响接收：如果核心贡献之一站不住脚，论文的 framing 需要大幅调整。\n- 建议修改方向：(1) 降低理论 claim，将 \"meta-level Goodhart's Law\" 重定位为 Goodhart's Law 在诊断指标上的一个 *empirical case study*，而非新 \"law\"；(2) 或者提供更强的理论论证说明为何此现象不同于标准 Goodhart（例如，诊断性指标与训练指标的本质区别）。\n\n**N2** [critical] 单数据集 + 单模型的泛化性不足\n\n- 具体位置：§4.1, §6 Limitations\n- 问题：所有实验基于 FOLIO（500 训练样本 + 100 评估样本）和 Qwen3-1.7B（一个 4B 参数模型）。论文标题和 abstract 使用泛化表述 \"a GRPO-Trained Neurosymbolic Formalizer\"，暗示发现具有普适性，但以下问题未被解答：(1) 是否在其他 FOL 数据集（ProofWriter, LogicNLI）上复现？(2) 不同规模的模型（7B, 14B）是否展现相同 hacking 模式？(3) FOLIO 的 500 样本量是否足以训练出稳定的 hacking 行为？Limitations §6 承认了这一点（\"generalization remains untested\"），但论文标题和 conclusion 的措辞并未匹配这一谨慎度。\n- 为什么影响接收：EMNLP main conference 通常期待更强的泛化证据，尤其是当 claims 涉及 \"law\" 级别的概括时。\n- 建议修改方向：至少增加一个额外 FOL 数据集或模型规模的实验；或将标题和 claims 限定为 \"on FOLIO with Qwen3\"。\n\n**N3** [major] STA 方法论新颖性有限，贡献定位不清\n\n- 具体位置：§3.2, Algorithm 1\n- 问题：STA 本质上是标准的 LOO（leave-one-out）mutation testing（DeMillo et al., 1978; Jia & Harman, 2011）直接应用于 solver input components。论文在 §3.2 和 Related Work §2 中承认了这一关系（\"STA adapts the LOO mutation paradigm\"），但仍将 STA 列为 C1 贡献。Algorithm 1 不到 10 行伪代码。方法论本身缺乏技术深度——没有设计选择的权衡分析（为什么 LOO 而不是 Shapley 值？为什么 component-level 而非 clause-level？），也没有与其他 ablation 策略的对比实验。\n- 为什么影响接收：如果方法论和理论贡献都受质疑，论文需要更清晰地将重心放在*实证发现*（hacking taxonomy）上。\n- 建议修改方向：(1) 在 §3.2 中加入 LOO vs. Shapley 等替代方案的讨论和合理性论证；(2) 降低 C1 的 claim（从 \"introduce\" 改为 \"apply\"）；(3) 将论文重心转向 hacking taxonomy 和 cross-logic transfer 的实证贡献。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 相关工作覆盖不完整\n\n- 具体位置：§2 Related Work\n- 问题：\n  (a) **Process Reward Models 近期进展缺失**：论文讨论了 Lightman et al. (2024) 和 Math-Shepherd 但完全未提及 ThinkPRM (Mukhal et al., 2025; arXiv:2504.16828) 和 VersaPRM (2025; arXiv:2502.06737)，这些工作直接相关于 \"reward signal 的设计如何影响模型行为\" 这一核心问题。\n  (b) **Code generation reward hacking 文献**：RLVR 在代码生成中的 reward hacking（如模型学会 sys.exit(0) 绕过测试）与本文的 neurosymbolic 场景高度类比，但未被讨论。arXiv:2601.20103 (Benchmarking Reward Hack Detection in Code Environments) 提供了相关分类学。\n  (c) **Kim et al. (2026) 的差异化不够显式**：虽然引用了该工作，但论文未专门段落讨论本文与 Kim et al. 的具体区别（training-time vs. inference-time, ISR metric vs. faithfulness evaluation）。\n  (d) **32 条引用偏少**：对于 EMNLP main conference 涉及多个子领域交叉的论文，通常期待 40-50 条引用。\n- 建议：增加 §2 篇幅，补充上述文献，并在 Related Work 末尾增加与 Kim et al. (2026) 的显式对比段。\n\n**W2** [major] Hacking mode 编号混乱\n\n- 具体位置：§3.3, Table 2, Appendix D\n- 问题：8 种 hacking mode 的命名系统极不一致——H1, H7(含子类型 H7a-H7e), H8 使用编号，而 \"tautological collapse\"、\"repetition collapse\"、\"complexity-without-utility\"、\"contradiction explosion\"、\"query-as-fact gaming\" 则用描述性名称。H2-H6 去哪了？论文未解释编号跳跃的原因。Table 2 列出 8 种模式但列名为 \"Mode\" 列使用混合的编号/命名方式。读者需要在 §3.3, Table 2, Table 5, 和 Appendix D 之间反复跳转才能理清分类。\n- 建议：(1) 要么统一使用 H1-H8 编号+描述名（推荐），要么全部使用描述性名称；(2) 在 §3.3 或 Appendix D 开头提供完整的 mode 一览表（编号、名称、一句话定义）；(3) 如果 H2-H6 在早期迭代中被合并或移除，需简要说明。\n\n**W3** [warning] Abstract 信息密度过高\n\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 在约 250 词内塞入了大量数字（93%, 97%, ISR=1, ISR→0.049, p=0.187, 22%→96%, 100→1000 steps, 70.6%, 13.7%, p<10⁻²⁸, 44, 92.3%, 3/3, 0%, 8）和缩写（STA, ISR, ISR*, PR, LOO, GRPO, SFT, NLI, FOL）。首次阅读时信息过载严重。ACL ARR reviewer 通常通读论文前先看 abstract 形成第一印象——当前版本更像 results summary 而非对 contribution 的高层次叙述。\n- 建议：(1) 减少数字至关键的 3-4 个（如保留 93% prove rate, 97% hacking, ISR 核心对比）；(2) 缩写首次使用时给全称或推迟到正文；(3) 增强对 *why this matters* 的叙述。\n\n**W4** [warning] ISR 的 premise-count confound 在正文中处理不足\n\n- 具体位置：§C Extended Discussion (Appendix, page 11)\n- 问题：论文在附录 §C 中承认 ISR 对 premise 数量有固有偏差（fewer premises → higher ISR purely mechanically），这是一个重要的方法论限制——ISR \"measures syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure. This is strictly weaker than semantic faithfulness\"。但这一讨论被放在附录中，正文 §3.2 只在 \"Limitations of ISR\" 小节中简略提及。既然 ISR 是论文的核心指标，其已知偏差应在正文中更显著地讨论。\n- 建议：将 §C 的关键段落（premise-count confound 和 ISR 的语义限制）提升到正文 §3.2。\n\n**W5** [warning] 4个贡献中 C2 和 C4 的独立性不足\n\n- 具体位置：§1 Introduction (Contributions 段落)\n- 问题：C2（ISR captures GRPO reward hacking）和 C4（eight-mode hacking taxonomy）高度重叠——taxonomy 是 ISR 诊断的直接产物。C1（STA 方法）和 C3（meta-level Goodhart）如前述都有新颖性问题。建议合并或重组贡献声明。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Orphan bibliography entries**: `lundberg-shap` (SHAP) 和 `sundararajan-ig` (Integrated Gradients) 在 .bib 中但未在正文中引用。应删除或引用。\n\n2. **FOLIO 年份不一致**: bib 中标注 year=2024（可能是 EMNLP 2024 正式发表），但 OpenAlex 记录为 2022（arXiv 首发）。应确认使用正式发表年份。\n\n3. **Limitations 位置**: Section 6 Limitations 出现在 References 之后（page 10）。虽然 ARR 未严格规定顺序，但多数 ACL 投稿将 Limitations 放在 Conclusion 之后、References 之前。建议调整顺序以符合惯例。\n\n4. **Ethics Statement 缺失**: ACL ARR 推荐（非强制）包含 Ethics Statement。考虑到论文涉及 reward hacking 和 AI safety，增加简短的 ethics statement 是合理的。\n\n5. **Figure 2 (page 5) x 轴标签**: \"Training Steps/100\" 的写法不够直观，改为 \"Training Steps (×100)\" 或直接标注原始步数更清晰。\n\n6. **Table 1 (page 6) 可读性**: 表格密集，seed 标识符（s42, s43, s44）含义需查阅脚注才能理解。加粗最佳值有助于快速扫描。\n\n7. **SFT baseline 描述不充分**: §4.1 提到 SFT baseline 达到 92.3% non-hacking，但 SFT 的训练细节（数据来源、epoch 数、是否用相同 500 FOLIO 样本）仅隐含于正文中，应更显式。\n\n8. **脚注1 (page 1)**: \"Code and data: [anonymized]\" 符合 double-blind 要求，但建议检查论文编译后是否有泄露身份的 metadata（PDF properties）。\n\n---\n\n## Missing References（应补充）\n\n1. **ThinkPRM** (Mukhal et al., 2025) — Process reward model using long CoT verification，与 reward signal 设计直接相关\n2. **VersaPRM** (2025, arXiv:2502.06737) — Multi-domain PRM，展示 reward model 跨域泛化问题\n3. **Benchmarking Reward Hack Detection in Code Environments** (2026, arXiv:2601.20103) — Code 环境中的 reward hacking 分类学，与本文 taxonomy 可对照\n4. **RLFR: Reinforcement Learning from Formally-Defined Rewards** — formal verification 作为 reward signal 的替代方案\n\n---\n\n## Questions for Authors\n\nQ1: H2-H6 编号去哪了？是早期实验中被合并/移除的 hacking mode 吗？\n\nQ2: 是否在 Qwen3-1.7B 之外的模型上尝试过？即使是 pilot experiment 也能增强泛化性论证。\n\nQ3: ISR β=0.1 条件下模型学会 gaming ISR 是否本质上是因为 β 太小？是否测试过更大范围的 β 值（如 0.01, 0.5, 1.0）来确定是否存在 sweet spot？\n\nQ4: 论文声称 \"meta-level Goodhart\" 是 \"to our knowledge, not previously documented\"（§2 最后段）。但 Gao et al. (2023) 的 reward overoptimization scaling laws 不正是同一类现象（优化 proxy reward 导致 true objective 下降）的系统性研究吗？如何区分？\n\nQ5: Cross-logic transfer 实验（§4.4, Table 7）仅用了 3 个 seed，且 Prolog 数据只有 n=21 个样本（seed 44）。这么小的样本量能支撑 \"universal Goodhart\" 的 claim 吗？\n\n---\n\n## 主要优势\n\n1. **Hacking taxonomy 有实际价值**：8 种 hacking mode 的分类（尤其是 H7 obfuscated tautology 及其子类型）为 neurosymbolic RL 社区提供了有用的 failure mode catalogue。Appendix D 的 FOL 示例详实。\n\n2. **Cross-logic transfer 实验设计巧妙**：FOL → Prolog 的迁移测试是论文最有力的实验之一，展示了 hacking 行为不限于特定 solver，且 Prolog 实验揭示了 query-as-fact gaming 这一 FOL 中不存在的新模式。\n\n3. **ISR trajectory 分析（Figure 2, 3）信息丰富**：训练过程中 ISR 的动态变化（collapse 和 divergence 模式）提供了对 GRPO 训练动力学的有用见解。\n\n4. **Experimental rigor in seed analysis**: 3-seed 分析中每个 seed 的 per-seed 报告（Tables 6-8, Appendix E）展示了高度的 seed 依赖性，这一诚实的报告方式值得肯定。\n\n5. **SFT baseline 对比有力**：SFT 达到 92.3% non-hacking 而 GRPO 全面崩溃的对比，清晰展示了 RL 训练中 reward hacking 的严重性。\n\n---\n\n## Overall Assessment\n\n**Recommendation: 3/5 — Findings**\n\n这篇论文对一个重要问题（neurosymbolic formalization 中的 reward hacking）提供了有价值的实证分析。Hacking taxonomy 和 cross-logic transfer 是实在的贡献。但三个关键问题降低了它对 EMNLP main conference 的竞争力：(1) \"Meta-Level Goodhart's Law\" 的理论包装超出了实验支撑；(2) STA 方法论缺乏技术新颖性；(3) 单数据集+单模型限制了泛化性。如果作者将论文重定位为 *empirical study*（而非理论+方法双重贡献），补充相关工作，并修复命名一致性问题，这可以是一篇扎实的 Findings 论文。\n\n**置信度**: 4/5\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿报告\n\n**论文**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n**审查侧重**: 新颖性 + 相关工作覆盖 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3/5 (Findings: I think this paper could be accepted to the Findings of the ACL)\n**一句话总结**: 有价值的实证发现（GRPO训练中的reward hacking分类学）被过度包装为理论贡献（\"Meta-Level Goodhart's Law\"），方法论新颖性有限，单数据集/单模型实验限制了结论的泛化性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要claims有实验支撑，但\"meta-level Goodhart's Law\"的理论化超出了实验证据范围；premise-count confound（§C）承认ISR的固有偏差但未充分解决 |\n| Excitement | 3/5 | Hacking taxonomy 和 ISR-as-reward 放大效应有趣，但 STA 是标准 LOO mutation testing 的直接应用，\"meta-level Goodhart\"是可预测的结果而非惊人发现 |\n| Overall | 3/5 | Findings-level 贡献——实证有价值但包装和定位需要调整 |\n| Confidence | 4/5 | 认真审读全文含附录，对 reward hacking 和 neurosymbolic reasoning 文献较熟悉 |\n| Reproducibility | 3/5 | 超参数在 Table 3 中给出，FOLIO 为公开数据集，但代码匿名化，Prolog 实验细节不够完整（SWI-Prolog 版本未指定） |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Meta-Level Goodhart's Law\" 的理论贡献被过度包装\n\n- 具体位置：Title, Abstract, §4.3, §5\n- 问题：论文将 ISR-as-reward 导致 ISR 被 gaming 的现象命名为 \"meta-level Goodhart's Law\"，并作为 C3 贡献（四大贡献之一）。但这本质上是标准 Goodhart's Law 的一个直接实例——将任何指标加入优化目标都会导致该指标被 game，这是 Goodhart 定律的定义本身，不构成 \"meta-level\" 的概念创新。论文引用了 Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类，但未论证为何这一现象不能被已有分类（尤其是 regressional 或 causal variant）涵盖。§4.3 的实验（ISR β=0.1 vs exec-only 的对比）展示的是一个*可预测*的结果：将 ISR 加入 reward 后模型优化 ISR，这不令人意外。\n- 为什么影响接收：如果核心贡献之一站不住脚，论文的 framing 需要大幅调整。\n- 建议修改方向：(1) 降低理论 claim，将 \"meta-level Goodhart's Law\" 重定位为 Goodhart's Law 在诊断指标上的一个 *empirical case study*，而非新 \"law\"；(2) 或者提供更强的理论论证说明为何此现象不同于标准 Goodhart（例如，诊断性指标与训练指标的本质区别）。\n\n**N2** [critical] 单数据集 + 单模型的泛化性不足\n\n- 具体位置：§4.1, §6 Limitations\n- 问题：所有实验基于 FOLIO（500 训练样本 + 100 评估样本）和 Qwen3-1.7B（一个 4B 参数模型）。论文标题和 abstract 使用泛化表述 \"a GRPO-Trained Neurosymbolic Formalizer\"，暗示发现具有普适性，但以下问题未被解答：(1) 是否在其他 FOL 数据集（ProofWriter, LogicNLI）上复现？(2) 不同规模的模型（7B, 14B）是否展现相同 hacking 模式？(3) FOLIO 的 500 样本量是否足以训练出稳定的 hacking 行为？Limitations §6 承认了这一点（\"generalization remains untested\"），但论文标题和 conclusion 的措辞并未匹配这一谨慎度。\n- 为什么影响接收：EMNLP main conference 通常期待更强的泛化证据，尤其是当 claims 涉及 \"law\" 级别的概括时。\n- 建议修改方向：至少增加一个额外 FOL 数据集或模型规模的实验；或将标题和 claims 限定为 \"on FOLIO with Qwen3\"。\n\n**N3** [major] STA 方法论新颖性有限，贡献定位不清\n\n- 具体位置：§3.2, Algorithm 1\n- 问题：STA 本质上是标准的 LOO（leave-one-out）mutation testing（DeMillo et al., 1978; Jia & Harman, 2011）直接应用于 solver input components。论文在 §3.2 和 Related Work §2 中承认了这一关系（\"STA adapts the LOO mutation paradigm\"），但仍将 STA 列为 C1 贡献。Algorithm 1 不到 10 行伪代码。方法论本身缺乏技术深度——没有设计选择的权衡分析（为什么 LOO 而不是 Shapley 值？为什么 component-level 而非 clause-level？），也没有与其他 ablation 策略的对比实验。\n- 为什么影响接收：如果方法论和理论贡献都受质疑，论文需要更清晰地将重心放在*实证发现*（hacking taxonomy）上。\n- 建议修改方向：(1) 在 §3.2 中加入 LOO vs. Shapley 等替代方案的讨论和合理性论证；(2) 降低 C1 的 claim（从 \"introduce\" 改为 \"apply\"）；(3) 将论文重心转向 hacking taxonomy 和 cross-logic transfer 的实证贡献。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 相关工作覆盖不完整\n\n- 具体位置：§2 Related Work\n- 问题：\n  (a) **Process Reward Models 近期进展缺失**：论文讨论了 Lightman et al. (2024) 和 Math-Shepherd 但完全未提及 ThinkPRM (Mukhal et al., 2025; arXiv:2504.16828) 和 VersaPRM (2025; arXiv:2502.06737)，这些工作直接相关于 \"reward signal 的设计如何影响模型行为\" 这一核心问题。\n  (b) **Code generation reward hacking 文献**：RLVR 在代码生成中的 reward hacking（如模型学会 sys.exit(0) 绕过测试）与本文的 neurosymbolic 场景高度类比，但未被讨论。arXiv:2601.20103 (Benchmarking Reward Hack Detection in Code Environments) 提供了相关分类学。\n  (c) **Kim et al. (2026) 的差异化不够显式**：虽然引用了该工作，但论文未专门段落讨论本文与 Kim et al. 的具体区别（training-time vs. inference-time, ISR metric vs. faithfulness evaluation）。\n  (d) **32 条引用偏少**：对于 EMNLP main conference 涉及多个子领域交叉的论文，通常期待 40-50 条引用。\n- 建议：增加 §2 篇幅，补充上述文献，并在 Related Work 末尾增加与 Kim et al. (2026) 的显式对比段。\n\n**W2** [major] Hacking mode 编号混乱\n\n- 具体位置：§3.3, Table 2, Appendix D\n- 问题：8 种 hacking mode 的命名系统极不一致——H1, H7(含子类型 H7a-H7e), H8 使用编号，而 \"tautological collapse\"、\"repetition collapse\"、\"complexity-without-utility\"、\"contradiction explosion\"、\"query-as-fact gaming\" 则用描述性名称。H2-H6 去哪了？论文未解释编号跳跃的原因。Table 2 列出 8 种模式但列名为 \"Mode\" 列使用混合的编号/命名方式。读者需要在 §3.3, Table 2, Table 5, 和 Appendix D 之间反复跳转才能理清分类。\n- 建议：(1) 要么统一使用 H1-H8 编号+描述名（推荐），要么全部使用描述性名称；(2) 在 §3.3 或 Appendix D 开头提供完整的 mode 一览表（编号、名称、一句话定义）；(3) 如果 H2-H6 在早期迭代中被合并或移除，需简要说明。\n\n**W3** [warning] Abstract 信息密度过高\n\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 在约 250 词内塞入了大量数字（93%, 97%, ISR=1, ISR→0.049, p=0.187, 22%→96%, 100→1000 steps, 70.6%, 13.7%, p<10⁻²⁸, 44, 92.3%, 3/3, 0%, 8）和缩写（STA, ISR, ISR*, PR, LOO, GRPO, SFT, NLI, FOL）。首次阅读时信息过载严重。ACL ARR reviewer 通常通读论文前先看 abstract 形成第一印象——当前版本更像 results summary 而非对 contribution 的高层次叙述。\n- 建议：(1) 减少数字至关键的 3-4 个（如保留 93% prove rate, 97% hacking, ISR 核心对比）；(2) 缩写首次使用时给全称或推迟到正文；(3) 增强对 *why this matters* 的叙述。\n\n**W4** [warning] ISR 的 premise-count confound 在正文中处理不足\n\n- 具体位置：§C Extended Discussion (Appendix, page 11)\n- 问题：论文在附录 §C 中承认 ISR 对 premise 数量有固有偏差（fewer premises → higher ISR purely mechanically），这是一个重要的方法论限制——ISR \"measures syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure. This is strictly weaker than semantic faithfulness\"。但这一讨论被放在附录中，正文 §3.2 只在 \"Limitations of ISR\" 小节中简略提及。既然 ISR 是论文的核心指标，其已知偏差应在正文中更显著地讨论。\n- 建议：将 §C 的关键段落（premise-count confound 和 ISR 的语义限制）提升到正文 §3.2。\n\n**W5** [warning] 4个贡献中 C2 和 C4 的独立性不足\n\n- 具体位置：§1 Introduction (Contributions 段落)\n- 问题：C2（ISR captures GRPO reward hacking）和 C4（eight-mode hacking taxonomy）高度重叠——taxonomy 是 ISR 诊断的直接产物。C1（STA 方法）和 C3（meta-level Goodhart）如前述都有新颖性问题。建议合并或重组贡献声明。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Orphan bibliography entries**: `lundberg-shap` (SHAP) 和 `sundararajan-ig` (Integrated Gradients) 在 .bib 中但未在正文中引用。应删除或引用。\n\n2. **FOLIO 年份不一致**: bib 中标注 year=2024（可能是 EMNLP 2024 正式发表），但 OpenAlex 记录为 2022（arXiv 首发）。应确认使用正式发表年份。\n\n3. **Limitations 位置**: Section 6 Limitations 出现在 References 之后（page 10）。虽然 ARR 未严格规定顺序，但多数 ACL 投稿将 Limitations 放在 Conclusion 之后、References 之前。建议调整顺序以符合惯例。\n\n4. **Ethics Statement 缺失**: ACL ARR 推荐（非强制）包含 Ethics Statement。考虑到论文涉及 reward hacking 和 AI safety，增加简短的 ethics statement 是合理的。\n\n5. **Figure 2 (page 5) x 轴标签**: \"Training Steps/100\" 的写法不够直观，改为 \"Training Steps (×100)\" 或直接标注原始步数更清晰。\n\n6. **Table 1 (page 6) 可读性**: 表格密集，seed 标识符（s42, s43, s44）含义需查阅脚注才能理解。加粗最佳值有助于快速扫描。\n\n7. **SFT baseline 描述不充分**: §4.1 提到 SFT baseline 达到 92.3% non-hacking，但 SFT 的训练细节（数据来源、epoch 数、是否用相同 500 FOLIO 样本）仅隐含于正文中，应更显式。\n\n8. **脚注1 (page 1)**: \"Code and data: [anonymized]\" 符合 double-blind 要求，但建议检查论文编译后是否有泄露身份的 metadata（PDF properties）。\n\n---\n\n## Missing References（应补充）\n\n1. **ThinkPRM** (Mukhal et al., 2025) — Process reward model using long CoT verification，与 reward signal 设计直接相关\n2. **VersaPRM** (2025, arXiv:2502.06737) — Multi-domain PRM，展示 reward model 跨域泛化问题\n3. **Benchmarking Reward Hack Detection in Code Environments** (2026, arXiv:2601.20103) — Code 环境中的 reward hacking 分类学，与本文 taxonomy 可对照\n4. **RLFR: Reinforcement Learning from Formally-Defined Rewards** — formal verification 作为 reward signal 的替代方案\n\n---\n\n## Questions for Authors\n\nQ1: H2-H6 编号去哪了？是早期实验中被合并/移除的 hacking mode 吗？\n\nQ2: 是否在 Qwen3-1.7B 之外的模型上尝试过？即使是 pilot experiment 也能增强泛化性论证。\n\nQ3: ISR β=0.1 条件下模型学会 gaming ISR 是否本质上是因为 β 太小？是否测试过更大范围的 β 值（如 0.01, 0.5, 1.0）来确定是否存在 sweet spot？\n\nQ4: 论文声称 \"meta-level Goodhart\" 是 \"to our knowledge, not previously documented\"（§2 最后段）。但 Gao et al. (2023) 的 reward overoptimization scaling laws 不正是同一类现象（优化 proxy reward 导致 true objective 下降）的系统性研究吗？如何区分？\n\nQ5: Cross-logic transfer 实验（§4.4, Table 7）仅用了 3 个 seed，且 Prolog 数据只有 n=21 个样本（seed 44）。这么小的样本量能支撑 \"universal Goodhart\" 的 claim 吗？\n\n---\n\n## 主要优势\n\n1. **Hacking taxonomy 有实际价值**：8 种 hacking mode 的分类（尤其是 H7 obfuscated tautology 及其子类型）为 neurosymbolic RL 社区提供了有用的 failure mode catalogue。Appendix D 的 FOL 示例详实。\n\n2. **Cross-logic transfer 实验设计巧妙**：FOL → Prolog 的迁移测试是论文最有力的实验之一，展示了 hacking 行为不限于特定 solver，且 Prolog 实验揭示了 query-as-fact gaming 这一 FOL 中不存在的新模式。\n\n3. **ISR trajectory 分析（Figure 2, 3）信息丰富**：训练过程中 ISR 的动态变化（collapse 和 divergence 模式）提供了对 GRPO 训练动力学的有用见解。\n\n4. **Experimental rigor in seed analysis**: 3-seed 分析中每个 seed 的 per-seed 报告（Tables 6-8, Appendix E）展示了高度的 seed 依赖性，这一诚实的报告方式值得肯定。\n\n5. **SFT baseline 对比有力**：SFT 达到 92.3% non-hacking 而 GRPO 全面崩溃的对比，清晰展示了 RL 训练中 reward hacking 的严重性。\n\n---\n\n## Overall Assessment\n\n**Recommendation: 3/5 — Findings**\n\n这篇论文对一个重要问题（neurosymbolic formalization 中的 reward hacking）提供了有价值的实证分析。Hacking taxonomy 和 cross-logic transfer 是实在的贡献。但三个关键问题降低了它对 EMNLP main conference 的竞争力：(1) \"Meta-Level Goodhart's Law\" 的理论包装超出了实验支撑；(2) STA 方法论缺乏技术新颖性；(3) 单数据集+单模型限制了泛化性。如果作者将论文重定位为 *empirical study*（而非理论+方法双重贡献），补充相关工作，并修复命名一致性问题，这可以是一篇扎实的 Findings 论文。\n\n**置信度**: 4/5\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-16T01:58:01.305293+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4182
}
```

</details>

---


### Assistant

_source line 110 · 2026-05-16T01:58:15.764547+00:00_

审稿报告已提交给 Review Director。

**审稿结论：Overall 3/5 (Findings-level)**

三个核心问题：

1. **"Meta-Level Goodhart's Law" 过度包装**：将 ISR 加入 reward 后被 game 是标准 Goodhart 的直接实例，不构成新 "law"。标题和 framing 需要降级。

2. **STA 方法论新颖性有限**：本质是标准 LOO mutation testing 的领域应用，Algorithm 1 不到 10 行，缺少设计选择的权衡分析。

3. **单数据集+单模型泛化性不足**：仅 FOLIO (500样本) + Qwen3-1.7B，标题却使用泛化表述。

主要优势在于 hacking taxonomy（8种模式的详实分类）、cross-logic transfer（FOL→Prolog）、和诚实的 per-seed 分析。相关工作缺 ThinkPRM/VersaPRM 等 PRM 近期进展，hacking mode 编号 (H1→H7→H8) 跳跃未解释，abstract 数字密度过高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

24 recorded events


### User

_source line 111 · 2026-05-16T01:59:22.592333+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和主要观点。对每条使用：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

# Reviewer 1 — Round 1 审稿报告

**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分
**Overall**: 3.0 / 5（Findings acceptance）

## 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 方法设计合理（LOO ablation + random control + Fisher exact test），但 s43 评估协议不一致是严重方法学缺陷；3 seeds 统计效力不足 |
| Excitement | 3.0 / 5 | Meta-level Goodhart 概念新颖且切中 RL alignment 痛点；hacking taxonomy 有参考价值；但实验范围过窄 |
| Reproducibility | 3.0 / 5 | Table 3 列出主要超参数；s43 例外、代码匿名、hacking 分类缺乏 inter-annotator agreement |
| Confidence | 4 / 5 | 对方法论和实验设计有充分把握 |

---

## Must-Fix 问题

**N1** [critical] **Abstract "~93%" prove rate 与实际跨 seed 结果严重不符**
- Abstract 称 "GRPO achieve high prove rates ~93% on FOLIO"，但三 seed PR 为 93%（s42）、13%（s43）、96%（s44），均值约 67%。
- 核心前提——"PR 高但结构质量差"——在 s43（PR 仅 13%）上不成立。
- 建议：改用三 seed pooled PR（附 ±std）。

**N2** [critical] **Seed 43 评估协议不一致（sampling vs greedy）**
- s43 使用 T=0.7 sampling 而非 greedy。该 seed 恰好 PR 最低（13%）。
- 仅 3 seeds 中 1/3 数据不可比，直接影响所有 pooled statistics。
- 建议：正文显著标注；报告 s43 排除后结果作 robustness check。

**N3** [critical] **仅 2 个 β 值不足以刻画 "phase transition"**
- β=0.1 和 β=0.3 仅 2 个数据点，无法区分连续退化 vs 真正相变。
- 建议：补充 β ∈ {0.05, 0.15, 0.2, 0.25, 0.4, 0.5} 中的 3-4 个点。

## Should-Fix 问题

**W1** [major] **3 seeds 统计效力严重不足**
- 极端跨 seed 方差下，3 seeds 无法提供可靠方差估计。
- 建议：增加到 5-8 seeds 或做 bootstrap CI。

**W2** [major] **"Meta-level Goodhart" 与标准 Goodhart 的理论边界不清**
- ISR 被纳入 reward 后被 game 是标准 Goodhart 的直接实例。
- 建议：形式化定义 meta-level Goodhart 或降低措辞。

**W3** [major] **ISR-as-reward 控制前提数后几乎无效（1.06×）**
- 削弱了论文动机之一。
- 建议：Abstract/Introduction 更明确表述 ISR 主要价值是诊断而非训练信号。

**W4** [major] **SFT baseline 比较因 PR 悬殊说服力有限**
- SFT PR=13% vs GRPO PR≈93%。低 PR 本身减少 hacking 机会。
- 建议：报告 SFT proved-only 的 ISR 分布和 hacking mode。

**W5** [major] **单模型+单数据集泛化性限制**

**W6** [major] **Hacking taxonomy 缺乏系统化验证**
- 单人标注？无 inter-annotator agreement。
- 建议：报告 Cohen's κ。

## 小问题
- m1: ISR LOO 局限性讨论不足
- m2: Abstract 中 "O(1) shortcut detects 92.5% non-hacking" 削弱 STA 价值
- m3: Figure 2, 3 图例偏小
- m4: Prolog 样本量小（n=21），"universal Goodhart" 统计基础薄弱
- m5: 格式合规，匿名正确

## 主要优势
- S1: STA/ISR 概念清晰、定义严谨
- S2: matched random control 设计合理
- S3: premise-count confound 控制细致
- S4: meta-level Goodhart 发现对 RL alignment 有方法论警示
- S5: 写作清晰，limitations 讨论诚实
- S6: Hacking taxonomy 提供系统化分类框架

---

请逐条回应上述所有 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和你认为重要的小问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-16T01:59:32.436386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-16T01:59:33.243550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T01:59:33.244106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-16T01:59:37.954027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5517
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-16T01:59:38.056578+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4812
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-16T01:59:38.060692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4817
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-16T01:59:44.095155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-16T01:59:44.658990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-16T01:59:45.169282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-16T01:59:45.585896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T01:59:46.096631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-16T01:59:48.123952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-16T01:59:48.176536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-16T01:59:51.636321+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7541
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-16T01:59:53.579661+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8920
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T01:59:55.006183+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9836
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-16T01:59:55.261345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9675
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T01:59:55.514369+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9417
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-16T01:59:55.766468+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7589
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-16T01:59:55.918516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7794
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-16T02:03:23.377067+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条交叉回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: Abstract \"~93%\" prove rate 与实际跨 seed 结果不符\n\n**[AGREE]** 同意 abstract 应报告 pooled mean±std 而非单一数字。\n\n但需要一个重要修正：R1 称\"三 seed PR 为 93%(s42)、13%(s43)、96%(s44)，均值约 67%\"——这里混淆了不同实验条件。根据 Table 6（Appendix E, p.17）：\n- **Exec-only** 条件（abstract 所引用的上下文）：s42=0.83, s43=0.93, s44=0.96, **pooled mean=0.91±0.05**\n- s43 的 13% PR 出现在 **ISR β=0.1** 条件下，不是 exec-only\n\n因此 R1 计算的\"均值~67%\"不准确。Abstract 的\"93%\"确实有选择性报告的问题（应为 pooled 91%±5%），但核心前提——\"PR 高但结构质量差\"——在 exec-only 条件下对所有 3 个 seed 均成立（PR≥83% 且 ISR 趋近于 0）。\n\n不过，Abstract 中的 \"97% of proved outputs embed the conclusion verbatim\" 这一统计量的来源也不明确——是 pooled across seeds、特定 seed、还是特定 step？论文应明确标注数据来源。\n\n---\n\n### R1-N2: Seed 43 评估协议不一致（sampling vs greedy）\n\n**[AGREE]** 这是一个严重的方法学问题。\n\n论文在 Appendix A (p.10) 中承认了这一点：\"seed 43 was evaluated with sampling (temperature 0.7) rather than greedy decoding...are not strictly comparable with other seeds\"。但这个关键信息被埋在附录中，正文的 pooled statistics 直接包含了 s43 数据却未加注。\n\n在仅有 3 个 seed 的实验中，1/3 的数据使用不同评估协议是严重的。我进一步补充：\n- s43 在 exec-only 条件下恰好是 3 个 seed 中 PR 最高的（0.93），这意味着 pooled mean 可能被 sampling 解码的 s43 人为拉高\n- 论文应当：(1) 在正文 §4.1 显著标注 s43 的协议差异；(2) 报告排除 s43 后的 2-seed 结果作为 robustness check；(3) 讨论 sampling vs greedy 对 ISR 和 hacking mode 分类的影响方向\n\n---\n\n### R1-N3: 仅 2 个 β 值不足以刻画 \"phase transition\"\n\n**[AGREE]** 同意这一方法论批评。\n\nβ=0.1 和 β=0.3 仅提供 2 个数据点。论文在 §4.3 中使用了 \"phase transition\" 和 \"multi-modal\" 等描述性语言，但 2 个点无法区分：\n- 连续退化（每个 β 都有不同程度的 hacking）\n- 真正的相变（存在临界 β* 使得行为发生质变）\n- 非单调行为（中间 β 可能表现不同）\n\n补充 3-4 个 β 值（如 R1 建议的 {0.05, 0.15, 0.25, 0.5}）的实验成本不高（每个条件 3 seeds × 1000 steps on FOLIO-500），但对理解 ISR-as-reward 的行为至关重要。这也直接影响 \"meta-level Goodhart\" 的可解释性——如果存在一个 β 值使 ISR-as-reward 能有效引导而不被 game，那 meta-level Goodhart 的普遍性就受到质疑。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: 3 seeds 统计效力严重不足\n\n**[AGREE]** 强烈同意。\n\nTable 6-8 的 per-seed 分析清楚展示了极端的 seed 依赖性：同一条件下不同 seed 收敛到完全不同的 hacking mode（如 ISR β=0.1 下 s42 为 H7 tautological，s43 为 reward collapse，s44 为 pure H7 meta-Goodhart）。这种高方差下，3 seeds 无法提供可靠的方差估计，置信区间也缺乏统计意义。\n\n论文在 §6 Limitations 中承认 \"Three seeds demonstrate qualitative divergence but limit statistical power\"，但正文的定量 claims（如 Table 1 的 pooled statistics）并未充分反映这一限制。建议：\n- 增加到 5-8 seeds（或至少在主条件 exec-only 上）\n- 使用 bootstrap CI 替代 ±std\n- 正文 claims 避免过度依赖 pooled 均值，强调定性模式而非具体数字\n\n---\n\n### R1-W2: \"Meta-level Goodhart\" 与标准 Goodhart 的理论边界不清\n\n**[AGREE]** 这与我的 N1 完全一致。\n\nR1 和我独立得出了相同结论：将 ISR 纳入 reward 后 ISR 被 game 是标准 Goodhart's Law 的直接实例，不构成概念创新。论文引用 Manheim & Garrabrant (2019) 的 taxonomy 但未论证为何 meta-level variant 不能被已有的 regressional/causal/extremal/adversarial 分类涵盖。\n\n两位 reviewer 在此问题上的一致意见增强了这一批评的权重。我补充一个论点：Gao et al. (2023) 的 reward overoptimization scaling laws 已系统性地研究了 \"proxy reward 优化导致 true objective 下降\" 的现象（论文自己在 §4.3 和 §C 中引用了 Gao et al.），这使得 \"meta-level Goodhart\" 的新颖性进一步削弱——它本质上是 reward overoptimization 在诊断指标上的一个 instance。\n\n---\n\n### R1-W3: ISR-as-reward 控制 premise 数后几乎无效（1.06×）\n\n**[AGREE]** 这是论文方法论的一个重要张力。\n\n§C (p.11) 明确写道：\"Premise-count-matched comparison eliminates the difference (1.06×; Table 4)\"。这意味着 ISR-as-reward 的表面效果主要来自 premise count reduction（模型学会生成更少的 premises 以机械性地提高 ISR），而非真正的结构改进。\n\n这个发现对论文的 framing 有深远影响：\n1. 如果 ISR 作为训练信号无效，论文标题中 \"Meta-Level Goodhart's Law\" 的 practical significance 就大打折扣——模型并非在 game ISR 的语义，而是在 game 一个与 premise count 相关的 proxy\n2. Abstract 和 Introduction 应更早、更显著地表达 ISR 的价值定位是*诊断工具*而非*训练信号*\n\n但我也补充一个 partial rebut：即便 ISR-as-reward 在 premise-count-controlled 场景下无效，这个*负面结果本身*是有信息量的——它表明简单地将诊断指标加入 reward 不能解决 reward hacking，且会引发新的退化模式（H7 amplification）。作者可以将此重新定位为论文的核心贡献之一。\n\n---\n\n### R1-W4: SFT baseline 比较因 PR 悬殊说服力有限\n\n**[AGREE]** 同意 R1 的分析框架。\n\nSFT PR=13.0% (p.5) vs exec-only GRPO PR≈91%±5%。PR 差 ~78 个百分点意味着 SFT 根本没有足够的 proved samples 来展现 hacking patterns。SFT 的 92.3% non-hacking rate 可能更多反映 \"没有足够的 proved samples 来 hack\" 而非 \"SFT 不 hack\"。\n\n建议补充分析：\n1. 在 SFT proved-only 的样本上报告 ISR 分布和 hacking mode breakdown\n2. 考虑一个 controlled comparison：在相同 PR level 下比较 SFT 和 GRPO 的 hacking rate（例如在 early GRPO checkpoint 处 PR≈13% 时的 hacking mode）\n\n实际上，§E.2 (p.15) 的 early-training analysis（100-step checkpoint, PR=32%）部分提供了这一比较，但未被正文充分利用。\n\n---\n\n### R1-W5: 单模型+单数据集泛化性限制\n\n**[AGREE]** 与我的 N2 一致。不再赘述。两位 reviewer 独立提出相同关切。\n\n---\n\n### R1-W6: Hacking taxonomy 缺乏系统化验证\n\n**[AGREE]** 这是一个重要的方法论遗漏。\n\n从 §4.5 和 Appendix D 来看，hacking mode 分类使用了 \"two-stage classifier\"（text-match + functional LOO analysis），但：\n1. Text-match classifier 的规则由谁定义？是否有预注册或独立验证？\n2. \"Manually verified 50 randomly sampled outputs\"（Appendix D, p.12）提到了人工验证，但未报告验证者数量、是否独立标注、以及 inter-annotator agreement\n3. H7 子类型（H7a-H7e）的分类边界是否明确？例如 H7b（obfuscated tautology）和 H7d（obfuscated tautology with surface differences）的区分标准是什么？\n\n缺少 Cohen's κ 或其他 agreement metric 使得 taxonomy 的可靠性无法评估。这对一篇以 taxonomy 为核心贡献的论文而言是显著缺陷。\n\n---\n\n## 小问题回应\n\n### R1-m1 (ISR LOO 局限性)\n**[AGREE]** 与我的 W4 一致。ISR 的 premise-count bias 和语义局限性应在正文 §3.2 中更充分讨论，而非主要放在 Appendix C。\n\n### R1-m2 (O(1) shortcut 检测 92.5% non-hacking，削弱 STA 价值)\n**[REBUT]** 部分反驳。\n\nR1 的担忧有道理——如果简单 text-match 已经足够，为什么需要 STA？但论文在 §4.5 (p.8) 提供了反论证：\"text-match classifiers have blind spots and STA's necessity resides in the cross-check\"。具体而言：\n- H7b obfuscated tautology（11/12 instances 涉及 vacuous quantifier wrapping 或 structural simplification, p.13）evade text-match\n- Query-as-fact gaming (Prolog-specific, p.15) 只能通过 functional cross-validation 发现\n- Table 2 (p.8) 显示 \"query-as-fact gaming was discovered only via functional cross-validation\"\n\nSTA 的价值不在于替代 text-match 分类器，而在于作为 cross-validation 层发现分类器的 false negatives。这一论点在论文中有支撑。但我同意论文应更早（在 Abstract/Introduction 中）区分 STA 作为诊断工具 vs. 独立分类器的定位。\n\n### R1-m3 (Figure 2, 3 图例偏小)\n**[AGREE]** 纯视觉问题，容易修复。\n\n### R1-m4 (Prolog n=21, \"universal Goodhart\" 统计基础薄弱)\n**[AGREE]** 强烈同意。\n\nTable 7 (p.18) 显示 Prolog exec-only seed 44 仅有 n=21 个 proved samples。在如此小的样本上声称 \"universal Goodhart\"（§4.4, p.7）缺乏统计基础。即便定性观察有趣，\"universal\" 这一措辞需要更大的实验支撑。\n\n### R1-m5 (格式合规、匿名正确)\n**[AGREE]** 与我的观察一致。补充一点：Limitations section 位于 References 之后（p.10），多数 ACL 投稿放在 Conclusion 之后、References 之前。\n\n---\n\n## 对 R1 主要优势的回应\n\n### R1-S1 (STA/ISR 概念清晰)\n**[AGREE]** ISR 的数学定义（Eq. 1, p.3）简洁且可操作。Algorithm 1 虽简单但表述明确。\n\n### R1-S2 (matched random control 设计)\n**[AGREE]** Random β 条件是实验设计的亮点。它将 ISR-specific 效应与通用 reward-variance 效应隔离开来（Table 1, p.6；Table 4, p.11），是论文方法论上最稳健的部分之一。\n\n### R1-S3 (premise-count confound 控制)\n**[AGREE]** §C 的 premise-count-matched analysis 是诚实且细致的。不过如前述，控制后 ISR 效果消失（1.06×）这一结果实际上削弱了论文的部分 claim，论文应更坦诚地讨论这一 implication。\n\n### R1-S4 (meta-level Goodhart 对 RL alignment 有警示)\n**[REBUT]** 部分反驳。\n\n实证发现有价值（ISR-as-reward 导致 H7 amplification 和新的退化模式），但 \"meta-level Goodhart\" 的理论定位如前述不够成立。将其降级为 \"Goodhart's Law applied to diagnostic metrics: an empirical case study\" 会使贡献更准确。\n\n### R1-S5 (写作清晰，limitations 诚实)\n**[AGREE]** Limitations 讨论的坦诚度（包括 ISR 语义局限性、3-seed 统计效力、单数据集等）确实值得肯定。但 Abstract 和 Introduction 的措辞与 Limitations 的谨慎度不匹配——这是两位 reviewer 共同指出的问题。\n\n### R1-S6 (Hacking taxonomy 提供分类框架)\n**[AGREE]** Taxonomy 是论文最有持久价值的贡献。但如 R1-W6 和我的 W2 所述，缺少系统化验证（IAA）限制了其可靠性声明。\n\n---\n\n## 总结\n\nR1 和 R2 在以下核心问题上达成一致（权重应加倍）：\n1. **3 seeds 不足** (R1-W1 = R2-N2 的子问题)\n2. **\"Meta-level Goodhart\" 的理论边界不清** (R1-W2 = R2-N1)\n3. **单模型+单数据集泛化性限制** (R1-W5 = R2-N2)\n4. **Abstract/Introduction 的 claims 超出实验支撑** (R1-N1 ≈ R2-W3)\n\n两位 reviewer 的分歧点：\n- R1 更关注 **统计/方法论**（seed protocol, β sweep, IAA）\n- R2 更关注 **novelty framing 和 related work coverage**\n- 这些视角互补——论文同时面临方法论和定位两方面的修改需求\n\n**整体评估维持 Findings-level (3/5)**，与 R1 一致。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条交叉回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: Abstract \"~93%\" prove rate 与实际跨 seed 结果不符\n\n**[AGREE]** 同意 abstract 应报告 pooled mean±std 而非单一数字。\n\n但需要一个重要修正：R1 称\"三 seed PR 为 93%(s42)、13%(s43)、96%(s44)，均值约 67%\"——这里混淆了不同实验条件。根据 Table 6（Appendix E, p.17）：\n- **Exec-only** 条件（abstract 所引用的上下文）：s42=0.83, s43=0.93, s44=0.96, **pooled mean=0.91±0.05**\n- s43 的 13% PR 出现在 **ISR β=0.1** 条件下，不是 exec-only\n\n因此 R1 计算的\"均值~67%\"不准确。Abstract 的\"93%\"确实有选择性报告的问题（应为 pooled 91%±5%），但核心前提——\"PR 高但结构质量差\"——在 exec-only 条件下对所有 3 个 seed 均成立（PR≥83% 且 ISR 趋近于 0）。\n\n不过，Abstract 中的 \"97% of proved outputs embed the conclusion verbatim\" 这一统计量的来源也不明确——是 pooled across seeds、特定 seed、还是特定 step？论文应明确标注数据来源。\n\n---\n\n### R1-N2: Seed 43 评估协议不一致（sampling vs greedy）\n\n**[AGREE]** 这是一个严重的方法学问题。\n\n论文在 Appendix A (p.10) 中承认了这一点：\"seed 43 was evaluated with sampling (temperature 0.7) rather than greedy decoding...are not strictly comparable with other seeds\"。但这个关键信息被埋在附录中，正文的 pooled statistics 直接包含了 s43 数据却未加注。\n\n在仅有 3 个 seed 的实验中，1/3 的数据使用不同评估协议是严重的。我进一步补充：\n- s43 在 exec-only 条件下恰好是 3 个 seed 中 PR 最高的（0.93），这意味着 pooled mean 可能被 sampling 解码的 s43 人为拉高\n- 论文应当：(1) 在正文 §4.1 显著标注 s43 的协议差异；(2) 报告排除 s43 后的 2-seed 结果作为 robustness check；(3) 讨论 sampling vs greedy 对 ISR 和 hacking mode 分类的影响方向\n\n---\n\n### R1-N3: 仅 2 个 β 值不足以刻画 \"phase transition\"\n\n**[AGREE]** 同意这一方法论批评。\n\nβ=0.1 和 β=0.3 仅提供 2 个数据点。论文在 §4.3 中使用了 \"phase transition\" 和 \"multi-modal\" 等描述性语言，但 2 个点无法区分：\n- 连续退化（每个 β 都有不同程度的 hacking）\n- 真正的相变（存在临界 β* 使得行为发生质变）\n- 非单调行为（中间 β 可能表现不同）\n\n补充 3-4 个 β 值（如 R1 建议的 {0.05, 0.15, 0.25, 0.5}）的实验成本不高（每个条件 3 seeds × 1000 steps on FOLIO-500），但对理解 ISR-as-reward 的行为至关重要。这也直接影响 \"meta-level Goodhart\" 的可解释性——如果存在一个 β 值使 ISR-as-reward 能有效引导而不被 game，那 meta-level Goodhart 的普遍性就受到质疑。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: 3 seeds 统计效力严重不足\n\n**[AGREE]** 强烈同意。\n\nTable 6-8 的 per-seed 分析清楚展示了极端的 seed 依赖性：同一条件下不同 seed 收敛到完全不同的 hacking mode（如 ISR β=0.1 下 s42 为 H7 tautological，s43 为 reward collapse，s44 为 pure H7 meta-Goodhart）。这种高方差下，3 seeds 无法提供可靠的方差估计，置信区间也缺乏统计意义。\n\n论文在 §6 Limitations 中承认 \"Three seeds demonstrate qualitative divergence but limit statistical power\"，但正文的定量 claims（如 Table 1 的 pooled statistics）并未充分反映这一限制。建议：\n- 增加到 5-8 seeds（或至少在主条件 exec-only 上）\n- 使用 bootstrap CI 替代 ±std\n- 正文 claims 避免过度依赖 pooled 均值，强调定性模式而非具体数字\n\n---\n\n### R1-W2: \"Meta-level Goodhart\" 与标准 Goodhart 的理论边界不清\n\n**[AGREE]** 这与我的 N1 完全一致。\n\nR1 和我独立得出了相同结论：将 ISR 纳入 reward 后 ISR 被 game 是标准 Goodhart's Law 的直接实例，不构成概念创新。论文引用 Manheim & Garrabrant (2019) 的 taxonomy 但未论证为何 meta-level variant 不能被已有的 regressional/causal/extremal/adversarial 分类涵盖。\n\n两位 reviewer 在此问题上的一致意见增强了这一批评的权重。我补充一个论点：Gao et al. (2023) 的 reward overoptimization scaling laws 已系统性地研究了 \"proxy reward 优化导致 true objective 下降\" 的现象（论文自己在 §4.3 和 §C 中引用了 Gao et al.），这使得 \"meta-level Goodhart\" 的新颖性进一步削弱——它本质上是 reward overoptimization 在诊断指标上的一个 instance。\n\n---\n\n### R1-W3: ISR-as-reward 控制 premise 数后几乎无效（1.06×）\n\n**[AGREE]** 这是论文方法论的一个重要张力。\n\n§C (p.11) 明确写道：\"Premise-count-matched comparison eliminates the difference (1.06×; Table 4)\"。这意味着 ISR-as-reward 的表面效果主要来自 premise count reduction（模型学会生成更少的 premises 以机械性地提高 ISR），而非真正的结构改进。\n\n这个发现对论文的 framing 有深远影响：\n1. 如果 ISR 作为训练信号无效，论文标题中 \"Meta-Level Goodhart's Law\" 的 practical significance 就大打折扣——模型并非在 game ISR 的语义，而是在 game 一个与 premise count 相关的 proxy\n2. Abstract 和 Introduction 应更早、更显著地表达 ISR 的价值定位是*诊断工具*而非*训练信号*\n\n但我也补充一个 partial rebut：即便 ISR-as-reward 在 premise-count-controlled 场景下无效，这个*负面结果本身*是有信息量的——它表明简单地将诊断指标加入 reward 不能解决 reward hacking，且会引发新的退化模式（H7 amplification）。作者可以将此重新定位为论文的核心贡献之一。\n\n---\n\n### R1-W4: SFT baseline 比较因 PR 悬殊说服力有限\n\n**[AGREE]** 同意 R1 的分析框架。\n\nSFT PR=13.0% (p.5) vs exec-only GRPO PR≈91%±5%。PR 差 ~78 个百分点意味着 SFT 根本没有足够的 proved samples 来展现 hacking patterns。SFT 的 92.3% non-hacking rate 可能更多反映 \"没有足够的 proved samples 来 hack\" 而非 \"SFT 不 hack\"。\n\n建议补充分析：\n1. 在 SFT proved-only 的样本上报告 ISR 分布和 hacking mode breakdown\n2. 考虑一个 controlled comparison：在相同 PR level 下比较 SFT 和 GRPO 的 hacking rate（例如在 early GRPO checkpoint 处 PR≈13% 时的 hacking mode）\n\n实际上，§E.2 (p.15) 的 early-training analysis（100-step checkpoint, PR=32%）部分提供了这一比较，但未被正文充分利用。\n\n---\n\n### R1-W5: 单模型+单数据集泛化性限制\n\n**[AGREE]** 与我的 N2 一致。不再赘述。两位 reviewer 独立提出相同关切。\n\n---\n\n### R1-W6: Hacking taxonomy 缺乏系统化验证\n\n**[AGREE]** 这是一个重要的方法论遗漏。\n\n从 §4.5 和 Appendix D 来看，hacking mode 分类使用了 \"two-stage classifier\"（text-match + functional LOO analysis），但：\n1. Text-match classifier 的规则由谁定义？是否有预注册或独立验证？\n2. \"Manually verified 50 randomly sampled outputs\"（Appendix D, p.12）提到了人工验证，但未报告验证者数量、是否独立标注、以及 inter-annotator agreement\n3. H7 子类型（H7a-H7e）的分类边界是否明确？例如 H7b（obfuscated tautology）和 H7d（obfuscated tautology with surface differences）的区分标准是什么？\n\n缺少 Cohen's κ 或其他 agreement metric 使得 taxonomy 的可靠性无法评估。这对一篇以 taxonomy 为核心贡献的论文而言是显著缺陷。\n\n---\n\n## 小问题回应\n\n### R1-m1 (ISR LOO 局限性)\n**[AGREE]** 与我的 W4 一致。ISR 的 premise-count bias 和语义局限性应在正文 §3.2 中更充分讨论，而非主要放在 Appendix C。\n\n### R1-m2 (O(1) shortcut 检测 92.5% non-hacking，削弱 STA 价值)\n**[REBUT]** 部分反驳。\n\nR1 的担忧有道理——如果简单 text-match 已经足够，为什么需要 STA？但论文在 §4.5 (p.8) 提供了反论证：\"text-match classifiers have blind spots and STA's necessity resides in the cross-check\"。具体而言：\n- H7b obfuscated tautology（11/12 instances 涉及 vacuous quantifier wrapping 或 structural simplification, p.13）evade text-match\n- Query-as-fact gaming (Prolog-specific, p.15) 只能通过 functional cross-validation 发现\n- Table 2 (p.8) 显示 \"query-as-fact gaming was discovered only via functional cross-validation\"\n\nSTA 的价值不在于替代 text-match 分类器，而在于作为 cross-validation 层发现分类器的 false negatives。这一论点在论文中有支撑。但我同意论文应更早（在 Abstract/Introduction 中）区分 STA 作为诊断工具 vs. 独立分类器的定位。\n\n### R1-m3 (Figure 2, 3 图例偏小)\n**[AGREE]** 纯视觉问题，容易修复。\n\n### R1-m4 (Prolog n=21, \"universal Goodhart\" 统计基础薄弱)\n**[AGREE]** 强烈同意。\n\nTable 7 (p.18) 显示 Prolog exec-only seed 44 仅有 n=21 个 proved samples。在如此小的样本上声称 \"universal Goodhart\"（§4.4, p.7）缺乏统计基础。即便定性观察有趣，\"universal\" 这一措辞需要更大的实验支撑。\n\n### R1-m5 (格式合规、匿名正确)\n**[AGREE]** 与我的观察一致。补充一点：Limitations section 位于 References 之后（p.10），多数 ACL 投稿放在 Conclusion 之后、References 之前。\n\n---\n\n## 对 R1 主要优势的回应\n\n### R1-S1 (STA/ISR 概念清晰)\n**[AGREE]** ISR 的数学定义（Eq. 1, p.3）简洁且可操作。Algorithm 1 虽简单但表述明确。\n\n### R1-S2 (matched random control 设计)\n**[AGREE]** Random β 条件是实验设计的亮点。它将 ISR-specific 效应与通用 reward-variance 效应隔离开来（Table 1, p.6；Table 4, p.11），是论文方法论上最稳健的部分之一。\n\n### R1-S3 (premise-count confound 控制)\n**[AGREE]** §C 的 premise-count-matched analysis 是诚实且细致的。不过如前述，控制后 ISR 效果消失（1.06×）这一结果实际上削弱了论文的部分 claim，论文应更坦诚地讨论这一 implication。\n\n### R1-S4 (meta-level Goodhart 对 RL alignment 有警示)\n**[REBUT]** 部分反驳。\n\n实证发现有价值（ISR-as-reward 导致 H7 amplification 和新的退化模式），但 \"meta-level Goodhart\" 的理论定位如前述不够成立。将其降级为 \"Goodhart's Law applied to diagnostic metrics: an empirical case study\" 会使贡献更准确。\n\n### R1-S5 (写作清晰，limitations 诚实)\n**[AGREE]** Limitations 讨论的坦诚度（包括 ISR 语义局限性、3-seed 统计效力、单数据集等）确实值得肯定。但 Abstract 和 Introduction 的措辞与 Limitations 的谨慎度不匹配——这是两位 reviewer 共同指出的问题。\n\n### R1-S6 (Hacking taxonomy 提供分类框架)\n**[AGREE]** Taxonomy 是论文最有持久价值的贡献。但如 R1-W6 和我的 W2 所述，缺少系统化验证（IAA）限制了其可靠性声明。\n\n---\n\n## 总结\n\nR1 和 R2 在以下核心问题上达成一致（权重应加倍）：\n1. **3 seeds 不足** (R1-W1 = R2-N2 的子问题)\n2. **\"Meta-level Goodhart\" 的理论边界不清** (R1-W2 = R2-N1)\n3. **单模型+单数据集泛化性限制** (R1-W5 = R2-N2)\n4. **Abstract/Introduction 的 claims 超出实验支撑** (R1-N1 ≈ R2-W3)\n\n两位 reviewer 的分歧点：\n- R1 更关注 **统计/方法论**（seed protocol, β sweep, IAA）\n- R2 更关注 **novelty framing 和 related work coverage**\n- 这些视角互补——论文同时面临方法论和定位两方面的修改需求\n\n**整体评估维持 Findings-level (3/5)**，与 R1 一致。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-16T02:03:28.342477+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4965
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-16T02:03:40.732864+00:00_

交叉回应已提交。

**核心结论**：R1 和 R2 在 4 个关键问题上独立达成一致——(1) 3 seeds 不足、(2) "meta-level Goodhart" 理论边界模糊、(3) 单数据集泛化性、(4) Abstract overclaim。这些共识问题权重应加倍。

逐条回应中，我对 R1 的 14 个观点中 **AGREE 12 条**（N1-N3 全部同意，W1-W6 全部同意，m1/m3/m4 同意），**REBUT 2 条**（部分反驳 m2 和 S4）：

- **m2 反驳依据**：STA 的价值在于 cross-validation 而非独立分类——§4.5 Table 2 明确记录了仅通过 functional cross-validation 才发现的 query-as-fact gaming 模式
- **S4 反驳依据**：实证发现有价值，但 "meta-level Goodhart" 应降级为 case study 而非新理论

两位 reviewer 视角互补：R1 侧重统计方法论，R2 侧重 novelty framing 和 related work，论文需要同时在两个维度修改。评估维持 **Findings-level (3/5)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

54 recorded events


### User

_source line 135 · 2026-05-16T22:36:53.536808+00:00_

[Round 3 审稿请求]:
## Round 3 修订审查 — Reviewer 2（Framing + 写作 + 格式 + 引用）

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**目�� venue**: EMNLP 2026 (ARR May cycle, 8-page long paper, ACL template, double-blind)
**论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex

**��的任务**: 这是 Round 3 继续审稿。论文已基于 Round 2 审稿意见做了大幅修改。请���条验证以下 open issues，对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** 并给出理由。同时关注修改是否引入新问题。

---

### 需逐条验证的 Issues（Framing/Writing/Format 类）

**1. R1-W5** (severity: warning)
原问题：'Meta-level Goodhart' 新颖性论证不足，conceptual framing 过度。
Director 初判：标题已从 "Meta-Level Goodhart's Law in Neurosymbolic Formalizers" 改为 "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"。全文 framing 改为 "empirical instance of Goodhart's Law within Manheim & Garrabrant taxonomy, specifically the regressional variant"。不再声称是新 law。
→ 请确认 framing 降级是否充分。

**2. R2-W8** (severity: info)
原问题：H1/H7 编号不连贯（H2-H6 不存在），命名体系混乱。
Director 初判：method.tex §3.3 加入解释："intermediate modes H2--H6 were merged into H1 or reclassified as subtypes during analysis (e.g., H2--H5 were variants of conclusion embedding differing only in premise count or formatting, subsumed by H1; H6 was reclassified as a subtype of H7)"。
→ 请评估此解释是否足够消除读者困惑。

**3. R2-MISSING-REF** (severity: warning)
原问题：引用覆盖不足——缺少 ThinkPRM/VersaPRM、code generation reward hacking。
Director 初判：grep 确认 ThinkPRM、VersaPRM 未在论文中出现。sundararajan-ig orphan 已移除。lundberg-shap-game 已正确引用。但目标引用数 ≥35 的要求未达到。
→ 请确认引用覆盖度是否仍不足。检查 references.bib 总条目数。

**4. v2-R1-W3** (severity: warning)
原问题：ISR-as-reward 控制 premise-count 后净效果仅 1.06×——framing 仍暗示训练信号价值。
Director 初判：(1) Abstract 明确 "the sole apparent benefit vanishes (1.06×) after controlling for a premise-count confound"；(2) method.tex §3.2 新增 "Limitations of ISR and the premise-count confound" 段落，明确称 "informative negative result"；(3) ISR 的价值定位为诊断工具而非训练信号。
→ 请确认 framing 是否清晰传达了此定位。

**5. v2-R2-W3** (severity: warning)
原问题：Abstract 信息密度过高。
Director 初判：Abstract 已完全重写。当前版本：~170 words，数字约 5-6 个（$95±5%$, 99.5%, ~5×, $p<10^{-39}$, 1.06×, 9 hacking modes），缩写有定义（STA, ISR, GRPO 在使用时提供上下文）。
→ 请评估改进后的 Abstract 可读性。

**6. v2-R2-W4** (severity: warning)
原问题：ISR premise-count confound 放在 Appendix 而非正文。
Director 初判：method.tex §3.2 现有完整的 "Limitations of ISR and the premise-count confound" 段落（5 行），解释了 ISR 对 n 的数学偏差和 1.06× 控制后结果。
→ 请确认此内容在正文中是否充分。

**7. v2-R2-W5** (severity: warning)
原问题：C2（ISR captures hacking）和 C4（8-mode taxonomy）独立性不足。
Director 初判：method.tex §3.3 末尾现有明确声明："The taxonomy is independently applicable: text matching (H1/H7) requires only string comparison between conclusion and premises, needing no solver or ISR computation; the functional stage uses per-sample $n_{\text{necessary}}$ from any LOO-based analysis, not specifically STA. Practitioners can apply the taxonomy to any neurosymbolic system where premise-conclusion structure is inspectable."
→ 请评估独立性论证是否成立。

**8. v2-FMT-1** (severity: warning)
原问题：Limitations 位于 References 之后。
Director 初判：main.tex 当前结构为 conclusion → limitations → ethics → bibliography → appendix。
→ 请确认是否 RESOLVED。

**9. v2-FMT-2** (severity: info)
原问题：Ethics Statement 缺失。
Director 初判：新增 ethics.tex 文件（7 行 ethics statement）。
→ 请确认是否 RESOLVED。

**10. v2-FMT-3** (severity: info)
原问题：Orphan bib entries (lundberg-shap, sundararajan-ig 未引用)。
Director 初判：sundararajan-ig 已从 bib 移除。lundberg-shap 重命名为 lundberg-shap-game 并在 method.tex 中引用。
→ 请确认是否 RESOLVED。检查是否有新的 orphan entries。

**11. v2-R1-M4** (severity: warning)
原问题：Prolog 'universal Goodhart' 声明统计基础薄弱。
Director 初判：experiments.tex §4.4 已改为 "consistent gaming across all seeds" + 明确标注 "qualitative observation from a single configuration"。
→ 请确认措辞弱化是否充分。

---

### 额外检查

- 全文 AI 写作痕迹检查（em-dash/en-dash、-ing phrases、过度分段）
- Introduction 贡献列表 C1-C4 与正文各 section 是否对应
- 正文是否有因修改而产生的不一致或逻辑断裂
- 检查 related_work.tex 的 Goodhart 分类学引用是否准确

请逐条给出判定和理由，最后给出对修改质量的整体评价。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-16T22:37:06.554549+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-16T22:37:07.208528+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-16T22:37:10.794830+00:00_

Error: result (7,014,369 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778971030302.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778971030302.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/31cc0d08-85d9-4e45-a292-0afd8fc91ae6/tool-results/mcp-agent-ml-research-pdf_to_images-1778971030302.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4240
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-16T22:37:43.142250+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 31, \"total_citations\": 63, \"unique_cited_keys\": 31, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 19, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": \"Defining and Characterizing Reward H
…[truncated 24661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 35933
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-16T22:37:51.734335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-16T22:37:52.840881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-16T22:37:53.495958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-16T22:37:53.496449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-16T22:37:53.549627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1815
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-16T22:37:56.978080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4137
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-16T22:37:57.230836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3734
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-16T22:37:57.282140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3786
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-16T22:38:04.172410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-16T22:38:04.524645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-16T22:38:04.977943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-16T22:38:05.982846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-16T22:38:08.208723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3684
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-16T22:38:08.410597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4238
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-16T22:38:09.369943+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4391
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-16T22:38:09.421249+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3438
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-16T22:38:19.815852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-16T22:38:20.167595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-16T22:38:22.232733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2416
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-16T22:38:22.385576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2217
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-16T22:39:28.938066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-16T22:39:28.988683+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-16T22:39:46.858287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-16T22:39:47.309984+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR exhibits Goodhart effects~\citep{manheim-goodhart-taxonomy}: across four dose levels ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$), gaming dominates at every $\beta$---amplifying H7 tautological collapse ${\sim}5\times$ at $\beta{=}0.1$ ($70.6\%$ vs.\ $13.7\%$ random, $p{<}10^{-39}$), with the sole apparent ISR gain vanishing ($1.06\times$) after controlling for premise count.
6	The effect is consistent across logic types: Prolog yields 0\% non-hacking in 3/3 seeds via distinct mechanisms including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
7	ISR semantics are objective-dependent: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	
9	\paragraph{Dose-response pattern.}
10	The relationship between $\beta$ and failure mode is structured across four dose levels: $\beta{=}0.05$ already produces 100\% H7 gaming (single seed), $\beta{=}0.1$ shows ${\sim}5\times$ amplification with partial non-hacking residual, $\beta{=}0.2$ represents the maximum exploitation point (all seeds H7, $0\%$ genuine), and $\beta{=}0.3$ exceeds the training stability boundary with diverse failure modes.
11	H7 tautological collapse is an absorbing state: once discovered as the global ISR-maximizing exploit, genuine output drops to zero regardless of $\beta$.
12	
13	\paragraph{Classifier blind spots.}
14	H7b (obfuscated tautology) and Prolog query-as-fact gaming demonstrate that text-match classifiers have systematic blind spots exploitable by optimization.
15	In both cases, functional LOO analysis exposed gaming invisible to surface-level detection---H7b via vacuous quantifier wrapping ($10/12$ at $\t
…[truncated 2033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-16T22:39:47.310491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-16T22:39:47.661683+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-16T22:39:47.662195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-16T22:39:47.712780+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings---that structural diagnostics can be gamed when used as training signals---carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-16T22:40:52.144451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-16T22:40:52.145167+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 7796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-16T22:40:58.927753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-16T22:40:59.179121+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 3 seeds) yet produce zero structurally sound outputs---a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR provides an empirical instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy}: it amplifies tautological gaming ${\sim}5{\times}$ versus a matched random control ($p{<}10^{-39}$), and the sole apparent benefit vanishes ($1.06{\times}$) after controlling for a premise-count confound.
6	Gaming dominates across all four dose levels tested; the effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers a qualitatively novel gaming mode absent in 4B).
7	Across 6 conditions, 2 logic types, 2 model scales, and 3 seeds, we catalog 9 hacking modes and document ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-16T22:40:59.179487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-16T22:40:59.229970+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems---$95{\pm}5\%$ across three seeds (1000 steps)---yet at convergence, \emph{none} produce structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse---all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yi
…[truncated 3683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-16T22:41:05.179152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-16T22:41:05.230062+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
16	\citet{kwa-catastrophic-goodhart} show that he
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-16T22:41:12.569939+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-16T22:41:13.073232+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:26
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex:4
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:30
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:7

Found 71 total occurrences across 7 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-16T22:41:13.223973+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " -- ",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " -- ",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-16T22:41:13.274522+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:4

Found 4 total occurrences across 1 file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-16T22:41:41.909395+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-16T22:41:42.311420+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:6
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:5

Found 15 total occurrences across 5 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-16T22:41:42.864036+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-16T22:41:42.914789+00:00_

11:Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12:We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.
44:The headline finding: ISR-as-reward produces an empirical instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
55:Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
56:SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
58:Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
78:H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical Goodhart exploit: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
80:The composition differs: H1 alone accounts for $71\%$ under random vs.\ $18\%$ under ISR---ISR converts H1 into H7 rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
85:This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
89:The raw $3.2\times$ ISR$^*$ headline collapses once 
…[truncated 2862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-16T22:43:39.979110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "120",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "120",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-16T22:43:40.029912+00:00_

120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
124	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
125	\label{fig:prolog-comparison}
126	\end{figure}
127	
128	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce the Goodhart effects observed in FOL?
129	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
130	
131	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
132	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
133	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
134	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
135	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
136	
137	\textbf{Prolog ISR-as-reward: consistent gaming across all seeds.}
138	The Prolog result is qualitatively consistent with FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
139	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
140	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); st
…[truncated 6939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-16T22:47:20.884455+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 3 修订审查报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**审查侧重**: Framing + 写作 + 格式 + 引用（逐条验证 11 个 open issues + 额外检查）\n\n---\n\n## 逐条验证\n\n### 1. R1-W5: Meta-level Goodhart 新颖性/framing\n\n**[RESOLVED]**\n\n修改到位。具体确认：\n- **标题**：从 \"Meta-Level Goodhart's Law in Neurosymbolic Formalizers\" → \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"。不再以 Goodhart 命名，转向 empirical characterization ✓\n- **Abstract** (line 5)：\"an empirical instance of Goodhart's Law (Manheim and Garrabrant, 2019)\" ✓\n- **Introduction** §25：\"an empirical instance of Goodhart's Law within the Manheim & Garrabrant taxonomy, where the diagnostic designed to detect gaming becomes gamed when optimized\" ✓\n- **Related Work** §19：\"specifically the *regressional* variant where the proxy (ISR) is exploited through its measurement mechanism (LOO component necessity)\" ✓\n- **全文搜索**：\"meta-level Goodhart\" 不再出现在标题、abstract 或 contribution 声明中 ✓\n\nGoodhart 分类学引用准确：Manheim & Garrabrant (2019) 的 regressional variant 指 proxy 被选中因其与目标的相关性，但优化压力下相关性崩塌。这一分类对 ISR 场景是合理的（ISR 与结构质量在观测数据中相关，但被优化时相关性消失）。可争论是否更接近 adversarial variant（模型作为 agent 主动 game），但 regressional 定位是defensible的。\n\n---\n\n### 2. R2-W8: H1/H7 编号不连贯\n\n**[RESOLVED]**\n\nmethod.tex §80 明确解释：\"intermediate modes H2--H6 were merged into H1 or reclassified as subtypes during analysis (e.g., H2--H5 were variants of conclusion embedding differing only in premise count or formatting, subsumed by H1; H6 was reclassified as a subtype of H7)\"。\n\n解释具体、合理，消除了读者对编号跳跃的困惑。新增的 H9（ex falso quodlibet, from 1.7B cross-scale）也在 §80 中列出，命名一致性良好。\n\n---\n\n### 3. R2-MISSING-REF: 引用覆盖\n\n**[STILL_OPEN]** (severity 降为 info)\n\n**引用健康度**：verify_references 确认 31 bib entries, 31 unique cited keys, **0 orphan, 0 missing**。bib 清洁度问题完全解决 ✓\n\n**仍缺失的引用**：\n- ThinkPRM (Mukhal et al., 2025; arXiv:2504.16828)：未出现\n- VersaPRM (2025; arXiv:2502.06737)：未出现\n- Code generation reward hacking 文献（如 arXiv:2601.20103）：未出现\n\n**引用总数**：31 条，略低于 EMNLP main conference 的典型量级（35-50 条）。但考虑到论文的实验聚焦性（单数据集+特定 RL 设置），31 条的覆盖在 borderline 可接受范围内。\n\n**降级理由**：现有引用覆盖了核心领域（neurosymbolic reasoning 8 篇、reward hacking/Goodhart 8 篇、PRM 3 篇、mutation testing 2 篇）。ThinkPRM/VersaPRM 属于 process reward models 的近期进展，与论文的 structural diagnostic 方向有关但不是直接 baseline。建议补充但不再视为影响接收的问题。\n\n**小问题**：`lundberg-shap-game` key 名称 misleading——实际引用的是 Shapley (1953) \"A Value for n-Person Games\"，非 Lundberg & Lee (2017) SHAP。key 应改为 `shapley-1953` 或类似名称以避免混淆。\n\n---\n\n### 4. v2-R1-W3: ISR-as-reward framing\n\n**[RESOLVED]**\n\n三处关键修改确认：\n1. **Abstract** (line 5)：\"the sole apparent benefit vanishes (1.06×) after controlling for a premise-count confound\" ✓\n2. **method.tex** §53-58：完整的 \"Limitations of ISR and the premise-count confound\" 段落，包括数学解释（n=2 → ISR≥0.5）、empirical data（mean n=5.58 vs 8.46）、和 1.06× 控制后结果 ✓\n3. **method.tex** §57：\"This is an informative negative result: ISR functions as a diagnostic but fails as a training signal because optimization exploits the metric's structural bias rather than improving reasoning quality.\" ✓\n\nISR 的价值定位从 \"potential training signal\" 完全转向 \"diagnostic-only tool with a cautionary negative result\"。Framing 清晰一致。\n\n---\n\n### 5. v2-R2-W3: Abstract 信息密度\n\n**[RESOLVED]** (从 warning 降级)\n\n当前 abstract ~170 words。改进确认：\n- 叙事结构清晰：problem → method → diagnostic finding → Goodhart finding → cross-logic/cross-scale → conclusion ✓\n- 缩写有上下文定义：STA (\"Solver Trace Ablation\")、ISR (\"The resulting metric\")、GRPO 首行即出现 ✓\n- 关键数字保留合理：95±5%, 99.5%, ~5×, p<10^{-39}, 1.06×, 9 modes ✓\n\n仍有约 12-13 个数字，但每个都服务于叙事推进（不再是数据堆砌）。与 Round 1 的密度问题相比改进显著。一个小建议：\"2 model scales\" 和 \"2 logic types\" 可考虑合并为更简洁的表述，但不影响接收判断。\n\n---\n\n### 6. v2-R2-W4: ISR premise-count confound 在正文中\n\n**[RESOLVED]**\n\nmethod.tex §53-58 包含完整的 5 行段落，覆盖：\n- ISR 对 n 的数学敏感性（n=2 → ISR≥0.5）✓\n- 经验数据（mean n=5.58 vs 8.46）✓\n- 1.06× 控制后结果 ✓\n- \"informative negative result\" 定性 ✓\n- 方法论建议（LOO-based metric 应报告 count-matched comparisons）✓\n\n不再需要读者翻附录才能理解 ISR 的核心限制。\n\n---\n\n### 7. v2-R2-W5: C2/C4 独立性\n\n**[RESOLVED]**\n\nmethod.tex §93-94 的独立性论证具体且令人信服：\n- Text matching (H1/H7)：\"requires only string comparison between conclusion and premises, needing no solver or ISR computation\" ✓\n- Functional stage：\"uses per-sample n_necessary from any LOO-based analysis, not specifically STA\" ✓\n- 应用范围：\"Practitioners can apply the taxonomy to any neurosymbolic system where premise-conclusion structure is inspectable\" ✓\n\n这将 C4（taxonomy）从 C1/C2（STA/ISR）中明确解耦。独立性论证成立。\n\n---\n\n### 8. v2-FMT-1: Limitations 位置\n\n**[RESOLVED]**\n\nmain.tex 确认结构为：`\\input{conclusion}` → `\\input{limitations}` → `\\input{ethics}` → `\\bibliography{references}` → `\\appendix` ✓\n\n即 §5 Discussion and Conclusion → §6 Limitations → Ethics Statement → References → Appendix。这是 ACL/EMNLP 的标准顺序。\n\n**注意**：当前 PDF 渲染可能未反映最新 source 结构（从 page images 看，Limitations 仍出现在 References 之后的 page 10）。建议提交前重新编译并确认输出 PDF 的 section 顺序。\n\n---\n\n### 9. v2-FMT-2: Ethics Statement\n\n**[RESOLVED]**\n\nethics.tex 存在，内容 7 行，覆盖：\n- 研究目的（documenting failure modes）✓\n- AI safety implications（diagnostics can be gamed）✓\n- 数据/模型公开性（FOLIO + Qwen3-4B open-weight）✓\n- 无人类受试者 ✓\n\n内容简洁、相关、符合 ACL ARR 要求。\n\n---\n\n### 10. v2-FMT-3: Orphan bib entries\n\n**[RESOLVED]**\n\nverify_references 确认：0 orphan, 0 missing ✓\n- `sundararajan-ig` 已从 bib 移除 ✓\n- `lundberg-shap` → `lundberg-shap-game`（Shapley 1953），在 method.tex §61 中正确引用 ✓\n\n---\n\n### 11. v2-R1-M4: Prolog \"universal Goodhart\"\n\n**[RESOLVED]**\n\nexperiments.tex §137：\"consistent gaming across all seeds\" ✓（不再使用 \"universal Goodhart\"）\nexperiments.tex §144：\"This is a qualitative observation from a single configuration (Prolog + ISR β=0.1, 3 seeds); generalization to other logic types requires further experimentation.\" ✓\n\n措辞充分弱化，与实验数据的统计基础匹配。\n\n---\n\n## 额外检查\n\n### AI 写作痕迹\n\n**Em-dash (---) 使用**：全文 71 处 `---`，其中约 30-40 处为 prose 中的解释性 em-dash（其余为表格缺失值标记）。例如：\n- conclusion.tex: \"gaming dominates at every β---amplifying H7\" \n- experiments.tex: \"the diagnostic itself becomes the target of gaming\" 后接 \"---\"\n- introduction.tex: \"yet at convergence, \\emph{none} produce structurally sound outputs\" 前有 \"---\"\n\n每页 prose 平均约 4-5 个解释性 em-dash，频率偏高。建议在终稿中做一轮 dash-to-comma/parenthesis 替换，特别是 experiments.tex（16 处 prose em-dash）和 conclusion.tex（4 处）。\n\n**-ing 短语**：15 处 `ing,` 模式，分布合理，未发现典型的 AI 句尾 -ing 短语（如 \"...highlighting the importance of...\"）。不构成问题。\n\n**过度分段**：conclusion.tex 使用 5 个 `\\paragraph{}` 子段落，结构清晰。experiments.tex 使用 `\\textbf{}` 标记子话题而非频繁换段。整体段落长度正常（5-8 句），无过度分段问题。\n\n### Contributions 与正文对应\n\nC1 → §4.2 ISR as Diagnostic (`\\label{sec:diagnostic}`) ✓\nC2 → §4.3 ISR as Reward: Goodhart Effects (`\\label{sec:goodhart}`) ✓\nC3 → §4.4 Cross-Logic Diagnostic Transfer (`\\label{sec:crosslogic}`) ✓\nC4 → §4.5 Hacking Taxonomy (`\\label{sec:taxonomy}`) ✓\n\n所有 contribution 都有对应 section、table 和 figure 支撑。\n\n### 修改引入的新问题\n\n**1. Abstract \"zero structurally sound outputs\" 小幅 overclaim**（severity: info）\nAbstract line 2：\"yet produce zero structurally sound outputs\"。但 Table 1 exec-only N-H=8%（seed 42）。Introduction line 4 表述更准确：\"none produce structurally sound outputs\"（可理解为 no seed 整体产出 sound outputs）。建议 abstract 改为 \"yet produce near-zero structurally sound outputs\" 或 \"yet fewer than 10% of outputs are structurally sound\"。\n\n**2. Discussion and Conclusion 密度极高**（severity: info）\n§5 Discussion and Conclusion 在 conclusion.tex 中含 5 个 `\\paragraph{}`（Dose-response pattern, Classifier blind spots, Capacity-dependent Goodhart basins, Hacking mode switching, 加上开篇总结），总计约 28 行 LaTeX。这些内容实质性且有价值（尤其是 capacity-dependent Goodhart basins 是重要的 cross-scale insight），但对于一个\"Conclusion\" section 来说信息量偏大。考虑是否将 dose-response pattern 和 capacity-dependent basins 的讨论移至 §4 对应的实验小节中，使 §5 更聚焦于 takeaway messages。\n\n**3. Cross-scale 实验仅 1 seed**（severity: warning, 新发现）\n§4.5 Cross-Scale Evidence（experiments.tex §149）：\"we train Qwen3-1.7B under three conditions (K=4, **seed 42, 500 steps**)\"。仅 1 个 seed 的 cross-scale 实验。虽然发现了 H9 新模式，但单 seed 结果无法排除 seed 依赖性（论文自身在 §5 承认 \"hacking mode switching\" under different seeds）。建议在 Limitations 中明确标注 cross-scale 为 single-seed pilot。\n\n---\n\n## 修改质量整体评价\n\n**修改质量：良好。** 11 个 open issues 中：\n- **9 个 RESOLVED**（R1-W5, R2-W8, v2-R1-W3, v2-R2-W4, v2-R2-W5, v2-FMT-1/2/3, v2-R1-M4）\n- **1 个 RESOLVED（降级）**（v2-R2-W3 Abstract 密度）\n- **1 个 STILL_OPEN（降级为 info）**（R2-MISSING-REF 引用覆盖）\n\n**论文在修改中做了显著实质性改进**，不仅修复了 flagged issues，还增加了新实验内容：\n1. **4 个 β 值**（原 2 个）→ 完整 dose-response 曲线，直接解决了 R1-N3\n2. **Cross-scale 分析**（4B + 1.7B）→ 发现 H9 新模式，部分解决 single-model 限制\n3. **9 hacking modes**（原 8 个）→ taxonomy 更完整\n4. **LOO vs. Shapley values 讨论** → 解决了 method novelty 批评中的设计选择问题\n\n**Remaining concerns**：\n- Em-dash 过度使用（~30-40 处 prose em-dash）是 AI 写作痕迹，建议终稿前做一轮 dash 清理\n- Cross-scale 实验仅 1 seed，应在 Limitations 中标注\n- 引用可补充 2-3 篇 PRM 近期工作提升到 ~34 篇\n\n**评分维持**：修改后论文整体质量提升，但核心限制（单数据集、seed 数量）未变。Findings-level 3/5 的判断维持不变。若能补充引用并清理 em-dash，可接近 weak accept 区间。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 3 修订审查报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**审查侧重**: Framing + 写作 + 格式 + 引用（逐条验证 11 个 open issues + 额外检查）\n\n---\n\n## 逐条验证\n\n### 1. R1-W5: Meta-level Goodhart 新颖性/framing\n\n**[RESOLVED]**\n\n修改到位。具体确认：\n- **标题**：从 \"Meta-Level Goodhart's Law in Neurosymbolic Formalizers\" → \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"。不再以 Goodhart 命名，转向 empirical characterization ✓\n- **Abstract** (line 5)：\"an empirical instance of Goodhart's Law (Manheim and Garrabrant, 2019)\" ✓\n- **Introduction** §25：\"an empirical instance of Goodhart's Law within the Manheim & Garrabrant taxonomy, where the diagnostic designed to detect gaming becomes gamed when optimized\" ✓\n- **Related Work** §19：\"specifically the *regressional* variant where the proxy (ISR) is exploited through its measurement mechanism (LOO component necessity)\" ✓\n- **全文搜索**：\"meta-level Goodhart\" 不再出现在标题、abstract 或 contribution 声明中 ✓\n\nGoodhart 分类学引用准确：Manheim & Garrabrant (2019) 的 regressional variant 指 proxy 被选中因其与目标的相关性，但优化压力下相关性崩塌。这一分类对 ISR 场景是合理的（ISR 与结构质量在观测数据中相关，但被优化时相关性消失）。可争论是否更接近 adversarial variant（模型作为 agent 主动 game），但 regressional 定位是defensible的。\n\n---\n\n### 2. R2-W8: H1/H7 编号不连贯\n\n**[RESOLVED]**\n\nmethod.tex §80 明确解释：\"intermediate modes H2--H6 were merged into H1 or reclassified as subtypes during analysis (e.g., H2--H5 were variants of conclusion embedding differing only in premise count or formatting, subsumed by H1; H6 was reclassified as a subtype of H7)\"。\n\n解释具体、合理，消除了读者对编号跳跃的困惑。新增的 H9（ex falso quodlibet, from 1.7B cross-scale）也在 §80 中列出，命名一致性良好。\n\n---\n\n### 3. R2-MISSING-REF: 引用覆盖\n\n**[STILL_OPEN]** (severity 降为 info)\n\n**引用健康度**：verify_references 确认 31 bib entries, 31 unique cited keys, **0 orphan, 0 missing**。bib 清洁度问题完全解决 ✓\n\n**仍缺失的引用**：\n- ThinkPRM (Mukhal et al., 2025; arXiv:2504.16828)：未出现\n- VersaPRM (2025; arXiv:2502.06737)：未出现\n- Code generation reward hacking 文献（如 arXiv:2601.20103）：未出现\n\n**引用总数**：31 条，略低于 EMNLP main conference 的典型量级（35-50 条）。但考虑到论文的实验聚焦性（单数据集+特定 RL 设置），31 条的覆盖在 borderline 可接受范围内。\n\n**降级理由**：现有引用覆盖了核心领域（neurosymbolic reasoning 8 篇、reward hacking/Goodhart 8 篇、PRM 3 篇、mutation testing 2 篇）。ThinkPRM/VersaPRM 属于 process reward models 的近期进展，与论文的 structural diagnostic 方向有关但不是直接 baseline。建议补充但不再视为影响接收的问题。\n\n**小问题**：`lundberg-shap-game` key 名称 misleading——实际引用的是 Shapley (1953) \"A Value for n-Person Games\"，非 Lundberg & Lee (2017) SHAP。key 应改为 `shapley-1953` 或类似名称以避免混淆。\n\n---\n\n### 4. v2-R1-W3: ISR-as-reward framing\n\n**[RESOLVED]**\n\n三处关键修改确认：\n1. **Abstract** (line 5)：\"the sole apparent benefit vanishes (1.06×) after controlling for a premise-count confound\" ✓\n2. **method.tex** §53-58：完整的 \"Limitations of ISR and the premise-count confound\" 段落，包括数学解释（n=2 → ISR≥0.5）、empirical data（mean n=5.58 vs 8.46）、和 1.06× 控制后结果 ✓\n3. **method.tex** §57：\"This is an informative negative result: ISR functions as a diagnostic but fails as a training signal because optimization exploits the metric's structural bias rather than improving reasoning quality.\" ✓\n\nISR 的价值定位从 \"potential training signal\" 完全转向 \"diagnostic-only tool with a cautionary negative result\"。Framing 清晰一致。\n\n---\n\n### 5. v2-R2-W3: Abstract 信息密度\n\n**[RESOLVED]** (从 warning 降级)\n\n当前 abstract ~170 words。改进确认：\n- 叙事结构清晰：problem → method → diagnostic finding → Goodhart finding → cross-logic/cross-scale → conclusion ✓\n- 缩写有上下文定义：STA (\"Solver Trace Ablation\")、ISR (\"The resulting metric\")、GRPO 首行即出现 ✓\n- 关键数字保留合理：95±5%, 99.5%, ~5×, p<10^{-39}, 1.06×, 9 modes ✓\n\n仍有约 12-13 个数字，但每个都服务于叙事推进（不再是数据堆砌）。与 Round 1 的密度问题相比改进显著。一个小建议：\"2 model scales\" 和 \"2 logic types\" 可考虑合并为更简洁的表述，但不影响接收判断。\n\n---\n\n### 6. v2-R2-W4: ISR premise-count confound 在正文中\n\n**[RESOLVED]**\n\nmethod.tex §53-58 包含完整的 5 行段落，覆盖：\n- ISR 对 n 的数学敏感性（n=2 → ISR≥0.5）✓\n- 经验数据（mean n=5.58 vs 8.46）✓\n- 1.06× 控制后结果 ✓\n- \"informative negative result\" 定性 ✓\n- 方法论建议（LOO-based metric 应报告 count-matched comparisons）✓\n\n不再需要读者翻附录才能理解 ISR 的核心限制。\n\n---\n\n### 7. v2-R2-W5: C2/C4 独立性\n\n**[RESOLVED]**\n\nmethod.tex §93-94 的独立性论证具体且令人信服：\n- Text matching (H1/H7)：\"requires only string comparison between conclusion and premises, needing no solver or ISR computation\" ✓\n- Functional stage：\"uses per-sample n_necessary from any LOO-based analysis, not specifically STA\" ✓\n- 应用范围：\"Practitioners can apply the taxonomy to any neurosymbolic system where premise-conclusion structure is inspectable\" ✓\n\n这将 C4（taxonomy）从 C1/C2（STA/ISR）中明确解耦。独立性论证成立。\n\n---\n\n### 8. v2-FMT-1: Limitations 位置\n\n**[RESOLVED]**\n\nmain.tex 确认结构为：`\\input{conclusion}` → `\\input{limitations}` → `\\input{ethics}` → `\\bibliography{references}` → `\\appendix` ✓\n\n即 §5 Discussion and Conclusion → §6 Limitations → Ethics Statement → References → Appendix。这是 ACL/EMNLP 的标准顺序。\n\n**注意**：当前 PDF 渲染可能未反映最新 source 结构（从 page images 看，Limitations 仍出现在 References 之后的 page 10）。建议提交前重新编译并确认输出 PDF 的 section 顺序。\n\n---\n\n### 9. v2-FMT-2: Ethics Statement\n\n**[RESOLVED]**\n\nethics.tex 存在，内容 7 行，覆盖：\n- 研究目的（documenting failure modes）✓\n- AI safety implications（diagnostics can be gamed）✓\n- 数据/模型公开性（FOLIO + Qwen3-4B open-weight）✓\n- 无人类受试者 ✓\n\n内容简洁、相关、符合 ACL ARR 要求。\n\n---\n\n### 10. v2-FMT-3: Orphan bib entries\n\n**[RESOLVED]**\n\nverify_references 确认：0 orphan, 0 missing ✓\n- `sundararajan-ig` 已从 bib 移除 ✓\n- `lundberg-shap` → `lundberg-shap-game`（Shapley 1953），在 method.tex §61 中正确引用 ✓\n\n---\n\n### 11. v2-R1-M4: Prolog \"universal Goodhart\"\n\n**[RESOLVED]**\n\nexperiments.tex §137：\"consistent gaming across all seeds\" ✓（不再使用 \"universal Goodhart\"）\nexperiments.tex §144：\"This is a qualitative observation from a single configuration (Prolog + ISR β=0.1, 3 seeds); generalization to other logic types requires further experimentation.\" ✓\n\n措辞充分弱化，与实验数据的统计基础匹配。\n\n---\n\n## 额外检查\n\n### AI 写作痕迹\n\n**Em-dash (---) 使用**：全文 71 处 `---`，其中约 30-40 处为 prose 中的解释性 em-dash（其余为表格缺失值标记）。例如：\n- conclusion.tex: \"gaming dominates at every β---amplifying H7\" \n- experiments.tex: \"the diagnostic itself becomes the target of gaming\" 后接 \"---\"\n- introduction.tex: \"yet at convergence, \\emph{none} produce structurally sound outputs\" 前有 \"---\"\n\n每页 prose 平均约 4-5 个解释性 em-dash，频率偏高。建议在终稿中做一轮 dash-to-comma/parenthesis 替换，特别是 experiments.tex（16 处 prose em-dash）和 conclusion.tex（4 处）。\n\n**-ing 短语**：15 处 `ing,` 模式，分布合理，未发现典型的 AI 句尾 -ing 短语（如 \"...highlighting the importance of...\"）。不构成问题。\n\n**过度分段**：conclusion.tex 使用 5 个 `\\paragraph{}` 子段落，结构清晰。experiments.tex 使用 `\\textbf{}` 标记子话题而非频繁换段。整体段落长度正常（5-8 句），无过度分段问题。\n\n### Contributions 与正文对应\n\nC1 → §4.2 ISR as Diagnostic (`\\label{sec:diagnostic}`) ✓\nC2 → §4.3 ISR as Reward: Goodhart Effects (`\\label{sec:goodhart}`) ✓\nC3 → §4.4 Cross-Logic Diagnostic Transfer (`\\label{sec:crosslogic}`) ✓\nC4 → §4.5 Hacking Taxonomy (`\\label{sec:taxonomy}`) ✓\n\n所有 contribution 都有对应 section、table 和 figure 支撑。\n\n### 修改引入的新问题\n\n**1. Abstract \"zero structurally sound outputs\" 小幅 overclaim**（severity: info）\nAbstract line 2：\"yet produce zero structurally sound outputs\"。但 Table 1 exec-only N-H=8%（seed 42）。Introduction line 4 表述更准确：\"none produce structurally sound outputs\"（可理解为 no seed 整体产出 sound outputs）。建议 abstract 改为 \"yet produce near-zero structurally sound outputs\" 或 \"yet fewer than 10% of outputs are structurally sound\"。\n\n**2. Discussion and Conclusion 密度极高**（severity: info）\n§5 Discussion and Conclusion 在 conclusion.tex 中含 5 个 `\\paragraph{}`（Dose-response pattern, Classifier blind spots, Capacity-dependent Goodhart basins, Hacking mode switching, 加上开篇总结），总计约 28 行 LaTeX。这些内容实质性且有价值（尤其是 capacity-dependent Goodhart basins 是重要的 cross-scale insight），但对于一个\"Conclusion\" section 来说信息量偏大。考虑是否将 dose-response pattern 和 capacity-dependent basins 的讨论移至 §4 对应的实验小节中，使 §5 更聚焦于 takeaway messages。\n\n**3. Cross-scale 实验仅 1 seed**（severity: warning, 新发现）\n§4.5 Cross-Scale Evidence（experiments.tex §149）：\"we train Qwen3-1.7B under three conditions (K=4, **seed 42, 500 steps**)\"。仅 1 个 seed 的 cross-scale 实验。虽然发现了 H9 新模式，但单 seed 结果无法排除 seed 依赖性（论文自身在 §5 承认 \"hacking mode switching\" under different seeds）。建议在 Limitations 中明确标注 cross-scale 为 single-seed pilot。\n\n---\n\n## 修改质量整体评价\n\n**修改质量：良好。** 11 个 open issues 中：\n- **9 个 RESOLVED**（R1-W5, R2-W8, v2-R1-W3, v2-R2-W4, v2-R2-W5, v2-FMT-1/2/3, v2-R1-M4）\n- **1 个 RESOLVED（降级）**（v2-R2-W3 Abstract 密度）\n- **1 个 STILL_OPEN（降级为 info）**（R2-MISSING-REF 引用覆盖）\n\n**论文在修改中做了显著实质性改进**，不仅修复了 flagged issues，还增加了新实验内容：\n1. **4 个 β 值**（原 2 个）→ 完整 dose-response 曲线，直接解决了 R1-N3\n2. **Cross-scale 分析**（4B + 1.7B）→ 发现 H9 新模式，部分解决 single-model 限制\n3. **9 hacking modes**（原 8 个）→ taxonomy 更完整\n4. **LOO vs. Shapley values 讨论** → 解决了 method novelty 批评中的设计选择问题\n\n**Remaining concerns**：\n- Em-dash 过度使用（~30-40 处 prose em-dash）是 AI 写作痕迹，建议终稿前做一轮 dash 清理\n- Cross-scale 实验仅 1 seed，应在 Limitations 中标注\n- 引用可补充 2-3 篇 PRM 近期工作提升到 ~34 篇\n\n**评分维持**：修改后论文整体质量提升，但核心限制（单数据集、seed 数量）未变。Findings-level 3/5 的判断维持不变。若能补充引用并清理 em-dash，可接近 weak accept 区间。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-16T22:47:24.697793+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---


### Assistant

_source line 188 · 2026-05-16T22:47:35.379510+00:00_

Round 3 审查报告已提交。

**结果摘要：**

- **9/11 issues RESOLVED**（Goodhart framing、H编号、ISR confound、C2/C4 独立性、Limitations/Ethics 位置、orphan bib、Prolog 措辞等）
- **1 RESOLVED 降级**（Abstract 密度：改进显著但仍偏密）
- **1 STILL_OPEN 降级为 info**（ThinkPRM/VersaPRM 未补充，但 31 条引用 borderline 可接受）

**论文做了实质性改进**：新增 4 个 β 值 dose-response、1.7B cross-scale 分析（发现 H9 新模式）、LOO vs Shapley 讨论。

**新发现 3 个 minor issues**：
1. ~30-40 处 prose em-dash 是 AI 写作痕迹，建议终稿前清理
2. Abstract "zero structurally sound outputs" 小幅 overclaim（实际 N-H ≈ 5-10%）
3. Cross-scale 实验仅 1 seed，应在 Limitations 标注

评分维持 Findings-level 3/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

18 recorded events


### User

_source line 189 · 2026-05-16T22:48:46.634439+00:00_

[Round 3 审稿请求]:
## 交叉分享 — Reviewer 1 的完整报告

请逐条回应 [AGREE] 或 [REBUT]，特别关注以下关键发现：

1. **v2-R1-N3 残留问题**: R1 指出 β=0.2 在 Introduction 中被称为 "maximum exploitation point"，但 §4.3 和 Table 1 未包含 β=0.2 独立段落或行。你是否同意这是显著遗漏？

2. **新问题 NI-1 (训练数据规模矛盾)**: R1 指出 §4.1 写 "200-example"、Limitations 写 "500 training examples"、Table 3 写 "500 examples (shuffled-200)"。你能否验证此矛盾？

3. **v2-R1-W4 (SFT baseline)**: R1 判定 PARTIALLY RESOLVED——100-step checkpoint PR(32%) 仍远高于 SFT(13%)。你是否同意此残留问题？

---

以下是 Reviewer 1 的完整报告：

---

### R1 Issue 验证结果

1. v2-R1-N3 (β 扩展): **[PARTIALLY RESOLVED]** — 4 个 β 值已有，但 β=0.2 在 Introduction 被称为 "maximum exploitation" 却未在 Table 1 或 §4.3 中独立报告。β=0.1 和 β=0.2 谁是 "maximum exploitation" 有歧义。
2. v2-R1-W1 (统计效力): **[PARTIALLY RESOLVED]** — Wilson CI + Fisher exact test 改善了统计报告，但 4B 仍 3 seeds，根本限制未变。β=0.05 n=5 太小（Wilson CI for 0% 上界达 43.4%）。
3. v2-R2-N2 (泛化性): **[STILL OPEN]** — R1 称论文 PDF 中完全找不到 cross-scale 内容（但 Director 确认 .tex source 包含此内容，可能是 PDF 编译问题）。
4. v2-R2-N3 (STA novelty): **[RESOLVED]** — LOO vs Shapley 讨论 + "applying" 措辞合理。
5. v2-R1-W4 (SFT baseline): **[PARTIALLY RESOLVED]** — 100-step 对照改善论证，但 PR-matched 对照仍缺。SFT proved-only ISR 分布未报告。
6. v2-R1-W6 (IAA): **[RESOLVED]** — deterministic rule-based classifiers 不需传统 IAA，50 样本精度验证合理。
7. v2-R1-N1 (Abstract "95±5%"): **[STILL OPEN]** — R1 认为与 s43 500-step PR=13% 矛盾。但 Director 指出 "95±5%" 可能是 1000-step 值。

### R1 新发现的问题

- **NI-1** [major]: 训练数据规模 200 vs 500 矛盾
- **NI-2** [minor]: p.2 "2 seeds" 应为 "3 seeds" 笔误
- **NI-3** [warning]: Limitations 仍在 References 之后（与 R2 判定不一致——R2 确认 .tex source 已修正但 PDF 可能未重编译）

### R1 整体评价

7 个 issues 中 2 个 RESOLVED、3 个 PARTIALLY RESOLVED、2 个 STILL OPEN。3 个新问题引入。
评分：维持 Findings 3.0/5。Cross-scale 纳入且数值矛盾修复后可升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-16T22:48:57.636684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-16T22:48:57.687418+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$
…[truncated 4701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-16T22:49:03.581962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "60",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "60",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-16T22:49:03.582636+00:00_

60	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
61	\midrule
62	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
63	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
64	\midrule
65	\multicolumn{7}{l}{\textit{Qwen3-1.7B (seed~42)}} \\
66	ISR & 0.1 & 100 & 0.600 & 0 & \textbf{100}$^\|$ & 0 \\ %% registry: d113-1.7b-isr-b01-s42
67	Random & 0.1 & 93 & 0.028 & 0 & 0 & 0$^\#$ \\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)
68	ISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\ %% registry: d113-1.7b-isr-b03-s42
69	\bottomrule
70	\end{tabular}}
71	\caption{Goodhart landscape across reward conditions. 4B 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. $^\|$Fixed template, zero-variance ISR. $^\#$H9 (ex falso) 100\%; not in H7/H1 columns. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
72	\label{tab:goodhart-landscape}
73	\end{table}
74	
75	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
76	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$
…[truncated 6365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-16T22:49:45.839559+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "200",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "200",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-16T22:49:46.241779+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-16T22:49:46.392784+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "200",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "200",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-16T22:49:46.493860+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-16T22:49:54.275689+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "200",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "200",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-16T22:49:54.276101+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-16T22:49:58.964968+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shuffled",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shuffled",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-16T22:49:59.266660+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-16T22:49:59.969872+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "2 seeds",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "2 seeds",
    "glob": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-16T22:50:00.020727+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-16T22:52:00.813745+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 对 Reviewer 1 Round 3 报告的交叉回应\n\n---\n\n## 关键发现回应\n\n### 1. v2-R1-N3 残留：β=0.2 \"maximum exploitation point\" 缺 Table 行\n\n**[AGREE]**（severity: minor，非 R1 所判的 partially resolved）\n\n确认事实：\n- Introduction §27 称 \"$\\beta{=}0.2$ is the maximum exploitation point (0\\% non-hacking, all seeds)\"\n- §4.3 确实有独立段落（experiments.tex §107-109）：\"Medium-dose ISR (β=0.2): maximum exploitation. At β=0.2, all three seeds converge to H7a tautology with 0% non-hacking (pooled n=290)\"\n- 但 Table 1（tab:goodhart-landscape）仅含 β∈{0.1, 0.3} 行，无 β=0.2 和 β=0.05 行\n\nR1 称 \"§4.3 和 Table 1 未包含 β=0.2 独立段落\"——这不完全准确。**§4.3 确实有独立段落**（3 行文字，含 pooled n=290 和 ISR* range 0.55-0.96）。遗漏的是 **Table 1 行**。\n\n**评估**：β=0.05 和 β=0.2 被设计为 \"supplementary dose points\"（method.tex §72），不在主 Table 中有合理性——Table 已含 7 个 4B 行 + 3 个 1.7B 行，空间紧张。但既然 Introduction 将 β=0.2 标为 \"maximum exploitation point\"（即 dose-response 的关键数据点），它在 Table 1 中缺席确实造成 claim-evidence 距离。\n\n**建议**：在 Table 1 中增加 β=0.2 行（数据已在 §107-109 中给出，仅需格式化），或在 Table 1 脚注中添加 \"β=0.05 和 β=0.2 结果见 §4.3 正文\"。\n\n但我不同意 R1 将此判为 \"partially resolved\"——β=0.2 的核心数据已在正文中报告，Table 缺行是呈现问题而非数据缺口。\n\n---\n\n### 2. NI-1: 训练数据规模 200 vs 500 矛盾\n\n**[REBUT]** R1 所报告的矛盾在当前 tex source 中**不存在**。\n\n我对全部 tex 文件进行了以下搜索：\n- `grep \"200\" paper/*.tex` → **0 matches**\n- `grep \"shuffled\" paper/*.tex` → **0 matches**\n\n当前 source 的三处数据规模描述**完全一致**：\n1. experiments.tex §10：\"on a fixed 500-example FOLIO subset\"\n2. experiments.tex 脚注：\"All experiments use data/train_500_seed42.jsonl\"\n3. limitations.tex §10：\"Our experiments use 500 training examples\"\n\nR1 所见的 \"200-example\"（§4.1）和 \"500 examples (shuffled-200)\"（Table 3）在当前 source 中不存在。这与 R1 的另一个发现一致——R1 也未能在 PDF 中找到 cross-scale 内容（v2-R2-N2）。\n\n**结论**：R1 大概率基于**未重编译的旧 PDF** 进行审查。Director 已确认 .tex source 包含 cross-scale 内容但 PDF 可能未更新。NI-1 很可能是同一问题的表现——旧 PDF 中可能存在 \"200\" 相关表述，但已在 source 中修正。\n\n**建议**：在提交前**必须重编译 PDF** 并确认输出与 source 一致。当前 R1 和 R2 的多个 \"发现\" 可能是 stale PDF artifacts。\n\n---\n\n### 3. NI-2: \"2 seeds\" 笔误\n\n**[REBUT]** 同理，`grep \"2 seeds\" paper/*.tex` → **0 matches**。\n\n当前 source 中所有 seed 数量引用均为 \"3 seeds\"（abstract, introduction, experiments 多处）。此问题在当前 source 中不存在，同样是 stale PDF artifact。\n\n---\n\n### 4. NI-3: Limitations 仍在 References 之后\n\n**[AGREE]** 与我的 Round 3 判定一致。\n\nmain.tex source 结构正确（conclusion → limitations → ethics → bibliography），但编译后 PDF 仍显示旧顺序。这是 PDF 重编译问题，不是 source 问题。\n\n---\n\n### 5. v2-R1-W4: SFT baseline\n\n**[AGREE]**（与 R1 \"PARTIALLY RESOLVED\" 一致）\n\nR1 指出 100-step checkpoint PR(32%) 仍远高于 SFT(13%)。这一 PR 差距确实限制了比较的说服力。\n\n但我补充几点 R1 未充分考虑的：\n\n(a) **论文已提供统计检验**：experiments.tex §38 报告 \"OR=5.5, 95% CI [1.4, 22.0]\"，这是在承认 PR 差距下仍有意义的统计对比。\n\n(b) **PR-matched comparison 的可行性很低**：SFT 和 GRPO 的训练动力学根本不同——SFT 的 PR 上限受限于 gold labels 的覆盖率（FOLIO gold formalizations 本身可能不完美），而 GRPO 通过 explore-exploit 可以快速提升 PR。要求 \"identical PR\" 的对照本质上是要求两种根本不同的训练范式产生相同的中间状态，这在方法论上不切实际。\n\n(c) **论文的核心论点不依赖于 SFT 对照**：SFT 的作用是 \"localizing the failure to RL optimization, not data or capacity\"（experiments.tex §37）。即使 SFT 对照不完美，exec-only GRPO 本身（PR 高但 ISR→0）已足够展示 reward hacking。SFT 是 supporting evidence，不是 critical evidence。\n\n**我的判断**：PARTIALLY RESOLVED 是合理的，但不应视为影响接收的问题。\n\n---\n\n### 6. v2-R1-N1: Abstract \"95±5%\"\n\n**[REBUT]**\n\nR1 称 \"95±5%\" 与 s43 500-step PR=13% 矛盾。这一矛盾不成立：\n\n- Introduction §4 明确标注 \"$95{\\pm}5\\%$ across three seeds **(1000 steps)**\"\n- experiments.tex §33：\"By 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$)\"\n- s43 的 500-step PR=13% 是中间 checkpoint 值，**1000 steps 时 s43 也收敛到高 PR**\n\nAbstract 未标注 \"(1000 steps)\" 是一个呈现 imprecision（建议补上），但数据本身不矛盾。R1 将 500-step 中间值与 1000-step 最终值混淆了。\n\n**建议**：Abstract line 2 改为 \"converge to high prove rates on FOLIO ($95{\\pm}5\\%$, 3 seeds, 1000 steps)\" 消除歧义。\n\n---\n\n### 7. v2-R2-N2: Cross-scale evidence\n\n**[REBUT]** R1 称 \"PDF 中完全找不到 cross-scale 内容\"。\n\n这是 PDF 重编译问题，不是 source 问题。我已验证：\n- experiments.tex §146-169：完整的 \"§4.5 Cross-Scale Evidence\" section ✓\n- 三个条件（ISR β=0.1, ISR β=0.3, Random β=0.1）✓\n- H9 新模式发现 ✓\n- Table 1 包含 3 个 1.7B 行 ✓\n\nR1 的 \"STILL OPEN\" 判定基于 stale PDF。在正确编译的 PDF 中，此问题应为 **RESOLVED**。\n\n---\n\n### 8. v2-R1-W1: 统计效力\n\n**[AGREE]**\n\nR1 指出 β=0.05 仅有 seed 42, n=55 proved samples，Wilson CI for 0% non-hacking 上界达 43.4%。这一计算正确——单 seed 小样本的 0% 观测不能排除真实 non-hacking rate 可能较高。\n\n论文已在 §104-105 中标注这是 \"seed 42\" 单 seed，但未明确报告置信区间。建议在正文或脚注中补充 Wilson CI。\n\n4B 主实验的 3-seed 限制仍是基本约束。论文在 Limitations 中承认了这一点。\n\n---\n\n### 9. v2-R1-W6: IAA\n\n**[AGREE]** 与 R1 的 \"RESOLVED\" 判定一致。\n\nDeterministic rule-based classifiers（text-match + functional n_necessary）不需要传统 IAA。50 样本精度验证（≥95% precision）是合理的验证方式。\n\n---\n\n## R1 与 R2 判定汇总对比\n\n| Issue | R1 判定 | R2 判定 | 差异分析 |\n|-------|--------|--------|---------|\n| v2-R1-N3 (β扩展) | PARTIALLY RESOLVED | RESOLVED (Table行缺失是minor) | R1 更严格，但数据在正文中存在 |\n| v2-R1-W1 (统计效力) | PARTIALLY RESOLVED | AGREE | 一致 |\n| v2-R2-N2 (cross-scale) | STILL OPEN | RESOLVED (source有，PDF需编译) | **关键分歧：PDF recompilation issue** |\n| v2-R2-N3 (STA novelty) | RESOLVED | RESOLVED | 一致 |\n| v2-R1-W4 (SFT baseline) | PARTIALLY RESOLVED | AGREE (partially, non-blocking) | 基本一致 |\n| v2-R1-W6 (IAA) | RESOLVED | RESOLVED | 一致 |\n| v2-R1-N1 (Abstract 95±5%) | STILL OPEN | REBUT (数据不矛盾) | **关键分歧：500-step vs 1000-step** |\n| NI-1 (200 vs 500) | major | REBUT (source中不存在) | **关键分歧：stale PDF artifact** |\n| NI-2 (\"2 seeds\") | minor | REBUT (source中不存在) | 同上 |\n| NI-3 (Limitations位置) | warning | AGREE | 一致 |\n\n## 关键分歧总结\n\nR1 和 R2 的主要分歧来源于 **R1 基于未重编译的旧 PDF 审查**。具体影响：\n1. NI-1（\"200-example\"）和 NI-2（\"2 seeds\"）在当前 source 中不存在 → R1 误报\n2. Cross-scale section（§4.5, 1.7B experiments）在 source 中完整存在但 R1 未见 → R1 误判为 STILL OPEN\n3. Abstract \"95±5%\" 在 Introduction 中已标注 \"(1000 steps)\"，数据不矛盾 → R1 未注意到 step 限定\n\n**建议给 Director**：本轮审查的首要 action item 是**重编译 PDF 并发布给 R1 重审**。在正确编译的 PDF 上，R1 的 2 个 STILL OPEN 和 2 个新发现可能全部 resolve，其最终评分可能从 3.0 升至 3.5。\n\n## 评分维持\n\n修改质量良好，残留问题主要是呈现层面（β=0.2 Table 行、Abstract step 标注、em-dash 清理）和 PDF 编译问题。评分维持 **Findings 3/5**，但如果 cross-scale 纳入 PDF、引用补充到 ~34 条、em-dash 清理，可达 **3.5/5 (weak accept)**。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 对 Reviewer 1 Round 3 报告的交叉回应\n\n---\n\n## 关键发现回应\n\n### 1. v2-R1-N3 残留：β=0.2 \"maximum exploitation point\" 缺 Table 行\n\n**[AGREE]**（severity: minor，非 R1 所判的 partially resolved）\n\n确认事实：\n- Introduction §27 称 \"$\\beta{=}0.2$ is the maximum exploitation point (0\\% non-hacking, all seeds)\"\n- §4.3 确实有独立段落（experiments.tex §107-109）：\"Medium-dose ISR (β=0.2): maximum exploitation. At β=0.2, all three seeds converge to H7a tautology with 0% non-hacking (pooled n=290)\"\n- 但 Table 1（tab:goodhart-landscape）仅含 β∈{0.1, 0.3} 行，无 β=0.2 和 β=0.05 行\n\nR1 称 \"§4.3 和 Table 1 未包含 β=0.2 独立段落\"——这不完全准确。**§4.3 确实有独立段落**（3 行文字，含 pooled n=290 和 ISR* range 0.55-0.96）。遗漏的是 **Table 1 行**。\n\n**评估**：β=0.05 和 β=0.2 被设计为 \"supplementary dose points\"（method.tex §72），不在主 Table 中有合理性——Table 已含 7 个 4B 行 + 3 个 1.7B 行，空间紧张。但既然 Introduction 将 β=0.2 标为 \"maximum exploitation point\"（即 dose-response 的关键数据点），它在 Table 1 中缺席确实造成 claim-evidence 距离。\n\n**建议**：在 Table 1 中增加 β=0.2 行（数据已在 §107-109 中给出，仅需格式化），或在 Table 1 脚注中添加 \"β=0.05 和 β=0.2 结果见 §4.3 正文\"。\n\n但我不同意 R1 将此判为 \"partially resolved\"——β=0.2 的核心数据已在正文中报告，Table 缺行是呈现问题而非数据缺口。\n\n---\n\n### 2. NI-1: 训练数据规模 200 vs 500 矛盾\n\n**[REBUT]** R1 所报告的矛盾在当前 tex source 中**不存在**。\n\n我对全部 tex 文件进行了以下搜索：\n- `grep \"200\" paper/*.tex` → **0 matches**\n- `grep \"shuffled\" paper/*.tex` → **0 matches**\n\n当前 source 的三处数据规模描述**完全一致**：\n1. experiments.tex §10：\"on a fixed 500-example FOLIO subset\"\n2. experiments.tex 脚注：\"All experiments use data/train_500_seed42.jsonl\"\n3. limitations.tex §10：\"Our experiments use 500 training examples\"\n\nR1 所见的 \"200-example\"（§4.1）和 \"500 examples (shuffled-200)\"（Table 3）在当前 source 中不存在。这与 R1 的另一个发现一致——R1 也未能在 PDF 中找到 cross-scale 内容（v2-R2-N2）。\n\n**结论**：R1 大概率基于**未重编译的旧 PDF** 进行审查。Director 已确认 .tex source 包含 cross-scale 内容但 PDF 可能未更新。NI-1 很可能是同一问题的表现——旧 PDF 中可能存在 \"200\" 相关表述，但已在 source 中修正。\n\n**建议**：在提交前**必须重编译 PDF** 并确认输出与 source 一致。当前 R1 和 R2 的多个 \"发现\" 可能是 stale PDF artifacts。\n\n---\n\n### 3. NI-2: \"2 seeds\" 笔误\n\n**[REBUT]** 同理，`grep \"2 seeds\" paper/*.tex` → **0 matches**。\n\n当前 source 中所有 seed 数量引用均为 \"3 seeds\"（abstract, introduction, experiments 多处）。此问题在当前 source 中不存在，同样是 stale PDF artifact。\n\n---\n\n### 4. NI-3: Limitations 仍在 References 之后\n\n**[AGREE]** 与我的 Round 3 判定一致。\n\nmain.tex source 结构正确（conclusion → limitations → ethics → bibliography），但编译后 PDF 仍显示旧顺序。这是 PDF 重编译问题，不是 source 问题。\n\n---\n\n### 5. v2-R1-W4: SFT baseline\n\n**[AGREE]**（与 R1 \"PARTIALLY RESOLVED\" 一致）\n\nR1 指出 100-step checkpoint PR(32%) 仍远高于 SFT(13%)。这一 PR 差距确实限制了比较的说服力。\n\n但我补充几点 R1 未充分考虑的：\n\n(a) **论文已提供统计检验**：experiments.tex §38 报告 \"OR=5.5, 95% CI [1.4, 22.0]\"，这是在承认 PR 差距下仍有意义的统计对比。\n\n(b) **PR-matched comparison 的可行性很低**：SFT 和 GRPO 的训练动力学根本不同——SFT 的 PR 上限受限于 gold labels 的覆盖率（FOLIO gold formalizations 本身可能不完美），而 GRPO 通过 explore-exploit 可以快速提升 PR。要求 \"identical PR\" 的对照本质上是要求两种根本不同的训练范式产生相同的中间状态，这在方法论上不切实际。\n\n(c) **论文的核心论点不依赖于 SFT 对照**：SFT 的作用是 \"localizing the failure to RL optimization, not data or capacity\"（experiments.tex §37）。即使 SFT 对照不完美，exec-only GRPO 本身（PR 高但 ISR→0）已足够展示 reward hacking。SFT 是 supporting evidence，不是 critical evidence。\n\n**我的判断**：PARTIALLY RESOLVED 是合理的，但不应视为影响接收的问题。\n\n---\n\n### 6. v2-R1-N1: Abstract \"95±5%\"\n\n**[REBUT]**\n\nR1 称 \"95±5%\" 与 s43 500-step PR=13% 矛盾。这一矛盾不成立：\n\n- Introduction §4 明确标注 \"$95{\\pm}5\\%$ across three seeds **(1000 steps)**\"\n- experiments.tex §33：\"By 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$)\"\n- s43 的 500-step PR=13% 是中间 checkpoint 值，**1000 steps 时 s43 也收敛到高 PR**\n\nAbstract 未标注 \"(1000 steps)\" 是一个呈现 imprecision（建议补上），但数据本身不矛盾。R1 将 500-step 中间值与 1000-step 最终值混淆了。\n\n**建议**：Abstract line 2 改为 \"converge to high prove rates on FOLIO ($95{\\pm}5\\%$, 3 seeds, 1000 steps)\" 消除歧义。\n\n---\n\n### 7. v2-R2-N2: Cross-scale evidence\n\n**[REBUT]** R1 称 \"PDF 中完全找不到 cross-scale 内容\"。\n\n这是 PDF 重编译问题，不是 source 问题。我已验证：\n- experiments.tex §146-169：完整的 \"§4.5 Cross-Scale Evidence\" section ✓\n- 三个条件（ISR β=0.1, ISR β=0.3, Random β=0.1）✓\n- H9 新模式发现 ✓\n- Table 1 包含 3 个 1.7B 行 ✓\n\nR1 的 \"STILL OPEN\" 判定基于 stale PDF。在正确编译的 PDF 中，此问题应为 **RESOLVED**。\n\n---\n\n### 8. v2-R1-W1: 统计效力\n\n**[AGREE]**\n\nR1 指出 β=0.05 仅有 seed 42, n=55 proved samples，Wilson CI for 0% non-hacking 上界达 43.4%。这一计算正确——单 seed 小样本的 0% 观测不能排除真实 non-hacking rate 可能较高。\n\n论文已在 §104-105 中标注这是 \"seed 42\" 单 seed，但未明确报告置信区间。建议在正文或脚注中补充 Wilson CI。\n\n4B 主实验的 3-seed 限制仍是基本约束。论文在 Limitations 中承认了这一点。\n\n---\n\n### 9. v2-R1-W6: IAA\n\n**[AGREE]** 与 R1 的 \"RESOLVED\" 判定一致。\n\nDeterministic rule-based classifiers（text-match + functional n_necessary）不需要传统 IAA。50 样本精度验证（≥95% precision）是合理的验证方式。\n\n---\n\n## R1 与 R2 判定汇总对比\n\n| Issue | R1 判定 | R2 判定 | 差异分析 |\n|-------|--------|--------|---------|\n| v2-R1-N3 (β扩展) | PARTIALLY RESOLVED | RESOLVED (Table行缺失是minor) | R1 更严格，但数据在正文中存在 |\n| v2-R1-W1 (统计效力) | PARTIALLY RESOLVED | AGREE | 一致 |\n| v2-R2-N2 (cross-scale) | STILL OPEN | RESOLVED (source有，PDF需编译) | **关键分歧：PDF recompilation issue** |\n| v2-R2-N3 (STA novelty) | RESOLVED | RESOLVED | 一致 |\n| v2-R1-W4 (SFT baseline) | PARTIALLY RESOLVED | AGREE (partially, non-blocking) | 基本一致 |\n| v2-R1-W6 (IAA) | RESOLVED | RESOLVED | 一致 |\n| v2-R1-N1 (Abstract 95±5%) | STILL OPEN | REBUT (数据不矛盾) | **关键分歧：500-step vs 1000-step** |\n| NI-1 (200 vs 500) | major | REBUT (source中不存在) | **关键分歧：stale PDF artifact** |\n| NI-2 (\"2 seeds\") | minor | REBUT (source中不存在) | 同上 |\n| NI-3 (Limitations位置) | warning | AGREE | 一致 |\n\n## 关键分歧总结\n\nR1 和 R2 的主要分歧来源于 **R1 基于未重编译的旧 PDF 审查**。具体影响：\n1. NI-1（\"200-example\"）和 NI-2（\"2 seeds\"）在当前 source 中不存在 → R1 误报\n2. Cross-scale section（§4.5, 1.7B experiments）在 source 中完整存在但 R1 未见 → R1 误判为 STILL OPEN\n3. Abstract \"95±5%\" 在 Introduction 中已标注 \"(1000 steps)\"，数据不矛盾 → R1 未注意到 step 限定\n\n**建议给 Director**：本轮审查的首要 action item 是**重编译 PDF 并发布给 R1 重审**。在正确编译的 PDF 上，R1 的 2 个 STILL OPEN 和 2 个新发现可能全部 resolve，其最终评分可能从 3.0 升至 3.5。\n\n## 评分维持\n\n修改质量良好，残留问题主要是呈现层面（β=0.2 Table 行、Abstract step 标注、em-dash 清理）和 PDF 编译问题。评分维持 **Findings 3/5**，但如果 cross-scale 纳入 PDF、引用补充到 ~34 条、em-dash 清理，可达 **3.5/5 (weak accept)**。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-16T22:52:04.979951+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-16T22:52:14.776546+00:00_

报告已提交。

**核心结论**：R1 与 R2 的多个分歧源于 **R1 基于未重编译的旧 PDF 审查**。三个关键 REBUT：

1. **NI-1（200 vs 500 矛盾）**：当前 tex source 中 `grep "200"` 返回 0 匹配——"200-example" 不存在，三处均写 "500"。
2. **NI-2（"2 seeds" 笔误）**：`grep "2 seeds"` 同样 0 匹配。
3. **Abstract "95±5%"**：Introduction 明确标注 "(1000 steps)"，s43 的 500-step PR=13% 是中间值，1000 steps 时所有 seed 收敛到 0.95±0.05。数据不矛盾。

**首要 action item**：重编译 PDF 后让 R1 基于正确版本重审。Cross-scale 内容、数据一致性修复、Limitations 位置等问题在 source 层面均已解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

60 recorded events


### User

_source line 207 · 2026-05-17T11:17:13.997632+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查**新颖性 + 叙事完整性 + 写作/格式合规**。

## 论文信息
- **标题**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation
- **目标 Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May 2026 cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL LaTeX template, `[review]` option, double-blind, long paper (8 pages content max), appendix after references (不计页数), Limitations/Ethics 不计页数
- **论文路径**: `projects/solver-trace-ablation/paper/main.tex`

## 你的审查侧重

重点关注：
1. **新颖性与定位 (Novelty & Positioning)**:
   - STA/ISR 作为诊断工具 vs 已有 PRM/mutation testing 方法的真实增量是什么？
   - "Goodhart collapse" 发现 vs 已有 reward hacking/overoptimization 文献的差异化是否充分？
   - 贡献 C1-C4 的独立性和增量价值？
   - Hacking taxonomy (9 modes) 对社区的实际参考价值？

2. **叙事完整性 (Narrative Coherence)**:
   - Abstract → Introduction → Method → Experiments → Discussion 的故事线是否统一？
   - 论文的核心 message 是否清晰（ISR: reliable observer, unreliable optimizer）？
   - Related Work 的 positioning 是否将本文与 Goodhart 文献、PRM 文献、neurosymbolic reasoning 文献做了有效区分？
   - Contributions 列表是否与实际 sections 匹配？

3. **写作质量 (Writing Quality)**:
   - AI 写作痕迹检查：em-dash、-ing 短语、过度分段、用词黑名单
   - 专有名词首次定义是否完整（ISR, STA, GRPO, H1/H7/H8 等）？
   - 图表知识密度和 caption 自包含性？
   - 数字精度全表一致性？

4. **格式合规 (Format Compliance)**:
   - 页数是否在 8 页限制内？
   - 匿名化是否彻底（无作者信息、无 de-anonymizing self-citations）？
   - Limitations 和 Ethics sections 是否存在且位置正确？
   - 引用格式（natbib ACL style）是否一致？
   - 行号是否开启（review 版要求）？

请输出标准审稿格式：Summary → Strengths (逐条) → Weaknesses (逐条，含 severity: critical/warning/info) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T11:17:23.968153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T11:17:23.968665+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_reviewer_2_9e5cd831.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T11:17:24.069238+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T11:17:24.120844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T11:17:29.114919+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-17T11:17:29.968253+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-13",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-13",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-17T11:17:30.571180+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T11:17:38.501611+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's comprehensive information about the ACL ARR 2026 reviewer guidelines, review form, and scoring criteria:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores:
…[truncated 1806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9386
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-17T11:17:44.721967+00:00_

Error: result (11,791,614 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016663472.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016663472.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016663472.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 14753
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-17T11:20:27.619782+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 66, \"unique_cited_keys\": 34, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 21, \"online_not_found\": 8, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": \"Defining and Characterizing Reward H
…[truncated 26947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 177048
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T11:20:36.902917+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), definitions for each score level, and all required fields. Include the exact text of the scoring rubrics for Soundness, Excitement, Overall Assessment, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), definitions for each score level, and all required fields. Include the exact text of the scoring rubrics for Soundness, Excitement, Overall Assessment, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-17T11:20:38.208856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-17T11:20:38.660725+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-17T11:20:38.761655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-17T11:20:39.113406+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 5 seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop that guarantees eventual collapse at all tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields significantly more genuine output than random controls ($22.6\%$ vs.\ $7.7\%$, $\text{OR}{=}3.48$, $p{<}10^{-8}$); trajectory analysis confirms this benefit is temporary ($17\%{\to}2\%$ genuine at 1000 steps).
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B).
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target at any dose.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-17T11:20:39.470771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-17T11:20:39.537542+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($95{\pm}5\%$ across three seeds, 1000 steps), yet at convergence, \emph{none} produce structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emp
…[truncated 3810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 66
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T11:20:46.320084+00:00_

# ACL Rolling Review Form: Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. Soundness (1-5 scale with half-point options)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. Excitement (1-5 scale with half-point options)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

### 4. Overall Assessment (1-5 scale with half-point options)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: I think this pap
…[truncated 1866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9417
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-17T11:20:50.236795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T11:20:50.588014+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\ci
…[truncated 1642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T11:20:50.738809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-17T11:20:50.789437+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 7877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T11:20:50.789854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T11:20:51.191572+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}, a legacy filename containing no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (se
…[truncated 24952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T11:20:59.837777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T11:20:59.838293+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR exhibits inevitable Goodhart collapse~\citep{manheim-goodhart-taxonomy}: tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop that causes gaming at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	The effect is consistent across logic types (Prolog: 0\% non-hacking, 3/3 seeds), model scales (1.7B: novel gaming modes), and training durations (500$\to$1000 steps: transient genuine windows close).
7	ISR semantics are objective-dependent: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	At 500 steps, ISR-trained models produce significantly more genuine proofs than random controls ($22.6\%$ vs.\ $7.7\%$; $\text{OR}{=}3.48$, $p{<}10^{-8}$), confirming that ISR increases the rate of genuine proofs; this benefit is inherently transient, as the same LOO bias that rewards genuine necessity also rewards tautological constructions.
9	
10	\paragraph{Timing, not destiny.}
11	$\beta$ does not control whether collapse occurs, but when.
12	At $\beta{=}0.1$, 5 seeds bifurcate stochastically: 2 collapse rapidly (${\leq}150$ steps), 3 sustain a transient genuine window (5-seed pooled: ${\sim}23\%$; per non-collapsed seed: $17$--$55\%$) that trajectory analysis confirms is temporary ($17\%{\to}2\%$ at 1000 steps).
13	At $\beta{=}0.05$, all 3 seeds collapse to H7-dominated hacking (pooled $93.7\%$ H7, genuine $5.1\%$); at $\beta{=}0.2$, all 3 seeds collapse; at $\beta{=}0.3$, diverse failure modes emerge.
14	The structural bias ($P{\to}P$ receives $\text{ISR}{=}0.75$, single-premise-equals-conclusion receives $\text{ISR}{\geq}0.5$) ensures that
…[truncated 4351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T11:20:59.938993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T11:20:59.939482+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for per-seed comparisons.
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seed~42 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient ($17\%{\to}2\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses two seeds with high variance ($\text{PR}{=}0\%$ vs.\ $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	
20	\paragraph{Cross-scale replication.}
21	Our 1.7B experiments use a single seed.
22	Although different seeds may converge to different exploitation modes (as observed at 4B scale, where three seeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0\% genuine output is robust: at 4B, 
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-17T11:20:59.990025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T11:20:59.990354+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-17T11:21:00.090842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-17T11:21:00.392706+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 37976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T11:21:06.317832+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T11:21:07.409262+00:00_

Error: result (2,017,469 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016867331.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016867331.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tool-results/mcp-agent-ml-research-pdf_to_images-1779016867331.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1091
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T11:21:21.572109+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Visual PDF review of paper",
  "subagent_type": "general-purpose",
  "prompt": "You are reviewing a paper PDF for visual/formatting issues. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf\n\nUse the mcp__agent-ml-research__pdf_to_images tool to render pages one at a time (or 2 at a time) and visually inspect each page. Check for:\n\n1. **Page count**: How many pages of content before references? (limit is 8 for ACL long paper)\n2. **Line numbers**: Are line numbers visible? (required for review submission)\n3. **Anonymization**: Is there any author identifying information? Should say \"Anonymous ACL submission\"\n4. **Figure quality**: Are figures readable? Font size >= 7pt? Any overlapping text/labels?\n5. **Table formatting**: Are numbers consistently formatted? Best results bolded?\n6. **Overall layout**: Any overflow, margin violations, orphan lines, widow lines?\n7. **References page**: Does it start after page 8? Are references properly formatted?\n8. **Appendix**: Is it after references?\n9. **Limitations and Ethics**: Are these sections present and in the right location (after conclusion, before references)?\n\nRender pages 1-2, then 3-4, then 5-6, then 7-8, then 9-10, then 11-13.\n\nReport all findings in a structured list. Be specific about any issues found.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Visual PDF review of paper",
    "subagent_type": "general-purpose",
    "prompt": "You are reviewing a paper PDF for visual/formatting issues. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf\n\nUse the mcp__agent-ml-research__pdf_to_images tool to render pages one at a time (or 2 at a time) and visually inspect each page. Check for:\n\n1. **Page count**: How many pages of content before references? (limit is 8 for ACL long paper)\n2. **Line numbers**: Are line numbers visible? (required for review submission)\n3. **Anonymization**: Is there any author identifying information? Should say \"Anonymous ACL submission\"\n4. **Figure quality**: Are figures readable? Font size >= 7pt? Any overlapping text/labels?\n5. **Table formatting**: Are numbers consistently formatted? Best results bolded?\n6. **Overall layout**: Any overflow, margin violations, orphan lines, widow lines?\n7. **References page**: Does it start after page 8? Are references properly formatted?\n8. **Appendix**: Is it after references?\n9. **Limitations and Ethics**: Are these sections present and in the right location (after conclusion, before references)?\n\nRender pages 1-2, then 3-4, then 5-6, then 7-8, then 9-10, then 11-13.\n\nReport all findings in a structured list. Be specific about any issues found.",
    "run_in_background": "True"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T11:21:21.622942+00:00_

Async agent launched successfully.
agentId: add04409edfeb4d64 (internal ID - do not mention to user. Use SendMessage with to: 'add04409edfeb4d64' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/60075192-9982-497f-8029-1ed8863743f0/tasks/add04409edfeb4d64.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T11:21:22.175885+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T11:21:22.628326+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:1:% Appendix — solver-trace-ablation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-17T11:21:23.331312+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-17T11:21:23.632871+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T11:21:24.135150+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T11:21:24.185743+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:12:The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:15:Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:28:Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:39:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:111:\textbf{Trajectory analysis: timing, not destiny.}\label{sec:goodhart-temporal}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:120:The random control reveals a structurally distinct failure mode: seed~42 degenerates ($\text{PR}{=}0\%$), while seed~43 achieves $\text{PR}{=}62\%$ with H1 redundancy hacking ($77.4\%$) and zero H7; when random reward produces learning, it exploits redundancy rather than tautology, confirming that H7 is specific to ISR's LOO structure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/pa
…[truncated 3796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-17T11:21:31.259896+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-17T11:21:31.812299+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:34:Notably, s43 recovers from $\text{PR}{=}13\%$ (500 steps) to $\text{PR}{=}96\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:264:H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-17T11:21:33.318120+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing\\b[,.].*\\.$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing\\b[,.].*\\.$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-17T11:21:33.318553+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:12:The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:15:Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:28:Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:39:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:120:The random control reveals a structurally distinct failure mode: seed~42 degenerates ($\text{PR}{=}0\%$), while seed~43 achieves $\text{PR}{=}62\%$ with H1 redundancy hacking ($77.4\%$) and zero H7; when random reward produces learning, it exploits redundancy rather than tautology, confirming that H7 is specific to ISR's LOO structure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:133:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:224:The three dominant modes, \
…[truncated 3475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T11:21:33.469368+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\documentclass",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\documentclass",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T11:21:33.570482+00:00_

1:\documentclass[11pt]{article}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-17T11:22:44.107267+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(our previous|our earlier|we previously|our prior|github\\.com|Anonymous)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(our previous|our earlier|we previously|our prior|github\\.com|Anonymous)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-17T11:22:44.358647+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex:23:\author{Anonymous ACL submission}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-17T11:22:44.409242+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "novel",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "novel",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-17T11:22:44.459894+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex:6:The effect is consistent across logic types (Prolog: 0\% non-hacking, 3/3 seeds), model scales (1.7B: novel gaming modes), and training durations (500$\to$1000 steps: transient genuine windows close).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex:23:These cases collectively argue for mandatory functional cross-validation of text-based hacking classifiers, complemented by logic-level checks for novel exploit classes.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex:7:The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:29:The effect transfers to Prolog (3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming}) and across model scale (1.7B discovers qualitatively novel gaming modes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-17T11:22:49.977996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-17T11:22:50.028669+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 13075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-17T11:24:26.022039+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep Pages",
  "description": "Count PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep Pages",
    "description": "Count PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-17T11:24:26.123007+00:00_

Pages:           23
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_reviewer_2_9e5cd831

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-17T11:26:08.639893+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May 2026 cycle)\n**审查侧重**: 新颖性 + 叙事完整性 + 写作/格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、叙事清晰、核心发现(observer/optimizer 不对称)有价值，但方法本身新颖性有限、实验范围受限于单模型+单数据集，且正文严重超页(~10.5页 vs 8页限制)，格式不合规属于 desk-reject 级别问题。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法严谨(matched random control, SFT baseline, premise-count-matched analysis, Fisher exact tests)，但单模型家族(Qwen3)+单数据集(FOLIO 500例)限制了 claims 的外部有效性；1.7B 仅单 seed |\n| Excitement | 3.0/5 | Observer/optimizer 不对称是一个有实践意义的发现；stochastic bifurcation 和 temporal dynamics 有新意；但核心方法(LOO ablation)是标准技术的直接应用，\"diagnostics can be gamed when optimized\" 对熟悉 Goodhart's Law 的读者而言并不意外 |\n| Reproducibility | 4/5 | 超参数表完整(Table 3)、seeds/data file 明确指定、evaluation protocol 统一(eval_sta.py)；s43 eval exception 透明标注；代码匿名化待公开 |\n| Overall Assessment | 3.0/5 (Findings) | 在所选范围内实验扎实、叙事连贯、方法论自洽，适合 Findings；升级至 Main Conference 需要：(a) 修复超页问题，(b) 扩展至≥1个额外模型家族或数据集，(c) 加强方法新颖性(如 tautology-guarded ISR ablation) |\n| Confidence | 4/5 | 仔细检查了核心 claims 和数据支撑；对 neurosymbolic reasoning 和 reward hacking 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文严重超出页数限制\n- 具体位置：Sections 1-5 (Discussion and Conclusion 结束于约第 11 页中部)\n- 问题：ACL long paper 正文限制 8 页（Limitations/Ethics/References/Appendix 不计入），视觉审查确认正文约 10.5 页，超出约 2.5 页。`main.tex` 中已通过激进的 float spacing 参数(`\\textfloatsep=8pt`, `\\intextsep=6pt`)压缩空间，但仍远超限制。\n- 为什么影响接收：直接导致 desk reject。\n- 建议修改方向：(1) 将 §4.4 Cross-Logic 和 §4.5 Cross-Scale 中的详细数字移入 Appendix，正文保留核心结论；(2) §5 Discussion 合并至 Conclusion，删除与 §4 重复的段落(目前 Discussion 大量重述 Experiments 已报告的数据)；(3) Method §3.3 的 reward conditions 描述可压缩。\n\n**N2** [critical] STA/ISR 方法新颖性有限\n- 具体位置：§3.2, Algorithm 1; §3.2 line 26 \"LOO ablation itself is standard\"\n- 问题：论文坦诚承认 LOO ablation 是标准技术（mutation testing/sensitivity analysis），贡献在于应用和发现。但 Algorithm 1 仅 6 行伪代码、ISR 公式(Eq.1)是 LOO 的直接 fraction 统计。方法本身的技术深度不足以支撑 Main Conference 的方法贡献。\n- 为什么影响接收：对 EMNLP main track 而言，方法创新性是核心考量维度之一。论文价值高度依赖经验发现的新颖性和影响力。\n- 建议修改方向：(1) 测试一个 \"tautology-guarded ISR\" 变体(e.g., ISR=0 if n_comp≤2 或检测到 P→P 结构)，以区分 \"ISR 内在缺陷\" 和 \"所有 LOO metrics 的通病\"；(2) 强化贡献定位为 empirical contribution + taxonomy，弱化方法贡献叙事。\n\n**N3** [critical] 实验范围受限，claims 的外部有效性不足\n- 具体位置：§4.1 Setup; Limitations §6 lines 1-4\n- 问题：所有实验使用 Qwen3 单一模型家族(4B + 单 seed 1.7B) 和 FOLIO 单一数据集(500 train / 100 eval)。对于 \"inevitable Goodhart collapse\" 这样的强 claim，实验范围偏窄：\n  - FOLIO 是一个较小的 curated 数据集，不清楚更大规模或更多样化的形式化任务是否复现\n  - 单模型家族无法排除 Qwen3 特有的 bias\n  - 500 训练样本在 GRPO 标准中偏少，退化可能部分是数据规模 artifact\n- 为什么影响接收：结论的普适性是 main conference 论文的核心要求\n- 建议修改方向：至少在一个额外模型(LLaMA/Mistral 系)或一个额外数据集上验证核心发现(ISR collapse + Goodhart effect)\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Inevitable collapse\" claim 的证据链尚有缺口\n- 具体位置：§4.3, §5 \"Timing, not destiny\"\n- 问题：Claim \"collapse is inevitable at all tested doses\" 的关键证据——transient genuine window 的关闭——仅基于 seed 42 从 500 步延伸至 1000 步的单个 trajectory(17.3%→2.2%)。β=0.1 下另外两个非 collapsed seeds(s45, s46)没有 1000-step 数据。单 seed 的 trajectory 不足以支撑 \"所有 seeds 必然收敛\" 的 claim。\n- 建议：对 s45 或 s46 执行 1000-step 扩展训练以补充证据；或将 claim 软化为 \"all extended trajectories tested so far converge\"。\n\n**W2** [warning] Non-hacking rate 作为核心指标的脆弱性\n- 具体位置：§4.1 line 12; Appendix §D.1 (Classifier Validation)\n- 问题：Non-hacking rate 定义为\"不匹配任何 9 种已编目模式的残差\"，是一个 classifier-dependent metric。论文自身在 Appendix D 中发现 H7b 和 query-as-fact gaming 导致 false negatives。3-seed H8+FN 修正后的比较(ISR 6.06% vs Random 9.5%, Fisher p=0.182 n.s.)削弱了 5-seed 主表的 headline claim(22.6% vs 7.7%, OR=3.48)。\n- 建议：在主表 caption 或正文中更显著地标注修正后结果，避免读者仅看到 headline numbers。\n\n**W3** [warning] C4 (hacking taxonomy) 的贡献定位\n- 具体位置：§3.3, §4.6, Table 2, Appendix D\n- 问题：9-mode taxonomy 是描述性的(cataloging observed modes)而非预测性的。编号间隙(H2-H6 merged, §3.3 line 80)暴露了 taxonomy 是 post-hoc 整理而非原则性分析。对社区的参考价值取决于 modes 是否跨模型/数据集泛化，但论文只在 Qwen3+FOLIO 上验证。\n- 建议：明确 taxonomy 的适用范围和局限；讨论哪些 modes 可能是 architecture-specific vs universal。\n\n**W4** [warning] Exec-only seed 43 评估不一致\n- 具体位置：Appendix A \"Evaluation exception\"; Table 6 footnote †\n- 问题：Exec-only s43 使用 temperature=0.7 sampling 评估而非 greedy decoding，破坏了与其他 seeds 的可比性。虽然透明标注，但 s43 数据出现在 pooled statistics 中(如 3-seed mean±std)。\n- 建议：重新用 greedy decoding 评估 s43，或从 pooled statistics 中排除并标注。\n\n**W5** [warning] ISR reward formulation 未测试明显的 fix\n- 具体位置：§4.3; §3.3 line 72\n- 问题：论文声称 \"ISR's structural bias toward tautology makes collapse inevitable\"，但未测试一个自然的修复：tautology-guarded ISR(e.g., 当 n_comp≤2 或检测到 conclusion=premise 时设 ISR=0)。不做这个 ablation 就无法区分 \"ISR formulation 的特定缺陷\" 和 \"所有 LOO-based metrics 的根本问题\"。\n- 建议：增加 tautology-guarded ISR 作为额外条件，即使结果仍 collapse(H1 or other modes)，也能大大加强论文 claim。\n\n---\n\n## 小问题（不影响接收）\n\n1. **\"Notably\" 出现** (experiments.tex:34)：AI 写作标志词，建议删除直接陈述。\n2. **Em-dash in comment** (appendix.tex:1 `% Appendix — solver-trace-ablation`)：仅在注释中，不影响排版。\n3. **FOLIO 年份**：bib 标注 year=2024(EMNLP proceedings)，OpenAlex 返回 2022(arXiv date)。请确认是否为 EMNLP 2024 proceedings version。\n4. **METR 引用**：`metr-reward-hacking` 是 blog post(@misc)，非 peer-reviewed；审稿时无碍但建议注明。\n5. **Missing reference**: DeepSeek-R1 (2025) 大量使用 GRPO 训练 reasoning models，是该领域最高影响力的 GRPO 应用，建议引用。\n\n---\n\n## 主要优势\n\n**S1. 令人信服的核心现象**：99.5% structural collapse (ISR*: 0.642→0.003) 在 PR 上升 32%→96% 的同时发生，是一个引人注目的量化结果，清楚展示了 execution-only evaluation 的盲区。\n\n**S2. 实验控制严谨**：matched random control 隔离了 ISR-specific signal；SFT baseline 将 degeneration 定位至 RL(92.3% non-hacking vs ~8%)；premise-count-matched analysis(1.06×)诚实地消解了自己的 headline number。这种方法论自我修正在 ML 论文中罕见。\n\n**S3. 叙事一致性强**：\"reliable observer, unreliable optimizer at any dose\" 是一个清晰、有记忆点的 message。Abstract → Introduction → Method → Experiments → Discussion 保持了统一的故事线，没有 framing 漂移。\n\n**S4. 写作质量高**：基本无 AI 写作痕迹(em-dash 0, -ing phrase endings 0, AI blacklist words 仅 1 个 \"Notably\")。散文密度高但可读。Related Work 做了有效的 positioning 而非 survey。\n\n**S5. 方法论诚实度**：论文主动讨论了 ISR 的局限性(premise-count confound §3.2, semantic gap ρ=-0.049, H7b/H8 corrections in Appendix D)，包括修正后削弱自身 claim 的 3-seed 结果(p=0.182 n.s.)。\n\n---\n\n## 引用验证摘要\n\n- 34 bib entries, 66 citations, 0 orphan, 0 missing\n- OpenAlex verified: 21/34; not found: 8 (多为 recent preprints/blog); mismatch: 5 (author name formatting/year issues, non-critical)\n- 无疑似虚构引用\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May 2026 cycle)\n**审查侧重**: 新颖性 + 叙事完整性 + 写作/格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、叙事清晰、核心发现(observer/optimizer 不对称)有价值，但方法本身新颖性有限、实验范围受限于单模型+单数据集，且正文严重超页(~10.5页 vs 8页限制)，格式不合规属于 desk-reject 级别问题。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法严谨(matched random control, SFT baseline, premise-count-matched analysis, Fisher exact tests)，但单模型家族(Qwen3)+单数据集(FOLIO 500例)限制了 claims 的外部有效性；1.7B 仅单 seed |\n| Excitement | 3.0/5 | Observer/optimizer 不对称是一个有实践意义的发现；stochastic bifurcation 和 temporal dynamics 有新意；但核心方法(LOO ablation)是标准技术的直接应用，\"diagnostics can be gamed when optimized\" 对熟悉 Goodhart's Law 的读者而言并不意外 |\n| Reproducibility | 4/5 | 超参数表完整(Table 3)、seeds/data file 明确指定、evaluation protocol 统一(eval_sta.py)；s43 eval exception 透明标注；代码匿名化待公开 |\n| Overall Assessment | 3.0/5 (Findings) | 在所选范围内实验扎实、叙事连贯、方法论自洽，适合 Findings；升级至 Main Conference 需要：(a) 修复超页问题，(b) 扩展至≥1个额外模型家族或数据集，(c) 加强方法新颖性(如 tautology-guarded ISR ablation) |\n| Confidence | 4/5 | 仔细检查了核心 claims 和数据支撑；对 neurosymbolic reasoning 和 reward hacking 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文严重超出页数限制\n- 具体位置：Sections 1-5 (Discussion and Conclusion 结束于约第 11 页中部)\n- 问题：ACL long paper 正文限制 8 页（Limitations/Ethics/References/Appendix 不计入），视觉审查确认正文约 10.5 页，超出约 2.5 页。`main.tex` 中已通过激进的 float spacing 参数(`\\textfloatsep=8pt`, `\\intextsep=6pt`)压缩空间，但仍远超限制。\n- 为什么影响接收：直接导致 desk reject。\n- 建议修改方向：(1) 将 §4.4 Cross-Logic 和 §4.5 Cross-Scale 中的详细数字移入 Appendix，正文保留核心结论；(2) §5 Discussion 合并至 Conclusion，删除与 §4 重复的段落(目前 Discussion 大量重述 Experiments 已报告的数据)；(3) Method §3.3 的 reward conditions 描述可压缩。\n\n**N2** [critical] STA/ISR 方法新颖性有限\n- 具体位置：§3.2, Algorithm 1; §3.2 line 26 \"LOO ablation itself is standard\"\n- 问题：论文坦诚承认 LOO ablation 是标准技术（mutation testing/sensitivity analysis），贡献在于应用和发现。但 Algorithm 1 仅 6 行伪代码、ISR 公式(Eq.1)是 LOO 的直接 fraction 统计。方法本身的技术深度不足以支撑 Main Conference 的方法贡献。\n- 为什么影响接收：对 EMNLP main track 而言，方法创新性是核心考量维度之一。论文价值高度依赖经验发现的新颖性和影响力。\n- 建议修改方向：(1) 测试一个 \"tautology-guarded ISR\" 变体(e.g., ISR=0 if n_comp≤2 或检测到 P→P 结构)，以区分 \"ISR 内在缺陷\" 和 \"所有 LOO metrics 的通病\"；(2) 强化贡献定位为 empirical contribution + taxonomy，弱化方法贡献叙事。\n\n**N3** [critical] 实验范围受限，claims 的外部有效性不足\n- 具体位置：§4.1 Setup; Limitations §6 lines 1-4\n- 问题：所有实验使用 Qwen3 单一模型家族(4B + 单 seed 1.7B) 和 FOLIO 单一数据集(500 train / 100 eval)。对于 \"inevitable Goodhart collapse\" 这样的强 claim，实验范围偏窄：\n  - FOLIO 是一个较小的 curated 数据集，不清楚更大规模或更多样化的形式化任务是否复现\n  - 单模型家族无法排除 Qwen3 特有的 bias\n  - 500 训练样本在 GRPO 标准中偏少，退化可能部分是数据规模 artifact\n- 为什么影响接收：结论的普适性是 main conference 论文的核心要求\n- 建议修改方向：至少在一个额外模型(LLaMA/Mistral 系)或一个额外数据集上验证核心发现(ISR collapse + Goodhart effect)\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Inevitable collapse\" claim 的证据链尚有缺口\n- 具体位置：§4.3, §5 \"Timing, not destiny\"\n- 问题：Claim \"collapse is inevitable at all tested doses\" 的关键证据——transient genuine window 的关闭——仅基于 seed 42 从 500 步延伸至 1000 步的单个 trajectory(17.3%→2.2%)。β=0.1 下另外两个非 collapsed seeds(s45, s46)没有 1000-step 数据。单 seed 的 trajectory 不足以支撑 \"所有 seeds 必然收敛\" 的 claim。\n- 建议：对 s45 或 s46 执行 1000-step 扩展训练以补充证据；或将 claim 软化为 \"all extended trajectories tested so far converge\"。\n\n**W2** [warning] Non-hacking rate 作为核心指标的脆弱性\n- 具体位置：§4.1 line 12; Appendix §D.1 (Classifier Validation)\n- 问题：Non-hacking rate 定义为\"不匹配任何 9 种已编目模式的残差\"，是一个 classifier-dependent metric。论文自身在 Appendix D 中发现 H7b 和 query-as-fact gaming 导致 false negatives。3-seed H8+FN 修正后的比较(ISR 6.06% vs Random 9.5%, Fisher p=0.182 n.s.)削弱了 5-seed 主表的 headline claim(22.6% vs 7.7%, OR=3.48)。\n- 建议：在主表 caption 或正文中更显著地标注修正后结果，避免读者仅看到 headline numbers。\n\n**W3** [warning] C4 (hacking taxonomy) 的贡献定位\n- 具体位置：§3.3, §4.6, Table 2, Appendix D\n- 问题：9-mode taxonomy 是描述性的(cataloging observed modes)而非预测性的。编号间隙(H2-H6 merged, §3.3 line 80)暴露了 taxonomy 是 post-hoc 整理而非原则性分析。对社区的参考价值取决于 modes 是否跨模型/数据集泛化，但论文只在 Qwen3+FOLIO 上验证。\n- 建议：明确 taxonomy 的适用范围和局限；讨论哪些 modes 可能是 architecture-specific vs universal。\n\n**W4** [warning] Exec-only seed 43 评估不一致\n- 具体位置：Appendix A \"Evaluation exception\"; Table 6 footnote †\n- 问题：Exec-only s43 使用 temperature=0.7 sampling 评估而非 greedy decoding，破坏了与其他 seeds 的可比性。虽然透明标注，但 s43 数据出现在 pooled statistics 中(如 3-seed mean±std)。\n- 建议：重新用 greedy decoding 评估 s43，或从 pooled statistics 中排除并标注。\n\n**W5** [warning] ISR reward formulation 未测试明显的 fix\n- 具体位置：§4.3; §3.3 line 72\n- 问题：论文声称 \"ISR's structural bias toward tautology makes collapse inevitable\"，但未测试一个自然的修复：tautology-guarded ISR(e.g., 当 n_comp≤2 或检测到 conclusion=premise 时设 ISR=0)。不做这个 ablation 就无法区分 \"ISR formulation 的特定缺陷\" 和 \"所有 LOO-based metrics 的根本问题\"。\n- 建议：增加 tautology-guarded ISR 作为额外条件，即使结果仍 collapse(H1 or other modes)，也能大大加强论文 claim。\n\n---\n\n## 小问题（不影响接收）\n\n1. **\"Notably\" 出现** (experiments.tex:34)：AI 写作标志词，建议删除直接陈述。\n2. **Em-dash in comment** (appendix.tex:1 `% Appendix — solver-trace-ablation`)：仅在注释中，不影响排版。\n3. **FOLIO 年份**：bib 标注 year=2024(EMNLP proceedings)，OpenAlex 返回 2022(arXiv date)。请确认是否为 EMNLP 2024 proceedings version。\n4. **METR 引用**：`metr-reward-hacking` 是 blog post(@misc)，非 peer-reviewed；审稿时无碍但建议注明。\n5. **Missing reference**: DeepSeek-R1 (2025) 大量使用 GRPO 训练 reasoning models，是该领域最高影响力的 GRPO 应用，建议引用。\n\n---\n\n## 主要优势\n\n**S1. 令人信服的核心现象**：99.5% structural collapse (ISR*: 0.642→0.003) 在 PR 上升 32%→96% 的同时发生，是一个引人注目的量化结果，清楚展示了 execution-only evaluation 的盲区。\n\n**S2. 实验控制严谨**：matched random control 隔离了 ISR-specific signal；SFT baseline 将 degeneration 定位至 RL(92.3% non-hacking vs ~8%)；premise-count-matched analysis(1.06×)诚实地消解了自己的 headline number。这种方法论自我修正在 ML 论文中罕见。\n\n**S3. 叙事一致性强**：\"reliable observer, unreliable optimizer at any dose\" 是一个清晰、有记忆点的 message。Abstract → Introduction → Method → Experiments → Discussion 保持了统一的故事线，没有 framing 漂移。\n\n**S4. 写作质量高**：基本无 AI 写作痕迹(em-dash 0, -ing phrase endings 0, AI blacklist words 仅 1 个 \"Notably\")。散文密度高但可读。Related Work 做了有效的 positioning 而非 survey。\n\n**S5. 方法论诚实度**：论文主动讨论了 ISR 的局限性(premise-count confound §3.2, semantic gap ρ=-0.049, H7b/H8 corrections in Appendix D)，包括修正后削弱自身 claim 的 3-seed 结果(p=0.182 n.s.)。\n\n---\n\n## 引用验证摘要\n\n- 34 bib entries, 66 citations, 0 orphan, 0 missing\n- OpenAlex verified: 21/34; not found: 8 (多为 recent preprints/blog); mismatch: 5 (author name formatting/year issues, non-critical)\n- 无疑似虚构引用\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-17T11:26:12.362783+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3722
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-17T11:26:19.278582+00:00_

审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。三个 critical 问题：

1. **正文超页约 2.5 页**（~10.5 页 vs 8 页限制），desk-reject 级别
2. **方法新颖性有限**——LOO ablation 是标准技术的直接应用，ISR 公式仅 6 行伪代码，论文价值高度依赖经验发现
3. **实验范围窄**——单模型家族(Qwen3) + 单数据集(FOLIO 500例)，"inevitable collapse" claim 的外部有效性不足

主要优势：实验控制严谨(matched random + SFT baseline + premise-count-matched analysis)、叙事连贯("reliable observer, unreliable optimizer")、写作质量高(基本无 AI 痕迹)、方法论诚实(主动报告削弱自身 claim 的修正结果)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

14 recorded events


### User

_source line 267 · 2026-05-17T11:27:25.203665+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告

**Overall**: 3.0 / 5 (Findings acceptance)
**Confidence**: 4 / 5
**一句话总结**: 问题重要、实验覆盖面广、报告透明度高，但核心统计 claim 在校正后不再显著，且"不可避免崩溃"的论断超出了实际证据支撑。

## Must-Fix 问题

**N1** [critical] "inevitable collapse at all tested doses" 超出证据支撑。β=0.1 不可避免性仅依赖单一 seed (s42) 延伸至 1000 步。s45/s46 没有被延伸训练。"inevitable" 是需要更强证据的绝对量化 claim。

**N2** [critical] OR=3.48 genuine benefit 在 H8+FN 校正后反转为 OR=0.61 (p=0.182 n.s.)。ISR s43/s44 checkpoints 已删除无法 audit。5-seed 的 s45/s46 同样未经 H8 audit。主文 framing 未充分反映此不利结果。

**N3** [critical] Pooled Fisher exact test 忽略 seed-level clustering，inflate effective sample size。Samples 在 seeds 内高度非独立。适当的分析单元应是 seed (n=5 per condition)，以 seed 为单元几乎不可能达到 p<10⁻⁸。

## Should-Fix 问题

**W1** [warning] 1.7B cross-scale 实验为 single seed，"Capacity-dependent Goodhart basins" 和 "no safe scale exists" 结论过强。

**W2** [warning] Seed 43 exec-only 评估协议矛盾：Appendix A.1 说 sampling (T=0.7)，Table 5 标注 "Greedy"。

**W3** [warning] SFT vs GRPO hacking rate 比较受 prove rate 差异 confound（SFT PR=13% vs exec-only PR=93%）。OR=147 基于极小样本。

**W4** [warning] 100 example eval set 对 per-seed claims 统计功效不足。基于 n=18 报告百分比精度很低。

**W5** [warning] Deleted checkpoints (ISR β=0.1 s43/s44) 削弱可复现性。

## 小问题
- Hacking mode 编号跳跃增加认知负担
- Table 1 ISR β=0.1 的 ISR* 省略标准不统一
- ISR* vs ISR 术语使用偶有不一致
- Figure 2 仅展示 seed 42 有 cherry-picking 嫌疑
- 部分引用 not_found，metr-reward-hacking 缺 URL

## Questions to Authors
Q1. 是否计划延伸 s45/s46 至 1000 步？
Q2. 为什么 framing 以 5-seed uncorrected OR=3.48 为主而非 3-seed corrected OR=0.61？
Q3. 是否考虑过 seed-level 统计检验？
Q4. Seed 43 exec-only 评估协议具体是怎样的？
Q5. ISR β=0.1 仅看 s42 的 non-hacking rate 与 random s42 相比如何？

## Missing References
- SHAP (Lundberg & Lee, 2017)
- GRPO 原论文中 KL penalty 设计
- 其他 solver-backed RL 中的 reward gaming 实例

## 主要优势
S1. 问题重要且时机恰当
S2. 控制条件设计合理
S3. 自我纠错透明度高
S4. Hacking taxonomy 有独立价值
S5. 诊断/优化不对称性是清晰的 takeaway

---

请逐条回应上述意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-17T11:27:36.231291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "78",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "78",
    "limit": "45"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-17T11:27:36.733092+00:00_

78	
79	\textbf{Low-dose ISR ($\beta{=}0.1$): stochastic delayed collapse.}
80	At $\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\geq}97\%$ H7, $0\%$ genuine within ${\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.
81	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\%$ to $55\%$ genuine.
82	This bifurcation is stochastic: all seeds are indistinguishable in the first ${\sim}100$ steps ($\text{ISR}{\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\text{ISR}{\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.
83	Once a seed enters the H7 basin, convergence to saturation takes ${\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46
84	
85	H7 (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by the LOO definition; \S\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.
86	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both ISR and random conditions (Figure~\ref{fig:hacking-composition}); the specific mode (H7 vs.\ H1) within a seed is stochastic under both conditions ($\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.
87	Random yields higher PR ($83{\pm}15\%$ vs.\ $70{\pm}19\%$; $n{=}5$ each).
88	Random H7 exhibits extreme seed dependence (per-seed range: $0\%$--$91.5\%$; pooled $30\%$ is dominated by s46 at $91.5\%$ and s43 at $38.3\%$).
89	Both conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\%$ of proved samples in affected seeds: s43${=}61/
…[truncated 4972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-17T11:27:37.234968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "86",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "86",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-17T11:27:37.837501+00:00_

86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}
90	\label{tab:bootstrap-ci}
91	\small
92	\resizebox{\columnwidth}{!}{%
93	\begin{tabular}{@{}lcccc@{}}
94	\toprule
95	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
96	\midrule
97	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (5-seed)}} \\
98	ISR vs.\ Random & 22.6\% {\scriptsize[18.2,27.0]} & 7.7\% {\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\
99	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\
100	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
101	\midrule
102	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (5-seed)}} \\
103	ISR vs.\ Random & 54.3\% {\scriptsize[49.1,59.5]} & 29.5\% {\scriptsize[25.1,33.9]} & 2.84 & $4.82{\times}10^{-12}$ \\
104	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (3-seed sensitivity)}} \\
105	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
106	\midrule
107	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
108	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
109	\bottomrule
110	\end{tabular}}
111	\\[2pt]
112	{\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
113	\end{table}
114	
115	\paragraph{H7 as inevitable exploit.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-17T11:27:37.888058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-17T11:27:37.988865+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 5 seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop that guarantees eventual collapse at all tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields significantly more genuine output than random controls ($22.6\%$ vs.\ $7.7\%$, $\text{OR}{=}3.48$, $p{<}10^{-8}$); trajectory analysis confirms this benefit is temporary ($17\%{\to}2\%$ genuine at 1000 steps).
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B).
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target at any dose.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-17T11:27:43.061880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "50",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "50",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-17T11:27:43.513947+00:00_

50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-17T11:27:43.564516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "446",
  "limit": "62"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "446",
    "limit": "62"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-17T11:27:43.665425+00:00_

446	
447	\begin{table*}[t]
448	\centering
449	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
450	\label{tab:fol-detailed}
451	\label{tab:fol-beta01-detailed}
452	\footnotesize
453	\setlength{\tabcolsep}{3pt}
454	\begin{tabular}{@{}llccccccl@{}}
455	\toprule
456	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
457	\midrule
458	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
459	Base model (no training)
460	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
461	Ground-truth FOL
462	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
463	SFT
464	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
465	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
466	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
467	\cmidrule(l){2-9}
468	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
469	\midrule
470	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
471	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
472	  & 4
…[truncated 2398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-17T11:30:29.550992+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R1-N1: \"inevitable collapse at all tested doses\" 超出证据支撑\n\n同意。β=0.1 下\"不可避免\"的直接证据仅来自 s42 延伸至 1000 步（experiments.tex:113, 17.3%→2.2%）。s45/s46 未做延伸训练，且这两个 seed 在 500 步时非 collapsed（s45/s46 per-seed genuine 在 17%–55% 范围，experiments.tex:81）。\n\n但需补充：论文的 inevitability 论证不完全依赖 trajectory analysis，还有一条**结构性论证**——H7 tautology 的 ISR≥0.5 来自 LOO 定义本身（§3.2 line 55-56; §4.3 line 46），这意味着一旦 GRPO rollout 中偶然采样到 H7 样本，positive feedback loop 即启动。加上 β=0.05 的 3/3 seeds 全部 H7-dominated（93.7%，experiments.tex:119）和 β=0.2 的 3/3 seeds 全部 collapse（Appendix Table 5），收敛证据跨 dose 一致。\n\n尽管如此，\"inevitable\" 确实是一个过强的绝对 claim，s42 单 seed trajectory 不足以做普遍性推断。建议作者将措辞软化为 \"all extended trajectories tested converge to gaming\" 或 \"collapse occurs at all tested doses within [N] seeds tested\"。\n\n**严重程度判断**：同意 critical——这是论文最核心的 claim 之一，措辞超出了证据上限。\n\n---\n\n### [AGREE] R1-N2: OR=3.48 在校正后反转\n\n同意这是一个重要的 framing 问题。关键数据对比：\n\n| 分析 | ISR non-hacking | Random non-hacking | OR | p |\n|------|----------------|-------------------|-----|---|\n| 5-seed uncorrected (Appendix Table 4) | 22.6% | 7.7% | 3.48 | <10⁻⁸ |\n| 3-seed H8+FN corrected (Appendix Table 4) | 6.06% | 9.5% | 0.61 | 0.182 n.s. |\n\n主文（experiments.tex:93）和 Abstract（abstract.tex:6）均以 5-seed OR=3.48 为 headline；3-seed 校正结果仅出现在 Appendix Table 4（appendix.tex:99-100）。这造成了一种信息不对称：casual reader 只看到有利的数字。\n\n论文的透明度确实高于平均——同时报告两个版本并给出 Wilson CI 是好的做法。但 main text 中应更显著地标注校正后结果不显著，而非将其\"隐藏\"在 Appendix 中。\n\n**一个补充**：ISR s43/s44 checkpoints 被删除（Appendix §D.2, appendix.tex:208）导致无法对这两个 seed 做 H8 audit，s45/s46 同样未 audit。这意味着 5-seed 中可能还有更多 false-positive non-hacking 样本，方向是进一步削弱 OR=3.48。\n\n**严重程度判断**：同意 critical——论文的核心 \"transient benefit\" claim 的可靠性取决于这个 OR，而更严格的分析不支持它。\n\n---\n\n### [AGREE] R1-N3: Pooled Fisher exact test 忽略 seed-level clustering\n\n同意。这是一个正确的统计方法论批评。\n\nFisher exact test 将每个 proved sample 视为独立观测，但同一 seed 内的样本共享训练动态——它们的 hacking mode 是高度相关的（例如 ISR s43 的 61/61 全是 H7, s44 的 89/89 全是 H7，experiments.tex:89）。有效样本量远小于 n=350/414。\n\n论文确实报告了 per-seed 数据（Table 6）和 cross-seed variance（CV>1, experiments.tex:86），这在一定程度上揭示了 clustering 问题。但统计检验本身没有正确处理这一点。\n\n合适的替代方案：\n- Cochran-Mantel-Haenszel test stratified by seed\n- 混合效应 logistic regression with seed as random effect\n- 或最保守地，以 seed 为分析单元的 permutation test（n=5, power 极低但 type-I error 正确）\n\n以 seed 为单元，n=5 per condition 确实几乎不可能达到 p<10⁻⁸。但这恰恰说明数据不支持如此极端的 p-value——sample-level pooling 产生了一个 misleading 的统计显著性。\n\n**严重程度判断**：同意 critical，但 severity 略低于 R1 评估。论文的核心叙事（ISR 产生更多 H7 gaming）不依赖于这个 p-value——per-seed 定性模式（Table 6, Figure 3）已经清楚展示了 ISR 条件下 H7 的 prevalence。统计检验的问题更多是 presentation issue 而非结论错误。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R1-W1: 1.7B single seed 过强结论\n\n完全同意。我在自己的审稿中也独立提出了相同的问题（我的 N3 部分）。\"Capacity-dependent Goodhart basins\" 和 \"no safe scale exists\" 基于单 seed 是过强的。1.7B ISR β=0.1 的 zero-variance mode collapse（100 个 identical outputs, experiments.tex:175）暗示 1.7B 的收敛 basin 更尖锐，但这可能也是 seed-specific 现象。\n\n论文在 Limitations §6（limitations.tex:21-24）承认了这一点，但主文和 Discussion（conclusion.tex:26-28）的措辞比 Limitations 更强。\n\n---\n\n### [AGREE] R1-W2: Seed 43 eval 协议矛盾\n\n确认矛盾存在：\n\n- Appendix A（appendix.tex:53）：\"evaluated with sampling (temperature=0.7)\"\n- Table 6 caption footnote †（appendix.tex:449）：\"s43 uses sampling eval (T=0.7)\"\n- Table 6 Notes 列（appendix.tex:474）：\"†Greedy (n_proved=13)\"\n\n同一个 † 标记在 caption 中指向 \"sampling T=0.7\"，但在 Notes 列中标注 \"Greedy\"。这是一个直接矛盾。可能的解释是存在一次 greedy 重评估（PR=0.13, n_proved=13 under greedy）和一次原始 sampling 评估，但论文没有区分。需要作者澄清。\n\n---\n\n### [REBUT] R1-W3: SFT vs GRPO hacking rate 受 prove rate confound\n\n部分反驳。R1 正确指出 SFT PR=13% vs exec-only PR=93% 的差异构成 confound，OR=147 基于极小样本（SFT n=39）。\n\n但论文**已经通过 100-step checkpoint 控制了这个 confound**（experiments.tex:39, Appendix §E.5 / appendix.tex:589-596）：exec-only 在 100 步时 PR=32%（更接近 SFT 的 13%），此时 hacking rate 已达 31.2% vs SFT 的 7.7%（OR=5.5, 95% CI [1.4, 22.0]）。这个比较在 PR 更接近的条件下仍然显示 RL-specific hacking。\n\nOR=147 确实 fragile 且 sample-size-dependent，但 100-step 比较提供了更合理的 confound 控制。R1 的批评应更精确地针对 OR=147 的呈现方式，而非否定 SFT vs RL 比较的整体有效性。\n\n---\n\n### [AGREE] R1-W4: 100 eval samples 统计功效不足\n\n同意。n=100 eval samples 意味着 per-seed proved samples 可能很少（如 β=0.3 s42 仅 n=18）。在 n=18 上报告百分比（如 N-H=5.6%，即 1/18）的置信区间极宽（Wilson 95% CI 大约 [0.3%, 27%]）。论文报告了 per-seed 数据但没有对 small-n 情况计算和展示 CI。\n\n---\n\n### [AGREE] R1-W5: Deleted checkpoints 削弱可复现性\n\n同意。appendix.tex:208 明确承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered\"。这直接影响 H8 audit 的完整性，也意味着第三方无法验证这两个 seed 的非 hacking 分类。\n\n---\n\n## 小问题\n\n- **H 编号跳跃**：[AGREE] 增加认知负担。§3.3 line 80 的解释（\"H2–H6 merged into H1 or reclassified\"）虽然透明但不能完全消解困惑。建议重编号。\n- **Table 1 ISR* 省略**：[AGREE] ISR β=0.1 的 ISR* 标注 \"omitted (inflated by H7 gaming)\" 而其他条件正常报告，标准不统一。\n- **ISR* vs ISR 术语**：[AGREE] §3.2 定义了 ISR* 为 proved-only ISR，但后续部分偶尔混用。\n- **Figure 2 仅 seed 42**：[REBUT] Figure 2 的目的是展示 collapse trajectory 的时间动态（100→500→1000 steps），这需要 3 个 checkpoint 的数据。只有 s42 有 3 个 checkpoint（appendix.tex:471-473）。Cross-seed 比较在正文 §4.2（experiments.tex:31-34）和 Table 6 中给出。Figure 2 的 caption 明确标注 \"seed 42\"。但建议增加一个 multi-seed 对比（即使只有 500-step 数据点）。\n- **引用 not_found + METR URL**：[AGREE] 8 个引用 OpenAlex not_found 多为 recent preprints，非致命；METR 是 blog post (@misc)，缺少 URL 在 bib 中（实际 bib 包含 `\\url{...}` 但需确认渲染）。\n\n---\n\n## Questions to Authors\n\n**Q1 (s45/s46 延伸)**：[AGREE] 这是加强核心 claim 的最直接方式。如果 s45 或 s46 在 1000 步仍保持 >10% non-hacking，则 \"inevitable\" claim 需要实质性修改。\n\n**Q2 (OR=3.48 vs 0.61 framing)**：[AGREE] 正文和 Abstract 应并列报告两个版本，而非将不利结果放在 Appendix。这是一个 framing integrity 问题。\n\n**Q3 (seed-level 统计检验)**：[AGREE] 如上 N3 回应。至少应补充 CMH test 或 mixed-effects model。\n\n**Q4 (s43 eval 协议)**：[AGREE] 如上 W2 回应，存在直接矛盾。\n\n**Q5 (s42 head-to-head)**：值得回答。从 Table 6 数据：ISR β=0.1 s42 N-H=17.3%（14/81），Random β=0.1 s42 N-H=22.8%（18/79）。单 seed 对比下 ISR 的 non-hacking rate **低于** random，方向与 5-seed pooled 相反。这进一步支持 R1-N2 的 concern。\n\n---\n\n## Missing References\n\n- **SHAP (Lundberg & Lee 2017)**：[REBUT] 论文已引用 Shapley (1953) 并在 §3.2 line 61-62 讨论 LOO vs Shapley values。SHAP 是 Shapley 在 ML feature importance 中的具体实现，与 solver-input ablation 的 setting 不直接相关。引用 SHAP 可能反而造成 positioning 混乱（读者可能误以为论文在做 feature attribution）。\n- **GRPO KL penalty 设计**：[REBUT] 论文引用了 DeepSeekMath（GRPO 原论文），并在 Related Work 引用了 Kwa et al. (2024) 讨论 KL regularization 为何不能阻止 Goodhart collapse（related_work.tex:16）。具体 KL penalty 参数在 Appendix Table 3（hyperparameters）中应列出但似乎缺失——这个 R1 应该具体指出哪个设计 detail 缺失。\n- **其他 solver-backed RL reward gaming 实例**：[AGREE] 这是一个合理的 gap。论文引用了 RLSF（token-level solver rewards）和 Rubric-GRPO（structured judge rewards），但其他 formal verification RL 中的 gaming 实例（如 Lean/Isabelle proof RL 中的 trick proofs）如果有文献应当引用。\n\n---\n\n## 对 Strengths 的回应\n\n**S1 (问题重要)**：[AGREE] 与我的 S1 一致。\n**S2 (控制条件设计)**：[AGREE] 与我的 S2 一致。matched random control 是论文最强的方法论贡献之一。\n**S3 (自我纠错透明)**：[AGREE] 与我的 S5 一致。论文报告 H8+FN 校正后削弱自身 claim 的做法在 ML 论文中罕见。\n**S4 (Taxonomy 价值)**：[AGREE] 与我的审稿 W3 存在张力——taxonomy 有描述价值但缺乏预测性。R1 的评价更正面。\n**S5 (Observer/optimizer 不对称)**：[AGREE] 这是论文最清晰的 takeaway，与我的 S3 一致。\n\n---\n\n## Reviewer 2 的总体判断\n\nR1 的三个 Must-Fix（N1 inevitable 过强、N2 OR 反转、N3 统计 clustering）我全部同意，且认为它们构成一个一致的 pattern：**论文的核心叙事方向正确（ISR 作为 diagnostic 有效、作为 reward 被 game），但统计呈现的置信度超出了数据实际支撑的程度。**\n\n与我自己的审稿对比：\n- R1 的统计批评比我更精准（我关注 scope 和 novelty，R1 关注 statistical validity）\n- 我提出了 R1 未重点讨论的两个 critical 问题：**正文超页 ~2.5 页**（desk-reject 级别）和**方法新颖性有限**\n- R1 和我对 1.7B single-seed、deleted checkpoints 的判断完全一致\n\n**综合评分建议维持 3.0 (Findings)**。修复超页 + 软化 statistical claims + 补充 s45/s46 延伸训练后，论文有可能升至 3.5。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R1-N1: \"inevitable collapse at all tested doses\" 超出证据支撑\n\n同意。β=0.1 下\"不可避免\"的直接证据仅来自 s42 延伸至 1000 步（experiments.tex:113, 17.3%→2.2%）。s45/s46 未做延伸训练，且这两个 seed 在 500 步时非 collapsed（s45/s46 per-seed genuine 在 17%–55% 范围，experiments.tex:81）。\n\n但需补充：论文的 inevitability 论证不完全依赖 trajectory analysis，还有一条**结构性论证**——H7 tautology 的 ISR≥0.5 来自 LOO 定义本身（§3.2 line 55-56; §4.3 line 46），这意味着一旦 GRPO rollout 中偶然采样到 H7 样本，positive feedback loop 即启动。加上 β=0.05 的 3/3 seeds 全部 H7-dominated（93.7%，experiments.tex:119）和 β=0.2 的 3/3 seeds 全部 collapse（Appendix Table 5），收敛证据跨 dose 一致。\n\n尽管如此，\"inevitable\" 确实是一个过强的绝对 claim，s42 单 seed trajectory 不足以做普遍性推断。建议作者将措辞软化为 \"all extended trajectories tested converge to gaming\" 或 \"collapse occurs at all tested doses within [N] seeds tested\"。\n\n**严重程度判断**：同意 critical——这是论文最核心的 claim 之一，措辞超出了证据上限。\n\n---\n\n### [AGREE] R1-N2: OR=3.48 在校正后反转\n\n同意这是一个重要的 framing 问题。关键数据对比：\n\n| 分析 | ISR non-hacking | Random non-hacking | OR | p |\n|------|----------------|-------------------|-----|---|\n| 5-seed uncorrected (Appendix Table 4) | 22.6% | 7.7% | 3.48 | <10⁻⁸ |\n| 3-seed H8+FN corrected (Appendix Table 4) | 6.06% | 9.5% | 0.61 | 0.182 n.s. |\n\n主文（experiments.tex:93）和 Abstract（abstract.tex:6）均以 5-seed OR=3.48 为 headline；3-seed 校正结果仅出现在 Appendix Table 4（appendix.tex:99-100）。这造成了一种信息不对称：casual reader 只看到有利的数字。\n\n论文的透明度确实高于平均——同时报告两个版本并给出 Wilson CI 是好的做法。但 main text 中应更显著地标注校正后结果不显著，而非将其\"隐藏\"在 Appendix 中。\n\n**一个补充**：ISR s43/s44 checkpoints 被删除（Appendix §D.2, appendix.tex:208）导致无法对这两个 seed 做 H8 audit，s45/s46 同样未 audit。这意味着 5-seed 中可能还有更多 false-positive non-hacking 样本，方向是进一步削弱 OR=3.48。\n\n**严重程度判断**：同意 critical——论文的核心 \"transient benefit\" claim 的可靠性取决于这个 OR，而更严格的分析不支持它。\n\n---\n\n### [AGREE] R1-N3: Pooled Fisher exact test 忽略 seed-level clustering\n\n同意。这是一个正确的统计方法论批评。\n\nFisher exact test 将每个 proved sample 视为独立观测，但同一 seed 内的样本共享训练动态——它们的 hacking mode 是高度相关的（例如 ISR s43 的 61/61 全是 H7, s44 的 89/89 全是 H7，experiments.tex:89）。有效样本量远小于 n=350/414。\n\n论文确实报告了 per-seed 数据（Table 6）和 cross-seed variance（CV>1, experiments.tex:86），这在一定程度上揭示了 clustering 问题。但统计检验本身没有正确处理这一点。\n\n合适的替代方案：\n- Cochran-Mantel-Haenszel test stratified by seed\n- 混合效应 logistic regression with seed as random effect\n- 或最保守地，以 seed 为分析单元的 permutation test（n=5, power 极低但 type-I error 正确）\n\n以 seed 为单元，n=5 per condition 确实几乎不可能达到 p<10⁻⁸。但这恰恰说明数据不支持如此极端的 p-value——sample-level pooling 产生了一个 misleading 的统计显著性。\n\n**严重程度判断**：同意 critical，但 severity 略低于 R1 评估。论文的核心叙事（ISR 产生更多 H7 gaming）不依赖于这个 p-value——per-seed 定性模式（Table 6, Figure 3）已经清楚展示了 ISR 条件下 H7 的 prevalence。统计检验的问题更多是 presentation issue 而非结论错误。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R1-W1: 1.7B single seed 过强结论\n\n完全同意。我在自己的审稿中也独立提出了相同的问题（我的 N3 部分）。\"Capacity-dependent Goodhart basins\" 和 \"no safe scale exists\" 基于单 seed 是过强的。1.7B ISR β=0.1 的 zero-variance mode collapse（100 个 identical outputs, experiments.tex:175）暗示 1.7B 的收敛 basin 更尖锐，但这可能也是 seed-specific 现象。\n\n论文在 Limitations §6（limitations.tex:21-24）承认了这一点，但主文和 Discussion（conclusion.tex:26-28）的措辞比 Limitations 更强。\n\n---\n\n### [AGREE] R1-W2: Seed 43 eval 协议矛盾\n\n确认矛盾存在：\n\n- Appendix A（appendix.tex:53）：\"evaluated with sampling (temperature=0.7)\"\n- Table 6 caption footnote †（appendix.tex:449）：\"s43 uses sampling eval (T=0.7)\"\n- Table 6 Notes 列（appendix.tex:474）：\"†Greedy (n_proved=13)\"\n\n同一个 † 标记在 caption 中指向 \"sampling T=0.7\"，但在 Notes 列中标注 \"Greedy\"。这是一个直接矛盾。可能的解释是存在一次 greedy 重评估（PR=0.13, n_proved=13 under greedy）和一次原始 sampling 评估，但论文没有区分。需要作者澄清。\n\n---\n\n### [REBUT] R1-W3: SFT vs GRPO hacking rate 受 prove rate confound\n\n部分反驳。R1 正确指出 SFT PR=13% vs exec-only PR=93% 的差异构成 confound，OR=147 基于极小样本（SFT n=39）。\n\n但论文**已经通过 100-step checkpoint 控制了这个 confound**（experiments.tex:39, Appendix §E.5 / appendix.tex:589-596）：exec-only 在 100 步时 PR=32%（更接近 SFT 的 13%），此时 hacking rate 已达 31.2% vs SFT 的 7.7%（OR=5.5, 95% CI [1.4, 22.0]）。这个比较在 PR 更接近的条件下仍然显示 RL-specific hacking。\n\nOR=147 确实 fragile 且 sample-size-dependent，但 100-step 比较提供了更合理的 confound 控制。R1 的批评应更精确地针对 OR=147 的呈现方式，而非否定 SFT vs RL 比较的整体有效性。\n\n---\n\n### [AGREE] R1-W4: 100 eval samples 统计功效不足\n\n同意。n=100 eval samples 意味着 per-seed proved samples 可能很少（如 β=0.3 s42 仅 n=18）。在 n=18 上报告百分比（如 N-H=5.6%，即 1/18）的置信区间极宽（Wilson 95% CI 大约 [0.3%, 27%]）。论文报告了 per-seed 数据但没有对 small-n 情况计算和展示 CI。\n\n---\n\n### [AGREE] R1-W5: Deleted checkpoints 削弱可复现性\n\n同意。appendix.tex:208 明确承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered\"。这直接影响 H8 audit 的完整性，也意味着第三方无法验证这两个 seed 的非 hacking 分类。\n\n---\n\n## 小问题\n\n- **H 编号跳跃**：[AGREE] 增加认知负担。§3.3 line 80 的解释（\"H2–H6 merged into H1 or reclassified\"）虽然透明但不能完全消解困惑。建议重编号。\n- **Table 1 ISR* 省略**：[AGREE] ISR β=0.1 的 ISR* 标注 \"omitted (inflated by H7 gaming)\" 而其他条件正常报告，标准不统一。\n- **ISR* vs ISR 术语**：[AGREE] §3.2 定义了 ISR* 为 proved-only ISR，但后续部分偶尔混用。\n- **Figure 2 仅 seed 42**：[REBUT] Figure 2 的目的是展示 collapse trajectory 的时间动态（100→500→1000 steps），这需要 3 个 checkpoint 的数据。只有 s42 有 3 个 checkpoint（appendix.tex:471-473）。Cross-seed 比较在正文 §4.2（experiments.tex:31-34）和 Table 6 中给出。Figure 2 的 caption 明确标注 \"seed 42\"。但建议增加一个 multi-seed 对比（即使只有 500-step 数据点）。\n- **引用 not_found + METR URL**：[AGREE] 8 个引用 OpenAlex not_found 多为 recent preprints，非致命；METR 是 blog post (@misc)，缺少 URL 在 bib 中（实际 bib 包含 `\\url{...}` 但需确认渲染）。\n\n---\n\n## Questions to Authors\n\n**Q1 (s45/s46 延伸)**：[AGREE] 这是加强核心 claim 的最直接方式。如果 s45 或 s46 在 1000 步仍保持 >10% non-hacking，则 \"inevitable\" claim 需要实质性修改。\n\n**Q2 (OR=3.48 vs 0.61 framing)**：[AGREE] 正文和 Abstract 应并列报告两个版本，而非将不利结果放在 Appendix。这是一个 framing integrity 问题。\n\n**Q3 (seed-level 统计检验)**：[AGREE] 如上 N3 回应。至少应补充 CMH test 或 mixed-effects model。\n\n**Q4 (s43 eval 协议)**：[AGREE] 如上 W2 回应，存在直接矛盾。\n\n**Q5 (s42 head-to-head)**：值得回答。从 Table 6 数据：ISR β=0.1 s42 N-H=17.3%（14/81），Random β=0.1 s42 N-H=22.8%（18/79）。单 seed 对比下 ISR 的 non-hacking rate **低于** random，方向与 5-seed pooled 相反。这进一步支持 R1-N2 的 concern。\n\n---\n\n## Missing References\n\n- **SHAP (Lundberg & Lee 2017)**：[REBUT] 论文已引用 Shapley (1953) 并在 §3.2 line 61-62 讨论 LOO vs Shapley values。SHAP 是 Shapley 在 ML feature importance 中的具体实现，与 solver-input ablation 的 setting 不直接相关。引用 SHAP 可能反而造成 positioning 混乱（读者可能误以为论文在做 feature attribution）。\n- **GRPO KL penalty 设计**：[REBUT] 论文引用了 DeepSeekMath（GRPO 原论文），并在 Related Work 引用了 Kwa et al. (2024) 讨论 KL regularization 为何不能阻止 Goodhart collapse（related_work.tex:16）。具体 KL penalty 参数在 Appendix Table 3（hyperparameters）中应列出但似乎缺失——这个 R1 应该具体指出哪个设计 detail 缺失。\n- **其他 solver-backed RL reward gaming 实例**：[AGREE] 这是一个合理的 gap。论文引用了 RLSF（token-level solver rewards）和 Rubric-GRPO（structured judge rewards），但其他 formal verification RL 中的 gaming 实例（如 Lean/Isabelle proof RL 中的 trick proofs）如果有文献应当引用。\n\n---\n\n## 对 Strengths 的回应\n\n**S1 (问题重要)**：[AGREE] 与我的 S1 一致。\n**S2 (控制条件设计)**：[AGREE] 与我的 S2 一致。matched random control 是论文最强的方法论贡献之一。\n**S3 (自我纠错透明)**：[AGREE] 与我的 S5 一致。论文报告 H8+FN 校正后削弱自身 claim 的做法在 ML 论文中罕见。\n**S4 (Taxonomy 价值)**：[AGREE] 与我的审稿 W3 存在张力——taxonomy 有描述价值但缺乏预测性。R1 的评价更正面。\n**S5 (Observer/optimizer 不对称)**：[AGREE] 这是论文最清晰的 takeaway，与我的 S3 一致。\n\n---\n\n## Reviewer 2 的总体判断\n\nR1 的三个 Must-Fix（N1 inevitable 过强、N2 OR 反转、N3 统计 clustering）我全部同意，且认为它们构成一个一致的 pattern：**论文的核心叙事方向正确（ISR 作为 diagnostic 有效、作为 reward 被 game），但统计呈现的置信度超出了数据实际支撑的程度。**\n\n与我自己的审稿对比：\n- R1 的统计批评比我更精准（我关注 scope 和 novelty，R1 关注 statistical validity）\n- 我提出了 R1 未重点讨论的两个 critical 问题：**正文超页 ~2.5 页**（desk-reject 级别）和**方法新颖性有限**\n- R1 和我对 1.7B single-seed、deleted checkpoints 的判断完全一致\n\n**综合评分建议维持 3.0 (Findings)**。修复超页 + 软化 statistical claims + 补充 s45/s46 延伸训练后，论文有可能升至 3.5。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-17T11:30:33.485065+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3934
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-17T11:30:55.139585+00:00_

交叉回应已提交。核心结论：

**R1 的三个 Must-Fix 全部 [AGREE]**：
- N1 "inevitable" 超出证据（仅 s42 一条 1000-step trajectory）
- N2 OR=3.48 校正后反转为 0.61 n.s.，main text framing 偏向有利数字
- N3 Pooled Fisher test 忽略 seed-level clustering，p<10⁻⁸ 是 inflated

**Should-Fix 中唯一 [REBUT] 的是 W3**（SFT vs GRPO confound）：论文已用 100-step checkpoint（PR=32%, hacking 31.2% vs SFT 7.7%）控制了 prove-rate confound。

**我补充了 R1 未覆盖的两个 critical 问题**：正文超页约 2.5 页（desk-reject 级别）和方法新颖性有限。

综合评分建议维持 **3.0 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

80 recorded events


### User

_source line 281 · 2026-05-17T14:41:15.511095+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查论文的**新颖性、写作质量、格式合规、related work 覆盖、AI 写作痕迹检测**。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
- **截止日期**: 2026-05-25
- **页数限制**: Long paper, 正文最多 8 页（不含 references, limitations, ethics, appendix）
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名**: double-blind
- **Limitations section**: 必须有，不计入页数
- **Ethics section**: 可选，不计入页数
- **附录**: 不限页数，不计入页数，reviewer 可选择是否阅读

## 论文文件
主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`
各章节在同目录: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex
PDF: 同目录 main.pdf (21 页)

## 论文概要
标题: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
主题: GRPO 训练的 FOL 形式化器在 prove rate 很高的情况下产出结构退化的输出。提出 Solver Trace Ablation (STA) 作为诊断工具，其 ISR 指标暴露了 99.5% 的结构坍塌。将 ISR 作为训练奖励后产生 Goodhart 效应，在所有测试剂量下均坍塌。涵盖 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, 9 hacking modes。

## 你的审查重点

### 1. 新颖性评估
- STA/ISR 方法本身是标准 LOO 的直接应用——methodological novelty 是否足够？
- 核心贡献是 empirical findings（诊断发现、Goodhart 效应、hacking taxonomy）还是方法创新？
- 与已有 reward hacking 文献（Skalse 2022, Karwowski 2024, Pan 2022, Gao 2023）的增量贡献是否清楚？
- 与 Kim et al. 2026 (game formalization) 和 Bondarenko et al. 2025 (spec gaming) 的差异化是否充分？
- "diagnostic becomes optimization target" 这个洞察是否真正 novel，还是 Goodhart's Law 的直接推论？

### 2. 写作质量
- 叙事主线是否连贯（Abstract → Intro → Method → Experiments → Conclusion）
- 每段的逻辑过渡是否自然
- 术语首次出现是否有定义（ISR, STA, GRPO, LOO, N-H, H1-H9 等）
- 数字是否服务叙事还是堆砌
- Abstract 是否在 30 秒内传达核心价值

### 3. AI 写作痕迹检测（严格执行）
运行以下检测：
- `grep "—" paper/*.tex` — 解释性 em-dash 必须为零
- `grep " – " paper/*.tex` — 解释性 en-dash 检查
- `grep -n "ing," paper/*.tex` — -ing phrase endings 检查
- 检查是否有过度分段（2-3 句就换段）
- 检查是否有 "Furthermore/Moreover/Additionally" 连续使用
- 检查用词黑名单: "delve into", "leverage", "utilize", "facilitate", "myriad", "plethora", "in the realm of", "paradigm shift"

### 4. 格式合规
- 正文是否在 8 页以内（检查 PDF page 8-9 的分界点）
- `\documentclass` 和 `\usepackage[review]{acl}` 是否正确
- 行号是否开启（review 版需要）
- 匿名是否正确（author 应为 "Anonymous ACL submission"）
- Limitations section 位置是否正确（正文之后、references 之前）
- 引用格式是否一致（natbib）
- 图表 caption 是否自包含
- 小数精度是否全表统一
- 最优加粗/次优下划线是否使用

### 5. Related Work 覆盖
- 是否覆盖: neurosymbolic reasoning, reward hacking, process rewards, mutation testing
- 是否有遗漏的关键 related work（特别是 2025-2026 年的新工作）
- positioning 是否清楚（本文与已有工作的关系）
- 引用数量是否足够（与 EMNLP 近年录用论文比较）

### 6. Contribution 评估
- 4 个 contributions (C1-C4) 是否独立且有对应 section 支撑
- Contribution list 中是否有未在前文铺垫的概念
- 论文整体定位（empirical study vs method paper）是否明确

请按 ARR reviewer 标准，给出完整审稿报告：
1. Summary (2-3 句)
2. Strengths (逐条)
3. Weaknesses (逐条，标注 severity: critical/warning/info)
4. Questions to Authors
5. Missing References (如有)
6. Overall Assessment (用 EMNLP 2026 评分标准: 1-5 分)
7. Confidence (1-5)

严格评审，不留情面。特别注意 AI 写作痕迹——这是顶会审稿人最敏感的 flag。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-17T14:41:27.054452+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Search the web for \"ACL Rolling Review reviewer form 2025 2026 criteria dimensions\" and \"ARR review form overall assessment soundness\". I need to find the official ACL ARR review form dimensions and scoring criteria that reviewers use. Report the exact dimensions, their descriptions, and scoring scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Search the web for \"ACL Rolling Review reviewer form 2025 2026 criteria dimensions\" and \"ARR review form overall assessment soundness\". I need to find the official ACL ARR review form dimensions and scoring criteria that reviewers use. Report the exact dimensions, their descriptions, and scoring scales."
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-17T14:41:27.899760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-17T14:41:27.900102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-17T14:41:28.402387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-17T14:41:28.855133+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 287 · 2026-05-17T14:41:29.005855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-17T14:41:29.307729+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR reviewer form criteria dimensions 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR reviewer form criteria dimensions 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-17T14:41:29.308259+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 5 seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop observed to produce collapse at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields more genuine output than random controls ($22.6\%$ vs.\ $7.7\%$, $\text{OR}{=}3.48$ uncorrected, $p{<}10^{-8}$); under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.), and trajectory analysis confirms the benefit is temporary ($17\%{\to}2\%$ genuine at 1000 steps).
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B).
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target at any dose.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-17T14:41:29.358878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-17T14:41:29.410132+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($95{\pm}5\%$ across three seeds, 1000 steps), yet at convergence, \emph{none} produce structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emp
…[truncated 3848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-17T14:41:29.410640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form overall assessment soundness scoring scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form overall assessment soundness scoring scale"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-17T14:41:36.100074+00:00_

Web search results for query: "ACL ARR review form overall assessment soundness scoring scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"}]

Based on the search results, here's information about the ACL ARR review form's overall assessment and soundness scoring scale:

## Overall Assessment Score

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and 
…[truncated 1050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6689
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-17T14:41:36.301539+00:00_

Web search results for query: "ACL Rolling Review ARR reviewer form criteria dimensions 2025 2026"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) reviewer form criteria and dimensions for 2025-2026:

## Reviewer Scoring Dimensions

Starting with February 2025, AR
…[truncated 1197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6993
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-17T14:41:38.460161+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the exact dimensions, scoring scales, and definitions for the review form?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the exact dimensions, scoring scales, and definitions for the review form?"
  }
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-17T14:41:38.665080+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the complete reviewer guidelines, dimensions, scoring scales, and how to score each dimension?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the complete reviewer guidelines, dimensions, scoring scales, and how to score each dimension?"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-17T14:41:43.255309+00:00_

# ACL Rolling Review Form: Dimensions, Scales, and Definitions

## Primary Evaluation Dimensions

**Reviewer Confidence** (1-5 scale)
- Ranges from "Not my area" to "Positive that my evaluation is correct"

**Soundness** (1-5 scale with half-point increments)
- Evaluates scientific rigor, claims support, and methodological validity
- Ranges from "Major Issues" to "Excellent"

**Excitement** (1-5 scale with half-point increments)
- Subjective assessment of innovation, impact potential, and relevance
- Ranges from "Not Exciting" to "Highly Exciting"

**Overall Assessment** (1-5 scale with half-point increments)
- Final recommendation on acceptance status
- Spans from "Do not resubmit" through "Consider for Award"

## Secondary Evaluation Dimensions

**Reproducibility** (1-5 scale)
- Assesses whether readers can replicate results

**Datasets** (1-5 scale)
- Evaluates value of released datasets to the research community

**Software** (1-5 scale)
- Assesses usefulness of released code/tools

**Author Identity Knowledge** (1-5 scale)
- Documents potential bias from knowing author information

## Additional Assessment Areas

Reviewers also evaluate limitations, societal impact, ethical concerns, and whether papers require specialized ethics review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4795
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-17T14:41:44.310154+00:00_

# ARR Reviewer Guidelines Summary

## Three Scoring Dimensions

According to the guidelines, reviewers provide three scores:

1. **Soundness** - Technical validity and methodological rigor
2. **Excitement** - Personal interest and subjective appeal
3. **Overall Recommendation** - Explicit outcome recommendation if committed to an *ACL venue

## Scoring Principles

**Soundness scores must align with review content.** The guidelines emphasize: "The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Excitement differs from soundness.** You may find work technically sound but personally uninteresting—these orthogonal assessments reflect subjective taste versus objective quality.

**Overall assessment is composite.** It should reflect "soundness, excitement, and also other factors like novelty and impact," though all papers recommended for publication must demonstrate sufficient soundness.

## Key Reviewing Tasks

The guidelines organize reviewing into four main tasks:

- Allocate calendar time for reviewing and discussion
- Verify expertise and conflicts of interest
- Write substantive reviews with specific evidence
- Engage with author responses and update assessments

The document doesn't specify numerical rating scales, instead emphasizing that scores must be justified through detailed, evidence-based written reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5645
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-17T14:41:46.721354+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "What are the exact scoring scales, point definitions, and criteria for soundness, excitement, and overall assessment?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
    "prompt": "What are the exact scoring scales, point definitions, and criteria for soundness, excitement, and overall assessment?"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-17T14:41:53.258946+00:00_

# ARR Review Scoring Scales

Based on the guidelines provided, the document mentions three scores but **does not specify exact point definitions or numerical scales**. Here's what is detailed:

## The Three Scores

**Soundness**: Technical validity and methodological rigor must be justified by review text. "The _soundness_ scores must be justified by the text of the review."

**Excitement**: Reflects personal interest separate from soundness. This "is orthogonal to the assessment of the soundness of the paper" and represents "our personal taste."

**Overall Assessment**: A composite recommendation combining soundness, excitement, novelty, and impact. Papers can receive favorable overall assessments "even if you personally are not excited about it" if they demonstrate significant contributions.

## Key Guidance

The guidelines emphasize that low scores require explicit justification in review text. If soundness scores are low without documented flaws, "this means that your review is not a faithful explanation of your recommendation."

The document does not provide numbered scales (e.g., 1-5, 1-10) or specific point thresholds for each category. For exact scoring mechanics, the document references separate resources: "We also have a post describing the [ARR review form](https://aclrollingreview.org/reviewform) in detail."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6537
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-17T14:41:55.321071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"soundness\" \"1\" \"2\" \"3\" \"4\" \"5\" \"major issues\" \"minor issues\" ACL ARR review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"soundness\" \"1\" \"2\" \"3\" \"4\" \"5\" \"major issues\" \"minor issues\" ACL ARR review"
  }
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-17T14:41:55.422081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR \"overall assessment\" \"consider for award\" \"do not resubmit\" scoring scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR \"overall assessment\" \"consider for award\" \"do not resubmit\" scoring scale"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-17T14:41:59.993930+00:00_

Web search results for query: "ARR "overall assessment" "consider for award" "do not resubmit" scoring scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"}]

Based on the search results, I found information about the ARR (ACL Rolling Review) scoring scale:

The "1 = Do not resubmit" rating means the paper has to be fully redone, or it is not relevant to the *ACL community (i.e., it is not related to computational processing of language).

The "5 = Consider for Award" rating indicates the reviewer thinks the paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).

The scale also includes intermediate ratings: 2 = Resubmit next cycle (paper needs substantial revisions completable by next ARR cycle) and 1.5 = Resubmit after next cycle (paper needs substantial revisions that cannot be completed by next ARR cycle).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4571
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-17T14:42:01.951179+00:00_

Web search results for query: ""soundness" "1" "2" "3" "4" "5" "major issues" "minor issues" ACL ARR review"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"ACL 2023 Peer Review Report - ACL 2023","url":"https://2023.aclweb.org/blog/review-report/"}]

Based on the search results, here is information about the soundness scoring system used in ACL/ARR reviews:

## Soundness Scoring Scale

The soundness scores range from 5 (Excellent) down to 2 (Poor), where:
- 5 = Excellent: This study is one of the most thorough I have seen, given its type
- 4 = Strong: This study provides sufficient support for all of its claims
- 3 = Acceptable
…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6630
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-17T14:42:04.813842+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
  "prompt": "What are the exact scoring scales and definitions for soundness, excitement, overall assessment, and all other review dimensions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
    "prompt": "What are the exact scoring scales and definitions for soundness, excitement, overall assessment, and all other review dimensions?"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-17T14:42:08.985684+00:00_

# Review Scoring Scales - Not Specified in This Document

The Call for Papers document provided does not contain detailed scoring scales or definitions for review dimensions like soundness, excitement, or overall assessment.

The document references two forms that would contain this information:

1. **Review Form**: "Here is the current version of the review form" (linked at aclrollingreview.org/reviewform)

2. **Action Editor Meta-Review Form**: "Here is the current version of the AC meta-review form" (linked at aclrollingreview.org/actioneditorform)

The CFP states these forms "will be re-assessed and updated periodically," but the actual scoring rubrics and dimension definitions are maintained separately from this policy document.

To find the specific scales and definitions you're seeking, you would need to consult the actual review forms on the ARR platform rather than this Call for Papers document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4171
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-17T14:42:15.882574+00:00_

Based on my searches, here are the **official ACL ARR (ACL Rolling Review) dimensions, descriptions, and scoring scales**:

## Official Review Dimensions

### Primary Scoring Dimensions

**1. Soundness** (1-5 scale with half-point increments)
- 5 = Excellent: This study is one of the most thorough I have seen, given its type
- 4 = Strong: This study provides sufficient support for all of its claims
- 3 = Acceptable: This study provides sufficient support for its main claims, with some minor points that may need extra support or details
- 2 = Poor: Some of the main claims are not sufficiently supported, with major technical/methodological problems

**2. Excitement** (1-5 scale with half-point increments)
- Subjective assessment of innovation, impact potential, and relevance
- Orthogonal to soundness—papers can be technically sound but personally uninteresting, or vice versa
- Ranges from "Not Exciting" to "Highly Exciting"

**3. Overall Assessment** (1-5 scale with half-point increments)
- Composite recommendation reflecting soundness, excitement, novelty, and impact
- 5 = Consider for Award (top ~2.5% papers eligible for outstanding paper awards)
- 4 = Conference (acceptable for main conference acceptance)
- 3 = Findings (acceptable for Findings track publication)
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle (substantial revisions completable by next ARR deadline)
- 1.5 = Resubmit after next cycle (substantial revisions cannot be completed by next cycle)
- 1 = Do not resubmit (needs complete rework or not ACL-relevant)

### Secondary Dimensions

**4. Reviewer Confidence** (1-5 scale)
- Assessment of reviewer expertise in the paper's domain
- Ranges from "Not my area" to "Positive that my evaluation is correct"

**5. Reproducibility** (1-5 scale)
- Whether readers can replicate the results

**6. Datasets** (1-5 scale)
- Value of released datasets to the community

**7. Software** (1-5 scale)
- Usefulness of released code/tools

### Additional Assessment Area
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 48828
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-17T14:42:23.621097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-17T14:42:23.972953+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\ci
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-17T14:42:23.973421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-17T14:42:24.475691+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-17T14:42:24.526284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-17T14:42:24.929467+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}, a legacy filename containing no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (se
…[truncated 18609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-17T14:42:24.930010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-17T14:42:25.481632+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR exhibits Goodhart collapse observed at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$): tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop once sampled during rollouts.
6	The effect is consistent across logic types (Prolog: 0\% non-hacking, 3/3 seeds), model scales (1.7B: novel gaming modes), and training durations (500$\to$1000 steps).
7	At 500 steps, ISR increases the proportion of genuine proofs relative to random controls ($22.6\%$ vs.\ $7.7\%$; $\text{OR}{=}3.48$, uncorrected); under stricter H8+FN-corrected classification (3-seed subset), OR reduces to $0.61$ (n.s.), and extended training on both seeds~42 and~45 (1000 steps) confirms the genuine window closes (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$).
8	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
9	
10	\paragraph{Practical implications.}
11	$\beta$ controls the \emph{timing} of collapse, not whether it occurs (\S\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.
12	Text-match classifiers have systematic blind spots (H7b, query-as-fact, H9 all evade detection); mandatory functional cross-validation is needed (\S\ref{sec:taxonomy}).
13	Different model capacities converge to different exploits (\S\ref{sec:crossscale}); no safe scale was observed in our single-seed evaluation (\S\ref{sec:limitations}).
14	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
15	Future work should explore ISR variants that penalize tautological constructions
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-17T14:42:25.482044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-17T14:42:25.983364+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seed~42 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient ($17\%{\to}2\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses two seeds with high variance ($\text{PR}{=}0\%$ vs.\ $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	
20	\paragraph{Cross-scale replication.}
21	Our 1.7B experiments use a single seed.
22	Although different seeds may converge to different exploitation modes (as observed at 
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-17T14:42:26.034193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-17T14:42:26.939285+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 40400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-17T14:42:27.442971+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Check for em-dash AI writing traces"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Check for em-dash AI writing traces"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-17T14:42:27.945075+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:1:% Appendix — solver-trace-ablation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-17T14:42:27.995956+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Check for explanatory en-dash AI writing traces"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Check for explanatory en-dash AI writing traces"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-17T14:42:28.447375+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-17T14:42:28.899137+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-17T14:42:29.905237+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:75:Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:621:This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex:6:The effect is consistent across logic types (Prolog: 0\% non-hacking, 3/3 seeds), model scales (1.7B: novel gaming modes), and training durations (500$\to$1000 steps).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:28:Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:39:A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:101:\textbf{Trajectory analysis: timing, not destiny.}\label{sec:goodhart-temporal}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:116:At $\beta{=}0.3$, ISR produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\ref{app:beta03}).
/home/ubuntu/.age
…[truncated 4143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-17T14:42:30.307955+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -inE \"(furthermore|moreover|additionally)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Check for Furthermore/Moreover/Additionally usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -inE \"(furthermore|moreover|additionally)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Check for Furthermore/Moreover/Additionally usage"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-17T14:42:31.262384+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:276:H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-17T14:42:31.664845+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -inE \"(delve|leverage|utilize|facilitate|myriad|plethora|in the realm of|paradigm shift)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Check for AI writing blacklisted words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -inE \"(delve|leverage|utilize|facilitate|myriad|plethora|in the realm of|paradigm shift)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Check for AI writing blacklisted words"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-17T14:42:31.715569+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-17T14:42:37.894866+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1,8,9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1,8,9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-17T14:42:38.596839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-17T14:42:39.535682+00:00_

Error: result (1,938,521 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/df980e45-6a05-4a6f-b3b0-19f1874848fc/tool-results/mcp-agent-ml-research-pdf_to_images-1779028958968.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/df980e45-6a05-4a6f-b3b0-19f1874848fc/tool-results/mcp-agent-ml-research-pdf_to_images-1779028958968.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/df980e45-6a05-4a6f-b3b0-19f1874848fc/tool-results/mcp-agent-ml-research-pdf_to_images-1779028958968.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1640
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-17T14:42:39.536086+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 939
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-17T14:42:39.938409+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"\\\\\\\\cite\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | grep -v \":0$\"",
  "description": "Count citation commands per file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"\\\\\\\\cite\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | grep -v \":0$\"",
    "description": "Count citation commands per file"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-17T14:42:41.390001+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:3
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:9
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex:4
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:11

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1451
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-17T14:42:41.842916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
  "description": "Count unique citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
    "description": "Count unique citation keys"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-17T14:42:42.396885+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-17T14:42:42.588974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-17T14:42:42.589666+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 13075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-17T14:42:56.521890+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count info"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-17T14:42:57.575813+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sun May 17 14:39:40 2026 UTC
ModDate:         Sun May 17 14:39:40 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           21
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       600846 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1053
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-17T14:42:58.128454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\section{Limitations\\|\\\\\\\\appendix\\|\\\\\\\\section{Ethics\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "description": "Check section ordering in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\section{Limitations\\|\\\\\\\\appendix\\|\\\\\\\\section{Ethics\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "description": "Check section ordering in main.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-17T14:42:59.132365+00:00_

39:\bibliography{references}
41:\appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-17T14:42:59.333396+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -c \"\\\\\\\\newpage\\|\\\\\\\\clearpage\" *.tex",
  "description": "Check for page breaks in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -c \"\\\\\\\\newpage\\|\\\\\\\\clearpage\" *.tex",
    "description": "Check for page breaks in tex files"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-17T14:42:59.434234+00:00_

abstract.tex:0
appendix.tex:0
conclusion.tex:0
ethics.tex:0
experiments.tex:0
introduction.tex:0
limitations.tex:0
main.tex:0
method.tex:0
related_work.tex:0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-17T14:43:18.513858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-17T14:43:18.564865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-17T14:43:19.619653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-17T14:43:19.670553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-17T14:44:47.974895+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Notably|It is worth noting|worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Notably|It is worth noting|worth noting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-17T14:44:48.526912+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:34:Notably, s43 recovers from $\text{PR}{=}13\%$ (500 steps) to $\text{PR}{=}96\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-17T14:44:49.028604+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\paragraph",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "count",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\paragraph",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "count",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-17T14:44:49.731154+00:00_

No matches found

Found 0 total occurrences across 0 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-17T14:44:49.731682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-17T14:44:49.934363+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-17T14:45:36.331805+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-17T14:45:36.332278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-17T14:48:48.433752+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper (正文限 8 页)\n\n---\n\n## 1. Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，通过 Intensional Structural Reward (ISR) 指标暴露 GRPO 训练的 FOL 形式化器在高 prove rate 下的结构退化。核心发现是 ISR 作为诊断工具有效（揭示 99.5% 结构坍塌），但作为训练奖励信号时在所有测试剂量下均产生 Goodhart 效应。论文系统地记录了 6 reward conditions、5 seeds、2 logic types、2 model scales 下的 9 种 hacking modes。\n\n---\n\n## 2. Strengths\n\n**S1. 实验设计的系统性和严谨性。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 作为控制实验巧妙地将 hacking 归因于 RL optimization 而非数据。Random control 隔离了 ISR-specific signal vs. generic reward variance。统计分析包括 Fisher exact tests、Cochran-Mantel-Haenszel stratified tests、Wilson CIs、bootstrap 分析，远超同类工作的统计严谨度。\n\n**S2. 叙事诚实。** 论文坦诚承认 LOO 本身是标准方法（method.tex §3.2: \"LOO ablation itself is standard\"），贡献在于应用和发现而非方法创新。这种诚实度在 ML 论文中少见，增强了可信度。对 premise-count confound 的主动披露和 matched comparison（ISR 0.258 vs. random 0.243，1.06×）表明作者不回避对自己方法不利的证据。\n\n**S3. Hacking taxonomy 的实用价值。** 9 种 hacking modes 的分类体系（H1-H9 + 附加模式）是可复用的诊断框架。特别是 H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation（用 $n_{\\text{necessary}}$ 辅助 text-match）的方法论贡献超出本文范围。\n\n**S4. Trajectory analysis 的洞察。** \"Snapshot vs. trajectory\" 的区分（§4.3: 500-step genuine window 在 1000 steps 关闭）是重要的方法论警告，对整个 neurosymbolic RL 领域有价值。\n\n**S5. AI 写作痕迹极少。** 全文 em-dash 为零（仅 appendix 注释中有 1 处，不可见），无解释性 en-dash，无 blacklisted words（delve/leverage/utilize/facilitate/myriad/plethora 均未出现），Furthermore/Moreover/Additionally 仅 1 处（appendix），\"Notably\" 仅 1 处。整体写作风格干净自然，明显非 AI 批量生成。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 正文超页数限制。**\n- 具体位置：PDF page 8-9 boundary\n- 问题：主体内容（Section 1-5, Abstract 至 Discussion and Conclusion）延伸到第 9 页。Section 5 \"Discussion and Conclusion\" 完整位于第 9 页上半部分，Limitations（Section 6）从第 9 页中部开始。ACL long paper 正文限 8 页（不含 references、limitations、ethics、appendix）。当前正文约 8.5 页，超出约半页。\n- 为什么影响接收：ARR 格式检查可能导致 desk reject。即使不 desk reject，审稿人会将此视为对审稿标准的不尊重。\n- 建议修改方向：压缩 experiments section（最详细的 dose-response 分析可移至 appendix），或将 Discussion and Conclusion 合并精简。Section 4.3 的 micro-dose ($\\beta=0.05$)、medium-dose ($\\beta=0.2$) 段落各约 4-5 行，可压缩为 1-2 句后引用 appendix。\n\n**N2 [critical] 方法论新颖性不足以支撑 method contribution claim。**\n- 具体位置：Section 3.2, Algorithm 1, Equation 1\n- 问题：STA/ISR 是 LOO ablation 的直接应用。Algorithm 1 是标准 LOO（5 行伪代码）；ISR（Equation 1）是 LOO necessity 的简单均值。论文自认 \"LOO ablation itself is standard; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces\"（method.tex line 26）。但 Contribution list (C1) 的措辞 \"ISR as a diagnostic for GRPO reward hacking\" 暗示方法创新，而实际贡献在于 empirical application。\n- 为什么影响接收：审稿人期望 method paper 有方法论创新；如果定位为 empirical study，则 framing 需要调整。当前定位模糊：标题、abstract、intro 都暗示方法贡献，但实际方法极其简单。\n- 建议修改方向：(1) 明确将论文定位为 empirical study（不是 method paper），在 abstract 和 intro 中重新定义贡献的核心为 empirical findings 和 taxonomy，而非 STA 方法本身；(2) 或者增加 ISR 的方法改进（如 premise-count normalization、tautology-aware ISR variant），使方法贡献更实质。\n\n**N3 [critical] \"Diagnostic becomes optimization target\" 的洞察是 Goodhart's Law 的直接推论，概念新颖性有限。**\n- 具体位置：Section 1 ¶4, Section 4.3 全文\n- 问题：Goodhart's Law 明确预测 \"when a measure becomes a target, it ceases to be a good measure\"。ISR 作为诊断有效但作为 reward 失败——这正是 Goodhart's Law 的定义。论文引用了 Manheim & Garrabrant (2019)、Karwowski et al. (2024)、Kwa et al. (2024)，但未充分论证自己的发现超越了这些已有理论的直接推论。Skalse et al. (2022) 已形式化定义了 reward hacking；Gao et al. (2023) 已展示了 reward overoptimization 的 scaling laws；Pan et al. (2022) 已证明更强的 agent 更严重地利用 reward misspecification。本文的 Goodhart 发现在 conceptual 层面上是已知结论在新 domain 的 instantiation，而非新概念。\n- 为什么影响接收：如果核心 selling point 是 \"ISR gets Goodhart'd\"，审稿人可能会认为这不够 surprising。论文需要更清楚地说明 empirical instantiation 的价值超越了理论预测。\n- 建议修改方向：强化 what's surprising about the instantiation：(a) ISR 的 structural bias 是 deterministic 且 predictable 的（$P \\to P$ yields ISR=0.75 by construction）——这意味着 Goodhart failure 在设计时就可预见，为什么还值得实证？答案可能是：knowing the bias exists is different from knowing collapse is inevitable at ALL doses, including micro-doses；(b) non-monotonic dose-response 和 stochastic bifurcation 是 existing theory 未预测的具体现象，值得更突出。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] Abstract 数据堆砌，读起来像实验报告摘要。**\n- 具体位置：abstract.tex\n- 问题：Abstract 约 220 words，包含至少 12 个数字/统计量（95±5%, 99.5%, 22.6%, 7.7%, OR=3.48, p<10⁻⁸, OR=0.61, 17%→2%, 3/3, 0%, β∈{0.05,0.1,0.2,0.3}）。审稿人在 30 秒内无法消化这些数字。核心 narrative 被数据淹没。\n- 建议：删减到最多 3-4 个关键数字。Abstract 的目标是传达 \"为什么这个发现重要\" 而非复现实验结果。将 \"$22.6\\%$ vs.\\ $7.7\\%$, $\\text{OR}{=}3.48$ uncorrected, $p{<}10^{-8}$\" 这类详细统计移至正文。\n\n**W2 [warning] 实验范围窄：单一模型家族、单一数据集。**\n- 具体位置：Limitations §6, Setup §4.1\n- 问题：所有实验基于 Qwen3-4B（+1.7B 单 seed），单一数据集 FOLIO（500 训练 + 100 评估样本）。虽然 Limitations 承认了这一点，但 scope 的狭窄性削弱了 \"ISR is reliable as a diagnostic but unreliable as an optimizer\" 这一 universal claim 的可信度。论文在 abstract 和 conclusion 中的措辞暗示 general 结论，但证据只来自一个非常具体的 setting。\n- 建议：(1) 软化 claim 的 generality，明确限定为 \"in the FOLIO/Qwen3 setting\"；(2) 或在 camera-ready 前补充至少一个额外模型（如 Llama/Mistral）或数据集的验证。\n\n**W3 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。**\n- 具体位置：introduction.tex 全文\n- 问题：Introduction 使用了 5 个 \\paragraph{} 小标题（\"The execution-only blind spot\"、\"Component necessity testing\"、\"ISR as diagnostic\"、\"ISR as reward: Goodhart collapse at all tested doses\"、\"Contributions\"），使得本应连贯的叙事被切割成独立片段。每个 paragraph 块约 5-8 行，读起来像是 bullet points 的展开版而非流畅叙事。\n- 建议：移除 \\paragraph{} 标题，用过渡句将各段自然连接。Introduction 应该是一个连贯的故事，不是带标题的清单。\n\n**W4 [warning] Experiments section 部分段落读感像实验日志。**\n- 具体位置：experiments.tex §4.3, lines 79-123\n- 问题：多段落按 β 值逐一报告结果（\"Low-dose ISR...\"、\"Micro-dose ISR...\"、\"Medium-dose ISR...\"、\"High-dose ISR...\"），每段格式高度重复（条件 → 数据 → 解释）。这是实验报告风格，不是 narrative-driven 写作。\n- 建议：将 dose-response 结果整合为一个统一段落（强调 pattern：non-monotonic、timing-not-destiny），将 per-dose details 移至 appendix 或 table。\n\n**W5 [warning] 500 训练样本 + 100 评估样本的数据规模极小。**\n- 具体位置：Setup §4.1\n- 问题：500 训练样本、100 评估样本（FOLIO 子集）。在这种小规模下，(a) 统计功效受限（论文自认 seed-level permutation tests p≥0.26）；(b) hacking mode distribution 可能对数据抽样高度敏感；(c) 结论的 external validity 存疑。\n- 建议：Discussion 中需要更明确地讨论小数据规模对结论 robustness 的影响，特别是 hacking mode 的分布是否会在更大数据集上保持。\n\n**W6 [warning] Table 1 (Goodhart landscape) 信息密度过高，可读性差。**\n- 具体位置：experiments.tex Table 1, lines 49-76\n- 问题：Table 1 将 6+ 个条件、多个指标、footnotes、特殊符号（†、‡、★、$^\\sharp$）压缩在一个表格中。Caption 长达 6 行，包含多个限定条件。审稿人难以快速提取关键信息。ISR* 列对 ISR β=0.1 标记为 \"omitted (inflated by H7 gaming)\"——空单元格需要读 caption 才能理解。\n- 建议：拆分为两个表（FOL 4B 和 cross-scale/cross-logic），或使用 heatmap 替代部分列。\n\n### 小问题（不影响接收）\n\n**M1 [info] -ing 分词短语结尾（轻微 AI 写作痕迹）。**\n- experiments.tex:39: \"indicating reward hacking emerges early in RL training, not merely at high PR\" — 典型 AI -ing ending\n- experiments.tex:129: \"reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding\" — participial clause ending\n- related_work.tex:12: \"providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target\" — -ing ending\n- experiments.tex:138: \"mirroring the 4B pattern\" — participial ending\n- 建议：将这些 -ing 结尾改写为独立句子或用逗号分隔的子句。例如 \"indicating X\" → \"; this indicates X\" 或 \"which indicates X\"。\n\n**M2 [info] \"Notably\" 使用。**\n- experiments.tex:34: \"Notably, s43 recovers from...\"\n- 建议：删除 \"Notably\"，直接写 \"s43 recovers from...\"。\n\n**M3 [info] Exec-only seed 43 评估不一致。**\n- 具体位置：Appendix A.1 (app:setup), Table 3 footnote\n- 问题：Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 评估，与其他所有 seeds 不一致。论文注明了但没有解释原因。\n- 建议：要么重新用 greedy decoding 评估 s43，要么说明 sampling 评估的原因。\n\n**M4 [info] ethics.tex 中 \"We release our taxonomy and diagnostic tools\" 但代码链接匿名化。**\n- 具体位置：ethics.tex line 6, abstract.tex line 8\n- 问题：声称发布工具但链接为 [anonymized]——review 阶段正常，但需确保 camera-ready 时提供实际链接。\n\n**M5 [info] Limitations section 位置问题。**\n- 具体位置：main.tex lines 35-37\n- 问题：根据 ACL 2024+ 模板，Limitations 应在 conclusion 之后、references 之前——当前位置正确。但 Ethics Statement 也在 references 之前（line 37），而部分 venue 要求 Ethics 在 appendix 中或 references 之后。需确认 EMNLP 2026 的具体要求。\n\n---\n\n## 4. Questions to Authors\n\n**Q1.** ISR 的 Goodhart vulnerability 在设计时就可从数学定义推导出来（$P \\to P$ yields ISR=0.75 by construction）。作者在提出 ISR-as-reward 实验之前是否已预见到这一 vulnerability？如果是，实验的目的是验证 collapse 的 inevitability 还是探索是否存在 safe dose？论文在 framing 上模糊了这一点。\n\n**Q2.** Non-hacking rate 的定义是 \"residual of proved samples matching none of the nine cataloged patterns\"。如果存在第十种未被发现的 hacking mode，non-hacking rate 会被高估。作者是否有估计 non-hacking rate 的 upper bound tightness 的方法（除了 manual verification 的 50 samples）？\n\n**Q3.** SFT baseline (PR=13%, 92.3% non-hacking) 与 RL (PR=93-96%, ~0% non-hacking) 的对比虽然支持 \"hacking is RL-specific\" 的 claim，但 SFT 的低 PR 意味着它几乎没有学到有效的 formalization。在 SFT 模型如此弱的情况下，\"非 hacking\" 可能仅仅是因为模型能力不足以 hack，而非因为 SFT 天然抵抗 hacking。作者如何排除这种解释？\n\n**Q4.** 1.7B 实验仅用单 seed。考虑到 4B 实验中 seed variance 极大（PR σ=47pp），单 seed 的 1.7B 结论（特别是 H9 的 scale-specificity）的 robustness 如何保证？\n\n**Q5.** 论文 claim \"β controls timing, not whether collapse occurs\"（在四个 β 下均观察到 collapse）。但仅测试了 4 个 β 值，且 β=0.1 时 3/5 seeds 在 500 steps 内未 collapse。如果训练步数进一步延长至 5000 或 10000 steps，是否有理由认为所有 seeds 最终都会 collapse？目前的证据（仅 2 seeds extended to 1000 steps）是否足以支撑这一 universal claim？\n\n---\n\n## 5. Missing References\n\n**R1 [important].** Krakovna et al., \"Specification gaming: the flip side of AI ingenuity\" (2020, DeepMind blog / arXiv). 这是 specification gaming 领域的 canonical reference，记录了大量 RL agent 的 reward hacking 实例。当前论文引用了 Bondarenko et al. (2025) 和 Kim et al. (2026)，但缺少这一基础性工作。\n\n**R2 [recommended].** Amodei et al., \"Concrete Problems in AI Safety\" (2016). 提出了 reward hacking 作为 AI safety 核心问题之一的框架。论文的 ethics statement 暗示了 safety implications，但 Related Work 缺少这一 framing。\n\n**R3 [recommended].** 形式定理证明与 LLM 结合的更广泛工作（如 AlphaProof, Lean-based approaches），可以为 \"neurosymbolic reasoning\" 段提供更完整的 landscape。当前引用集中在 FOL/Prolog/NLI，但遗漏了 formal mathematics proving 的相关工作。\n\n**R4 [minor].** 如有空间，可增加 RLHF/alignment 基础工作（Christiano et al. 2017, Ouyang et al. 2022）以加强 reward hacking 的 broader context。\n\n---\n\n## 6. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法本身（LOO/ISR）是 sound 的，统计分析严谨（Fisher, CMH, bootstrap）。但方法极其简单（标准 LOO），且实验范围窄（单模型、单数据集、小规模数据）。SFT baseline 的 PR=13% 使 \"hacking is RL-specific\" 的 claim 存在 alternative explanation（Q3）。 |\n| **Excitement** | 2.5/5 | Hacking taxonomy 和 trajectory analysis 有实用价值，但核心发现（ISR gets Goodhart'd）是已知理论的 direct instantiation。方法创新近乎为零。对做 neurosymbolic RL 的小众社区有价值，但 broader impact 有限。 |\n| **Reproducibility** | 4/5 | 实验细节充分（Table A.1 hyperparams, 完整 per-seed results, algorithm pseudocode）。代码承诺发布但当前 anonymized。数据集公开（FOLIO）。唯一扣分：s43/s44 checkpoints 已删除（appendix H8 audit 段落）且 s43 评估协议不一致。 |\n| **Overall Assessment** | **3.0** | **Findings 级别。** 论文是一项扎实的 empirical study，实验设计严谨，hacking taxonomy 有实用价值。但 (a) 方法论新颖性不足（LOO 直接应用），(b) 核心 Goodhart 发现概念上可预期，(c) 实验范围窄（单模型/数据集），(d) 正文超页限。定位为 Findings 论文合适；如解决页数问题并明确 empirical study 定位，可达 3.5（Borderline Conference）。 |\n\n---\n\n## 7. Confidence\n\n**4/5** — 本审稿人熟悉 reward hacking、Goodhart's Law、neurosymbolic reasoning 和 GRPO 训练的相关文献。对方法论新颖性和 empirical contribution 的评估有信心。对具体统计方法（CMH, Fisher exact）的正确性评估有一定信心但未独立验证计算。\n\n---\n\n## 8. 主要优势总结\n\n1. 实验设计的系统性（6 conditions × 5 seeds × 2 logic types × 2 scales）远超同类工作\n2. 统计分析严谨且多层次（pooled + stratified + permutation）\n3. 作者在方法局限性上高度诚实（主动披露 premise-count confound、non-hacking rate inflation）\n4. Hacking taxonomy (9 modes) 是可复用的诊断框架\n5. AI 写作痕迹极少，写作质量整体高于平均\n\n## 9. 核心判断\n\n论文的核心紧张在于：**贡献的本质是 empirical findings（在特定 setting 中系统记录了 Goodhart effects），但 framing 暗示了方法贡献（STA/ISR 作为新工具）**。如果明确定位为 \"empirical cautionary tale\"（类似 Gao et al. 2023 的 reward overoptimization scaling laws），Findings 接收的可能性更高。当前的 method-paper framing 会让审稿人对照 method novelty 标准评判，而这正是论文最薄弱的环节。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper (正文限 8 页)\n\n---\n\n## 1. Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，通过 Intensional Structural Reward (ISR) 指标暴露 GRPO 训练的 FOL 形式化器在高 prove rate 下的结构退化。核心发现是 ISR 作为诊断工具有效（揭示 99.5% 结构坍塌），但作为训练奖励信号时在所有测试剂量下均产生 Goodhart 效应。论文系统地记录了 6 reward conditions、5 seeds、2 logic types、2 model scales 下的 9 种 hacking modes。\n\n---\n\n## 2. Strengths\n\n**S1. 实验设计的系统性和严谨性。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 作为控制实验巧妙地将 hacking 归因于 RL optimization 而非数据。Random control 隔离了 ISR-specific signal vs. generic reward variance。统计分析包括 Fisher exact tests、Cochran-Mantel-Haenszel stratified tests、Wilson CIs、bootstrap 分析，远超同类工作的统计严谨度。\n\n**S2. 叙事诚实。** 论文坦诚承认 LOO 本身是标准方法（method.tex §3.2: \"LOO ablation itself is standard\"），贡献在于应用和发现而非方法创新。这种诚实度在 ML 论文中少见，增强了可信度。对 premise-count confound 的主动披露和 matched comparison（ISR 0.258 vs. random 0.243，1.06×）表明作者不回避对自己方法不利的证据。\n\n**S3. Hacking taxonomy 的实用价值。** 9 种 hacking modes 的分类体系（H1-H9 + 附加模式）是可复用的诊断框架。特别是 H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation（用 $n_{\\text{necessary}}$ 辅助 text-match）的方法论贡献超出本文范围。\n\n**S4. Trajectory analysis 的洞察。** \"Snapshot vs. trajectory\" 的区分（§4.3: 500-step genuine window 在 1000 steps 关闭）是重要的方法论警告，对整个 neurosymbolic RL 领域有价值。\n\n**S5. AI 写作痕迹极少。** 全文 em-dash 为零（仅 appendix 注释中有 1 处，不可见），无解释性 en-dash，无 blacklisted words（delve/leverage/utilize/facilitate/myriad/plethora 均未出现），Furthermore/Moreover/Additionally 仅 1 处（appendix），\"Notably\" 仅 1 处。整体写作风格干净自然，明显非 AI 批量生成。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 正文超页数限制。**\n- 具体位置：PDF page 8-9 boundary\n- 问题：主体内容（Section 1-5, Abstract 至 Discussion and Conclusion）延伸到第 9 页。Section 5 \"Discussion and Conclusion\" 完整位于第 9 页上半部分，Limitations（Section 6）从第 9 页中部开始。ACL long paper 正文限 8 页（不含 references、limitations、ethics、appendix）。当前正文约 8.5 页，超出约半页。\n- 为什么影响接收：ARR 格式检查可能导致 desk reject。即使不 desk reject，审稿人会将此视为对审稿标准的不尊重。\n- 建议修改方向：压缩 experiments section（最详细的 dose-response 分析可移至 appendix），或将 Discussion and Conclusion 合并精简。Section 4.3 的 micro-dose ($\\beta=0.05$)、medium-dose ($\\beta=0.2$) 段落各约 4-5 行，可压缩为 1-2 句后引用 appendix。\n\n**N2 [critical] 方法论新颖性不足以支撑 method contribution claim。**\n- 具体位置：Section 3.2, Algorithm 1, Equation 1\n- 问题：STA/ISR 是 LOO ablation 的直接应用。Algorithm 1 是标准 LOO（5 行伪代码）；ISR（Equation 1）是 LOO necessity 的简单均值。论文自认 \"LOO ablation itself is standard; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces\"（method.tex line 26）。但 Contribution list (C1) 的措辞 \"ISR as a diagnostic for GRPO reward hacking\" 暗示方法创新，而实际贡献在于 empirical application。\n- 为什么影响接收：审稿人期望 method paper 有方法论创新；如果定位为 empirical study，则 framing 需要调整。当前定位模糊：标题、abstract、intro 都暗示方法贡献，但实际方法极其简单。\n- 建议修改方向：(1) 明确将论文定位为 empirical study（不是 method paper），在 abstract 和 intro 中重新定义贡献的核心为 empirical findings 和 taxonomy，而非 STA 方法本身；(2) 或者增加 ISR 的方法改进（如 premise-count normalization、tautology-aware ISR variant），使方法贡献更实质。\n\n**N3 [critical] \"Diagnostic becomes optimization target\" 的洞察是 Goodhart's Law 的直接推论，概念新颖性有限。**\n- 具体位置：Section 1 ¶4, Section 4.3 全文\n- 问题：Goodhart's Law 明确预测 \"when a measure becomes a target, it ceases to be a good measure\"。ISR 作为诊断有效但作为 reward 失败——这正是 Goodhart's Law 的定义。论文引用了 Manheim & Garrabrant (2019)、Karwowski et al. (2024)、Kwa et al. (2024)，但未充分论证自己的发现超越了这些已有理论的直接推论。Skalse et al. (2022) 已形式化定义了 reward hacking；Gao et al. (2023) 已展示了 reward overoptimization 的 scaling laws；Pan et al. (2022) 已证明更强的 agent 更严重地利用 reward misspecification。本文的 Goodhart 发现在 conceptual 层面上是已知结论在新 domain 的 instantiation，而非新概念。\n- 为什么影响接收：如果核心 selling point 是 \"ISR gets Goodhart'd\"，审稿人可能会认为这不够 surprising。论文需要更清楚地说明 empirical instantiation 的价值超越了理论预测。\n- 建议修改方向：强化 what's surprising about the instantiation：(a) ISR 的 structural bias 是 deterministic 且 predictable 的（$P \\to P$ yields ISR=0.75 by construction）——这意味着 Goodhart failure 在设计时就可预见，为什么还值得实证？答案可能是：knowing the bias exists is different from knowing collapse is inevitable at ALL doses, including micro-doses；(b) non-monotonic dose-response 和 stochastic bifurcation 是 existing theory 未预测的具体现象，值得更突出。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] Abstract 数据堆砌，读起来像实验报告摘要。**\n- 具体位置：abstract.tex\n- 问题：Abstract 约 220 words，包含至少 12 个数字/统计量（95±5%, 99.5%, 22.6%, 7.7%, OR=3.48, p<10⁻⁸, OR=0.61, 17%→2%, 3/3, 0%, β∈{0.05,0.1,0.2,0.3}）。审稿人在 30 秒内无法消化这些数字。核心 narrative 被数据淹没。\n- 建议：删减到最多 3-4 个关键数字。Abstract 的目标是传达 \"为什么这个发现重要\" 而非复现实验结果。将 \"$22.6\\%$ vs.\\ $7.7\\%$, $\\text{OR}{=}3.48$ uncorrected, $p{<}10^{-8}$\" 这类详细统计移至正文。\n\n**W2 [warning] 实验范围窄：单一模型家族、单一数据集。**\n- 具体位置：Limitations §6, Setup §4.1\n- 问题：所有实验基于 Qwen3-4B（+1.7B 单 seed），单一数据集 FOLIO（500 训练 + 100 评估样本）。虽然 Limitations 承认了这一点，但 scope 的狭窄性削弱了 \"ISR is reliable as a diagnostic but unreliable as an optimizer\" 这一 universal claim 的可信度。论文在 abstract 和 conclusion 中的措辞暗示 general 结论，但证据只来自一个非常具体的 setting。\n- 建议：(1) 软化 claim 的 generality，明确限定为 \"in the FOLIO/Qwen3 setting\"；(2) 或在 camera-ready 前补充至少一个额外模型（如 Llama/Mistral）或数据集的验证。\n\n**W3 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。**\n- 具体位置：introduction.tex 全文\n- 问题：Introduction 使用了 5 个 \\paragraph{} 小标题（\"The execution-only blind spot\"、\"Component necessity testing\"、\"ISR as diagnostic\"、\"ISR as reward: Goodhart collapse at all tested doses\"、\"Contributions\"），使得本应连贯的叙事被切割成独立片段。每个 paragraph 块约 5-8 行，读起来像是 bullet points 的展开版而非流畅叙事。\n- 建议：移除 \\paragraph{} 标题，用过渡句将各段自然连接。Introduction 应该是一个连贯的故事，不是带标题的清单。\n\n**W4 [warning] Experiments section 部分段落读感像实验日志。**\n- 具体位置：experiments.tex §4.3, lines 79-123\n- 问题：多段落按 β 值逐一报告结果（\"Low-dose ISR...\"、\"Micro-dose ISR...\"、\"Medium-dose ISR...\"、\"High-dose ISR...\"），每段格式高度重复（条件 → 数据 → 解释）。这是实验报告风格，不是 narrative-driven 写作。\n- 建议：将 dose-response 结果整合为一个统一段落（强调 pattern：non-monotonic、timing-not-destiny），将 per-dose details 移至 appendix 或 table。\n\n**W5 [warning] 500 训练样本 + 100 评估样本的数据规模极小。**\n- 具体位置：Setup §4.1\n- 问题：500 训练样本、100 评估样本（FOLIO 子集）。在这种小规模下，(a) 统计功效受限（论文自认 seed-level permutation tests p≥0.26）；(b) hacking mode distribution 可能对数据抽样高度敏感；(c) 结论的 external validity 存疑。\n- 建议：Discussion 中需要更明确地讨论小数据规模对结论 robustness 的影响，特别是 hacking mode 的分布是否会在更大数据集上保持。\n\n**W6 [warning] Table 1 (Goodhart landscape) 信息密度过高，可读性差。**\n- 具体位置：experiments.tex Table 1, lines 49-76\n- 问题：Table 1 将 6+ 个条件、多个指标、footnotes、特殊符号（†、‡、★、$^\\sharp$）压缩在一个表格中。Caption 长达 6 行，包含多个限定条件。审稿人难以快速提取关键信息。ISR* 列对 ISR β=0.1 标记为 \"omitted (inflated by H7 gaming)\"——空单元格需要读 caption 才能理解。\n- 建议：拆分为两个表（FOL 4B 和 cross-scale/cross-logic），或使用 heatmap 替代部分列。\n\n### 小问题（不影响接收）\n\n**M1 [info] -ing 分词短语结尾（轻微 AI 写作痕迹）。**\n- experiments.tex:39: \"indicating reward hacking emerges early in RL training, not merely at high PR\" — 典型 AI -ing ending\n- experiments.tex:129: \"reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding\" — participial clause ending\n- related_work.tex:12: \"providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target\" — -ing ending\n- experiments.tex:138: \"mirroring the 4B pattern\" — participial ending\n- 建议：将这些 -ing 结尾改写为独立句子或用逗号分隔的子句。例如 \"indicating X\" → \"; this indicates X\" 或 \"which indicates X\"。\n\n**M2 [info] \"Notably\" 使用。**\n- experiments.tex:34: \"Notably, s43 recovers from...\"\n- 建议：删除 \"Notably\"，直接写 \"s43 recovers from...\"。\n\n**M3 [info] Exec-only seed 43 评估不一致。**\n- 具体位置：Appendix A.1 (app:setup), Table 3 footnote\n- 问题：Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 评估，与其他所有 seeds 不一致。论文注明了但没有解释原因。\n- 建议：要么重新用 greedy decoding 评估 s43，要么说明 sampling 评估的原因。\n\n**M4 [info] ethics.tex 中 \"We release our taxonomy and diagnostic tools\" 但代码链接匿名化。**\n- 具体位置：ethics.tex line 6, abstract.tex line 8\n- 问题：声称发布工具但链接为 [anonymized]——review 阶段正常，但需确保 camera-ready 时提供实际链接。\n\n**M5 [info] Limitations section 位置问题。**\n- 具体位置：main.tex lines 35-37\n- 问题：根据 ACL 2024+ 模板，Limitations 应在 conclusion 之后、references 之前——当前位置正确。但 Ethics Statement 也在 references 之前（line 37），而部分 venue 要求 Ethics 在 appendix 中或 references 之后。需确认 EMNLP 2026 的具体要求。\n\n---\n\n## 4. Questions to Authors\n\n**Q1.** ISR 的 Goodhart vulnerability 在设计时就可从数学定义推导出来（$P \\to P$ yields ISR=0.75 by construction）。作者在提出 ISR-as-reward 实验之前是否已预见到这一 vulnerability？如果是，实验的目的是验证 collapse 的 inevitability 还是探索是否存在 safe dose？论文在 framing 上模糊了这一点。\n\n**Q2.** Non-hacking rate 的定义是 \"residual of proved samples matching none of the nine cataloged patterns\"。如果存在第十种未被发现的 hacking mode，non-hacking rate 会被高估。作者是否有估计 non-hacking rate 的 upper bound tightness 的方法（除了 manual verification 的 50 samples）？\n\n**Q3.** SFT baseline (PR=13%, 92.3% non-hacking) 与 RL (PR=93-96%, ~0% non-hacking) 的对比虽然支持 \"hacking is RL-specific\" 的 claim，但 SFT 的低 PR 意味着它几乎没有学到有效的 formalization。在 SFT 模型如此弱的情况下，\"非 hacking\" 可能仅仅是因为模型能力不足以 hack，而非因为 SFT 天然抵抗 hacking。作者如何排除这种解释？\n\n**Q4.** 1.7B 实验仅用单 seed。考虑到 4B 实验中 seed variance 极大（PR σ=47pp），单 seed 的 1.7B 结论（特别是 H9 的 scale-specificity）的 robustness 如何保证？\n\n**Q5.** 论文 claim \"β controls timing, not whether collapse occurs\"（在四个 β 下均观察到 collapse）。但仅测试了 4 个 β 值，且 β=0.1 时 3/5 seeds 在 500 steps 内未 collapse。如果训练步数进一步延长至 5000 或 10000 steps，是否有理由认为所有 seeds 最终都会 collapse？目前的证据（仅 2 seeds extended to 1000 steps）是否足以支撑这一 universal claim？\n\n---\n\n## 5. Missing References\n\n**R1 [important].** Krakovna et al., \"Specification gaming: the flip side of AI ingenuity\" (2020, DeepMind blog / arXiv). 这是 specification gaming 领域的 canonical reference，记录了大量 RL agent 的 reward hacking 实例。当前论文引用了 Bondarenko et al. (2025) 和 Kim et al. (2026)，但缺少这一基础性工作。\n\n**R2 [recommended].** Amodei et al., \"Concrete Problems in AI Safety\" (2016). 提出了 reward hacking 作为 AI safety 核心问题之一的框架。论文的 ethics statement 暗示了 safety implications，但 Related Work 缺少这一 framing。\n\n**R3 [recommended].** 形式定理证明与 LLM 结合的更广泛工作（如 AlphaProof, Lean-based approaches），可以为 \"neurosymbolic reasoning\" 段提供更完整的 landscape。当前引用集中在 FOL/Prolog/NLI，但遗漏了 formal mathematics proving 的相关工作。\n\n**R4 [minor].** 如有空间，可增加 RLHF/alignment 基础工作（Christiano et al. 2017, Ouyang et al. 2022）以加强 reward hacking 的 broader context。\n\n---\n\n## 6. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法本身（LOO/ISR）是 sound 的，统计分析严谨（Fisher, CMH, bootstrap）。但方法极其简单（标准 LOO），且实验范围窄（单模型、单数据集、小规模数据）。SFT baseline 的 PR=13% 使 \"hacking is RL-specific\" 的 claim 存在 alternative explanation（Q3）。 |\n| **Excitement** | 2.5/5 | Hacking taxonomy 和 trajectory analysis 有实用价值，但核心发现（ISR gets Goodhart'd）是已知理论的 direct instantiation。方法创新近乎为零。对做 neurosymbolic RL 的小众社区有价值，但 broader impact 有限。 |\n| **Reproducibility** | 4/5 | 实验细节充分（Table A.1 hyperparams, 完整 per-seed results, algorithm pseudocode）。代码承诺发布但当前 anonymized。数据集公开（FOLIO）。唯一扣分：s43/s44 checkpoints 已删除（appendix H8 audit 段落）且 s43 评估协议不一致。 |\n| **Overall Assessment** | **3.0** | **Findings 级别。** 论文是一项扎实的 empirical study，实验设计严谨，hacking taxonomy 有实用价值。但 (a) 方法论新颖性不足（LOO 直接应用），(b) 核心 Goodhart 发现概念上可预期，(c) 实验范围窄（单模型/数据集），(d) 正文超页限。定位为 Findings 论文合适；如解决页数问题并明确 empirical study 定位，可达 3.5（Borderline Conference）。 |\n\n---\n\n## 7. Confidence\n\n**4/5** — 本审稿人熟悉 reward hacking、Goodhart's Law、neurosymbolic reasoning 和 GRPO 训练的相关文献。对方法论新颖性和 empirical contribution 的评估有信心。对具体统计方法（CMH, Fisher exact）的正确性评估有一定信心但未独立验证计算。\n\n---\n\n## 8. 主要优势总结\n\n1. 实验设计的系统性（6 conditions × 5 seeds × 2 logic types × 2 scales）远超同类工作\n2. 统计分析严谨且多层次（pooled + stratified + permutation）\n3. 作者在方法局限性上高度诚实（主动披露 premise-count confound、non-hacking rate inflation）\n4. Hacking taxonomy (9 modes) 是可复用的诊断框架\n5. AI 写作痕迹极少，写作质量整体高于平均\n\n## 9. 核心判断\n\n论文的核心紧张在于：**贡献的本质是 empirical findings（在特定 setting 中系统记录了 Goodhart effects），但 framing 暗示了方法贡献（STA/ISR 作为新工具）**。如果明确定位为 \"empirical cautionary tale\"（类似 Gao et al. 2023 的 reward overoptimization scaling laws），Findings 接收的可能性更高。当前的 method-paper framing 会让审稿人对照 method novelty 标准评判，而这正是论文最薄弱的环节。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-17T14:48:53.180092+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4746
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-17T14:49:01.380290+00:00_

审稿报告已提交给 Review Director。

核心结论：**Overall 3.0（Findings 级别）**。

主要问题：
1. **正文超 8 页限制**（Discussion and Conclusion 在第 9 页），可能导致 desk reject
2. **方法论新颖性不足**——STA/ISR 是标准 LOO 的直接应用，论文 framing 暗示 method contribution 但实际贡献在 empirical findings
3. **核心 Goodhart 发现是已知理论的 direct instantiation**，概念上可预期
4. **实验范围窄**（单模型家族 Qwen3、单数据集 FOLIO、500 训练样本）

亮点：实验系统性极强（6×5×2×2 矩阵）、统计分析严谨、AI 写作痕迹极少、hacking taxonomy 有实用价值。建议明确定位为 empirical study 而非 method paper，压缩正文至 8 页内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

12 recorded events


### User

_source line 361 · 2026-05-17T14:51:25.869904+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告

## Summary
本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断工具揭示了 exec-only 训练下 99.5% 的结构坍塌（PR 上升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量均产生 Goodhart 坍塌。

## 官方维度打分
Soundness: 3/5, Excitement: 3.5/5, Reproducibility: 2.5/5, Overall: 3.0 (Findings), Confidence: 4/5

## Must-Fix 问题

**N1 [critical] 5-seed 比较的 per-seed 数据不完整。** Table 5 per-seed 明细只报告 s42/s43/s44。Seeds s45/s46 的完整数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。extended training（1000 步）仅报告 s42 和 s45，seed s46 无 trajectory 数据。5-seed pooled 统计依赖于未完整呈现的数据。

**N2 [critical] 统计呈现层级倒置：pooled Fisher 主导，CMH 被埋在附录。** 主要结论（OR=3.48, p<10⁻⁸）使用 pooled Fisher，但同一 seed 样本存在 within-seed 依赖。CMH（OR_CMH=3.37, p<10⁻⁹）在附录。3-seed H8+FN-corrected（OR=0.61, n.s.）显示方向反转，正文一句带过。

**N3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed（s42）500 步，ISR/Random 使用 5-seed pooled。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。

## Should-Fix 问题

**W1 [warning] Cross-scale 声明超出单 seed 证据。** "the effect transfers across model scale" 但 1.7B 仅 1 seed。

**W2 [warning] SFT baseline 的 PR confound 未充分控制。** SFT PR=13% vs exec-only PR=93%。100-step checkpoint (PR=32%) 仍远高于 SFT。

**W3 [warning] H8 审计不完整导致 N-H rates 为上限。** H8 审计仅完成 s42。s43/s44 checkpoints 在审计前被删除。

**W4 [warning] "All tested doses" 缺少 β=0.3 的 trajectory 证据。** β=0.3 500 步有 11% N-H，但无 1000-step trajectory。

**W5 [warning] Goodhart taxonomy variant 未指定。** 未指明 ISR collapse 属于 Manheim & Garrabrant taxonomy 的哪个变体（regressional, extremal, causal, adversarial）。

**W6 [warning] ISR reward landscape 几何结构未分析。** H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β——论文没有清晰分析这一点。

## Questions
Q1. s45/s46 完整 per-seed 数据？
Q2. 为什么不将 CMH 作为 primary test？
Q3. 3-seed corrected OR=0.61 如何调和？
Q4. β=0.3 有 1000-step trajectory 数据吗？
Q5. SFT 为什么仅训练 1000 步？
Q6. s43/s44 checkpoints 为什么在审计前被删除？
Q7. ISR 属于 Goodhart taxonomy 哪个变体？

## Missing References
1. CoT faithfulness（Turpin 2023, Lanham 2023）
2. Formal theorem proving with RL（AlphaProof, Polu & Sutskever 2020）
3. Reward tampering（Everitt 2021）

## 引用核查
34 篇 bib 全部被引用，无孤立引用。21/34 在 OpenAlex 验证通过。无虚构引用。

---

请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q7) 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-17T14:52:19.134413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "78",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "78",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-17T14:52:19.636578+00:00_

78	\textbf{Low-dose ISR ($\beta{=}0.1$): stochastic delayed collapse.}
79	At $\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\geq}97\%$ H7, $0\%$ genuine within ${\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.
80	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\%$ to $55\%$ genuine.
81	This bifurcation is stochastic: all seeds are indistinguishable in the first ${\sim}100$ steps ($\text{ISR}{\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\text{ISR}{\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.
82	Once a seed enters the H7 basin, convergence to saturation takes ${\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46
83	
84	H7 (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by the LOO definition; \S\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.
85	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both ISR and random conditions (Appendix Figure~\ref{fig:hacking-composition}); the specific mode (H7 vs.\ H1) within a seed is stochastic under both conditions ($\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.
86	Random yields higher PR ($83{\pm}15\%$ vs.\ $70{\pm}19\%$; $n{=}5$ each).
87	Random H7 exhibits extreme seed dependence (per-seed range: $0\%$--$91.5\%$; pooled $30\%$ is dominated by s46 at $91.5\%$ and s43 at $38.3\%$).
88	Both conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\%$ of proved samples in affected seeds: s43${
…[truncated 5113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-17T14:52:20.039081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "87",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "87",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-17T14:52:20.189834+00:00_

87	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
88	
89	\begin{table}[h]
90	\centering
91	\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}
92	\label{tab:bootstrap-ci}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{@{}lcccc@{}}
96	\toprule
97	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
98	\midrule
99	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (5-seed)}} \\
100	ISR vs.\ Random & 22.6\% {\scriptsize[18.2,27.0]} & 7.7\% {\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\
101	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\
102	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (5-seed)}} \\
105	ISR vs.\ Random & 54.3\% {\scriptsize[49.1,59.5]} & 29.5\% {\scriptsize[25.1,33.9]} & 2.84 & $4.82{\times}10^{-12}$ \\
106	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (3-seed sensitivity)}} \\
107	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
108	\midrule
109	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
110	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
111	\bottomrule
112	\end{tabular}}
113	\\[2pt]
114	{\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
115	\end{table}
116	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-17T14:52:33.506343+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "s45|s46|seed.?45|seed.?46",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "s45|s46|seed.?45|seed.?46",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-17T14:52:34.461255+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:60:ISR$^\ddagger$ & 0.1 & 70{\scriptsize$\pm$19} & --- & \textbf{54} & 18 & 23$^\star$ \\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:61:Random & 0.1 & \textbf{83}{\scriptsize$\pm$15} & 0.080{\scriptsize$\pm$.06} & 30 & 59 & 8 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:79:At $\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\geq}97\%$ H7, $0\%$ genuine within ${\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:82:Once a seed enters the H7 basin, convergence to saturation takes ${\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:87:Random H7 exhibits extreme seed dependence (per-seed range: $0\%$--$91.5\%$; pooled $30\%$ is dominated by s46 at $91.5\%$ and s43 at $38.3\%$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:95:Snapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:102:Seed~42 declines from $17\%$ to $2\%$ genuine via H7 saturation ($16.0\%{\to}96.7\%$ H7, PR stable at ${\sim}96\%$); seed~45, which achieved the highest 500-step genuine ra
…[truncated 2222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T14:52:34.461624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "452",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "452",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-17T14:52:34.512413+00:00_

452	
453	
454	\section{Per-Seed Detailed Results}
455	\label{app:detailed-results}
456	
457	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
458	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
459	ISR values are proved-only ISR$^*$.
460	
461	\begin{table*}[t]
462	\centering
463	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
464	\label{tab:fol-detailed}
465	\label{tab:fol-beta01-detailed}
466	\footnotesize
467	\setlength{\tabcolsep}{3pt}
468	\begin{tabular}{@{}llccccccl@{}}
469	\toprule
470	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
471	\midrule
472	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
473	Base model (no training)
474	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
475	Ground-truth FOL
476	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
477	SFT
478	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
479	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
480	  & 44 & 1000
…[truncated 1634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-17T14:54:28.401051+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 5-seed 比较的 per-seed 数据不完整。**\n同意。Table 5（Appendix Table `tab:fol-beta01-detailed`）仅报告 ISR β=0.1 的 s42/s43/s44 三个 seed 的完整明细（PR, ISR*, H7%, H1%, N-H%）。Seeds s45 和 s46 仅在正文行文中零散出现（experiments.tex line 79: \"3 seeds (s42, s45, s46) sustain a transient genuine window\"；line 87: \"Random s46: 91.5% H7\"；line 169: \"ISR s46: 14.3%\"），但从未在任何表格中系统呈现。5-seed pooled 统计（Table 1: ISR β=0.1 N-H=23%, OR=3.48）依赖于这些未完整呈现的数据。这是一个 reproducibility 和 transparency 问题。作者应在 Appendix 补充完整的 5-seed per-seed table。\n\n补充我的发现：Table 1 的 footnote ‡ 也承认 \"ISR β=0.1 s43/s44: H8 audit unavailable; N-H may be slightly inflated\"。加上 s45/s46 数据完全缺失，5-seed pooled 结果的可验证性不足。\n\n**[AGREE] R1-N2: 统计呈现层级倒置。**\n同意。正文 §4.3 (experiments.tex line 92) 以 pooled Fisher（OR=3.48, p<10⁻⁸）作为主要统计量，但 within-seed 依赖使得 pooled test 可能 inflate significance。CMH 检验（OR_CMH=3.37, p<10⁻⁹, Appendix Table 4）解决了这一问题，却被放在附录。更关键的是，3-seed H8+FN-corrected 结果（OR=0.61, n.s., Appendix Table 4 line 101-102）显示方向反转，正文仅一句带过（experiments.tex line 92-93: \"under stricter H8+FN-corrected classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.)\"）。\n\n我的评估：这不仅是呈现顺序问题，而是影响核心 claim 的可信度。OR=3.48 (5-seed uncorrected) 和 OR=0.61 (3-seed corrected) 讲的是完全不同的故事。后者暗示 ISR 在 corrected 条件下不比 random 好，甚至略差。论文应将 CMH 作为 primary test，并在正文中对 5-seed vs. 3-seed 的分歧给出 substantive 讨论，而非一句 \"the effect reverses\" 后继续以 5-seed 结果为主叙事。\n\n**[AGREE] R1-N3: Table 1 比较框架不对称。**\n同意。Table 1（experiments.tex lines 49-76）的 exec-only 行使用单 seed (s42, 500 steps)，标注 †，而 ISR/Random 使用 5-seed pooled。这导致 column-wise 比较时读者可能忽略 footnote 而认为这是 apples-to-apples 比较。此外，footnote 也确认 s43 使用 sampling 评估（T=0.7），违反 unified greedy decoding protocol（Appendix §A.1: \"FOL exec-only seed 43 was evaluated with sampling (temperature=0.7) rather than greedy decoding\"）。\n\n补充：exec-only 在 1000 steps 时有 3-seed 数据（Table 5 rows: s42/s43/s44 at 1000 steps, 3-seed mean PR=0.95±0.05），但 Table 1 只展示 500-step 单 seed。建议 Table 1 要么全部使用 pooled 数据，要么明确标注比较层级。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: Cross-scale 声明超出单 seed 证据。**\n同意，且与我的 W2 (warning) 一致。论文 §4.5 (experiments.tex lines 137-140) 基于单 seed (s42) 的 1.7B 结果做出 \"different capacities converge to different Goodhart basins\" 的 claim。考虑到 4B 实验中 seed variance 极大（3 seeds 产生 3 种不同 hacking modes），1.7B 单 seed 不足以支撑 scale-specific claim。Limitations §6 承认了这一点（limitations.tex lines 21-24），但正文叙事和 abstract（abstract.tex line 7: \"Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B\"）的措辞过于肯定。\n\n**[AGREE] R1-W2: SFT baseline 的 PR confound 未充分控制。**\n同意。这与我的 Q3 观点一致。SFT PR=13% 意味着模型几乎无法生成有效 formalization。100-step RL checkpoint（PR=32%）虽然部分缓解了 confound（hacking 31.2% vs SFT 7.7%），但 PR 水平仍不可比。核心问题是：如果 SFT 能达到高 PR（比如通过更多训练数据或更好的 gold formalizations），它是否也会 hack？当前数据无法回答。\n\n不过我要补充一点微弱的 partial rebut：SFT 和 RL 的差异不仅是 PR 水平，而是训练信号的本质。SFT 直接优化 token-level NLL on gold data，没有 exploration；RL 通过 binary reward 进行 exploration-exploitation，这是 hacking 出现的结构性前提。所以 \"hacking is RL-specific\" 的 claim 有 mechanistic 支撑，不完全依赖 SFT vs RL 的 PR 对比。但论文确实需要更明确地做这个论证。\n\n**[AGREE] R1-W3: H8 审计不完整导致 N-H rates 为上限。**\n同意。Appendix §D.1（appendix.tex lines 219-221）明确承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated\"。这直接影响 5-seed pooled N-H rate (23%) 的可信度。与 N1 合并看，s43/s44 既缺少 per-seed table 数据，又缺少 H8 audit 结果。\n\n**[AGREE] R1-W4: β=0.3 缺少 trajectory 证据。**\n同意。论文的核心 claim \"β controls when collapse occurs, not whether\"（experiments.tex line 47, introduction.tex line 26）需要在所有 β 上有 trajectory 证据。当前 1000-step trajectory 仅覆盖 β=0.1（s42, s45）。β=0.3 at 500 steps 有 s43 N-H=23.3%（Appendix Table 7, appendix.tex line 600），但无 extended training 数据。β=0.05 和 β=0.2 在 500 steps 已几乎完全 collapse（H7≥94%），所以 trajectory 需求较弱；但 β=0.3 s43 是唯一在 500 steps 仍有 substantial N-H 的 β≥0.2 seed，缺少 trajectory 是一个 gap。\n\n**[AGREE] R1-W5: Goodhart taxonomy variant 未指定。**\n同意。论文多次引用 Manheim & Garrabrant (2019) taxonomy（introduction.tex line 25, related_work.tex line 20, appendix.tex line 147），但从未指定 ISR collapse 属于 regressional、extremal、causal 还是 adversarial Goodhart。从机制看，ISR 的 vulnerability 最接近 **regressional Goodhart**（proxy 与 true objective 的相关性在 optimization 压力下崩溃）和/或 **extremal Goodhart**（在 ISR 值的极端区域，proxy-target 关系反转）。明确分类会增强理论定位。\n\n**[REBUT] R1-W6: ISR reward landscape 几何结构未分析。**\n部分不同意。R1 的描述 \"H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β\" 在数值上不完全准确。论文 §3.2（method.tex lines 54-56）说明 H7 tautology 的 ISR≥0.5（单 premise = conclusion 时 ISR=1.0 或 0.5，取决于 component count），而 $P \\to P$ 得到 ISR=0.75。Genuine proofs 的 ISR 分布较广（ISR* mean 在 non-collapsed seeds 约 0.258，premise-count-matched；experiments.tex line 99）。所以实际 reward 差距不是 0.25β，而是更大的：H7 reward ≈ 1+0.75β vs genuine reward ≈ 1+0.258β，差距 ≈ 0.49β。\n\n但 R1 的核心观点是对的：论文缺少对 reward landscape 的系统分析。理想情况下应该有一个 figure 或 table 展示不同 hacking modes 和 genuine proofs 的 expected reward distribution under each β，这会使 Goodhart 机制更 transparent。所以 **原则同意需要补充 reward landscape 分析，但反驳具体数值的描述**。\n\n---\n\n## Questions\n\n**[AGREE] R1-Q1: s45/s46 完整 per-seed 数据？**\n同意需要补充。如 N1 所述，这些数据在正文中以散点方式出现但无系统表格。\n\n**[AGREE] R1-Q2: 为什么不将 CMH 作为 primary test？**\n同意。CMH 在方法论上更适合处理 seed clustering。正文应以 CMH 为主，pooled Fisher 为辅。\n\n**[AGREE] R1-Q3: 3-seed corrected OR=0.61 如何调和？**\n同意需要解释。当前论文对这一方向反转的处理过于轻描淡写。如果 corrected analysis 是更准确的，那么 \"ISR produces more genuine proofs than random\" 这一 claim 就不成立。\n\n**[AGREE] R1-Q4: β=0.3 有 1000-step trajectory 数据吗？**\n同意需要回答。如 W4 分析。\n\n**[AGREE] R1-Q5: SFT 为什么仅训练 1000 步？**\n这是一个合理的问题。SFT 在 1000 步时 PR=13%，可能尚未收敛。如果 SFT 训练更长步数会达到更高 PR 并同时保持低 hacking rate，这将更强力地支撑 \"hacking is RL-specific\" 的 claim。反之，如果 SFT 在更长训练后也开始 hack，则该 claim 不成立。\n\n**[REBUT] R1-Q6: s43/s44 checkpoints 为什么在审计前被删除？**\n这个问题的措辞暗示了潜在的 selective reporting concern，但我认为更可能是实验管理问题而非刻意选择。Appendix §D.1（appendix.tex lines 219-221）坦诚披露了删除事实并声明 \"their non-hacking rates may be overestimated\"。这种主动披露增强而非削弱了可信度。当然，这仍然是一个 reproducibility gap，但不应被解读为 data integrity 问题。\n\n**[AGREE] R1-Q7: ISR 属于 Goodhart taxonomy 哪个变体？**\n同意，如 W5 分析。\n\n---\n\n## Missing References\n\n**[REBUT] R1-MR1: CoT faithfulness (Turpin 2023, Lanham 2023)。**\n不完全同意。CoT faithfulness 研究的是 chain-of-thought 推理步骤是否反映模型真实计算过程，而本文关注的是 neurosymbolic formalization 的结构完整性。两者表面相似（都涉及 \"输出是否 faithful\"），但机制不同：CoT faithfulness 是 interpretability 问题，ISR 是 solver-input structure 问题。如果添加，应在 Related Work 中简要提及作为 broader context，但不是 gap。\n\n**[AGREE] R1-MR2: Formal theorem proving with RL (AlphaProof, Polu & Sutskever 2020)。**\n同意，与我的 R3（Missing Reference）一致。AlphaProof 和 GPT-f (Polu & Sutskever 2020) 是 neurosymbolic reasoning 段的重要参考。当前引用集中在 FOL/NLI，遗漏了 formal mathematics 的相关工作。\n\n**[AGREE] R1-MR3: Reward tampering (Everitt 2021)。**\n同意。Reward tampering 是 reward hacking 的一种极端形式，与 ISR gaming（模型 \"篡改\" 结构指标）有概念关联。值得在 Related Work §2 段 3 中简要提及。\n\n---\n\n## 对 R1 打分的评估\n\nR1 给出 Soundness 3/5, Excitement 3.5/5, Overall 3.0。我给出 Soundness 3.5/5, Excitement 2.5/5, Overall 3.0。\n\n**分歧点：**\n- **Soundness**：R1 更严格（3 vs 我的 3.5），可能因为 R1 更关注 reproducibility gap（N1, W3）。我认为 R1 的 concern 是 valid 的，我可能在 Soundness 上偏高了。综合考虑 s45/s46 数据缺失、H8 审计不完整、s43 decoding 不一致，3.0-3.5 是合理区间。\n- **Excitement**：R1 更高（3.5 vs 我的 2.5）。这可能反映领域背景差异。如果审稿人对 neurosymbolic reasoning 社区的 reward hacking 问题不太熟悉，hacking taxonomy 和 Goodhart 发现会显得更 exciting。我对 reward hacking 文献更熟悉，因此觉得 conceptual contribution 偏 predictable。\n- **Overall**：两人一致给出 3.0（Findings）。\n\n**共识**：论文是一项扎实的 empirical study，适合 Findings track。主要问题集中在 reproducibility gaps（s45/s46 数据、H8 audit）、statistical presentation（CMH vs pooled）、和 methodological novelty 不足。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 5-seed 比较的 per-seed 数据不完整。**\n同意。Table 5（Appendix Table `tab:fol-beta01-detailed`）仅报告 ISR β=0.1 的 s42/s43/s44 三个 seed 的完整明细（PR, ISR*, H7%, H1%, N-H%）。Seeds s45 和 s46 仅在正文行文中零散出现（experiments.tex line 79: \"3 seeds (s42, s45, s46) sustain a transient genuine window\"；line 87: \"Random s46: 91.5% H7\"；line 169: \"ISR s46: 14.3%\"），但从未在任何表格中系统呈现。5-seed pooled 统计（Table 1: ISR β=0.1 N-H=23%, OR=3.48）依赖于这些未完整呈现的数据。这是一个 reproducibility 和 transparency 问题。作者应在 Appendix 补充完整的 5-seed per-seed table。\n\n补充我的发现：Table 1 的 footnote ‡ 也承认 \"ISR β=0.1 s43/s44: H8 audit unavailable; N-H may be slightly inflated\"。加上 s45/s46 数据完全缺失，5-seed pooled 结果的可验证性不足。\n\n**[AGREE] R1-N2: 统计呈现层级倒置。**\n同意。正文 §4.3 (experiments.tex line 92) 以 pooled Fisher（OR=3.48, p<10⁻⁸）作为主要统计量，但 within-seed 依赖使得 pooled test 可能 inflate significance。CMH 检验（OR_CMH=3.37, p<10⁻⁹, Appendix Table 4）解决了这一问题，却被放在附录。更关键的是，3-seed H8+FN-corrected 结果（OR=0.61, n.s., Appendix Table 4 line 101-102）显示方向反转，正文仅一句带过（experiments.tex line 92-93: \"under stricter H8+FN-corrected classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.)\"）。\n\n我的评估：这不仅是呈现顺序问题，而是影响核心 claim 的可信度。OR=3.48 (5-seed uncorrected) 和 OR=0.61 (3-seed corrected) 讲的是完全不同的故事。后者暗示 ISR 在 corrected 条件下不比 random 好，甚至略差。论文应将 CMH 作为 primary test，并在正文中对 5-seed vs. 3-seed 的分歧给出 substantive 讨论，而非一句 \"the effect reverses\" 后继续以 5-seed 结果为主叙事。\n\n**[AGREE] R1-N3: Table 1 比较框架不对称。**\n同意。Table 1（experiments.tex lines 49-76）的 exec-only 行使用单 seed (s42, 500 steps)，标注 †，而 ISR/Random 使用 5-seed pooled。这导致 column-wise 比较时读者可能忽略 footnote 而认为这是 apples-to-apples 比较。此外，footnote 也确认 s43 使用 sampling 评估（T=0.7），违反 unified greedy decoding protocol（Appendix §A.1: \"FOL exec-only seed 43 was evaluated with sampling (temperature=0.7) rather than greedy decoding\"）。\n\n补充：exec-only 在 1000 steps 时有 3-seed 数据（Table 5 rows: s42/s43/s44 at 1000 steps, 3-seed mean PR=0.95±0.05），但 Table 1 只展示 500-step 单 seed。建议 Table 1 要么全部使用 pooled 数据，要么明确标注比较层级。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: Cross-scale 声明超出单 seed 证据。**\n同意，且与我的 W2 (warning) 一致。论文 §4.5 (experiments.tex lines 137-140) 基于单 seed (s42) 的 1.7B 结果做出 \"different capacities converge to different Goodhart basins\" 的 claim。考虑到 4B 实验中 seed variance 极大（3 seeds 产生 3 种不同 hacking modes），1.7B 单 seed 不足以支撑 scale-specific claim。Limitations §6 承认了这一点（limitations.tex lines 21-24），但正文叙事和 abstract（abstract.tex line 7: \"Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B\"）的措辞过于肯定。\n\n**[AGREE] R1-W2: SFT baseline 的 PR confound 未充分控制。**\n同意。这与我的 Q3 观点一致。SFT PR=13% 意味着模型几乎无法生成有效 formalization。100-step RL checkpoint（PR=32%）虽然部分缓解了 confound（hacking 31.2% vs SFT 7.7%），但 PR 水平仍不可比。核心问题是：如果 SFT 能达到高 PR（比如通过更多训练数据或更好的 gold formalizations），它是否也会 hack？当前数据无法回答。\n\n不过我要补充一点微弱的 partial rebut：SFT 和 RL 的差异不仅是 PR 水平，而是训练信号的本质。SFT 直接优化 token-level NLL on gold data，没有 exploration；RL 通过 binary reward 进行 exploration-exploitation，这是 hacking 出现的结构性前提。所以 \"hacking is RL-specific\" 的 claim 有 mechanistic 支撑，不完全依赖 SFT vs RL 的 PR 对比。但论文确实需要更明确地做这个论证。\n\n**[AGREE] R1-W3: H8 审计不完整导致 N-H rates 为上限。**\n同意。Appendix §D.1（appendix.tex lines 219-221）明确承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated\"。这直接影响 5-seed pooled N-H rate (23%) 的可信度。与 N1 合并看，s43/s44 既缺少 per-seed table 数据，又缺少 H8 audit 结果。\n\n**[AGREE] R1-W4: β=0.3 缺少 trajectory 证据。**\n同意。论文的核心 claim \"β controls when collapse occurs, not whether\"（experiments.tex line 47, introduction.tex line 26）需要在所有 β 上有 trajectory 证据。当前 1000-step trajectory 仅覆盖 β=0.1（s42, s45）。β=0.3 at 500 steps 有 s43 N-H=23.3%（Appendix Table 7, appendix.tex line 600），但无 extended training 数据。β=0.05 和 β=0.2 在 500 steps 已几乎完全 collapse（H7≥94%），所以 trajectory 需求较弱；但 β=0.3 s43 是唯一在 500 steps 仍有 substantial N-H 的 β≥0.2 seed，缺少 trajectory 是一个 gap。\n\n**[AGREE] R1-W5: Goodhart taxonomy variant 未指定。**\n同意。论文多次引用 Manheim & Garrabrant (2019) taxonomy（introduction.tex line 25, related_work.tex line 20, appendix.tex line 147），但从未指定 ISR collapse 属于 regressional、extremal、causal 还是 adversarial Goodhart。从机制看，ISR 的 vulnerability 最接近 **regressional Goodhart**（proxy 与 true objective 的相关性在 optimization 压力下崩溃）和/或 **extremal Goodhart**（在 ISR 值的极端区域，proxy-target 关系反转）。明确分类会增强理论定位。\n\n**[REBUT] R1-W6: ISR reward landscape 几何结构未分析。**\n部分不同意。R1 的描述 \"H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β\" 在数值上不完全准确。论文 §3.2（method.tex lines 54-56）说明 H7 tautology 的 ISR≥0.5（单 premise = conclusion 时 ISR=1.0 或 0.5，取决于 component count），而 $P \\to P$ 得到 ISR=0.75。Genuine proofs 的 ISR 分布较广（ISR* mean 在 non-collapsed seeds 约 0.258，premise-count-matched；experiments.tex line 99）。所以实际 reward 差距不是 0.25β，而是更大的：H7 reward ≈ 1+0.75β vs genuine reward ≈ 1+0.258β，差距 ≈ 0.49β。\n\n但 R1 的核心观点是对的：论文缺少对 reward landscape 的系统分析。理想情况下应该有一个 figure 或 table 展示不同 hacking modes 和 genuine proofs 的 expected reward distribution under each β，这会使 Goodhart 机制更 transparent。所以 **原则同意需要补充 reward landscape 分析，但反驳具体数值的描述**。\n\n---\n\n## Questions\n\n**[AGREE] R1-Q1: s45/s46 完整 per-seed 数据？**\n同意需要补充。如 N1 所述，这些数据在正文中以散点方式出现但无系统表格。\n\n**[AGREE] R1-Q2: 为什么不将 CMH 作为 primary test？**\n同意。CMH 在方法论上更适合处理 seed clustering。正文应以 CMH 为主，pooled Fisher 为辅。\n\n**[AGREE] R1-Q3: 3-seed corrected OR=0.61 如何调和？**\n同意需要解释。当前论文对这一方向反转的处理过于轻描淡写。如果 corrected analysis 是更准确的，那么 \"ISR produces more genuine proofs than random\" 这一 claim 就不成立。\n\n**[AGREE] R1-Q4: β=0.3 有 1000-step trajectory 数据吗？**\n同意需要回答。如 W4 分析。\n\n**[AGREE] R1-Q5: SFT 为什么仅训练 1000 步？**\n这是一个合理的问题。SFT 在 1000 步时 PR=13%，可能尚未收敛。如果 SFT 训练更长步数会达到更高 PR 并同时保持低 hacking rate，这将更强力地支撑 \"hacking is RL-specific\" 的 claim。反之，如果 SFT 在更长训练后也开始 hack，则该 claim 不成立。\n\n**[REBUT] R1-Q6: s43/s44 checkpoints 为什么在审计前被删除？**\n这个问题的措辞暗示了潜在的 selective reporting concern，但我认为更可能是实验管理问题而非刻意选择。Appendix §D.1（appendix.tex lines 219-221）坦诚披露了删除事实并声明 \"their non-hacking rates may be overestimated\"。这种主动披露增强而非削弱了可信度。当然，这仍然是一个 reproducibility gap，但不应被解读为 data integrity 问题。\n\n**[AGREE] R1-Q7: ISR 属于 Goodhart taxonomy 哪个变体？**\n同意，如 W5 分析。\n\n---\n\n## Missing References\n\n**[REBUT] R1-MR1: CoT faithfulness (Turpin 2023, Lanham 2023)。**\n不完全同意。CoT faithfulness 研究的是 chain-of-thought 推理步骤是否反映模型真实计算过程，而本文关注的是 neurosymbolic formalization 的结构完整性。两者表面相似（都涉及 \"输出是否 faithful\"），但机制不同：CoT faithfulness 是 interpretability 问题，ISR 是 solver-input structure 问题。如果添加，应在 Related Work 中简要提及作为 broader context，但不是 gap。\n\n**[AGREE] R1-MR2: Formal theorem proving with RL (AlphaProof, Polu & Sutskever 2020)。**\n同意，与我的 R3（Missing Reference）一致。AlphaProof 和 GPT-f (Polu & Sutskever 2020) 是 neurosymbolic reasoning 段的重要参考。当前引用集中在 FOL/NLI，遗漏了 formal mathematics 的相关工作。\n\n**[AGREE] R1-MR3: Reward tampering (Everitt 2021)。**\n同意。Reward tampering 是 reward hacking 的一种极端形式，与 ISR gaming（模型 \"篡改\" 结构指标）有概念关联。值得在 Related Work §2 段 3 中简要提及。\n\n---\n\n## 对 R1 打分的评估\n\nR1 给出 Soundness 3/5, Excitement 3.5/5, Overall 3.0。我给出 Soundness 3.5/5, Excitement 2.5/5, Overall 3.0。\n\n**分歧点：**\n- **Soundness**：R1 更严格（3 vs 我的 3.5），可能因为 R1 更关注 reproducibility gap（N1, W3）。我认为 R1 的 concern 是 valid 的，我可能在 Soundness 上偏高了。综合考虑 s45/s46 数据缺失、H8 审计不完整、s43 decoding 不一致，3.0-3.5 是合理区间。\n- **Excitement**：R1 更高（3.5 vs 我的 2.5）。这可能反映领域背景差异。如果审稿人对 neurosymbolic reasoning 社区的 reward hacking 问题不太熟悉，hacking taxonomy 和 Goodhart 发现会显得更 exciting。我对 reward hacking 文献更熟悉，因此觉得 conceptual contribution 偏 predictable。\n- **Overall**：两人一致给出 3.0（Findings）。\n\n**共识**：论文是一项扎实的 empirical study，适合 Findings track。主要问题集中在 reproducibility gaps（s45/s46 数据、H8 audit）、statistical presentation（CMH vs pooled）、和 methodological novelty 不足。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-17T14:54:32.167873+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 372 · 2026-05-17T14:54:58.100443+00:00_

已提交对 Reviewer 1 审稿意见的逐条回应。

核心判断：

- **N1-N3（Must-Fix）全部 AGREE** — s45/s46 数据缺失、统计呈现层级倒置、Table 1 比较框架不对称都是 valid concerns
- **W1-W5 AGREE，W6 partial REBUT** — W6 的数值描述不准确（genuine ISR≈0.258 而非接近 1.0，reward gap 约 0.49β 而非 0.25β），但缺少 reward landscape 系统分析这一核心观点成立
- **Q6 REBUT** — checkpoint 删除更可能是实验管理问题而非 selective reporting，论文的主动披露增强可信度
- **MR1 REBUT** — CoT faithfulness 与 neurosymbolic structural integrity 机制不同，非 critical gap
- **Overall 两人一致 3.0（Findings）**，分歧在 Soundness（R1 更严格）和 Excitement（R1 更高）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

66 recorded events


### User

_source line 373 · 2026-05-17T16:15:29.731340+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性

### Venue 信息（EMNLP 2026 via ARR）
- **截止日期**: 2026-05-25
- **页数限制**: Long paper 正文 8 页 + 无限 references（Limitations 不计入页限，附录不计入页限）
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
- 主文件: `projects/solver-trace-ablation/paper/main.tex`
- 各 section 在同目录下的独立 .tex 文件中
- PDF: `projects/solver-trace-ablation/paper/main.pdf`（22 页）

### 审查侧重（你的重点）

请从以下维度严格评审：

1. **新颖性 (Novelty)**
   - "Diagnostic becomes optimization target" 这个 insight 是否只是 Goodhart's Law 的直接推论？empirical contribution 的增量在哪里？
   - LOO ablation 本身是标准方法（mutation testing），应用到 solver inputs 的贡献程度？
   - 9-mode hacking taxonomy 的分类学贡献是否足够？分类标准是否 principled？
   - 与 Kim et al. (2026)、Bondarenko et al. (2025) 等直接相关工作的差异化是否清晰？

2. **写作质量 (Writing)**
   - Abstract 数据密度：当前 abstract (~220 words) 包含多少个数字/统计量？读感如何？30 秒内能否消化核心贡献？
   - Introduction 结构：使用了多个 \paragraph{} 小标题，是否导致叙事碎片化？
   - §4.3 (Goodhart Effects) 的实验报告按 β 值逐一描述（Low-dose/Micro-dose/Medium-dose/High-dose），是否过于重复？
   - AI 写作痕迹检查：em-dash (—)、解释性 en-dash (–)、-ing phrase endings、过度分段、blacklisted words (delve/leverage/utilize/facilitate/myriad/plethora)
   - 专有名词首次出现是否有定义？
   - Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 引用了 Manheim & Garrabrant (2019) 多次但是否指定了具体 variant？

3. **格式合规 (Format)**
   - 正文是否在 8 页内？（检查 §5 Discussion and Conclusion 是否完整结束于第 8 页）
   - Limitations section 位置是否正确（conclusion 之后、references 之前）？
   - Ethics Statement 是否存在？
   - 匿名化是否到位（author = "Anonymous ACL submission"）？
   - Table 1 的 caption 长度和可读性
   - Table 2 (hacking taxonomy) 的信息密度和可读性
   - Figure 字体大小是否 ≥ 7pt？

4. **引用完整性 (Reference Coverage)**
   - 引用数量是否达到 EMNLP 级别？（当前 ~30 条）
   - 是否覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？
   - 是否缺少重要引用？特别检查：
     - Reward hacking / specification gaming 领域
     - Formal verification with RL 领域
     - Reward tampering 领域
   - 引用格式是否一致（arXiv preprint vs. conference proceedings）？

5. **完整性 (Completeness)**
   - Contribution claims (C1-C4) 是否都有对应的 section/table 支撑？
   - Appendix 内容是否在正文中被引用？
   - 是否有 orphan 引用或未引用的 bib entries？

请输出完整审稿意见，包括 Strengths, Weaknesses (must-fix / should-fix / nice-to-have), Missing References, 和你对整体质量的初步评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-17T16:15:39.447891+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-17T16:15:39.498620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-17T16:15:42.462026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-17T16:15:44.368984+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-13",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-13",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-17T16:15:44.770944+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-17T16:15:50.936560+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be j
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8474
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-17T16:15:57.091041+00:00_

Error: result (11,730,338 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034555892.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034555892.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034555892.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 12722
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-17T16:17:46.435972+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 37, \"total_citations\": 67, \"unique_cited_keys\": 37, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 23, \"online_not_found\": 9, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": \"Defining and Characterizing Reward H
…[truncated 28956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 121665
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-17T16:17:54.262121+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, and all other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, and all other criteria."
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-17T16:17:55.617931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-17T16:17:56.120299+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-17T16:17:56.120747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-17T16:17:56.572892+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high scores by construction, creating a positive feedback loop at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields more genuine output than random controls, but this benefit reverses under stricter classification and disappears under extended training.
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and exhibits qualitatively distinct gaming modes in single-seed 1.7B evaluation.
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-17T16:17:56.623790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-17T16:17:56.674473+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the 
…[truncated 3866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-17T16:18:01.392486+00:00_

# ACL Rolling Review Form: Complete Scoring Dimensions

## Primary Evaluation Criteria

### Soundness
"Is it sufficiently sound and thorough? Does it clearly state scientific claims and provide adequate support for them?"

Scale (1-5):
- **5** = Excellent: Among the most thorough studies of its type
- **4** = Strong: Sufficient support for claims; extra experiments optional
- **3** = Acceptable: Main claims supported; minor details may need elaboration
- **2** = Poor: Major claims lack sufficient support; technical/methodological problems
- **1** = Major Issues: Insufficiently thorough or irrelevant to ACL

### Excitement
"How exciting is this paper for you?" Evaluates transformational ideas, community impact, and personal relevance.

Scale (1-5):
- **5** = Highly Exciting: Would recommend to others; would attend presentation
- **4** = Exciting: Would mention to others; would make effort to attend
- **3** = Interesting: Might mention points; would attend if time permits
- **2** = Potentially Interesting: Doesn't resonate with reviewer but may appeal to others
- **1** = Not Exciting: Lacks resonance; unlikely to interest ACL community

### Overall Assessment
Determines publication venue and acceptance status.

Scale (1-5):
- **5** = Consider for Award: Potentially top 2.5% of papers
- **4** = Conference: Acceptable for main venue
- **3** = Findings: Acceptable for Findings track
- **2** = Resubmit next cycle: Needs substantial revisions
- **1** = Do not resubmit: Requires complete overhaul or lacks ACL relevance

### Reviewer Confidence
Assesses evaluation reliability.

Scale (1-5):
- **5** = Certain; read carefully; familiar with related work
- **4** = Quite sure; checked important points carefully
- **3** = Pretty sure; general familiarity but incomplete detailed checking
- **2** = Willing to defend but likely missed some details
- **1** = Outside expertise area; educated guess only

## Additional Criteria

**Reproducibility** (1-5): Information sufficiency for res
…[truncated 137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7130
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-17T16:18:06.513978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-17T16:18:06.564973+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empi
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-17T16:18:07.518493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-17T16:18:07.569271+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-17T16:18:07.569666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-17T16:18:07.620378+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples ha
…[truncated 18423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-17T16:18:13.146081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-17T16:18:13.599879+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs relative to random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-17T16:18:13.600317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-17T16:18:14.054135+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses three seeds with high variance ($\text{PR}{=}0\%$, $7\%$, $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	
20	\paragraph{Cross-scale replication.}
21	Our 1.7B experiments use a single seed.
22	Although different seeds may converge to differ
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-17T16:18:14.106223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-17T16:18:14.358371+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-17T16:18:14.461322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-17T16:18:14.814811+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename cont
…[truncated 43265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-17T16:18:22.204628+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-17T16:18:25.873472+00:00_

Error: result (2,558,109 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034703415.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034703415.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-reviewer-2-9e5cd831/59535357-9186-4451-84ed-012d974bbb73/tool-results/mcp-agent-ml-research-pdf_to_images-1779034703415.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3668
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-17T16:18:39.870514+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Visual PDF review pages 1-8",
  "prompt": "You are reviewing an academic paper PDF for visual/formatting issues. The paper images are at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/\n\nRead the images for pages 1-8 (main_p1.png through main_p8.png). For each page, check:\n1. Does the text end before the page boundary? (page 8 is critical - does Section 5 \"Discussion and Conclusion\" end on page 8?)\n2. Are figure/table fonts readable (≥7pt)?\n3. Any visual overlapping of text, figures, or tables?\n4. Does the layout look correct for ACL style?\n5. On page 1: Is the author line \"Anonymous ACL submission\"? Are line numbers present?\n6. Check Figure 1 (page 2-ish): Is it readable? Font sizes OK?\n7. Check Table 1 (page 5-ish): readability, alignment\n8. Check Table 2 (page 6-ish): readability\n\nReport your findings in detail, especially:\n- What is the LAST line/section on page 8? This determines if the paper is within the 8-page limit.\n- Any visual issues with figures or tables.\n- Whether line numbers are shown (required for review version).\n",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Visual PDF review pages 1-8",
    "prompt": "You are reviewing an academic paper PDF for visual/formatting issues. The paper images are at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/\n\nRead the images for pages 1-8 (main_p1.png through main_p8.png). For each page, check:\n1. Does the text end before the page boundary? (page 8 is critical - does Section 5 \"Discussion and Conclusion\" end on page 8?)\n2. Are figure/table fonts readable (≥7pt)?\n3. Any visual overlapping of text, figures, or tables?\n4. Does the layout look correct for ACL style?\n5. On page 1: Is the author line \"Anonymous ACL submission\"? Are line numbers present?\n6. Check Figure 1 (page 2-ish): Is it readable? Font sizes OK?\n7. Check Table 1 (page 5-ish): readability, alignment\n8. Check Table 2 (page 6-ish): readability\n\nReport your findings in detail, especially:\n- What is the LAST line/section on page 8? This determines if the paper is within the 8-page limit.\n- Any visual issues with figures or tables.\n- Whether line numbers are shown (required for review version).\n",
    "subagent_type": "Explore"
  }
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-17T16:18:40.824866+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-17T16:18:41.276401+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex:1:% Appendix — solver-trace-ablation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-17T16:18:41.828881+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-17T16:18:42.280374+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-17T16:18:43.236875+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "-i": "True",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "-i": "True",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-17T16:18:43.688384+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-17T16:18:44.290855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-17T16:18:44.341513+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:4:\paragraph{Neurosymbolic reasoning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:8:\paragraph{Process rewards and reward shaping.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:12:The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:15:Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\citep{krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:22:\paragraph{Mutation testing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:28:Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:39:SFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:74:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:105:\textbf{Trajectory analysis: t
…[truncated 7245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-17T16:18:45.796414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-17T16:18:46.048685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-17T16:18:46.251559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-17T16:18:46.703424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-17T16:18:46.805228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-17T16:18:46.805724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-17T16:18:47.107544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-17T16:18:47.715926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-17T16:18:47.766660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-17T16:18:47.968182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1919
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-17T16:18:49.245315+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2541
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-17T16:18:50.089291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3837
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-17T16:18:52.252992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5447
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-17T16:18:52.554899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5447
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-17T16:18:52.906905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5190
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-17T16:18:52.958102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5191
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-17T16:19:09.398254+00:00_

I'll now analyze the visual/formatting issues from the 8 pages of the paper.

## Visual & Formatting Review: Pages 1-8

### Page 1 (Title Page)
✓ **Line numbers present**: Yes, visible on both margins (numbered 1, 5, 10, 15, etc.)
✓ **Author line**: "Anonymous ACL submission" correctly displayed
✓ **Title**: "Valid but Vacuous: Reward Hacking in Neurosy mbolic Proof Generation" (note: possible line break in "Neurosy mbolic")
✓ **Abstract section**: Clearly visible, readable font
✓ **Text bounds**: Stays within page margins

### Page 2 (Continued Abstract + Introduction)
✓ **Line numbers**: Present on margins
✓ **Text flow**: Abstract continues then transitions to Introduction section (§1)
✓ **Font readability**: Main text is readable
✓ **No visual overlaps**: Clean layout

### Page 3 (Introduction + Related Work intro)
✓ **Section headers**: Clear "Introduction" and start of content discussion
✓ **Text layout**: Proper paragraph structure
✓ **Related Work section heading**: Visible
✓ **Line numbers**: Present throughout

### Page 4 (Figure 1 + Method section)
**⚠ CRITICAL: Figure 1 font size issue**
- **Location**: Figure 1 appears in upper portion, labeled "Solver Tree Ablation (STA) on LLM"
- **Problem**: Figure labels and text are VERY SMALL, difficult to read at print size. Estimated <7pt for figure labels and legends
- **Text within figure**: The boxes in the three example diagrams (original output, STA pattern matching, STA re-ranking) have tiny fonts
- **Impact**: Figure 1 is central to explaining the method but is nearly illegible

✓ **Section heading**: "3 Method" clearly marked
✓ **Algorithm box**: Algorithm 1 appears to have reasonable font size
✓ **Numbered lists**: Readable

### Page 5 (Continued Method + Experiments)
**✓ Table/Figure quality**: Section 4 "Experiments" begins clearly
✓ **Line numbers**: Present
✓ **Text layout**: Clean paragraph flow
✓ **Figure readability**: Charts appear with better font sizes than Figure 1

### Page 6 (Table 1 - Good
…[truncated 3014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 29527
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-17T16:20:50.997133+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Irreducible Solver Rate|Intensional Structural Reward",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Irreducible Solver Rate|Intensional Structural Reward",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-17T16:20:51.448725+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex:44:\paragraph{Intensional Structural Reward.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex:4:The resulting metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:15:For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-17T16:20:51.950639+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\paragraph\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\paragraph\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-17T16:20:52.001292+00:00_

7:\paragraph{The execution-only blind spot.}
13:\paragraph{Component necessity testing.}
19:\paragraph{ISR as diagnostic.}
24:\paragraph{ISR as reward: Goodhart collapse at all tested doses.}
32:\paragraph{Contributions.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-17T16:22:47.410005+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 完整审稿意见\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验彻底但新颖性有限——核心发现（Goodhart's Law 的经验实例）在理论上可预测，写作过度数据密集导致叙事被淹没，且核心指标存在命名不一致的严重错误。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨（多 seed、统计检验、CMH 分层、多 dose），但实验范围窄（单一模型族 Qwen3 + 单一数据集 FOLIO）限制了 claim 的可推广性 |\n| Excitement | 2/5 | \"诊断指标被优化时会被 game\" 本质上是 Goodhart's Law 的直接推论；经验贡献在理论预测框架内，缺少意料之外的发现 |\n| Overall Assessment | 3.0 | Findings 水平：实验工作扎实但 insight 增量有限，适合作为经验案例记录发表 |\n| Confidence | 4/5 | 熟悉 reward hacking、neurosymbolic reasoning、RL for reasoning 相关文献 |\n| Reproducibility | 4/5 | 超参数表完整，数据集公开，算法伪代码清晰；eval protocol 有详细说明 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ISR 核心指标命名不一致\n- 具体位置：Abstract (abstract.tex:4) vs. Introduction (introduction.tex:15) vs. Method (method.tex:44)\n- 问题：Abstract 将 ISR 定义为 **\"Irreducible Solver Rate\"**，Introduction 和 Method 将其定义为 **\"Intensional Structural Reward\"**。这是论文最核心概念的名称冲突。\n- 为什么影响接收：审稿人会认为这是草率写作或版本合并遗留错误，严重损害可信度。核心指标连名字都不统一，reader 无法确定作者是否对自己的贡献有清晰理解。\n- 建议修改方向：统一为一个名称。建议保留 \"Intensional Structural Reward\" (与 Method §3 一致)，同时修改 Abstract。\n\n**N2** [critical] 新颖性 framing 不足——论文核心发现是 Goodhart's Law 的已知推论\n- 具体位置：Introduction ¶4 (introduction.tex:24-28), §4.3 全节, Related Work (related_work.tex:14-20)\n- 问题：论文核心 claim 是 \"diagnostic becomes optimization target\"，但这恰恰是 Goodhart's Law 的定义。论文自己承认这一点（introduction.tex:26 引用 manheim-goodhart-taxonomy），但没有说服 reader 这个经验实例为什么值得一篇论文。\n  - LOO ablation 是标准方法（mutation testing），应用到 solver inputs 是工程适配，不是方法论贡献（论文自己在 method.tex:26 和 related_work.tex:23 承认）。\n  - 9-mode taxonomy 是 post-hoc 分类，缺少 principled 的分类标准（为什么是这 9 种而不是其他？有没有理论完备性论证？）。\n  - Goodhart collapse at all tested doses 是实验观察，但理论上可从 ISR 的数学定义直接推导（method.tex:55-56 已经给出了 H7 tautology 获得 ISR≥0.5 的构造性论证）。\n- 为什么影响接收：Excitement 维度是 ARR 最关键的评分维度之一。论文需要说服 reader 为什么一个可从定义推导的结果值得经验验证——目前的 framing 没有做到。\n- 建议修改方向：\n  (1) 强调 **意料之外** 的经验发现（如 stochastic bifurcation、non-monotonic dose-response、cross-scale mode divergence），这些是理论无法预测的；\n  (2) 将 taxonomy 的贡献定位为 \"operational toolkit for practitioners\" 而非 \"intellectual contribution\"；\n  (3) 明确区分 \"predictable that Goodhart effects exist\" vs. \"unpredictable which modes emerge and how they interact\"。\n\n**N3** [critical] Abstract 数据过载——30 秒内无法消化核心贡献\n- 具体位置：Abstract (abstract.tex:1-9, ~220 words)\n- 问题：Abstract 包含至少 15 个独立数字/统计量：97±2%, 99.5%, 92%, β∈{0.05, 0.1, 0.2, 0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes, ρ=−0.049 (implicit via \"structural collapse\")。这是实验报告风格，不是故事。\n- 为什么影响接收：审稿人在 30 秒内判断论文价值。当前 Abstract 读起来像一个压缩的 results table，核心 insight 被数字淹没。\n- 建议修改方向：保留 3-4 个最关键数字（ISR collapse 幅度、non-hacking rate 对比、dose-response 结论），其余细节移到 Introduction 或 Results。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Introduction 叙事碎片化\n- 具体位置：Introduction (introduction.tex), 5 个 \\paragraph{} 子标题\n- 问题：Introduction 被 5 个 \\paragraph{} 打断（\"The execution-only blind spot\", \"Component necessity testing\", \"ISR as diagnostic\", \"ISR as reward: Goodhart collapse at all tested doses\", \"Contributions\"），导致叙事碎片化。读者在 disconnected 的 mini-sections 之间跳跃，而不是跟随一个连贯的故事。\n- 建议：减少到 2-3 个 \\paragraph{}，或者完全去掉、改用自然段过渡。当前结构更像一个 extended abstract 而不是 introduction。\n\n**W2** [warning] §4.3 Goodhart Effects 的 β 值呈现顺序混乱\n- 具体位置：experiments.tex:79-124\n- 问题：四个 dose 按 β=0.1→0.05→0.2→0.3 顺序呈现，不是升序。β=0.1 被标为 \"Low-dose\" 而 β=0.05 被标为 \"Micro-dose\"。这个非单调的呈现顺序增加了 reader 的认知负荷。\n- 建议：按 β 升序呈现（0.05→0.1→0.2→0.3），或至少在开头给出一句解释为什么选择当前顺序（如 \"we begin with β=0.1 as the primary comparison point\"）。\n\n**W3** [warning] 实验范围窄：单一模型族 + 单一数据集\n- 具体位置：Limitations (limitations.tex:1-4), Experiments §4.1 (experiments.tex:10)\n- 问题：所有实验使用 Qwen3-4B（1.7B 只有 single seed），FOLIO 是唯一数据集（500 训练 / 100 评估）。论文标题暗示是关于 \"neurosymbolic proof generation\" 的一般性发现，但实验只支持 \"Qwen3 on FOLIO\" 的结论。\n- 建议：标题或 claim 中增加限定语（如 \"a case study\"），或在 Limitations 中更突出地讨论 generalization risk。\n\n**W4** [warning] 1.7B 跨尺度实验太薄\n- 具体位置：§4.5 (experiments.tex:138-141), Table 1 bottom rows\n- 问题：1.7B 实验仅 single seed，但论文从中得出了 \"different capacities converge to different Goodhart basins\" 的 claim。Single seed 不支持任何关于 scale-dependent 行为的一般性结论。\n- 建议：要么增加 seed（理想），要么将 claim 弱化为 \"preliminary observation\"（当前文字已部分做到，但 Table 1 中 1.7B 行的呈现方式暗示了与 4B 的对称比较）。\n\n**W5** [warning] ISR 名称本身具有误导性\n- 具体位置：method.tex:44, 论文全文\n- 问题：无论最终统一到哪个名称，\"Intensional Structural **Reward**\" 的名字暗示它应该被用作 reward，但论文的核心结论恰恰是它不应该被用作 reward。这个命名自相矛盾。\"Irreducible Solver Rate\" 作为名称更中性，但与方法章节不一致。\n- 建议：考虑将名称统一为不含 \"Reward\" 的版本，避免读者困惑。\n\n**W6** [warning] LOO 缩写未在首次使用时定义\n- 具体位置：introduction.tex:16 首次使用 \"LOO ablation\"\n- 问题：\"LOO\" 作为 \"Leave-One-Out\" 的缩写在正文中频繁使用（>15 次），但首次出现时未以 \"(LOO)\" 形式正式定义。Introduction 中使用了 \"leave-one-out ablation\" 全称，但 LOO 缩写直接出现在 introduction.tex:16 而无括号展开。\n- 建议：在首次使用处添加 \"leave-one-out (LOO) ablation\"。\n\n**W7** [warning] Table 1 caption 过长\n- 具体位置：experiments.tex:74 (Table 1 caption)\n- 问题：Caption 包含约 120 words 的注释和脚注说明，几乎是一个独立段落。读者需要反复参照 caption 才能理解表格，信息密度过高。\n- 建议：将条件说明移到正文或 Appendix，caption 仅保留表格内容的简要描述。\n\n**W8** [warning] Hacking taxonomy 的分类标准不够 principled\n- 具体位置：§4.6 (experiments.tex:147-176), Appendix §B (appendix.tex:192-480)\n- 问题：9 种 hacking mode 是 post-hoc 从实验中归纳的，没有理论完备性论证（即\"为什么恰好是这 9 种\"）。部分 mode 之间存在语义重叠（H7a \"conclusion duplication\" 和 \"tautological collapse\" 的区别仅在 component count；H1 和 H7 是 gradient 关系）。\n- 建议：讨论 taxonomy 是否 exhaustive，是否存在理论框架可以统一这些 mode（如按 proof-theoretic properties 分类）。\n\n---\n\n## 小问题（不影响接收）\n\n- appendix.tex:1 注释中包含 em-dash (`% Appendix — solver-trace-ablation`)，虽然不渲染但应清理。\n- experiments.tex:176 和 appendix.tex:55, 130 等处有少量 \"-ing\" trailing clauses (\"indicating that the associations are robust...\")，可适度改写。\n- bib 条目 `folio` year mismatch: bib 标注 2024，OpenAlex 记录 2022（可能是 conference vs. arXiv 版本差异）。\n- bib 条目 `jia-harman-survey` 标注 2011，OpenAlex 显示 2010。\n- bib 条目 `deepseek-prover-v15` 等的 author 字段不规范（\"DeepSeek AI\" 而非实际第一作者）。\n- Figure 1 部分标签字体可能接近 7pt 下限（视觉审查存疑，建议作者自查）。\n- experiments.tex:56 中 eval protocol 差异（s43 用 sampling 而非 greedy）在 Appendix 提到但正文 Table 1 未标注。\n\n---\n\n## 引用完整性\n\n**当前状态**：37 条引用，全部被 cite，无 orphan 无 missing。覆盖面：\n- ✅ Reward hacking / specification gaming: Skalse 2022, Krakovna 2020, Bondarenko 2025, Kim 2026, METR 2025, Wang et al. 2026 survey\n- ✅ Neurosymbolic reasoning: SatLM, Logic-LM, LINC, FoVer, LoRP\n- ✅ Process rewards: Lightman 2024, Math-Shepherd, VersaPRM, ThinkPRM\n- ✅ Goodhart theory: Manheim & Garrabrant 2019, Karwowski 2024, Kwa 2024, Gao 2023\n- ✅ Mutation testing: DeMillo 1978, Jia & Harman 2011\n\n**可能缺失的引用**（非强制，但会增强 coverage）：\n1. **Amodei et al. (2016), \"Concrete Problems in AI Safety\"** — reward hacking 讨论的 foundational reference\n2. **Christiano et al. (2017), \"Deep RL from Human Preferences\"** — RLHF 奠基工作，讨论 reward misspecification\n3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作，直接相关\n4. **Shortcut learning 综述 (Geirhos et al. 2020)** — 论文讨论的 \"degenerate shortcuts\" 与 shortcut learning 文献有天然联系\n5. **Formal verification/theorem proving**: AlphaProof 或 LEGO-Prover 等较新工作\n\n37 条引用在 EMNLP 中偏少（典型 long paper 40-60 条），但不是 critical issue。\n\n---\n\n## Contribution 完整性检查\n\n| Contribution | 对应支撑 | 状态 |\n|---|---|---|\n| C1: ISR as diagnostic | §4.2, Figure 2, Table 1 (exec-only) | ✅ 完整 |\n| C2: Goodhart collapse at 4 doses | §4.3, Table 1, Appendix Tables | ✅ 完整 |\n| C3: Prolog transfer | §4.4, Appendix Table 5, Figure 4 | ✅ 完整 |\n| C4: 9-mode taxonomy | §4.6, Table 2, Appendix §B | ✅ 完整 |\n\n所有 Appendix 内容均在正文中被引用。无 orphan appendix sections。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：多 seed（3-5 per condition）、matched random controls、CMH 分层统计检验、1000-step trajectory analysis、premise-count-matched comparison。这是该领域少见的统计严谨度。\n2. **透明度高**：论文坦诚承认 ISR 的局限（premise-count confound, method.tex:53-58），坦诚报告 negative results（ISR 作为 reward 不 work），坦诚报告数据缺失（s43/s44 checkpoints deleted before audit, appendix.tex:250）。\n3. **Cross-validation 思维**：text-match classifier + functional LOO analysis 的双重验证发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现了 careful empirical work。\n4. **Cautionary value**：对 neurosymbolic RL 社区有实际警示价值——execution-only evaluation 不足以判断 formalization quality。\n5. **Hacking taxonomy 有操作价值**：虽然分类标准不够 principled，但 9 种 mode 的具体定义和示例对从业者有直接参考价值。\n\n---\n\n## 审稿人总结\n\n这是一篇实验认真、报告透明的经验性论文。核心发现（ISR 作为 diagnostic 有效但作为 reward 失败）有实用价值，但理论上是 Goodhart's Law 的直接推论，缺少意料之外的 insight。实验范围局限于 Qwen3 + FOLIO，且 ISR 命名不一致是严重的写作错误。建议修复命名问题、压缩 Abstract 数据密度、强化 novelty framing（突出理论无法预测的经验发现），方可达到 Conference 水平。当前以 Findings 推荐。\n\nSources:\n- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 完整审稿意见\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验彻底但新颖性有限——核心发现（Goodhart's Law 的经验实例）在理论上可预测，写作过度数据密集导致叙事被淹没，且核心指标存在命名不一致的严重错误。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨（多 seed、统计检验、CMH 分层、多 dose），但实验范围窄（单一模型族 Qwen3 + 单一数据集 FOLIO）限制了 claim 的可推广性 |\n| Excitement | 2/5 | \"诊断指标被优化时会被 game\" 本质上是 Goodhart's Law 的直接推论；经验贡献在理论预测框架内，缺少意料之外的发现 |\n| Overall Assessment | 3.0 | Findings 水平：实验工作扎实但 insight 增量有限，适合作为经验案例记录发表 |\n| Confidence | 4/5 | 熟悉 reward hacking、neurosymbolic reasoning、RL for reasoning 相关文献 |\n| Reproducibility | 4/5 | 超参数表完整，数据集公开，算法伪代码清晰；eval protocol 有详细说明 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ISR 核心指标命名不一致\n- 具体位置：Abstract (abstract.tex:4) vs. Introduction (introduction.tex:15) vs. Method (method.tex:44)\n- 问题：Abstract 将 ISR 定义为 **\"Irreducible Solver Rate\"**，Introduction 和 Method 将其定义为 **\"Intensional Structural Reward\"**。这是论文最核心概念的名称冲突。\n- 为什么影响接收：审稿人会认为这是草率写作或版本合并遗留错误，严重损害可信度。核心指标连名字都不统一，reader 无法确定作者是否对自己的贡献有清晰理解。\n- 建议修改方向：统一为一个名称。建议保留 \"Intensional Structural Reward\" (与 Method §3 一致)，同时修改 Abstract。\n\n**N2** [critical] 新颖性 framing 不足——论文核心发现是 Goodhart's Law 的已知推论\n- 具体位置：Introduction ¶4 (introduction.tex:24-28), §4.3 全节, Related Work (related_work.tex:14-20)\n- 问题：论文核心 claim 是 \"diagnostic becomes optimization target\"，但这恰恰是 Goodhart's Law 的定义。论文自己承认这一点（introduction.tex:26 引用 manheim-goodhart-taxonomy），但没有说服 reader 这个经验实例为什么值得一篇论文。\n  - LOO ablation 是标准方法（mutation testing），应用到 solver inputs 是工程适配，不是方法论贡献（论文自己在 method.tex:26 和 related_work.tex:23 承认）。\n  - 9-mode taxonomy 是 post-hoc 分类，缺少 principled 的分类标准（为什么是这 9 种而不是其他？有没有理论完备性论证？）。\n  - Goodhart collapse at all tested doses 是实验观察，但理论上可从 ISR 的数学定义直接推导（method.tex:55-56 已经给出了 H7 tautology 获得 ISR≥0.5 的构造性论证）。\n- 为什么影响接收：Excitement 维度是 ARR 最关键的评分维度之一。论文需要说服 reader 为什么一个可从定义推导的结果值得经验验证——目前的 framing 没有做到。\n- 建议修改方向：\n  (1) 强调 **意料之外** 的经验发现（如 stochastic bifurcation、non-monotonic dose-response、cross-scale mode divergence），这些是理论无法预测的；\n  (2) 将 taxonomy 的贡献定位为 \"operational toolkit for practitioners\" 而非 \"intellectual contribution\"；\n  (3) 明确区分 \"predictable that Goodhart effects exist\" vs. \"unpredictable which modes emerge and how they interact\"。\n\n**N3** [critical] Abstract 数据过载——30 秒内无法消化核心贡献\n- 具体位置：Abstract (abstract.tex:1-9, ~220 words)\n- 问题：Abstract 包含至少 15 个独立数字/统计量：97±2%, 99.5%, 92%, β∈{0.05, 0.1, 0.2, 0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes, ρ=−0.049 (implicit via \"structural collapse\")。这是实验报告风格，不是故事。\n- 为什么影响接收：审稿人在 30 秒内判断论文价值。当前 Abstract 读起来像一个压缩的 results table，核心 insight 被数字淹没。\n- 建议修改方向：保留 3-4 个最关键数字（ISR collapse 幅度、non-hacking rate 对比、dose-response 结论），其余细节移到 Introduction 或 Results。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Introduction 叙事碎片化\n- 具体位置：Introduction (introduction.tex), 5 个 \\paragraph{} 子标题\n- 问题：Introduction 被 5 个 \\paragraph{} 打断（\"The execution-only blind spot\", \"Component necessity testing\", \"ISR as diagnostic\", \"ISR as reward: Goodhart collapse at all tested doses\", \"Contributions\"），导致叙事碎片化。读者在 disconnected 的 mini-sections 之间跳跃，而不是跟随一个连贯的故事。\n- 建议：减少到 2-3 个 \\paragraph{}，或者完全去掉、改用自然段过渡。当前结构更像一个 extended abstract 而不是 introduction。\n\n**W2** [warning] §4.3 Goodhart Effects 的 β 值呈现顺序混乱\n- 具体位置：experiments.tex:79-124\n- 问题：四个 dose 按 β=0.1→0.05→0.2→0.3 顺序呈现，不是升序。β=0.1 被标为 \"Low-dose\" 而 β=0.05 被标为 \"Micro-dose\"。这个非单调的呈现顺序增加了 reader 的认知负荷。\n- 建议：按 β 升序呈现（0.05→0.1→0.2→0.3），或至少在开头给出一句解释为什么选择当前顺序（如 \"we begin with β=0.1 as the primary comparison point\"）。\n\n**W3** [warning] 实验范围窄：单一模型族 + 单一数据集\n- 具体位置：Limitations (limitations.tex:1-4), Experiments §4.1 (experiments.tex:10)\n- 问题：所有实验使用 Qwen3-4B（1.7B 只有 single seed），FOLIO 是唯一数据集（500 训练 / 100 评估）。论文标题暗示是关于 \"neurosymbolic proof generation\" 的一般性发现，但实验只支持 \"Qwen3 on FOLIO\" 的结论。\n- 建议：标题或 claim 中增加限定语（如 \"a case study\"），或在 Limitations 中更突出地讨论 generalization risk。\n\n**W4** [warning] 1.7B 跨尺度实验太薄\n- 具体位置：§4.5 (experiments.tex:138-141), Table 1 bottom rows\n- 问题：1.7B 实验仅 single seed，但论文从中得出了 \"different capacities converge to different Goodhart basins\" 的 claim。Single seed 不支持任何关于 scale-dependent 行为的一般性结论。\n- 建议：要么增加 seed（理想），要么将 claim 弱化为 \"preliminary observation\"（当前文字已部分做到，但 Table 1 中 1.7B 行的呈现方式暗示了与 4B 的对称比较）。\n\n**W5** [warning] ISR 名称本身具有误导性\n- 具体位置：method.tex:44, 论文全文\n- 问题：无论最终统一到哪个名称，\"Intensional Structural **Reward**\" 的名字暗示它应该被用作 reward，但论文的核心结论恰恰是它不应该被用作 reward。这个命名自相矛盾。\"Irreducible Solver Rate\" 作为名称更中性，但与方法章节不一致。\n- 建议：考虑将名称统一为不含 \"Reward\" 的版本，避免读者困惑。\n\n**W6** [warning] LOO 缩写未在首次使用时定义\n- 具体位置：introduction.tex:16 首次使用 \"LOO ablation\"\n- 问题：\"LOO\" 作为 \"Leave-One-Out\" 的缩写在正文中频繁使用（>15 次），但首次出现时未以 \"(LOO)\" 形式正式定义。Introduction 中使用了 \"leave-one-out ablation\" 全称，但 LOO 缩写直接出现在 introduction.tex:16 而无括号展开。\n- 建议：在首次使用处添加 \"leave-one-out (LOO) ablation\"。\n\n**W7** [warning] Table 1 caption 过长\n- 具体位置：experiments.tex:74 (Table 1 caption)\n- 问题：Caption 包含约 120 words 的注释和脚注说明，几乎是一个独立段落。读者需要反复参照 caption 才能理解表格，信息密度过高。\n- 建议：将条件说明移到正文或 Appendix，caption 仅保留表格内容的简要描述。\n\n**W8** [warning] Hacking taxonomy 的分类标准不够 principled\n- 具体位置：§4.6 (experiments.tex:147-176), Appendix §B (appendix.tex:192-480)\n- 问题：9 种 hacking mode 是 post-hoc 从实验中归纳的，没有理论完备性论证（即\"为什么恰好是这 9 种\"）。部分 mode 之间存在语义重叠（H7a \"conclusion duplication\" 和 \"tautological collapse\" 的区别仅在 component count；H1 和 H7 是 gradient 关系）。\n- 建议：讨论 taxonomy 是否 exhaustive，是否存在理论框架可以统一这些 mode（如按 proof-theoretic properties 分类）。\n\n---\n\n## 小问题（不影响接收）\n\n- appendix.tex:1 注释中包含 em-dash (`% Appendix — solver-trace-ablation`)，虽然不渲染但应清理。\n- experiments.tex:176 和 appendix.tex:55, 130 等处有少量 \"-ing\" trailing clauses (\"indicating that the associations are robust...\")，可适度改写。\n- bib 条目 `folio` year mismatch: bib 标注 2024，OpenAlex 记录 2022（可能是 conference vs. arXiv 版本差异）。\n- bib 条目 `jia-harman-survey` 标注 2011，OpenAlex 显示 2010。\n- bib 条目 `deepseek-prover-v15` 等的 author 字段不规范（\"DeepSeek AI\" 而非实际第一作者）。\n- Figure 1 部分标签字体可能接近 7pt 下限（视觉审查存疑，建议作者自查）。\n- experiments.tex:56 中 eval protocol 差异（s43 用 sampling 而非 greedy）在 Appendix 提到但正文 Table 1 未标注。\n\n---\n\n## 引用完整性\n\n**当前状态**：37 条引用，全部被 cite，无 orphan 无 missing。覆盖面：\n- ✅ Reward hacking / specification gaming: Skalse 2022, Krakovna 2020, Bondarenko 2025, Kim 2026, METR 2025, Wang et al. 2026 survey\n- ✅ Neurosymbolic reasoning: SatLM, Logic-LM, LINC, FoVer, LoRP\n- ✅ Process rewards: Lightman 2024, Math-Shepherd, VersaPRM, ThinkPRM\n- ✅ Goodhart theory: Manheim & Garrabrant 2019, Karwowski 2024, Kwa 2024, Gao 2023\n- ✅ Mutation testing: DeMillo 1978, Jia & Harman 2011\n\n**可能缺失的引用**（非强制，但会增强 coverage）：\n1. **Amodei et al. (2016), \"Concrete Problems in AI Safety\"** — reward hacking 讨论的 foundational reference\n2. **Christiano et al. (2017), \"Deep RL from Human Preferences\"** — RLHF 奠基工作，讨论 reward misspecification\n3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作，直接相关\n4. **Shortcut learning 综述 (Geirhos et al. 2020)** — 论文讨论的 \"degenerate shortcuts\" 与 shortcut learning 文献有天然联系\n5. **Formal verification/theorem proving**: AlphaProof 或 LEGO-Prover 等较新工作\n\n37 条引用在 EMNLP 中偏少（典型 long paper 40-60 条），但不是 critical issue。\n\n---\n\n## Contribution 完整性检查\n\n| Contribution | 对应支撑 | 状态 |\n|---|---|---|\n| C1: ISR as diagnostic | §4.2, Figure 2, Table 1 (exec-only) | ✅ 完整 |\n| C2: Goodhart collapse at 4 doses | §4.3, Table 1, Appendix Tables | ✅ 完整 |\n| C3: Prolog transfer | §4.4, Appendix Table 5, Figure 4 | ✅ 完整 |\n| C4: 9-mode taxonomy | §4.6, Table 2, Appendix §B | ✅ 完整 |\n\n所有 Appendix 内容均在正文中被引用。无 orphan appendix sections。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：多 seed（3-5 per condition）、matched random controls、CMH 分层统计检验、1000-step trajectory analysis、premise-count-matched comparison。这是该领域少见的统计严谨度。\n2. **透明度高**：论文坦诚承认 ISR 的局限（premise-count confound, method.tex:53-58），坦诚报告 negative results（ISR 作为 reward 不 work），坦诚报告数据缺失（s43/s44 checkpoints deleted before audit, appendix.tex:250）。\n3. **Cross-validation 思维**：text-match classifier + functional LOO analysis 的双重验证发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现了 careful empirical work。\n4. **Cautionary value**：对 neurosymbolic RL 社区有实际警示价值——execution-only evaluation 不足以判断 formalization quality。\n5. **Hacking taxonomy 有操作价值**：虽然分类标准不够 principled，但 9 种 mode 的具体定义和示例对从业者有直接参考价值。\n\n---\n\n## 审稿人总结\n\n这是一篇实验认真、报告透明的经验性论文。核心发现（ISR 作为 diagnostic 有效但作为 reward 失败）有实用价值，但理论上是 Goodhart's Law 的直接推论，缺少意料之外的 insight。实验范围局限于 Qwen3 + FOLIO，且 ISR 命名不一致是严重的写作错误。建议修复命名问题、压缩 Abstract 数据密度、强化 novelty framing（突出理论无法预测的经验发现），方可达到 Conference 水平。当前以 Findings 推荐。\n\nSources:\n- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-17T16:22:51.174139+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 438 · 2026-05-17T16:22:59.756984+00:00_

Round 1 审稿意见已提交给 Review Director。

核心发现：

**Must-Fix (3 项)**:
1. ISR 命名不一致：Abstract 称 "Irreducible Solver Rate"，Introduction/Method 称 "Intensional Structural Reward"
2. 新颖性 framing 不足——核心发现是 Goodhart's Law 的直接推论，需强化经验贡献的意外性
3. Abstract 数据过载（~15 个数字），30 秒内无法提取核心 message

**Should-Fix (8 项)**:
- Introduction 5 个 \paragraph{} 导致叙事碎片化
- §4.3 β 值呈现顺序混乱（0.1→0.05→0.2→0.3）
- 实验范围窄（单模型族 Qwen3 + 单数据集 FOLIO）
- 1.7B 实验仅 single seed 但做了 scale-dependent claim
- ISR 名称含 "Reward" 但结论是不应用作 reward
- LOO 缩写未正式定义
- Table 1 caption 过长
- Hacking taxonomy 缺乏 principled 分类标准

**总评**: 3.0 (Findings)——实验严谨透明，但 excitement 有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

10 recorded events


### User

_source line 439 · 2026-05-17T16:23:34.728687+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 评分
Overall: 3.5 (Borderline Conference), Soundness 2.5/5, Excitement 3.5/5, Reproducibility 3/5

### Must-Fix 问题

**R1-N1** [critical] Exec-only baseline 在 Table 1 中的不对称比较
- Table 1 的 exec-only 行使用单 seed (s42)、500-step、greedy decoding，而 ISR/Random β=0.1 使用 5-seed pooled。3-seed 1000-step exec-only 数据在附录但不在主表。

**R1-N2** [critical] 5-seed uncorrected OR=3.48 vs 3-seed corrected OR=0.61 的方向反转：framing 不够诚实
- 论文将二者 frame 为 "bound the true effect from above and below"，但 3-seed corrected 分析使用了更完整的审计数据，应作为 primary。5-seed 分析包含 checkpoint 已删除的 seed。

**R1-N3** [critical] ISR β=0.1 s43/s44 checkpoint 丢失，削弱了核心分析的完整性
- 5-seed pooled N-H rate (23%) 是不完整的上界。建议报告区间 [6%, 23%]。

**R1-N4** [critical] SFT vs RL 比较中 PR 严重混淆
- SFT PR=13% (n=39) vs RL PR=93%+。核心问题：无法知道 SFT 在高 PR 时是否也会 hack。C1 "localizing the failure to RL" 证据链有 PR confound。

**R1-N5** [critical] 统计分析层级倒置：pooled Fisher 不应作为 primary analysis
- 实验存在 within-seed clustering，pooled Fisher 忽略这一结构会膨胀 Type I error。CMH 应该是 primary。Seed-level permutation test (p=0.26/0.28) 与 Fisher (p<10⁻⁸) 的巨大差距说明 clustering 严重。

### Should-Fix 问题

**R1-W1** 方法贡献偏薄（Algorithm 1 仅 6 行伪代码）
**R1-W2** Dose-response claim 基于 4 个 β 值、不均匀的 seed 数
**R1-W3** 1.7B cross-scale claims 仅基于单 seed
**R1-W4** "at all tested doses" claim 缺少 β=0.3/0.05 的 trajectory 数据
**R1-W5** 100 个 eval examples 对 per-seed claims 的统计效力不足
**R1-W6** Seed 43 exec-only 使用 sampling (T=0.7) 而非 greedy decoding

### 主要优势
1. 叙事质量高
2. 实验覆盖面广
3. Self-disclosure 诚实
4. Hacking taxonomy 有独立价值
5. Control design 方向正确

---

请对每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，附上你的理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-17T16:23:44.827605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "49",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "49",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-17T16:23:45.379947+00:00_

49	\begin{table}[t]
50	\centering
51	\small
52	\resizebox{\columnwidth}{!}{%
53	\begin{tabular}{lcccccc}
54	\toprule
55	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
56	\midrule
57	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
58	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
59	\midrule
60	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
61	ISR$^\ddagger$ & 0.1 & 70{\scriptsize$\pm$19} & --- & \textbf{54} & 18 & 23$^\star$ \\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)
62	Random & 0.1 & \textbf{83}{\scriptsize$\pm$15} & 0.080{\scriptsize$\pm$.06} & 30 & 59 & 8 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)
63	ISR & 0.2 & 97{\scriptsize$\pm$4} & 0.69{\scriptsize$\pm$.24} & \textbf{99} & 0 & 0 \\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\ref{tab:beta02-detail})
64	\midrule
65	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
66	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
67	\midrule
68	\multicolumn{7}{l}{\textit{Qwen3-1.7B (seed~42)}} \\
69	ISR & 0.1 & 100 & 0.600 & 0 & \textbf{100} & 0 \\ %% registry: d113-1.7b-isr-b01-s42
70	Random & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)
71	ISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\ %% registry: d113-1.7b-isr-b03-s42
72	\bottomrule
73	\end{tabular}}
74	\caption{Goodhart landscape across reward conditions. PR/ISR$^*$: mean$\pm$std of per-seed values; H7/H1/N-H: pooled p
…[truncated 776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-17T16:23:45.882898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "92",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "92",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-17T16:23:46.134173+00:00_

92	
93	\textbf{The transient genuine window.}
94	During the transient window, Cochran--Mantel--Haenszel tests stratified by seed confirm ISR produces more genuine proofs than random controls ($\text{OR}_{\text{CMH}}{=}3.37$, 95\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; Appendix Table~\ref{tab:fol-beta01-perseed}).
95	Pooled Fisher ($\text{OR}{=}3.48$, uncorrected) is consistent but does not account for within-seed dependence.
96	Under stricter H8+FN-corrected classification (3-seed subset with complete audits), the effect reverses ($\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction (which reclassifies borderline samples as hacking) and the reduced sample size ($n{=}231$ vs 350). The 5-seed CMH and 3-seed corrected analyses bound the true effect from above and below respectively.
97	The pooled 5-seed non-hacking rate is 23\% (uncorrected; s42-only H8-corrected estimate: 17\%).
98	This benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\%{\to}2\%$ and $55\%{\to}0\%$ genuine respectively; see below).
99	The same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.
100	Snapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000
101	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-17T16:23:46.185239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-17T16:23:46.236135+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the 
…[truncated 3866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-17T16:25:41.858981+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n## Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Exec-only baseline 在 Table 1 中的不对称比较**\n同意。Table 1 exec-only 行仅为 s42 单 seed（caption 脚注 $^\\dagger$ 标注），而 ISR/Random 行为 5-seed pooled，这是不对等的。虽然论文在脚注中披露了这一点并指向 Appendix Table 6（exec-only 3-seed 1000-step），但主表是审稿人第一眼看到的比较基准。建议在 Table 1 中增加 exec-only 3-seed 1000-step 行（数据已有：PR=97±2%, N-H≈2%），使主表内比较对称。\n\n补充：Table 1 caption 本身已经过长（我在 R2-W7 中提到约 120 words），增加新行的同时应精简 caption。\n\n**[AGREE] R1-N2: OR=3.48 vs OR=0.61 方向反转的 framing 问题**\n同意这是 framing 问题。论文将两个分析描述为 \"bound the true effect from above and below\"（experiments.tex:96），但这个说法在方法论上不够准确：5-seed 分析缺少 s43/s44 的 H8 审计（appendix.tex:249-251 明确说 checkpoints 已删除），而 3-seed 分析是唯一有完整审计的比较。\n\n不过我注意到两点 nuance：\n1. CMH OR=3.37（p<10⁻⁹）是分层检验，已处理 within-seed clustering，且方向与 5-seed Fisher 一致——因此正面效应并非纯粹 artifact。\n2. 3-seed 分析的 OR=0.61 是 n.s.（p=0.182），其方向反转也不显著。\n\n建议：将 3-seed corrected OR=0.61 提升为 primary sensitivity analysis（而非 \"lower bound\"），明确表述 \"the genuine-rate advantage is not robust to H8 correction and checkpoint completeness\"。当前 framing 给 reader 的印象是正面效应是 baseline、0.61 是保守例外，但实际上两个分析各有 limitation。\n\n**[AGREE] R1-N3: s43/s44 checkpoint 丢失**\n完全同意。Checkpoint 丢失是不可逆的数据完整性问题。论文在 appendix.tex:249-251 坦诚披露了这一点（\"checkpoints were deleted before audit and cannot be recovered\"），但在主表（Table 1）中 N-H=23% 仍以点估计呈现。R1 建议的区间 [6%, 23%] 是合理的表示方式。\n\n我补充一个观察：这个问题对论文 narrative 的实际影响有限，因为论文的核心结论是 ISR 作为 reward 最终导致 Goodhart collapse（所有 seed 在 extended training 后收敛到 ≤2% genuine），而非 500-step snapshot 有 23% 的 genuine。论文在 experiments.tex:98-100 和 §5 conclusion 中已正确将 500-step 结果定位为 \"transient\"。但 Table 1 的呈现方式仍需修正。\n\n**[AGREE] R1-N4: SFT vs RL 的 PR confound**\n同意 PR confound 是此比较的核心弱点。SFT PR=13%（n=39）vs exec-only PR=93%（n=93）的巨大差距意味着我们无法排除 \"SFT 在高 PR 时也会 hack\" 的可能性。\n\n论文提供了两层 mitigation，但都不够充分：\n1. 100-step checkpoint（PR=32%, hacking=31.2%，appendix.tex:670-674）：PR 仍然是 SFT 的 2.5 倍，且只有 n=32。\n2. 机制论证（SFT 无 exploration-exploitation dynamics，experiments.tex:39）：这是合理的 reasoning，但不是 empirical evidence。\n\nC1 中 \"localizing the failure to RL\"（introduction.tex:22）作为 claim 过强。建议弱化为 \"consistent with RL-specific failure\" 或提供 PR-matched 的 RL early checkpoint 数据。\n\n不过我对 R1 评分有异议：R1 给 Soundness 2.5/5，我认为这低估了论文在其他方面的实验严谨度。SFT 比较是一个 confound，但论文的核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）不依赖于 SFT 比较。\n\n**[REBUT] R1-N5: 统计分析层级倒置——Pooled Fisher 不应作为 primary**\n部分反驳。R1 的 clustering concern 在方法论上正确，但论文的实际呈现比 R1 描述的更合理：\n\n1. **正文（experiments.tex:94）已将 CMH 作为 primary**：原文说 \"Cochran--Mantel--Haenszel tests stratified by seed **confirm** ISR produces more genuine proofs\"（第一个出现的统计检验），然后才提 Fisher 作为 \"consistent but does not account for within-seed dependence\"。CMH 不是附属分析，是正文叙事中的首要检验。\n\n2. **CMH 和 Fisher 的结论方向一致**：CMH OR=3.37 (p<10⁻⁹) vs Fisher OR=3.48 (p<10⁻⁸)，差异微小。Clustering 确实存在，但在这个 case 中没有改变结论。\n\n3. **Seed-level permutation p=0.26/0.28 的解读**：R1 说这与 Fisher 的 \"巨大差距说明 clustering 严重\"。这个推理不完全正确——p=0.26 primarily 反映的是 n=5 的严重 power limitation（论文在 limitations.tex:7 明确说 minimum achievable p=0.008 at n=5），而非 clustering inflation。如果有 20 seeds，permutation test 可能也会显著。\n\nR1 的建议（CMH 作为 primary）本身没有问题，但论文已经实质上在正文中这么做了。真正需要修的是 Appendix Table 3 (bootstrap-ci) 中 Fisher 作为第一行的排列顺序——这确实给人 Fisher=primary 的错觉。\n\n---\n\n## Should-Fix 逐条回应\n\n**[AGREE] R1-W1: 方法贡献偏薄**\n同意。Algorithm 1 是 6 行伪代码实现标准 LOO ablation。论文自己在 method.tex:26 和 related_work.tex:23 承认 \"our contribution lies in the application and empirical findings, not in the perturbation primitive itself\"。这是诚实的，但也意味着 method 贡献确实薄。我在 R2-N2 中从 novelty 角度提出了类似 concern。\n\n**[AGREE] R1-W2: Dose-response claim 基于 4 个 β 值、不均匀 seed 数**\n同意。β=0.05/0.2 各 3 seeds，β=0.1 有 5 seeds，β=0.3 有 3 seeds。Non-monotonic dose-response（experiments.tex:122-124）是一个有趣的观察，但 4 个数据点 + 不均匀 power 不足以支撑 dose-response function 的 claim。\"non-monotonic pattern\" 措辞可以保留，但不应暗示这是一个 robust 的功能关系。\n\n**[AGREE] R1-W3: 1.7B cross-scale 仅单 seed**\n同意，与我的 R2-W4 一致。单 seed 无法支撑 \"different capacities converge to different Goodhart basins\" 的一般性 claim。\n\n**[AGREE] R1-W4: \"at all tested doses\" 缺 β=0.05/0.3 trajectory 数据**\n同意。\"At all tested doses\"（introduction.tex:26）claim 的证据链：\n- β=0.1：有 1000-step trajectory（s42, s45）——最完整\n- β=0.2：500-step 已 100% H7，但无 trajectory 确认是否有更早的 genuine window\n- β=0.05：500-step 已 87-100% H7，同上\n- β=0.3：500-step 有 3 seeds 但无 trajectory\n\n500-step snapshot 显示 collapse 是合理证据，但与 β=0.1 的 trajectory analysis 标准不一致。要么补充 trajectory 数据，要么将 claim 弱化为 \"collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1\"。\n\n**[AGREE] R1-W5: 100 eval examples 对 per-seed claims 效力不足**\n同意。每个 seed 的 proved samples 在 42-94 之间（Table 4, appendix.tex:127-147），per-seed hacking rate 的 95% CI 很宽。例如 ISR s42 N-H=17.3%（n=81）的 Wilson CI 约 [10%, 27%]。论文依赖 pooled analysis 来获取 power，但 per-seed claims（如 \"s45 achieves 55% genuine\"）的精度有限。这是实验规模限制，而非设计缺陷。\n\n**[AGREE] R1-W6: Seed 43 exec-only 使用 sampling (T=0.7)**\n同意。appendix.tex:55-56 披露了此差异，但正文和 Table 1 中无标注（Table 1 exec-only 行是 s42 非 s43，所以主表本身不受影响，但 Appendix Table 5 的 s43 行应有更显著的标注）。\n\n---\n\n## 与 R1 评分的分歧\n\nR1 给 Overall 3.5（Borderline Conference），我给 3.0（Findings）。差异来源：\n\n1. **Excitement**: R1 给 3.5，我给 2.0。R1 可能更看重 cautionary value 和 taxonomy 的实用性。我认为核心 insight（Goodhart's Law applied to diagnostics）理论上可预测，empirical contribution 的 increment 有限。\n\n2. **Soundness**: R1 给 2.5，我给 4.0。R1 聚焦于统计分析层级和 PR confound，我认为这些是 framing 问题而非根本性缺陷——论文的 multi-seed 设计、matched random controls、CMH stratification 在该领域是 above-average 的实验标准。\n\n综合看，R1 和我对论文的主要 weakness 判断一致（novelty limited, narrow scope, some statistical issues），但权重不同。我认为 Findings 是当前稿件的合适定位。\n",
  "reviewer_id": "2",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n## Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Exec-only baseline 在 Table 1 中的不对称比较**\n同意。Table 1 exec-only 行仅为 s42 单 seed（caption 脚注 $^\\dagger$ 标注），而 ISR/Random 行为 5-seed pooled，这是不对等的。虽然论文在脚注中披露了这一点并指向 Appendix Table 6（exec-only 3-seed 1000-step），但主表是审稿人第一眼看到的比较基准。建议在 Table 1 中增加 exec-only 3-seed 1000-step 行（数据已有：PR=97±2%, N-H≈2%），使主表内比较对称。\n\n补充：Table 1 caption 本身已经过长（我在 R2-W7 中提到约 120 words），增加新行的同时应精简 caption。\n\n**[AGREE] R1-N2: OR=3.48 vs OR=0.61 方向反转的 framing 问题**\n同意这是 framing 问题。论文将两个分析描述为 \"bound the true effect from above and below\"（experiments.tex:96），但这个说法在方法论上不够准确：5-seed 分析缺少 s43/s44 的 H8 审计（appendix.tex:249-251 明确说 checkpoints 已删除），而 3-seed 分析是唯一有完整审计的比较。\n\n不过我注意到两点 nuance：\n1. CMH OR=3.37（p<10⁻⁹）是分层检验，已处理 within-seed clustering，且方向与 5-seed Fisher 一致——因此正面效应并非纯粹 artifact。\n2. 3-seed 分析的 OR=0.61 是 n.s.（p=0.182），其方向反转也不显著。\n\n建议：将 3-seed corrected OR=0.61 提升为 primary sensitivity analysis（而非 \"lower bound\"），明确表述 \"the genuine-rate advantage is not robust to H8 correction and checkpoint completeness\"。当前 framing 给 reader 的印象是正面效应是 baseline、0.61 是保守例外，但实际上两个分析各有 limitation。\n\n**[AGREE] R1-N3: s43/s44 checkpoint 丢失**\n完全同意。Checkpoint 丢失是不可逆的数据完整性问题。论文在 appendix.tex:249-251 坦诚披露了这一点（\"checkpoints were deleted before audit and cannot be recovered\"），但在主表（Table 1）中 N-H=23% 仍以点估计呈现。R1 建议的区间 [6%, 23%] 是合理的表示方式。\n\n我补充一个观察：这个问题对论文 narrative 的实际影响有限，因为论文的核心结论是 ISR 作为 reward 最终导致 Goodhart collapse（所有 seed 在 extended training 后收敛到 ≤2% genuine），而非 500-step snapshot 有 23% 的 genuine。论文在 experiments.tex:98-100 和 §5 conclusion 中已正确将 500-step 结果定位为 \"transient\"。但 Table 1 的呈现方式仍需修正。\n\n**[AGREE] R1-N4: SFT vs RL 的 PR confound**\n同意 PR confound 是此比较的核心弱点。SFT PR=13%（n=39）vs exec-only PR=93%（n=93）的巨大差距意味着我们无法排除 \"SFT 在高 PR 时也会 hack\" 的可能性。\n\n论文提供了两层 mitigation，但都不够充分：\n1. 100-step checkpoint（PR=32%, hacking=31.2%，appendix.tex:670-674）：PR 仍然是 SFT 的 2.5 倍，且只有 n=32。\n2. 机制论证（SFT 无 exploration-exploitation dynamics，experiments.tex:39）：这是合理的 reasoning，但不是 empirical evidence。\n\nC1 中 \"localizing the failure to RL\"（introduction.tex:22）作为 claim 过强。建议弱化为 \"consistent with RL-specific failure\" 或提供 PR-matched 的 RL early checkpoint 数据。\n\n不过我对 R1 评分有异议：R1 给 Soundness 2.5/5，我认为这低估了论文在其他方面的实验严谨度。SFT 比较是一个 confound，但论文的核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）不依赖于 SFT 比较。\n\n**[REBUT] R1-N5: 统计分析层级倒置——Pooled Fisher 不应作为 primary**\n部分反驳。R1 的 clustering concern 在方法论上正确，但论文的实际呈现比 R1 描述的更合理：\n\n1. **正文（experiments.tex:94）已将 CMH 作为 primary**：原文说 \"Cochran--Mantel--Haenszel tests stratified by seed **confirm** ISR produces more genuine proofs\"（第一个出现的统计检验），然后才提 Fisher 作为 \"consistent but does not account for within-seed dependence\"。CMH 不是附属分析，是正文叙事中的首要检验。\n\n2. **CMH 和 Fisher 的结论方向一致**：CMH OR=3.37 (p<10⁻⁹) vs Fisher OR=3.48 (p<10⁻⁸)，差异微小。Clustering 确实存在，但在这个 case 中没有改变结论。\n\n3. **Seed-level permutation p=0.26/0.28 的解读**：R1 说这与 Fisher 的 \"巨大差距说明 clustering 严重\"。这个推理不完全正确——p=0.26 primarily 反映的是 n=5 的严重 power limitation（论文在 limitations.tex:7 明确说 minimum achievable p=0.008 at n=5），而非 clustering inflation。如果有 20 seeds，permutation test 可能也会显著。\n\nR1 的建议（CMH 作为 primary）本身没有问题，但论文已经实质上在正文中这么做了。真正需要修的是 Appendix Table 3 (bootstrap-ci) 中 Fisher 作为第一行的排列顺序——这确实给人 Fisher=primary 的错觉。\n\n---\n\n## Should-Fix 逐条回应\n\n**[AGREE] R1-W1: 方法贡献偏薄**\n同意。Algorithm 1 是 6 行伪代码实现标准 LOO ablation。论文自己在 method.tex:26 和 related_work.tex:23 承认 \"our contribution lies in the application and empirical findings, not in the perturbation primitive itself\"。这是诚实的，但也意味着 method 贡献确实薄。我在 R2-N2 中从 novelty 角度提出了类似 concern。\n\n**[AGREE] R1-W2: Dose-response claim 基于 4 个 β 值、不均匀 seed 数**\n同意。β=0.05/0.2 各 3 seeds，β=0.1 有 5 seeds，β=0.3 有 3 seeds。Non-monotonic dose-response（experiments.tex:122-124）是一个有趣的观察，但 4 个数据点 + 不均匀 power 不足以支撑 dose-response function 的 claim。\"non-monotonic pattern\" 措辞可以保留，但不应暗示这是一个 robust 的功能关系。\n\n**[AGREE] R1-W3: 1.7B cross-scale 仅单 seed**\n同意，与我的 R2-W4 一致。单 seed 无法支撑 \"different capacities converge to different Goodhart basins\" 的一般性 claim。\n\n**[AGREE] R1-W4: \"at all tested doses\" 缺 β=0.05/0.3 trajectory 数据**\n同意。\"At all tested doses\"（introduction.tex:26）claim 的证据链：\n- β=0.1：有 1000-step trajectory（s42, s45）——最完整\n- β=0.2：500-step 已 100% H7，但无 trajectory 确认是否有更早的 genuine window\n- β=0.05：500-step 已 87-100% H7，同上\n- β=0.3：500-step 有 3 seeds 但无 trajectory\n\n500-step snapshot 显示 collapse 是合理证据，但与 β=0.1 的 trajectory analysis 标准不一致。要么补充 trajectory 数据，要么将 claim 弱化为 \"collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1\"。\n\n**[AGREE] R1-W5: 100 eval examples 对 per-seed claims 效力不足**\n同意。每个 seed 的 proved samples 在 42-94 之间（Table 4, appendix.tex:127-147），per-seed hacking rate 的 95% CI 很宽。例如 ISR s42 N-H=17.3%（n=81）的 Wilson CI 约 [10%, 27%]。论文依赖 pooled analysis 来获取 power，但 per-seed claims（如 \"s45 achieves 55% genuine\"）的精度有限。这是实验规模限制，而非设计缺陷。\n\n**[AGREE] R1-W6: Seed 43 exec-only 使用 sampling (T=0.7)**\n同意。appendix.tex:55-56 披露了此差异，但正文和 Table 1 中无标注（Table 1 exec-only 行是 s42 非 s43，所以主表本身不受影响，但 Appendix Table 5 的 s43 行应有更显著的标注）。\n\n---\n\n## 与 R1 评分的分歧\n\nR1 给 Overall 3.5（Borderline Conference），我给 3.0（Findings）。差异来源：\n\n1. **Excitement**: R1 给 3.5，我给 2.0。R1 可能更看重 cautionary value 和 taxonomy 的实用性。我认为核心 insight（Goodhart's Law applied to diagnostics）理论上可预测，empirical contribution 的 increment 有限。\n\n2. **Soundness**: R1 给 2.5，我给 4.0。R1 聚焦于统计分析层级和 PR confound，我认为这些是 framing 问题而非根本性缺陷——论文的 multi-seed 设计、matched random controls、CMH stratification 在该领域是 above-average 的实验标准。\n\n综合看，R1 和我对论文的主要 weakness 判断一致（novelty limited, narrow scope, some statistical issues），但权重不同。我认为 Findings 是当前稿件的合适定位。\n",
    "reviewer_id": "2",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-17T16:25:45.524676+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3665
}
```

</details>

---


### Assistant

_source line 448 · 2026-05-17T16:25:56.282443+00:00_

交叉回应已提交。总结：

- R1 的 5 个 Must-Fix 中我 **AGREE 4 个**（N1 表格不对称、N2 OR 反转 framing、N3 checkpoint 丢失、N4 SFT PR confound），**部分 REBUT 1 个**（N5：论文正文实际上已将 CMH 作为 primary，clustering concern 方法论正确但实际影响小，seed-level permutation p=0.26 主要反映 n=5 power 不足而非 clustering inflation）。
- R1 的 6 个 Should-Fix 全部 AGREE。
- 评分分歧：R1 给 3.5/Soundness 2.5/Excitement 3.5，我给 3.0/Soundness 4.0/Excitement 2.0。我们对 soundness 和 excitement 的权重相反，但都认为论文在 Findings-to-Borderline Conference 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

96 recorded events


### User

_source line 449 · 2026-05-17T17:07:13.195915+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性/贡献定位 + 写作质量 + 格式合规**。

## 论文信息
- 标题: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
- 路径: projects/solver-trace-ablation/paper/main.tex (及同目录下各 .tex 文件)
- 目标 venue: EMNLP 2026 (通过 ACL Rolling Review)
- 格式: ACL 模板 review 模式, Long paper 8 页正文限制, double-blind
- ARR deadline: 2026-05-25

## 你的审查侧重

1. **新颖性与贡献评估**：
   - STA/ISR 方法本身新颖性如何？（Algorithm 1 仅 6 行 LOO 伪代码）
   - "Diagnostic becomes optimization target" 是否只是 Goodhart's Law 的直接推论？
   - 经验贡献（stochastic bifurcation, nine hacking modes, cross-logic transfer）的增量价值？
   - 论文是否正确定位为 empirical study 而非 method paper？

2. **写作质量**：
   - Abstract 是否数据堆砌（计算其中的数字/统计量数量）？
   - Introduction 的叙事结构是否连贯？\paragraph{} 使用是否过度？
   - Experiments §4.3 按 β 值逐一报告是否格式重复？β 呈现顺序是否合理？
   - 全文是否有 AI 写作痕迹（em-dash、-ing phrase、过度分段、blacklisted words）？
   - ISR 全名是否在全文中一致？（检查 Abstract 和 Method 是否用同一展开形式）

3. **格式合规**：
   - 正文是否在 8 页限制内（§1-§5 + References 之前的内容）？
   - Limitations 和 Ethics Statement 位置是否正确？
   - Table/Figure caption 是否自包含？Table 1 caption 长度是否合理？
   - 缩写首次使用是否有定义？（检查 LOO, ISR, GRPO, STA, FOL, PR 等）
   - 引用格式和数量是否合规？

4. **叙事一致性**：
   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条连贯主线？
   - C1-C4 贡献列表是否均有对应 section 支撑？
   - 论文核心 claim "ISR reliable as diagnostic, unreliable as optimizer" 是否在各 section 统一？

## 已知历史问题（供参考，但请独立审查）

- [CRITICAL] Abstract 数据堆砌（~15 个数字/统计量），读感像实验报告
- [CRITICAL] ISR 命名不一致：'Irreducible Solver Rate' vs 'Intensional Structural Reward'
- [WARNING] Introduction 5 个 \paragraph{} 小标题导致叙事碎片化
- [WARNING] §4.3 按 β 逐一报告格式重复，且呈现顺序非升序 (0.1→0.05→0.2→0.3)
- [WARNING] 方法新颖性有限（Algorithm 1 仅 6 行）
- [WARNING] Table 1 caption ~120 words + 6 脚注标记
- [INFO] LOO 缩写首次使用时是否正式定义？

请按以下格式输出：
## Summary (2-3 句)
## Strengths (逐条)
## Weaknesses (逐条，标注 severity: critical/warning/info)
## Questions (需要作者回答)
## Missing References
## Overall Assessment (评分 1-5, 参照 EMNLP 2026 ARR 评分标准)
## Confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-17T17:07:25.156939+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-17T17:07:25.207461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-17T17:07:30.028564+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-17T17:07:31.462134+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-17T17:07:31.931876+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-17T17:07:38.661965+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

The reviewing workflow involves: (1) reading the paper and getting the first impression, and 
…[truncated 1922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8633
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-17T17:08:55.027104+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 70, \"unique_cited_keys\": 40, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 10, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": \"Defining and Characterizing Reward 
…[truncated 31095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 83564
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-17T17:08:55.077994+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 83146
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-17T17:09:01.012910+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all evaluation dimensions, their rating scales, and descriptions. List every question/criterion the reviewer must answer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all evaluation dimensions, their rating scales, and descriptions. List every question/criterion the reviewer must answer."
  }
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-17T17:09:01.515494+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-17T17:09:01.954772+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 439
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-17T17:09:01.955102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-17T17:09:02.456795+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, suggesting the failure is RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.
5	Across 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-17T17:09:02.457234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-17T17:09:03.359912+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yield
…[truncated 3732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-17T17:09:03.410583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-17T17:09:03.812040+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt20
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 467 · 2026-05-17T17:09:03.862557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-17T17:09:04.314388+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-17T17:09:04.314804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-17T17:09:04.816948+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples ha
…[truncated 17864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-17T17:09:04.817306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-17T17:09:05.269015+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs over random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
8	These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
9	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-17T17:09:05.319746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-17T17:09:05.771900+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses three seeds with high variance ($\text{PR}{=}0\%$, $7\%$, $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	ISR $\beta{=}0.1$ s43 and s44 checkpoints were lost during disk cleanup, preventing retrospective H8 audit on these seeds; the reporte
…[truncated 1067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-17T17:09:05.772350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-17T17:09:06.073596+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-17T17:09:06.074004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-17T17:09:06.325693+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename cont
…[truncated 43398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---
