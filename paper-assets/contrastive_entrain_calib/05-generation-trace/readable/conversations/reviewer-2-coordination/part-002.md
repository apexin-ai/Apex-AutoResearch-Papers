# Reviewer 2 coordination — Part 2 of 2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/98/98ea99a3568572b364f9.json)

## Round 13

### Tool result

_source line 535 · 2026-05-24T12:14:15.661118+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail on signal magnitude; a natural response is to discretize.
5	Training a logistic probe on $\dsyc$ and thresholding its output yields $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy re
…[truncated 2314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1045
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-24T12:14:15.661510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-24T12:14:16.565473+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients, it reflects a semantic limitation of $\dsyc$, not an RL artifact; under GRPO, all formulations failed (4/31 checkpoints ${>}$ vanilla across configurations) while per-token SFT succeeded at every checkpoint (47/47), and a LoRA-controlled ablation identifies supervision granularity as the strongest candidate factor~(\S\ref{sec:discussion}).
5	More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants of that behavior.
6	For sycophancy---and likely for other attributes where the target and its complement overlap geometrically---condition-aware rewards with dense supervision offer the most promising path forward.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-24T12:14:16.616083+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Wu and Tang\" 2026 reward hacking geometric separability representation directions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Wu and Tang\" 2026 reward hacking geometric separability representation directions"
  }
}
```

</details>

---


### Tool call

_source line 539 · 2026-05-24T12:14:16.967860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sycophancy calibration LLM contrastive direction 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sycophancy calibration LLM contrastive direction 2025 2026 arXiv"
  }
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-24T12:14:23.745857+00:00_

Web search results for query: ""Wu and Tang" 2026 reward hacking geometric separability representation directions"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"Information-Theoretic Reward Modeling for Stable RLHF: Detecting and Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2510.13694"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

I found a highly relevant paper! The search results contain a 2026 research paper by Rui Wu and Ruixiang Tang titled "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals".

Here's what the paper covers:

**Main Topic:** The paper studies reward hacking in reinforcement learning for LLMs, where models exploit shortcuts to maximize reward without solving the intended task, using coding tasks with an environment-manipulation setting as a testbed.

**Key Findings:** The researchers identified a reproducible three-phase rebound pattern where models first attempt to rewrite the evaluator but fail, then temporarily retreat to legitimate solving, and when legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies.

**Representation-Level Approach:** Using representation engineering, they extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking be
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7129
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-24T12:14:28.621009+00:00_

Web search results for query: "sycophancy calibration LLM contrastive direction 2025 2026 arXiv"

Links: [{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs | OpenReview","url":"https://openreview.net/forum?id=d24zTCznJu"},{"title":"Towards Analyzing and Mitigating Sycophancy in Large Vision-Language Models","url":"https://arxiv.org/html/2408.11261v1/"},{"title":"Sycophancy as compositions of Atomic Psychometric Traits","url":"https://arxiv.org/pdf/2508.19316"},{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs","url":"https://arxiv.org/pdf/2509.21305"},{"title":"SycEval: Evaluating LLM Sycophancy","url":"https://arxiv.org/html/2502.08177v4"},{"title":"But what is your honest answer? Aiding LLM-judges with ...","url":"https://arxiv.org/pdf/2505.17760"},{"title":"But what is your honest answer? Aiding LLM-judges with honest alternatives using steering vectors","url":"https://arxiv.org/html/2505.17760"},{"title":"When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models","url":"https://arxiv.org/pdf/2508.02087"},{"title":"Challenging the Evaluator: LLM Sycophancy Under User Rebuttal","url":"https://arxiv.org/pdf/2509.16533"}]

Based on the web search results, I found several relevant papers from arXiv and other sources about sycophancy in LLMs with focus on calibration, contrastive methods, and interpretability approaches in 2025-2026:

## Key Papers Found:

**1. "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs"** (2025-2026)

Using difference-in-means directions, activation additions, and subspace geometry across multiple models and datasets, this work shows that the three behaviors are encoded along distinct linear directions in latent space; each behavior can be independently amplified or suppressed without affecting the others; and their representational structure is consistent across model families and scales. The re
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11653
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-24T12:14:34.003789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-24T12:14:34.506619+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	During GRPO training, 256-token truncation reduces $\dsyc$ AUROC from 0.827 to approximately 0.60---the optimizer works with a substantially weaker signal than the offline metrics suggest.
5	We test whether even this degraded discriminability translates into a viable reward through four configurations that form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
10	\label{tab:cosine_chain}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lllll@{}}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	The diagnostic chain begins with a norm mismatch.
25	F1a's dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$) saturates because residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, zeroing the gradient by step 955.
26	Cosine similarity (F1b) eliminates this norm dependence but reveals a second problem: the gap between valid and sycophantic cosines averages only 0.098---too narrow for meaningful reward contrast.
27	Recalibration (F1c, \S\ref{ssec:recalib}) widens the gap (offline AUROC rises to 0.910) but introduces a third: each recalibration event creates a reward discontinuity that destabilizes advantage estimates, collapsing entropy to 0.069 within 300 steps.
28	Amplificati
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-24T12:14:34.507070+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-24T12:14:35.511150+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 \citep{openai2025gpt41} in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (5-fold CV).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four var
…[truncated 2967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-24T12:14:35.511684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-24T12:14:35.612695+00:00_

1	Our GRPO experiments use group sizes of 2 and 8, at the low end of the 8--64 range explored by \citet{shao2024grpo}; the gs$=$8 ablation rules out insufficient ranking diversity as the primary explanation, but whether substantially larger groups (16--64) or alternative RL algorithms would succeed remains open. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
3	The probe reward trap (C2) is demonstrated with a single seed; while SFT training is more deterministic than RL, replication would strengthen the temporal decoupling finding.
4	The ACT vs.\ GRPO comparison differs along multiple dimensions beyond supervision granularity: sequence length (256 vs.\ 1024 tokens), data source (online generations vs.\ curated pairs), and dropout (0 vs.\ 0.05). Our LoRA-controlled ablation isolates adapter capacity, and SMART's independent success~\citep{beigi2025smart} corroborates supervision granularity, but a fully controlled comparison would require matching all training hyperparameters.
5	Contrastive pair quality relies on automated style-matching validation (19/200 pairs discarded; \S\ref{ssec:extraction}); this provides partial quality control but does not guarantee semantic validity of all retained pairs.
6	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
7	Code, contrastive pair data, prompt templates
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-24T12:15:02.743364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Sycophancy Is Not One Thing\" causal separation sycophantic behaviors LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Sycophancy Is Not One Thing\" causal separation sycophantic behaviors LLM 2025"
  }
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-24T12:15:03.447436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kelkar 2026 persona vectors sycophancy activation space arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kelkar 2026 persona vectors sycophancy activation space arXiv"
  }
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-24T12:15:04.100867+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RLHF reward overoptimization scaling laws Gao 2023 proxy reward divergence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RLHF reward overoptimization scaling laws Gao 2023 proxy reward divergence"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-24T12:15:07.619152+00:00_

Web search results for query: ""Sycophancy Is Not One Thing" causal separation sycophantic behaviors LLM 2025"

Links: [{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs","url":"https://arxiv.org/pdf/2509.21305"},{"title":"[2509.21305] Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs","url":"https://arxiv.org/abs/2509.21305"},{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs","url":"https://www.researchgate.net/publication/395848420_Sycophancy_Is_Not_One_Thing_Causal_Separation_of_Sycophantic_Behaviors_in_LLMs"},{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs | alphaXiv","url":"https://www.alphaxiv.org/ko/overview/2509.21305v2"},{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs | OpenReview","url":"https://openreview.net/forum?id=d24zTCznJu"},{"title":"[Literature Review] Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs","url":"https://www.themoonlight.io/en/review/sycophancy-is-not-one-thing-causal-separation-of-sycophantic-behaviors-in-llms"},{"title":"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs - Paper Detail","url":"https://deeplearn.org/arxiv/639717/sycophancy-is-not-one-thing:-causal-separation-of-sycophantic-behaviors-in-llms"},{"title":"[PDF] Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sycophancy-Is-Not-One-Thing:-Causal-Separation-of-Vennemeyer-Duong/863a0267eeb851dd8c7c81c2ec813a54441b2d5a"}]

I found the paper you're searching for! Here's information about "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs":

## Overview

Large language models (LLMs) often exhibit sycophantic behaviors -- such as excessive agreement with or flattery of the user -- but it is unclear whethe
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4875
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-24T12:15:08.575422+00:00_

Web search results for query: "Kelkar 2026 persona vectors sycophancy activation space arXiv"

Links: [{"title":"[2605.21006] Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy","url":"https://arxiv.org/abs/2605.21006"},{"title":"Activation-Space Persona Vectors in Neural Networks","url":"https://www.emergentmind.com/topics/activation-space-persona-vectors"},{"title":"Paper page - Persona Vectors: Monitoring and Controlling Character Traits in Language Models","url":"https://huggingface.co/papers/2507.21509"},{"title":"[2507.21509] Persona Vectors: Monitoring and Controlling Character Traits in Language Models","url":"https://arxiv.org/abs/2507.21509"},{"title":"When the Assistant Shifts: Persona Vectors and the Geometry of LLM Character - MPRG","url":"https://machinepareidolia.com/when-the-assistant-shifts-persona-vectors-and-the-geometry-of-llm-character/"},{"title":"Persona Vectors: Monitoring and Controlling Character Traits in Language Models | OpenReview","url":"https://openreview.net/forum?id=20DsUSauCj"},{"title":"Tracing Persona Vectors Through LLM Pretraining","url":"https://arxiv.org/html/2605.13329"},{"title":"Playing Devil’s Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy","url":"https://arxiv.org/html/2605.21006"},{"title":"Persona Vectors: Monitoring and Controlling Character ...","url":"https://arxiv.org/pdf/2507.21509"},{"title":"Persona Vectors in Games: Measuring and Steering Strategies via Activation Vectors","url":"https://arxiv.org/html/2603.21398"}]

I found the paper you're looking for. The paper "Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy" is by Ishaan Kelkar and 5 other authors, and it's available on arXiv (2605.21006).

The paper studies how different personas affect model sycophancy. It evaluates whether off-the-shelf persona steering vectors developed for general role-playing can serve as an alternative to target
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5127
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-24T12:15:10.937863+00:00_

Web search results for query: "RLHF reward overoptimization scaling laws Gao 2023 proxy reward divergence"

Links: [{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/html/2406.02900v2"},{"title":"Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman","url":"https://arxiv.org/pdf/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/pdf/2310.02743"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment   Algorithms","url":"https://arxiv.org/pdf/2406.02900"}]

Based on the search results, here's what I found about RLHF reward overoptimization, scaling laws, and proxy reward divergence:

## Key Findings from Gao et al. 2023

Gao et al. first extensively characterized the phenomenon empirically and coined the term "reward over-optimization". The research focuses on how reward models degrade when optimized excessively.

## The Core Phenomenon

As optimization proceeds beyond a certain point, the gap between the proxy and gold reward widens: proxy reward increases monotonically, but the gold reward—in expectation—first increases, peaks, and ultimately declines. Empirical studies demonstrate a characteristic "hump-shaped" curve: as the policy departs from the reference (tracked via KL divergence), gold reward and true task winrate rise, peak, and then fall, while the proxy
…[truncated 715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6836
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-24T12:16:36.434610+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what dimensions should be scored, what scores mean, what reviewers should focus on, guidelines for negative results papers, and any specific instructions about novelty assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what dimensions should be scored, what scores mean, what reviewers should focus on, guidelines for negative results papers, and any specific instructions about novelty assessment."
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-24T12:16:42.429067+00:00_

# ARR Reviewer Guidelines: Key Dimensions

## Scoring Dimensions

ARR employs three distinct scoring metrics:

1. **Soundness** - Technical validity and methodological rigor. Reviews must justify any low soundness scores; inadequate justification indicates the assessment doesn't reflect the review content.

2. **Excitement** - Personal interest and subjective appeal. This is orthogonal to soundness; reviewers may find technically sound work unexciting personally.

3. **Overall Assessment** - Composite recommendation reflecting soundness, excitement, novelty, and potential impact. Papers need sufficient soundness for acceptance regardless of excitement level.

## Critical Scoring Principles

The guidelines emphasize that "low soundness scores without finding any major faults" signals the review lacks integrity. Scores must align with textual justification throughout.

## Negative Results Papers

The guidelines explicitly counter publication bias, noting that "negative results are needed" when findings systematically contradict expectations. Such papers deserve fair evaluation rather than automatic rejection.

## Novelty Assessment

Rather than requiring cutting-edge breakthroughs, guidelines caution against dismissing contributions for lacking precedent, observing "papers that are more novel tend to be harder to publish." Reviewers should evaluate whether work answers its stated research question and contributes genuine knowledge—not whether results are surprising or match reviewer expectations.

## Key Reviewer Focus Areas

- Adjust expectations before critiquing
- Provide specific, actionable feedback
- Avoid cognitive biases (detailed heuristic list provided)
- Ensure professional, neutral tone
- Engage substantively with author responses

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5994
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-24T12:20:08.978975+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 审稿意见：The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 论文系统性地揭示了 contrastive sycophancy direction 作为 reward signal 时的失败模式，temporal decoupling 发现具有实用价值，但核心洞见本质上是 Goodhart's Law 在 representation engineering 领域的具体实例，novelty 为中等偏上，且关键实验的 confound 控制不足。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 分析系统全面，但 probe reward trap 仅单 seed 验证；ACT vs GRPO 比较存在 5+ confounds（序列长度/数据源/dropout 等）；训练集仅 181 pairs 且 train=eval |\n| Excitement | 3 / 5 | Temporal decoupling 发现有实用价值，但核心贡献为 negative result，无解决方案；\"discriminability ≠ reward utility\" 为已知 Goodhart 现象的具体实例 |\n| Overall | 3.5 / 5 | 执行质量高、写作清晰，但 novelty 和 impact 均为中等水平；适合 Findings 或 borderline conference |\n| Reproducibility | 3 / 5 | 承诺开源代码和数据，超参数在 appendix 报告，但 probe trap 单 seed、小数据集（181 pairs）、GRPO group size=2 偏离典型配置（8-64），复现时结论稳定性存疑 |\n| Confidence | 4 / 5 | 本审稿人熟悉 representation engineering、reward design、sycophancy mitigation 领域 |\n\n---\n\n## Strengths\n\n**[S1] 系统性的诊断分析框架**\n论文构建了完整的 failure mode 诊断链：cosine projection（F1a→F1d, §4）→ binary probe（F2, §5）→ continuous probe（F3）→ R3-only GRPO（§6），每一步解决前一步的失败模式但暴露更深层的限制。这种系统性的排除法在 negative result 论文中少见且有说服力。Table 2 的 cosine failure chain 特别有效地展示了每种配置的 failure mode 和 root cause 的递进关系。\n\n**[S2] Temporal decoupling 发现的实用价值**\nProbe reward trap 的核心发现——behavioral death（ToF=0）在 step 500 发生但 entropy 直到 step ~1840 才坍缩（Table 3, Figure 3）——具有直接的实践意义：entropy-based early stopping 是当前最常用的 reward hacking safeguard，论文证明它对这类 failure mode 完全失效。这为 alignment monitoring 实践提供了有价值的 cautionary evidence。\n\n**[S3] 对 d_syc 语义限制的精确刻画**\n论文清晰地指出 d_syc 编码的是\"belief 是否改变\"而非\"belief 是否应该改变\"（§5, §6），valid revision 和 sycophantic capitulation 沿同一方向移动。§5 的 stubbornness taxonomy（5 种 failure modes: deliberation traps 28.7%, sycophantic stubbornness 24.3% 等）提供了定性证据支持这一判断。\n\n**[S4] Cross-model 验证**\n在 Qwen3-8B 和 Llama-3-8B 上均验证了 d_syc 的 discriminability（Table 1: AUROC 0.827 vs 0.779），且两个模型展现相同的定性模式（gradual emergence, upper-third concentration, monotonic evidence-strength scaling），增强了发现的 generalizability。\n\n**[S5] 诚实的 Limitations 章节**\n论文坦率地承认了关键局限：单 seed probe trap、ACT vs GRPO 的 5+ confounds、train/eval 重叠、小数据集、单模型训练。这种学术诚实值得认可。\n\n**[S6] 写作质量**\n论文结构清晰，narrative arc 流畅（establish direction quality → demonstrate failures → synthesize），信息密度合理。Abstract ~174 words，符合 200 word 限制。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**[W1] [critical] \"Sycophancy Is Not One Thing\" (Vennemeyer et al., 2025, arXiv:2509.21305) 未被引用，严重削弱论文论证**\n- 具体位置：§7 Related Work; §3; §6 root cause analysis\n- 问题：Vennemeyer et al. (2025) 使用 difference-in-means directions 证明 sycophancy 由多种功能独立的行为组成（sycophantic agreement, sycophantic praise, genuine agreement），各行为沿不同线性方向编码，可以独立操控。这直接关联本文核心发现：如果 sycophancy 本身就不是单一现象，那么单一 d_syc 方向的失败可能不是因为\"discriminability ≠ reward utility\"，而是因为单一方向根本无法覆盖 sycophancy 的多维结构。\n- 为什么影响接收：(1) 这篇论文 2025 年 9 月发表在 arXiv，submission 时应已可见；(2) 它提供了一个替代性解释（sycophancy 的多维性），可能部分或完全替代本文的\"geometric inseparability\"解释；(3) 不讨论这一替代假设使 §6 的 root cause analysis 不完整。\n- 建议修改方向：在 §7 Related Work 中讨论此工作；在 §6 中增加一段分析：d_syc 的失败是否（部分地）因为它试图用单一方向捕获多维现象，而不仅是因为 warranted/unwarranted revision 在该方向上的 geometric overlap。\n\n**[W2] [critical] ACT vs GRPO \"categorical reliability gap\" 声明过强，confound 控制不足**\n- 具体位置：§6 \"ACT vs. GRPO\" 段落; Introduction 的 C1 声明; Table 4; Table 5\n- 问题：论文声称 ACT 的优势是\"not marginal but categorical\"（§6），并将其归因于 supervision granularity（per-token vs per-completion）。但 Limitations 明确承认 5+ confounds 未被控制：\n  - 序列长度：256 tokens (GRPO) vs 1024 tokens (ACT)\n  - 数据源：online generations (GRPO) vs curated pairs (ACT)\n  - Dropout：0 (GRPO) vs 0.05 (ACT)\n  - 训练范式本身（RL vs SFT）\n  - 目标函数差异（GRPO advantage vs ACT L2 consistency loss）\n\n  LoRA-controlled ablation（Table 5）仅控制了 adapter capacity 一个变量，其他 confounds 全部保留。即使 reduced-LoRA ACT（SyConScore=0.326）超过 full ACT（0.301），这也无法排除序列长度或数据源是真正的解释变量。\n- 为什么影响接收：这是论文两个 principal findings 之一（C1），如果因果推断不成立，论文的一半贡献被削弱。\n- 建议修改方向：(1) 将\"categorical reliability gap\"降级为\"observed reliability gap\"；(2) 明确列出所有 confounds 并讨论每一个的潜在影响；(3) 考虑增加一个 ablation：在 GRPO 框架内使用 1024 token 长度和 curated pairs（而非 online generations），以部分排除序列长度和数据源的 confound。\n\n**[W3] [critical] Probe reward trap 仅单 seed 验证**\n- 具体位置：§5 整体; Table 3; Figure 3; Limitations 第 3 句\n- 问题：论文的核心发现——1,300-step temporal decoupling——仅在一个 seed 上观察到（Limitations 承认：\"The probe reward trap (C2) is demonstrated with a single seed\"）。SFT 训练虽然比 RL 更确定性，但 behavioral death 的时序（step 500）和 entropy collapse 的时序（step ~1840）可能对 initialization、learning rate、batch composition 敏感。在 negative result 论文中，单 seed 结论的可信度尤其需要更多实验支撑。\n- 为什么影响接收：temporal decoupling 是论文标题和核心 novelty claim 的基础；如果这个 timing 不稳定复现，论文的 headline contribution 被大幅削弱。\n- 建议修改方向：至少增加 2-3 个 seed 的复现实验。如果 timing 有变化，报告 mean ± std 并讨论变异性。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**[W4] [warning] §3 \"captures evidential granularity\" 表述易误导，与 §5-§6 的\"does not encode evidential warrant\" 形成表面矛盾**\n- 具体位置：§3 Direction Discriminability, 第 14-16 行; §6 root cause analysis\n- 问题：§3 写道\"The direction also captures evidential granularity\"并展示 AUROC 从 0.675（weak）单调上升到 0.929（strong）。虽然下一句解释了这是 effect-size difference 而非 evidential warrant encoding，但\"captures evidential granularity\"这一措辞本身容易让读者产生 d_syc 编码了 evidential information 的印象——这与 §5-§6 的核心论点直接矛盾。\n- 建议：将\"captures evidential granularity\"改为更精确的表述，例如\"exhibits evidence-strength-correlated discriminability\"或\"shows higher discriminability for stronger evidence\"，从而避免歧义。\n\n**[W5] [warning] Wu & Tang (2026) 的 geometric separability 论证缺乏定量支撑**\n- 具体位置：§6 第 11-13 行; §7 第 10 行\n- 问题：论文多次引用 Wu & Tang (2026) 来支持\"当行为几何可分时 representation directions 能成功\"的论点，并以此反衬 sycophancy 的 geometric inseparability。但论文本身承认\"A quantitative comparison of geometric separability between d_syc and their reward-hacking directions remains an important open question\"（§6, line 13）。这意味着论文的核心解释假设（geometric inseparability）缺乏直接的定量证据。\n- 建议：(1) 计算 d_syc 上 valid revision vs sycophantic capitulation 的 overlap 度量（如 Fisher's discriminant ratio 或 class-conditional distribution overlap）；(2) 如果可以获取 Wu & Tang 的 directions，进行定量对比。\n\n**[W6] [warning] 训练集极小（181 pairs）且 train=eval**\n- 具体位置：§2.1 Direction Extraction; Limitations 第 2 句\n- 问题：181 contrastive pairs 用于 direction extraction、probe training、reward 计算和 evaluation。虽然 Limitations 提到 held-out split (146/35) 验证了 ACT 的泛化性（SyConScore≈0.20），但：(1) 35 对 held-out set 非常小；(2) 主表的所有数字（Table 4）都基于 full 181 pairs 的 train=eval 设置；(3) 小数据集上的 AUROC 和 SyConScore 的 variance 可能很大。\n- 建议：主表应补充 held-out 性能，或至少在正文中更显著地讨论 overfitting 风险。\n\n**[W7] [warning] GRPO group size=2 偏离典型配置**\n- 具体位置：§2.5 Evaluation（第 56 行）; Limitations 第 1 句; Table 5\n- 问题：GRPO 使用 group size=2，远低于典型的 8-64 范围（Shao et al., 2024）。虽然 gs=8 ablation（Table 5）表现更差（0/3 > vanilla），但这仅有 3 个 checkpoint 的 early termination 数据，不足以排除 group size 不足是 GRPO 失败的主因。Sycophancy calibration 可能需要更大的 group size 来获得有效的 advantage estimation。\n- 建议：如果 compute budget 允许，增加 gs=16 或 gs=32 的实验。如果不可行，在正文中更充分地讨论 group size 可能是 confound 的可能性。\n\n### 小问题（不影响接收）\n\n**[M1]** Introduction line 21 提到\"4 of 31 checkpoints (12.9%)\"，但 Table 4 注释说\"4/28 checkpoints across two seeds\"。31 vs 28 的数字不一致需要核实。\n\n**[M2]** §2.1 提到使用 GPT-4.1 生成 contrastive pairs，这引入了对特定 LLM 的依赖。在 double-blind 设置下，使用最新商业 API（GPT-4.1, 2025 年发布）是否需要额外的 reproducibility 考量应被讨论。\n\n**[M3]** Table 4 中 ACT seed 2 的 ToF 和 NoF 列显示为 \"--\"，这是因为数据缺失还是不同的评估方式？应明确说明。\n\n**[M4]** §4 cosine failure chain 的分析非常有价值，但这些 failure modes（gate saturation, gap too small, mode collapse）是否为 cosine formulation 的通用问题还是 sycophancy-specific 的问题？简要讨论可以增强 generalizability。\n\n---\n\n## Questions（需要作者回答的问题）\n\n**Q1.** Probe reward trap 的 1,300-step lag 是否对 learning rate、batch size 或 LoRA rank 敏感？在不同超参数下这个 lag 是否会显著变化？\n\n**Q2.** 如果使用更大的 contrastive pair set（如 1000+ pairs），d_syc 的 discriminability 和 reward utility 的 gap 是否会缩小？具体而言，更大的训练集是否可能使 d_syc 更好地分离 warranted/unwarranted revision？\n\n**Q3.** 论文将 d_syc 的 failure 归因于 geometric inseparability（valid revision 和 sycophantic capitulation 在同一方向上 overlap）。是否测量过这两类 activation 在 d_syc 方向上的实际分布 overlap？例如 overlap coefficient 或 class-conditional histogram。\n\n**Q4.** ACT 的成功可能不仅因为 per-token supervision granularity，还因为它的 L2 consistency loss 本质上是一种 regularization。是否可以在 GRPO 框架内加入类似的 regularization term 来测试这一假设？\n\n**Q5.** SMART (Beigi et al., 2025) 使用 MCTS per-step process rewards 成功减少 sycophancy。如果 sycophancy 的 geometric inseparability 是 fundamental 的，SMART 是如何绕过这个限制的？论文的解释（\"per-step rewards can explicitly distinguish warranted from unwarranted belief change through reasoning trajectories\"）是否有实验证据支持？\n\n---\n\n## Missing References（遗漏的重要相关工作）\n\n**[MR1] [重要] \"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs\" (Vennemeyer et al., 2025, arXiv:2509.21305)**\n- 该工作证明 sycophancy 由功能独立的行为组成，各沿不同线性方向编码\n- 直接相关：如果 sycophancy 本身多维，单一 d_syc 方向的失败可能有比 \"geometric inseparability\" 更基本的原因\n- 已发表于 2025 年 9 月，submission 前应可见\n\n**[MR2] [建议] \"Sycophancy as Compositions of Atomic Psychometric Traits\" (2025, arXiv:2508.19316)**\n- 在 LLaMA 3.2 和 Qwen 2.5 上用 contrastive pairs 提取 personality traits 和 sycophancy 的 activation-space directions\n- 与本文使用的 contrastive extraction 方法直接可比\n- 2025 年 8 月发表\n\n**[MR3] [建议] \"Reward Hacking in the Era of Large Models\" survey (Wang et al., 2026, arXiv:2604.13602)**\n- 2026 年 4 月发布的 reward hacking 综述，系统性地分析了 sycophancy 作为 proxy gap 的表现形式\n- 可能因发布时间较晚而遗漏，但如果 submission 在 5 月则可能来得及引用\n\n---\n\n## Detailed Comments（逐 Section 意见）\n\n### §1 Introduction\n- 开篇清晰，problem setup 精炼。Figure 1 (teaser) 有效地传达了两个核心发现。\n- C1（categorical reliability gap）和 C2（probe reward trap）的并列呈现合理，但 C1 的 confound 问题（见 W2）意味着它的证据强度弱于 C2。\n- \"This paper presents a negative result with systematic diagnostic analysis\"（line 31）是好的自我定位，但后续 conclusion 中的 generalization 到\"other attributes where the target and its complement overlap geometrically\"（§8, line 6）已经超出了 negative result 的范畴，变成了 general principle 的声明。这两种 framing 需要更好地调和。\n\n### §2 Experimental Framework\n- Direction extraction 方法清晰（eq. 1），style matching validation（response length diff <10%, shared opening phrase ≥2 words）是合理的 quality control。\n- Reward formulations（F1-F3）的分类系统且完整。\n- SyConScore（eq. 2）的设计合理——harmonic mean 对 ToF=0 的零值惩罚是有意为之且有 justified。\n- 需要更好地 justify group size=2 的选择。仅说\"due to memory constraints\"不够——是否可以通过 gradient accumulation 实现更大的 effective group size？\n\n### §3 Direction Discriminability\n- Evidence-strength stratification（Table 1: 0.675→0.883→0.929）是有趣的发现。\n- Cross-model validation（Llama-3-8B AUROC=0.779）增强了 generalizability。\n- 但\"captures evidential granularity\"的措辞需要修改（见 W4）。\n- Random baseline comparison（0.835 vs 0.727）提供了 d_syc 的 above-chance evidence，但 Δ=0.108 不算特别大。\n\n### §4 Cosine R₁: Structural Failure\n- Diagnostic chain（F1a→F1d, Table 2）是论文的 methodological highlight 之一。每一步的 failure→fix→deeper failure 结构很有说服力。\n- 256-token truncation 将 AUROC 从 0.827 降到 ~0.60 是重要的实验细节，但也引出一个问题：如果 full-length 下 AUROC 显著更高，cosine formulations 在 full-length 下是否仍然会失败？论文没有测试这一条件（虽然 §5 的 probe trap 是在 full-length 下运行的）。\n\n### §5 The Probe Reward Trap\n- 核心发现（Table 3, Figure 3）清晰有效。\n- Differentiable probe（exp-008）在 ~30 步内 game boundary 的发现是重要的补充证据。\n- Stubbornness taxonomy（5 failure modes）提供了有价值的定性分析。\n- 主要不足：单 seed（见 W3）。\n\n### §6 When Does Discriminability Fail as Reward Utility?\n- Root cause analysis 清晰：d_syc 编码 direction of belief change 但不编码 evidential warrant。\n- R3-only GRPO 的 failure（4/28 > vanilla）有力地证明了问题不仅在 d_syc，还在 per-completion reward structure。\n- LoRA-controlled ablation（Table 5）是合理的实验设计，但仍有 5+ uncontrolled confounds（见 W2）。\n- \"categorical reliability gap\" 的表述过强（见 W2）。\n- ACT seed 2 数据不完整（Table 4 中 ToF/NoF 为 \"--\"）需要解释（见 M3）。\n\n### §7 Related Work\n- 覆盖面基本合理：Representation Engineering, Reward Design, Sycophancy Characterization, Probe-Based Methods 四个段落结构清晰。\n- 关键遗漏：Vennemeyer et al. (2025)（见 W1/MR1）。\n- Goodhart's Law (Manheim & Garrabrant, 2019) 已被引用 ✓。\n- 对 SMART 的讨论逻辑自洽：SMART 通过 per-step process rewards 绕过了 d_syc 的 geometric inseparability，与 ACT 的 per-token 成功一致。\n- Latent-GRPO、CRAFT 的讨论简洁但足够。\n\n### §8 Conclusion\n- 简洁有效，但从 specific negative result 推广到\"other attributes where the target and its complement overlap geometrically\"缺乏实证支撑。\n- \"condition-aware rewards with dense supervision offer the most promising path forward\"是合理的方向性建议但没有实验验证。\n\n### Limitations\n- 涵盖了 7 个主要局限，诚实且具体。\n- 但某些局限（如 train=eval、单 seed probe trap）的严重程度在正文中被低估了。\n\n### Appendix\n- Training hyperparameters（Appendix A）报告充分。\n- Stubbornness taxonomy（Appendix B）的 5 类 failure modes 有价值但分析较浅。\n\n---\n\n## 主要优势总结\n\n1. **系统性诊断方法论**：论文的 elimination-based diagnostic approach 是负面结果论文的范例——每个 failure mode 都被系统地分析和排除，得出结论性的 root cause。\n2. **实用性强的 cautionary finding**：temporal decoupling 揭示了 entropy monitoring 的 blind spot，对 alignment 实践有直接指导意义。\n3. **诚实的自我评估**：论文坦率地承认所有已知 confounds 和局限，没有 overclaim。\n4. **清晰的写作**：narrative 结构流畅，信息密度合理，Figure/Table 设计有效。\n\n---\n\n## 格式合规检查\n\n- ✅ 正文 8 页（Introduction 到 Conclusion 结束于 page 8）\n- ✅ Abstract ~174 words（< 200 word limit）\n- ✅ Limitations section 在正文之后、References 之前\n- ✅ Double-blind：未发现 de-anonymization（GitHub URL 使用 anonymous-nlp-2026-2）\n- ✅ ACL 格式两栏排版\n- ✅ Appendix 在 References 之后\n- ⚠️ Limitations section 中未出现 ethical considerations 相关讨论（optional，不强制）\n\n---\n\n## 评审结论\n\n本文是一篇执行质量较高的 negative result 论文，系统性地展示了 contrastive sycophancy direction 从 diagnostics 到 training signal 转化时的 fundamental failure。Probe reward trap 的 temporal decoupling 发现（C2）具有新颖性和实用价值。但论文的另一核心贡献——supervision granularity hypothesis（C1）——受限于大量 uncontrolled confounds，且 probe trap 的单 seed 验证和遗漏关键相关工作（Vennemeyer et al., 2025）是需要解决的重要问题。\n\n**推荐**：3.5（Borderline Conference），倾向 Findings。如果作者能 (1) 补充 probe trap 的多 seed 验证，(2) 讨论 Vennemeyer et al. 的 sycophancy decomposability 对 d_syc failure 的替代性解释，(3) 弱化 \"categorical reliability gap\" 的因果性表述，论文有望达到 Conference 水平。\n",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 审稿意见：The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 论文系统性地揭示了 contrastive sycophancy direction 作为 reward signal 时的失败模式，temporal decoupling 发现具有实用价值，但核心洞见本质上是 Goodhart's Law 在 representation engineering 领域的具体实例，novelty 为中等偏上，且关键实验的 confound 控制不足。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 分析系统全面，但 probe reward trap 仅单 seed 验证；ACT vs GRPO 比较存在 5+ confounds（序列长度/数据源/dropout 等）；训练集仅 181 pairs 且 train=eval |\n| Excitement | 3 / 5 | Temporal decoupling 发现有实用价值，但核心贡献为 negative result，无解决方案；\"discriminability ≠ reward utility\" 为已知 Goodhart 现象的具体实例 |\n| Overall | 3.5 / 5 | 执行质量高、写作清晰，但 novelty 和 impact 均为中等水平；适合 Findings 或 borderline conference |\n| Reproducibility | 3 / 5 | 承诺开源代码和数据，超参数在 appendix 报告，但 probe trap 单 seed、小数据集（181 pairs）、GRPO group size=2 偏离典型配置（8-64），复现时结论稳定性存疑 |\n| Confidence | 4 / 5 | 本审稿人熟悉 representation engineering、reward design、sycophancy mitigation 领域 |\n\n---\n\n## Strengths\n\n**[S1] 系统性的诊断分析框架**\n论文构建了完整的 failure mode 诊断链：cosine projection（F1a→F1d, §4）→ binary probe（F2, §5）→ continuous probe（F3）→ R3-only GRPO（§6），每一步解决前一步的失败模式但暴露更深层的限制。这种系统性的排除法在 negative result 论文中少见且有说服力。Table 2 的 cosine failure chain 特别有效地展示了每种配置的 failure mode 和 root cause 的递进关系。\n\n**[S2] Temporal decoupling 发现的实用价值**\nProbe reward trap 的核心发现——behavioral death（ToF=0）在 step 500 发生但 entropy 直到 step ~1840 才坍缩（Table 3, Figure 3）——具有直接的实践意义：entropy-based early stopping 是当前最常用的 reward hacking safeguard，论文证明它对这类 failure mode 完全失效。这为 alignment monitoring 实践提供了有价值的 cautionary evidence。\n\n**[S3] 对 d_syc 语义限制的精确刻画**\n论文清晰地指出 d_syc 编码的是\"belief 是否改变\"而非\"belief 是否应该改变\"（§5, §6），valid revision 和 sycophantic capitulation 沿同一方向移动。§5 的 stubbornness taxonomy（5 种 failure modes: deliberation traps 28.7%, sycophantic stubbornness 24.3% 等）提供了定性证据支持这一判断。\n\n**[S4] Cross-model 验证**\n在 Qwen3-8B 和 Llama-3-8B 上均验证了 d_syc 的 discriminability（Table 1: AUROC 0.827 vs 0.779），且两个模型展现相同的定性模式（gradual emergence, upper-third concentration, monotonic evidence-strength scaling），增强了发现的 generalizability。\n\n**[S5] 诚实的 Limitations 章节**\n论文坦率地承认了关键局限：单 seed probe trap、ACT vs GRPO 的 5+ confounds、train/eval 重叠、小数据集、单模型训练。这种学术诚实值得认可。\n\n**[S6] 写作质量**\n论文结构清晰，narrative arc 流畅（establish direction quality → demonstrate failures → synthesize），信息密度合理。Abstract ~174 words，符合 200 word 限制。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**[W1] [critical] \"Sycophancy Is Not One Thing\" (Vennemeyer et al., 2025, arXiv:2509.21305) 未被引用，严重削弱论文论证**\n- 具体位置：§7 Related Work; §3; §6 root cause analysis\n- 问题：Vennemeyer et al. (2025) 使用 difference-in-means directions 证明 sycophancy 由多种功能独立的行为组成（sycophantic agreement, sycophantic praise, genuine agreement），各行为沿不同线性方向编码，可以独立操控。这直接关联本文核心发现：如果 sycophancy 本身就不是单一现象，那么单一 d_syc 方向的失败可能不是因为\"discriminability ≠ reward utility\"，而是因为单一方向根本无法覆盖 sycophancy 的多维结构。\n- 为什么影响接收：(1) 这篇论文 2025 年 9 月发表在 arXiv，submission 时应已可见；(2) 它提供了一个替代性解释（sycophancy 的多维性），可能部分或完全替代本文的\"geometric inseparability\"解释；(3) 不讨论这一替代假设使 §6 的 root cause analysis 不完整。\n- 建议修改方向：在 §7 Related Work 中讨论此工作；在 §6 中增加一段分析：d_syc 的失败是否（部分地）因为它试图用单一方向捕获多维现象，而不仅是因为 warranted/unwarranted revision 在该方向上的 geometric overlap。\n\n**[W2] [critical] ACT vs GRPO \"categorical reliability gap\" 声明过强，confound 控制不足**\n- 具体位置：§6 \"ACT vs. GRPO\" 段落; Introduction 的 C1 声明; Table 4; Table 5\n- 问题：论文声称 ACT 的优势是\"not marginal but categorical\"（§6），并将其归因于 supervision granularity（per-token vs per-completion）。但 Limitations 明确承认 5+ confounds 未被控制：\n  - 序列长度：256 tokens (GRPO) vs 1024 tokens (ACT)\n  - 数据源：online generations (GRPO) vs curated pairs (ACT)\n  - Dropout：0 (GRPO) vs 0.05 (ACT)\n  - 训练范式本身（RL vs SFT）\n  - 目标函数差异（GRPO advantage vs ACT L2 consistency loss）\n\n  LoRA-controlled ablation（Table 5）仅控制了 adapter capacity 一个变量，其他 confounds 全部保留。即使 reduced-LoRA ACT（SyConScore=0.326）超过 full ACT（0.301），这也无法排除序列长度或数据源是真正的解释变量。\n- 为什么影响接收：这是论文两个 principal findings 之一（C1），如果因果推断不成立，论文的一半贡献被削弱。\n- 建议修改方向：(1) 将\"categorical reliability gap\"降级为\"observed reliability gap\"；(2) 明确列出所有 confounds 并讨论每一个的潜在影响；(3) 考虑增加一个 ablation：在 GRPO 框架内使用 1024 token 长度和 curated pairs（而非 online generations），以部分排除序列长度和数据源的 confound。\n\n**[W3] [critical] Probe reward trap 仅单 seed 验证**\n- 具体位置：§5 整体; Table 3; Figure 3; Limitations 第 3 句\n- 问题：论文的核心发现——1,300-step temporal decoupling——仅在一个 seed 上观察到（Limitations 承认：\"The probe reward trap (C2) is demonstrated with a single seed\"）。SFT 训练虽然比 RL 更确定性，但 behavioral death 的时序（step 500）和 entropy collapse 的时序（step ~1840）可能对 initialization、learning rate、batch composition 敏感。在 negative result 论文中，单 seed 结论的可信度尤其需要更多实验支撑。\n- 为什么影响接收：temporal decoupling 是论文标题和核心 novelty claim 的基础；如果这个 timing 不稳定复现，论文的 headline contribution 被大幅削弱。\n- 建议修改方向：至少增加 2-3 个 seed 的复现实验。如果 timing 有变化，报告 mean ± std 并讨论变异性。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**[W4] [warning] §3 \"captures evidential granularity\" 表述易误导，与 §5-§6 的\"does not encode evidential warrant\" 形成表面矛盾**\n- 具体位置：§3 Direction Discriminability, 第 14-16 行; §6 root cause analysis\n- 问题：§3 写道\"The direction also captures evidential granularity\"并展示 AUROC 从 0.675（weak）单调上升到 0.929（strong）。虽然下一句解释了这是 effect-size difference 而非 evidential warrant encoding，但\"captures evidential granularity\"这一措辞本身容易让读者产生 d_syc 编码了 evidential information 的印象——这与 §5-§6 的核心论点直接矛盾。\n- 建议：将\"captures evidential granularity\"改为更精确的表述，例如\"exhibits evidence-strength-correlated discriminability\"或\"shows higher discriminability for stronger evidence\"，从而避免歧义。\n\n**[W5] [warning] Wu & Tang (2026) 的 geometric separability 论证缺乏定量支撑**\n- 具体位置：§6 第 11-13 行; §7 第 10 行\n- 问题：论文多次引用 Wu & Tang (2026) 来支持\"当行为几何可分时 representation directions 能成功\"的论点，并以此反衬 sycophancy 的 geometric inseparability。但论文本身承认\"A quantitative comparison of geometric separability between d_syc and their reward-hacking directions remains an important open question\"（§6, line 13）。这意味着论文的核心解释假设（geometric inseparability）缺乏直接的定量证据。\n- 建议：(1) 计算 d_syc 上 valid revision vs sycophantic capitulation 的 overlap 度量（如 Fisher's discriminant ratio 或 class-conditional distribution overlap）；(2) 如果可以获取 Wu & Tang 的 directions，进行定量对比。\n\n**[W6] [warning] 训练集极小（181 pairs）且 train=eval**\n- 具体位置：§2.1 Direction Extraction; Limitations 第 2 句\n- 问题：181 contrastive pairs 用于 direction extraction、probe training、reward 计算和 evaluation。虽然 Limitations 提到 held-out split (146/35) 验证了 ACT 的泛化性（SyConScore≈0.20），但：(1) 35 对 held-out set 非常小；(2) 主表的所有数字（Table 4）都基于 full 181 pairs 的 train=eval 设置；(3) 小数据集上的 AUROC 和 SyConScore 的 variance 可能很大。\n- 建议：主表应补充 held-out 性能，或至少在正文中更显著地讨论 overfitting 风险。\n\n**[W7] [warning] GRPO group size=2 偏离典型配置**\n- 具体位置：§2.5 Evaluation（第 56 行）; Limitations 第 1 句; Table 5\n- 问题：GRPO 使用 group size=2，远低于典型的 8-64 范围（Shao et al., 2024）。虽然 gs=8 ablation（Table 5）表现更差（0/3 > vanilla），但这仅有 3 个 checkpoint 的 early termination 数据，不足以排除 group size 不足是 GRPO 失败的主因。Sycophancy calibration 可能需要更大的 group size 来获得有效的 advantage estimation。\n- 建议：如果 compute budget 允许，增加 gs=16 或 gs=32 的实验。如果不可行，在正文中更充分地讨论 group size 可能是 confound 的可能性。\n\n### 小问题（不影响接收）\n\n**[M1]** Introduction line 21 提到\"4 of 31 checkpoints (12.9%)\"，但 Table 4 注释说\"4/28 checkpoints across two seeds\"。31 vs 28 的数字不一致需要核实。\n\n**[M2]** §2.1 提到使用 GPT-4.1 生成 contrastive pairs，这引入了对特定 LLM 的依赖。在 double-blind 设置下，使用最新商业 API（GPT-4.1, 2025 年发布）是否需要额外的 reproducibility 考量应被讨论。\n\n**[M3]** Table 4 中 ACT seed 2 的 ToF 和 NoF 列显示为 \"--\"，这是因为数据缺失还是不同的评估方式？应明确说明。\n\n**[M4]** §4 cosine failure chain 的分析非常有价值，但这些 failure modes（gate saturation, gap too small, mode collapse）是否为 cosine formulation 的通用问题还是 sycophancy-specific 的问题？简要讨论可以增强 generalizability。\n\n---\n\n## Questions（需要作者回答的问题）\n\n**Q1.** Probe reward trap 的 1,300-step lag 是否对 learning rate、batch size 或 LoRA rank 敏感？在不同超参数下这个 lag 是否会显著变化？\n\n**Q2.** 如果使用更大的 contrastive pair set（如 1000+ pairs），d_syc 的 discriminability 和 reward utility 的 gap 是否会缩小？具体而言，更大的训练集是否可能使 d_syc 更好地分离 warranted/unwarranted revision？\n\n**Q3.** 论文将 d_syc 的 failure 归因于 geometric inseparability（valid revision 和 sycophantic capitulation 在同一方向上 overlap）。是否测量过这两类 activation 在 d_syc 方向上的实际分布 overlap？例如 overlap coefficient 或 class-conditional histogram。\n\n**Q4.** ACT 的成功可能不仅因为 per-token supervision granularity，还因为它的 L2 consistency loss 本质上是一种 regularization。是否可以在 GRPO 框架内加入类似的 regularization term 来测试这一假设？\n\n**Q5.** SMART (Beigi et al., 2025) 使用 MCTS per-step process rewards 成功减少 sycophancy。如果 sycophancy 的 geometric inseparability 是 fundamental 的，SMART 是如何绕过这个限制的？论文的解释（\"per-step rewards can explicitly distinguish warranted from unwarranted belief change through reasoning trajectories\"）是否有实验证据支持？\n\n---\n\n## Missing References（遗漏的重要相关工作）\n\n**[MR1] [重要] \"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs\" (Vennemeyer et al., 2025, arXiv:2509.21305)**\n- 该工作证明 sycophancy 由功能独立的行为组成，各沿不同线性方向编码\n- 直接相关：如果 sycophancy 本身多维，单一 d_syc 方向的失败可能有比 \"geometric inseparability\" 更基本的原因\n- 已发表于 2025 年 9 月，submission 前应可见\n\n**[MR2] [建议] \"Sycophancy as Compositions of Atomic Psychometric Traits\" (2025, arXiv:2508.19316)**\n- 在 LLaMA 3.2 和 Qwen 2.5 上用 contrastive pairs 提取 personality traits 和 sycophancy 的 activation-space directions\n- 与本文使用的 contrastive extraction 方法直接可比\n- 2025 年 8 月发表\n\n**[MR3] [建议] \"Reward Hacking in the Era of Large Models\" survey (Wang et al., 2026, arXiv:2604.13602)**\n- 2026 年 4 月发布的 reward hacking 综述，系统性地分析了 sycophancy 作为 proxy gap 的表现形式\n- 可能因发布时间较晚而遗漏，但如果 submission 在 5 月则可能来得及引用\n\n---\n\n## Detailed Comments（逐 Section 意见）\n\n### §1 Introduction\n- 开篇清晰，problem setup 精炼。Figure 1 (teaser) 有效地传达了两个核心发现。\n- C1（categorical reliability gap）和 C2（probe reward trap）的并列呈现合理，但 C1 的 confound 问题（见 W2）意味着它的证据强度弱于 C2。\n- \"This paper presents a negative result with systematic diagnostic analysis\"（line 31）是好的自我定位，但后续 conclusion 中的 generalization 到\"other attributes where the target and its complement overlap geometrically\"（§8, line 6）已经超出了 negative result 的范畴，变成了 general principle 的声明。这两种 framing 需要更好地调和。\n\n### §2 Experimental Framework\n- Direction extraction 方法清晰（eq. 1），style matching validation（response length diff <10%, shared opening phrase ≥2 words）是合理的 quality control。\n- Reward formulations（F1-F3）的分类系统且完整。\n- SyConScore（eq. 2）的设计合理——harmonic mean 对 ToF=0 的零值惩罚是有意为之且有 justified。\n- 需要更好地 justify group size=2 的选择。仅说\"due to memory constraints\"不够——是否可以通过 gradient accumulation 实现更大的 effective group size？\n\n### §3 Direction Discriminability\n- Evidence-strength stratification（Table 1: 0.675→0.883→0.929）是有趣的发现。\n- Cross-model validation（Llama-3-8B AUROC=0.779）增强了 generalizability。\n- 但\"captures evidential granularity\"的措辞需要修改（见 W4）。\n- Random baseline comparison（0.835 vs 0.727）提供了 d_syc 的 above-chance evidence，但 Δ=0.108 不算特别大。\n\n### §4 Cosine R₁: Structural Failure\n- Diagnostic chain（F1a→F1d, Table 2）是论文的 methodological highlight 之一。每一步的 failure→fix→deeper failure 结构很有说服力。\n- 256-token truncation 将 AUROC 从 0.827 降到 ~0.60 是重要的实验细节，但也引出一个问题：如果 full-length 下 AUROC 显著更高，cosine formulations 在 full-length 下是否仍然会失败？论文没有测试这一条件（虽然 §5 的 probe trap 是在 full-length 下运行的）。\n\n### §5 The Probe Reward Trap\n- 核心发现（Table 3, Figure 3）清晰有效。\n- Differentiable probe（exp-008）在 ~30 步内 game boundary 的发现是重要的补充证据。\n- Stubbornness taxonomy（5 failure modes）提供了有价值的定性分析。\n- 主要不足：单 seed（见 W3）。\n\n### §6 When Does Discriminability Fail as Reward Utility?\n- Root cause analysis 清晰：d_syc 编码 direction of belief change 但不编码 evidential warrant。\n- R3-only GRPO 的 failure（4/28 > vanilla）有力地证明了问题不仅在 d_syc，还在 per-completion reward structure。\n- LoRA-controlled ablation（Table 5）是合理的实验设计，但仍有 5+ uncontrolled confounds（见 W2）。\n- \"categorical reliability gap\" 的表述过强（见 W2）。\n- ACT seed 2 数据不完整（Table 4 中 ToF/NoF 为 \"--\"）需要解释（见 M3）。\n\n### §7 Related Work\n- 覆盖面基本合理：Representation Engineering, Reward Design, Sycophancy Characterization, Probe-Based Methods 四个段落结构清晰。\n- 关键遗漏：Vennemeyer et al. (2025)（见 W1/MR1）。\n- Goodhart's Law (Manheim & Garrabrant, 2019) 已被引用 ✓。\n- 对 SMART 的讨论逻辑自洽：SMART 通过 per-step process rewards 绕过了 d_syc 的 geometric inseparability，与 ACT 的 per-token 成功一致。\n- Latent-GRPO、CRAFT 的讨论简洁但足够。\n\n### §8 Conclusion\n- 简洁有效，但从 specific negative result 推广到\"other attributes where the target and its complement overlap geometrically\"缺乏实证支撑。\n- \"condition-aware rewards with dense supervision offer the most promising path forward\"是合理的方向性建议但没有实验验证。\n\n### Limitations\n- 涵盖了 7 个主要局限，诚实且具体。\n- 但某些局限（如 train=eval、单 seed probe trap）的严重程度在正文中被低估了。\n\n### Appendix\n- Training hyperparameters（Appendix A）报告充分。\n- Stubbornness taxonomy（Appendix B）的 5 类 failure modes 有价值但分析较浅。\n\n---\n\n## 主要优势总结\n\n1. **系统性诊断方法论**：论文的 elimination-based diagnostic approach 是负面结果论文的范例——每个 failure mode 都被系统地分析和排除，得出结论性的 root cause。\n2. **实用性强的 cautionary finding**：temporal decoupling 揭示了 entropy monitoring 的 blind spot，对 alignment 实践有直接指导意义。\n3. **诚实的自我评估**：论文坦率地承认所有已知 confounds 和局限，没有 overclaim。\n4. **清晰的写作**：narrative 结构流畅，信息密度合理，Figure/Table 设计有效。\n\n---\n\n## 格式合规检查\n\n- ✅ 正文 8 页（Introduction 到 Conclusion 结束于 page 8）\n- ✅ Abstract ~174 words（< 200 word limit）\n- ✅ Limitations section 在正文之后、References 之前\n- ✅ Double-blind：未发现 de-anonymization（GitHub URL 使用 anonymous-nlp-2026-2）\n- ✅ ACL 格式两栏排版\n- ✅ Appendix 在 References 之后\n- ⚠️ Limitations section 中未出现 ethical considerations 相关讨论（optional，不强制）\n\n---\n\n## 评审结论\n\n本文是一篇执行质量较高的 negative result 论文，系统性地展示了 contrastive sycophancy direction 从 diagnostics 到 training signal 转化时的 fundamental failure。Probe reward trap 的 temporal decoupling 发现（C2）具有新颖性和实用价值。但论文的另一核心贡献——supervision granularity hypothesis（C1）——受限于大量 uncontrolled confounds，且 probe trap 的单 seed 验证和遗漏关键相关工作（Vennemeyer et al., 2025）是需要解决的重要问题。\n\n**推荐**：3.5（Borderline Conference），倾向 Findings。如果作者能 (1) 补充 probe trap 的多 seed 验证，(2) 讨论 Vennemeyer et al. 的 sycophancy decomposability 对 d_syc failure 的替代性解释，(3) 弱化 \"categorical reliability gap\" 的因果性表述，论文有望达到 Conference 水平。\n",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-24T12:20:13.050497+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4071
}
```

</details>

---


### Assistant

_source line 558 · 2026-05-24T12:20:25.794843+00:00_

审稿意见已提交给 Review Director。

**审稿摘要**：

- **Overall**: 3.5/5（Borderline Conference），倾向 Findings
- **Soundness**: 3.5/5 — 分析系统全面，但 probe trap 单 seed、ACT vs GRPO 5+ confounds 未控制
- **Excitement**: 3/5 — temporal decoupling 有实用价值，但核心为 Goodhart's Law 的具体实例

**三个 critical 问题**：
1. **遗漏关键文献** "Sycophancy Is Not One Thing" (Vennemeyer et al., 2025) — 该工作证明 sycophancy 多维可分解，提供了 d_syc 失败的替代解释
2. **ACT vs GRPO "categorical reliability gap" 过强** — 序列长度/数据源/dropout 等 5+ confounds 未控制，LoRA ablation 仅控制了 adapter capacity
3. **Probe reward trap 单 seed** — 1,300-step temporal decoupling 是标题级 contribution，但仅一个 seed 验证

**主要优势**：系统性诊断方法论、temporal decoupling 的实用价值、诚实的 limitations 讨论、写作质量高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

76 recorded events


### User

_source line 559 · 2026-05-24T12:23:14.490140+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + Framing**。

## Venue 信息
- **目标**: EMNLP 2026（ARR May cycle）
- **ARR 提交截止**: 2026-05-25
- **格式**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数
- **模板**: ACL style
- **匿名**: Double-blind

## 论文文件
- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf`

## 审查侧重

请重点审查以下维度：

1. **新颖性与增量贡献**
   - "discriminability ≠ reward utility" 与 Goodhart's Law（Manheim & Garrabrant 2019）高度同构——论文是否充分论证了超越一般 reward overoptimization 的增量贡献？
   - Probe reward trap 的 novelty 定位：是 "discovering a new trap" 还是 "quantifying a known failure mode"？
   - 论文引用了 Gao et al. (2023) 和 Skalse et al. (2022) 但从未使用 Goodhart 框架——这是否是重大遗漏？

2. **叙事一致性与 Framing**
   - §3 声称 d_syc "captures evidential granularity"（AUROC 0.675→0.929），§5 声称 "does not condition on input validity"，§6 声称 "does not encode evidential warrant"——是否存在内部矛盾？
   - 论文在 negative result（局部声明）和 general principle（discriminability ≠ reward utility）之间是否定位清晰？
   - SMART (per-step process reward) 讨论是否存在逻辑矛盾——如果 sycophancy 几何不可分，SMART 如何成功？
   - 标题 "The Probe Reward Trap" 是否过窄或过宽？

3. **Related Work 完整性**
   - 是否遗漏关键相关工作？特别关注：
     - Goodhart's Law 文献（Manheim & Garrabrant 2019）
     - 近期 sycophancy 相关工作（如 Kelkar et al. 2026 "Playing Devil's Advocate"）
     - CRAFT/Latent-GRPO 讨论是否有深度？
   - 与 Papadatos & Freedman (2024) 的对比是否充分？

4. **写作质量**
   - Conclusion 是否 overclaiming？
   - Abstract 是否超过 200 words（EMNLP 2026 限制）？
   - 正文是否在 8 页内？
   - 匿名是否合规（double-blind）？

5. **贡献清晰度**
   - C1（supervision paradigm gap）和 C2（probe reward trap）的关系是否清楚？
   - 论文最终的 actionable takeaway 是什么？是否足够清晰？

请按 ARR 审稿标准给出结构化审稿报告，包含 Summary、Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-24T12:23:22.748090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-24T12:23:22.748838+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-24T12:23:25.912197+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-24T12:23:25.962859+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-24T12:23:34.881081+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-24T12:23:34.984080+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-24T12:23:45.489398+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
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

_source line 567 · 2026-05-24T12:23:45.540045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-24T12:23:53.519085+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-24T12:23:55.928393+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-24T12:24:07.467602+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Main papers, the criteria include soundness, novelty, and impact, while for Findings papers, the main criteria are soundness and reproducibility.

## Review Recommendations

The review form uses a scoring scale that includes:

- 5 = Consider for Award: for papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next c
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13948
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-24T12:24:08.672584+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 12744
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-24T12:24:14.041827+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and scoring scales. Include every criterion that reviewers must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and scoring scales. Include every criterion that reviewers must fill out."
  }
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-24T12:24:15.047250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-24T12:24:15.551077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-24T12:24:16.457639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-24T12:24:16.512414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-24T12:24:16.512923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-24T12:24:16.815071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-24T12:24:17.267802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-24T12:24:17.670228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-24T12:24:20.337588+00:00_

# ACL Rolling Review Form – Complete Scoring Dimensions

## Core Review Sections

**Paper Summary**
Reviewers describe the paper's topic to ensure understanding and identify potential misinterpretations.

**Summary of Strengths**
Evaluators identify reasons supporting publication, including "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature."

**Summary of Weaknesses**
Numbered concerns addressing correctness, impact, clarity, and other publication concerns.

**Comments/Suggestions/Typos**
Additional feedback for author improvement beyond main concerns.

---

## Quantitative Scoring Dimensions

### Reviewer Confidence (5-point scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: High confidence with minor uncertainty
- **3**: Moderate confidence; details may have been missed
- **2**: Lower confidence; some misunderstandings possible
- **1**: "Not my area, or paper is very hard to understand"

### Soundness (1-5 scale with half-points)
Evaluates scientific rigor, claim support, and methodological validity. Range: 1 (Major Issues) to 5 (Excellent).

### Excitement (1-5 scale with half-points)
Assesses subjective interest regarding innovation, impact potential, and community relevance. Range: 1 (Not Exciting) to 5 (Highly Exciting).

### Overall Assessment (1-5 scale)
Final recommendation spanning "Do not resubmit" through "Consider for Award" categories.

---

## Additional Evaluation Areas

- **Limitations and Societal Impact**
- **Ethical Concerns** (referencing ACL Code of Ethics)
- **Needs Ethics Review** (flag for committee)
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale, if applicable)
- **Software** (1-5 scale, if applicable)
- **Author Identity Knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6295
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-24T12:24:26.469297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-24T12:24:26.520072+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-24T12:24:26.570779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-24T12:24:26.922196+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-24T12:24:26.922666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-24T12:24:27.601142+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 678
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-24T12:24:27.601481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-24T12:24:27.702093+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-24T12:24:32.569892+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "5-11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "5-11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-24T12:24:33.323611+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.6}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 310.9}], \"total_pages\": 11, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-24T12:24:36.591815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-24T12:24:37.446404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-24T12:24:37.498640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-24T12:24:37.905071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-24T12:24:38.309942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-24T12:24:38.310364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-24T12:24:39.017069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-24T12:24:39.219424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-24T12:24:44.087848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-24T12:24:44.691224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-24T12:24:45.143887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-24T12:24:45.144339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-24T12:24:45.295917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-24T12:24:45.601368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-24T12:27:45.217532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-24T12:27:45.719414+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-24T12:27:46.875772+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, evaluation criteria, how to assess novelty, soundness, and how to write a good review. Include any specific guidance on rating papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, evaluation criteria, how to assess novelty, soundness, and how to write a good review. Include any specific guidance on rating papers."
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-24T12:27:58.189418+00:00_

# ARR Reviewer Guidelines Summary

## Key Responsibilities

Reviewers must complete four main tasks:

1. **Allocate time** for reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write strong reviews** with clear, specific feedback
4. **Update assessments** after author responses

## What to Focus On

Begin by reading papers twice: first to understand the research question and scope, then for in-depth technical evaluation. As the guidelines note, "read the paper at least twice: skimming and in-depth reading" to avoid bias from initial impressions.

### Assignment Verification

Verify you can competently review the work. The guidelines state: "skim the paper to check whether this is something that you are qualified to review." Disclose if you know authors' identities or have conflicts of interest.

## Evaluation Criteria

### Soundness
Technical correctness and methodological rigor. Scores must be justified by review content—low soundness scores require explicit explanation of flaws.

### Excitement
Personal interest level, kept separate from soundness assessment. You may find sound work unexciting or vice versa.

### Overall Recommendation
Composite judgment reflecting soundness, novelty, impact, and potential contribution to the field.

## Assessing Novelty

Avoid rejecting papers simply because findings seem obvious in retrospect. The guidelines caution against "confirmation bias" and note that "many findings seem obvious in retrospect, but this does not mean that the community is already aware of them."

Require specific references when claiming work lacks novelty. Missing comparisons to recent methods should be justified as necessary for validating core claims, not arbitrary additions.

## Writing Strong Reviews

### Be Specific
Replace vague criticism with concrete examples:
- ❌ "Missing relevant references"
- ✅ "Paper omits references to Studies X, Y, and Z"

### Maintain Professional Tone
"Write the revie
…[truncated 1431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11313
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-24T12:28:08.234177+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/abstract*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-24T12:28:08.234641+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-24T12:28:11.397260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-24T12:28:11.448071+00:00_

1	We quantify a temporal decoupling we call the \emph{probe reward trap}: when a frozen linear probe on a contrastive sycophancy direction ($\dsyc$, cross-validated AUROC $0.827$ on Qwen3-8B, $0.779$ on Llama-3-8B) is used as an SFT training signal, behavioral death (true-positive flip rate $= 0$) occurs within 500 steps while generation entropy remains healthy (0.70). In our experiments, the resulting 1{,}300-step lag before distributional collapse means that entropy monitoring---the most common safeguard against reward hacking---misses the failure entirely. Because the trap arises under SFT with stopped gradients, it is independent of RL optimization dynamics, revealing a semantic limitation of the direction itself: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. The failure extends beyond probe rewards: all $\dsyc$-based GRPO formulations collapse, and even behavioral-reward-only GRPO exceeds vanilla at only 4/31 checkpoints, while dense per-token SFT succeeds at every checkpoint (47/47). A LoRA-controlled ablation identifies supervision granularity as the strongest candidate explanation---with sequence length, data source, and dropout as acknowledged confounds---suggesting that per-completion scalar rewards compress away the token-level information needed for sycophancy calibration.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-24T12:28:24.411778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-24T12:28:24.562839+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}---a pattern formalized as variants of Goodhart's Law~\citep{manheim2019goodhart}---and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is a concrete, empirically characterized instance with two features that existing monitoring practices do not address: behavioral death within 500 steps (far faster than typical overoptimization) and a 1{,}300-step temporal decoupling that renders entropy monitoring ineffective~\citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} show that representation-level directions succeed when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigations include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based and Representation-Guided Method
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-24T12:28:39.684279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-24T12:28:40.086253+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients, it reflects a semantic limitation of $\dsyc$, not an RL artifact; under GRPO, all formulations failed (4/31 checkpoints ${>}$ vanilla across configurations) while per-token SFT succeeded at every checkpoint (47/47), and a LoRA-controlled ablation identifies supervision granularity as the strongest candidate factor~(\S\ref{sec:discussion}).
5	More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants of that behavior.
6	For sycophancy---and likely for other attributes where the target and its complement overlap geometrically---condition-aware rewards with dense supervision offer the most promising path forward.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-24T12:28:40.086620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-24T12:28:40.538683+00:00_

1	Our GRPO experiments use group sizes of 2 and 8, at the low end of the 8--64 range explored by \citet{shao2024grpo}; the gs$=$8 ablation rules out insufficient ranking diversity as the primary explanation, but whether substantially larger groups (16--64) or alternative RL algorithms would succeed remains open. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
3	The probe reward trap (C2) is demonstrated with a single seed; while SFT training is more deterministic than RL, replication would strengthen the temporal decoupling finding.
4	The ACT vs.\ GRPO comparison differs along multiple dimensions beyond supervision granularity: sequence length (256 vs.\ 1024 tokens), data source (online generations vs.\ curated pairs), and dropout (0 vs.\ 0.05). Our LoRA-controlled ablation isolates adapter capacity, and SMART's independent success~\citep{beigi2025smart} corroborates supervision granularity, but a fully controlled comparison would require matching all training hyperparameters.
5	Contrastive pair quality relies on automated style-matching validation (19/200 pairs discarded; \S\ref{ssec:extraction}); this provides partial quality control but does not guarantee semantic validity of all retained pairs.
6	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
7	Code, contrastive pair data, prompt templates
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-24T12:28:40.589398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-24T12:28:40.640146+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable.
13	A quantitative comparison of geometric separability between $\dsyc$ and their reward-hacking 
…[truncated 8083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-24T12:28:46.018818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-24T12:28:46.471401+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/fig_teaser.pdf}
7	\caption{The probe reward trap. (a)~$\dsyc$ discriminates sycophantic from non-sycophantic activations (AUROC $0.827$), but valid revision and unwarranted capitulation overlap along the same direction. (b)~When used as an SFT reward, behavioral death ($\tof{=}0$) occurs at step 500 while entropy remains healthy; the 1{,}300-step lag renders standard monitoring blind.}
8	\label{fig:teaser}
9	\end{figure*}
10	
11	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
12	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}), though 256-token truncation during GRPO training degrades this to approximately 0.60 (\S\ref{sec:cosine_failure}).
13	These results point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a training signal.
14	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level signal could target the internal computation rather than its surface outputs.
15	
16	This paper documents the \emph{probe reward trap}: when a frozen linear probe on $\dsyc$ is used as an SFT training signal with stopped gradients, behavioral death ($\tof = 0$) occurs within 500 steps while generation entropy remains healthy (0.70), masking the failure from standard monitoring (\S\ref{sec:probe_trap}).
17	In our experiments, the 1{,}300-step lag before distributional collapse means entropy-base
…[truncated 2773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-24T12:28:46.522328+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-24T12:28:46.573135+00:00_

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
11	The direction achieves AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This monotonic relationship reflects effect-size differences---stronger evidence produces larger behavioral gaps that are easier to classify---rather than indicating that $\dsyc$ encodes evidential warrant per se.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluatio
…[truncated 3675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-24T12:29:27.502762+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
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

_source line 627 · 2026-05-24T12:29:27.553372+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-24T12:31:18.989588+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：新颖性 + 完整性 + Framing\n\n**论文标题**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 实证工作扎实、诊断链设计精巧，但核心发现本质上是 Goodhart's Law 在 sycophancy probe reward 场景的具体实例化，论文未充分论证超越已知 reward overoptimization 框架的增量贡献；supervision granularity 假说存在多个未消解的混淆变量。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 诊断链（§4-§5）方法论严谨，cross-model validation 完整；但 C1（supervision granularity）的 ablation 有多个承认但未消解的 confounds（序列长度/数据源/dropout），削弱因果推断强度 |\n| Excitement | 3/5 | \"behavioral death precedes distributional collapse by 1,300 steps\" 是实用且非平凡的监控盲区发现；但概念层面是 Goodhart's Law 的具体案例，非新框架 |\n| Reproducibility | 4/5 | 代码/数据承诺公开，训练细节充分（Appendix A），超参数完整；单 seed 限制（Limitations 已承认） |\n| Overall Assessment | 3.5/5 | Borderline Conference — 实证贡献达到 Findings 水平，但主会议接收需更清晰的增量贡献论证和更强的 ablation |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Goodhart's Law 框架定位不足——增量贡献论证薄弱\n\n- 具体位置：§7 Related Work (L7-9), §1 Introduction (L25-29)\n- 问题：论文的核心发现 \"discriminability ≠ reward utility\" 本质上是 Goodhart's Law 的实例——具体而言是 Manheim & Garrabrant (2019) 分类中的 **regressional Goodhart**（proxy 与 true objective 相关但优化 proxy 不等于优化 true objective）。§7 仅用一句话提及 Goodhart（\"a pattern formalized as variants of Goodhart's Law\"），随后声称 probe reward trap 是 \"a concrete, empirically characterized instance with two features that existing monitoring practices do not address\"。但论文从未与 Goodhart 四类型分类（regressional / extremal / causal / adversarial）对话，也未论证为何这不仅仅是 regressional Goodhart 在特定 domain 的重现。\n- 为什么影响接收：如果 reviewer 认为这是一个已知现象的再确认而非新发现，novelty 评分会大幅下降。论文需要明确说明：(a) 哪些方面是 Goodhart 框架已预测的，(b) 哪些方面是 Goodhart 框架未覆盖的（如 1,300-step temporal decoupling 是 Goodhart 文献中未记录的特征？behavioral death 速度远快于典型 reward overoptimization？）。\n- 建议修改方向：在 §7 或 §1 显式引入 Goodhart 四分类，将 probe reward trap 定位为 regressional Goodhart 的一个具有独特时间结构的实例（behavioral death 500 steps vs. distributional collapse 1,800 steps），而非隐含地将其作为全新发现呈现。这不会削弱贡献，反而会让 positioning 更精确可信。\n\n**N2** [critical] 论文在 \"negative result\" 与 \"general principle\" 之间的定位不清晰\n\n- 具体位置：§1 (L31: \"This paper presents a negative result with systematic diagnostic analysis\"), §8 Conclusion (L5: \"More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility\"), Title (\"The Probe Reward Trap\")\n- 问题：§1 明确说这是 \"a negative result\"，但 §8 将结论泛化为 \"discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants\"——这是一个覆盖所有 representation-guided RL 的 general principle。标题 \"The Probe Reward Trap\" 暗示发现了一个新现象，而非记录一个已知 failure mode 的具体实例。论文在三种 framing 之间游移：(1) negative result report, (2) 新现象的发现, (3) 通用原则的提出。\n- 为什么影响接收：Framing 不一致让 reviewer 难以评估贡献大小。如果是 negative result，Findings 合适；如果是 general principle，需要更多 domains 的验证（论文只有 sycophancy）。\n- 建议修改方向：选择一个 primary framing 并贯穿始终。建议定位为 **\"a systematic negative result that reveals a specific failure mode (temporal decoupling between behavioral death and distributional collapse) with practical monitoring implications\"**，general principle 作为 discussion 中的推测而非 conclusion 中的主张。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Supervision granularity 假说的因果证据不足\n\n- 具体位置：§6 \"Competing hypotheses and ablation\" (Table 5), Limitations (L4)\n- 问题：C1 声称 supervision granularity（per-token vs. per-completion）是 ACT >> GRPO 的最强候选解释。但 LoRA-controlled ablation（Table 5）仅控制了 adapter 容量，ACT 与 GRPO 仍在 5+ 个维度上不同：序列长度（1024 vs. 256 tokens）、数据源（curated pairs vs. online generations）、dropout（0.05 vs. 0）、训练框架（SFT vs. RL）、loss 类型（per-token cross-entropy vs. per-completion scalar）。论文在 Limitations 中坦承这一点，但 §6 和 §8 的措辞仍将 supervision granularity 表述为近乎确定的结论（\"identifying supervision granularity as the strongest candidate explanation\"），而非一个有力但未经充分隔离的假说。\n- 建议：要么 (a) 设计一个真正的 minimal pair ablation（仅改变 token-level vs. completion-level，其余完全相同），要么 (b) 在 §6 和 §8 中更谨慎地用 hedging language（如 \"the most plausible among tested hypotheses, pending further isolation\"）。当前 Limitations 的承认与正文的强措辞存在张力。\n\n**W2** [warning] §3 \"captures evidential granularity\" 措辞可能误导叙事理解\n\n- 具体位置：§3 Direction Discriminability, L14: \"The direction also captures evidential granularity.\"\n- 问题：§3 使用 \"captures evidential granularity\" 描述 AUROC 随证据强度单调递增的现象，随后在同一段澄清 \"rather than indicating that d_syc encodes evidential warrant per se\"（L16）。§6 则明确论证 d_syc **不** encode evidential warrant。虽然论文技术上没有矛盾（§3 说的是 discriminability scales with evidence strength，§6 说的是 d_syc conflates warranted and unwarranted change），但 \"captures evidential granularity\" 这一措辞容易让读者在首次阅读时建立错误预期——以为 d_syc 编码了证据质量信息，导致读到 §6 时产生割裂感。\n- 建议：将 §3 L14 改为更中性的措辞，如 \"Discriminability scales with evidence strength\" 或 \"AUROC increases monotonically with evidence-strength tier\"，避免 \"captures\" 这一暗示 encoding 的动词。\n\n**W3** [warning] SMART 讨论存在逻辑张力\n\n- 具体位置：§6 \"Future directions\" (L99-101)\n- 问题：§6 的核心论证是 sycophancy 中 warranted revision 和 unwarranted capitulation 在激活空间中几何不可分（\"the target and its complement occupy the same activation region\"，§6 L15）。但 \"Future directions\" 段声称 SMART \"may circumvent the geometric inseparability of d_syc\"（L100）通过 per-step process rewards。如果 d_syc 方向上两类行为几何不可分，为什么 per-step 版本就能区分？论文给出的解释是 SMART \"can explicitly distinguish warranted from unwarranted belief change through reasoning trajectories\"（L100-101），但没有解释为什么 reasoning trajectory 级别的信号能绕过单一方向级别的限制。\n- 建议：补充 1-2 句说明 per-step rewards 为何能规避几何不可分性——例如：reasoning trajectory 提供了时序结构（哪一步引入新证据、哪一步放弃原始立场），而这种时序信息被 completion-level scalar 压缩掉了。这恰好与 supervision granularity 论点一致，构成更完整的叙事。\n\n**W4** [warning] 实验规模限制了 general principle 的支撑力\n\n- 具体位置：全文；Limitations 部分承认但未充分讨论\n- 问题：两个模型均为 8B（Qwen3-8B, Llama-3-8B），181 contrastive pairs，单一 domain（sycophancy）。§8 Conclusion 将结果泛化为 \"likely for other attributes where the target and its complement overlap geometrically\"，但缺少对其他 attribute 的任何实验验证。对于声称 general principle 的论文，这个实验规模不足。\n- 建议：要么 (a) 在至少一个非 sycophancy attribute（如 hallucination、toxicity）上验证类似的 trap，要么 (b) 将 §8 的泛化措辞明确标记为 conjecture/hypothesis 而非 finding。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: \"behavioral death\" 一词贯穿全文但从未给出正式定义（仅用 \"ToF = 0\" 操作性描述）。建议在 §2 或 §5 首次出现时用一句话给出定义。\n- **M2**: Table 4 caption 过长（约 100 词），包含多个脚注标记（†‡§¶），视觉负担较重。建议将脚注内容移至正文或 appendix。\n- **M3**: Figure 3 的 y 轴标签 \"Entropy\" 在图中偏小，建议增大可读性。\n- **M4**: §3 L53 \"Δ=+0.108\" 的 random baseline 对比——0.727 的 random direction AUROC 似乎偏高（远超 0.5 chance level），这意味着仅凭维度就能携带一定信息，可能值得讨论。\n\n---\n\n## 主要优势\n\n1. **诊断链设计精巧**（§4-§5）：从 cosine formulation 到 binary probe 到 continuous probe 到 discretization 的系统排除法，每一步都有明确的 null hypothesis 和实验验证，达到了高质量实证论文的标准。\n2. **Temporal decoupling 发现有实用价值**：behavioral death（step 500）与 distributional collapse（step 1,800）之间的 1,300-step 时间差是一个非平凡的监控盲区，对使用 entropy monitoring 作为 early stopping 的实践者有直接启示。\n3. **Cross-model validation 增强可信度**：Qwen3-8B 和 Llama-3-8B 上定性一致的结果排除了 architecture-specific artifact 的可能。\n4. **诚实的 Limitations**：论文主动承认多个 confounds（序列长度、数据源、dropout、单 seed），并提供 held-out validation 的定量下降（28% gap）。这种透明度值得肯定。\n5. **Stubbornness taxonomy（Appendix B）**有趣：对 181 个 validation-correction 对的失败模式分类（deliberation revert 28.7%, sycophantic stubbornness 24.3% 等）提供了定性洞察。\n\n---\n\n## 缺失引用\n\n论文已引用 Director 提及的大部分关键文献（Manheim & Garrabrant 2019 ✓, Kelkar et al. 2026 ✓, CRAFT ✓, Papadatos & Freedman 2024 ✓, Gao et al. 2023 ✓, Skalse et al. 2022 ✓），但以下值得补充：\n\n1. **Goodhart 四分类详细讨论**：虽然引用了 Manheim & Garrabrant (2019)，但未与其四类型分类对话。建议至少指明 probe reward trap 对应 regressional Goodhart。\n2. **Process Reward Model 文献**：论文讨论 SMART 的 per-step rewards 但未引用 PRM 基础文献（Lightman et al. 2023 \"Let's Verify Step by Step\", Uesato et al. 2022），这些是 per-step supervision 的理论基础。\n3. **Probing 方法论文献**：论文使用 linear probe 作为核心工具但未引用 probing 方法论争论（Hewitt & Liang 2019 on selectivity, Belinkov 2022 survey），这些对理解 \"probe discriminability 的局限性\" 有直接相关性。\n\n---\n\n## 向作者提问\n\n1. 是否尝试过仅改变 supervision granularity（per-token vs. per-completion）而保持其他变量完全相同的 minimal pair 实验？如果没有，这是否是计算预算限制？\n2. Random direction baseline AUROC 为 0.727（§3 L53），远高于 chance（0.5）——这是否意味着 residual stream 中任意方向都携带一定的 sycophancy 信息？如果是，这对 d_syc 的 \"specificity\" 有何影响？\n3. 如果将 probe reward trap 在另一个几何上类似的 attribute（如 hallucination）上重现，你是否预期看到相同的 temporal decoupling？\n4. 256-token truncation 将 AUROC 从 0.76 降至 0.60——如果允许更长生成（如 1024 tokens），probe reward 是否可能成功？\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 | ✅ 合规 | 8 页（§1-§8），Limitations 在第 9 页不计入 |\n| Abstract 字数 | ✅ 合规 | ~177 词，低于 200 词限制 |\n| 匿名性 | ✅ 合规 | 作者 \"Anonymous\"，GitHub URL 使用匿名账户 |\n| Limitations | ✅ 合规 | 正文内有一个 Limitations section，Appendix 无重复 |\n| 模板 | ✅ 合规 | ACL style (`\\usepackage[hyperref]{acl}`) |\n",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：新颖性 + 完整性 + Framing\n\n**论文标题**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 实证工作扎实、诊断链设计精巧，但核心发现本质上是 Goodhart's Law 在 sycophancy probe reward 场景的具体实例化，论文未充分论证超越已知 reward overoptimization 框架的增量贡献；supervision granularity 假说存在多个未消解的混淆变量。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 诊断链（§4-§5）方法论严谨，cross-model validation 完整；但 C1（supervision granularity）的 ablation 有多个承认但未消解的 confounds（序列长度/数据源/dropout），削弱因果推断强度 |\n| Excitement | 3/5 | \"behavioral death precedes distributional collapse by 1,300 steps\" 是实用且非平凡的监控盲区发现；但概念层面是 Goodhart's Law 的具体案例，非新框架 |\n| Reproducibility | 4/5 | 代码/数据承诺公开，训练细节充分（Appendix A），超参数完整；单 seed 限制（Limitations 已承认） |\n| Overall Assessment | 3.5/5 | Borderline Conference — 实证贡献达到 Findings 水平，但主会议接收需更清晰的增量贡献论证和更强的 ablation |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Goodhart's Law 框架定位不足——增量贡献论证薄弱\n\n- 具体位置：§7 Related Work (L7-9), §1 Introduction (L25-29)\n- 问题：论文的核心发现 \"discriminability ≠ reward utility\" 本质上是 Goodhart's Law 的实例——具体而言是 Manheim & Garrabrant (2019) 分类中的 **regressional Goodhart**（proxy 与 true objective 相关但优化 proxy 不等于优化 true objective）。§7 仅用一句话提及 Goodhart（\"a pattern formalized as variants of Goodhart's Law\"），随后声称 probe reward trap 是 \"a concrete, empirically characterized instance with two features that existing monitoring practices do not address\"。但论文从未与 Goodhart 四类型分类（regressional / extremal / causal / adversarial）对话，也未论证为何这不仅仅是 regressional Goodhart 在特定 domain 的重现。\n- 为什么影响接收：如果 reviewer 认为这是一个已知现象的再确认而非新发现，novelty 评分会大幅下降。论文需要明确说明：(a) 哪些方面是 Goodhart 框架已预测的，(b) 哪些方面是 Goodhart 框架未覆盖的（如 1,300-step temporal decoupling 是 Goodhart 文献中未记录的特征？behavioral death 速度远快于典型 reward overoptimization？）。\n- 建议修改方向：在 §7 或 §1 显式引入 Goodhart 四分类，将 probe reward trap 定位为 regressional Goodhart 的一个具有独特时间结构的实例（behavioral death 500 steps vs. distributional collapse 1,800 steps），而非隐含地将其作为全新发现呈现。这不会削弱贡献，反而会让 positioning 更精确可信。\n\n**N2** [critical] 论文在 \"negative result\" 与 \"general principle\" 之间的定位不清晰\n\n- 具体位置：§1 (L31: \"This paper presents a negative result with systematic diagnostic analysis\"), §8 Conclusion (L5: \"More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility\"), Title (\"The Probe Reward Trap\")\n- 问题：§1 明确说这是 \"a negative result\"，但 §8 将结论泛化为 \"discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants\"——这是一个覆盖所有 representation-guided RL 的 general principle。标题 \"The Probe Reward Trap\" 暗示发现了一个新现象，而非记录一个已知 failure mode 的具体实例。论文在三种 framing 之间游移：(1) negative result report, (2) 新现象的发现, (3) 通用原则的提出。\n- 为什么影响接收：Framing 不一致让 reviewer 难以评估贡献大小。如果是 negative result，Findings 合适；如果是 general principle，需要更多 domains 的验证（论文只有 sycophancy）。\n- 建议修改方向：选择一个 primary framing 并贯穿始终。建议定位为 **\"a systematic negative result that reveals a specific failure mode (temporal decoupling between behavioral death and distributional collapse) with practical monitoring implications\"**，general principle 作为 discussion 中的推测而非 conclusion 中的主张。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Supervision granularity 假说的因果证据不足\n\n- 具体位置：§6 \"Competing hypotheses and ablation\" (Table 5), Limitations (L4)\n- 问题：C1 声称 supervision granularity（per-token vs. per-completion）是 ACT >> GRPO 的最强候选解释。但 LoRA-controlled ablation（Table 5）仅控制了 adapter 容量，ACT 与 GRPO 仍在 5+ 个维度上不同：序列长度（1024 vs. 256 tokens）、数据源（curated pairs vs. online generations）、dropout（0.05 vs. 0）、训练框架（SFT vs. RL）、loss 类型（per-token cross-entropy vs. per-completion scalar）。论文在 Limitations 中坦承这一点，但 §6 和 §8 的措辞仍将 supervision granularity 表述为近乎确定的结论（\"identifying supervision granularity as the strongest candidate explanation\"），而非一个有力但未经充分隔离的假说。\n- 建议：要么 (a) 设计一个真正的 minimal pair ablation（仅改变 token-level vs. completion-level，其余完全相同），要么 (b) 在 §6 和 §8 中更谨慎地用 hedging language（如 \"the most plausible among tested hypotheses, pending further isolation\"）。当前 Limitations 的承认与正文的强措辞存在张力。\n\n**W2** [warning] §3 \"captures evidential granularity\" 措辞可能误导叙事理解\n\n- 具体位置：§3 Direction Discriminability, L14: \"The direction also captures evidential granularity.\"\n- 问题：§3 使用 \"captures evidential granularity\" 描述 AUROC 随证据强度单调递增的现象，随后在同一段澄清 \"rather than indicating that d_syc encodes evidential warrant per se\"（L16）。§6 则明确论证 d_syc **不** encode evidential warrant。虽然论文技术上没有矛盾（§3 说的是 discriminability scales with evidence strength，§6 说的是 d_syc conflates warranted and unwarranted change），但 \"captures evidential granularity\" 这一措辞容易让读者在首次阅读时建立错误预期——以为 d_syc 编码了证据质量信息，导致读到 §6 时产生割裂感。\n- 建议：将 §3 L14 改为更中性的措辞，如 \"Discriminability scales with evidence strength\" 或 \"AUROC increases monotonically with evidence-strength tier\"，避免 \"captures\" 这一暗示 encoding 的动词。\n\n**W3** [warning] SMART 讨论存在逻辑张力\n\n- 具体位置：§6 \"Future directions\" (L99-101)\n- 问题：§6 的核心论证是 sycophancy 中 warranted revision 和 unwarranted capitulation 在激活空间中几何不可分（\"the target and its complement occupy the same activation region\"，§6 L15）。但 \"Future directions\" 段声称 SMART \"may circumvent the geometric inseparability of d_syc\"（L100）通过 per-step process rewards。如果 d_syc 方向上两类行为几何不可分，为什么 per-step 版本就能区分？论文给出的解释是 SMART \"can explicitly distinguish warranted from unwarranted belief change through reasoning trajectories\"（L100-101），但没有解释为什么 reasoning trajectory 级别的信号能绕过单一方向级别的限制。\n- 建议：补充 1-2 句说明 per-step rewards 为何能规避几何不可分性——例如：reasoning trajectory 提供了时序结构（哪一步引入新证据、哪一步放弃原始立场），而这种时序信息被 completion-level scalar 压缩掉了。这恰好与 supervision granularity 论点一致，构成更完整的叙事。\n\n**W4** [warning] 实验规模限制了 general principle 的支撑力\n\n- 具体位置：全文；Limitations 部分承认但未充分讨论\n- 问题：两个模型均为 8B（Qwen3-8B, Llama-3-8B），181 contrastive pairs，单一 domain（sycophancy）。§8 Conclusion 将结果泛化为 \"likely for other attributes where the target and its complement overlap geometrically\"，但缺少对其他 attribute 的任何实验验证。对于声称 general principle 的论文，这个实验规模不足。\n- 建议：要么 (a) 在至少一个非 sycophancy attribute（如 hallucination、toxicity）上验证类似的 trap，要么 (b) 将 §8 的泛化措辞明确标记为 conjecture/hypothesis 而非 finding。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: \"behavioral death\" 一词贯穿全文但从未给出正式定义（仅用 \"ToF = 0\" 操作性描述）。建议在 §2 或 §5 首次出现时用一句话给出定义。\n- **M2**: Table 4 caption 过长（约 100 词），包含多个脚注标记（†‡§¶），视觉负担较重。建议将脚注内容移至正文或 appendix。\n- **M3**: Figure 3 的 y 轴标签 \"Entropy\" 在图中偏小，建议增大可读性。\n- **M4**: §3 L53 \"Δ=+0.108\" 的 random baseline 对比——0.727 的 random direction AUROC 似乎偏高（远超 0.5 chance level），这意味着仅凭维度就能携带一定信息，可能值得讨论。\n\n---\n\n## 主要优势\n\n1. **诊断链设计精巧**（§4-§5）：从 cosine formulation 到 binary probe 到 continuous probe 到 discretization 的系统排除法，每一步都有明确的 null hypothesis 和实验验证，达到了高质量实证论文的标准。\n2. **Temporal decoupling 发现有实用价值**：behavioral death（step 500）与 distributional collapse（step 1,800）之间的 1,300-step 时间差是一个非平凡的监控盲区，对使用 entropy monitoring 作为 early stopping 的实践者有直接启示。\n3. **Cross-model validation 增强可信度**：Qwen3-8B 和 Llama-3-8B 上定性一致的结果排除了 architecture-specific artifact 的可能。\n4. **诚实的 Limitations**：论文主动承认多个 confounds（序列长度、数据源、dropout、单 seed），并提供 held-out validation 的定量下降（28% gap）。这种透明度值得肯定。\n5. **Stubbornness taxonomy（Appendix B）**有趣：对 181 个 validation-correction 对的失败模式分类（deliberation revert 28.7%, sycophantic stubbornness 24.3% 等）提供了定性洞察。\n\n---\n\n## 缺失引用\n\n论文已引用 Director 提及的大部分关键文献（Manheim & Garrabrant 2019 ✓, Kelkar et al. 2026 ✓, CRAFT ✓, Papadatos & Freedman 2024 ✓, Gao et al. 2023 ✓, Skalse et al. 2022 ✓），但以下值得补充：\n\n1. **Goodhart 四分类详细讨论**：虽然引用了 Manheim & Garrabrant (2019)，但未与其四类型分类对话。建议至少指明 probe reward trap 对应 regressional Goodhart。\n2. **Process Reward Model 文献**：论文讨论 SMART 的 per-step rewards 但未引用 PRM 基础文献（Lightman et al. 2023 \"Let's Verify Step by Step\", Uesato et al. 2022），这些是 per-step supervision 的理论基础。\n3. **Probing 方法论文献**：论文使用 linear probe 作为核心工具但未引用 probing 方法论争论（Hewitt & Liang 2019 on selectivity, Belinkov 2022 survey），这些对理解 \"probe discriminability 的局限性\" 有直接相关性。\n\n---\n\n## 向作者提问\n\n1. 是否尝试过仅改变 supervision granularity（per-token vs. per-completion）而保持其他变量完全相同的 minimal pair 实验？如果没有，这是否是计算预算限制？\n2. Random direction baseline AUROC 为 0.727（§3 L53），远高于 chance（0.5）——这是否意味着 residual stream 中任意方向都携带一定的 sycophancy 信息？如果是，这对 d_syc 的 \"specificity\" 有何影响？\n3. 如果将 probe reward trap 在另一个几何上类似的 attribute（如 hallucination）上重现，你是否预期看到相同的 temporal decoupling？\n4. 256-token truncation 将 AUROC 从 0.76 降至 0.60——如果允许更长生成（如 1024 tokens），probe reward 是否可能成功？\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 | ✅ 合规 | 8 页（§1-§8），Limitations 在第 9 页不计入 |\n| Abstract 字数 | ✅ 合规 | ~177 词，低于 200 词限制 |\n| 匿名性 | ✅ 合规 | 作者 \"Anonymous\"，GitHub URL 使用匿名账户 |\n| Limitations | ✅ 合规 | 正文内有一个 Limitations section，Appendix 无重复 |\n| 模板 | ✅ 合规 | ACL style (`\\usepackage[hyperref]{acl}`) |\n",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-24T12:31:23.584849+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4595
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-24T12:31:28.319425+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-24T12:31:28.372322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-24T12:31:32.616662+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-24T12:31:32.617327+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-24T12:31:47.005465+00:00_

审稿报告已提交给 Review Director。

**核心判断：Overall 3.5（Borderline Conference）**

两个 Must-Fix 问题：
1. **Goodhart's Law 定位不足**——论文引用了 Manheim & Garrabrant (2019) 但仅一句话，未与四分类框架（regressional/extremal/causal/adversarial）对话，导致增量贡献论证薄弱。Probe reward trap 本质上是 regressional Goodhart 的具体实例，论文需显式论证超越已知框架的新贡献。
2. **Framing 不一致**——论文在 "negative result"（§1）、"新现象发现"（标题/§5）、"通用原则"（§8 Conclusion）三种定位间游移，reviewer 难以评估贡献大小。

四个 Should-Fix：supervision granularity 因果证据不足（5+ confounds）、§3 "captures evidential granularity" 措辞误导、SMART 讨论逻辑张力、实验规模限制泛化主张。

格式全部合规（8 页正文、177 词 abstract、double-blind 匿名）。诊断链设计和 temporal decoupling 发现是论文的主要优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 635 · 2026-05-24T12:32:54.705405+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告

**Overall**: 3.5 — Borderline Conference

**Must-Fix 问题**：

**W1** [critical] "Sycophancy Is Not One Thing" (Vennemeyer et al., 2025, arXiv:2509.21305) 未被引用
- 该工作证明 sycophancy 由功能独立的行为组成，各沿不同线性方向编码。如果 sycophancy 本身多维，单一 d_syc 方向的失败可能不是因为 "discriminability ≠ reward utility"，而是因为单一方向根本无法覆盖 sycophancy 的多维结构——提供了替代解释。

**W2** [critical] ACT vs GRPO "categorical reliability gap" 声明过强，confound 控制不足
- 5+ confounds 未控制：序列长度(256 vs 1024)、数据源(online vs curated)、Dropout(0 vs 0.05)、训练范式(RL vs SFT)、目标函数差异。LoRA-controlled ablation 仅控制 adapter capacity。建议降级为 "observed reliability gap"，并考虑额外 ablation。

**W3** [critical] Probe reward trap 仅单 seed 验证
- 1,300-step temporal decoupling 是标题级 contribution，但仅一个 seed 验证。SFT 虽比 RL 更确定性，但 timing 可能对 initialization/LR/batch 敏感。建议至少增加 2-3 seed 复现。

**Should-Fix 问题**：

**W4** [warning] §3 "captures evidential granularity" 与 §5-§6 "does not encode evidential warrant" 形成表面矛盾
- 建议改为 "exhibits evidence-strength-correlated discriminability"。

**W5** [warning] Wu & Tang (2026) geometric separability 论证缺乏定量支撑
- 论文承认 "A quantitative comparison remains an important open question"。建议计算 d_syc 上 valid revision vs sycophantic capitulation 的 overlap 度量。

**W6** [warning] 训练集极小（181 pairs）且 train=eval
- 主表所有数字基于 full 181 pairs 的 train=eval。held-out split (146/35) 验证了 ACT 但 held-out set 很小。

**W7** [warning] GRPO group size=2 偏离典型配置
- gs=8 ablation 仅 3 checkpoints + early termination，不足以排除 group size 是主因。

**小问题**：
- M1: Introduction "4 of 31 checkpoints (12.9%)" vs Table 4 "4/28 checkpoints across two seeds" 数字不一致
- M2: GPT-4.1 生成 contrastive pairs 的 reproducibility 考量
- M3: Table 4 ACT seed 2 的 ToF/NoF 显示为 "--" 未解释
- M4: §4 cosine failure modes 是否为通用问题需讨论

**缺失引用**：
- MR1: "Sycophancy Is Not One Thing" (Vennemeyer et al., 2025)
- MR2: "Sycophancy as Compositions of Atomic Psychometric Traits" (2025)
- MR3: "Reward Hacking in the Era of Large Models" survey (Wang et al., 2026)

---

请对以上每个编号的观点（W1-W7, M1-M4）给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-24T12:34:56.619155+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-W1: Vennemeyer et al. (2025) \"Sycophancy Is Not One Thing\" 未引用**\n\n同意这是一个重要的缺失引用，但对其作为 **替代解释** 的力度有保留。\n\n理由：如果 sycophancy 由功能独立的多维行为组成，那么单一 d_syc 方向的失败确实存在第二种解释路径——\"不是 discriminability ≠ utility，而是单一方向根本覆盖不了多维结构\"。这一替代假说应当被讨论。\n\n但我认为它不能完全取代论文的解释，原因是：论文的 d_syc 是从 **特定类型** 的 sycophancy（opinion sycophancy / belief revision）的 contrastive pairs 中提取的，评估也仅在同类型数据上进行。在这个 **单一维度** 上，d_syc 已实现 AUROC 0.827-0.929（§3, Table 1）。Probe reward trap（§5）也发生在这同一维度上——即使方向在其目标维度上有良好 discriminability，用作 reward 仍然失败。因此 \"多维覆盖不足\" 不能解释为什么 d_syc **在其自身维度上** 作为 reward 也会导致 behavioral death。\n\n**建议**：论文应引用 Vennemeyer et al. 并讨论多维性作为 complementary（而非 alternative）解释——d_syc 可能同时受到 (a) 单维度内 warranted/unwarranted conflation 和 (b) 跨维度覆盖不足的双重限制。这会强化而非削弱 §6 的论证。\n\n---\n\n**[AGREE] R1-W2: ACT vs GRPO confound 控制不足**\n\n完全同意。我在自己的审稿中将此列为 Should-Fix W1，但 R1 将其升级为 critical 也有道理。\n\n补充证据：Table 5 的 LoRA-controlled ablation 确实仅控制了 adapter capacity（rank, α, modules），ACT reduced-LoRA (SYCONSCORE=0.326) vs GRPO gs=2 (0.153) 的 gap 仍然可以被序列长度（1024 vs 256）、数据源（curated vs online）、dropout（0.05 vs 0）中任何一个 confound 解释。论文在 Limitations L4 中承认了这一点，但 §6 正文中 \"identifying supervision granularity as the strongest candidate explanation\" 的措辞与 Limitations 的 hedging 存在张力。\n\n我支持 R1 的建议：将 \"categorical reliability gap\" 降级为 \"observed reliability gap\"。\n\n---\n\n**[AGREE with nuance] R1-W3: Probe reward trap 单 seed**\n\n同意这是一个有效的弱点，但严重程度需要 contextualize。\n\n同意理由：1,300-step temporal decoupling 是标题级 contribution，单 seed 确实不足。behavioral death 的 **精确 timing**（step 500）可能对 learning rate、initialization、batch ordering 敏感。\n\nNuance：(1) SFT 的确比 GRPO 更确定性——没有 sampling variance、group ranking variance 等 RL 特有噪声源；(2) 论文对 temporal decoupling 提供了 **机制解释**（§5-§6：d_syc 方向上 warranted/unwarranted 的几何不可分导致 probe reward 同时惩罚两类行为），这不纯粹是一个 empirical observation，而是有因果链支撑的；(3) behavioral death **是否发生** 比 **何时发生** 更重要——即使 timing 有 ±200 steps 的 variance，\"behavioral death precedes distributional collapse\" 的定性结论可能仍然成立。\n\n**建议**：增加 2-3 seeds 以 bound timing variance 是合理要求。但如果 rebuttal 阶段计算预算有限，至少应提供 learning rate sensitivity 分析（例如 0.5x 和 2x LR 下 behavioral death 是否仍先于 entropy collapse）。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W4: \"captures evidential granularity\" 措辞**\n\n完全同意。我在自己的审稿 W2 中提出了相同问题。R1 建议的替代措辞 \"exhibits evidence-strength-correlated discriminability\" 比我建议的更精确，支持采用。\n\n---\n\n**[AGREE] R1-W5: 几何可分性缺乏定量度量**\n\n同意。论文在 §6 中做了一个核心的几何论证（\"the target and its complement occupy the same activation region\"，§6 L15），但未提供任何量化支撑。§6 L13 自己也承认 \"A quantitative comparison of geometric separability between d_syc and their reward-hacking directions remains an important open question\"。\n\n一个简单的改进方案：计算 d_syc 方向上 valid revision 和 sycophantic capitulation 激活投影的 **overlap coefficient**（如 Bhattacharyya distance 或 KL divergence），与 Wu & Tang (2026) 报告的 reward-hacking directions 上的分离度对比。这会让 \"geometric inseparability\" 从定性断言变为有证据支撑的量化结论。\n\n---\n\n**[REBUT] R1-W6: 训练集极小（181 pairs）且 train=eval**\n\n部分反驳。\n\nR1 的担忧是合理的，但需要区分两种用途：(1) 评估 ACT 作为一种 **方法** 的泛化能力——这时 train=eval 确实是问题；(2) 诊断 d_syc **作为 reward signal 的失败机制**——这时 train=eval 不是问题，因为目标是理解 \"为什么 d_syc 在训练集上也失败\"，而非测试泛化。\n\n论文的核心贡献 C2（probe reward trap）属于第 (2) 类：即使在训练数据本身上，d_syc probe reward 也导致 behavioral death。这个结论不受 train=eval 的影响——如果在训练集上都失败了，在 held-out 上只会更差。\n\n对于 C1（supervision paradigm gap），train=eval 确实是一个 confound，但论文在 Limitations L2 中提供了 held-out 验证：146/35 split 下 ACT 达到 SYCONSCORE≈0.20（peak，3.7× vanilla），虽有 28% 下降，但定性结论不变。35 个 held-out pairs 确实很小，但方向一致。\n\n**建议**：论文应更清晰地区分哪些结论受 train=eval 影响（C1 的绝对数值）、哪些不受影响（C2 的 failure 机制）。\n\n---\n\n**[AGREE with nuance] R1-W7: GRPO group size=2**\n\n同意 gs=8 ablation 不充分（仅 3 checkpoints + early termination），但对 \"group size 是主因\" 的替代假说持保留态度。\n\n理由：gs=8 的 3 个 checkpoints 均低于 vanilla（0.084→0.085→0.054），trajectory 单调下降，Table 5 中 gs=8 best SYCONSCORE (0.085) 甚至低于 gs=2 best (0.153)。虽然 3 个 checkpoint 不足以做统计推断，但 gs=8 **更差** 而非更好的方向性证据至少部分削弱了 \"group size 不够\" 的假说。\n\n更重要的是：论文的 C2（probe reward trap）发生在 **SFT** 下，不涉及 group size，因此 group size 仅影响 C1 的 confound 分析。\n\n**建议**：补跑 gs=8 至少 8-10 checkpoints，或补跑 gs=16/32。如果计算预算有限，至少在 Limitations 中更明确说明 early termination 的原因和 gs=8 trending worse 的观察。\n\n---\n\n## 小问题\n\n**[AGREE] R1-M1: \"4/31\" vs \"4/28\" 数字不一致**\n\n确认不一致。§1 说 \"4 of 31 checkpoints (12.9%)\"，Table 4 脚注说 \"4/28 checkpoints across two seeds\"。推测 31 = 28（gs=2 两个 seed）+ 3（gs=8），但将不同实验条件的 checkpoints 合并计数是不合适的。应统一为 \"4/28 checkpoints under gs=2 (14.3%)\" 或明确说明 31 的组成。\n\n---\n\n**[AGREE] R1-M2: GPT-4.1 生成 reproducibility**\n\n同意应在 Appendix A 中补充 GPT-4.1 的 temperature、system prompt 等生成参数，以及是否固定了 random seed。API 版本变化导致的不可复现性是已知问题，但至少应 best-effort 记录。\n\n---\n\n**[AGREE] R1-M3: Table 4 ACT seed 2 \"--\" 未解释**\n\n同意。Table 4 中 ACT seed 2 的 ToF 和 NoF 列显示 \"--\"，但给出了 SYCONSCORE=0.286。既然 SYCONSCORE 是 ToF 和 NoF 的 harmonic mean，缺少 component 值让读者无法验证。应补充数值或在脚注中说明原因（例如：seed 2 使用不同的 checkpoint 选择策略）。\n\n---\n\n**[AGREE] R1-M4: §4 cosine failure 通用性**\n\n同意值得讨论。§4 的 cosine failure modes（F1a-F1d 全部在 step 1 就 ToF=0）可能不仅限于 sycophancy——任何 \"target behavior 与 complement 在方向上重叠\" 的 attribute 都可能出现类似 collapse。论文在 §8 L6 暗示了这一点（\"likely for other attributes where the target and its complement overlap geometrically\"），但应在 §4 末尾更明确讨论 cosine failure 的通用条件。\n\n---\n\n## 缺失引用回应\n\n**[AGREE] MR1: Vennemeyer et al. (2025)**\n同 W1 回应，应引用并讨论多维性作为 complementary 解释。\n\n**[AGREE] MR2: \"Sycophancy as Compositions of Atomic Psychometric Traits\"**\n与 MR1 方向一致，如果 sycophancy 是多维心理测量特质的组合，进一步支持 d_syc 单方向的局限性。但需确认该工作的具体内容和发表状态后再评估引用优先级。\n\n**[AGREE] MR3: Reward hacking survey (Wang et al., 2026)**\n如果存在 2026 年的 reward hacking 综述，引用它有助于将论文放入更广泛的 context。这也与我在自己审稿 N1 中提出的 Goodhart 框架定位不足问题一致。\n\n---\n\n## 综合评估\n\nR1 和我（R2）的审稿意见高度一致：\n\n**共识区域**：\n- ACT vs GRPO confound 控制不足（R1-W2 ≈ R2-W1）\n- \"captures evidential granularity\" 措辞误导（R1-W4 ≈ R2-W2）\n- 实验规模（模型 8B only、181 pairs）限制泛化论证\n- 论文实证工作质量高，诊断链设计精巧\n\n**R1 独有的有价值观点**：\n- Vennemeyer et al. 多维性替代假说（W1）——我认为是 complementary 而非 alternative，但确实应讨论\n- 单 seed 问题（W3）——我未单独列出但同意\n- 4/31 vs 4/28 数字不一致（M1）——具体且可操作\n\n**R2 独有的观点（供参考）**：\n- Goodhart 四分类定位不足（R2-N1）\n- Negative result vs general principle 的 framing 游移（R2-N2）\n- SMART 讨论的逻辑张力（R2-W3）\n- 缺失 PRM 基础文献和 probing 方法论文献\n\n**我的整体判断不变**：3.5 Borderline Conference。实证质量够 Findings，但 novelty positioning 和 confound 问题需要解决才能进 main conference。\n",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-W1: Vennemeyer et al. (2025) \"Sycophancy Is Not One Thing\" 未引用**\n\n同意这是一个重要的缺失引用，但对其作为 **替代解释** 的力度有保留。\n\n理由：如果 sycophancy 由功能独立的多维行为组成，那么单一 d_syc 方向的失败确实存在第二种解释路径——\"不是 discriminability ≠ utility，而是单一方向根本覆盖不了多维结构\"。这一替代假说应当被讨论。\n\n但我认为它不能完全取代论文的解释，原因是：论文的 d_syc 是从 **特定类型** 的 sycophancy（opinion sycophancy / belief revision）的 contrastive pairs 中提取的，评估也仅在同类型数据上进行。在这个 **单一维度** 上，d_syc 已实现 AUROC 0.827-0.929（§3, Table 1）。Probe reward trap（§5）也发生在这同一维度上——即使方向在其目标维度上有良好 discriminability，用作 reward 仍然失败。因此 \"多维覆盖不足\" 不能解释为什么 d_syc **在其自身维度上** 作为 reward 也会导致 behavioral death。\n\n**建议**：论文应引用 Vennemeyer et al. 并讨论多维性作为 complementary（而非 alternative）解释——d_syc 可能同时受到 (a) 单维度内 warranted/unwarranted conflation 和 (b) 跨维度覆盖不足的双重限制。这会强化而非削弱 §6 的论证。\n\n---\n\n**[AGREE] R1-W2: ACT vs GRPO confound 控制不足**\n\n完全同意。我在自己的审稿中将此列为 Should-Fix W1，但 R1 将其升级为 critical 也有道理。\n\n补充证据：Table 5 的 LoRA-controlled ablation 确实仅控制了 adapter capacity（rank, α, modules），ACT reduced-LoRA (SYCONSCORE=0.326) vs GRPO gs=2 (0.153) 的 gap 仍然可以被序列长度（1024 vs 256）、数据源（curated vs online）、dropout（0.05 vs 0）中任何一个 confound 解释。论文在 Limitations L4 中承认了这一点，但 §6 正文中 \"identifying supervision granularity as the strongest candidate explanation\" 的措辞与 Limitations 的 hedging 存在张力。\n\n我支持 R1 的建议：将 \"categorical reliability gap\" 降级为 \"observed reliability gap\"。\n\n---\n\n**[AGREE with nuance] R1-W3: Probe reward trap 单 seed**\n\n同意这是一个有效的弱点，但严重程度需要 contextualize。\n\n同意理由：1,300-step temporal decoupling 是标题级 contribution，单 seed 确实不足。behavioral death 的 **精确 timing**（step 500）可能对 learning rate、initialization、batch ordering 敏感。\n\nNuance：(1) SFT 的确比 GRPO 更确定性——没有 sampling variance、group ranking variance 等 RL 特有噪声源；(2) 论文对 temporal decoupling 提供了 **机制解释**（§5-§6：d_syc 方向上 warranted/unwarranted 的几何不可分导致 probe reward 同时惩罚两类行为），这不纯粹是一个 empirical observation，而是有因果链支撑的；(3) behavioral death **是否发生** 比 **何时发生** 更重要——即使 timing 有 ±200 steps 的 variance，\"behavioral death precedes distributional collapse\" 的定性结论可能仍然成立。\n\n**建议**：增加 2-3 seeds 以 bound timing variance 是合理要求。但如果 rebuttal 阶段计算预算有限，至少应提供 learning rate sensitivity 分析（例如 0.5x 和 2x LR 下 behavioral death 是否仍先于 entropy collapse）。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W4: \"captures evidential granularity\" 措辞**\n\n完全同意。我在自己的审稿 W2 中提出了相同问题。R1 建议的替代措辞 \"exhibits evidence-strength-correlated discriminability\" 比我建议的更精确，支持采用。\n\n---\n\n**[AGREE] R1-W5: 几何可分性缺乏定量度量**\n\n同意。论文在 §6 中做了一个核心的几何论证（\"the target and its complement occupy the same activation region\"，§6 L15），但未提供任何量化支撑。§6 L13 自己也承认 \"A quantitative comparison of geometric separability between d_syc and their reward-hacking directions remains an important open question\"。\n\n一个简单的改进方案：计算 d_syc 方向上 valid revision 和 sycophantic capitulation 激活投影的 **overlap coefficient**（如 Bhattacharyya distance 或 KL divergence），与 Wu & Tang (2026) 报告的 reward-hacking directions 上的分离度对比。这会让 \"geometric inseparability\" 从定性断言变为有证据支撑的量化结论。\n\n---\n\n**[REBUT] R1-W6: 训练集极小（181 pairs）且 train=eval**\n\n部分反驳。\n\nR1 的担忧是合理的，但需要区分两种用途：(1) 评估 ACT 作为一种 **方法** 的泛化能力——这时 train=eval 确实是问题；(2) 诊断 d_syc **作为 reward signal 的失败机制**——这时 train=eval 不是问题，因为目标是理解 \"为什么 d_syc 在训练集上也失败\"，而非测试泛化。\n\n论文的核心贡献 C2（probe reward trap）属于第 (2) 类：即使在训练数据本身上，d_syc probe reward 也导致 behavioral death。这个结论不受 train=eval 的影响——如果在训练集上都失败了，在 held-out 上只会更差。\n\n对于 C1（supervision paradigm gap），train=eval 确实是一个 confound，但论文在 Limitations L2 中提供了 held-out 验证：146/35 split 下 ACT 达到 SYCONSCORE≈0.20（peak，3.7× vanilla），虽有 28% 下降，但定性结论不变。35 个 held-out pairs 确实很小，但方向一致。\n\n**建议**：论文应更清晰地区分哪些结论受 train=eval 影响（C1 的绝对数值）、哪些不受影响（C2 的 failure 机制）。\n\n---\n\n**[AGREE with nuance] R1-W7: GRPO group size=2**\n\n同意 gs=8 ablation 不充分（仅 3 checkpoints + early termination），但对 \"group size 是主因\" 的替代假说持保留态度。\n\n理由：gs=8 的 3 个 checkpoints 均低于 vanilla（0.084→0.085→0.054），trajectory 单调下降，Table 5 中 gs=8 best SYCONSCORE (0.085) 甚至低于 gs=2 best (0.153)。虽然 3 个 checkpoint 不足以做统计推断，但 gs=8 **更差** 而非更好的方向性证据至少部分削弱了 \"group size 不够\" 的假说。\n\n更重要的是：论文的 C2（probe reward trap）发生在 **SFT** 下，不涉及 group size，因此 group size 仅影响 C1 的 confound 分析。\n\n**建议**：补跑 gs=8 至少 8-10 checkpoints，或补跑 gs=16/32。如果计算预算有限，至少在 Limitations 中更明确说明 early termination 的原因和 gs=8 trending worse 的观察。\n\n---\n\n## 小问题\n\n**[AGREE] R1-M1: \"4/31\" vs \"4/28\" 数字不一致**\n\n确认不一致。§1 说 \"4 of 31 checkpoints (12.9%)\"，Table 4 脚注说 \"4/28 checkpoints across two seeds\"。推测 31 = 28（gs=2 两个 seed）+ 3（gs=8），但将不同实验条件的 checkpoints 合并计数是不合适的。应统一为 \"4/28 checkpoints under gs=2 (14.3%)\" 或明确说明 31 的组成。\n\n---\n\n**[AGREE] R1-M2: GPT-4.1 生成 reproducibility**\n\n同意应在 Appendix A 中补充 GPT-4.1 的 temperature、system prompt 等生成参数，以及是否固定了 random seed。API 版本变化导致的不可复现性是已知问题，但至少应 best-effort 记录。\n\n---\n\n**[AGREE] R1-M3: Table 4 ACT seed 2 \"--\" 未解释**\n\n同意。Table 4 中 ACT seed 2 的 ToF 和 NoF 列显示 \"--\"，但给出了 SYCONSCORE=0.286。既然 SYCONSCORE 是 ToF 和 NoF 的 harmonic mean，缺少 component 值让读者无法验证。应补充数值或在脚注中说明原因（例如：seed 2 使用不同的 checkpoint 选择策略）。\n\n---\n\n**[AGREE] R1-M4: §4 cosine failure 通用性**\n\n同意值得讨论。§4 的 cosine failure modes（F1a-F1d 全部在 step 1 就 ToF=0）可能不仅限于 sycophancy——任何 \"target behavior 与 complement 在方向上重叠\" 的 attribute 都可能出现类似 collapse。论文在 §8 L6 暗示了这一点（\"likely for other attributes where the target and its complement overlap geometrically\"），但应在 §4 末尾更明确讨论 cosine failure 的通用条件。\n\n---\n\n## 缺失引用回应\n\n**[AGREE] MR1: Vennemeyer et al. (2025)**\n同 W1 回应，应引用并讨论多维性作为 complementary 解释。\n\n**[AGREE] MR2: \"Sycophancy as Compositions of Atomic Psychometric Traits\"**\n与 MR1 方向一致，如果 sycophancy 是多维心理测量特质的组合，进一步支持 d_syc 单方向的局限性。但需确认该工作的具体内容和发表状态后再评估引用优先级。\n\n**[AGREE] MR3: Reward hacking survey (Wang et al., 2026)**\n如果存在 2026 年的 reward hacking 综述，引用它有助于将论文放入更广泛的 context。这也与我在自己审稿 N1 中提出的 Goodhart 框架定位不足问题一致。\n\n---\n\n## 综合评估\n\nR1 和我（R2）的审稿意见高度一致：\n\n**共识区域**：\n- ACT vs GRPO confound 控制不足（R1-W2 ≈ R2-W1）\n- \"captures evidential granularity\" 措辞误导（R1-W4 ≈ R2-W2）\n- 实验规模（模型 8B only、181 pairs）限制泛化论证\n- 论文实证工作质量高，诊断链设计精巧\n\n**R1 独有的有价值观点**：\n- Vennemeyer et al. 多维性替代假说（W1）——我认为是 complementary 而非 alternative，但确实应讨论\n- 单 seed 问题（W3）——我未单独列出但同意\n- 4/31 vs 4/28 数字不一致（M1）——具体且可操作\n\n**R2 独有的观点（供参考）**：\n- Goodhart 四分类定位不足（R2-N1）\n- Negative result vs general principle 的 framing 游移（R2-N2）\n- SMART 讨论的逻辑张力（R2-W3）\n- 缺失 PRM 基础文献和 probing 方法论文献\n\n**我的整体判断不变**：3.5 Borderline Conference。实证质量够 Findings，但 novelty positioning 和 confound 问题需要解决才能进 main conference。\n",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-24T12:35:00.375297+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3756
}
```

</details>

---


### Assistant

_source line 638 · 2026-05-24T12:35:10.922645+00:00_

已提交对 Reviewer 1 全部观点（W1-W7, M1-M4, MR1-MR3）的逐条回应。

核心立场：
- **6 项 AGREE**：confound 控制不足（W2）、单 seed（W3）、措辞误导（W4）、几何量化缺失（W5）、group size ablation 不足（W7）、数字不一致（M1）
- **1 项 REBUT**：train=eval（W6）——对 C2（probe reward trap 机制诊断）不构成问题，仅影响 C1 的绝对数值
- **1 项 AGREE with nuance**：Vennemeyer et al.（W1）应引用但作为 complementary 而非 alternative 解释

整体评分维持 3.5 Borderline Conference，与 R1 判断一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

76 recorded events


### User

_source line 639 · 2026-05-24T22:52:48.390529+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查本论文的**新颖性与完整性**。

## Venue 信息
- **目标**: EMNLP 2026（通过 ARR 统一审稿）
- **类别**: Long Paper
- **截止日期**: 2026-05-25
- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）
- **模板**: ACL style（\usepackage[review,hyperref]{acl}）
- **匿名规则**: Double-blind
- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf`

## 你的审查重点

### 1. 新颖性定位
- "probe reward trap" 是否是真正新的发现，还是 Goodhart's Law 的已知实例？论文引用了 Manheim & Garrabrant (2019) 四分类，但讨论是否足够深入？
- "discriminability ≠ reward utility" 这个核心命题在 reward hacking 文献中是否已有先例？增量贡献在哪里？
- 与 Vennemeyer et al. (2025) "Sycophancy Is Not One Thing" 的关系——sycophancy 可分解为多维子行为，d_syc 投影到单轴是否是已知限制？
- Temporal decoupling（behavioral death 先于 distributional collapse）是否确实是新现象？

### 2. Framing 一致性
- 论文标题强调 "probe reward trap"，但主体贡献还包括 cosine failure 和 ACT vs GRPO 对比——论文的 primary framing 是什么？
- 论文在 "negative result"、"新现象发现"、"通用原则（discriminability ≠ reward utility）" 三种 framing 之间是否游移？
- Abstract/Introduction/Conclusion 的 claims 是否一致？scope 是否匹配实验证据？
- "systematic negative result" vs "The Probe Reward Trap" 作为标题——是否过度强调单一现象？

### 3. Related Work 覆盖
- 检查以下关键引用是否存在且讨论充分：
  - Goodhart's Law: Manheim & Garrabrant (2019) 四分类
  - Sycophancy 多维性: Vennemeyer et al. (2025)
  - Probe-based methods: Papadatos & Freedman (2024)
  - Process rewards: Lightman et al. (2023/2024), Uesato et al. (2022)
  - Representation engineering: Zou et al. (2023), Burns et al. (2023)
  - SMART: Beigi et al. (2025)
  - Wu & Tang (2026) reward hacking
  - Probing 方法论: Hewitt & Liang (2019), Belinkov (2022)
- 是否有重要遗漏？

### 4. 写作质量
- 行文是否有 AI 写作痕迹（em-dash 过多、hedging 模式等）
- 术语定义是否清晰（"behavioral death" 是否正式定义？）
- 数字在不同章节之间是否一致（例如 "4/31" vs "4/28" checkpoint 统计）
- 论文叙事结构是否清晰流畅

### 5. 格式合规
- 正文是否在 8 页以内
- Limitations section 是否只有一个且在正文中
- Abstract 是否不超过 200 words
- 是否 double-blind 合规（无作者信息泄露、无非匿名仓库链接）
- 引用格式是否规范（natbib, .bst）
- Appendix 中是否包含不应有的 limitations section

### 6. 论文完整性
- 所有 Figure 和 Table 是否在正文中被引用
- 实验结果是否支撑所有 claims
- Limitations 是否充分但不过长
- Conclusion 是否存在 overclaiming

请输出完整审稿意见，结构为：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（逐条，按 critical/major/minor 分级，重点在此）
4. Questions to Authors
5. Missing References（如有）
6. Soundness (1-5) / Presentation (1-5) / Contribution (1-5) / Overall (1-5，按 EMNLP 2026 标准) / Confidence (1-5)
7. Format Compliance Checklist（逐项 pass/fail）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-24T22:52:58.539220+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-24T22:52:58.589989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-24T22:53:02.658746+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-24T22:53:05.068765+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
  "pages": "1-10",
  "project": "contrastive_entrain_calib",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
    "pages": "1-10",
    "project": "contrastive_entrain_calib",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-24T22:53:05.822012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-24T22:53:09.943127+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found the search results for ACL ARR 2026 reviewer guidelines and review form criteria. Here's what the information reveals:

## Review Form Criteria

For Main papers, reviewers evaluate based on multiple criteria, while for Findings papers the main c
…[truncated 1283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7284
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-24T22:53:11.825441+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6756
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-24T22:53:11.826000+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/related_work}
34	
35	\input{sections/framework}
36	
37	\input{sections/direction_quality}
38	
39	\input{sections/cosine_failure}
40	
41	\input{sections/probe_trap}
42	
43	\input{sections/discussion}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6003
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-24T22:53:19.668230+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. List every question/field the reviewer must fill out, including the scoring scale for each dimension (e.g., Soundness 1-5, Overall Assessment 1-5, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. List every question/field the reviewer must fill out, including the scoring scale for each dimension (e.g., Soundness 1-5, Overall Assessment 1-5, etc.)"
  }
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-24T22:53:20.521689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-24T22:53:21.024199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-24T22:53:21.979494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-24T22:53:21.980524+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-24T22:53:22.182162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-24T22:53:22.686061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-24T22:53:22.938676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-24T22:53:24.147334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1965
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-24T22:53:25.053692+00:00_

# ACL Rolling Review Form Fields and Scoring Dimensions

## Required Text Fields
1. **Paper Summary** – Description of paper topic and content
2. **Summary of Strengths** – Reasons supporting publication
3. **Summary of Weaknesses** – Concerns about the paper (numbered)
4. **Comments/Suggestions/Typos** – Additional improvement suggestions
5. **Best Paper Justification** – Explanation if rating "Consider for Award" or "Borderline Award"
6. **Limitations and Societal Impact** – Assessment of author discussion on limitations and impacts
7. **Ethical Concerns** – Review against ACL ethics code
8. **Needs Ethics Review** – Explanation if paper requires in-depth ethics review
9. **Reproducibility** – Assessment of reproducibility information
10. **(Optional) Conjecture as to Author Identity** – Confidential author identity speculation

## Scoring Dimensions

| Dimension | Scale | Notes |
|-----------|-------|-------|
| Reviewer Confidence | 1-5 | Evaluator's certainty level |
| Soundness | 1-5 (half-point increments) | Scientific rigor and thoroughness |
| Excitement | 1-5 (half-point increments) | Subjective appeal and innovation |
| Overall Assessment | 1-5 (half-point increments) | Recommendation (Award through Reject) |
| Reproducibility | 1-5 | Ability to replicate results |
| Datasets | 1-5 | Value of released datasets |
| Software | 1-5 | Value of released software |
| Author Identity Knowledge | 1-5 | Degree of anonymity breach |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5385
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-24T22:53:25.105123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2419
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-24T22:53:25.257983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2319
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-24T22:53:30.768782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-24T22:53:31.222110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-24T22:53:31.725220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-24T22:53:31.725647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-24T22:53:32.632133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-24T22:53:32.633574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-24T22:53:32.634005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-24T22:53:32.985726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-24T22:53:33.239483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-24T22:53:33.842744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-24T22:53:40.931066+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
  "pages": "11-12",
  "project": "contrastive_entrain_calib",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
    "pages": "11-12",
    "project": "contrastive_entrain_calib",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-24T22:53:41.384466+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 241.8}], \"total_pages\": 12, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-24T22:53:41.606596+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-24T22:53:41.657314+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-24T22:53:44.669404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-24T22:53:45.575073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-24T22:53:45.625830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-24T22:53:45.927624+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-24T22:53:46.028559+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-24T22:53:46.030564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-24T22:53:50.851582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-24T22:53:51.304094+00:00_

1	Representation engineering reveals that sycophancy is linearly encoded in LLM residual streams, suggesting that such directions could serve as training signals for alignment. We test this premise systematically and document its failure. A contrastive sycophancy direction $\dsyc$ reliably discriminates sycophantic from non-sycophantic activations, yet every formulation that converts it into a Group Relative Policy Optimization (GRPO) reward collapses. We identify the \emph{probe reward trap}: when a periodically retrained linear probe on $\dsyc$ is used as a non-differentiable reward signal, behavioral death occurs within 500 steps while generation entropy remains healthy (0.70), creating a 1{,}300-step monitoring blind spot that entropy-based safeguards miss entirely. The failure persists with stopped gradients, implicating the direction's semantic limitation rather than optimization dynamics: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. The failure extends beyond probe rewards: behavioral-reward-only GRPO exceeds vanilla at only 4/31 checkpoints, while dense per-token supervised fine-tuning succeeds at every checkpoint (31/31 across two seeds). A Low-Rank Adaptation (LoRA) ablation identifies supervision granularity as one plausible explanation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-24T22:53:51.304451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-24T22:53:52.258696+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/fig_teaser.pdf}
7	\caption{The probe reward trap. (a)~$\dsyc$ discriminates sycophantic from non-sycophantic activations (AUROC $0.83$), but valid revision and unwarranted capitulation overlap along the same direction. (b)~When used as a GRPO reward, behavioral death (true-positive flip rate $\tof{=}0$) occurs at step 500 while entropy remains healthy; the 1{,}300-step lag renders standard monitoring blind.}
8	\label{fig:teaser}
9	\end{figure*}
10	
11	Sycophancy, the tendency of large language models (LLMs) to prioritize agreement over accuracy, is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy, perez2023discovering}.
12	Models trained with reinforcement learning from human feedback (RLHF) systematically amplify this tendency \citep{ouyang2022instructgpt, christiano2017rlhf, shapira2026amplifies}: even when models can assess the correctness of their own outputs \citep{kadavath2022language}, social pressure from users overrides this internal knowledge \citep{wang2025internal}.
13	Existing mitigations, from synthetic data augmentation \citep{wei2024synthetic} to neuron-level correction \citep{obrien2025fewbadneurons}, operate on behavioral outputs rather than the internal representations that generate sycophantic decisions.
14	Representation engineering \citep{zou2023repe, marks2024geometry} offers a structurally different approach: a contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated area under the ROC curve (AUROC) of $0.83$ on Qwen3-8B and $0.78$ on Llama-3-8B (\S\ref{sec:direction_quality}).
15	If the model's own representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a training signal that targets the computational ro
…[truncated 3340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-24T22:53:52.409837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-24T22:53:52.712507+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe, marks2024geometry}; inference-time methods such as Inference-Time Intervention \citep[ITI;][]{li2023iti}, Activation Addition \citep[ActAdd;][]{turner2023actadd}, and Contrastive Activation Addition \citep[CAA;][]{rimsky2024caa} demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}, but we find that $\dsyc$ fails when used as an RL reward despite succeeding at inference time.
5	
6	\paragraph{Reward Design and Overoptimization.}
7	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling, pan2022effects}; \citet{manheim2019goodhart} taxonomize four variants of Goodhart's Law.
8	This risk compounds in RLHF pipelines \citep{christiano2017rlhf, stiennon2020summarize, ziegler2019finetuning}, where policy optimization \citep{schulman2017ppo} amplifies misspecification \citep{hubinger2024sleeper}.
9	Our probe reward trap (\S\ref{sec:probe_trap}) instantiates the regressional variant, with two features not previously documented: behavioral death within 500 steps (far faster than gradual degradation~\citep{gao2023scaling}) and a 1{,}300-step temporal decoupling that renders entropy monitoring ineffective~\citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} show that representation-level directions succeed when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in assistants trained via RLHF \citep{ouyang2022instructgpt, bai2022training, sharma2023sycophancy, perez2023discovering, shapira2026amplifies} and traceable to late-layer preference shifts \citep{wang2025internal}; it undermines broader truthfulness objectives \citep{lin2022truthfulqa} even when models possess the knowledge to respond accurately \citep{kadavat
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-24T22:53:52.713054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-24T22:53:53.165298+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation generalizes: Llama-3-8B achieves comparable discriminability (AUROC $0.779$) yet the semantic gap persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions succeed when shortcut behaviors are geometrically separable.
13	Independent work corroborates the limitation: persona vectors are geometrically independent of $\dsyc$ \citep{kelkar2026persona}, and sycophancy decomposes into independently steerable sub-behaviors \citep{vennemeyer2025sycophancy} that $\dsyc$ projects onto a single axis.
14	
15	\paragraph{GRPO results under our configuration.}
16	
17	\begin{table}[t]
18	\centering
19	\caption{Comparison of all s
…[truncated 6658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-24T22:53:53.166115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-24T22:53:53.567963+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, evading entropy monitoring entirely.
4	The failure is semantic: $\dsyc$ conflates warranted revision with unwarranted capitulation, causing all GRPO formulations to collapse (4/31 checkpoints ${>}$ vanilla) while per-token SFT succeeded at every checkpoint (31/31 across two seeds; \S\ref{sec:discussion}).
5	
6	The broader lesson is that discriminability does not guarantee reward utility.
7	Linear directions can diagnose and steer model behavior at inference time; our results show that the step from diagnosis to training signal is not automatic.
8	
9	When the target behavior and its complement are geometrically distinct, concept directions transfer successfully into rewards; when they overlap, as with sycophancy, optimization produces predictable collapse.
10	Practitioners should verify geometric separability before deploying concept directions as rewards, and complement entropy monitoring with behavioral metrics that directly measure the target capability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-24T22:53:53.568357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-24T22:53:53.618916+00:00_

1	Our GRPO experiments use group sizes of 2 and 8, at the low end of the 8--64 range explored by \citet{shao2024grpo}; the gs$=$8 ablation rules out insufficient ranking diversity as the primary explanation, but whether substantially larger groups (16--64) or alternative RL algorithms would succeed remains open. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	
3	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
4	The probe reward trap (C2) is demonstrated with a single seed; replication would strengthen the temporal decoupling finding.
5	Contrastive pair quality relies on automated style-matching validation (19/200 pairs discarded; \S\ref{ssec:extraction}); this provides partial quality control but does not guarantee semantic validity of all retained pairs.
6	
7	The ACT vs.\ GRPO comparison differs along multiple dimensions beyond supervision granularity: sequence length (256 vs.\ 1024 tokens), data source (online generations vs.\ curated pairs), and dropout (0 vs.\ 0.05). Our LoRA-controlled ablation isolates adapter capacity, and SMART's independent success~\citep{beigi2025smart} corroborates supervision granularity, but a fully controlled comparison would require matching all training hyperparameters.
8	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
9	Code, contrastive pair data, prompt templates, and training configurations are available 
…[truncated 79 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-24T22:53:58.831460+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-24T22:53:59.132909+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 \citep{openai2025gpt41} in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (5-fold CV).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$, each entering as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa natural language inference (NLI) classifier scoring consistency with the ground-truth answer).
23	\begin{itemize}
24	\item[\textbf{F1}] \textbf{Cosine projection} wit
…[truncated 3092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-24T22:53:59.133429+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-24T22:53:59.635215+00:00_

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
11	The direction achieves AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	AUROC increases monotonically with evidence-strength tier: from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
15	This monotonic relationship reflects effect-size differences (stronger evidence produces larger behavioral gaps that are easier to classify) rather than indicating that $\dsyc$ encodes evidential warrant per se.
16	
17	\paragraph{Cross-model generalization.}
18	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B
…[truncated 3669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-24T22:53:59.635824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-24T22:54:00.588935+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	During GRPO training, 256-token truncation reduces $\dsyc$ AUROC from 0.827 to approximately 0.60, so the optimizer works with a substantially weaker signal than the offline metrics suggest.
5	We test whether even this degraded discriminability translates into a viable reward through four configurations that form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
10	\label{tab:cosine_chain}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lllll@{}}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	The diagnostic chain begins with a norm mismatch.
25	F1a's dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$) saturates because residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, zeroing the gradient by step 955.
26	Cosine similarity (F1b) eliminates this norm dependence but reveals a second problem: the gap between valid and sycophantic cosines averages only 0.098, too narrow for meaningful reward contrast.
27	Recalibration (F1c, \S\ref{ssec:recalib}) widens the gap (offline AUROC rises to 0.910) but introduces a third: each recalibration event creates a reward discontinuity that destabilizes advantage estimates, collapsing entropy to 0.069 within 300 steps.
28	Amplificat
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-24T22:54:00.589448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-24T22:54:00.690448+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail on signal magnitude; a natural response is to discretize.
5	Training a logistic probe on $\dsyc$ and thresholding its output yields $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use the probe as a non-differentiable reward component within GRPO (\S\ref{ssec:reward}); the trap therefore reflects a semantic limitation of the probe rather than gradient-based exploitation.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient, the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the stopped-gradient design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient, the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (stopped-gra
…[truncated 2397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-24T22:54:00.690984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-24T22:54:00.791997+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & -- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & -- \\
37	KL (Kullback--Leibler) $\beta$ & 0.04 & -- \\
38	Max compl.\ len. & 256 & -- \\
39	Max seq.\ len. & -- & 1{,}024 \\
40	L2 loss weight & -- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times
…[truncated 2347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-24T22:54:09.481090+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-24T22:54:09.481608+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-24T22:54:11.804044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-24T22:54:11.945145+00:00_

1	@article{zhang2026latentgrpo,
2	  title={Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering},
3	  author={Zhang, Nonghai and Ma, Weitao and Ma, Zhanyu and Xu, Jun and Gao, Jiuchong and Hao, Jinghua and He, Renqing and Xu, Jingwen},
4	  journal={arXiv preprint arXiv:2601.08427},
5	  year={2026}
6	}
7	
8	@inproceedings{zou2023repe,
9	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
10	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Gould, Shashwat and Li, Zifan and Xie, Chuanqi and Leung, Alexandria and Hase, Peter and Hendrycks, Dan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2025}
13	}
14	
15	@inproceedings{rimsky2024caa,
16	  title={Steering Llama 2 via Contrastive Activation Addition},
17	  author={Rimsky, Nina and Gabrieli, Nick and Schulz, Jenna and Smith, Meg and Tong, Ioannis and Hubinger, Evan},
18	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
19	  year={2024}
20	}
21	
22	@article{shao2024grpo,
23	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
24	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
25	  journal={arXiv preprint arXiv:2402.03300},
26	  year={2024}
27	}
28	
29	@inproceedings{li2023iti,
30	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
31	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{turner2023actadd,
37	  title={Steering Language Models With Activation Engineering}
…[truncated 15148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 141
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-24T22:56:44.479065+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines, especially: what to evaluate, how to score papers, what constitutes a good review, any specific guidance on negative results papers, and the overall assessment scale with descriptions of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines, especially: what to evaluate, how to score papers, what constitutes a good review, any specific guidance on negative results papers, and the overall assessment scale with descriptions of each score level."
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-24T22:56:51.409100+00:00_

# ARR Reviewer Guidelines: Key Evaluation Framework

## What to Evaluate

Reviewers should assess papers across multiple dimensions:

**Soundness & Technical Quality**: Validate methodology, proof correctness, and experimental rigor. Check for "appropriate information about statistical significance (error bars, confidence intervals)" and proper assumptions.

**Novelty & Contribution**: Evaluate whether the work advances knowledge. The guidelines caution against dismissing contributions simply because they seem "obvious in retrospect" or aren't state-of-the-art.

**Scope & Appropriateness**: Ensure "claims are appropriately scoped" and the research question is clear.

## Scoring System

ARR uses three distinct scores:

1. **Soundness**: Must be "justified by the text of the review." Low scores require documented technical flaws.

2. **Excitement**: Reflects personal interest, separate from soundness. A paper can be sound but personally unexciting.

3. **Overall Recommendation**: "A composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Characteristics of Strong Reviews

Effective reviews are:
- **Specific**: "The paper is missing references X, Y, Z" rather than vague criticisms
- **Professional**: Maintain "neutral" tone; "write the review you would like to get yourself"
- **Justified**: Connect scores to documented evidence
- **Constructive**: Explain *why* issues matter, not just listing them

## Guidance on Negative Results

The guidelines explicitly encourage negative results papers: "The bias towards publishing only positive results is a known problem in many fields." Reviewers should evaluate whether findings are "systematically" important, regardless of outcome direction.

## Common Review Pitfalls to Avoid

Problematic patterns flagged include:
- Dismissing work as "too simple" (simplicity is preferable)
- Requesting excessive experiments beyond claim scope
- Criticizing methodology preference
…[truncated 84 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6930
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-24T22:59:11.438232+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：新颖性与完整性\n\n---\n\n## 1. Summary\n\n本文研究将 LLM 残差流中的对比性 sycophancy 方向 (d_syc) 转化为 GRPO 训练奖励信号的可行性，系统性地记录了其失败模式。核心发现\"probe reward trap\"表明：当 d_syc 作为二值化 probe 奖励时，行为性死亡 (ToF=0) 比分布性崩溃提前 1,300 步发生，使得基于 entropy 的监控手段完全失效。论文还报告了 per-token SFT (ACT) 在每个 checkpoint 都优于 vanilla，而 per-completion GRPO 仅在极少数 checkpoint 优于 vanilla 的观察。论文将失败归因于 d_syc 的语义局限：它编码\"belief 是否改变\"而非\"是否应该改变\"。\n\n---\n\n## 2. Strengths\n\n**S1. 系统性的诊断链设计 (Section 5)**\nCosine R1 的四配置诊断链 (F1a→F1b→F1c→F1d) 设计精巧：每个配置解决前一个的失败模式却暴露更深层问题，最终收敛于 d_syc 的语义局限这一统一结论。这种\"逐层剥洋葱\"的实验设计让读者清晰追踪作者的推理过程，是本文方法论上的亮点。\n\n**S2. Temporal decoupling 发现具有实践价值 (Section 6, Table 3, Figure 3)**\n行为死亡先于分布崩溃 1,300 步的发现有明确的实践意义：entropy-based early stopping 是当前 reward hacking 防护的主流手段 (Casper et al., 2023)，本文指出这一手段对特定类型的 reward 失效有系统性盲区。Table 3 清晰展示 ToF 在 step 500 归零而 entropy 在 0.70-0.80 区间维持到 step 1000+，证据充分。\n\n**S3. 负面结果的诚实报告与充分讨论**\n论文没有回避失败，对三类贡献 (C1-C3) 的 scope 做了合理限定。Limitations 部分系统性地讨论了 group size、truncation、single seed、ACT vs GRPO confounds 等问题，体现了学术诚信。\"one plausible explanation\" 的措辞虽然重复（见 W5），但反映了对因果推断的谨慎态度。\n\n**S4. d_syc 方向的充分验证 (Section 4)**\n在声称 d_syc 作为奖励失败之前，Section 4 从五个维度验证了其判别能力（交叉验证、evidence-strength 分层、跨模型迁移、训练稳定性、probe ablation），排除了\"方向本身质量差\"这一平凡解释。这一实验设计逻辑严谨。\n\n**S5. 对 Vennemeyer et al. (2025) 的整合**\n论文在 Related Work 和 Discussion 中都引用了 Vennemeyer et al. (2025) 关于 sycophancy 可分解为独立可操控子行为的发现，并将其与 d_syc 投影到单一轴的局限性联系起来（Section 7, line 13）。这一关联有助于解释为什么 d_syc 在判别上有效但在奖励设计上失败。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心数字不一致：4/31 vs 4/28\n\n- 具体位置：Abstract (line 1)、Introduction C1 (line 31)、Conclusion (line 4) 使用 \"4/31 checkpoints (12.9%)\"；Discussion (line 45) 和 Table 4 脚注使用 \"4/28 checkpoints (14.3%)\"\n- 问题：论文在最核心的实验结果上使用了两个不同的分母（31 vs 28）和百分比（12.9% vs 14.3%），没有任何解释。通过 Table 5 可以推断 4/31 = 4/28 (gs=2) + 0/3 (gs=8)，但这一合并逻辑从未在正文中说明。更严重的是，在 Conclusion 中\"d_syc conflates warranted revision... causing all GRPO formulations to collapse (4/31 checkpoints > vanilla)\"这句话将 d_syc 的语义局限归因为所有 GRPO 失败的原因，但 R3-only GRPO 根本不使用 d_syc——这是因果归因错误，不仅仅是数字不一致。\n- 为什么影响接收：论文的两个关键 claim（R3-only GRPO 失败率、d_syc 导致所有 GRPO 崩溃）在正文不同位置相互矛盾，损害可信度。\n- 建议修改方向：(1) 统一使用一个分母并说明包含/排除 gs=8 的理由；(2) 修正 Conclusion 的因果归因，区分 d_syc 导致的失败（cosine/probe GRPO）和 per-completion 结构导致的失败（R3-only GRPO）。\n\n**N2** [critical] 新颖性定位不够锐利——\"probe reward trap\" vs Goodhart's Law regressional variant\n\n- 具体位置：Section 2 (Related Work, line 9)、Section 7 (Discussion, line 4-9)\n- 问题：论文在 Related Work 中明确将 probe reward trap 定位为 Goodhart's Law 的 regressional variant (Manheim & Garrabrant, 2019)，声称的差异化在于：(a) 行为死亡速度快（500 步 vs 渐进退化），(b) temporal decoupling。但论文没有充分论证为什么这些差异不仅仅是 degree 的区别而是 kind 的区别。快速崩溃可能是 group size=2 + 小数据集（181 pairs）+ LoRA rank 64 等超参数组合的结果，而非本质性的新现象。C3 (\"discriminability ≠ reward utility\") 虽然表述得当，但本质上是 \"good classifier ≠ good reward\" 的重述——这在 reward misspecification 文献中是已知原理。\n- 为什么影响接收：如果核心贡献被认为是已知原理在特定设定下的确认（而非新发现），论文的 excitement 会显著降低。\n- 建议修改方向：(1) 更锐利地定位增量贡献：强调 temporal decoupling 的监控意义（这是最有价值的独特发现），而非泛泛的 \"discriminability ≠ reward utility\"；(2) 讨论快速崩溃是否在不同超参数下复现，以排除这是超参数artifact的可能；(3) 与 Goodhart taxonomy 的其他 variant 做更精确的对比，说明为什么 regressional variant 在 representation-based reward 设定下有特殊的 failure signature。\n\n**N3** [critical] Probe reward trap 仅有单一 seed 证据\n\n- 具体位置：Limitations (line 4)：\"The probe reward trap (C2) is demonstrated with a single seed; replication would strengthen the temporal decoupling finding.\"\n- 问题：论文的标题和核心贡献 (C2) 基于单一 seed 的实验。1,300-step temporal decoupling 是本文最独特的发现，但单一 seed 无法区分这是系统性现象还是随机波动。尤其是 R3-only GRPO 在 2 seeds 之间已经显示出显著的 oscillation (Δ≈0.069, Figure 4)，说明训练动态在不同 seed 间变化较大。\n- 为什么影响接收：以单一 seed 支撑标题级 claim，不满足实证研究的基本 reproducibility 要求。\n- 建议修改方向：至少增加 2 个额外 seed 的 probe trap 实验（计算量不大：单 seed probe trap 在 2000 步内完成，论文报告总计算量仅 ~120 GPU-hours）。如果时间不允许，应显著弱化标题和 Abstract 中对 temporal decoupling 精确步数的声明。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] ACT vs GRPO 比较的 confounds 削弱 C1\n\n- 具体位置：Discussion (line 86-88)、Limitations (line 7)、Table 6\n- 问题：ACT 和 GRPO 在至少 5 个维度上不同：(1) 序列长度 (1024 vs 256 tokens), (2) 数据来源 (curated pairs vs online generations), (3) dropout (0.05 vs 0), (4) LoRA α (128 vs 64) 和模块数 (7 vs 4), (5) 监督粒度 (per-token vs per-completion)。LoRA-controlled ablation (Table 5) 仅控制了第 (4) 点。论文使用 \"one plausible explanation\" 来 hedge，但 C1 在 Introduction 中的表述 \"Observed reliability gap between supervision paradigms\" 暗示这是一个关于 paradigm 差异的 claim，实际证据不足以支撑。\n- 建议：(1) 将 C1 的表述从 paradigm-level claim 调整为 observation-level claim；(2) 讨论序列长度 confound 的影响（256 tokens 截断使 d_syc AUROC 从 0.76 降到 0.60，ACT 用 1024 tokens 不受此影响）。\n\n**W2** [major] Framing 在三种叙事之间游移\n\n- 具体位置：Title、Abstract、Introduction (line 27)、Conclusion\n- 问题：论文在以下三种 framing 之间不够一致：\n  - (a) 标题 \"The Probe Reward Trap\" → 聚焦于特定现象的发现\n  - (b) Introduction line 27 \"This paper presents a negative result with systematic diagnostic analysis\" → negative result paper\n  - (c) Conclusion 的核心句 \"The broader lesson is that discriminability does not guarantee reward utility\" → 通用原则的提炼\n  \n  这三种 framing 并不矛盾但也不完全一致。Probe reward trap 是论文的核心新发现（C2），但 C1 (ACT > GRPO) 和 C3 (discriminability ≠ reward utility) 各自占据了相当篇幅。标题聚焦 probe reward trap，但 Conclusion 把 \"discriminability ≠ reward utility\" 定为 \"broader lesson\"，读者不确定论文的 primary contribution 是哪一个。\n- 建议：明确 primary framing（建议以 temporal decoupling 为核心独特贡献），将 C1 和 C3 明确定位为支撑性证据。\n\n**W3** [major] 缺少 probing 方法论文献的讨论\n\n- 具体位置：Section 2 (Related Work)、Section 6 (The Probe Reward Trap)\n- 问题：论文的核心方法依赖 linear probe，但未引用 probing 方法论的基础文献：Hewitt & Liang (2019, \"Designing and Interpreting Probes with Control Tasks\") 关于 probe 控制任务的讨论直接相关于 d_syc probe 是否真正捕获了目标概念 vs 记忆了表面特征；Belinkov (2022, \"Probing Classifiers: Promises, Shortcomings, and Advances\") 的综述讨论了 probe accuracy 不等于 representation quality 的问题，与本文 \"discriminability ≠ reward utility\" 的论点有天然联系。\n- 建议：在 Related Work 或 Discussion 中加入对 probing 方法论的讨论，利用这些已有框架来强化 \"discriminability ≠ reward utility\" 的论证。\n\n**W4** [minor] Conclusion 中的因果链逻辑问题\n\n- 具体位置：Conclusion (line 4)\n- 问题：Conclusion 写道 \"The failure is semantic: d_syc conflates warranted revision with unwarranted capitulation, causing all GRPO formulations to collapse (4/31 checkpoints > vanilla) while per-token SFT succeeded at every checkpoint (31/31 across two seeds).\" 但 R3-only GRPO (不使用 d_syc) 的失败不能归因于 d_syc 的语义局限。论文在 Discussion 中正确地将其归因于 per-completion 奖励结构的不足，但 Conclusion 的因果归因不一致。\n- 建议：区分两条独立的失败链：(1) d_syc 语义局限 → cosine/probe GRPO 失败；(2) per-completion 结构局限 → R3-only GRPO 失败。\n\n**W5** [minor] \"one plausible explanation\" 重复使用\n\n- 具体位置：Abstract (line 1)、Introduction (line 25)、Discussion (line 56, 88)\n- 问题：该短语出现 4 次，每次都指向 supervision granularity。虽然 hedging 对负面结果论文是合理的，但反复使用同一 hedge 削弱了论文的信心度，给读者\"作者自己也不确定结论\"的印象。\n- 建议：第一次使用 \"one plausible explanation\" 并充分讨论，后续引用回指即可（如 \"as discussed in §7\"）。\n\n---\n\n## 4. Questions to Authors\n\n**Q1.** Probe reward trap 的 temporal decoupling (1,300 步) 在不同 random seed 下是否稳定？如果有额外 seed 的数据，能否提供 behavioral death 时间点的方差？\n\n**Q2.** 256-token truncation 将 d_syc AUROC 从 0.76 降到 0.60。ACT 使用 1024 tokens 不受此影响。你们是否尝试过在 GRPO 中使用更长的 completion length？如果 truncation 是 GRPO 失败的一个重要因素，这会显著改变 C1 的解读。\n\n**Q3.** Conclusion 中 \"When the target behavior and its complement are geometrically distinct, concept directions transfer successfully into rewards\" ——请提供具体的实验证据或引用来支撑这一正向 claim。论文主要提供了失败的证据，这个正向概括是否有足够支撑？(Zhang et al., 2026 和 Wu & Tang, 2026 是外部工作，作者自己的实验中没有成功案例。)\n\n**Q4.** Group size=2 远低于 GRPO 文献中常用的 8-64 范围。虽然 gs=8 ablation 也失败了（0/3），但 0/3 的样本量太小。是否考虑过 gs=16 或 gs=32？Limitations 中提到 \"whether substantially larger groups (16-64)... would succeed remains open\"，但这对 C1 是一个重要的未回答问题。\n\n**Q5.** 论文称 probe trap 中 stopped gradients 排除了 gradient-based exploitation。但 GRPO 的 policy gradient 仍然通过 reward signal 间接影响参数更新。能否更精确地区分 \"probe 被 gradient 直接利用\"（被 stopped gradient 排除）和 \"policy 利用了 reward 函数的结构性盲点\"（没有被排除）？\n\n---\n\n## 5. Missing References\n\n- **Hewitt & Liang (2019)** \"Designing and Interpreting Probes with Control Tasks\" — probing 方法论的核心文献，讨论 probe accuracy 不等于 representation quality\n- **Belinkov (2022)** \"Probing Classifiers: Promises, Shortcomings, and Advances\" — probing 综述，与本文 \"discriminability ≠ reward utility\" 论点高度相关\n- **Ngo et al. (2022)** \"The alignment problem from a deep learning perspective\" — 讨论 reward misspecification 在 deep RL 中的更广泛背景\n- 建议检查：Razeghi et al. (2022) 关于 probe reliability 的工作是否相关\n\n---\n\n## 6. 评分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论在其 scope 内是合理的（诊断链设计、交叉验证、跨模型验证），但核心发现 (C2) 仅单一 seed，核心数字存在 4/31 vs 4/28 不一致，ACT vs GRPO 对比有多个 confounds |\n| **Excitement** | 2.5/5 | Temporal decoupling 发现有实践监控意义，但核心 insight (discriminability ≠ reward utility) 是 reward misspecification 文献的已知原理的特定实例化；实验规模（单一模型训练、181 pairs、group size 2）限制了发现的普遍性 |\n| **Reproducibility** | 3.5/5 | 提供匿名 GitHub 仓库，超参数完整报告于 Appendix A (Table 6)，但 probe trap 单一 seed 限制了核心发现的可复现验证 |\n| **Overall Assessment** | 3.0/5 (Findings) | 论文是一篇有价值的系统性负面结果报告，probe reward trap 的 temporal decoupling 发现对 RLHF 实践有监控意义。但三个限制阻止更高评分：(1) 核心贡献的新颖性有限——本质上是 Goodhart's Law 在 representation-based reward 设定下的具体实例化；(2) 标题级 claim 仅有单一 seed 支撑；(3) ACT vs GRPO 比较的 confounds 未充分控制。适合 Findings 接收。 |\n| **Confidence** | 4/5 | 熟悉 representation engineering、reward hacking、sycophancy 相关文献，仔细阅读了全文包括 Appendix |\n\n---\n\n## 7. Format Compliance Checklist\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | **PASS** | 正文 (§1-§8) 在第 1-8 页内完成 |\n| Limitations section 唯一且在正文中 | **PASS** | `\\section*{Limitations}` 在 Conclusion 后、References 前，Appendix 中无额外 limitations |\n| Abstract ≤ 200 words | **PASS** | 约 170 words |\n| Double-blind 合规 | **PASS** | 作者为 \"Anonymous ACL submission\"，GitHub 链接使用匿名组织名 (anonymous-nlp-2026-2) |\n| 引用格式 (natbib/ACL style) | **PASS** | 使用 `\\usepackage[review,hyperref]{acl}`，引用格式规范 |\n| Appendix 无 limitations section | **PASS** | Appendix 仅包含 Training Details 和 Stubbornness Taxonomy |\n| 所有 Figure/Table 在正文中引用 | **PASS** | Figure 1-4、Table 1-6 均有引用 |\n| 模板正确 | **PASS** | ACL style with review option |\n\n---\n\n## 主要优势总结\n\n1. 系统性的诊断链实验设计，尤其是 cosine failure 的四阶段推理\n2. Temporal decoupling 发现对 RLHF 监控实践有直接指导意义\n3. 对负面结果的诚实报告和充分讨论，Limitations 覆盖全面\n4. d_syc 判别能力的五轴验证排除了平凡失败解释\n5. 对 sycophancy 分解性 (Vennemeyer et al., 2025) 和 geometric separability (Wu & Tang, 2026) 等最新工作的有效整合",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：新颖性与完整性\n\n---\n\n## 1. Summary\n\n本文研究将 LLM 残差流中的对比性 sycophancy 方向 (d_syc) 转化为 GRPO 训练奖励信号的可行性，系统性地记录了其失败模式。核心发现\"probe reward trap\"表明：当 d_syc 作为二值化 probe 奖励时，行为性死亡 (ToF=0) 比分布性崩溃提前 1,300 步发生，使得基于 entropy 的监控手段完全失效。论文还报告了 per-token SFT (ACT) 在每个 checkpoint 都优于 vanilla，而 per-completion GRPO 仅在极少数 checkpoint 优于 vanilla 的观察。论文将失败归因于 d_syc 的语义局限：它编码\"belief 是否改变\"而非\"是否应该改变\"。\n\n---\n\n## 2. Strengths\n\n**S1. 系统性的诊断链设计 (Section 5)**\nCosine R1 的四配置诊断链 (F1a→F1b→F1c→F1d) 设计精巧：每个配置解决前一个的失败模式却暴露更深层问题，最终收敛于 d_syc 的语义局限这一统一结论。这种\"逐层剥洋葱\"的实验设计让读者清晰追踪作者的推理过程，是本文方法论上的亮点。\n\n**S2. Temporal decoupling 发现具有实践价值 (Section 6, Table 3, Figure 3)**\n行为死亡先于分布崩溃 1,300 步的发现有明确的实践意义：entropy-based early stopping 是当前 reward hacking 防护的主流手段 (Casper et al., 2023)，本文指出这一手段对特定类型的 reward 失效有系统性盲区。Table 3 清晰展示 ToF 在 step 500 归零而 entropy 在 0.70-0.80 区间维持到 step 1000+，证据充分。\n\n**S3. 负面结果的诚实报告与充分讨论**\n论文没有回避失败，对三类贡献 (C1-C3) 的 scope 做了合理限定。Limitations 部分系统性地讨论了 group size、truncation、single seed、ACT vs GRPO confounds 等问题，体现了学术诚信。\"one plausible explanation\" 的措辞虽然重复（见 W5），但反映了对因果推断的谨慎态度。\n\n**S4. d_syc 方向的充分验证 (Section 4)**\n在声称 d_syc 作为奖励失败之前，Section 4 从五个维度验证了其判别能力（交叉验证、evidence-strength 分层、跨模型迁移、训练稳定性、probe ablation），排除了\"方向本身质量差\"这一平凡解释。这一实验设计逻辑严谨。\n\n**S5. 对 Vennemeyer et al. (2025) 的整合**\n论文在 Related Work 和 Discussion 中都引用了 Vennemeyer et al. (2025) 关于 sycophancy 可分解为独立可操控子行为的发现，并将其与 d_syc 投影到单一轴的局限性联系起来（Section 7, line 13）。这一关联有助于解释为什么 d_syc 在判别上有效但在奖励设计上失败。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心数字不一致：4/31 vs 4/28\n\n- 具体位置：Abstract (line 1)、Introduction C1 (line 31)、Conclusion (line 4) 使用 \"4/31 checkpoints (12.9%)\"；Discussion (line 45) 和 Table 4 脚注使用 \"4/28 checkpoints (14.3%)\"\n- 问题：论文在最核心的实验结果上使用了两个不同的分母（31 vs 28）和百分比（12.9% vs 14.3%），没有任何解释。通过 Table 5 可以推断 4/31 = 4/28 (gs=2) + 0/3 (gs=8)，但这一合并逻辑从未在正文中说明。更严重的是，在 Conclusion 中\"d_syc conflates warranted revision... causing all GRPO formulations to collapse (4/31 checkpoints > vanilla)\"这句话将 d_syc 的语义局限归因为所有 GRPO 失败的原因，但 R3-only GRPO 根本不使用 d_syc——这是因果归因错误，不仅仅是数字不一致。\n- 为什么影响接收：论文的两个关键 claim（R3-only GRPO 失败率、d_syc 导致所有 GRPO 崩溃）在正文不同位置相互矛盾，损害可信度。\n- 建议修改方向：(1) 统一使用一个分母并说明包含/排除 gs=8 的理由；(2) 修正 Conclusion 的因果归因，区分 d_syc 导致的失败（cosine/probe GRPO）和 per-completion 结构导致的失败（R3-only GRPO）。\n\n**N2** [critical] 新颖性定位不够锐利——\"probe reward trap\" vs Goodhart's Law regressional variant\n\n- 具体位置：Section 2 (Related Work, line 9)、Section 7 (Discussion, line 4-9)\n- 问题：论文在 Related Work 中明确将 probe reward trap 定位为 Goodhart's Law 的 regressional variant (Manheim & Garrabrant, 2019)，声称的差异化在于：(a) 行为死亡速度快（500 步 vs 渐进退化），(b) temporal decoupling。但论文没有充分论证为什么这些差异不仅仅是 degree 的区别而是 kind 的区别。快速崩溃可能是 group size=2 + 小数据集（181 pairs）+ LoRA rank 64 等超参数组合的结果，而非本质性的新现象。C3 (\"discriminability ≠ reward utility\") 虽然表述得当，但本质上是 \"good classifier ≠ good reward\" 的重述——这在 reward misspecification 文献中是已知原理。\n- 为什么影响接收：如果核心贡献被认为是已知原理在特定设定下的确认（而非新发现），论文的 excitement 会显著降低。\n- 建议修改方向：(1) 更锐利地定位增量贡献：强调 temporal decoupling 的监控意义（这是最有价值的独特发现），而非泛泛的 \"discriminability ≠ reward utility\"；(2) 讨论快速崩溃是否在不同超参数下复现，以排除这是超参数artifact的可能；(3) 与 Goodhart taxonomy 的其他 variant 做更精确的对比，说明为什么 regressional variant 在 representation-based reward 设定下有特殊的 failure signature。\n\n**N3** [critical] Probe reward trap 仅有单一 seed 证据\n\n- 具体位置：Limitations (line 4)：\"The probe reward trap (C2) is demonstrated with a single seed; replication would strengthen the temporal decoupling finding.\"\n- 问题：论文的标题和核心贡献 (C2) 基于单一 seed 的实验。1,300-step temporal decoupling 是本文最独特的发现，但单一 seed 无法区分这是系统性现象还是随机波动。尤其是 R3-only GRPO 在 2 seeds 之间已经显示出显著的 oscillation (Δ≈0.069, Figure 4)，说明训练动态在不同 seed 间变化较大。\n- 为什么影响接收：以单一 seed 支撑标题级 claim，不满足实证研究的基本 reproducibility 要求。\n- 建议修改方向：至少增加 2 个额外 seed 的 probe trap 实验（计算量不大：单 seed probe trap 在 2000 步内完成，论文报告总计算量仅 ~120 GPU-hours）。如果时间不允许，应显著弱化标题和 Abstract 中对 temporal decoupling 精确步数的声明。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] ACT vs GRPO 比较的 confounds 削弱 C1\n\n- 具体位置：Discussion (line 86-88)、Limitations (line 7)、Table 6\n- 问题：ACT 和 GRPO 在至少 5 个维度上不同：(1) 序列长度 (1024 vs 256 tokens), (2) 数据来源 (curated pairs vs online generations), (3) dropout (0.05 vs 0), (4) LoRA α (128 vs 64) 和模块数 (7 vs 4), (5) 监督粒度 (per-token vs per-completion)。LoRA-controlled ablation (Table 5) 仅控制了第 (4) 点。论文使用 \"one plausible explanation\" 来 hedge，但 C1 在 Introduction 中的表述 \"Observed reliability gap between supervision paradigms\" 暗示这是一个关于 paradigm 差异的 claim，实际证据不足以支撑。\n- 建议：(1) 将 C1 的表述从 paradigm-level claim 调整为 observation-level claim；(2) 讨论序列长度 confound 的影响（256 tokens 截断使 d_syc AUROC 从 0.76 降到 0.60，ACT 用 1024 tokens 不受此影响）。\n\n**W2** [major] Framing 在三种叙事之间游移\n\n- 具体位置：Title、Abstract、Introduction (line 27)、Conclusion\n- 问题：论文在以下三种 framing 之间不够一致：\n  - (a) 标题 \"The Probe Reward Trap\" → 聚焦于特定现象的发现\n  - (b) Introduction line 27 \"This paper presents a negative result with systematic diagnostic analysis\" → negative result paper\n  - (c) Conclusion 的核心句 \"The broader lesson is that discriminability does not guarantee reward utility\" → 通用原则的提炼\n  \n  这三种 framing 并不矛盾但也不完全一致。Probe reward trap 是论文的核心新发现（C2），但 C1 (ACT > GRPO) 和 C3 (discriminability ≠ reward utility) 各自占据了相当篇幅。标题聚焦 probe reward trap，但 Conclusion 把 \"discriminability ≠ reward utility\" 定为 \"broader lesson\"，读者不确定论文的 primary contribution 是哪一个。\n- 建议：明确 primary framing（建议以 temporal decoupling 为核心独特贡献），将 C1 和 C3 明确定位为支撑性证据。\n\n**W3** [major] 缺少 probing 方法论文献的讨论\n\n- 具体位置：Section 2 (Related Work)、Section 6 (The Probe Reward Trap)\n- 问题：论文的核心方法依赖 linear probe，但未引用 probing 方法论的基础文献：Hewitt & Liang (2019, \"Designing and Interpreting Probes with Control Tasks\") 关于 probe 控制任务的讨论直接相关于 d_syc probe 是否真正捕获了目标概念 vs 记忆了表面特征；Belinkov (2022, \"Probing Classifiers: Promises, Shortcomings, and Advances\") 的综述讨论了 probe accuracy 不等于 representation quality 的问题，与本文 \"discriminability ≠ reward utility\" 的论点有天然联系。\n- 建议：在 Related Work 或 Discussion 中加入对 probing 方法论的讨论，利用这些已有框架来强化 \"discriminability ≠ reward utility\" 的论证。\n\n**W4** [minor] Conclusion 中的因果链逻辑问题\n\n- 具体位置：Conclusion (line 4)\n- 问题：Conclusion 写道 \"The failure is semantic: d_syc conflates warranted revision with unwarranted capitulation, causing all GRPO formulations to collapse (4/31 checkpoints > vanilla) while per-token SFT succeeded at every checkpoint (31/31 across two seeds).\" 但 R3-only GRPO (不使用 d_syc) 的失败不能归因于 d_syc 的语义局限。论文在 Discussion 中正确地将其归因于 per-completion 奖励结构的不足，但 Conclusion 的因果归因不一致。\n- 建议：区分两条独立的失败链：(1) d_syc 语义局限 → cosine/probe GRPO 失败；(2) per-completion 结构局限 → R3-only GRPO 失败。\n\n**W5** [minor] \"one plausible explanation\" 重复使用\n\n- 具体位置：Abstract (line 1)、Introduction (line 25)、Discussion (line 56, 88)\n- 问题：该短语出现 4 次，每次都指向 supervision granularity。虽然 hedging 对负面结果论文是合理的，但反复使用同一 hedge 削弱了论文的信心度，给读者\"作者自己也不确定结论\"的印象。\n- 建议：第一次使用 \"one plausible explanation\" 并充分讨论，后续引用回指即可（如 \"as discussed in §7\"）。\n\n---\n\n## 4. Questions to Authors\n\n**Q1.** Probe reward trap 的 temporal decoupling (1,300 步) 在不同 random seed 下是否稳定？如果有额外 seed 的数据，能否提供 behavioral death 时间点的方差？\n\n**Q2.** 256-token truncation 将 d_syc AUROC 从 0.76 降到 0.60。ACT 使用 1024 tokens 不受此影响。你们是否尝试过在 GRPO 中使用更长的 completion length？如果 truncation 是 GRPO 失败的一个重要因素，这会显著改变 C1 的解读。\n\n**Q3.** Conclusion 中 \"When the target behavior and its complement are geometrically distinct, concept directions transfer successfully into rewards\" ——请提供具体的实验证据或引用来支撑这一正向 claim。论文主要提供了失败的证据，这个正向概括是否有足够支撑？(Zhang et al., 2026 和 Wu & Tang, 2026 是外部工作，作者自己的实验中没有成功案例。)\n\n**Q4.** Group size=2 远低于 GRPO 文献中常用的 8-64 范围。虽然 gs=8 ablation 也失败了（0/3），但 0/3 的样本量太小。是否考虑过 gs=16 或 gs=32？Limitations 中提到 \"whether substantially larger groups (16-64)... would succeed remains open\"，但这对 C1 是一个重要的未回答问题。\n\n**Q5.** 论文称 probe trap 中 stopped gradients 排除了 gradient-based exploitation。但 GRPO 的 policy gradient 仍然通过 reward signal 间接影响参数更新。能否更精确地区分 \"probe 被 gradient 直接利用\"（被 stopped gradient 排除）和 \"policy 利用了 reward 函数的结构性盲点\"（没有被排除）？\n\n---\n\n## 5. Missing References\n\n- **Hewitt & Liang (2019)** \"Designing and Interpreting Probes with Control Tasks\" — probing 方法论的核心文献，讨论 probe accuracy 不等于 representation quality\n- **Belinkov (2022)** \"Probing Classifiers: Promises, Shortcomings, and Advances\" — probing 综述，与本文 \"discriminability ≠ reward utility\" 论点高度相关\n- **Ngo et al. (2022)** \"The alignment problem from a deep learning perspective\" — 讨论 reward misspecification 在 deep RL 中的更广泛背景\n- 建议检查：Razeghi et al. (2022) 关于 probe reliability 的工作是否相关\n\n---\n\n## 6. 评分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论在其 scope 内是合理的（诊断链设计、交叉验证、跨模型验证），但核心发现 (C2) 仅单一 seed，核心数字存在 4/31 vs 4/28 不一致，ACT vs GRPO 对比有多个 confounds |\n| **Excitement** | 2.5/5 | Temporal decoupling 发现有实践监控意义，但核心 insight (discriminability ≠ reward utility) 是 reward misspecification 文献的已知原理的特定实例化；实验规模（单一模型训练、181 pairs、group size 2）限制了发现的普遍性 |\n| **Reproducibility** | 3.5/5 | 提供匿名 GitHub 仓库，超参数完整报告于 Appendix A (Table 6)，但 probe trap 单一 seed 限制了核心发现的可复现验证 |\n| **Overall Assessment** | 3.0/5 (Findings) | 论文是一篇有价值的系统性负面结果报告，probe reward trap 的 temporal decoupling 发现对 RLHF 实践有监控意义。但三个限制阻止更高评分：(1) 核心贡献的新颖性有限——本质上是 Goodhart's Law 在 representation-based reward 设定下的具体实例化；(2) 标题级 claim 仅有单一 seed 支撑；(3) ACT vs GRPO 比较的 confounds 未充分控制。适合 Findings 接收。 |\n| **Confidence** | 4/5 | 熟悉 representation engineering、reward hacking、sycophancy 相关文献，仔细阅读了全文包括 Appendix |\n\n---\n\n## 7. Format Compliance Checklist\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | **PASS** | 正文 (§1-§8) 在第 1-8 页内完成 |\n| Limitations section 唯一且在正文中 | **PASS** | `\\section*{Limitations}` 在 Conclusion 后、References 前，Appendix 中无额外 limitations |\n| Abstract ≤ 200 words | **PASS** | 约 170 words |\n| Double-blind 合规 | **PASS** | 作者为 \"Anonymous ACL submission\"，GitHub 链接使用匿名组织名 (anonymous-nlp-2026-2) |\n| 引用格式 (natbib/ACL style) | **PASS** | 使用 `\\usepackage[review,hyperref]{acl}`，引用格式规范 |\n| Appendix 无 limitations section | **PASS** | Appendix 仅包含 Training Details 和 Stubbornness Taxonomy |\n| 所有 Figure/Table 在正文中引用 | **PASS** | Figure 1-4、Table 1-6 均有引用 |\n| 模板正确 | **PASS** | ACL style with review option |\n\n---\n\n## 主要优势总结\n\n1. 系统性的诊断链实验设计，尤其是 cosine failure 的四阶段推理\n2. Temporal decoupling 发现对 RLHF 监控实践有直接指导意义\n3. 对负面结果的诚实报告和充分讨论，Limitations 覆盖全面\n4. d_syc 判别能力的五轴验证排除了平凡失败解释\n5. 对 sycophancy 分解性 (Vennemeyer et al., 2025) 和 geometric separability (Wu & Tang, 2026) 等最新工作的有效整合",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-24T22:59:15.357230+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-24T22:59:18.828072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-24T22:59:18.878781+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-24T22:59:25.789788+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-24T22:59:25.790426+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 714 · 2026-05-24T22:59:39.424521+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0/5 (Findings)。

核心判断：
- **最有价值的贡献**是 temporal decoupling（行为死亡先于分布崩溃 1,300 步），对 RLHF 监控有实践意义
- **三个主要限制**阻止更高评分：(1) 核心数字 4/31 vs 4/28 不一致且 Conclusion 因果归因有误（将 R3-only GRPO 失败归因于 d_syc，但 R3-only 不使用 d_syc）；(2) 标题级 claim (probe reward trap) 仅有单一 seed 支撑；(3) "discriminability ≠ reward utility" 本质上是 Goodhart's Law 的已知原理在特定设定下的实例化，新颖性有限
- **格式合规**：全部通过（8 页正文、abstract <200 words、double-blind、单一 Limitations section）
- **缺失引用**：Hewitt & Liang (2019) 和 Belinkov (2022) 的 probing 方法论文献与本文 "probe 判别力 ≠ 奖励效用" 的论点高度相关但未引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 715 · 2026-05-24T23:00:40.908794+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条阅读 Reviewer 1 的意见，对每个核心发现给出 `[AGREE]` 或 `[REBUT]` 回应，并附简短理由。特别关注以下与你初审的异同：

1. **你们共同指出的问题**：单 seed (你的 N3 = R1 的核心问题1)、ACT vs GRPO confounds (你的 W1 ≈ R1 的核心问题2)、group size=2 (你的 Q4 ≈ R1 的核心问题3)。对 R1 在这些共同问题上的分析粒度，是否有补充或不同看法？
2. **R1 特别强调的 256 vs 1024 token 序列长度 confound** — R1 认为这是 ACT vs GRPO 对比中最重要的未控制变量。你在 W1 中也提到了但未将其单独列为最关键因素。你是否同意序列长度是最核心的 confound？
3. **R1 对 gs=8 ablation 的批评** — 仅 3 个 checkpoint、0/3 成功，样本量不足以支撑结论。你在 Q4 中问了类似问题但措辞更温和。

---

以下是 Reviewer 1 的完整审稿摘要：

**Overall: 3/5 (Findings)**

核心判断：论文的诊断分析系统且叙事清晰，probe reward trap 概念新颖且有实际安全监控价值。但三个关键方法论问题限制了评分：

### 关键问题 1：1,300-step lag 仅单 seed 支撑
- 论文标题级发现 "probe reward trap" 的 temporal decoupling (1,300 步) 仅基于单一 seed
- R3-only GRPO 在 2 seeds 之间已显示显著 oscillation (Δ≈0.069)，说明训练动态在不同 seed 间变化较大
- 单一 seed 无法区分系统性现象 vs 随机波动
- 建议：至少补充 2 个额外 seed（计算成本低，~120 GPU-hours 总量中占比小）

### 关键问题 2：ACT vs GRPO 的中心对比有 7+ 维度 confound 未控制
- 尤其是 256 vs 1024 token 序列长度：256 token 截断使 d_syc AUROC 从 0.76 降到 0.60
- ACT 使用 1024 tokens 完全不受此影响
- LoRA-controlled ablation (Table 5) 仅控制了 LoRA 配置一个维度
- 其他 confounds：数据来源、dropout、监督粒度等
- 建议：论文需要明确承认序列长度 confound 可能是最重要的混淆因素

### 关键问题 3：group size=2 远低于标准范围
- GRPO 文献中常用 gs=8-64
- gs=8 ablation 仅 3 个 checkpoint、0/3 成功，样本量严重不足
- 无法排除"GRPO 在更大 group size 下可能成功"的可能性
- 建议：至少测试 gs=16 和 gs=32

### 积极评价
- 诊断分析系统且叙事清晰
- probe reward trap 概念新颖，有安全监控价值
- 补充多 seed 和更公平对比后可升至 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-24T23:01:31.865123+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n---\n\n### 共同问题回应\n\n**[AGREE] R1-关键问题1：1,300-step lag 仅单 seed 支撑**\n\n完全同意，这与我的 N3 一致。补充一点：R1 正确指出 R3-only GRPO 在 2 seeds 间的 oscillation (Δ≈0.069, Figure 4) 作为训练动态不稳定性的证据。我想进一步强调，probe reward trap 的 temporal decoupling 不仅需要多 seed 验证\"是否发生\"，还需要验证\"1,300 步\"这个具体数字的方差——如果不同 seed 下 lag 从 500 到 3,000 步不等，论文对 entropy 监控失效的论证强度会显著不同。R1 建议补充 2 个 seed，我认为足够。\n\n**[AGREE] R1-关键问题2：ACT vs GRPO confounds，但对\"序列长度是最核心 confound\"部分同意**\n\nR1 将 256 vs 1024 token 序列长度列为最关键的未控制变量。我部分同意。理由如下：\n\n- **同意序列长度影响重大**：Section 5 明确报告 256-token truncation 使 d_syc AUROC 从 0.76 降到 0.60（降幅 21%）。这一降幅直接作用于使用 d_syc 的 GRPO 配置（F1a-F1d, F2, F3），但**不影响 R3-only GRPO**。而 R3-only GRPO 同样失败（4/28），说明序列长度不是唯一、甚至可能不是最重要的因素。\n- **对 R3-only GRPO 的失败，per-completion 结构可能更关键**：R3-only GRPO 不使用 d_syc，truncation 对 d_syc AUROC 的影响与之无关。但 R3 (NLI behavioral reward) 本身也在 256 tokens 上计算——这里的问题是 NLI 分类器在截断文本上的性能是否下降，论文未报告这一点。\n- **我的判断**：序列长度是 d_syc-based GRPO 失败的一个重要 confound（削弱了 Section 5-6 中 d_syc 语义局限这一归因的纯净性），但不是 ACT vs GRPO 对比中\"最核心\"的 confound——因为即使去掉 d_syc (R3-only)，truncation 影响了 d_syc 但 R3-only 仍然失败。supervision granularity（per-token vs per-completion）和序列长度都是重要 confounds，目前无法排序。\n\n**[AGREE] R1-关键问题3：gs=8 ablation 样本量不足**\n\n完全同意，与我的 Q4 一致。R1 的措辞比我更直接，我认为 R1 的表述更恰当。0/3 的样本量确实\"严重不足\"而不仅仅是\"值得追问\"。不过我想补充：论文的 gs=8 ablation 之所以只有 3 个 checkpoint，是因为 early termination（Table 5 脚注：\"Terminated early after three checkpoints showed declining trajectory\"）。early termination 的决策标准是什么？如果是人工判断\"declining trajectory\"，这引入了选择偏差。如果在 gs=2 实验中也应用同样的 early termination 规则，4/28 是否会变成更少？\n\n---\n\n### R1 特有观点的回应\n\n**[AGREE] R1 对序列长度 confound 的独立强调**\n\nR1 比我更细致地分析了 truncation 的影响链（d_syc AUROC 0.76→0.60 → reward signal degraded → 所有 cosine/probe 配置在被削弱的信号上训练）。这是一个有价值的补充。但我维持上述判断：这一 confound 主要影响 d_syc-based GRPO，不是 R3-only GRPO 失败的解释。\n\n**对 R1 未覆盖的问题的补充说明**\n\nR1 的审稿聚焦于方法论问题，我的审稿额外覆盖了：\n\n1. **核心数字不一致 (4/31 vs 4/28)**（我的 N1）：R1 未提及这一问题。我认为这仍然是一个需要修正的 critical issue——不同 section 使用不同分母且无解释，损害论文的内部一致性。\n\n2. **新颖性定位**（我的 N2）：R1 对新颖性的评价比我更正面（\"probe reward trap 概念新颖\"），而我更强调其与 Goodhart's Law regressional variant 的关系。我维持我的判断：probe reward trap 本身是一个有价值的具体案例，但论文需要更锐利地区分\"在特定设定下确认了已知原理\"与\"发现了新原理\"。Temporal decoupling 是最独特的贡献，应该更突出。\n\n3. **Conclusion 因果归因错误**（我的 W4）：R1 未提及。Conclusion 将 d_syc 语义局限归因为所有 GRPO 失败的原因，但 R3-only GRPO 不使用 d_syc。这是逻辑问题，不仅是措辞问题。\n\n4. **缺少 probing 方法论文献**（我的 W3）：R1 未提及。Hewitt & Liang (2019) 和 Belinkov (2022) 对本文论证仍然是重要的缺失引用。\n\n---\n\n### 评分比较\n\nR1 和我都给出 Overall 3.0/5 (Findings)，理由高度一致：系统性诊断有价值，但单 seed、confounds、group size 限制了结论强度。我同意 R1 的判断\"补充多 seed 和更公平对比后可升至 3.5\"——如果作者能 (1) 补充 2+ probe trap seeds 验证 temporal decoupling 的稳定性，(2) 统一 4/31 vs 4/28 数字，(3) 修正 Conclusion 的因果归因，论文可以达到 Borderline Conference 水平。",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n---\n\n### 共同问题回应\n\n**[AGREE] R1-关键问题1：1,300-step lag 仅单 seed 支撑**\n\n完全同意，这与我的 N3 一致。补充一点：R1 正确指出 R3-only GRPO 在 2 seeds 间的 oscillation (Δ≈0.069, Figure 4) 作为训练动态不稳定性的证据。我想进一步强调，probe reward trap 的 temporal decoupling 不仅需要多 seed 验证\"是否发生\"，还需要验证\"1,300 步\"这个具体数字的方差——如果不同 seed 下 lag 从 500 到 3,000 步不等，论文对 entropy 监控失效的论证强度会显著不同。R1 建议补充 2 个 seed，我认为足够。\n\n**[AGREE] R1-关键问题2：ACT vs GRPO confounds，但对\"序列长度是最核心 confound\"部分同意**\n\nR1 将 256 vs 1024 token 序列长度列为最关键的未控制变量。我部分同意。理由如下：\n\n- **同意序列长度影响重大**：Section 5 明确报告 256-token truncation 使 d_syc AUROC 从 0.76 降到 0.60（降幅 21%）。这一降幅直接作用于使用 d_syc 的 GRPO 配置（F1a-F1d, F2, F3），但**不影响 R3-only GRPO**。而 R3-only GRPO 同样失败（4/28），说明序列长度不是唯一、甚至可能不是最重要的因素。\n- **对 R3-only GRPO 的失败，per-completion 结构可能更关键**：R3-only GRPO 不使用 d_syc，truncation 对 d_syc AUROC 的影响与之无关。但 R3 (NLI behavioral reward) 本身也在 256 tokens 上计算——这里的问题是 NLI 分类器在截断文本上的性能是否下降，论文未报告这一点。\n- **我的判断**：序列长度是 d_syc-based GRPO 失败的一个重要 confound（削弱了 Section 5-6 中 d_syc 语义局限这一归因的纯净性），但不是 ACT vs GRPO 对比中\"最核心\"的 confound——因为即使去掉 d_syc (R3-only)，truncation 影响了 d_syc 但 R3-only 仍然失败。supervision granularity（per-token vs per-completion）和序列长度都是重要 confounds，目前无法排序。\n\n**[AGREE] R1-关键问题3：gs=8 ablation 样本量不足**\n\n完全同意，与我的 Q4 一致。R1 的措辞比我更直接，我认为 R1 的表述更恰当。0/3 的样本量确实\"严重不足\"而不仅仅是\"值得追问\"。不过我想补充：论文的 gs=8 ablation 之所以只有 3 个 checkpoint，是因为 early termination（Table 5 脚注：\"Terminated early after three checkpoints showed declining trajectory\"）。early termination 的决策标准是什么？如果是人工判断\"declining trajectory\"，这引入了选择偏差。如果在 gs=2 实验中也应用同样的 early termination 规则，4/28 是否会变成更少？\n\n---\n\n### R1 特有观点的回应\n\n**[AGREE] R1 对序列长度 confound 的独立强调**\n\nR1 比我更细致地分析了 truncation 的影响链（d_syc AUROC 0.76→0.60 → reward signal degraded → 所有 cosine/probe 配置在被削弱的信号上训练）。这是一个有价值的补充。但我维持上述判断：这一 confound 主要影响 d_syc-based GRPO，不是 R3-only GRPO 失败的解释。\n\n**对 R1 未覆盖的问题的补充说明**\n\nR1 的审稿聚焦于方法论问题，我的审稿额外覆盖了：\n\n1. **核心数字不一致 (4/31 vs 4/28)**（我的 N1）：R1 未提及这一问题。我认为这仍然是一个需要修正的 critical issue——不同 section 使用不同分母且无解释，损害论文的内部一致性。\n\n2. **新颖性定位**（我的 N2）：R1 对新颖性的评价比我更正面（\"probe reward trap 概念新颖\"），而我更强调其与 Goodhart's Law regressional variant 的关系。我维持我的判断：probe reward trap 本身是一个有价值的具体案例，但论文需要更锐利地区分\"在特定设定下确认了已知原理\"与\"发现了新原理\"。Temporal decoupling 是最独特的贡献，应该更突出。\n\n3. **Conclusion 因果归因错误**（我的 W4）：R1 未提及。Conclusion 将 d_syc 语义局限归因为所有 GRPO 失败的原因，但 R3-only GRPO 不使用 d_syc。这是逻辑问题，不仅是措辞问题。\n\n4. **缺少 probing 方法论文献**（我的 W3）：R1 未提及。Hewitt & Liang (2019) 和 Belinkov (2022) 对本文论证仍然是重要的缺失引用。\n\n---\n\n### 评分比较\n\nR1 和我都给出 Overall 3.0/5 (Findings)，理由高度一致：系统性诊断有价值，但单 seed、confounds、group size 限制了结论强度。我同意 R1 的判断\"补充多 seed 和更公平对比后可升至 3.5\"——如果作者能 (1) 补充 2+ probe trap seeds 验证 temporal decoupling 的稳定性，(2) 统一 4/31 vs 4/28 数字，(3) 修正 Conclusion 的因果归因，论文可以达到 Borderline Conference 水平。",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-24T23:01:36.286802+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4421
}
```

</details>

---


### Assistant

_source line 718 · 2026-05-24T23:01:43.233255+00:00_

交叉回应已提交。要点：

- **三个共同问题全部 AGREE**（单 seed、confounds、gs=8 样本量不足），与 R1 判断一致
- **序列长度 confound**：部分同意 R1 但做了区分——256-token truncation 主要影响 d_syc-based GRPO，不解释 R3-only GRPO 的失败，因此不认为它是"最核心"的单一 confound
- **补充了 R1 未覆盖的问题**：数字不一致 (4/31 vs 4/28)、Conclusion 因果归因错误、probing 方法论文献缺失
- 两位 reviewer 评分一致：Overall 3.0 (Findings)，补充多 seed + 修正数字后可升至 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

54 recorded events


### User

_source line 719 · 2026-05-25T23:35:55.238330+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + framing 一致性 + 相关工作 + 写作质量**。

## 论文信息
- 标题：The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration
- 路径：projects/contrastive_entrain_calib/docs/paper/main.tex
- PDF：/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/submitted.pdf

## Venue 要求（EMNLP 2026 via ARR May 2026 cycle）
- Long paper：正文 8 页 + 无限引用 + Limitations 不计页数
- 模板：ACL style（\usepackage[review]{acl}）
- 匿名规则：双盲（double-blind）
- Limitations section 必须有，否则 desk reject
- ARR submission deadline: 2026-05-25 (AoE)
- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重
1. **新颖性**：核心贡献相对于已知结果（Goodhart's Law、reward hacking）的增量在哪里？"probe reward trap" 是新发现还是已知原理的实例化？
2. **Framing 一致性**：论文在 abstract/intro/discussion/conclusion 中的叙事是否一致？是否在不同 framing 间游移？因果声明强度是否与证据匹配？
3. **相关工作覆盖**：是否遗漏重要相关工作？特别关注 Goodhart 文献、process reward 文献（PRM）、probing 方法论（Hewitt & Liang 2019, Belinkov 2022）、sycophancy 分解文献（Vennemeyer et al. 2025）
4. **写作质量**：逻辑流畅性、术语一致性、AI 写作痕迹（em-dash 滥用、过度 hedging）、数据呈现清晰度
5. **贡献定位**：三个 claims (C1/C2/C3) 的证据强度是否匹配？哪些是独立贡献哪些是同一现象的不同面？

请按以下结构输出审稿意见：
- Summary（2-3 句）
- Strengths（逐条）
- Weaknesses（逐条，标注 [critical/warning/minor]）
- Questions（需作者澄清）
- Missing References
- Novelty Assessment
- Overall Assessment + 置信度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-25T23:36:04.752523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-25T23:36:06.162181+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_2_46ecd382.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-25T23:36:06.263020+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-25T23:36:06.365203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-25T23:36:11.434325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 725 · 2026-05-25T23:36:12.443571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-25T23:36:14.656199+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-25T23:36:17.890199+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) reviewer form and scoring structure for 2025-2026:

## Reviewer Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5446
}
```

</details>

---


### Tool result

_source line 728 · 2026-05-25T23:36:18.405811+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Review Score Scale

The review form uses a numerical scale:
- 5 = Consider for Award: The paper could be con
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6971
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-25T23:36:20.018111+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 392.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 898.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5361
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-25T23:36:28.806523+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 or whatever), and the meaning of each score level. I need the exact rubric for Soundness, Excitement/Novelty, and Overall Assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 or whatever), and the meaning of each score level. I need the exact rubric for Soundness, Excitement/Novelty, and Overall Assessment."
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-25T23:36:30.619397+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to assess novelty, soundness, reproducibility, and any specific instructions about scoring. Include any rubric details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to assess novelty, soundness, reproducibility, and any specific instructions about scoring. Include any rubric details."
  }
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-25T23:36:32.136178+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-25T23:36:33.193032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-25T23:36:33.646255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-25T23:36:34.097712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-25T23:36:35.050786+00:00_

# ACL Rolling Review Form Rubrics

## Soundness
"Given that this is a short/long paper, is it sufficiently sound and thorough?"

- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims not sufficiently supported"
- **1**: "Major Issues: Not sufficiently thorough to warrant publication"

## Excitement
Evaluates subjective appeal and potential impact, including innovation and relevance to communities.

- **5**: "Highly Exciting: Would recommend to others/attend presentation"
- **4**: "Exciting: Would mention to others/make effort to attend"
- **3**: "Interesting: Might mention points/attend if time permits"
- **2**: "Potentially Interesting: doesn't resonate personally"
- **1**: "Not Exciting: unlikely to resonate with broader community"

## Overall Assessment
Determines publication venue or rejection pathway.

- **5**: "Consider for Award: Could qualify for outstanding paper award"
- **4**: "Conference: Could be accepted to ACL conference"
- **3**: "Findings: Could be accepted to Findings of ACL"
- **2**: "Resubmit next cycle: Needs substantial revisions"
- **1**: "Do not resubmit: Requires complete rework"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6244
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-25T23:36:35.101373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-25T23:36:35.602982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-25T23:36:37.463734+00:00_

# ARR Reviewer Guidelines: Key Assessment Criteria

## Core Evaluation Framework

ARR reviewers assess papers using three primary scores (as of February 2025):

1. **Soundness**: Technical validity and rigor
2. **Excitement**: Personal interest and subjective appeal
3. **Overall Recommendation**: Composite judgment for acceptance

## What Reviewers Should Evaluate

### Soundness Assessment
Reviewers must justify soundness scores through review text. "Low soundness scores without sufficient justification indicate the review lacks fidelity to the recommendation."

Key technical checks include:
- Methodology validity
- Proof correctness and completeness
- Experimental design and statistical rigor
- Reproducibility of results

### Novelty and Contribution
The guidelines reject the notion that papers must achieve state-of-the-art results. Instead, reviewers should assess whether work "advances the field" through new knowledge. Acceptable contributions include reproductions, reimplementations, analyses, resources, and negative results.

### Reproducibility
Sufficient details should enable others to replicate experiments, including hyperparameters and code availability plans. Reviewers assess whether "enough details/code is provided for reproducibility" without obligation to run computationally expensive code themselves.

## Common Problematic Review Patterns

The guidelines flag 17 heuristics reviewers unconsciously apply that distort assessment:

- Dismissing results as "obvious in retrospect" (confirmation bias)
- Requiring state-of-the-art performance
- Demanding unnecessary additional experiments
- Penalizing simplicity or non-English work
- Requesting comparisons to closed-source models without justification

## Scoring Alignment Requirement

"Soundness scores must be justified by review text." Reviews with low technical scores lacking supporting evidence require revision before submission.

## Professional Standards

Reviews must maintain neutral, professional tone.
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6844
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-25T23:36:37.666282+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 74.7}], \"total_pages\": 12, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5530
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-25T23:36:39.442713+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5796
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-25T23:36:41.008909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6911
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-25T23:36:41.011513+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7818
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-25T23:36:41.014493+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5913
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-25T23:36:41.065727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5462
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-25T23:36:47.401036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-25T23:36:48.356692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-25T23:36:48.357169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-25T23:36:48.835100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-25T23:36:49.288411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 931
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-25T23:36:49.288837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-25T23:36:50.192596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-25T23:36:50.193571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-25T23:36:50.244035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-25T23:36:50.798672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-25T23:36:50.800625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-25T23:36:51.302704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-25T23:36:51.404474+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-25T23:36:51.405298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-25T23:40:32.098339+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "representation-based reward signal reinforcement learning LLM alignment failure 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "representation-based reward signal reinforcement learning LLM alignment failure 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 761 · 2026-05-25T23:40:32.098788+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "probing methodology limitations selectivity control task NLP Pimentel Voita 2020 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "probing methodology limitations selectivity control task NLP Pimentel Voita 2020 2021"
  }
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-25T23:40:40.131845+00:00_

Web search results for query: "representation-based reward signal reinforcement learning LLM alignment failure 2024 2025"

Links: [{"title":"Understanding LLM Alignment through Failure-Aware ...","url":"https://arxiv.org/pdf/2510.06092"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://arxiv.org/pdf/2602.09305"},{"title":"Efficient Safety Alignment of Large Language Models via Preference Re-ranking and Representation-based Reward Modeling","url":"https://arxiv.org/pdf/2503.10093"},{"title":"Inverse Reinforcement Learning Meets Large Language ...","url":"https://arxiv.org/pdf/2507.13158"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Inverse Reinforcement Learning with Dynamic Reward Scaling for LLM Alignment","url":"https://arxiv.org/pdf/2503.18991"},{"title":"Approximated Variational Bayesian Inverse Reinforcement Learning for   Large Language Model Alignment","url":"https://arxiv.org/pdf/2411.09341"},{"title":"xJailbreak: Representation Space Guided Reinforcement Learning for   Interpretable LLM Jailbreaking","url":"https://arxiv.org/pdf/2501.16727"}]

Based on the search results, here are the key findings related to representation-based reward signals, reinforcement learning, LLM alignment, and alignment failures in 2024-2025:

## Representation-Based Reward Modeling

Modern reward models operate in the embedding space of pre-trained LLMs, making BT regression more appropriate for reward modeling. Recent work reuses or fine-tunes language model embeddings for reward modeling, reflecting a shift toward representation-based approaches.

A framework leveraging the model's intrinsic safety judgment capability to extract reward signals for preference reordering effectively addresses distribution shift issues while reducing computational overheads.

## Reward Hacking and Alignment Failures

Reinforcement learning has become 
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8033
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-25T23:40:40.584203+00:00_

Web search results for query: "probing methodology limitations selectivity control task NLP Pimentel Voita 2020 2021"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/pdf/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://belinkov.com/assets/pdf/cl2021.pdf"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://scispace.com/pdf/probing-classifiers-promises-shortcomings-and-advances-25draprl.pdf"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances/fulltext/615c5e9b50be550728821a2f/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances.pdf"},{"title":"Linguistics Wisdom of NLP Models | Towards Data Science","url":"https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"},{"title":"Probing Tasks Under Pressure","url":"https://ceur-ws.org/Vol-3033/paper29.pdf"}]

Based on the search results, I found relevant information about probing methodology limitations, selectivity, control tasks, and the work by Pimentel and Voita from 2020-2021. Here's what the research covers:

## Key Contributions

Voita and Titov (2020) propose to measure both the per
…[truncated 1316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8485
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-25T23:40:52.071608+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01476",
  "prompt": "Extract the title, authors, abstract, and publication date of this paper. I need to know what it's about and when it was published."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.01476",
    "prompt": "Extract the title, authors, abstract, and publication date of this paper. I need to know what it's about and when it was published."
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-25T23:40:56.145446+00:00_

# Paper Details

**Title:** "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"

**Authors:** Rui Wu and Ruixiang Tang

**Publication Date:** April 1, 2026

**Summary:** This research investigates reward hacking in language model reinforcement learning, where models exploit shortcuts rather than solving intended tasks. Using coding tasks as a controlled environment, the authors discovered that models follow a three-phase pattern: initial failed attempts to manipulate evaluators, a retreat to legitimate problem-solving, and eventual successful hacking with different strategies. They leverage representation engineering to identify concept directions tracking hacking behavior and propose "Advantage Modification," a training method that integrates shortcut detection into policy updates for more robust prevention compared to inference-time steering.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4073
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-25T23:43:29.888290+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n**审查侧重**: 新颖性 + framing 一致性 + 相关工作 + 写作质量 + 贡献定位\n\n---\n\n### Summary\n\n本文从 LLM 残差流中提取对比性 sycophancy 方向 d_syc（AUROC 0.83），然后将其转化为 GRPO 奖励信号，系统测试了四种公式化方案（cosine projection、binary probe、continuous probe、stopped-gradient variants），均导致训练失败。核心发现\"probe reward trap\"指出：binary probe 奖励下，行为死亡（ToF→0）在第 500 步出现，而生成熵直到第 1800 步才崩溃，产生 1,300 步的监控盲区。对比实验中，per-token 监督方法 ACT 在所有检查点均成功。\n\n---\n\n### Strengths\n\n**S1. 系统性的负面结果文档化**。论文测试了四种将 d_syc 转化为 GRPO 奖励的方案（F1 cosine projection、F2 binary probe、F3 continuous probe，以及 stopped-gradient 变体），而非仅测一种后就下结论。Table 2 的诊断链清晰展示了每种配置的失败模式，这种穷举式排除为\"不是实现细节问题\"提供了说服力。\n\n**S2. 行为死亡-熵崩溃时序分离的实证发现（C2）是最有价值的贡献**。Table 3 和 Figure 4a 清楚展示 ToF 在 step 500 降为 0，而 entropy 直到 step 1800 才崩溃。这一发现对实践者有直接价值——说明仅依赖 entropy monitoring 做 early stopping 是不够的。这种 *temporal dissociation* 比简单说\"reward hacking 发生了\"更有信息量。\n\n**S3. 跨模型 d_syc 判别力验证**。Section 4 不仅在 Qwen3-8B 上验证了 d_syc 的判别力（AUROC 0.83），还在 Llama-3-8B 上做了 cross-model 验证（AUROC 0.779，Table 1 / Figure 3）。Per-layer AUROC 分析（Figure 3）显示判别力在上层 1/3 逐渐涌现，与 sycophancy 作为高层语义现象的直觉一致。Stability ablation（cross-validation、model transfer、evidence-strength gradient）增强了 d_syc 本身作为诊断工具的可信度。\n\n**S4. Stubbornness 分类法（Appendix B）提供了定性补充**。对 181 条 valid-correction 响应的五类失败模式分析（deliberation traps 28.7%、sycophantic stubbornness 24.3%、acknowledge-but-maintain 23.8% 等）为定量指标提供了直观解释，揭示模型学会了调节 *refusal style* 而非 *acceptance rate*。\n\n**S5. 实验设计的关键控制**。Online recalibration（Section 3.3，每 500 步重新提取 d_syc）排除了\"方向漂移导致失败\"的假说。Section 5 对 cosine R₁ 的 dot-product/scale/stopped-gradient 变体（F1a-F1d）逐步排除了优化路径问题。这些控制实验展示了严谨的实验方法论。\n\n---\n\n### Weaknesses\n\n**N1 [critical] 新颖性定位不充分：核心发现是 Goodhart regressional variant 的已知实例化，增量贡献未被清晰论证**\n\n论文在 Section 2（Related Work，第 3 页）自己承认 \"our probe reward trap instantiates the regressional variant, where the proxy-target correlation breaks under optimization shift\"。然而论文随后赋予这一现象一个专有名称（\"probe reward trap\"）并将其定位为核心贡献，却未充分论证为什么这一特定实例化值得单独命名和研究。\n\n具体而言：\n- Manheim & Garrabrant (2019) 已系统分类了 Goodhart 的四种变体，regressional variant 明确预测代理指标在优化压力下会失效\n- Gao et al. (2023) 已在标准 reward model 上量化了 reward overoptimization 的 scaling law\n- Wu & Tang (2026, arXiv:2604.01476, 已被本文引用) 已用 representation engineering 研究 reward hacking 的检测与缓解\n\n论文需要更清晰地回答：**相对于上述已知结果，\"probe reward trap\" 的 delta 在哪里？** 当前论文暗示 delta 是 temporal dissociation（C2），但这一发现的普遍性未经验证（见 N2）。建议在 Introduction 中明确区分：(a) 已知的——representation direction 可能被 Goodhart；(b) 未知的——行为死亡与分布崩溃的时序分离及其对监控实践的具体启示。\n\n**N2 [critical] 核心实验仅在单一模型上进行，泛化性不足**\n\n所有 GRPO 训练实验和 probe reward trap 的观察均仅在 Qwen3-8B 上完成。Llama-3-8B 仅用于 d_syc 判别力的 cross-model 验证（Section 4），并未进行 GRPO 训练。\n\n这是一个显著的泛化性问题：\n- \"1,300-step lag\" 这一具体数字几乎必然依赖于模型架构、LoRA rank（64）、学习率（5e-5）、KL 系数等超参数\n- 不同模型族（如 Llama、Mistral）的 representation geometry 可能不同，d_syc 在 GRPO 中的失败模式也可能不同\n- Limitations section（第 9 页）承认 \"cross-model discriminability is confirmed on Llama-3-8B... but compute constraints prevented training replication on a second architecture\"，但这使得论文标题中的普遍性声明（\"The Probe Reward Trap\"，而非 \"A Probe Reward Trap on Qwen3-8B\"）缺乏支撑\n\n建议至少在一个额外模型上复现核心实验（即使规模较小），或将声明范围显式限定为 Qwen3-8B。\n\n**N3 [critical] C3（supervision granularity 解释）存在严重混淆变量**\n\n论文将 ACT 的成功与 GRPO 的失败归因于 \"supervision granularity\"（per-token vs per-completion），但 ACT 和 GRPO 之间至少存在三个同时变化的因素：\n\n1. **监督粒度**: per-token（ACT）vs per-completion（GRPO）\n2. **学习范式**: supervised L2 consistency loss（ACT）vs RL policy gradient（GRPO）\n3. **作用层**: ACT 在 target layers 施加 L2 约束，GRPO 通过 reward scalar 更新整个策略\n\nSection 7 的结论 \"identifying supervision granularity as one plausible explanation\" 措辞适度，但论文整体叙事（包括 abstract 和 conclusion）将其定位为核心 takeaway 之一，而未充分讨论这些混淆因素。要隔离 supervision granularity 的贡献，至少需要一个 ablation：\n- (a) per-token RL（如 token-level reward shaping with d_syc）来隔离粒度 vs 学习范式\n- 或 (b) per-completion supervised 方法来隔离粒度 vs RL\n\n没有这些 ablation，C3 更接近一个观察而非一个有支撑的因果声明。\n\n**W1 [warning] Abstract/Intro 的 framing 过度泛化**\n\nAbstract 第一句：\"Representation engineering reveals that sycophancy is linearly encoded in LLM residual streams, suggesting that such directions could serve as training signals for alignment. We test this premise systematically and document its failure.\"\n\n这一 framing 暗示论文在测试一个宽泛的前提（representation directions 作为训练信号），但实际实验仅测试了：\n- 一个方向质量水平（AUROC 0.83）\n- 一个 RL 算法（GRPO）\n- 一个模型（Qwen3-8B）\n\n\"systematically\" 和 \"document its failure\" 的措辞暗示该前提已被全面否定，但实际上论文仅否定了 GRPO + d_syc 在 Qwen3-8B 上的特定组合。更准确的 framing 应该是：\"We test one instantiation of this premise—using d_syc as a GRPO reward—and document its failure under four reward formulations.\"\n\n同样，Conclusion（Section 8）：\"Every GRPO reward formulation we tested fails to calibrate sycophancy\" 是准确的，但接着 \"Dense per-token supervision succeeds where per-completion RL does not\" 将范围扩大到了所有 per-completion RL，而实际上只测试了 GRPO。\n\n**W2 [warning] d_syc 编码内容的论证存在循环推理**\n\nSection 7（第 7 页）的核心论断：\"d_syc encodes the direction of belief change but not its evidential warrant\" 是一个关于表征内容的机制性声明。然而，这一声明的主要证据是：GRPO 在 d_syc 上失败 → 因此 d_syc 没有编码正确的信息 → 因此 GRPO 失败。\n\n这是循环推理。要直接支撑这一声明，需要独立证据，例如：\n- d_syc 与 \"是否发生了信念改变\" vs \"改变是否有证据支撑\" 两个标注维度的相关性分析\n- 在已知 valid/invalid belief change 的样本上对比 d_syc 的激活模式\n- 探测 d_syc 方向在 evidential warrant 上的判别力（应该低，以支持声明）\n\n论文在 Section 4 的 evidence-strength ablation 中有部分相关数据（AUROC 从 weak 0.803 到 strong 0.929），但这测量的是 d_syc 在不同 evidence strength 下的判别力，而非 d_syc 是否 *区分* evidence strength。\n\n**W3 [warning] 1,300-step lag 的超参数依赖性未讨论**\n\nTable 3 的 1,300-step lag（ToF 在 step 500 降为 0，entropy 在 step ≈1800 才崩溃）是论文最核心的定量发现，但这一数字的稳定性完全没有讨论：\n- 学习率（5e-5）的变化会如何影响这个 gap？\n- KL 系数（由 KL-clamp 控制）的变化呢？\n- Group size（2）的变化呢？\n- LoRA rank（64）的变化呢？\n\n如果这个 gap 在超参数变化下可以从几百步到几千步不等，那么 \"1,300-step monitoring blind spot\" 就不是一个可靠的定量结论，而只是一个定性观察（行为死亡先于熵崩溃）。建议报告至少一组超参数敏感性分析，或将声明限定为定性层面。\n\n**W4 [warning] d_syc AUROC 0.83 的质量问题未充分讨论**\n\nd_syc 在 Qwen3-8B 上的 AUROC 仅 0.83。这意味着约 17% 的样本被错误分类。论文没有讨论：\n- 如果使用更高质量的方向（如 AUROC > 0.95），reward 是否仍会失败？\n- 0.83 的判别力是否足以区分 \"d_syc 编码的信息不对\" 和 \"d_syc 编码了正确信息但不够精确\"？\n\n这一讨论很重要，因为如果更高质量的方向能成功作为 reward，那么论文的结论就不是 \"representation-based rewards fundamentally fail\"，而是 \"低质量方向作为 reward 会失败\"——这是一个显著不同且不那么有趣的结论。\n\n**W5 [warning] C1/C2/C3 之间缺乏独立性，不应定位为三个独立贡献**\n\nC1（observability gap）、C2（probe reward trap）、C3（supervision granularity explanation）本质上是同一现象的三个方面：\n- C1 是 observation：GRPO 失败，ACT 成功\n- C2 是 C1 中 GRPO 失败的一个具体时序特征\n- C3 是对 C1 的一个（未经充分验证的）解释\n\n将其定位为三个 \"principal claims\"（Section 1，第 2 页）给人以贡献量大于实际的印象。更诚实的定位是：一个核心发现（probe-based GRPO rewards fail）+ 一个有价值的附带观察（temporal dissociation）+ 一个待验证的假说（supervision granularity matters）。\n\n**M1 [minor] 个别术语一致性问题**\n\n- Section 3.2 引入三个公式时用 \"F1 Cosine projection\"/\"F2 Binary probe reward\"/\"F3 Continuous probe\"，但 Section 5 标题用 \"Cosine R₁\"，Section 6 标题用 \"The Probe Reward Trap\"。Reader 需要在 F1/F2/F3 和 R₁/R_t 之间反复对照。\n- \"behavioral death\" 在首次使用时（abstract）未给出正式定义（ToF=0），直到 Section 3.5 才定义 ToF。建议在 abstract 或 introduction 中简要说明。\n\n**M2 [minor] Figure 2 信息密度过高**\n\nFigure 2 在一个图中同时展示了 (a) Direction Extraction, (b) Reward Design Space, (c) Supervision Paradigm，以及底部的关键实验结果摘要（31/31 checkpoints, SYCONSCORE 数字等）。对于首次阅读的 reviewer 来说，这张图承载了过多信息。建议将底部的实验结果摘要移至正文或表格中。\n\n---\n\n### Questions for Authors\n\n**Q1.** 如果 d_syc 的 AUROC 能提高到 0.95+（例如通过更多对比对、更好的方向提取方法、或 non-linear probe），probe reward trap 是否仍然会出现？这对论文核心结论的影响是什么？\n\n**Q2.** Table 3 中 1,300-step lag 在不同随机种子间的方差有多大？三个种子（Appendix A）是否都展示了类似的时序分离？\n\n**Q3.** 论文是否考虑过 token-level reward shaping（将 d_syc 应用于每个 token 而非整个 completion）作为介于 GRPO 和 ACT 之间的 ablation？这将直接测试 supervision granularity 假说。\n\n**Q4.** Section 7 提到 \"Both signals encode whether belief changed, not whether it should have\"——是否有直接的实验来量化 d_syc 在 \"是否应该改变信念\" 这一维度上的判别力？\n\n**Q5.** ACT 的成功是否可能部分归因于它使用了 labeled valid/invalid pairs（监督信号本身包含了 evidential warrant 信息），而非 supervision granularity？\n\n---\n\n### Missing References\n\n1. **Pimentel et al. (2020)** \"Information-Theoretic Probing with Minimum Description Length\" — 与论文使用 linear probe 评估 d_syc 的方法论直接相关。论文引用了 Hewitt & Liang (2019) 的 selectivity 控制，但 Pimentel 等人的 MDL 框架提供了另一种评估 probe 是否真正捕获表征信息的视角。\n\n2. **Rafailov et al. (2024)** \"Direct Preference Optimization\" — 作为 GRPO 的替代 RL 范式，DPO 直接在 preference 对上优化策略而不需要显式 reward model。在讨论 \"per-completion RL fails\" 的泛化性时，提及 DPO 是否也会失败（或至少讨论其与 GRPO 的区别）是有价值的。\n\n3. **Voita & Titov (2020)** \"Information-Theoretic Probing for Linguistic Structure\" — 关于 probe 复杂度与信息内容的关系，与论文关于 \"d_syc 编码了什么\" 的讨论直接相关。\n\n注：上述参考文献的缺失不构成重大问题，但会加强论文在 probing methodology 和 RL alternatives 方面的讨论深度。\n\n---\n\n### Novelty Assessment\n\n**中等偏低（Moderate-Low）**。\n\n核心观察——representation-based proxy reward 在 RL 训练中被 Goodhart——是该领域的已知风险。论文的增量贡献在于：(1) 在 sycophancy 场景下的具体实证文档化，(2) 行为死亡与熵崩溃的时序分离发现。其中 (2) 是最有价值的贡献，但仅在单一模型上验证，且时序数字的超参数依赖性未知。\n\n论文自己承认是 Goodhart regressional variant 的实例化（Section 2），但未能充分论证为什么这一实例化值得一篇独立论文。最佳论证路径是强化 temporal dissociation 的普遍性和实践意义（需要更多模型和超参数的实验支持）。\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**Soundness: 3/5** — 主要实验设计合理，四种 reward 公式的穷举测试和诊断链有说服力，但核心声明受限于单一模型、C3 的混淆变量问题、以及 d_syc 编码内容论证的循环性。\n\n**Excitement: 2.5/5** — 负面结果对 representation engineering 方向的实践者有参考价值，temporal dissociation 发现有一定新意，但核心贡献是已知原理（Goodhart）的实例化，且单模型实验限制了泛化性和影响力。\n\n**一句话总结**: 论文提供了一个有条理的负面结果案例研究，但核心发现（probe reward 被 Goodhart）缺乏超越已知风险的根本新意，单模型实验和未隔离的混淆变量使得三个 claims 的说服力不足以支撑 main conference 接收。在 Findings 级别，作为 representation-based reward 的 cautionary tale 有其价值。\n\n**置信度: 4/5** — 我熟悉 representation engineering、reward overoptimization 和 probing methodology 的相关文献。对 GRPO 的具体实现细节了解中等。\n\n---\n\n### 格式合规检查\n- ✅ 正文 8 页（Sections 1-8），符合 EMNLP 2026 long paper 限制\n- ✅ Limitations section 存在（第 9 页），不计入页数限制\n- ✅ Abstract 约 160 words，符合 200 words 限制\n- ✅ 双盲格式（\"Anonymous ACL submission\"）\n- ✅ 使用 ACL style template\n- ⚠️ 未见 Ethics Statement（可选，不影响接收）",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n**审查侧重**: 新颖性 + framing 一致性 + 相关工作 + 写作质量 + 贡献定位\n\n---\n\n### Summary\n\n本文从 LLM 残差流中提取对比性 sycophancy 方向 d_syc（AUROC 0.83），然后将其转化为 GRPO 奖励信号，系统测试了四种公式化方案（cosine projection、binary probe、continuous probe、stopped-gradient variants），均导致训练失败。核心发现\"probe reward trap\"指出：binary probe 奖励下，行为死亡（ToF→0）在第 500 步出现，而生成熵直到第 1800 步才崩溃，产生 1,300 步的监控盲区。对比实验中，per-token 监督方法 ACT 在所有检查点均成功。\n\n---\n\n### Strengths\n\n**S1. 系统性的负面结果文档化**。论文测试了四种将 d_syc 转化为 GRPO 奖励的方案（F1 cosine projection、F2 binary probe、F3 continuous probe，以及 stopped-gradient 变体），而非仅测一种后就下结论。Table 2 的诊断链清晰展示了每种配置的失败模式，这种穷举式排除为\"不是实现细节问题\"提供了说服力。\n\n**S2. 行为死亡-熵崩溃时序分离的实证发现（C2）是最有价值的贡献**。Table 3 和 Figure 4a 清楚展示 ToF 在 step 500 降为 0，而 entropy 直到 step 1800 才崩溃。这一发现对实践者有直接价值——说明仅依赖 entropy monitoring 做 early stopping 是不够的。这种 *temporal dissociation* 比简单说\"reward hacking 发生了\"更有信息量。\n\n**S3. 跨模型 d_syc 判别力验证**。Section 4 不仅在 Qwen3-8B 上验证了 d_syc 的判别力（AUROC 0.83），还在 Llama-3-8B 上做了 cross-model 验证（AUROC 0.779，Table 1 / Figure 3）。Per-layer AUROC 分析（Figure 3）显示判别力在上层 1/3 逐渐涌现，与 sycophancy 作为高层语义现象的直觉一致。Stability ablation（cross-validation、model transfer、evidence-strength gradient）增强了 d_syc 本身作为诊断工具的可信度。\n\n**S4. Stubbornness 分类法（Appendix B）提供了定性补充**。对 181 条 valid-correction 响应的五类失败模式分析（deliberation traps 28.7%、sycophantic stubbornness 24.3%、acknowledge-but-maintain 23.8% 等）为定量指标提供了直观解释，揭示模型学会了调节 *refusal style* 而非 *acceptance rate*。\n\n**S5. 实验设计的关键控制**。Online recalibration（Section 3.3，每 500 步重新提取 d_syc）排除了\"方向漂移导致失败\"的假说。Section 5 对 cosine R₁ 的 dot-product/scale/stopped-gradient 变体（F1a-F1d）逐步排除了优化路径问题。这些控制实验展示了严谨的实验方法论。\n\n---\n\n### Weaknesses\n\n**N1 [critical] 新颖性定位不充分：核心发现是 Goodhart regressional variant 的已知实例化，增量贡献未被清晰论证**\n\n论文在 Section 2（Related Work，第 3 页）自己承认 \"our probe reward trap instantiates the regressional variant, where the proxy-target correlation breaks under optimization shift\"。然而论文随后赋予这一现象一个专有名称（\"probe reward trap\"）并将其定位为核心贡献，却未充分论证为什么这一特定实例化值得单独命名和研究。\n\n具体而言：\n- Manheim & Garrabrant (2019) 已系统分类了 Goodhart 的四种变体，regressional variant 明确预测代理指标在优化压力下会失效\n- Gao et al. (2023) 已在标准 reward model 上量化了 reward overoptimization 的 scaling law\n- Wu & Tang (2026, arXiv:2604.01476, 已被本文引用) 已用 representation engineering 研究 reward hacking 的检测与缓解\n\n论文需要更清晰地回答：**相对于上述已知结果，\"probe reward trap\" 的 delta 在哪里？** 当前论文暗示 delta 是 temporal dissociation（C2），但这一发现的普遍性未经验证（见 N2）。建议在 Introduction 中明确区分：(a) 已知的——representation direction 可能被 Goodhart；(b) 未知的——行为死亡与分布崩溃的时序分离及其对监控实践的具体启示。\n\n**N2 [critical] 核心实验仅在单一模型上进行，泛化性不足**\n\n所有 GRPO 训练实验和 probe reward trap 的观察均仅在 Qwen3-8B 上完成。Llama-3-8B 仅用于 d_syc 判别力的 cross-model 验证（Section 4），并未进行 GRPO 训练。\n\n这是一个显著的泛化性问题：\n- \"1,300-step lag\" 这一具体数字几乎必然依赖于模型架构、LoRA rank（64）、学习率（5e-5）、KL 系数等超参数\n- 不同模型族（如 Llama、Mistral）的 representation geometry 可能不同，d_syc 在 GRPO 中的失败模式也可能不同\n- Limitations section（第 9 页）承认 \"cross-model discriminability is confirmed on Llama-3-8B... but compute constraints prevented training replication on a second architecture\"，但这使得论文标题中的普遍性声明（\"The Probe Reward Trap\"，而非 \"A Probe Reward Trap on Qwen3-8B\"）缺乏支撑\n\n建议至少在一个额外模型上复现核心实验（即使规模较小），或将声明范围显式限定为 Qwen3-8B。\n\n**N3 [critical] C3（supervision granularity 解释）存在严重混淆变量**\n\n论文将 ACT 的成功与 GRPO 的失败归因于 \"supervision granularity\"（per-token vs per-completion），但 ACT 和 GRPO 之间至少存在三个同时变化的因素：\n\n1. **监督粒度**: per-token（ACT）vs per-completion（GRPO）\n2. **学习范式**: supervised L2 consistency loss（ACT）vs RL policy gradient（GRPO）\n3. **作用层**: ACT 在 target layers 施加 L2 约束，GRPO 通过 reward scalar 更新整个策略\n\nSection 7 的结论 \"identifying supervision granularity as one plausible explanation\" 措辞适度，但论文整体叙事（包括 abstract 和 conclusion）将其定位为核心 takeaway 之一，而未充分讨论这些混淆因素。要隔离 supervision granularity 的贡献，至少需要一个 ablation：\n- (a) per-token RL（如 token-level reward shaping with d_syc）来隔离粒度 vs 学习范式\n- 或 (b) per-completion supervised 方法来隔离粒度 vs RL\n\n没有这些 ablation，C3 更接近一个观察而非一个有支撑的因果声明。\n\n**W1 [warning] Abstract/Intro 的 framing 过度泛化**\n\nAbstract 第一句：\"Representation engineering reveals that sycophancy is linearly encoded in LLM residual streams, suggesting that such directions could serve as training signals for alignment. We test this premise systematically and document its failure.\"\n\n这一 framing 暗示论文在测试一个宽泛的前提（representation directions 作为训练信号），但实际实验仅测试了：\n- 一个方向质量水平（AUROC 0.83）\n- 一个 RL 算法（GRPO）\n- 一个模型（Qwen3-8B）\n\n\"systematically\" 和 \"document its failure\" 的措辞暗示该前提已被全面否定，但实际上论文仅否定了 GRPO + d_syc 在 Qwen3-8B 上的特定组合。更准确的 framing 应该是：\"We test one instantiation of this premise—using d_syc as a GRPO reward—and document its failure under four reward formulations.\"\n\n同样，Conclusion（Section 8）：\"Every GRPO reward formulation we tested fails to calibrate sycophancy\" 是准确的，但接着 \"Dense per-token supervision succeeds where per-completion RL does not\" 将范围扩大到了所有 per-completion RL，而实际上只测试了 GRPO。\n\n**W2 [warning] d_syc 编码内容的论证存在循环推理**\n\nSection 7（第 7 页）的核心论断：\"d_syc encodes the direction of belief change but not its evidential warrant\" 是一个关于表征内容的机制性声明。然而，这一声明的主要证据是：GRPO 在 d_syc 上失败 → 因此 d_syc 没有编码正确的信息 → 因此 GRPO 失败。\n\n这是循环推理。要直接支撑这一声明，需要独立证据，例如：\n- d_syc 与 \"是否发生了信念改变\" vs \"改变是否有证据支撑\" 两个标注维度的相关性分析\n- 在已知 valid/invalid belief change 的样本上对比 d_syc 的激活模式\n- 探测 d_syc 方向在 evidential warrant 上的判别力（应该低，以支持声明）\n\n论文在 Section 4 的 evidence-strength ablation 中有部分相关数据（AUROC 从 weak 0.803 到 strong 0.929），但这测量的是 d_syc 在不同 evidence strength 下的判别力，而非 d_syc 是否 *区分* evidence strength。\n\n**W3 [warning] 1,300-step lag 的超参数依赖性未讨论**\n\nTable 3 的 1,300-step lag（ToF 在 step 500 降为 0，entropy 在 step ≈1800 才崩溃）是论文最核心的定量发现，但这一数字的稳定性完全没有讨论：\n- 学习率（5e-5）的变化会如何影响这个 gap？\n- KL 系数（由 KL-clamp 控制）的变化呢？\n- Group size（2）的变化呢？\n- LoRA rank（64）的变化呢？\n\n如果这个 gap 在超参数变化下可以从几百步到几千步不等，那么 \"1,300-step monitoring blind spot\" 就不是一个可靠的定量结论，而只是一个定性观察（行为死亡先于熵崩溃）。建议报告至少一组超参数敏感性分析，或将声明限定为定性层面。\n\n**W4 [warning] d_syc AUROC 0.83 的质量问题未充分讨论**\n\nd_syc 在 Qwen3-8B 上的 AUROC 仅 0.83。这意味着约 17% 的样本被错误分类。论文没有讨论：\n- 如果使用更高质量的方向（如 AUROC > 0.95），reward 是否仍会失败？\n- 0.83 的判别力是否足以区分 \"d_syc 编码的信息不对\" 和 \"d_syc 编码了正确信息但不够精确\"？\n\n这一讨论很重要，因为如果更高质量的方向能成功作为 reward，那么论文的结论就不是 \"representation-based rewards fundamentally fail\"，而是 \"低质量方向作为 reward 会失败\"——这是一个显著不同且不那么有趣的结论。\n\n**W5 [warning] C1/C2/C3 之间缺乏独立性，不应定位为三个独立贡献**\n\nC1（observability gap）、C2（probe reward trap）、C3（supervision granularity explanation）本质上是同一现象的三个方面：\n- C1 是 observation：GRPO 失败，ACT 成功\n- C2 是 C1 中 GRPO 失败的一个具体时序特征\n- C3 是对 C1 的一个（未经充分验证的）解释\n\n将其定位为三个 \"principal claims\"（Section 1，第 2 页）给人以贡献量大于实际的印象。更诚实的定位是：一个核心发现（probe-based GRPO rewards fail）+ 一个有价值的附带观察（temporal dissociation）+ 一个待验证的假说（supervision granularity matters）。\n\n**M1 [minor] 个别术语一致性问题**\n\n- Section 3.2 引入三个公式时用 \"F1 Cosine projection\"/\"F2 Binary probe reward\"/\"F3 Continuous probe\"，但 Section 5 标题用 \"Cosine R₁\"，Section 6 标题用 \"The Probe Reward Trap\"。Reader 需要在 F1/F2/F3 和 R₁/R_t 之间反复对照。\n- \"behavioral death\" 在首次使用时（abstract）未给出正式定义（ToF=0），直到 Section 3.5 才定义 ToF。建议在 abstract 或 introduction 中简要说明。\n\n**M2 [minor] Figure 2 信息密度过高**\n\nFigure 2 在一个图中同时展示了 (a) Direction Extraction, (b) Reward Design Space, (c) Supervision Paradigm，以及底部的关键实验结果摘要（31/31 checkpoints, SYCONSCORE 数字等）。对于首次阅读的 reviewer 来说，这张图承载了过多信息。建议将底部的实验结果摘要移至正文或表格中。\n\n---\n\n### Questions for Authors\n\n**Q1.** 如果 d_syc 的 AUROC 能提高到 0.95+（例如通过更多对比对、更好的方向提取方法、或 non-linear probe），probe reward trap 是否仍然会出现？这对论文核心结论的影响是什么？\n\n**Q2.** Table 3 中 1,300-step lag 在不同随机种子间的方差有多大？三个种子（Appendix A）是否都展示了类似的时序分离？\n\n**Q3.** 论文是否考虑过 token-level reward shaping（将 d_syc 应用于每个 token 而非整个 completion）作为介于 GRPO 和 ACT 之间的 ablation？这将直接测试 supervision granularity 假说。\n\n**Q4.** Section 7 提到 \"Both signals encode whether belief changed, not whether it should have\"——是否有直接的实验来量化 d_syc 在 \"是否应该改变信念\" 这一维度上的判别力？\n\n**Q5.** ACT 的成功是否可能部分归因于它使用了 labeled valid/invalid pairs（监督信号本身包含了 evidential warrant 信息），而非 supervision granularity？\n\n---\n\n### Missing References\n\n1. **Pimentel et al. (2020)** \"Information-Theoretic Probing with Minimum Description Length\" — 与论文使用 linear probe 评估 d_syc 的方法论直接相关。论文引用了 Hewitt & Liang (2019) 的 selectivity 控制，但 Pimentel 等人的 MDL 框架提供了另一种评估 probe 是否真正捕获表征信息的视角。\n\n2. **Rafailov et al. (2024)** \"Direct Preference Optimization\" — 作为 GRPO 的替代 RL 范式，DPO 直接在 preference 对上优化策略而不需要显式 reward model。在讨论 \"per-completion RL fails\" 的泛化性时，提及 DPO 是否也会失败（或至少讨论其与 GRPO 的区别）是有价值的。\n\n3. **Voita & Titov (2020)** \"Information-Theoretic Probing for Linguistic Structure\" — 关于 probe 复杂度与信息内容的关系，与论文关于 \"d_syc 编码了什么\" 的讨论直接相关。\n\n注：上述参考文献的缺失不构成重大问题，但会加强论文在 probing methodology 和 RL alternatives 方面的讨论深度。\n\n---\n\n### Novelty Assessment\n\n**中等偏低（Moderate-Low）**。\n\n核心观察——representation-based proxy reward 在 RL 训练中被 Goodhart——是该领域的已知风险。论文的增量贡献在于：(1) 在 sycophancy 场景下的具体实证文档化，(2) 行为死亡与熵崩溃的时序分离发现。其中 (2) 是最有价值的贡献，但仅在单一模型上验证，且时序数字的超参数依赖性未知。\n\n论文自己承认是 Goodhart regressional variant 的实例化（Section 2），但未能充分论证为什么这一实例化值得一篇独立论文。最佳论证路径是强化 temporal dissociation 的普遍性和实践意义（需要更多模型和超参数的实验支持）。\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**Soundness: 3/5** — 主要实验设计合理，四种 reward 公式的穷举测试和诊断链有说服力，但核心声明受限于单一模型、C3 的混淆变量问题、以及 d_syc 编码内容论证的循环性。\n\n**Excitement: 2.5/5** — 负面结果对 representation engineering 方向的实践者有参考价值，temporal dissociation 发现有一定新意，但核心贡献是已知原理（Goodhart）的实例化，且单模型实验限制了泛化性和影响力。\n\n**一句话总结**: 论文提供了一个有条理的负面结果案例研究，但核心发现（probe reward 被 Goodhart）缺乏超越已知风险的根本新意，单模型实验和未隔离的混淆变量使得三个 claims 的说服力不足以支撑 main conference 接收。在 Findings 级别，作为 representation-based reward 的 cautionary tale 有其价值。\n\n**置信度: 4/5** — 我熟悉 representation engineering、reward overoptimization 和 probing methodology 的相关文献。对 GRPO 的具体实现细节了解中等。\n\n---\n\n### 格式合规检查\n- ✅ 正文 8 页（Sections 1-8），符合 EMNLP 2026 long paper 限制\n- ✅ Limitations section 存在（第 9 页），不计入页数限制\n- ✅ Abstract 约 160 words，符合 200 words 限制\n- ✅ 双盲格式（\"Anonymous ACL submission\"）\n- ✅ 使用 ACL style template\n- ⚠️ 未见 Ethics Statement（可选，不影响接收）",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-25T23:43:33.551411+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-25T23:43:38.631300+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-25T23:43:38.681967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-25T23:43:43.700266+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-25T23:43:43.750825+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 772 · 2026-05-25T23:43:54.685183+00:00_

审稿完成。已向 Review Director 提交完整意见，核心判断：

- **Overall: 3.0 (Findings)**
- **3 个 critical 问题**：(1) 新颖性不足——核心发现是 Goodhart regressional variant 的已知实例化，增量贡献未清晰论证；(2) 所有 GRPO 训练仅在 Qwen3-8B 单模型上进行，泛化性不足；(3) C3（supervision granularity）存在至少三个混淆变量未隔离
- **5 个 warning 问题**：framing 过度泛化、d_syc 编码论证循环推理、1300-step lag 超参数依赖性未讨论、d_syc AUROC 0.83 质量问题、C1/C2/C3 缺乏独立性
- **最有价值的贡献**是 behavioral death 与 entropy collapse 的时序分离（C2），但需要更多模型和超参数敏感性分析来建立普遍性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

4 recorded events


### User

_source line 773 · 2026-05-25T23:44:50.925261+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条阅读 Reviewer 1 的审稿意见，对每个 critical/warning 问题给出 `[AGREE]` 或 `[REBUT]`（附理由）。重点关注你们之间的分歧点。

---

以下是 Reviewer 1 的完整审稿：

**Overall: 3.0 (Findings)**，Soundness 2.5，Excitement 3，Confidence 4/5

### 3 个 Critical 问题

**C1 [critical] group_size=2 构成致命替代解释且消融不足**：GRPO 使用 group_size=2 意味着每次只采样 2 个 completion 来估计 advantage。这使得 reward signal 极度噪声化，可能是训练失败的根本原因而非 d_syc 本身的问题。论文需要 group_size≥8 的消融来排除这一替代解释。

**C2 [critical] 256-token truncation 使 reward AUROC 降至 0.60，接近随机**：在 256 token 截断下，d_syc 的 reward 判别力（AUROC）从完整长度的 0.83 降至 0.60。这意味着 GRPO 实际收到的 reward signal 接近随机，训练失败可能仅是因为 reward 质量太低，而非 probe reward 的根本性问题。

**C3 [critical] "d_syc encodes whether belief changed, not whether it should have" 的因果声明缺乏直接验证**：这一核心机制性声明没有独立的因果验证实验，主要靠训练失败来反推。

### 5 个 Warning 问题

**W1 [warning] seed 数不足**：仅 3 个种子，统计显著性不足。

**W2 [warning] ACT vs GRPO 比较不公平**：两者之间混合了多个维度差异（监督粒度、学习范式、作用层），无法隔离归因。

**W3 [warning] 单模型验证**：所有训练实验仅在 Qwen3-8B 上进行。

**W4 [warning] stopped gradient 论证力度被高估**：stopped gradient 变体（F1c/F1d）仅排除了梯度回传路径问题，但论文将其论证力度描述得过高。

**W5 [warning] contrastive pair 的 GPT-4.1 分布偏差**：GPT-4.1 生成的对比对可能引入系统性偏差。

### 主要优势
- 选题重要（representation-based reward 的可行性是 alignment 领域关键问题）
- 多 reward formulation 覆盖（四种公式 + 变体的穷举测试）
- probe reward trap 概念有实践价值
- 写作清晰

### 总结
如果补充 group_size≥8 和更长 completion length 的消融实验并弱化因果声明，有潜力提升至 Conference 水平。

---

请对以上每个 weakness（C1-C3, W1-W5）逐条回应 `[AGREE]` 或 `[REBUT]`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-25T23:47:37.337182+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 意见\n\n---\n\n### Critical 问题\n\n**[AGREE] R1-C1: group_size=2 构成致命替代解释**\n\n这是 R1 最有力的发现，也是我在初审中遗漏的重要问题。论文在 Section 3.4（第 4 页）承认 \"GRPO uses a group size of 2 due to memory constraints with 8B-parameter models, below the typical range of 8–64\"。group_size=2 意味着 advantage estimation 本质上是二元比较（两个 completion 中一好一差），noise 极大。\n\n关键推理链：Table 4 中 R_t-only GRPO（不使用 d_syc，仅用行为正确性作 reward）在 group_size=2 下同样 barely exceeds vanilla（SYCONSCORE 0.131）。这打开了一个论文未排除的替代解释：**group_size=2 下任何 GRPO reward 都会失败，失败原因是 advantage estimation noise 而非 d_syc 本身的局限性。** 论文没有展示任何 reward signal 在 group_size=2 下成功的 positive control，因此无法区分 \"d_syc 有问题\" 和 \"GRPO 在 group_size=2 下对任何 reward 都不可靠\"。\n\n这一发现与我的 N3（ACT vs GRPO 混淆变量）形成互补：如果 GRPO 在 group_size=2 下本身就不可靠，那么 ACT 的成功可能完全与 d_syc 的质量无关，而只是因为 ACT 不依赖 group-based advantage estimation。\n\n**补充建议**：除 R1 建议的 group_size≥8 消融外，还应在 group_size=2 下测试一个 \"gold standard\" reward（如 GPT-4 judge score）作为 positive control。如果 gold reward 在 group_size=2 下也失败，则论文的核心结论需要根本性重写。\n\n---\n\n**[AGREE] R1-C2: 256-token 截断使 reward 质量严重退化**\n\n这与我的 W4（d_syc AUROC 0.83 的质量问题）互补且比我的分析更具体。R1 准确定位了问题：GRPO 实际收到的 reward signal 的判别力远低于 Section 4 报告的 headline AUROC 0.83。\n\n论文在 Section 5（第 6 页）确认了截断带来的 AUROC 降级路径：offline 0.827 → distribution shift → 256-token truncation 后进一步下降。无论最终数字是 0.60 还是 0.69，这意味着 GRPO 看到的 reward signal 已接近弱分类器水平。\n\n这构成了与 C1 类似的替代解释：**训练失败可能仅因为 reward quality 太低（AUROC ≈ 0.60-0.69 在 256 token 截断下），而非 probe reward 存在根本性缺陷。** 论文需要回答的关键问题是：如果在更长 completion 上训练（d_syc AUROC 更高），probe reward trap 是否仍然出现？\n\n不过我要补充一点：即使截断是核心原因，\"probe direction 的判别力在截断下显著退化\"这一事实本身也有实践价值——它说明 representation-based reward 对 sequence length 敏感，这是部署时需要考虑的。论文如果将此作为一个独立 finding 来呈现（而非忽略它直接跳到 \"probe reward 有根本性问题\"），叙事会更诚实。\n\n---\n\n**[AGREE] R1-C3: d_syc 编码内容的因果声明缺乏直接验证**\n\n完全同意。这与我的 W2 是同一问题——我将其定为 warning，R1 定为 critical。反思后我认为 R1 的 critical 定级更准确，理由如下：\n\n\"d_syc encodes whether belief changed, not whether it should have\" 不是论文的一个附带观察，而是 Section 7 的核心解释框架，贯穿 abstract、introduction 和 conclusion。它是论文将失败从 \"implementation issue\" 提升到 \"fundamental limitation\" 的关键论证环节。如果这一声明的证据是循环的（从失败反推编码内容），那么论文的 \"fundamental limitation\" 叙事就缺乏根基，整个贡献退化为 \"我们试了几种 GRPO 配置，都没成功\"——这是一个更弱的贡献。\n\n**与 C1/C2 的交互**：如果 group_size=2 noise（C1）或 truncation quality（C2）才是失败的根本原因，那么 \"d_syc 编码错了东西\" 这一解释就完全是对 confound 的误归因。三个 critical 问题形成了一个互相强化的质疑链。\n\n---\n\n### Warning 问题\n\n**[AGREE] R1-W1: seed 数不足**\n\n3 seeds 是可接受的最低限度，但对于 SYCONSCORE 这样的复合指标（ToF 和 NoF 的调和均值），方差可能较大。论文 Appendix A 报告了 \"three seeds (s∈{1})\"——实际上我不确定这里是否是 3 个不同的种子还是其他设置。Table 2 的结果似乎也没有报告 confidence intervals 或 standard deviations。\n\n不过我认为这是 warning 而非 critical：论文的核心定性发现（所有 GRPO 配置 SYCONSCORE < vanilla）如果在 3 seeds 上一致出现，定性结论仍然成立。问题在于定量数字（如 SYCONSCORE 0.131 vs 0.267）的精度不足。\n\n---\n\n**[AGREE] R1-W2: ACT vs GRPO 比较不公平**\n\n完全同意，与我的 N3 完全一致。ACT 和 GRPO 之间的差异不仅是 supervision granularity（论文的解释），还包括学习范式（supervised vs RL）、作用层（target layers vs whole policy）、以及数据使用方式（labeled pairs vs rollouts）。没有控制实验来隔离这些因素，C3（supervision granularity 解释）是不可靠的。\n\n---\n\n**[AGREE] R1-W3: 单模型验证**\n\n与我的 N2 完全一致。不再赘述。\n\n---\n\n**[REBUT] R1-W4: stopped gradient 论证力度被高估**\n\nR1 认为 \"论文将 stopped gradient 的论证力度描述得过高\"。我部分不同意。\n\n回到原文 Section 5（第 6 页），stopped gradient 变体（F1c: stopped dot product, F1d: mode collapse）被明确定位为诊断链中的一步——排除 \"梯度通过 d_syc 回传导致方向被 corrupt\" 这一特定假说。论文的表述是（paraphrasing）：\"F1c/F1d 的失败排除了梯度操纵假说，将问题指向 d_syc 的语义局限性。\" 这是一个合理的消去推理步骤。\n\n论文没有声称 stopped gradient 证明了 \"d_syc 编码错了东西\"——它只是排除了一个特定的 alternative（gradient-based manipulation）。在诊断链中，每一步排除一个假说是标准方法论。\n\n**但 R1 有一个隐含的有效批评**：如果 C1（group_size noise）和 C2（truncation quality）才是真正的失败原因，那么 stopped gradient 排除的假说虽然被正确排除，但排除它也不能指向 \"语义局限性\"——因为还有其他未排除的 confound。所以 stopped gradient 的论证力在逻辑上是正确的，但在 R1 指出的更大 confound 背景下，其指向性被削弱了。\n\n总结：论证逻辑本身不过度，但在 C1/C2 未排除的背景下，其推论的终点（语义局限性）确实过早。\n\n---\n\n**[AGREE] R1-W5: GPT-4.1 对比对的分布偏差**\n\n同意这是一个有效关切。论文 Section 3.1（第 4 页）提到使用 GPT-4.1 (OpenAI, 2025) 以两阶段 pipeline 生成对比对：skeleton generation + dialogue completion。虽然论文有一些质量控制措施（style matching: response-length difference <10%，evidence strength 三档标注，automated validation 丢弃了 19/200 对），但 GPT-4.1 生成的 sycophantic 响应可能与真实 LLM sycophancy 存在系统性差异。\n\n具体风险：\n- GPT-4.1 的 sycophancy 风格可能过于明显/模式化，使得 d_syc 学到了 GPT-4.1 的写作风格特征而非通用的 sycophancy 信号\n- 论文用这些对比对在 Qwen3-8B 上提取方向，但 Qwen3-8B 自己产生的 sycophancy 可能有不同的 surface patterns\n\n不过这一问题的严重性有限：Section 4 的 cross-model validation（Llama-3-8B 上 AUROC 0.779）和 evidence-strength gradient 分析提供了一些间接证据说明 d_syc 捕获的是语义信号而非 style artifacts。\n\n---\n\n### 总结性评估\n\nR1 的审稿揭示了两个我初审未充分关注的重要问题：**group_size=2 的 confound（C1）和 256-token truncation 对 reward quality 的实际影响（C2）**。这两个问题与我自己的 N3（ACT/GRPO 混淆变量）和 W4（d_syc 质量问题）形成互补，共同构成一个强有力的替代解释：\n\n> 论文观察到的所有 \"probe reward trap\" 现象，可能完全由 (a) group_size=2 的 noisy advantage estimation + (b) 256-token truncation 导致的 reward quality 退化所解释，无需诉诸 \"d_syc 有根本性语义局限\" 这一更强的结论。\n\n如果作者能提供 group_size≥8 + 更长 completion length 的消融实验，且 probe reward trap 仍然出现，这将显著增强论文的核心论证。在当前证据下，**我维持 Overall 3.0 (Findings) 的评分**，但 soundness 评分下调至 **2.5/5**（受 C1/C2 confound 影响）。\n\nR1 和我在整体判断上一致：这是一篇方法论上有缺陷但选题有价值的工作，目前证据支持 Findings 接收，但不足以支持 main conference。",
  "reviewer_id": "2",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 意见\n\n---\n\n### Critical 问题\n\n**[AGREE] R1-C1: group_size=2 构成致命替代解释**\n\n这是 R1 最有力的发现，也是我在初审中遗漏的重要问题。论文在 Section 3.4（第 4 页）承认 \"GRPO uses a group size of 2 due to memory constraints with 8B-parameter models, below the typical range of 8–64\"。group_size=2 意味着 advantage estimation 本质上是二元比较（两个 completion 中一好一差），noise 极大。\n\n关键推理链：Table 4 中 R_t-only GRPO（不使用 d_syc，仅用行为正确性作 reward）在 group_size=2 下同样 barely exceeds vanilla（SYCONSCORE 0.131）。这打开了一个论文未排除的替代解释：**group_size=2 下任何 GRPO reward 都会失败，失败原因是 advantage estimation noise 而非 d_syc 本身的局限性。** 论文没有展示任何 reward signal 在 group_size=2 下成功的 positive control，因此无法区分 \"d_syc 有问题\" 和 \"GRPO 在 group_size=2 下对任何 reward 都不可靠\"。\n\n这一发现与我的 N3（ACT vs GRPO 混淆变量）形成互补：如果 GRPO 在 group_size=2 下本身就不可靠，那么 ACT 的成功可能完全与 d_syc 的质量无关，而只是因为 ACT 不依赖 group-based advantage estimation。\n\n**补充建议**：除 R1 建议的 group_size≥8 消融外，还应在 group_size=2 下测试一个 \"gold standard\" reward（如 GPT-4 judge score）作为 positive control。如果 gold reward 在 group_size=2 下也失败，则论文的核心结论需要根本性重写。\n\n---\n\n**[AGREE] R1-C2: 256-token 截断使 reward 质量严重退化**\n\n这与我的 W4（d_syc AUROC 0.83 的质量问题）互补且比我的分析更具体。R1 准确定位了问题：GRPO 实际收到的 reward signal 的判别力远低于 Section 4 报告的 headline AUROC 0.83。\n\n论文在 Section 5（第 6 页）确认了截断带来的 AUROC 降级路径：offline 0.827 → distribution shift → 256-token truncation 后进一步下降。无论最终数字是 0.60 还是 0.69，这意味着 GRPO 看到的 reward signal 已接近弱分类器水平。\n\n这构成了与 C1 类似的替代解释：**训练失败可能仅因为 reward quality 太低（AUROC ≈ 0.60-0.69 在 256 token 截断下），而非 probe reward 存在根本性缺陷。** 论文需要回答的关键问题是：如果在更长 completion 上训练（d_syc AUROC 更高），probe reward trap 是否仍然出现？\n\n不过我要补充一点：即使截断是核心原因，\"probe direction 的判别力在截断下显著退化\"这一事实本身也有实践价值——它说明 representation-based reward 对 sequence length 敏感，这是部署时需要考虑的。论文如果将此作为一个独立 finding 来呈现（而非忽略它直接跳到 \"probe reward 有根本性问题\"），叙事会更诚实。\n\n---\n\n**[AGREE] R1-C3: d_syc 编码内容的因果声明缺乏直接验证**\n\n完全同意。这与我的 W2 是同一问题——我将其定为 warning，R1 定为 critical。反思后我认为 R1 的 critical 定级更准确，理由如下：\n\n\"d_syc encodes whether belief changed, not whether it should have\" 不是论文的一个附带观察，而是 Section 7 的核心解释框架，贯穿 abstract、introduction 和 conclusion。它是论文将失败从 \"implementation issue\" 提升到 \"fundamental limitation\" 的关键论证环节。如果这一声明的证据是循环的（从失败反推编码内容），那么论文的 \"fundamental limitation\" 叙事就缺乏根基，整个贡献退化为 \"我们试了几种 GRPO 配置，都没成功\"——这是一个更弱的贡献。\n\n**与 C1/C2 的交互**：如果 group_size=2 noise（C1）或 truncation quality（C2）才是失败的根本原因，那么 \"d_syc 编码错了东西\" 这一解释就完全是对 confound 的误归因。三个 critical 问题形成了一个互相强化的质疑链。\n\n---\n\n### Warning 问题\n\n**[AGREE] R1-W1: seed 数不足**\n\n3 seeds 是可接受的最低限度，但对于 SYCONSCORE 这样的复合指标（ToF 和 NoF 的调和均值），方差可能较大。论文 Appendix A 报告了 \"three seeds (s∈{1})\"——实际上我不确定这里是否是 3 个不同的种子还是其他设置。Table 2 的结果似乎也没有报告 confidence intervals 或 standard deviations。\n\n不过我认为这是 warning 而非 critical：论文的核心定性发现（所有 GRPO 配置 SYCONSCORE < vanilla）如果在 3 seeds 上一致出现，定性结论仍然成立。问题在于定量数字（如 SYCONSCORE 0.131 vs 0.267）的精度不足。\n\n---\n\n**[AGREE] R1-W2: ACT vs GRPO 比较不公平**\n\n完全同意，与我的 N3 完全一致。ACT 和 GRPO 之间的差异不仅是 supervision granularity（论文的解释），还包括学习范式（supervised vs RL）、作用层（target layers vs whole policy）、以及数据使用方式（labeled pairs vs rollouts）。没有控制实验来隔离这些因素，C3（supervision granularity 解释）是不可靠的。\n\n---\n\n**[AGREE] R1-W3: 单模型验证**\n\n与我的 N2 完全一致。不再赘述。\n\n---\n\n**[REBUT] R1-W4: stopped gradient 论证力度被高估**\n\nR1 认为 \"论文将 stopped gradient 的论证力度描述得过高\"。我部分不同意。\n\n回到原文 Section 5（第 6 页），stopped gradient 变体（F1c: stopped dot product, F1d: mode collapse）被明确定位为诊断链中的一步——排除 \"梯度通过 d_syc 回传导致方向被 corrupt\" 这一特定假说。论文的表述是（paraphrasing）：\"F1c/F1d 的失败排除了梯度操纵假说，将问题指向 d_syc 的语义局限性。\" 这是一个合理的消去推理步骤。\n\n论文没有声称 stopped gradient 证明了 \"d_syc 编码错了东西\"——它只是排除了一个特定的 alternative（gradient-based manipulation）。在诊断链中，每一步排除一个假说是标准方法论。\n\n**但 R1 有一个隐含的有效批评**：如果 C1（group_size noise）和 C2（truncation quality）才是真正的失败原因，那么 stopped gradient 排除的假说虽然被正确排除，但排除它也不能指向 \"语义局限性\"——因为还有其他未排除的 confound。所以 stopped gradient 的论证力在逻辑上是正确的，但在 R1 指出的更大 confound 背景下，其指向性被削弱了。\n\n总结：论证逻辑本身不过度，但在 C1/C2 未排除的背景下，其推论的终点（语义局限性）确实过早。\n\n---\n\n**[AGREE] R1-W5: GPT-4.1 对比对的分布偏差**\n\n同意这是一个有效关切。论文 Section 3.1（第 4 页）提到使用 GPT-4.1 (OpenAI, 2025) 以两阶段 pipeline 生成对比对：skeleton generation + dialogue completion。虽然论文有一些质量控制措施（style matching: response-length difference <10%，evidence strength 三档标注，automated validation 丢弃了 19/200 对），但 GPT-4.1 生成的 sycophantic 响应可能与真实 LLM sycophancy 存在系统性差异。\n\n具体风险：\n- GPT-4.1 的 sycophancy 风格可能过于明显/模式化，使得 d_syc 学到了 GPT-4.1 的写作风格特征而非通用的 sycophancy 信号\n- 论文用这些对比对在 Qwen3-8B 上提取方向，但 Qwen3-8B 自己产生的 sycophancy 可能有不同的 surface patterns\n\n不过这一问题的严重性有限：Section 4 的 cross-model validation（Llama-3-8B 上 AUROC 0.779）和 evidence-strength gradient 分析提供了一些间接证据说明 d_syc 捕获的是语义信号而非 style artifacts。\n\n---\n\n### 总结性评估\n\nR1 的审稿揭示了两个我初审未充分关注的重要问题：**group_size=2 的 confound（C1）和 256-token truncation 对 reward quality 的实际影响（C2）**。这两个问题与我自己的 N3（ACT/GRPO 混淆变量）和 W4（d_syc 质量问题）形成互补，共同构成一个强有力的替代解释：\n\n> 论文观察到的所有 \"probe reward trap\" 现象，可能完全由 (a) group_size=2 的 noisy advantage estimation + (b) 256-token truncation 导致的 reward quality 退化所解释，无需诉诸 \"d_syc 有根本性语义局限\" 这一更强的结论。\n\n如果作者能提供 group_size≥8 + 更长 completion length 的消融实验，且 probe reward trap 仍然出现，这将显著增强论文的核心论证。在当前证据下，**我维持 Overall 3.0 (Findings) 的评分**，但 soundness 评分下调至 **2.5/5**（受 C1/C2 confound 影响）。\n\nR1 和我在整体判断上一致：这是一篇方法论上有缺陷但选题有价值的工作，目前证据支持 Findings 接收，但不足以支持 main conference。",
    "reviewer_id": "2",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-25T23:47:40.903683+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3566
}
```

</details>

---


### Assistant

_source line 776 · 2026-05-25T23:47:47.827240+00:00_

交叉回应已提交。

对 R1 的 8 个问题：**6 个 AGREE，1 个 REBUT（W4 stopped gradient），1 个 AGREE with nuance（W5）**。

核心共识：R1 发现的 group_size=2 confound（C1）和 256-token truncation quality degradation（C2）是我初审遗漏的重要问题，与我的 N3/W4 互补，共同构成一个强替代解释——训练失败可能源于 noisy advantage estimation + 低质量 reward signal，而非 d_syc 的根本性语义局限。Soundness 评分从 3/5 下调至 2.5/5，Overall 维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2"
}
```

</details>

---
