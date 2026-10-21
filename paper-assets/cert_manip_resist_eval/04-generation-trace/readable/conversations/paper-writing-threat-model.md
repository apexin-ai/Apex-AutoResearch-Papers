# paper writing threat model

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_writing_threat_model_20260522T151212.jsonl`
- **Structured JSON:** [`5caa2069e8735b032188.json`](../../sessions/5c/5caa2069e8735b032188.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-22T15:13:02.027548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/paper/theorem1_proof.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/paper/theorem1_proof.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T15:13:02.028277+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage{amsmath, amssymb, amsthm}
4	\usepackage{mathtools}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{enumitem}
7	
8	\newtheorem{theorem}{Theorem}
9	\newtheorem{lemma}[theorem]{Lemma}
10	\newtheorem{proposition}[theorem]{Proposition}
11	\newtheorem{corollary}[theorem]{Corollary}
12	\newtheorem{definition}[theorem]{Definition}
13	\newtheorem*{remark}{Remark}
14	
15	\DeclareMathOperator*{\argmax}{arg\,max}
16	
17	\title{Weakest-Link Monotonicity Theorem for\\Majority-Vote Panel ASR}
18	\author{}
19	\date{}
20	
21	\begin{document}
22	\maketitle
23	
24	%% ================================================================
25	\section{Setup and Definitions}
26	%% ================================================================
27	
28	\begin{definition}[Panel and Majority Vote]
29	\label{def:panel}
30	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges ($K$ odd) that independently evaluate a candidate text. The panel uses \emph{majority-vote aggregation}: it is \emph{compromised} if and only if at least $t = \lceil K/2 \rceil$ judges are individually compromised.
31	\end{definition}
32	
33	\begin{definition}[Attack Model]
34	\label{def:attack}
35	An \emph{attack} $a \in \mathcal{A}$ is an adversarial perturbation applied to the input that all judges evaluate. Under attack $a$, the judges' failure outcomes are described by a joint distribution over binary random variables $(X_1^a, \ldots, X_K^a) \in \{0,1\}^K$, where $X_j^a = 1$ indicates that judge $J_j$ is compromised. The \emph{individual vulnerability} of $J_j$ under attack $a$ is
36	\[
37	    \eta_j(a) \;=\; \Pr(X_j^a = 1).
38	\]
39	The \emph{panel ASR} under attack $a$ is
40	\[
41	    \mathrm{ASR}(\mathcal{P}, a) \;=\; \Pr\!\Bigl(\textstyle\sum_{j=1}^K X_j^a \;\geq\; t\Bigr).
42	\]
43	\end{definition}
44	
45	\begin{definition}[Adaptive Adversary]
46	\label{def:adversary}
47	An \emph{adaptive adversary} has full knowledge of the panel composition $\ma
…[truncated 20455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T15:13:02.028518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T15:13:02.028700+00:00_

1	\section{Threat Model and Problem Formulation}
2	% [PLACEHOLDER — to be written by Worker]
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T15:13:02.028919+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex",
  "content": "\\section{Threat Model and Problem Formulation}\n\nA \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \\lceil K/2 \\rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised independently with probability $\\eta_j(a) = \\Pr(X_j^a = 1)$, where $X_j^a \\in \\{0,1\\}$ denotes the failure indicator. We write $\\eta_{\\max} = \\max_j \\eta_j$ for the vulnerability of the weakest judge. The \\emph{panel attack success rate} is $\\mathrm{ASR}(\\mathcal{P}, a) = \\Pr\\!\\bigl(\\sum_{j=1}^K X_j^a \\geq t\\bigr)$.\n\nTo quantify diversity, we derive the \\emph{effective independence} $K_{\\mathrm{eff}}$ from the eigenspectrum of the pairwise mutual-information matrix $\\mathbf{M}$ among judges. Let $\\lambda_1, \\ldots, \\lambda_K$ be the eigenvalues of $\\mathbf{M}$; then $K_{\\mathrm{eff}} = (\\sum_i \\lambda_i)^2 / \\sum_i \\lambda_i^2$. This quantity ranges from $K_{\\mathrm{eff}} = K$ (fully independent judges) to $K_{\\mathrm{eff}} = 1$ (perfectly correlated judges). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\\eta_{\\mathrm{joint}} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$, suggesting that diversity should help---but this bound assumes non-adaptive faults.\n\n\\begin{definition}[Adaptive Adversary]\n\\label{def:adversary}\nAn \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$ to maximize the panel ASR, yielding $\\mathrm{ASR}^*(\\mathcal{P}) = \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$.\n\\end{definition}\n\nThis departs from Byzantine fault-tolerance (BFT) models~\\cite{lamport1982byzantine,castro1999practical}, which assume faults are independent and randomly distributed. An adaptive adversary instead concentrates attack effort on the weakest link~\\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.\n\n\\begin{theorem}[Weakest-Link Monotonicity]\n\\label{thm:monotonicity}\nLet $\\mathcal{P}$ and $\\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$.\n\\end{theorem}\n\n\\noindent Proof in Appendix~\\ref{app:proof}. Intuitively, the replaced judge is \\emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n\nThe theorem yields a testable prediction: in a regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, we should observe $\\beta_1 > 0$ (significant) while $\\beta_2 \\approx 0$ (non-significant), since monotonicity is established in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$. Our experiments in \\S\\ref{sec:experiments} directly test this prediction across 12 conditions spanning two benchmarks and six attack types.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex",
    "content": "\\section{Threat Model and Problem Formulation}\n\nA \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \\lceil K/2 \\rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised independently with probability $\\eta_j(a) = \\Pr(X_j^a = 1)$, where $X_j^a \\in \\{0,1\\}$ denotes the failure indicator. We write $\\eta_{\\max} = \\max_j \\eta_j$ for the vulnerability of the weakest judge. The \\emph{panel attack success rate} is $\\mathrm{ASR}(\\mathcal{P}, a) = \\Pr\\!\\bigl(\\sum_{j=1}^K X_j^a \\geq t\\bigr)$.\n\nTo quantify diversity, we derive the \\emph{effective independence} $K_{\\mathrm{eff}}$ from the eigenspectrum of the pairwise mutual-information matrix $\\mathbf{M}$ among judges. Let $\\lambda_1, \\ldots, \\lambda_K$ be the eigenvalues of $\\mathbf{M}$; then $K_{\\mathrm{eff}} = (\\sum_i \\lambda_i)^2 / \\sum_i \\lambda_i^2$. This quantity ranges from $K_{\\mathrm{eff}} = K$ (fully independent judges) to $K_{\\mathrm{eff}} = 1$ (perfectly correlated judges). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\\eta_{\\mathrm{joint}} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$, suggesting that diversity should help---but this bound assumes non-adaptive faults.\n\n\\begin{definition}[Adaptive Adversary]\n\\label{def:adversary}\nAn \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$ to maximize the panel ASR, yielding $\\mathrm{ASR}^*(\\mathcal{P}) = \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$.\n\\end{definition}\n\nThis departs from Byzantine fault-tolerance (BFT) models~\\cite{lamport1982byzantine,castro1999practical}, which assume faults are independent and randomly distributed. An adaptive adversary instead concentrates attack effort on the weakest link~\\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.\n\n\\begin{theorem}[Weakest-Link Monotonicity]\n\\label{thm:monotonicity}\nLet $\\mathcal{P}$ and $\\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$.\n\\end{theorem}\n\n\\noindent Proof in Appendix~\\ref{app:proof}. Intuitively, the replaced judge is \\emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n\nThe theorem yields a testable prediction: in a regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, we should observe $\\beta_1 > 0$ (significant) while $\\beta_2 \\approx 0$ (non-significant), since monotonicity is established in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$. Our experiments in \\S\\ref{sec:experiments} directly test this prediction across 12 conditions spanning two benchmarks and six attack types.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T15:13:02.029143+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_threat_model_20260522T151212",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-22T15:13:02.029312+00:00_

已写入 `docs/paper/threat_model.tex`。~470 词，覆盖全部 5 个段落：panel/majority-vote 设置、$K_{\mathrm{eff}}$ 定义与 SDPI bound、adaptive adversary definition 环境（含 BFT 对比）、weakest-link monotonicity theorem（标签 `thm:monotonicity`，证明留 appendix，含 pivotal voter 直觉）、testable prediction 连接实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_threat_model_20260522T151212"
}
```

</details>

---
