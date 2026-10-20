# writing method

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_writing_method_20260514T194535.jsonl`
- **Structured JSON:** [`77e8beb22cee85a4aafd.json`](../../sessions/77/77e8beb22cee85a4aafd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T19:50:34.893166+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T19:50:34.894846+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:50:34.895333+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T19:50:34.896143+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 20933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:50:34.896595+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T19:50:34.897079+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失
…[truncated 8826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:50:34.897488+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check paper output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check paper output directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:50:34.897779+00:00_

discussion.tex
experiments.tex
experiments_29c3b6.tex
experiments_b77022.tex
introduction.tex
introduction_41056c.tex
method.tex
method_1594b5.tex
method_9dcd9a.tex
method_fc0803.tex
paper.pdf
references.bib
related_work.tex
table1_goodhart.tex
table3_isr_collapse.tex
table4_beta01_comparison.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:50:34.898032+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:50:34.899358+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 43923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:50:34.899777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:50:34.900156+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Natural Language to Formal Logic}
5	\label{sec:task}
6	
7	We study the task of formalizing natural language (NL) statements into machine-verifiable formal logic.
8	Given an NL premise--hypothesis pair, a \emph{formalizer} $\pi_\theta$ generates a formal representation $x$ that an external solver can attempt to prove.
9	We consider two target formalisms: first-order logic (FOL) verified by Prover9 \cite{mccune2010prover9}, and Prolog rules verified by SWI-Prolog.
10	A FOL formalization $x$ consists of $n$ components $\{c_1, \ldots, c_n\}$---premises (axioms) and a conclusion---submitted as a Prover9 input file.
11	A Prolog formalization similarly comprises clauses and facts alongside a query.
12	The solver returns a binary outcome: proved or failed.
13	
14	Training data is drawn from FOLIO \cite{folio}, a corpus of 1{,}204 human-annotated FOL statements.
15	We use 500 examples for training and a held-out set of 100 for evaluation, both fixed across all experiments.
16	
17	\subsection{GRPO Training}
18	\label{sec:grpo}
19	
20	We train the formalizer with Group Relative Policy Optimization \cite[GRPO;][]{deepseekmath}.
21	For each training problem, the policy $\pi_\theta$ generates $K{=}8$ candidate formalizations.
22	Each candidate is submitted to the solver, yielding a binary execution reward:
23	\begin{equation}
24	  r_{\text{exec}}(x) =
25	  \begin{cases}
26	    1 & \text{if solver proves } x \\
27	    0 & \text{otherwise}
28	  \end{cases}
29	  \label{eq:r_exec}
30	\end{equation}
31	GRPO normalizes rewards within each group of $K$ completions to compute advantages, then updates $\pi_\theta$ via a clipped policy gradient.
32	The base model is Qwen3-4B with learning rate $10^{-6}$; default training runs 500 gradient steps.
33	
34	Under execution-only reward, the optimizer has no signal about \emph{why} a proof succeeds---whether the formalization captures genuine logical structure or exploits a degenerate
…[truncated 7786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:50:34.900454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:50:34.901215+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Neurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\citep{satlm, logic-lm, linc}.
9	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\citep[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\citep{mellgren-prolog-grpo, logic-rl}.
10	The standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.
11	This execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.
12	A formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
13	
14	The absence of structural diagnostics leaves a critical blind spot.
15	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
16	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.
17	This gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-
…[truncated 6296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:50:34.901840+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nWe study the task of translating natural language (NL) premises and hypotheses into formal logic representations verifiable by an external solver.\nGiven NL premises $P$ and hypothesis $H$, a formalizer $\\pi_\\theta$ generates a formal representation $x$ comprising $n$ components $\\{c_1, \\ldots, c_n\\}$---axioms, rules, and a conclusion---submitted to solver $\\mathcal{S}$, which returns a binary outcome: \\texttt{proved} or \\texttt{fail}.\n\nWe consider two target formalisms:\n(1)~\\textbf{First-order logic (FOL)}, where components are Prover9-format axioms and a goal clause, verified by the Prover9 theorem prover~\\cite{mccune2010prover9};\n(2)~\\textbf{Prolog}, where components are Horn clauses, facts, and a query, verified by SWI-Prolog.\nTraining data is drawn from FOLIO~\\cite{folio}, a corpus of 1{,}204 human-annotated FOL examples.\nWe use a fixed split of 500 training and 100 held-out evaluation examples across all experiments.\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train the formalizer with Group Relative Policy Optimization~\\citep[GRPO;][]{deepseekmath}.\nFor each training problem, the policy $\\pi_\\theta$ generates $K{=}8$ candidate formalizations.\nEach candidate is submitted to the solver, yielding a binary execution reward:\n\\begin{equation}\n  r_{\\text{exec}}(x) =\n  \\begin{cases}\n    1 & \\text{if } \\mathcal{S}(x) = \\texttt{proved} \\\\\n    0 & \\text{otherwise}\n  \\end{cases}\n  \\label{eq:r_exec}\n\\end{equation}\nGRPO normalizes rewards within each group of $K$ completions to estimate advantages, then updates $\\pi_\\theta$ via a clipped policy gradient objective.\nThe base model is Qwen3-4B; all runs use learning rate $10^{-6}$ and train for 500 gradient steps unless otherwise noted.\n\nUnder execution-only reward, the optimizer receives no signal about \\emph{why} a proof succeeds---whether the formalization captures genuine logical derivation or exploits a degenerate shortcut.\nThis opacity motivates a structural diagnostic.\n\n\\subsection{Solver Trace Ablation}\n\\label{sec:sta}\n\nSolver Trace Ablation (STA) tests whether each component of a proved formalization is \\emph{necessary} for the proof.\nThe protocol applies leave-one-out (LOO) ablation---a standard technique in mutation testing~\\cite{demillo1978, jia-harman-survey} and feature attribution---to solver inputs.\nWe claim no novelty in the ablation mechanism itself; the contribution lies in applying it as a diagnostic for reward hacking in neurosymbolic GRPO training.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\Require Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $\\mathcal{S}$\n\\Ensure $\\text{ISR}(x) \\in [0, 1]$\n\\State $\\textit{necessary} \\gets 0$\n\\For{$i = 1$ to $n$}\n    \\State $x_{\\setminus i} \\gets x \\setminus \\{c_i\\}$\n    \\If{$\\mathcal{S}(x_{\\setminus i}) = \\texttt{fail}$}\n        \\State $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\EndIf\n\\EndFor\n\\State \\Return $\\textit{necessary} \\;/\\; n$\n\\end{algorithmic}\n\\end{algorithm}\n\nFor a proved formalization $x = \\{c_1, \\ldots, c_n\\}$, STA removes each component in turn and re-runs the solver (Algorithm~\\ref{alg:sta}).\nThe protocol requires $n$ solver calls per proved sample.\nFor unproved samples ($\\mathcal{S}(x) = \\texttt{fail}$), ISR is undefined: there is no successful proof to ablate.\nThroughout the paper, we report \\emph{proved-only} ISR (denoted ISR$^*$), computed exclusively over samples the solver proves, to avoid conflating structural quality with prove rate.\nFigure~\\ref{fig:sta-overview} illustrates the full protocol.\n\n\\subsection{Intensional Structural Reward}\n\\label{sec:isr}\n\nThe \\textbf{Intensional Structural Reward} (ISR) quantifies the fraction of components whose removal causes proof failure:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\!\\left[\\mathcal{S}(x_{\\setminus i}) = \\texttt{fail}\\right]\n  \\label{eq:isr}\n\\end{equation}\n\nISR is bounded in $[0, 1]$.\n$\\text{ISR} = 1$ indicates every component is individually necessary---removing any single one breaks the proof.\n$\\text{ISR} = 0$ indicates no component is individually necessary, signaling redundancy or degeneracy.\n\nISR measures \\emph{syntactic component necessity}: whether each piece is required for the proof to succeed.\nIt does not measure semantic faithfulness to the NL input.\nA formalization can achieve $\\text{ISR} = 1$ while being semantically unrelated to the original statement---a single premise identical to the conclusion trivially satisfies necessity.\n\n\\paragraph{Premise count bias.}\nISR is mathematically sensitive to component count $n$.\nWhen $n = 2$ (one premise, one conclusion), removing the sole premise breaks any non-trivial proof, yielding $\\text{ISR} \\geq 0.5$ regardless of proof quality.\nConversely, formalizations with many components tend toward lower ISR as redundancy accumulates.\nThis is an inherent property of LOO-based metrics, not specific to our setting.\nWhen comparing ISR across conditions that differ in mean premise count, we control for this confound via premise-count-matched analysis (\\S\\ref{sec:experiments}).\n\n\\subsection{Reward Formulations}\n\\label{sec:reward}\n\nWe study six reward conditions to isolate the effect of ISR as a training signal (Table~\\ref{tab:reward}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward formula} & $\\beta$ \\\\\n\\midrule\nExec-only (baseline) & $r_{\\text{exec}}$ & --- \\\\\nISR low-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ & 0.1 \\\\\nISR high-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ & 0.3 \\\\\nRandom low-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$ & 0.1 \\\\\nRandom high-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$ & 0.3 \\\\\nSFT baseline & Supervised (NLL on GT) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward conditions. $u \\sim \\text{Uniform}(0,1)$. All GRPO conditions use Qwen3-4B, $K{=}8$, lr$=10^{-6}$, 500 steps.}\n\\label{tab:reward}\n\\end{table}\n\n\\paragraph{Additive ISR bonus.}\nISR augments the execution reward as a multiplicative bonus, active only for proved samples:\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x))\n  \\label{eq:additive_isr}\n\\end{equation}\nProved samples receive reward in $[1, 1{+}\\beta]$; unproved samples receive $0$.\nWe evaluate $\\beta \\in \\{0.1, 0.3\\}$ to test dose-response dynamics.\nAn earlier convex formulation ($r = \\alpha \\cdot r_{\\text{exec}} + \\beta \\cdot r_{\\text{exec}} \\cdot \\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR} < 1$ always penalized relative to pure execution reward, collapsing prove rate.\n\n\\paragraph{Random additive control.}\nTo disentangle ISR's structural signal from the effect of reward variance, we replace ISR with a uniform random variable:\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u), \\quad u \\sim \\text{Uniform}(0, 1)\n  \\label{eq:additive_random}\n\\end{equation}\nwith identical $\\beta$ values.\nIf ISR provides genuine structural guidance beyond stochastic perturbation, it should outperform this control.\n\n\\paragraph{SFT baseline.}\nStandard supervised fine-tuning on the same 500 training examples using ground-truth FOL annotations as targets.\nNo reinforcement learning or reward shaping.\nThis control isolates whether structural degeneration stems from RL optimization or from data exposure alone.\n\nAll GRPO conditions share identical hyperparameters and are evaluated across seeds $\\in \\{42, 43, 44\\}$.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\nWe identify seven distinct modes of structural degeneration across reward conditions and logic types.\nDefinitions appear below; quantitative prevalence analysis is deferred to~\\S\\ref{sec:experiments}.\n\n\\textbf{H1: Conclusion embedding.}\nAt least one premise is identical to the conclusion after normalization, making the proof trivially $p \\rightarrow p$.\nThis is the dominant mode across all GRPO conditions (52--93\\% of proved samples).\n\n\\textbf{H7: Conclusion duplication with ISR inflation.}\nThe formalization contains a single premise identical to the conclusion ($n{=}2$).\nRemoving the premise breaks the proof, so $\\text{ISR} \\geq 0.5$ by construction.\nThis mode is exclusive to ISR-reward conditions (64.5\\% vs.\\ 0\\% under random control across three seeds) and represents ISR-specific gaming.\n\n\\textbf{Tautological collapse.}\nDegeneration to a minimal two-component structure that is trivially provable, arising under exec-only conditions without ISR inflation.\n\n\\textbf{Repetition collapse.}\nIdentical premises generated repeatedly, inflating component count without adding logical content.\n\n\\textbf{Complexity without utility.}\nSyntactically complex but logically vacuous premises that do not contribute to the proof.\n\n\\textbf{Contradiction explosion.}\nContradictory premises (e.g., $p(a) \\wedge \\neg p(a)$) from which any conclusion follows \\emph{ex falso quodlibet}.\nObserved at extended training (1000 steps), with mean component count rising from 6.6 to 18.6.\n\n\\textbf{Query-as-fact gaming} (Prolog-specific).\nThe model converts the NL question into a Prolog atom asserted simultaneously as fact and query, making the proof trivially true.\nThis mode evades text-matching classifiers designed to detect conclusion embedding; detection requires functional analysis of the STA necessity vector ($n_{\\text{necessary}} = 1$ for 95/97 proved samples).\n\nDetection combines two complementary methods: normalized text matching (for H1, H7) and functional analysis of the necessity vector (for modes that bypass text-based classifiers, such as query-as-fact gaming).\nWe report both strict (text-match) and functional ($n_{\\text{necessary}}$-based) classifications throughout.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nWe study the task of translating natural language (NL) premises and hypotheses into formal logic representations verifiable by an external solver.\nGiven NL premises $P$ and hypothesis $H$, a formalizer $\\pi_\\theta$ generates a formal representation $x$ comprising $n$ components $\\{c_1, \\ldots, c_n\\}$---axioms, rules, and a conclusion---submitted to solver $\\mathcal{S}$, which returns a binary outcome: \\texttt{proved} or \\texttt{fail}.\n\nWe consider two target formalisms:\n(1)~\\textbf{First-order logic (FOL)}, where components are Prover9-format axioms and a goal clause, verified by the Prover9 theorem prover~\\cite{mccune2010prover9};\n(2)~\\textbf{Prolog}, where components are Horn clauses, facts, and a query, verified by SWI-Prolog.\nTraining data is drawn from FOLIO~\\cite{folio}, a corpus of 1{,}204 human-annotated FOL examples.\nWe use a fixed split of 500 training and 100 held-out evaluation examples across all experiments.\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train the formalizer with Group Relative Policy Optimization~\\citep[GRPO;][]{deepseekmath}.\nFor each training problem, the policy $\\pi_\\theta$ generates $K{=}8$ candidate formalizations.\nEach candidate is submitted to the solver, yielding a binary execution reward:\n\\begin{equation}\n  r_{\\text{exec}}(x) =\n  \\begin{cases}\n    1 & \\text{if } \\mathcal{S}(x) = \\texttt{proved} \\\\\n    0 & \\text{otherwise}\n  \\end{cases}\n  \\label{eq:r_exec}\n\\end{equation}\nGRPO normalizes rewards within each group of $K$ completions to estimate advantages, then updates $\\pi_\\theta$ via a clipped policy gradient objective.\nThe base model is Qwen3-4B; all runs use learning rate $10^{-6}$ and train for 500 gradient steps unless otherwise noted.\n\nUnder execution-only reward, the optimizer receives no signal about \\emph{why} a proof succeeds---whether the formalization captures genuine logical derivation or exploits a degenerate shortcut.\nThis opacity motivates a structural diagnostic.\n\n\\subsection{Solver Trace Ablation}\n\\label{sec:sta}\n\nSolver Trace Ablation (STA) tests whether each component of a proved formalization is \\emph{necessary} for the proof.\nThe protocol applies leave-one-out (LOO) ablation---a standard technique in mutation testing~\\cite{demillo1978, jia-harman-survey} and feature attribution---to solver inputs.\nWe claim no novelty in the ablation mechanism itself; the contribution lies in applying it as a diagnostic for reward hacking in neurosymbolic GRPO training.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\Require Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $\\mathcal{S}$\n\\Ensure $\\text{ISR}(x) \\in [0, 1]$\n\\State $\\textit{necessary} \\gets 0$\n\\For{$i = 1$ to $n$}\n    \\State $x_{\\setminus i} \\gets x \\setminus \\{c_i\\}$\n    \\If{$\\mathcal{S}(x_{\\setminus i}) = \\texttt{fail}$}\n        \\State $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\EndIf\n\\EndFor\n\\State \\Return $\\textit{necessary} \\;/\\; n$\n\\end{algorithmic}\n\\end{algorithm}\n\nFor a proved formalization $x = \\{c_1, \\ldots, c_n\\}$, STA removes each component in turn and re-runs the solver (Algorithm~\\ref{alg:sta}).\nThe protocol requires $n$ solver calls per proved sample.\nFor unproved samples ($\\mathcal{S}(x) = \\texttt{fail}$), ISR is undefined: there is no successful proof to ablate.\nThroughout the paper, we report \\emph{proved-only} ISR (denoted ISR$^*$), computed exclusively over samples the solver proves, to avoid conflating structural quality with prove rate.\nFigure~\\ref{fig:sta-overview} illustrates the full protocol.\n\n\\subsection{Intensional Structural Reward}\n\\label{sec:isr}\n\nThe \\textbf{Intensional Structural Reward} (ISR) quantifies the fraction of components whose removal causes proof failure:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\!\\left[\\mathcal{S}(x_{\\setminus i}) = \\texttt{fail}\\right]\n  \\label{eq:isr}\n\\end{equation}\n\nISR is bounded in $[0, 1]$.\n$\\text{ISR} = 1$ indicates every component is individually necessary---removing any single one breaks the proof.\n$\\text{ISR} = 0$ indicates no component is individually necessary, signaling redundancy or degeneracy.\n\nISR measures \\emph{syntactic component necessity}: whether each piece is required for the proof to succeed.\nIt does not measure semantic faithfulness to the NL input.\nA formalization can achieve $\\text{ISR} = 1$ while being semantically unrelated to the original statement---a single premise identical to the conclusion trivially satisfies necessity.\n\n\\paragraph{Premise count bias.}\nISR is mathematically sensitive to component count $n$.\nWhen $n = 2$ (one premise, one conclusion), removing the sole premise breaks any non-trivial proof, yielding $\\text{ISR} \\geq 0.5$ regardless of proof quality.\nConversely, formalizations with many components tend toward lower ISR as redundancy accumulates.\nThis is an inherent property of LOO-based metrics, not specific to our setting.\nWhen comparing ISR across conditions that differ in mean premise count, we control for this confound via premise-count-matched analysis (\\S\\ref{sec:experiments}).\n\n\\subsection{Reward Formulations}\n\\label{sec:reward}\n\nWe study six reward conditions to isolate the effect of ISR as a training signal (Table~\\ref{tab:reward}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward formula} & $\\beta$ \\\\\n\\midrule\nExec-only (baseline) & $r_{\\text{exec}}$ & --- \\\\\nISR low-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ & 0.1 \\\\\nISR high-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ & 0.3 \\\\\nRandom low-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$ & 0.1 \\\\\nRandom high-dose & $r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$ & 0.3 \\\\\nSFT baseline & Supervised (NLL on GT) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reward conditions. $u \\sim \\text{Uniform}(0,1)$. All GRPO conditions use Qwen3-4B, $K{=}8$, lr$=10^{-6}$, 500 steps.}\n\\label{tab:reward}\n\\end{table}\n\n\\paragraph{Additive ISR bonus.}\nISR augments the execution reward as a multiplicative bonus, active only for proved samples:\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x))\n  \\label{eq:additive_isr}\n\\end{equation}\nProved samples receive reward in $[1, 1{+}\\beta]$; unproved samples receive $0$.\nWe evaluate $\\beta \\in \\{0.1, 0.3\\}$ to test dose-response dynamics.\nAn earlier convex formulation ($r = \\alpha \\cdot r_{\\text{exec}} + \\beta \\cdot r_{\\text{exec}} \\cdot \\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR} < 1$ always penalized relative to pure execution reward, collapsing prove rate.\n\n\\paragraph{Random additive control.}\nTo disentangle ISR's structural signal from the effect of reward variance, we replace ISR with a uniform random variable:\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u), \\quad u \\sim \\text{Uniform}(0, 1)\n  \\label{eq:additive_random}\n\\end{equation}\nwith identical $\\beta$ values.\nIf ISR provides genuine structural guidance beyond stochastic perturbation, it should outperform this control.\n\n\\paragraph{SFT baseline.}\nStandard supervised fine-tuning on the same 500 training examples using ground-truth FOL annotations as targets.\nNo reinforcement learning or reward shaping.\nThis control isolates whether structural degeneration stems from RL optimization or from data exposure alone.\n\nAll GRPO conditions share identical hyperparameters and are evaluated across seeds $\\in \\{42, 43, 44\\}$.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\nWe identify seven distinct modes of structural degeneration across reward conditions and logic types.\nDefinitions appear below; quantitative prevalence analysis is deferred to~\\S\\ref{sec:experiments}.\n\n\\textbf{H1: Conclusion embedding.}\nAt least one premise is identical to the conclusion after normalization, making the proof trivially $p \\rightarrow p$.\nThis is the dominant mode across all GRPO conditions (52--93\\% of proved samples).\n\n\\textbf{H7: Conclusion duplication with ISR inflation.}\nThe formalization contains a single premise identical to the conclusion ($n{=}2$).\nRemoving the premise breaks the proof, so $\\text{ISR} \\geq 0.5$ by construction.\nThis mode is exclusive to ISR-reward conditions (64.5\\% vs.\\ 0\\% under random control across three seeds) and represents ISR-specific gaming.\n\n\\textbf{Tautological collapse.}\nDegeneration to a minimal two-component structure that is trivially provable, arising under exec-only conditions without ISR inflation.\n\n\\textbf{Repetition collapse.}\nIdentical premises generated repeatedly, inflating component count without adding logical content.\n\n\\textbf{Complexity without utility.}\nSyntactically complex but logically vacuous premises that do not contribute to the proof.\n\n\\textbf{Contradiction explosion.}\nContradictory premises (e.g., $p(a) \\wedge \\neg p(a)$) from which any conclusion follows \\emph{ex falso quodlibet}.\nObserved at extended training (1000 steps), with mean component count rising from 6.6 to 18.6.\n\n\\textbf{Query-as-fact gaming} (Prolog-specific).\nThe model converts the NL question into a Prolog atom asserted simultaneously as fact and query, making the proof trivially true.\nThis mode evades text-matching classifiers designed to detect conclusion embedding; detection requires functional analysis of the STA necessity vector ($n_{\\text{necessary}} = 1$ for 95/97 proved samples).\n\nDetection combines two complementary methods: normalized text matching (for H1, H7) and functional analysis of the necessity vector (for modes that bypass text-based classifiers, such as query-as-fact gaming).\nWe report both strict (text-match) and functional ($n_{\\text{necessary}}$-based) classifications throughout.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:50:34.902544+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:50:34.906984+00:00_

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
  "session": "worker_writing_method_20260514T194535",
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

_source line 18 · 2026-05-14T19:50:34.907234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T19:50:34.907487+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method.tex",
  "type": "paper",
  "description": "Method section (Section 3) for EMNLP 2026 submission. Covers task formulation, GRPO training, STA protocol with Algorithm 1, ISR definition with premise-count bias, 6 reward conditions (Table 1), and 7-mode hacking taxonomy.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex",
  "tags": "['paper', 'method', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method.tex",
    "type": "paper",
    "description": "Method section (Section 3) for EMNLP 2026 submission. Covers task formulation, GRPO training, STA protocol with Algorithm 1, ISR definition with premise-count bias, 6 reward conditions (Table 1), and 7-mode hacking taxonomy.",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex",
    "tags": "['paper', 'method', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T19:50:34.907791+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_4d5248\", \"name\": \"method.tex\", \"type\": \"paper\", \"description\": \"Method section (Section 3) for EMNLP 2026 submission. Covers task formulation, GRPO training, STA protocol with Algorithm 1, ISR definition with premise-count bias, 6 reward conditions (Table 1), and 7-mode hacking taxonomy.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/method_4d5248.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T19:50:03.620663+00:00\", \"tags\": [\"paper\", \"method\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:50:34.908077+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
  "description": "Estimate word count of method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/method.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
    "description": "Estimate word count of method.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:50:34.908305+00:00_

1019

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_method_20260514T194535",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T19:50:34.908585+00:00_

```json
{
  "section": "Method (Section 3)",
  "word_count": "~1020 (prose) + Algorithm 1 + Table 1 + 4 equations ≈ 1200 equivalent",
  "citations_needed": [
    "mccune2010prover9 (Prover9)",
    "folio (FOLIO dataset)",
    "deepseekmath (GRPO)",
    "demillo1978 (mutation testing)",
    "jia-harman-survey (mutation testing survey)"
  ],
  "figures_needed": [
    "fig:sta-overview (3-panel: formalization pipeline / STA ablation protocol / ISR as diagnostic vs reward)"
  ],
  "tables_needed": [
    "tab:reward (Table 1: 6 reward conditions, already included inline)"
  ],
  "notes": [
    "Introduced ISR* (proved-only ISR) notation for use throughout paper",
    "Convex formulation mentioned as discarded design choice, not a main condition",
    "Feature attribution citation placeholder needs a specific reference (e.g., Shapley/LIME)",
    "Figure reference uses fig:sta-overview (matches introduction)",
    "Premise-count bias flagged here, controlled-analysis deferred to §4",
    "Taxonomy quantitative analysis deferred to §4 (Experiments)"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_method_20260514T194535"
}
```

</details>

---
