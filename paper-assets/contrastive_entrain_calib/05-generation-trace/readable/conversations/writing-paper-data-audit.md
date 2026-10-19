# writing paper data audit

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_writing_paper-data-audit_20260525T083134.jsonl`
- **Structured JSON:** [`24bd37fc6c666bfc45fd.json`](../../sessions/24/24bd37fc6c666bfc45fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-25T08:39:14.296246+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/",
  "description": "List all section tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/",
    "description": "List all section tex files"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T08:39:14.296592+00:00_

abstract.tex
appendix.tex
conclusion.tex
cosine_failure.tex
direction_quality.tex
discussion.tex
framework.tex
introduction.tex
limitations.tex
probe_trap.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T08:39:14.296768+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/*.tex",
  "description": "List top-level tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/*.tex",
    "description": "List top-level tex files"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T08:39:14.296953+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T08:39:14.297097+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T08:39:14.297223+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T08:39:14.297354+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T08:39:14.297482+00:00_

1	Representation engineering reveals that sycophancy is linearly encoded in LLM residual streams, suggesting that such directions could serve as training signals for alignment. We test this premise systematically and document its failure. A contrastive sycophancy direction $\dsyc$ reliably discriminates sycophantic from non-sycophantic activations, yet every formulation that converts it into a Group Relative Policy Optimization (GRPO) reward collapses. We identify the \emph{probe reward trap}: when a periodically retrained linear probe on $\dsyc$ is used as a non-differentiable reward signal, behavioral death occurs within 500 steps while generation entropy remains healthy (0.70), creating a 1{,}300-step monitoring blind spot that entropy-based safeguards miss entirely. The failure persists with stopped gradients, implicating the direction's semantic limitation rather than optimization dynamics: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. The failure extends beyond probe rewards: behavioral-reward-only GRPO exceeds vanilla at only 4/28 checkpoints across two seeds, while dense per-token supervised fine-tuning succeeds at every checkpoint (31/31 across two seeds). A Low-Rank Adaptation (LoRA) ablation identifies supervision granularity as one plausible explanation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T08:39:14.297610+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T08:39:14.297769+00:00_

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
…[truncated 3405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T08:39:14.297960+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T08:39:14.298153+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T08:39:14.298316+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T08:39:14.298481+00:00_

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
…[truncated 3752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T08:39:14.298625+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T08:39:14.298779+00:00_

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
11	Replication across two seeds (42, 43) confirms determinism: both collapse within ${\sim}50$ steps, with each probe retraining (AUROC ${\to}1.0$) re-gamed within ${\sim}10$ steps.
12	This motivates the stopped-gradient design below.
13	
14	\paragraph{Binary probe: the stubbornness trap.}
15	With stop-gradient, the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
16	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
17	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix
…[truncated 2221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T08:39:14.298949+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T08:39:14.299107+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T08:39:14.299255+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T08:39:14.299439+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately (mode collapse, F1c--F1d); the binary probe $\rone$ rewards all resistance regardless of input validity (stubbornness trap, $\tof{=}0$ by step 500)---dual consequences of a direction that conflates resisting invalid challenges with refusing valid corrections.
8	Although $\dsyc$ separability correlates with evidence strength (\S\ref{sec:direction_quality}), it encodes \emph{how much} belief changed, not whether the change was appropriate (\S\ref{sec:probe_trap}).
9	Cross-model evidence (Llama-3-8B AUROC $0.779$) confirms the limitation generalizes.
10	This contrasts with safety directions~\citep{zhang2026latentgrpo}, where the target behavior is geometrically distinct; concept directions succeed when shortcuts are separable~\citep{wu2026rewardhacking}.
11	Independent work corroborates: persona vectors are independent of $\dsyc$ \citep{kelkar2026persona}, and sycophancy sub-behaviors \citep{vennemeyer2025sycophancy} collapse onto $\dsyc$'s single axis.
12	
13	\paragraph{GRPO results under our configuration.}
14	
15	\begin{table}[t]
16	\centering
17	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the harmonic mean of the true-positive flip rate ($\tof$) and no-flip rate ($\nof$); higher indicates better calibration. Best result in \textbf{bold}. $^\dagger$Best checkpoint (seed 1, step 6500); only 4/28 checkpoints across two s
…[truncated 6685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T08:39:14.299582+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T08:39:14.299706+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, evading entropy monitoring entirely.
4	$\dsyc$-based rewards collapse because the direction conflates warranted revision with unwarranted capitulation; $\rthree$-only GRPO fails independently (4/28 checkpoints ${>}$ vanilla across two seeds), implicating the per-completion reward structure itself~(\S\ref{sec:discussion}), while per-token SFT succeeds at every checkpoint (31/31 across two seeds).
5	Discriminability does not guarantee reward utility: linear directions can diagnose behavior at inference time, but the step to training signal is not automatic.
6	Practitioners should verify geometric separability before deploying directions as rewards and monitor behavior directly, not entropy alone.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T08:39:14.299828+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T08:39:14.300009+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe, marks2024geometry}; inference-time methods such as Inference-Time Intervention \citep[ITI;][]{li2023iti}, Activation Addition \citep[ActAdd;][]{turner2023actadd}, and Contrastive Activation Addition \citep[CAA;][]{rimsky2024caa} demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}, but we find that $\dsyc$ fails when used as an RL reward despite succeeding at inference time.
5	
6	\paragraph{Reward Design and Overoptimization.}
7	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling, pan2022effects}.
8	\citet{manheim2019goodhart} taxonomize four Goodhart variants: \emph{regressional} (proxy-target correlation breaks under optimization shift), \emph{extremal} (divergence at distribution tails), \emph{causal} (intervening on proxy severs its link to the target), and \emph{adversarial} (an agent explicitly exploits the proxy).
9	Our probe reward trap instantiates the regressional variant: $\dsyc$ discriminates sycophantic activations under the pre-training distribution but ceases to correlate with the target once optimization shifts the policy.
10	The failure is not extremal (collapse occurs at moderate optimization pressure, not distribution tails), not causal (stopped gradients prevent intervention on the direction), and not adversarial (the policy does not model the probe).
11	The incremental contribution over prior regressional analyses~\citep{gao2023scaling} is temporal: we document behavioral death within 500 steps---an order of magnitude faster than gradual degradation curves---and a 1{,}300-step lag that renders entropy monitoring blind~\citep{skalse2022hacking}.
12	\citet{wu2026rewardhacking} show that representation-level directions succeed when behaviors are geometrically separable (\S\ref{sec:discussi
…[truncated 1749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T08:39:14.300156+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T08:39:14.300283+00:00_

1	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
2	The ACT vs.\ GRPO comparison differs along multiple dimensions (sequence length, data source, dropout); our LoRA-controlled ablation isolates adapter capacity, but a fully controlled comparison would require matching all hyperparameters.
3	The probe trap's 1{,}300-step behavioral-distributional lag is observed from a single seed ($n{=}1$); gradient gaming is replicated across two seeds (\S\ref{sec:probe_trap}), but replication of the temporal lag across seeds and models would strengthen confidence.
4	Code, data, and configurations are available at \url{https://github.com/anonymous-nlp-2026-2/contrastive_entrain_calib}.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T08:39:14.300405+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T08:39:14.300567+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}$=$256.
10	Across all 362 evaluation responses, the maximum observed length is 129 tokens (Qwen tokenizer) and 155 tokens (DeBERTa tokenizer), so no response was actually truncated at inference time.
11	Full-length vs.\ 256-truncated NLI agreement is 100\%, confirming that the truncation setting does not affect $\rthree$ reward computation.
12	Truncation may affect $\dsyc$ AUROC at the direction extraction stage (0.76 vs.\ 0.60; see Limitations).
13	
14	\paragraph{Hyperparameters.}
15	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
16	
17	\begin{table}[h]
18	\centering
19	\small
20	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
21	\label{tab:hyperparams}
22	\begin{tabular}{lcc}
23	\toprule
24	& GRPO (F1, F3)$^e$ & ACT \\
25	\midrule
26	Learning rate & 5e-5 & 5e-5 \\
27	Effective batch & 16 & 16 \\
28	Max steps & 8{,}000 & 8{,}000 \\
29	Warmup steps & 200 & 200 \\
30	LR schedule & linear$^a$ & linear \\
31	Grad.\ clipping & -- & 1.0 \\
32	\midrule
33	LoRA rank & 64 & 64 \\
34	LoRA $\alpha$ & 64 & 128 \\
35	LoRA modules & 4$^b$ & 7$^c$ \\
36	LoRA dropout & 0 & 0.05 \\
37	\midrule
38	Group size & 2$^d$ & -- \\
39	KL (Kullback--Leibler) $\beta$ & 0.04 & -- \\
40	Max compl.\ len. & 256 & -- \\
41	Max seq.\ len. & -- & 1{,}024 \\
42	L2 loss weight 
…[truncated 2963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T08:39:14.300740+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T08:39:14.300975+00:00_

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
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T08:39:14.301133+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "limit": "0",
  "fields": "['metrics', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "limit": "0",
    "fields": "['metrics', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T08:39:14.301793+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-act-256\": {\"conclusion\": \"killed\"}, \"exp-003-len512-v3\": {\"conclusion\": \"killed\"}, \"exp-008-seed4\": {\"metrics\": {\"training_summary\": {\"total_steps\": 2000, \"probe_gaming_onset\": \"step ~60 (S(t) → 0)\", \"probe_retrain_count\": 20, \"probe_retrain_acc\": \"1.0 every retrain\", \"probe_retrain_auroc\": \"1.0 every retrain\", \"final_loss\": -0.0622, \"final_sft_loss\": 0.0002, \"step_time_sec\": 3.5}}}, \"exp-008-seed4-eval\": {}, \"exp-008-seed3\": {\"metrics\": {\"eval\": {\"ckpt-500\": {\"ToF\": 0.2541, \"NoF\": 0.7403, \"SYCONScore\": 0.3784, \"entropy\": 0.454}, \"ckpt-1000\": {\"ToF\": 0.2873, \"NoF\": 0.6961, \"SYCONScore\": 0.4067, \"entropy\": 0.1752}, \"ckpt-1500\": {\"ToF\": 0.1878, \"NoF\": 0.8287, \"SYCONScore\": 0.3063, \"entropy\": 0.1424}, \"ckpt-2000\": {\"ToF\": 0.0442, \"NoF\": 0.9613, \"SYCONScore\": 0.0845, \"entropy\": 0.1701}, \"final\": {\"ToF\": 0.0442, \"NoF\": 0.9613, \"SYCONScore\": 0.0845, \"entropy\": 0.1701}}, \"best_checkpoint\": \"ckpt-1000\", \"best_sycon\": 0.4067, \"trend\": \"peaks at ckpt-1000, then monotonic decline; ckpt-2000 and final identical — converged before step 2000, clear overfitting after ckpt-1000\"}, \"conclusion\": \"success\"}, \"exp-008-seed2\": {\"metrics\": {\"training_summary\": {\"total_steps\": 2000, \"probe_gaming_onset\": \"step ~50 (S(t) → 0)\", \"probe_retrain_count\": 20, \"probe_retrain_acc\": \"1.0 every retrain\", \"probe_retrain_auroc\": \"1.0 every retrain\", \"post_retrain_gaming\": \"~10 steps after each retrain S(t) returns to 0\", \"step_time_sec\": 3.5}, \"eval\": {\"ckpt-500\": {\"ToF\": 0.2762, \"NoF\": 0.6796, \"SYCONScore\": 0.3928, \"entropy\": 0.364}, \"ckpt-1000\": {\"ToF\": 0.1492, \"NoF\": 0.884, \"SYCONScore\": 0.2553, \"entropy\": 0.222}, \"ckpt-1500\": {\"ToF\": 0.105, \"NoF\": 0.9392, \"SYCONScore\": 0.1888, \"entropy\": 0.328}, \"ckpt-2000\": {\"ToF\": 0.0442, \"NoF\": 0.9724, \"SYCONScore\": 0.
…[truncated 30122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T08:39:14.302229+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "XX\\.X|TBD|TODO|FIXME|\\?\\?|---[^}]|\\\\textcolor|PLACEHOLDER|FILL|CITE",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Grep",
  "tool_args": {
    "pattern": "XX\\.X|TBD|TODO|FIXME|\\?\\?|---[^}]|\\\\textcolor|PLACEHOLDER|FILL|CITE",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T08:39:14.302407+00:00_

docs/paper/_stale/related_work.tex:5:Inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control at test time.
docs/paper/_stale/discussion.tex:38:The $\sycon$ trajectory shows partial recovery that peaks at vanilla: 0.074 at checkpoint 1000, 0.085 at checkpoint 2000, 0.095 at checkpoint 3000, 0.114 at checkpoint 4000, a transient spike to 0.134 at checkpoint 4500---approximately matching vanilla in $\sycon$---followed by regression to 0.114 at checkpoints 5000 and 5500.
docs/paper/_stale/introduction.tex:18:The ceiling of sparse behavioral reward is the untrained vanilla level---it cannot push calibration beyond the pre-training baseline.
docs/paper/_stale/cosine_failure.tex:25:Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
docs/paper/_stale/cosine_failure.tex:31:This is not a calibration artifact---recalibration improves discriminability yet rewards still fail---but a semantic limitation of any continuous $\dsyc$-based reward.
docs/paper/acl.sty:115:% save space --- suggested by drstrip@sandia-2
docs/paper/sections/related_work.tex:11:The incremental contribution over prior regressional analyses~\citep{gao2023scaling} is temporal: we document behavioral death within 500 steps---an order of magnitude faster than gradual degradation curves---and a 1{,}300-step lag that renders entropy monitoring blind~\citep{skalse2022hacking}.
docs/paper/sections/probe_trap.tex:52:Escaping requires a signal encoding the evidential warrant of the user's challenge---a dimension absent from $\dsyc$~\citep{denison2024subterfuge}.
docs/paper/sections/discussion.tex:7:Cosine $\rone$ penalizes all belief change indiscriminately (mode collapse, F1c--F1d); the binary probe $\rone$ rewards all resistance regardle
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T08:39:14.302568+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{\\\\?\\}|\\\\ref\\{\\\\?\\}|NEED|MISSING|DUMMY",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{\\\\?\\}|\\\\ref\\{\\\\?\\}|NEED|MISSING|DUMMY",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T08:39:14.302702+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T08:39:14.302891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex",
  "offset": "54",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex",
    "offset": "54",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T08:39:14.303033+00:00_

54	
55	\paragraph{Early termination criterion.}
56	We applied early termination to gs$=$8 after three consecutive declining checkpoints ($\sycon$: $0.084{\to}0.085{\to}0.054$).
57	The same criterion would not have terminated gs$=$2, whose initial trajectory was monotonically increasing ($0.074{\to}0.085{\to}0.095$); gs$=$2 first exhibited three consecutive declines in the step 4500--6000 range, well into training.
58	
59	\paragraph{GRPO reward variants.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T08:39:14.303212+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex",
  "old_string": "We applied early termination to gs$=$8 after three consecutive declining checkpoints ($\\sycon$: $0.084{\\to}0.085{\\to}0.054$).",
  "new_string": "We applied early termination to gs$=$8 after three consecutive checkpoints showed no sustained improvement ($\\sycon$: $0.084{\\to}0.085{\\to}0.054$, all well below vanilla)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex",
    "old_string": "We applied early termination to gs$=$8 after three consecutive declining checkpoints ($\\sycon$: $0.084{\\to}0.085{\\to}0.054$).",
    "new_string": "We applied early termination to gs$=$8 after three consecutive checkpoints showed no sustained improvement ($\\sycon$: $0.084{\\to}0.085{\\to}0.054$, all well below vanilla)."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T08:39:14.303366+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_paper-data-audit_20260525T083134",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-25T08:39:14.303561+00:00_

修复完成。以下是完整审计报告。

---

## 数据一致性审计报告

### (a) 修改记录

| 文件 | 行号 | 旧值 | 新值 | 原因 |
|------|------|------|------|------|
| `appendix.tex` | L56 | "three consecutive declining checkpoints" | "three consecutive checkpoints showed no sustained improvement (..., all well below vanilla)" | Registry: gs=8 轨迹为 0.0844→0.0845→0.0538，第一步是微增(+0.0001)不是下降 |

### (b) 一致性核对结果：全部通过

6 处交叉核对均一致：

**AUROC 值**：
- Intro 用近似值 0.83/0.78，Framework/Direction Quality 用精确值 0.827±0.028 / 0.779±0.019 — 一致 ✓
- Registry truth: 0.8269±0.0278 (Qwen), 0.7793±0.0189 (Llama) — 四舍五入正确 ✓

**4/28 GRPO > vanilla**：Abstract、Intro(×2)、Discussion(×2)、Conclusion、Fig caption — 全部一致 ✓。14.3% = 4/28 ✓

**31/31 ACT > vanilla**：Abstract、Intro(×2)、Discussion、Conclusion、Fig caption — 全部一致 ✓。Registry 确认 16/16 (s1) + 15/15 (s2) = 31/31 ✓

**1,300-step lag**：Abstract、Intro(×2)、Probe Trap(×2)、Conclusion、Related Work、Limitations — 全部一致 ✓ (1840-500=1340≈1300)

**Entropy 0.70**：Abstract、Intro、Probe Trap table (0.702→0.70) — 一致 ✓

**Vanilla 0.134**：Main table、Ablation table footnote — 一致 ✓。Registry: 0.1335→0.134 ✓

### 主结果表 vs Registry 逐行核对

| 方法 | 论文 SYCONScore | Registry 值 | 匹配 |
|------|----------------|-------------|------|
| Vanilla | 0.134 | 0.1335 | ✓ |
| Cosine R1 (F1a-d) | 0.000 | collapse confirmed | ✓ |
| Binary Probe (F2) | 0.000 | exp-008v3: 0.000 | ✓ |
| Continuous Probe (F3) | 0.124 | exp-009: 0.1238 | ✓ |
| R3-only GRPO | 0.153 | exp-003 ckpt-6500: 0.1529 | ✓ |
| SFT probe (s2) | 0.393 | exp-008-seed2: 0.3928 | ✓ |
| SFT probe (s3) | 0.407 | exp-008-seed3: 0.4067 | ✓ |
| ActAdd α=5 | 0.054 | exp-016: 0.0537 | ✓ |
| ACT s1 | 0.301 | exp-004 ckpt-8000: 0.3013 | ✓ |
| ACT s2 | 0.286 | exp-004-s2 ckpt-7000: 0.2858 | ✓ |

### Ablation 表 vs Registry

| 方法 | 论文 Best | Registry | 匹配 |
|------|----------|----------|------|
| GRPO gs=2 | 0.153, 4/28 | 0.1529, 4/28 | ✓ |
| GRPO gs=8 | 0.085, 0/3 | 0.0845, 0/3 | ✓ |
| ACT reduced | 0.326, 16/16 | 0.3257, 16/16 | ✓ |
| ACT full s1 | 0.301, 16/16 | 0.3013, 16/16 | ✓ |
| ACT full s2 | 0.286, 15/15 | 0.2858, 15/15 | ✓ |

### Direction Quality 表 vs Registry

| 指标 | 论文 | Registry | 匹配 |
|------|------|----------|------|
| Qwen L19 AUROC | 0.827±0.028 | 0.8269±0.0278 | ✓ |
| Qwen weak/med/strong | 0.675/0.883/0.929 | 0.675/0.883/0.929 | ✓ |
| Llama L16 AUROC | 0.779±0.019 | 0.7793±0.0189 | ✓ |
| Llama weak/med/strong | 0.711/0.864/0.911 | 0.7106/0.8635/0.9109 | ✓ |
| Probe vs random | 0.835 vs 0.727 (Δ+0.108) | 0.835/0.727/0.108 | ✓ |

### (c) 占位符检查

搜索 `XX.X`, `TBD`, `TODO`, `FIXME`, `??`, `PLACEHOLDER`, `\cite{?}`, `\ref{?}` — **无占位符**。

### (d) 需要 Director 确认的问题

1. **Discussion held-out 0.205 的来源**：`discussion.tex` L87 写 "held-out $0.205$, $3.7{\times}$ vanilla"。Registry 中 ACT s1 ckpt-500 held-out = 0.2045→0.205，ckpt-8000 held-out = 0.2841。用 ckpt-500 的 held-out 值而非最佳 checkpoint 的，是否有意为之？如果是报告最佳 checkpoint 的 held-out，应改为 0.284。

2. **Cosine failure 两处 AUROC 基线差异**：`cosine_failure.tex` L4 写 "from 0.827 to approximately 0.60"，L30 写 "from 0.76 (full response) to 0.60"。前者是离线 CV AUROC→截断后 AUROC，后者是训练时全长→截断 AUROC。两处描述不同测量语境，可能让读者误以为矛盾。建议确认是否需要加一句澄清。

3. **Probe gaming onset 的 "~30 steps"**：`probe_trap.tex` L10 写 "within ~30 steps"，L11 写 "both collapse within ~50 steps"。Registry 显示两个 seed 分别在 ~50 和 ~60 步 onset。~30 偏低，但因为是近似值（~），不一定需要修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_paper-data-audit_20260525T083134"
}
```

</details>

---
