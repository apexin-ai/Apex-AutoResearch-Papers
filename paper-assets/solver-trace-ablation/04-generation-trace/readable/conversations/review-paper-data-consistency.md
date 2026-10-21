# review paper data consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_review_paper-data-consistency_20260514T214424.jsonl`
- **Structured JSON:** [`3f101ece011845afb035.json`](../../sessions/3f/3f101ece011845afb035.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

60 recorded events

### Assistant

_source line 1 · 2026-05-14T21:44:31.431780+00:00_

You've hit your limit · resets 11:10pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_paper-data-consistency_20260514T214424"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T21:49:39.175268+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T21:49:39.175517+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
experiments.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.log
main.out
main.pdf
main.tex
method.tex
paper.aux
paper.bbl
paper.blg
paper.log
paper.out
paper.pdf
paper.tex
references.bib
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:49:39.175656+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
    "description": "List project root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:49:39.175867+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:49:39.175996+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:49:39.176114+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:49:39.176226+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'status': 'success'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'status': 'success'}"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:49:39.176342+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
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

_source line 10 · 2026-05-14T21:49:39.176458+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5021}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T21:49:39.176783+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 20933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:49:39.176990+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T21:49:39.177598+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T18:47:53.131Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"Reviewer 独立核实: query-as-fact gaming, 0% genuine. 97/97 proved 样本中 95/97 n_necessary=1（功能性 H7）。模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。PR=0.97, ISR=0.885 是 gaming artifact（高 ISR 因单 clause = query）。第三种 Goodhart pathway（vs s42 clean H7, s43 degenerate syntax H1）。对照: s42=negative (clean H7=100%), s43=negative (uppercase pseudo-Prolog H1=97.4%), s44=negative (query-as-fact gaming, functional H7=95/97).\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T18:20:56.947Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"Eval: PR=0.38, ISR=0.185 proved-only. Strict classifier: H7=0%, H1=0%, Genuine=100%. 但功能分析显示所有 38 proved 样本 n_necessary=1（功能性 H7）。模型生成大写伪 Prolog（如 MARY_IS_AN_AVADEOTE.）—— 非标准语法，strict classifier 无法匹配 conclusion。与 s42 (clean H7=100%) 不同的 Goodhart 路径，但同样是 hacking。磁盘 240G/250G 需清理。\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100,
…[truncated 39575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:49:39.177909+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T21:49:39.178102+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:49:39.178263+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:49:39.178476+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
10	Process reward models~\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \S\ref{sec:related-work} for full context).
12	
13	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
14	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intens
…[truncated 2679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:49:39.178644+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:49:39.178900+00:00_

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
…[truncated 7429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:49:39.179058+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T21:49:39.179217+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
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
27	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$, each removing one component, and re-runs the solver.
28	A compo
…[truncated 2965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:49:39.179357+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:49:39.179476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T21:49:39.179601+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'in_progress'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'pending'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'pending'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'pending'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'pending'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'pending'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'pending'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'in_progress'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'pending'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'pending'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'pending'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'pending'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'pending'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'pending'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T21:49:39.179816+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:49:39.179951+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T21:49:39.180090+00:00_

1	\section{Discussion and Conclusion}
2	
3	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
4	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
5	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
6	Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero genuine proofs, each via a distinct mechanism (\S\ref{sec:crosslogic}).
7	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	
9	\paragraph{Interpreting ISR.}
10	ISR values must always be read relative to the optimization objective: under exec-only Prolog training, \emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \emph{high} ISR reflects metric gaming.
11	The premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.
12	
13	\paragraph{Meta-Level Goodhart.}
14	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagnostic metric risks becoming a target when optimized.
15	The dose-response pattern ($\beta{=}0.1$: proxy gaming; $\beta{=}0.3$: performance collapse) maps onto the trajectory predicte
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:49:39.180227+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T21:49:39.180366+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:49:39.180508+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T21:49:39.180795+00:00_

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
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T21:49:39.181031+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "2\\.4(x|×|\\\\times)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "2\\.4(x|×|\\\\times)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T21:49:39.181168+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:49:39.181290+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "six (modes|hacking|distinct)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "six (modes|hacking|distinct)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T21:49:39.181408+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T21:49:39.181521+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "no hacking|zero hacking|hacking-free|hacking free",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "no hacking|zero hacking|hacking-free|hacking free",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T21:49:39.181651+00:00_

paper/experiments.tex:104:\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine).}
paper/experiments.tex:110:SFT remains the only condition with near-zero hacking (Figure~\ref{fig:hacking-composition}), confirming hacking is RL-reward-specific.
paper/abstract.tex:4:ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming the degeneration is RL-specific.
paper/introduction.tex:18:A supervised fine-tuning (SFT) baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.
paper/conclusion.tex:4:Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
paper/main.aux:511:\@writefile{lof}{\contentsline {figure}{\numberline {3}{\ignorespaces Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine).}}{6}{figure.caption.10}\protected@file@percent }
paper/main.aux:512:\newlabel{fig:hacking-composition}{{3}{6}{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% genuine)}{figure.caption.10}{}}
paper/paper.aux:899:\@writefile{lof}{\contentsline {figure}{\numberline {4}{\ignorespaces Hacking mode composition across
…[truncated 615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T21:49:39.181816+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "additive vs.? convex|convex vs.? additive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "additive vs.? convex|convex vs.? additive",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T21:49:39.181936+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:49:39.182052+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "3\\.2(x|×|\\\\times)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "3\\.2(x|×|\\\\times)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T21:49:39.182173+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T21:49:39.182291+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.143",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.143",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T21:49:39.182400+00:00_

paper/experiments.tex:64:ISR & 0.3 & 18 & 0.143 & --- & --- & --- \\
paper/appendix.tex:355:  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T21:49:39.182506+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seven|7 (modes|hacking)|seven (modes|hacking)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seven|7 (modes|hacking)|seven (modes|hacking)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T21:49:39.182637+00:00_

paper/experiments.tex:108:[Omitted long matching line]
paper/conclusion.tex:7:Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
paper/method.tex:63:Across conditions, seeds, and logic types, we identify seven hacking modes (H1, H7, tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, query-as-fact gaming; full definitions in \S\ref{sec:taxonomy} and Appendix~\ref{app:hacking-modes}).
paper/appendix.tex:122:We identify seven distinct reward hacking modes across all experiments.
paper/introduction.tex:30:\item We catalog 7 hacking modes including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of diagnostics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T21:49:39.182796+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{|\\\\ref\\{|\\\\autoref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{|\\\\ref\\{|\\\\autoref\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T21:49:39.182964+00:00_

paper/related_work.tex:2:\label{sec:related-work}
paper/related_work.tex:9:STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
paper/related_work.tex:14:ISR is solver-grounded rather than learned (no reward-model noise), yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.
paper/experiments.tex:2:\label{sec:experiments}
paper/experiments.tex:4:We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
paper/experiments.tex:7:\label{sec:setup}
paper/experiments.tex:16:Full hyperparameters are in Appendix~\ref{app:setup}.
paper/experiments.tex:19:\label{sec:diagnostic}
paper/experiments.tex:25:\label{fig:isr-collapse}
paper/experiments.tex:29:Figure~\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).
paper/experiments.tex:38:The cross-seed PR $\sigma{=}\pm47$\,pp is itself a finding: aggregate metrics obscure qualitatively different failure modes (per-seed details in Table~\ref{tab:beta01-3seed}).
paper/experiments.tex:45:\label{sec:goodhart}
paper/experiments.tex:68:\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\pm$std (ISR/Random $\beta{=}0.1$); other rows are single seed. $^\dagger$Seed~42; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\ref{tab:beta01-3see
…[truncated 7503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T21:49:39.183118+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'completed'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'completed'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'completed'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'completed'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'completed'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'completed'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'completed'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'in_progress'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'completed'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'completed'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'completed'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'completed'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'completed'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'completed'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'completed'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'in_progress'}]"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T21:49:39.183282+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T21:49:39.183443+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR & 0.1|Random & 0.1|0\\.582|0\\.5816",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR & 0.1|Random & 0.1|0\\.582|0\\.5816",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T21:49:39.183566+00:00_

paper/experiments.tex:61:ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 \\
paper/experiments.tex:62:Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 19 \\
paper/appendix.tex:343:  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
paper/figures/gen_fig4.py:18:fol_isr = [0.132, 0.000, 0.582]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T21:49:39.183691+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.557|0\\.559|0\\.55|sta-gt|ground.truth FOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.557|0\\.559|0\\.55|sta-gt|ground.truth FOL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T21:49:39.183834+00:00_

paper/appendix.tex:333:Ground-truth FOL
paper/appendix.tex:334:  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T21:49:39.183962+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/ 2>/dev/null | head -20",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/ 2>/dev/null | head -20",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T21:49:39.184081+00:00_

_deprecated
_project
analysis_random_vs_isr_b01_interim.md
claim_coverage_audit.md
component_count_analysis.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T21:49:39.184230+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md",
  "content": "# 论文数据一致性审查报告\n\n生成日期: 2026-05-14\n审查范围: `paper/{abstract,introduction,method,experiments,conclusion,related_work,appendix}.tex`\n数据源: `registry.yaml`（success/DONE 实验）+ `paper_framing.md`\n\n总体结论: **PASS（无 critical 数据错误）**。所有引用数字均可追溯至 registry，且与 `paper_framing.md` 一致。仅发现 2 处 minor 方法学不一致和 1 处需注意的约定（proved-only ISR 而非 mean ISR）——均不影响 paper claim 的正确性。\n\n---\n\n## 1. 数字一致性核对\n\n### 1.1 ISR 崩塌轨迹（abstract / intro / experiments §3.2 / appendix tab:beta01-3seed）\n\n| Step | 论文值 | Registry 来源 | Registry 实际值 | 状态 |\n|------|--------|---------------|------------------|------|\n| 100  | PR=32%, ISR=0.642 | plan003-eval-exec-only-r5 | prove_rate=0.32, proved_only_isr=0.6423 | ✓ |\n| 500  | PR=93%, ISR=0.132 | plan001-exec-only-s42-r2 | eval_prove_rate=0.93, eval_proved_only_isr=0.1324 | ✓ |\n| 1000 | PR=96%, ISR=0.003, components=18.55, 94.8% ISR=0 | plan016-extended-1000-s42 | prove_rate=0.96, isr=0.003 (proved_only=0.0028), components=18.55, isr_zero=94.8% | ✓ |\n\n**99.5% degradation** (abstract): (0.642 − 0.003)/0.642 = 99.53% ✓\n**−79.4% / −99.6%** (appendix): (0.642 − 0.132)/0.642 = 79.4%; (0.642 − 0.003)/0.642 = 99.5%。Appendix 写 −99.6% 实际是 99.5%，**rounding off by 0.1 pp**（minor，不需修）。\n\n### 1.2 PR 轨迹\n\n论文: 32% → 93% → 96%。Registry: 0.32 → 0.93 → 0.96。 ✓\n\n### 1.3 ISR β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.81 | 0.415 | 16.0 | 51.9 | 30.9 | plan002-additive-b01-s42 | PR=0.81, ISR*=0.4154, h7=0.16, h1=0.519, genuine=0.309 | ✓ |\n| s43 | 0.61 | 0.830 | 96.7 | 0 | ~3 | plan002-additive-b01-s43 | PR=0.61, ISR*=0.8301, h7=0.967, h1=0 | ✓ |\n| s44 | 0.89 | 0.902 | 86.5 | 0 | ~13.5 | plan002-additive-b01-s44 | PR=0.89, mean_isr=0.803 → proved_only=0.803/0.89=0.902, h7=0.865 | ✓ |\n\n3-seed mean: PR=0.77±0.14, ISR*=0.716±0.26。重新计算：\n- PR mean=(0.81+0.61+0.89)/3=0.770; std≈0.144 ✓\n- ISR mean=(0.415+0.830+0.902)/3=0.716; std≈0.262 ✓\n\n### 1.4 Random β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.79 | 0.131 | 0 | 70.9 | 29.1 | plan018-additive-random-b01-s42 | PR=0.79, ISR*=0.1314 | ✓ |\n| s43 | 0.88 | 0.058 | 0 | 93.2 | 6.8 | plan018-additive-random-b01-s43-r2 | h1_rate=93.2, genuine_rate=6.8 (PR/ISR 在 framing 中确认) | ✓ |\n| s44 | 0.89 | 0.070 | 0 | 79.8 | 20.2 | plan018-additive-random-b01-s44 | PR=0.89, ISR*=0.0695 | ✓ |\n\n3-seed mean: PR=0.85±0.06, ISR*=0.086±0.039。重算：\n- PR mean=(0.79+0.88+0.89)/3=0.853; std≈0.055 ✓\n- ISR mean=(0.131+0.058+0.070)/3=0.0863; std≈0.039 ✓\n\n### 1.5 SFT Baseline\n\n| 指标 | 论文值 | Registry plan009-sft-baseline-s42-r4 | 状态 |\n|------|--------|--------------------------------------|------|\n| PR | 14% | 0.14 | ✓ |\n| ISR* | 0.571 | 0.571 | ✓ |\n| H7 | 0/14 (0%) | h7_count=0 | ✓ |\n| H1 | 1/14 (7.1%) | h1_count=1, h1_rate=0.071 | ✓ |\n| Genuine | 13/14 (92.9%) | genuine_count=13, genuine_rate=0.929 | ✓ |\n\n### 1.6 Prolog 数字 (tab:prolog-crosslogic / §3.3)\n\n**Exec-only:**\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.83 | 0.037 | plan006-prolog-exec-s42: PR=0.83, ISR*=0.037 | ✓ |\n| s43 | 0.56 | 0.015 | plan006-prolog-exec-s43-r3: PR=0.56, ISR*=0.015 | ✓ |\n| s44 | 0.21 | 0.387 | plan006-prolog-exec-s44: PR=0.21, ISR*=0.3866 | ✓ |\n\n3-seed mean: PR=0.53±0.31, ISR=0.146±0.21\n- (0.037+0.015+0.387)/3 = 0.146 ✓\n- std≈0.213 ✓\n\n**Exec+ISR (STA reward):**\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | Registry | 状态 |\n|------|---------|-----------|----------|----------|----------|------|\n| s42 | 0.50 | 1.000 | 100 | 0 | plan006-prolog-sta-s42: PR=0.5, ISR*=1, h7=1 | ✓ |\n| s43 | 0.38 | 0.185 | 0 (strict; functional 100%) | 97.4 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853, h7=0, h1=37/38=97.4% | ✓ |\n| s44 | 0.97 | 0.912 | 0 (strict; functional 95/97) | 0 | plan006-prolog-sta-s44: PR=0.97, mean_isr=0.885 → proved_only=0.885/0.97=0.9124 | ✓ |\n\n3-seed mean: PR=0.62±0.31, ISR=0.699±0.45\n- (0.5+0.38+0.97)/3=0.617 ✓\n- (1.0+0.185+0.912)/3=0.699 ✓\n\n### 1.7 1000-step extended run (§3.2)\n\n论文: ISR=0.003, 94.8% ISR=0, mean components 18.55, H1=100%, Gen=0%。\nRegistry plan016-extended-1000-s42: isr=0.003, components=18.55, h1_rate=1, genuine_rate=0, n_necessary=0 ratio=94.8%。 ✓\n\n### 1.8 Exec-only 跨 seed (§3.2)\n\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.93, H1=87.1% | — | plan001-exec-only-s42-r2: PR=0.93, h1=0.871 | ✓ |\n| s43 | 0.14, ISR=0 | sampling T=0.7 | plan001-exec-only-s43-r4: sampling_PR=0.14, sampling_ISR=0 | ✓ |\n| s44 | 0.98, H7=100%, components=2.04 | — | plan001-exec-only-s44: PR=0.98, h7=1, components=2.04 | ✓ |\n\n3-seed PR σ=±47pp: std(0.93, 0.14, 0.98)=0.471 ✓\n\n### 1.9 其他基线 (appendix tab:beta01-3seed)\n\n| 行 | 论文值 | Registry | 状态 |\n|----|--------|----------|------|\n| Base model (no training) | PR=0.12, ISR=0.064 | sta-phase0-baseline: prove_rate=0.12, mean_isr=0.0641 | ✓ |\n| Ground-truth FOL | PR=0.18, ISR=0.559 | sta-gt-isr-baseline: prove_rate=0.18, mean_isr=0.5588 | ✓ |\n\n### 1.10 Random β=0.3 (Goodhart landscape)\n\n论文: PR=48, ISR=0.094, components=9.6。\nRegistry plan017-additive-random-s42: PR=0.48, ISR*=0.0943, components=9.6。 ✓\n\n### 1.11 ISR β=0.3 (无独立 eval registry 项)\n\n论文: PR=18, ISR*=0.143。\nRegistry plan002-additive-b03-s42 仅记录训练统计（无 eval_*），但与 framing 一致：framing 给出 mean_isr=0.026，而 0.143 × 0.18 = 0.0257 ≈ 0.026，所以 paper 的 0.143（proved-only）与 framing 的 0.026（mean）数学一致。 ✓\n\n### 1.12 Premise-count-matched (§3.2 / Limitations)\n\n论文: 1.06× (ISR-genuine ISR=0.258 n=11 vs random-genuine ISR=0.243 n=21)。\nFraming: ISR s42 genuine n_prem≥3: n=11, mean ISR=0.2578; Random s42 genuine n_prem≥3: n=21, mean ISR=0.2434。Ratio=1.06×。 ✓\n\n### 1.13 Component-count s42\n\n论文: ISR s42 mean=5.58 components, Random s42 mean=8.46 components。\nRegistry plan002-b01-s42: component_count_mean=5.58。plan018-random-s42: component_count_mean=8.46。 ✓\n\n### 1.14 NLI Limitation (Conclusion / Appendix)\n\n论文: Spearman ρ=−0.049, p=0.187。\nRegistry plan014-downstream-nli-s42: spearman_rho=-0.049, spearman_p=0.187。 ✓\n\n### 1.15 H7 pooled rate\n\n论文: 64.5% (149/231), Random 0% (0/256)。\n- ISR pooled: (13 + 59 + 77)/(81+61+89) = 149/231 = 64.50% ✓\n- Random pooled: (0+0+0)/(79+88+89) = 0/256 ✓\n\n---\n\n## 2. 硬约束检查\n\n| 约束 | 状态 | 证据 |\n|------|------|------|\n| D051: \"2.4x\" 已作废，不应出现 | ✅ PASS | grep `2\\.4(x|×|\\\\times)` 在 paper/*.tex 0 matches |\n| 旧的 \"3.2x\" 也已移除 | ✅ PASS | grep `3\\.2(x|×|\\\\times)` 0 matches |\n| Hacking taxonomy = 7 modes (非 6) | ✅ PASS | abstract/method/conclusion/appendix 均说 \"seven\" / \"7\"。`six modes` 0 matches |\n| ISR β=0.1 不应标 \"no hacking\" | ✅ PASS | \"near-zero hacking\" 仅用于 SFT (92.9% genuine)；ISR β=0.1 在论文中明确标注 H7 主导 |\n| s44 Prolog STA: query-as-fact gaming, 0% genuine | ✅ PASS | appendix tab:prolog-crosslogic 标 Gen=0%，footnote $^b$ 解释功能性 H7 (95/97) |\n| plan013 vs plan017 不简化为 \"additive vs convex\" | ✅ PASS | grep 0 matches |\n| C006: ISR 双语义区分（exec-only low ISR=冗余编码 vs ISR-reward high ISR=metric gaming） | ✅ PASS | conclusion §\"Interpreting ISR\" 和 appendix §\"What ISR measures\" 均明确区分 |\n\n---\n\n## 3. 内部一致性检查\n\n### 3.1 跨章节核心数字一致\n\n- 93% PR + 87% H1: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 64.5% H7 vs 0% random: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 1.06× premise-matched: abstract / intro §1 / experiments §3.2 / appendix。一致 ✓\n- 18% vs 48%（β=0.3 ISR vs Random）: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 92.9% genuine SFT: abstract / intro / experiments §3.1 / Table 1 / appendix。一致 ✓\n- 3/3 Prolog seeds gaming, 0% genuine: abstract / intro / experiments §3.3 / conclusion / appendix。一致 ✓\n- 7 hacking modes: method §2.4 / experiments §3.4 / conclusion / appendix §C。一致 ✓\n- 6 reward conditions: method §2.3 / experiments §3 setup / conclusion。一致 ✓ (Exec-only / ISR β=0.1 / ISR β=0.3 / Random β=0.1 / Random β=0.3 / SFT = 6)\n- ISR 崩塌 0.642→0.132→0.003: abstract / intro / experiments §3.2 / appendix §F。一致 ✓\n\n### 3.2 交叉引用\n\n所有 `\\ref{}` 标签均能在 paper/*.tex 找到对应定义：\n- sec:setup, sec:diagnostic, sec:goodhart, sec:crosslogic, sec:taxonomy, sec:taxonomy-method, sec:method, sec:task, sec:sta, sec:rewards, sec:experiments, sec:related-work ✓\n- fig:sta-overview, fig:isr-collapse, fig:hacking-composition, fig:prolog-comparison ✓\n- tab:goodhart-landscape, tab:hyperparams, tab:hacking-taxonomy-app, tab:fol-detailed / tab:beta01-3seed, tab:prolog-detailed / tab:prolog-crosslogic ✓\n- alg:sta ✓\n- eq:isr ✓\n- app:setup, app:algorithm, app:extended-discussion, app:hacking-modes, app:detailed-results ✓\n\n### 3.3 Minor 内部不一致\n\n#### 3.3.1 H1 mean 算法不一致（simple mean vs pooled）\n\n- **H7 ISR β=0.1 (论文 65%)**: pooled = 149/231 = 64.5% → 论文用 pooled\n- **H1 ISR β=0.1 (论文 17%)**: simple mean = (51.9+0+0)/3 = 17.3% vs pooled = 42/231 = 18.2% → 论文用 simple mean\n\n这与 framing 一致（framing 也是混用），但同一行同一指标用两种平均方法略不规范。**Impact: 0.8pp 差异，不影响 claim**。\n\n建议：在 caption 或正文 footnote 中说明 H7/H1 用 simple mean of seeds（而非 pooled）。\n\n#### 3.3.2 Appendix line 414 微小 rounding\n\n> \"ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.6$\\% from step 100).\"\n\n(0.642−0.003)/0.642 = 0.9953 = **99.5%**，paper 写 99.6%。Abstract 写 99.5%（正确）。\n\n**建议**：把 appendix 改为 99.5%，与 abstract 对齐。\n\n#### 3.3.3 Appendix tab:beta01-3seed exec-only s44 ISR* = 0.582\n\nRegistry 值 0.5816 — 四舍五入应为 0.582 ✓。但 framing 文本写 0.57（粗略），paper 用更精确的 0.582。无问题。\n\n#### 3.3.4 Proved-only vs mean ISR 表达约定\n\nPaper 全文使用 ISR* = proved-only。Registry 中部分 metrics 仅存 mean_isr（all samples，含 unproved=0）。当看到 paper 给的 0.902 (ISR s44) vs registry 0.803 (mean_isr) 时，需理解：proved_only = mean_isr / PR (∵ unproved=0)。\n\n- ISR β=0.1 s44: 0.803/0.89 = 0.902 ✓\n- Prolog STA s44: 0.885/0.97 = 0.912 ✓\n- ISR β=0.3 s42: 0.0257/0.18 = 0.143 ✓ (framing 写 0.026 = mean, paper 写 0.143 = proved-only)\n- Random β=0.3 s42: 0.0453/0.48 = 0.0944 ✓\n\n约定一致，无错误。但**建议在 §3.1 Setup 中明确 footnote**：「除非另有说明，所有 ISR 报告均为 proved-only ISR* ≡ mean of ISR over proved samples」。Setup 已在第 13 行说明「we report ... proved-only ISR (ISR*, over proved samples only)」，已 OK。\n\n---\n\n## 4. 总结与建议修改\n\n### 4.1 总体评价\n\n**论文数据层面 PASS**。所有定量 claim 均可追溯至 registry，跨章节一致，硬约束全部遵守。\n\n### 4.2 建议修改（均为 minor）\n\n1. **Appendix line 414**: `−99.6%` → `−99.5%` 以与 abstract 99.5% 对齐。\n2. **Table 1 caption 或 §3.2 footnote**: 添加一句说明 3-seed mean H7/H1 是 simple mean across seeds（非 pooled），以避免审稿人质疑 H7=65% 与 H1=17% 计算口径差异。\n3. **可选**: appendix line 388 Prolog STA s44 后 footnote $^b$ 提到「strict classifier reports Genuine=100%」，但表中已经写 Gen=0%（覆盖），建议在表内 Gen 列标注 `0$^b$` 或类似显眼标记，避免读者误读 ground-truth 标签。当前 footnote 在右下角，可能被忽略。\n\n### 4.3 无 critical 错误\n\n- 没有引用作废的 2.4× 优势\n- 没有混淆 binary _fast_fn 训练 ISR 与 full STA eval ISR\n- 没有把 s44 Prolog STA 误标为 genuine\n- 7-mode taxonomy 全文一致\n- C001 数据约束（train_500_seed42.jsonl）在 setup 和 appendix 均明确\n\n报告结束。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md",
    "content": "# 论文数据一致性审查报告\n\n生成日期: 2026-05-14\n审查范围: `paper/{abstract,introduction,method,experiments,conclusion,related_work,appendix}.tex`\n数据源: `registry.yaml`（success/DONE 实验）+ `paper_framing.md`\n\n总体结论: **PASS（无 critical 数据错误）**。所有引用数字均可追溯至 registry，且与 `paper_framing.md` 一致。仅发现 2 处 minor 方法学不一致和 1 处需注意的约定（proved-only ISR 而非 mean ISR）——均不影响 paper claim 的正确性。\n\n---\n\n## 1. 数字一致性核对\n\n### 1.1 ISR 崩塌轨迹（abstract / intro / experiments §3.2 / appendix tab:beta01-3seed）\n\n| Step | 论文值 | Registry 来源 | Registry 实际值 | 状态 |\n|------|--------|---------------|------------------|------|\n| 100  | PR=32%, ISR=0.642 | plan003-eval-exec-only-r5 | prove_rate=0.32, proved_only_isr=0.6423 | ✓ |\n| 500  | PR=93%, ISR=0.132 | plan001-exec-only-s42-r2 | eval_prove_rate=0.93, eval_proved_only_isr=0.1324 | ✓ |\n| 1000 | PR=96%, ISR=0.003, components=18.55, 94.8% ISR=0 | plan016-extended-1000-s42 | prove_rate=0.96, isr=0.003 (proved_only=0.0028), components=18.55, isr_zero=94.8% | ✓ |\n\n**99.5% degradation** (abstract): (0.642 − 0.003)/0.642 = 99.53% ✓\n**−79.4% / −99.6%** (appendix): (0.642 − 0.132)/0.642 = 79.4%; (0.642 − 0.003)/0.642 = 99.5%。Appendix 写 −99.6% 实际是 99.5%，**rounding off by 0.1 pp**（minor，不需修）。\n\n### 1.2 PR 轨迹\n\n论文: 32% → 93% → 96%。Registry: 0.32 → 0.93 → 0.96。 ✓\n\n### 1.3 ISR β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.81 | 0.415 | 16.0 | 51.9 | 30.9 | plan002-additive-b01-s42 | PR=0.81, ISR*=0.4154, h7=0.16, h1=0.519, genuine=0.309 | ✓ |\n| s43 | 0.61 | 0.830 | 96.7 | 0 | ~3 | plan002-additive-b01-s43 | PR=0.61, ISR*=0.8301, h7=0.967, h1=0 | ✓ |\n| s44 | 0.89 | 0.902 | 86.5 | 0 | ~13.5 | plan002-additive-b01-s44 | PR=0.89, mean_isr=0.803 → proved_only=0.803/0.89=0.902, h7=0.865 | ✓ |\n\n3-seed mean: PR=0.77±0.14, ISR*=0.716±0.26。重新计算：\n- PR mean=(0.81+0.61+0.89)/3=0.770; std≈0.144 ✓\n- ISR mean=(0.415+0.830+0.902)/3=0.716; std≈0.262 ✓\n\n### 1.4 Random β=0.1 三 seed (tab:beta01-3seed)\n\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |\n|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|\n| s42 | 0.79 | 0.131 | 0 | 70.9 | 29.1 | plan018-additive-random-b01-s42 | PR=0.79, ISR*=0.1314 | ✓ |\n| s43 | 0.88 | 0.058 | 0 | 93.2 | 6.8 | plan018-additive-random-b01-s43-r2 | h1_rate=93.2, genuine_rate=6.8 (PR/ISR 在 framing 中确认) | ✓ |\n| s44 | 0.89 | 0.070 | 0 | 79.8 | 20.2 | plan018-additive-random-b01-s44 | PR=0.89, ISR*=0.0695 | ✓ |\n\n3-seed mean: PR=0.85±0.06, ISR*=0.086±0.039。重算：\n- PR mean=(0.79+0.88+0.89)/3=0.853; std≈0.055 ✓\n- ISR mean=(0.131+0.058+0.070)/3=0.0863; std≈0.039 ✓\n\n### 1.5 SFT Baseline\n\n| 指标 | 论文值 | Registry plan009-sft-baseline-s42-r4 | 状态 |\n|------|--------|--------------------------------------|------|\n| PR | 14% | 0.14 | ✓ |\n| ISR* | 0.571 | 0.571 | ✓ |\n| H7 | 0/14 (0%) | h7_count=0 | ✓ |\n| H1 | 1/14 (7.1%) | h1_count=1, h1_rate=0.071 | ✓ |\n| Genuine | 13/14 (92.9%) | genuine_count=13, genuine_rate=0.929 | ✓ |\n\n### 1.6 Prolog 数字 (tab:prolog-crosslogic / §3.3)\n\n**Exec-only:**\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.83 | 0.037 | plan006-prolog-exec-s42: PR=0.83, ISR*=0.037 | ✓ |\n| s43 | 0.56 | 0.015 | plan006-prolog-exec-s43-r3: PR=0.56, ISR*=0.015 | ✓ |\n| s44 | 0.21 | 0.387 | plan006-prolog-exec-s44: PR=0.21, ISR*=0.3866 | ✓ |\n\n3-seed mean: PR=0.53±0.31, ISR=0.146±0.21\n- (0.037+0.015+0.387)/3 = 0.146 ✓\n- std≈0.213 ✓\n\n**Exec+ISR (STA reward):**\n| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | Registry | 状态 |\n|------|---------|-----------|----------|----------|----------|------|\n| s42 | 0.50 | 1.000 | 100 | 0 | plan006-prolog-sta-s42: PR=0.5, ISR*=1, h7=1 | ✓ |\n| s43 | 0.38 | 0.185 | 0 (strict; functional 100%) | 97.4 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853, h7=0, h1=37/38=97.4% | ✓ |\n| s44 | 0.97 | 0.912 | 0 (strict; functional 95/97) | 0 | plan006-prolog-sta-s44: PR=0.97, mean_isr=0.885 → proved_only=0.885/0.97=0.9124 | ✓ |\n\n3-seed mean: PR=0.62±0.31, ISR=0.699±0.45\n- (0.5+0.38+0.97)/3=0.617 ✓\n- (1.0+0.185+0.912)/3=0.699 ✓\n\n### 1.7 1000-step extended run (§3.2)\n\n论文: ISR=0.003, 94.8% ISR=0, mean components 18.55, H1=100%, Gen=0%。\nRegistry plan016-extended-1000-s42: isr=0.003, components=18.55, h1_rate=1, genuine_rate=0, n_necessary=0 ratio=94.8%。 ✓\n\n### 1.8 Exec-only 跨 seed (§3.2)\n\n| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |\n|------|---------|-----------|----------|------|\n| s42 | 0.93, H1=87.1% | — | plan001-exec-only-s42-r2: PR=0.93, h1=0.871 | ✓ |\n| s43 | 0.14, ISR=0 | sampling T=0.7 | plan001-exec-only-s43-r4: sampling_PR=0.14, sampling_ISR=0 | ✓ |\n| s44 | 0.98, H7=100%, components=2.04 | — | plan001-exec-only-s44: PR=0.98, h7=1, components=2.04 | ✓ |\n\n3-seed PR σ=±47pp: std(0.93, 0.14, 0.98)=0.471 ✓\n\n### 1.9 其他基线 (appendix tab:beta01-3seed)\n\n| 行 | 论文值 | Registry | 状态 |\n|----|--------|----------|------|\n| Base model (no training) | PR=0.12, ISR=0.064 | sta-phase0-baseline: prove_rate=0.12, mean_isr=0.0641 | ✓ |\n| Ground-truth FOL | PR=0.18, ISR=0.559 | sta-gt-isr-baseline: prove_rate=0.18, mean_isr=0.5588 | ✓ |\n\n### 1.10 Random β=0.3 (Goodhart landscape)\n\n论文: PR=48, ISR=0.094, components=9.6。\nRegistry plan017-additive-random-s42: PR=0.48, ISR*=0.0943, components=9.6。 ✓\n\n### 1.11 ISR β=0.3 (无独立 eval registry 项)\n\n论文: PR=18, ISR*=0.143。\nRegistry plan002-additive-b03-s42 仅记录训练统计（无 eval_*），但与 framing 一致：framing 给出 mean_isr=0.026，而 0.143 × 0.18 = 0.0257 ≈ 0.026，所以 paper 的 0.143（proved-only）与 framing 的 0.026（mean）数学一致。 ✓\n\n### 1.12 Premise-count-matched (§3.2 / Limitations)\n\n论文: 1.06× (ISR-genuine ISR=0.258 n=11 vs random-genuine ISR=0.243 n=21)。\nFraming: ISR s42 genuine n_prem≥3: n=11, mean ISR=0.2578; Random s42 genuine n_prem≥3: n=21, mean ISR=0.2434。Ratio=1.06×。 ✓\n\n### 1.13 Component-count s42\n\n论文: ISR s42 mean=5.58 components, Random s42 mean=8.46 components。\nRegistry plan002-b01-s42: component_count_mean=5.58。plan018-random-s42: component_count_mean=8.46。 ✓\n\n### 1.14 NLI Limitation (Conclusion / Appendix)\n\n论文: Spearman ρ=−0.049, p=0.187。\nRegistry plan014-downstream-nli-s42: spearman_rho=-0.049, spearman_p=0.187。 ✓\n\n### 1.15 H7 pooled rate\n\n论文: 64.5% (149/231), Random 0% (0/256)。\n- ISR pooled: (13 + 59 + 77)/(81+61+89) = 149/231 = 64.50% ✓\n- Random pooled: (0+0+0)/(79+88+89) = 0/256 ✓\n\n---\n\n## 2. 硬约束检查\n\n| 约束 | 状态 | 证据 |\n|------|------|------|\n| D051: \"2.4x\" 已作废，不应出现 | ✅ PASS | grep `2\\.4(x|×|\\\\times)` 在 paper/*.tex 0 matches |\n| 旧的 \"3.2x\" 也已移除 | ✅ PASS | grep `3\\.2(x|×|\\\\times)` 0 matches |\n| Hacking taxonomy = 7 modes (非 6) | ✅ PASS | abstract/method/conclusion/appendix 均说 \"seven\" / \"7\"。`six modes` 0 matches |\n| ISR β=0.1 不应标 \"no hacking\" | ✅ PASS | \"near-zero hacking\" 仅用于 SFT (92.9% genuine)；ISR β=0.1 在论文中明确标注 H7 主导 |\n| s44 Prolog STA: query-as-fact gaming, 0% genuine | ✅ PASS | appendix tab:prolog-crosslogic 标 Gen=0%，footnote $^b$ 解释功能性 H7 (95/97) |\n| plan013 vs plan017 不简化为 \"additive vs convex\" | ✅ PASS | grep 0 matches |\n| C006: ISR 双语义区分（exec-only low ISR=冗余编码 vs ISR-reward high ISR=metric gaming） | ✅ PASS | conclusion §\"Interpreting ISR\" 和 appendix §\"What ISR measures\" 均明确区分 |\n\n---\n\n## 3. 内部一致性检查\n\n### 3.1 跨章节核心数字一致\n\n- 93% PR + 87% H1: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 64.5% H7 vs 0% random: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 1.06× premise-matched: abstract / intro §1 / experiments §3.2 / appendix。一致 ✓\n- 18% vs 48%（β=0.3 ISR vs Random）: abstract / intro / experiments §3.2 / appendix。一致 ✓\n- 92.9% genuine SFT: abstract / intro / experiments §3.1 / Table 1 / appendix。一致 ✓\n- 3/3 Prolog seeds gaming, 0% genuine: abstract / intro / experiments §3.3 / conclusion / appendix。一致 ✓\n- 7 hacking modes: method §2.4 / experiments §3.4 / conclusion / appendix §C。一致 ✓\n- 6 reward conditions: method §2.3 / experiments §3 setup / conclusion。一致 ✓ (Exec-only / ISR β=0.1 / ISR β=0.3 / Random β=0.1 / Random β=0.3 / SFT = 6)\n- ISR 崩塌 0.642→0.132→0.003: abstract / intro / experiments §3.2 / appendix §F。一致 ✓\n\n### 3.2 交叉引用\n\n所有 `\\ref{}` 标签均能在 paper/*.tex 找到对应定义：\n- sec:setup, sec:diagnostic, sec:goodhart, sec:crosslogic, sec:taxonomy, sec:taxonomy-method, sec:method, sec:task, sec:sta, sec:rewards, sec:experiments, sec:related-work ✓\n- fig:sta-overview, fig:isr-collapse, fig:hacking-composition, fig:prolog-comparison ✓\n- tab:goodhart-landscape, tab:hyperparams, tab:hacking-taxonomy-app, tab:fol-detailed / tab:beta01-3seed, tab:prolog-detailed / tab:prolog-crosslogic ✓\n- alg:sta ✓\n- eq:isr ✓\n- app:setup, app:algorithm, app:extended-discussion, app:hacking-modes, app:detailed-results ✓\n\n### 3.3 Minor 内部不一致\n\n#### 3.3.1 H1 mean 算法不一致（simple mean vs pooled）\n\n- **H7 ISR β=0.1 (论文 65%)**: pooled = 149/231 = 64.5% → 论文用 pooled\n- **H1 ISR β=0.1 (论文 17%)**: simple mean = (51.9+0+0)/3 = 17.3% vs pooled = 42/231 = 18.2% → 论文用 simple mean\n\n这与 framing 一致（framing 也是混用），但同一行同一指标用两种平均方法略不规范。**Impact: 0.8pp 差异，不影响 claim**。\n\n建议：在 caption 或正文 footnote 中说明 H7/H1 用 simple mean of seeds（而非 pooled）。\n\n#### 3.3.2 Appendix line 414 微小 rounding\n\n> \"ISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.6$\\% from step 100).\"\n\n(0.642−0.003)/0.642 = 0.9953 = **99.5%**，paper 写 99.6%。Abstract 写 99.5%（正确）。\n\n**建议**：把 appendix 改为 99.5%，与 abstract 对齐。\n\n#### 3.3.3 Appendix tab:beta01-3seed exec-only s44 ISR* = 0.582\n\nRegistry 值 0.5816 — 四舍五入应为 0.582 ✓。但 framing 文本写 0.57（粗略），paper 用更精确的 0.582。无问题。\n\n#### 3.3.4 Proved-only vs mean ISR 表达约定\n\nPaper 全文使用 ISR* = proved-only。Registry 中部分 metrics 仅存 mean_isr（all samples，含 unproved=0）。当看到 paper 给的 0.902 (ISR s44) vs registry 0.803 (mean_isr) 时，需理解：proved_only = mean_isr / PR (∵ unproved=0)。\n\n- ISR β=0.1 s44: 0.803/0.89 = 0.902 ✓\n- Prolog STA s44: 0.885/0.97 = 0.912 ✓\n- ISR β=0.3 s42: 0.0257/0.18 = 0.143 ✓ (framing 写 0.026 = mean, paper 写 0.143 = proved-only)\n- Random β=0.3 s42: 0.0453/0.48 = 0.0944 ✓\n\n约定一致，无错误。但**建议在 §3.1 Setup 中明确 footnote**：「除非另有说明，所有 ISR 报告均为 proved-only ISR* ≡ mean of ISR over proved samples」。Setup 已在第 13 行说明「we report ... proved-only ISR (ISR*, over proved samples only)」，已 OK。\n\n---\n\n## 4. 总结与建议修改\n\n### 4.1 总体评价\n\n**论文数据层面 PASS**。所有定量 claim 均可追溯至 registry，跨章节一致，硬约束全部遵守。\n\n### 4.2 建议修改（均为 minor）\n\n1. **Appendix line 414**: `−99.6%` → `−99.5%` 以与 abstract 99.5% 对齐。\n2. **Table 1 caption 或 §3.2 footnote**: 添加一句说明 3-seed mean H7/H1 是 simple mean across seeds（非 pooled），以避免审稿人质疑 H7=65% 与 H1=17% 计算口径差异。\n3. **可选**: appendix line 388 Prolog STA s44 后 footnote $^b$ 提到「strict classifier reports Genuine=100%」，但表中已经写 Gen=0%（覆盖），建议在表内 Gen 列标注 `0$^b$` 或类似显眼标记，避免读者误读 ground-truth 标签。当前 footnote 在右下角，可能被忽略。\n\n### 4.3 无 critical 错误\n\n- 没有引用作废的 2.4× 优势\n- 没有混淆 binary _fast_fn 训练 ISR 与 full STA eval ISR\n- 没有把 s44 Prolog STA 误标为 genuine\n- 7-mode taxonomy 全文一致\n- C001 数据约束（train_500_seed42.jsonl）在 setup 和 appendix 均明确\n\n报告结束。\n"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T21:49:39.184539+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T21:49:39.184684+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'completed'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'completed'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'completed'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'completed'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'completed'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'completed'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'completed'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all paper sections (conclusion, related_work, appendix)', 'activeForm': 'Reading remaining paper sections', 'status': 'completed'}, {'content': 'Cross-check ISR collapse trajectory numbers (0.642/0.132/0.003)', 'activeForm': 'Cross-checking ISR collapse numbers', 'status': 'completed'}, {'content': 'Cross-check 3-seed β=0.1 ISR/Random numbers in Table 1 and appendix', 'activeForm': 'Cross-checking β=0.1 3-seed numbers', 'status': 'completed'}, {'content': 'Cross-check SFT baseline numbers (PR=14%, ISR=0.571, 92.9%)', 'activeForm': 'Cross-checking SFT baseline numbers', 'status': 'completed'}, {'content': 'Cross-check Prolog numbers in experiments/appendix', 'activeForm': 'Cross-checking Prolog numbers', 'status': 'completed'}, {'content': 'Check hard constraints (no 2.4x, hacking taxonomy 7, etc.)', 'activeForm': 'Checking hard constraints from paper_framing', 'status': 'completed'}, {'content': 'Check internal consistency between abstract/intro/experiments/conclusion', 'activeForm': 'Checking internal consistency', 'status': 'completed'}, {'content': 'Write consistency report to artifacts/', 'activeForm': 'Writing consistency report', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T21:49:39.184878+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_paper-data-consistency_20260514T214424",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-14T21:49:39.185035+00:00_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md`。

**核心结论：PASS（无 critical 错误）**

- 所有数字（ISR 崩塌轨迹 0.642→0.132→0.003、3-seed β=0.1 ISR/Random、SFT 92.9%、Prolog 3-seed、1000-step 18.55 components 等）均与 registry 一致
- 所有硬约束遵守：0 处 "2.4x"、0 处 "six modes"、s44 query-as-fact gaming 正确标 0% genuine、plan013 vs plan017 未简化为 additive/convex 对照、ISR β=0.1 未误标 "no hacking"
- "near-zero hacking" 仅用于 SFT（92.9% genuine），不用于 ISR β=0.1
- proved-only ISR* 约定全文一致（registry 中部分 mean_isr 数学换算后吻合）

**3 处 minor 建议修改：**
1. Appendix line 414 把 `−99.6%` 改为 `−99.5%`（与 abstract 对齐）
2. Table 1 caption 或 §3.2 footnote 说明 H7/H1 是 simple mean across seeds（H1=17% 用 simple mean，H7=65% 用 pooled，口径差异 ~0.8pp）
3. 可选：Prolog STA s44 的 Gen=0 在表内更显眼标注，避免读者忽略 footnote $^b$ 中的 strict classifier 100% genuine 误报

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_paper-data-consistency_20260514T214424"
}
```

</details>

---
