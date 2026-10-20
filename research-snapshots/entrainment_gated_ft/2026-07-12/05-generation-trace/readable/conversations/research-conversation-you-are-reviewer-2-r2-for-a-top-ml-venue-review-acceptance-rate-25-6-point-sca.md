# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae9b035990daf2b76.jsonl`
- **Structured JSON:** [`76aeb50b64d83ab1d76d.json`](../../sessions/76/76aeb50b64d83ab1d76d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-16T03:01:18.806Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus area is **Novelty and Related Work**.

## Paper Summary

**Title:** "Per-Head KV Cache Quantization: When It Helps, When It Hurts, and How to Tell"

**Core claim:** Per-head mixed-precision KV cache quantization rarely helps. At 4× compression, only 1/5 architectures (Qwen2.5-7B) benefits (+29.4% PPL reduction); the other four show no benefit or minor degradation. The paper frames itself as a systematic empirical study providing: (1) a cross-architecture benchmark, (2) a sensitivity-based taxonomy (Spread/Spike/Flat), (3) a two-metric diagnostic (top-5% concentration ≥0.50 AND t1/t5 ≤0.70).

**Architectures tested:** Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, Yi-1.5-9B, Gemma-2-9B (all 7-14B scale).

**Key experimental results:**
- Table 1 (Cross-arch benchmark): Qwen +29.4%, Yi ≈0%, Llama +0.2%, Mistral -0.4%, Gemma-2 -0.3%
- Table 3 (Downstream eval, 0-shot): Qwen +1.9pp avg; Yi -0.77pp; Llama -0.99pp; Mistral -0.48pp; Gemma-2 +0.14pp. No multi-seed CI.
- Table 4 (Budget sweep, Qwen only): 2× +3.4%, 4× +29.4%, 8× >45×
- Table 5 (Compounding sweep): Architecture-specific patterns (Qwen U-shape, Llama flat-then-cliff, Mistral monotonic). Paper acknowledges compounding is a known phenomenon (RateQuant Appendix M).
- Table 6 (Solver comparison): Greedy=MCKP under constraint. Paper acknowledges RateQuant greedy designed for {2,...,6} not {2,4,8,16}.
- Table 7 (Oracle): Avg gap 0.005 PPL → constrained problem trivially small.
- Table 8 (L0 heuristic): Captures ~80% of MCKP benefit on Qwen at zero cost.
- Table 10 (K/V separation): Hurts by 0.31 PPL. Paper acknowledges RateQuant's approach may be better.
- Table 11 (Multi-seed): 3 seeds on Qwen only, 90.2% allocation agreement.
- Table 13 (Inference): 8% latency overhead, same compression.
- 70B profiling killed.
- Diagnostic validated on n=5 models, 100% correct classification.

**Related work cited:**
- KIVI [Liu et al., 2024]: uniform per-channel K, per-token V quantization
- KVQuant [Hooper et al., 2024]: sensitivity-weighted non-uniform quantization with outlier-aware calibration
- GEAR [Kang et al., 2024]: low-rank + quantization
- RateQuant [Zhang et al., 2024]: rate-distortion framework, greedy on consecutive {2,...,6}, Appendix M discusses compounding
- HAWQ [Dong et al., 2019]: Hessian-based mixed-precision for weights

**Paper's claimed contributions:**
1. Systematic benchmark across 5 architectures
2. Sensitivity taxonomy (Spread/Spike/Flat)
3. Two-metric diagnostic
4. Compounding characterization + cardinality constraint
5. Solver equivalence finding
6. Honest negative results

**Experiment design context:**
- 18 planned experiments covering cross-architecture, downstream, budget sweep, compounding, solver comparison, oracle, L0 heuristic, profiling resolution, K/V separation, multi-seed, cross-dataset, inference perf, 70B attempt
- Key limitations: n=5 architectures, multi-seed only on Qwen (3 seeds), no experimental comparison with KIVI/GEAR/KVQuant, 70B killed, budget sweep only on Qwen

## Your Review Task

Evaluate **novelty** and **related work** positioning with the following structure:

### 1. Novelty Assessment
- Is the "systematic empirical study" framing sufficient for a top venue? What precedent exists for negative-result / benchmark papers being accepted?
- Is the sensitivity taxonomy (Spread/Spike/Flat) a novel contribution or a straightforward categorization of distribution shapes?
- Is the two-metric diagnostic novel? How does it compare to existing profiling-based decision-making in quantization literature?
- Is the compounding characterization novel given RateQuant Appendix M already discusses it?
- Is the cardinality constraint (single parameter k) a contribution or trivial regularization?
- Is solver equivalence (greedy=MCKP under constraint) surprising or expected?
- The "honest negative results" framing — does reporting negative results constitute a contribution?

### 2. Related Work Positioning
- Is the related work section adequate? Key omissions?
- Only 5 references — is this sufficient for a top venue paper?
- KIVI, KVQuant, GEAR are cited but not experimentally compared. How significant is this gap?
- The RateQuant comparison is acknowledged as unfair (evaluating greedy on non-consecutive set). Does this undermine or strengthen the paper?
- Missing related work: SqueezeLLM, QuIP, AQLM, QServe, FlexGen, etc.? Mixed-precision inference literature?
- How does this work position against the broader quantization literature?

### 3. Contribution Significance
- For a top venue (25% acceptance rate): do the contributions meet the bar?
- What would elevate this paper to acceptance?
- Is the negative-result framing executed well enough to stand on its own?

### 4. Strengths and Weaknesses (bullet lists)

### 5. Questions for Authors (3-5 specific questions)

### 6. Score and Confidence
- Overall score (1-6)
- Confidence (1-5: 1=low, 5=expert)
- One-line summary

Be rigorous and fair. Evaluate the paper on what it claims to be (a systematic empirical study), not on what it doesn't claim to be (a novel algorithm paper).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "8158cc49-ebaa-4acc-bf24-aa3d7ce505b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T03:01:18.809Z_

```json
{
  "parentUuid": "8158cc49-ebaa-4acc-bf24-aa3d7ce505b1",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9a7a8df8-a617-41ef-b29c-f69bb7fc9910",
  "timestamp": "2026-05-16T03:01:18.809Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-16T03:01:20.871Z_



I'll start by reading the paper's key sections to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a7a8df8-a617-41ef-b29c-f69bb7fc9910",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W5hAy3YP72a1iNYUtG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0db7e631-2af4-432e-ae12-8fac02262cfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sQsaBUmCAKzwS4FbHD5Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7435,
      "cache_read_input_tokens": 9324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7435,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T03:01:22.273Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pv4a1kGEC81Q9G6ZUEcMTH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db7e631-2af4-432e-ae12-8fac02262cfc",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W5hAy3YP72a1iNYUtG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d9399b2-6dd5-41ae-9b90-8de4561d0abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sQsaBUmCAKzwS4FbHD5Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7435,
      "cache_read_input_tokens": 9324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7435,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T03:01:22.280Z_

<details><summary>↩ Tool result · `toolu_01Pv4a1kGEC81Q9G6ZUEcMTH`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The issue traces not to solver suboptimality but to a violation of the additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.
17	The additive model predicts $\sim$11 PPL; the actual PPL is $3$--$4\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.
18	
19	This observation points to a minimal intervention: cap the number of 2-bit assignments.
20	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
21	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 10.91 PPL---a 29.4\% reduction over uniform 4-bit.
22	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
23	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
24	The constraint is beneficial even on flat-distribution architectures: on Gemma-2-9B, unconstrained MCKP assigns 31.5\% of heads to 2-bit, producing a moderate $1.47\times$ degradation; the constraint reduces this to within 0.5\% of uniform.
25	
26	A surprising consequence is that the cardinality constraint renders solver choice irrelevant.
27	Constrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm.
28	A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
29	
30	However, non-uniform allocation does not help universally.
31	On the remaining eight models---including Qwen2.5-14B, where the $3.4\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.
32	The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').
33	
34	This motivates a question prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
35	We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.
36	Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
37	
38	Our contributions are:
39	\begin{enumerate}[nosep]
40	\item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
41	
42	\item RateQuant~\cite{zuo2026ratequant} formalized per-head MCKP and proved greedy optimality for consecutive integer bit-widths. Our algorithmic contribution is a single cardinality constraint (Eq.~\ref{eq:constraint}); the scientific contribution is the systematic finding that this constraint suffices to prevent compounding, yet eight of nine tested models do not benefit from non-uniform allocation---the constraint renders solver choice irrelevant, with constrained greedy and MCKP producing equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
43	
44	\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d9399b2-6dd5-41ae-9b90-8de4561d0abf",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "7d5f5c32-249c-4f59-8b88-6ca97c85df23",
  "sourceToolAssistantUUID": "5d9399b2-6dd5-41ae-9b90-8de4561d0abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T03:01:22.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F7PkfgUMiRjtbPcZXea9wj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d5f5c32-249c-4f59-8b88-6ca97c85df23",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W5hAy3YP72a1iNYUtG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14fbd34c-0aa3-4a95-8e35-78c67fbf1454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sQsaBUmCAKzwS4FbHD5Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7435,
      "cache_read_input_tokens": 9324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7435,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T03:01:22.761Z_

<details><summary>↩ Tool result · `toolu_01F7PkfgUMiRjtbPcZXea9wj`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\mathcal{B} = \{2, 4, 8, 16\}$, without per-token scaling.
25	We profile each head by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
26	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
27	
28	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
29	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
30	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
31	
32	\subsection{Compounding Effect}
33	\label{sec:compounding}
34	
35	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.
36	
37	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
38	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
39	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
40	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
41	
42	This compounding is specific to 2-bit quantization and is \emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\times$ at $k{=}64$.
43	A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.
44	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
45	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
46	
47	The relationship between $k$ and PPL is U-shaped (Figure~\ref{fig:compounding}, Appendix~\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 10.89 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.
48	
49	\subsection{Cardinality Constraint}
50	\label{sec:cardinality}
51	
52	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
53	\begin{equation}
54	\label{eq:constraint}
55	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
56	\end{equation}
57	
58	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
59	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
60	
61	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
62	
63	One might expect Layer-0 heads to require explicit protection.
64	On Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\%, L0H2: $+$23.2\%, L0H3: $+$11.7\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.
65	Running the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.
66	
67	\paragraph{Restoring additivity.}
68	The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.
69	Restricting 2-bit heads to $k \ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.
70	For Qwen2.5-7B, $k{=}8$ ($\sim$7\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\ref{fig:compounding}).
71	This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
72	
73	\subsection{Solver Equivalence}
74	\label{sec:solver_equiv}
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
80	\label{tab:solver_equiv}
81	\begin{tabular}{llcccc}
82	\toprule
83	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
84	 & & & 2-bit & 4-bit & 8/16-bit \\
85	\midrule
86	Greedy & None & 32.45 & 68 & 30 & 14 \\
87	MCKP & None & 36.92 & 75 & 33 & 4 \\
88	Greedy & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
89	MCKP & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
90	Uniform & --- & 15.45 & 0 & 112 & 0 \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}
95	
96	With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.
97	
98	\paragraph{Empirical observation.}
99	When $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.
100	The constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.
101	We verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).
102	Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.
103	Practitioners can therefore use the simpler $O(H \log H)$ greedy algorithm without sacrificing optimality.
104	
105	A per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14fbd34c-0aa3-4a95-8e35-78c67fbf1454",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "23f277ef-fe2f-46b4-8226-4b34a217625d",
  "sourceToolAssistantUUID": "14fbd34c-0aa3-4a95-8e35-78c67fbf1454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T03:01:23.224Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ng1eRiK8UaXmH4BpXzczGR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23f277ef-fe2f-46b4-8226-4b34a217625d",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W5hAy3YP72a1iNYUtG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5631745-c52d-4c4a-a7da-26b499c9addb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sQsaBUmCAKzwS4FbHD5Bn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7435,
      "cache_read_input_tokens": 9324,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 240,
          "cache_read_input_tokens": 9324,
          "cache_creation_input_tokens": 7435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7435,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T03:01:23.228Z_

<details><summary>↩ Tool result · `toolu_01Ng1eRiK8UaXmH4BpXzczGR`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate eight models spanning six architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
14	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
15	\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
16	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
17	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
18	
19	\paragraph{Evaluation.}
20	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
21	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
22	
23	\paragraph{Profiling.}
24	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
25	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
26	
27	\paragraph{Compression and constraint.}
28	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
29	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).
30	
31	\paragraph{Baselines.}
32	We compare against:
33	(1)~uniform 4-bit quantization;
34	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
35	(3)~unconstrained MCKP allocation;
36	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
37	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
38	
39	\subsection{Main Results}
40	\label{sec:main_results}
41	
42	\begin{table}[t]
43	\centering
44	\small
45	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
46	\label{tab:main_results}
47	\begin{tabular}{lccccc}
48	\toprule
49	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
50	\cmidrule(lr){4-5}
51	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
52	\midrule
53	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
54	Qwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\
55	Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
56	Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
57	Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
58	Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
59	Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\
60	Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
66	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
67	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
68	
69	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
70	Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
71	
72	On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
73	On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
74	
75	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
76	Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
77	
78	On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\times$ bf16). %exp_id=phi3_medium_constrained_mckp
79	
80	Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
81	See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
82	
83	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
84	
85	\paragraph{Comparison with KIVI.}
86	KIVI~\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.
87	At 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.
88	Within the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).
89	The two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.
90	However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.
91	Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.
92	
93	\subsection{Cross-Architecture Compounding}
94	\label{sec:compounding_cross}
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\columnwidth]{figures/fig_compounding_curves.pdf}
99	\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\times$). All three stay near-baseline for $k{\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment).}
100	\label{fig:compounding_cross}
101	\end{figure}
102	
103	Figure~\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.
104	At small $k$ (${\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\leq}2.5\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.
105	
106	Beyond $k{=}8$, divergence is stark.
107	Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.
108	Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\times$) and $98.75$ at $k{=}256$ ($10.1\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.
109	Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.
110	
111	These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\times$ baseline) is ${\sim}32$ for Qwen, ${\sim}64$ for Llama, and ${\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.
112	
113	\subsection{Downstream Evaluation}
114	\label{sec:downstream}
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen values are mean over 3 calibration seeds ($\pm$1$\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}
120	\label{tab:downstream}
121	\begin{tabular}{lccccc}
122	\toprule
123	Model & ARC-C & HS & PIQA & WG & Avg \\
124	\midrule
125	Qwen2.5-7B        & $+$0.0{\scriptsize$\pm$0.4} & $+$4.1{\scriptsize$\pm$0.2} & $+$2.0{\scriptsize$\pm$0.2} & $+$1.6{\scriptsize$\pm$1.2} & $+$1.9 \\
126	Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\
127	Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
128	Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\
129	Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
135	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
136	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
137	Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5631745-c52d-4c4a-a7da-26b499c9addb",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "997bc7c0-5c34-459c-bbe2-d43abdf91c2e",
  "sourceToolAssistantUUID": "f5631745-c52d-4c4a-a7da-26b499c9addb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T03:01:28.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q79maaTzgzeneLEEi6FtEs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997bc7c0-5c34-459c-bbe2-d43abdf91c2e",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W62HR4pQEwLpwn8TsW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a97d58f-ec23-49f8-9867-fedd398dd7bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh8FR7Me3Kt7PF9tQp53Qa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10917,
      "cache_read_input_tokens": 16759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T03:01:28.581Z_

<details><summary>↩ Tool result · `toolu_01Q79maaTzgzeneLEEi6FtEs`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling
21	
22	Llama-3.1-8B has concentration $0.57$---comparable to Qwen's $0.61$---yet its spike pattern ($t_1/t_5{=}0.85$), dominated by a single head (L2H5), yields allocation indistinguishable from uniform ($+$0.36 vs.\ $+$0.38), demonstrating that concentration alone is insufficient without spread structure. %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
23	CodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\%$ of top-5 delta, $11.3\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling
24	Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
25	
26	Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).
27	Low concentration ($0.24$) and $t_1/t_5{=}0.28$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline
28	
29	Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.24$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp
30	
31	\paragraph{Scale-dependent concentration dilution.}
32	Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is similar (0.57 vs.\ 0.68), but concentration drops from 0.61 (7B) to 0.33 (14B)---diluted by $3.4\times$ more heads into the flat regime.
33	Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.
34	Concentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\times$scale combination where non-uniform allocation helps.
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\times$ compression. $t_1/t_5$: ratio of the most sensitive head's 2-bit distortion to the sum of the top-5\% of heads' distortions (low${=}$spread, high${=}$spike); the percentage threshold ensures comparability across models with different head counts (112--400). $^*$BOS-corrected.}
40	\label{tab:heterogeneity}
41	\begin{tabular}{lcccccc}
42	\toprule
43	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
44	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
45	\midrule
46	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
47	Qwen2.5-14B & 5:1 & 0.33 & 0.68 & $+$0.33 & $+$0.35 & Flat \\
48	Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
49	Llama-3.1-8B & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
50	Mistral-7B-v0.3 & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.10 & Flat \\
51	Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
52	Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & $+$0.16 & $+$0.18 & Flat \\
53	CodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\
54	Pythia-1.4B & 1:1 & 0.24 & 0.28 & $+$7.80 & $+$7.96 & Flat \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
60	
61	\subsection{Empirical Decision Rule}
62	\label{sec:diagnostic}
63	
64	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
65	This motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.
66	Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
67	\begin{itemize}[nosep]
68	\item \textbf{Spread} (concentration $\geq 0.50$ \emph{and} $t_1/t_5 \leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
69	\item \textbf{Spike} ($t_1/t_5 > 0.70$ \emph{and} concentration $\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.
70	\item \textbf{Flat} (concentration $< 0.25$, or concentration $\in [0.25, 0.50)$ with $t_1/t_5 \leq 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.24), Gemma-2 (0.23), Phi-3-medium (0.17), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.
71	\end{itemize}
72	
73	Both conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \geq 0.70$) correctly override.
74	A concentration-only rule would misclassify all three as spread; $t_1/t_5$ is the critical second discriminator.
75	The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
76	Only Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as preliminary until confirmed on additional models.
77	The rule reuses profiling data already required by the solver and adds no overhead.
78	
79	\paragraph{Why is Qwen-7B the only spread model?}
80	We offer two non-exclusive hypotheses, both requiring further validation.
81	First, Qwen-7B's high GQA ratio (7:1) means each KV head aggregates attention from 7 query heads, potentially driving greater functional specialization and thus larger inter-head sensitivity differences.
82	However, Yi-1.5 (8:1) and Qwen-14B (5:1) have comparable or higher GQA ratios yet do not exhibit spread, so GQA ratio alone is insufficient.
83	Second, scale-dependent concentration dilution may play a role: Qwen-14B (same architecture family, $3.4\times$ more heads) dilutes into the flat regime despite similar within-head structure ($t_1/t_5$ 0.68 vs.\ 0.57).
84	This suggests that increasing head count may systematically reduce concentration, making spread less likely at larger scales---a hypothesis consistent with the Qwen-7B/14B contrast but requiring evaluation on additional model families and scales.
85	
86	Additional analyses---granularity tradeoff (Appendix~\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\ref{sec:granularity}--\ref{sec:kv_separation}.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a97d58f-ec23-49f8-9867-fedd398dd7bf",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "8b68c38c-e93b-43fc-ac3f-89a82b7c4e7b",
  "sourceToolAssistantUUID": "0a97d58f-ec23-49f8-9867-fedd398dd7bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T03:01:29.066Z_

<details open><summary>🔧 Tool call — Read · `toolu_014iye8sAjzeihMK8iaH4tDK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b68c38c-e93b-43fc-ac3f-89a82b7c4e7b",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W62HR4pQEwLpwn8TsW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ce00dd4-4ac4-4d1b-88bf-6db8af1d53fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh8FR7Me3Kt7PF9tQp53Qa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10917,
      "cache_read_input_tokens": 16759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10917,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T03:01:29.071Z_

<details><summary>↩ Tool result · `toolu_014iye8sAjzeihMK8iaH4tDK`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.
6	An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
7	Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	\paragraph{$N{=}1$ spread.}
12	The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
13	
14	\paragraph{Model scale.}
15	The largest model evaluated is 14B parameters (384 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.
16	
17	\paragraph{Runtime.}
18	All latency measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} dispatch and do not represent optimized CUDA kernel performance. The overhead reported in Appendix~\ref{sec:runtime} is an upper bound on the mixed-precision penalty; production inference engines with fused attention kernels would likely narrow this gap. No real-kernel latency benchmarks are reported.
19	
20	\paragraph{Downstream scope.}
21	Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\texttt{acc}) rather than length-normalized accuracy (\texttt{acc\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.
22	
23	\paragraph{Calibration domain.}
24	Cross-dataset stability is verified only between WikiText-2 and C4 (96--97\% bit-assignment agreement); other domains (code, dialogue, multilingual) are untested.
25	
26	\paragraph{Long-context.}
27	Long-context evaluation extends only to 8K tokens; deployment scenarios at 32K--128K context lengths are not tested.
28	
29	\paragraph{Missing direct competitors.}
30	No existing tool performs per-head mixed-precision KV cache quantization on hardware-aligned bit-widths, precluding direct comparison with an established baseline at the same granularity.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ce00dd4-4ac4-4d1b-88bf-6db8af1d53fa",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "89175c0f-d62c-4429-9b75-865fb3edfdfb",
  "sourceToolAssistantUUID": "1ce00dd4-4ac4-4d1b-88bf-6db8af1d53fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T03:01:29.488Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SvbBuspgNNn61V1sQL5NBD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89175c0f-d62c-4429-9b75-865fb3edfdfb",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W62HR4pQEwLpwn8TsW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eb3dfe4-e297-4957-a2e5-80624e766506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh8FR7Me3Kt7PF9tQp53Qa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10917,
      "cache_read_input_tokens": 16759,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 16759,
          "cache_creation_input_tokens": 10917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10917,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T03:01:29.491Z_

<details><summary>↩ Tool result · `toolu_01SvbBuspgNNn61V1sQL5NBD`</summary>

```text
1	Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\{2,4,8,16\}$ provides negligible improvement over uniform 4-bit for eight of nine models.
2	The sole exception is Qwen2.5-7B, where a cardinality-constrained solver achieves 10.91 perplexity at $4\times$ compression---a 29.4\% reduction over uniform 4-bit (15.45)---while unconstrained solvers degrade catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
3	The benefit depends not on GQA ratio or model scale, but on whether sensitivity heterogeneity is \emph{spread} across multiple heads with cross-bitwidth gradients---a pattern observed in only one model ($N{=}1$) in our study.
4	On the remaining eight models---including Qwen2.5-14B, where scaling dilutes the spread pattern---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its single-outlier ``spike'' has no cross-bitwidth gradient.
5	The cardinality constraint prevents catastrophic over-allocation on Qwen-7B and moderate degradation on flat models (Gemma-2: unconstrained $1.47\times$ degradation reduced to within 0.5\% of uniform), while rendering solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\log H)$ greedy algorithm.
6	We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eb3dfe4-e297-4957-a2e5-80624e766506",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "60f7a931-b3bd-4609-9e70-c1c1b5f9f12c",
  "sourceToolAssistantUUID": "8eb3dfe4-e297-4957-a2e5-80624e766506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T03:01:32.126Z_

Now let me check the related work / bibliography for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f7a931-b3bd-4609-9e70-c1c1b5f9f12c",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W6V6i8CgobigUd4ER5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4fb845-0e11-4bb6-a9a9-fb19fd7cfae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYTVwsABLao7AenRcFvWC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 27676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T03:01:33.675Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XJNMqvJVyYdAhb11RKuyYu`</summary>

```json
{
  "pattern": "**/refs.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4fb845-0e11-4bb6-a9a9-fb19fd7cfae7",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W6V6i8CgobigUd4ER5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60de26ec-3300-4d24-bd09-313d0f93dfd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYTVwsABLao7AenRcFvWC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 27676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T03:01:33.685Z_

<details><summary>↩ Tool result · `toolu_01XJNMqvJVyYdAhb11RKuyYu`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60de26ec-3300-4d24-bd09-313d0f93dfd2",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "d8d16691-9876-4c1c-b745-3545e1f0ba1f",
  "sourceToolAssistantUUID": "60de26ec-3300-4d24-bd09-313d0f93dfd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T03:01:34.063Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KNULKjiVFKJwWtm8F6eg5w`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8d16691-9876-4c1c-b745-3545e1f0ba1f",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W6V6i8CgobigUd4ER5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "598908ca-cf3e-4700-92dd-06a5be24bef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYTVwsABLao7AenRcFvWC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 27676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T03:01:34.073Z_

<details><summary>↩ Tool result · `toolu_01KNULKjiVFKJwWtm8F6eg5w`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "598908ca-cf3e-4700-92dd-06a5be24bef7",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "4e799d73-0adf-46bd-b44d-accbc4b49a69",
  "sourceToolAssistantUUID": "598908ca-cf3e-4700-92dd-06a5be24bef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T03:01:36.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DEGRdUTtwEhArMPJNDtwE7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e799d73-0adf-46bd-b44d-accbc4b49a69",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W6pewznqSDWDweMWq7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72865292-176f-46b8-9ce0-a1edafdb9a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBjxsL8APiVnmXQApSidtE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 32973,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 32973,
          "cache_creation_input_tokens": 374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 374,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T03:01:36.721Z_

<details><summary>↩ Tool result · `toolu_01DEGRdUTtwEhArMPJNDtwE7`</summary>

```text
1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},
47	  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},
48	  year = {2024},
49	  note = {arXiv preprint},
50	  url = {https://arxiv.org/abs/2405.06219},
51	  eprint = {2405.06219},
52	  archivePrefix = {arXiv},
53	}
54	
55	@inproceedings{zhang2023h2o,
56	  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
57	  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},
58	  year = {2023},
59	  booktitle = {NeurIPS 2023},
60	  url = {https://arxiv.org/abs/2306.14048},
61	}
62	
63	@inproceedings{li2024snapkv,
64	  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},
65	  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},
66	  year = {2024},
67	  booktitle = {NeurIPS 2024},
68	  url = {https://arxiv.org/abs/2404.14469},
69	}
70	
71	@inproceedings{ge2024fastgen,
72	  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},
73	  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},
74	  year = {2024},
75	  booktitle = {ICLR 2024},
76	  url = {https://arxiv.org/abs/2310.01801},
77	}
78	
79	@inproceedings{xiao2024streamingllm,
80	  title = {Efficient Streaming Language Models with Attention Sinks},
81	  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
82	  year = {2024},
83	  booktitle = {ICLR 2024},
84	  url = {https://arxiv.org/abs/2309.17453},
85	}
86	
87	@inproceedings{liu2024scissorhands,
88	  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},
89	  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},
90	  year = {2023},
91	  booktitle = {NeurIPS 2023},
92	  url = {https://arxiv.org/abs/2305.17118},
93	}
94	
95	@inproceedings{yang2024pyramidinfer,
96	  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},
97	  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},
98	  year = {2024},
99	  booktitle = {Findings of ACL 2024},
100	  url = {https://arxiv.org/abs/2405.12532},
101	}
102	
103	@misc{zuo2026ratequant,
104	  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},
105	  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},
106	  year = {2026},
107	  note = {arXiv preprint},
108	  url = {https://arxiv.org/abs/2605.06675},
109	  eprint = {2605.06675},
110	  archivePrefix = {arXiv},
111	}
112	
113	@misc{lei2026arkv,
114	  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
115	  author = {Jianlong Lei and Shashikant Ilager},
116	  year = {2026},
117	  note = {arXiv preprint},
118	  url = {https://arxiv.org/abs/2603.08727},
119	  eprint = {2603.08727},
120	  archivePrefix = {arXiv},
121	}
122	
123	@misc{li2025kvmix,
124	  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},
125	  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},
126	  year = {2025},
127	  note = {arXiv preprint},
128	  url = {https://arxiv.org/abs/2506.08018},
129	  eprint = {2506.08018},
130	  archivePrefix = {arXiv},
131	}
132	
133	@misc{zhang2025mixkvq,
134	  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
135	  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},
136	  year = {2025},
137	  note = {arXiv preprint},
138	  url = {https://arxiv.org/abs/2512.19206},
139	  eprint = {2512.19206},
140	  archivePrefix = {arXiv},
141	}
142	
143	@inproceedings{kim2024squeezellm,
144	  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},
145	  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},
146	  year = {2024},
147	  booktitle = {ICML 2024},
148	  url = {https://arxiv.org/abs/2306.07629},
149	}
150	
151	@inproceedings{fu2025headkv,
152	  title = {Not All Heads Matter: A Head-Level {KV} Cache Compression Method with Integrated Retrieval and Reasoning},
153	  author = {Yu Fu and Zefan Cai and Abdelrahman Sid-Lakhdar and Wayne Xin Zhao and Richard Peng},
154	  year = {2025},
155	  booktitle = {ICLR 2025},
156	  url = {https://arxiv.org/abs/2410.19258},
157	}
158	
159	@inproceedings{feng2025adakv,
160	  title = {{Ada-KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation},
161	  author = {Yuan Feng and Junlin Lv and Yukun Cao and Xike Xie and S. Kevin Zhou},
162	  year = {2025},
163	  booktitle = {NeurIPS 2025},
164	  url = {https://arxiv.org/abs/2407.11550},
165	}
166	
167	@inproceedings{li2025kvtuner,
168	  title = {{KVTuner}: Sensitivity-Aware Layer-Wise Mixed-Precision {KV} Cache Quantization for Efficient and Nearly Lossless {LLM} Inference},
169	  author = {Li, Zhongzhi and Shen, Yuhan and Tang, Yixuan and Luo, Jian and Dai, Yonggang},
170	  year = {2025},
171	  booktitle = {ICML 2025},
172	  url = {https://arxiv.org/abs/2502.04420},
173	}
174	
175	@inproceedings{voita2019analyzing,
176	  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
177	  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},
178	  year = {2019},
179	  booktitle = {ACL 2019},
180	  url = {https://arxiv.org/abs/1905.09418},
181	}
182	
183	@inproceedings{michel2019sixteen,
184	  title = {Are Sixteen Heads Really Better than One?},
185	  author = {Paul Michel and Omer Levy and Graham Neubig},
186	  year = {2019},
187	  booktitle = {NeurIPS 2019},
188	  url = {https://arxiv.org/abs/1905.10650},
189	}
190	
191	@inproceedings{dong2019hawq,
192	  title = {{HAWQ}: {Hessian} AWare Quantization of Neural Networks with Mixed-Precision},
193	  author = {Zhen Dong and Zhewei Yao and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},
194	  year = {2019},
195	  booktitle = {ICCV 2019},
196	  url = {https://arxiv.org/abs/1905.03696},
197	}
198	
199	@inproceedings{dong2020hawqv2,
200	  title = {{HAWQ-V2}: {Hessian} Aware trace-Weighted Quantization of Neural Networks},
201	  author = {Zhen Dong and Zhewei Yao and Yaohui Cai and Daiyaan Arfeen and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},
202	  year = {2020},
203	  booktitle = {NeurIPS 2020},
204	  url = {https://arxiv.org/abs/1911.03852},
205	}
206	
207	@inproceedings{wang2019haq,
208	  title = {{HAQ}: Hardware-Aware Automated Quantization with Mixed Precision},
209	  author = {Kuan Wang and Zhijian Liu and Yujun Lin and Ji Lin and Song Han},
210	  year = {2019},
211	  booktitle = {CVPR 2019},
212	  url = {https://arxiv.org/abs/1811.08886},
213	}
214	
215	@inproceedings{su2025rotatekv,
216	  title = {{RotateKV}: Accurate and Robust 2-Bit {KV} Cache Quantization for {LLMs} via Outlier-Aware Adaptive Rotations},
217	  author = {Zunhai Su and Zhe Chen and Wang Shen and Hanyu Wei and Linge Li and Huangqi Yu and Kehong Yuan},
218	  year = {2025},
219	  booktitle = {IJCAI 2025},
220	  url = {https://arxiv.org/abs/2501.16383},
221	}
222	
223	@inproceedings{sharma2025minikv,
224	  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},
225	  author = {Akshat Sharma and Hangliang Ding and Jianping Li and Neel Dani and Minjia Zhang},
226	  year = {2025},
227	  booktitle = {Findings of ACL 2025},
228	  url = {https://arxiv.org/abs/2411.18077},
229	}
230	
231	@inproceedings{shutova2025aquakv,
232	  title = {Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models},
233	  author = {Alina Shutova and Vladimir Malinovskii and Vage Egiazarian and Denis Kuznedelev and Denis Mazur and Nikita Surkov and Ivan Ermakov and Dan Alistarh},
234	  year = {2025},
235	  booktitle = {ICML 2025},
236	  url = {https://arxiv.org/abs/2501.19392},
237	}
238	
239	@misc{liu2025pmkvq,
240	  title = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-CoT {LLMs}},
241	  author = {Tengxuan Liu and Shiyao Li and Jiayi Yang and Tianchen Zhao and Feng Zhou and Xiaohui Song and Guohao Dai and Shengen Yan and Huazhong Yang and Yu Wang},
242	  year = {2025},
243	  note = {arXiv preprint},
244	  url = {https://arxiv.org/abs/2505.18610},
245	  eprint = {2505.18610},
246	  archivePrefix = {arXiv},
247	}
248	
249	@misc{xia2025kitty,
250	  title = {{Kitty}: Accurate and Efficient 2-bit {KV} Cache Quantization with Dynamic Channel-wise Precision Boost},
251	  author = {Haojun Xia and Xiaoxia Wu and Jisen Li and Robert Wu and Junxiong Wang and Jue Wang and Chenxi Li and Aman Singhal and Alay Dilipbhai Shah and Alpay Ariyak and Donglin Zhuang and Zhongzhu Zhou and Ben Athiwaratkun and Zhen Zheng and Shuaiwen Leon Song},
252	  year = {2025},
253	  note = {arXiv preprint},
254	  url = {https://arxiv.org/abs/2511.18643},
255	  eprint = {2511.18643},
256	  archivePrefix = {arXiv},
257	}
258	
259	@inproceedings{haeriboroujeni2026dontwaste,
260	  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},
261	  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},
262	  year = {2026},
263	  booktitle = {CVPR 2026},
264	  url = {https://arxiv.org/abs/2604.04722},
265	}
266	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72865292-176f-46b8-9ce0-a1edafdb9a9d",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "c911d7ae-954c-4520-bdea-52bf40cc766a",
  "sourceToolAssistantUUID": "72865292-176f-46b8-9ce0-a1edafdb9a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T03:01:39.729Z_

Now let me check the main.tex for the full related work section and any additional content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c911d7ae-954c-4520-bdea-52bf40cc766a",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W71rPxkg6KFKK4d5nm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b34a465b-3228-481d-9571-6ed779690195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2Z5ERXo7UGVNGSgRKn7Rp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5083,
      "cache_read_input_tokens": 33347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5083,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T03:01:41.370Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CQHDJGj1PVqr9mJ6xBX9bV`</summary>

```json
{
  "pattern": "docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b34a465b-3228-481d-9571-6ed779690195",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W71rPxkg6KFKK4d5nm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5226076b-a1aa-4543-adac-cb5073bc82a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2Z5ERXo7UGVNGSgRKn7Rp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5083,
      "cache_read_input_tokens": 33347,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 33347,
          "cache_creation_input_tokens": 5083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5083,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T03:01:41.391Z_

<details><summary>↩ Tool result · `toolu_01CQHDJGj1PVqr9mJ6xBX9bV`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5226076b-a1aa-4543-adac-cb5073bc82a7",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "67883d9a-0d00-4ca4-b2e9-ecc21b3d75d0",
  "sourceToolAssistantUUID": "5226076b-a1aa-4543-adac-cb5073bc82a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T03:01:44.141Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GxV5QSxihUcVx5vGydeb9L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67883d9a-0d00-4ca4-b2e9-ecc21b3d75d0",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7MutqgwDm3MenB3NJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c1cb88-fd5c-4dd8-bb9d-e166fa730a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8AbF3PGURT9yV4Pasgyrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 138,
      "cache_read_input_tokens": 38430,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 38430,
          "cache_creation_input_tokens": 138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 138,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T03:01:44.158Z_

<details><summary>↩ Tool result · `toolu_01GxV5QSxihUcVx5vGydeb9L`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c1cb88-fd5c-4dd8-bb9d-e166fa730a36",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "ee8022ad-fd69-480d-a511-7396ec375fab",
  "sourceToolAssistantUUID": "46c1cb88-fd5c-4dd8-bb9d-e166fa730a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T03:01:47.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K3YwoGBmao6A5KPfjETrTh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee8022ad-fd69-480d-a511-7396ec375fab",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7ZqzeVHbWPoebSdC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12620ce5-e622-455f-924e-347e1436bb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uezz4p6rcku1VYhu42iRFm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 38568,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 38568,
          "cache_creation_input_tokens": 390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 390,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T03:01:47.359Z_

<details><summary>↩ Tool result · `toolu_01K3YwoGBmao6A5KPfjETrTh`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, sliding-window adaptation~\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\cite{su2025rotatekv}, 2-bit with adaptive token retention~\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\cite{shutova2025aquakv}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \emph{at what precision} (bit-width selection across heads).
7	The two can be composed, though the per-channel method dominates when available (\S\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.
8	
9	\paragraph{KV Cache Eviction.}
10	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
11	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
12	
13	
14	\paragraph{Mixed-Precision Quantization (Weights).}
15	Mixed-precision allocation has a long history at the weight level.
16	HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.
17	These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.
18	KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\S\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.
19	Our primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
20	
21	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
22	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.
23	On hardware-aligned $\{2,4,8,16\}$, the 4$\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.
24	Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.
25	The constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.
26	Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\cite{xia2025kitty}, token-level via a learned on-device controller~\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\cite{lei2026arkv}---at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
27	
28	\paragraph{Attention Head Analysis.}
29	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
30	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12620ce5-e622-455f-924e-347e1436bb4d",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "d211c7de-2036-4901-9f4e-c669fc845b65",
  "sourceToolAssistantUUID": "12620ce5-e622-455f-924e-347e1436bb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-16T03:01:49.615Z_

Now let me also check the appendix for additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d211c7de-2036-4901-9f4e-c669fc845b65",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7oL7E46aUnpAH9s8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbaee905-88fd-4e6b-b37a-d518770d820c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es7sRKNKKzccPynGPnZdhN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 38958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:01:50.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ei2Rh6vBZPy1aBxh8THKJS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbaee905-88fd-4e6b-b37a-d518770d820c",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7oL7E46aUnpAH9s8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c965dd66-c370-42de-9f49-70b6d8941472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es7sRKNKKzccPynGPnZdhN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 38958,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 38958,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1668,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:01:50.033Z_

<details><summary>↩ Tool result · `toolu_01Ei2Rh6vBZPy1aBxh8THKJS`</summary>

```text
1	\appendix
2	
3	\section{Compounding Curve}
4	\label{sec:compounding_appendix}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
9	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
10	\label{fig:compounding}
11	\end{figure}
12	
13	\section{Heuristic Baselines}
14	\label{sec:heuristic_appendix}
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}2$ for Mistral). Llama and Mistral use hires profiling.}
20	\label{tab:heuristic}
21	\begin{tabular}{lcccc}
22	\toprule
23	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
24	 & & Median & Mean$\pm$Std & Positional \\
25	\midrule
26	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
27	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
28	Mistral-7B-v0.3 & 7.13  & 7.20  & 7.24$\pm$0.07  & 7.21 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL.
34	On Llama ($k{=}2$), all methods cluster within 0.17 PPL; on Mistral ($k{=}2$), MCKP (7.13) matches uniform (7.13), while heuristic baselines remain slightly worse.
35	Heuristic baselines use a slightly higher budget (0.256 vs.\ 0.248, a 3\% difference); despite this advantage, they still underperform MCKP.
36	
37	\section{Allocation Visualization}
38	\label{sec:allocation_appendix}
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
43	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
44	\label{fig:allocation}
45	\end{figure}
46	
47	\section{Per-Head Sensitivity Heatmap}
48	\label{sec:heatmap_appendix}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
53	\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}
54	\label{fig:heatmap}
55	\end{figure*}
56	
57	\section{Granularity Tradeoff}
58	\label{sec:granularity}
59	
60	Quantization budget can in principle be allocated at three granularities, each with a distinct cost--benefit profile.
61	\emph{Layer-level} allocation (KVmix~\cite{li2025kvmix}, KVTuner~\cite{li2025kvtuner}) keeps the search space small ($L$ layers) but forces all heads in a layer to share one bitwidth.
62	This is fundamentally limited when within-layer variance is large: in Qwen2.5-7B Layer-0, per-head 2-bit deltas are 6.74, 2.12, 1.31, and 1.24---a more than $5\times$ spread that any layer-level assignment must average over.
63	\emph{Per-head} allocation (ours) exposes this heterogeneity to the solver and yields a 29.4\% PPL improvement on Qwen, at the cost of $H$ profiling passes; the cardinality constraint developed in \S\ref{sec:cardinality} renders the choice of solver irrelevant, amortizing the search overhead.
64	\emph{Token-level} allocation (ZipCache~\cite{he2024zipcache}, KIVI~\cite{liu2024kivi}) is the finest grain available but introduces runtime overhead from online importance scoring.
65	Importantly, per-head and per-token granularities are orthogonal: a head's bitwidth (static, determined offline) and a token's importance (dynamic, determined online) compose without conflict, so the two can be combined.
66	Per-head therefore occupies the sweet spot for static allocation---fine enough to capture the head-level heterogeneity that drives MCKP benefit on spread-pattern models, yet free of any per-step runtime cost.
67	
68	\section{Budget Sweep}
69	\label{sec:budget_sweep}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling.}
75	\label{tab:budget_sweep}
76	\begin{tabular}{cccc}
77	\toprule
78	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
79	\midrule
80	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
81	4$\times$ & 15.45 & 11.23 & $+$4.22 \\
82	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
88	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16); constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments.
89	At 4$\times$, constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement; hires profiling further reduces this to 10.91 (Appendix~\ref{sec:profiling_resolution}).
90	At 8$\times$, both methods degrade catastrophically, but constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads.
91	
92	\section{Cross-Dataset Stability}
93	\label{sec:cross_dataset}
94	
95	To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, at $4\times$ compression.
96	On Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
97	In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on the C4 held-out split (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline on this split is 15.32).
98	All three models show ${>}96\%$ bit-assignment agreement across calibration sources: Qwen 96.4\% (108/112 heads), Llama 97.7\% (250/256), and Mistral 96.5\% (247/256).
99	Qwen's agreement is the most informative, as all 112 heads have variable assignments; on Llama, 253 of 256 heads are forced to 4-bit by the $k{=}2$ constraint, inflating agreement.
100	The cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).
101	
102	\section{Aggressive Compression}
103	\label{sec:aggressive}
104	
105	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
106	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
107	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
108	The intermediate regime ($5.3\times$) provides the largest relative benefit.
109	
110	\section{Profiling Resolution and Stability}
111	\label{sec:profiling_resolution}
112	
113	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
114	
115	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
116	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
117	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
118	
119	The additional signal changes 8 of 112 head assignments.
120	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
121	
122	\paragraph{Multi-seed stability.}
123	The profiled allocation is stable across calibration subsets.
124	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
125	The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
126	This stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.
127	
128	\paragraph{Numerical precision.}
129	Float32 profiling (64 $\times$ 2048 tokens) yields an identical constrained allocation and PPL within seed variance (10.89 vs.\ 10.91, $\Delta = 0.02 < \sigma = 0.06$), confirming that bfloat16 precision is sufficient for the profiling step.
130	
131	\paragraph{Per-layer optimality.}
132	To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
133	Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
134	All three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.
135	The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
136	
137	\section{KV Separation Ablation}
138	\label{sec:kv_separation}
139	
140	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
141	
142	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
143	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
144	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
145	
146	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
147	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
148	
149	Joint allocation is sufficient under the current constraint formulation.
150	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
151	
152	\section{Runtime Benchmark}
153	\label{sec:runtime}
154	
155	\begin{table}[ht]
156	\centering
157	\caption{PyTorch-level latency on Qwen2.5-7B (single NVIDIA RTX PRO 6000 (96\,GB), prompt\_len=256, gen\_len=128, mean of 10 runs). All conditions store KV in bf16 with simulated per-head quantize/dequantize calls; peak GPU memory is identical across rows.}
158	\label{tab:runtime}
159	\begin{tabular}{lccc}
160	\toprule
161	Condition & Prefill (ms) & Decode (ms/tok) & Throughput (tok/s) \\
162	\midrule
163	Baseline bf16       & 45.86 & 33.78 & 29.6 \\
164	Uniform 4-bit       & 54.25 & 42.46 & 23.6 \\
165	Constrained MCKP    & 57.03 & 46.09 & 21.8 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	Table~\ref{tab:runtime} reports end-to-end latency for three KV cache configurations.
171	Uniform 4-bit quantization adds 25.7\% decode overhead relative to the bf16 baseline (42.46 vs.\ 33.78~ms/tok), reflecting per-head quantize/dequantize calls at every attention step.
172	Constrained MCKP adds a further 8.5\% over uniform (46.09 vs.\ 42.46~ms/tok), because mixed-precision allocation dispatches different dequantization kernels for 2-bit, 4-bit, and 8-bit heads within the same layer.
173	The MCKP solver itself runs in ${\sim}5$~ms and is invoked once at initialization, contributing negligibly to end-to-end latency.
174	Both quantized conditions achieve the same $4\times$ KV cache compression (5.25~MB vs.\ 21~MB at bf16), so the latency difference between uniform and MCKP reflects only the mixed-precision dispatch overhead, not a memory trade-off.
175	
176	\paragraph{Caveat.}
177	These measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} calls and do \emph{not} represent optimized CUDA kernel performance.
178	Production inference engines such as vLLM and TensorRT-LLM employ fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost that dominates the gap between uniform and MCKP in our simulation.
179	The 8.5\% overhead reported here should therefore be treated as an upper bound on the mixed-precision penalty; real-world deployment with fused kernels would likely narrow or eliminate this gap.
180	As noted in the Limitations section, we report no real-kernel latency benchmarks: the numbers above quantify simulation overhead, not production inference speedup.
181	
182	\section{Long-Context Generalization}
183	\label{sec:long_context}
184	
185	\begin{table}[ht]
186	\centering
187	\small
188	\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
189	\label{tab:long_context}
190	\begin{tabular}{llcc}
191	\toprule
192	Model & Method & 2K PPL & 8K PPL \\
193	\midrule
194	 & BF16 baseline & 9.81 & 6.97 \\
195	Qwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\
196	 & Uniform 4-bit & 15.45 & 77.75 \\
197	\midrule
198	 & BF16 baseline & 8.09 & 5.60 \\
199	Llama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\
200	 & Uniform 4-bit & 8.47 & 6.04 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
206	On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
207	Constrained MCKP remains robust ($1.11\times$ at 2K, $1.23\times$ at 8K), recovering 97.7\% of the quantization loss at 8K vs.\ 80.8\% at 2K.
208	On Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\ 6.04), consistent with the 2K result.
209	The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
210	Profiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.
211	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c965dd66-c370-42de-9f49-70b6d8941472",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "021f7e2a-ef5e-4193-8d3c-e9032d537f44",
  "sourceToolAssistantUUID": "c965dd66-c370-42de-9f49-70b6d8941472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-16T03:01:52.766Z_

Now I have a thorough understanding of the paper. Let me also check the experiment plan and provenance to understand the full scope.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "021f7e2a-ef5e-4193-8d3c-e9032d537f44",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7zt8hH2FvF7FMQvoj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9640087-16ea-4556-bfa3-d7437789e102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AaPZdN7RaxKwwwBX5b4c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5645,
      "cache_read_input_tokens": 40626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T03:01:54.280Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S9c6ZwjHhHxhTrsKQ63856`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_provenance.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9640087-16ea-4556-bfa3-d7437789e102",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W7zt8hH2FvF7FMQvoj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3afe360-4d88-4916-b87e-9bbe2defcad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AaPZdN7RaxKwwwBX5b4c7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5645,
      "cache_read_input_tokens": 40626,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 40626,
          "cache_creation_input_tokens": 5645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5645,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T03:01:54.286Z_

<details><summary>↩ Tool result · `toolu_01S9c6ZwjHhHxhTrsKQ63856`</summary>

```text
1	paper:
2	  title: ''
3	  version: 69
4	  generated_at: '2026-05-15T08:39:28.787717+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: method
9	    paragraph: 0
10	    sentence: 0
11	  text: Unconstrained greedy assigns 68 heads to 2-bit, PPL=32.45
12	  type: quantitative
13	  evidence:
14	  - oracle_comparison
15	  decisions: []
16	  deprecated: false
17	- id: C003
18	  location:
19	    section: method
20	    paragraph: 0
21	    sentence: 0
22	  text: Unconstrained MCKP assigns 75 heads to 2-bit, PPL=36.92
23	  type: quantitative
24	  evidence:
25	  - exp_b_hires_quant
26	  decisions: []
27	  deprecated: false
28	- id: C006
29	  location:
30	    section: method
31	    paragraph: 0
32	    sentence: 0
33	  text: Constrained greedy = constrained MCKP, PPL=11.23, bit dist {8/100/4}
34	  type: quantitative
35	  evidence:
36	  - greedy_cardinality_ablation
37	  decisions: []
38	  deprecated: false
39	- id: C010
40	  location:
41	    section: method
42	    paragraph: 0
43	    sentence: 0
44	  text: 'Compounding curve U-shaped: k=0 15.45, k=8 11.23 optimal, k=75 35.35'
45	  type: quantitative
46	  evidence:
47	  - compounding_sweep
48	  - compounding_sweep_k10_12
49	  decisions: []
50	  deprecated: false
51	- id: C015
52	  location:
53	    section: method
54	    paragraph: 0
55	    sentence: 0
56	  text: 'L0 distortion: L0H0 +31.9%, L0H2 +23.2%, L0H3 +11.7%'
57	  type: quantitative
58	  evidence:
59	  - p0_2_cliff_7B
60	  decisions: []
61	  deprecated: false
62	- id: C021
63	  location:
64	    section: method
65	    paragraph: 0
66	    sentence: 0
67	  text: 'Solver with/without L0 exclusion: 112/112 identical'
68	  type: quantitative
69	  evidence:
70	  - exp_d_no_l0_exclusion
71	  decisions: []
72	  deprecated: false
73	- id: C028
74	  location:
75	    section: method
76	    paragraph: 0
77	    sentence: 0
78	  text: 'Per-head verification: Qwen 112/112, Llama 256/256, Mistral 255/256'
79	  type: quantitative
80	  evidence:
81	  - greedy_cardinality_ablation
82	  decisions: []
83	  deprecated: false
84	- id: C029
85	  location:
86	    section: analysis
87	    paragraph: 0
88	    sentence: 0
89	  text: Qwen top-5% concentration 0.59-0.66
90	  type: quantitative
91	  evidence:
92	  - p0_2_cliff_7B
93	  decisions: []
94	  deprecated: false
95	- id: C031
96	  location:
97	    section: analysis
98	    paragraph: 0
99	    sentence: 0
100	  text: Constrained MCKP reduces degradation from +5.64 to +1.42, 27.3% improvement
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3afe360-4d88-4916-b87e-9bbe2defcad7",
  "isSidechain": true,
  "promptId": "95593d94-fcef-49a0-b391-f39b7aca900b",
  "agentId": "ae9b035990daf2b76",
  "type": "user",
  "uuid": "71aacf83-25d9-4248-b329-291c7795a492",
  "sourceToolAssistantUUID": "f3afe360-4d88-4916-b87e-9bbe2defcad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-16T03:03:32.689Z_

I now have sufficient material to write the review. Let me now produce the comprehensive review.

---

## Review: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"

**Reviewer 2 (R2) -- Focus: Novelty and Related Work**

---

### 1. Novelty Assessment

**Is the "systematic empirical study" framing sufficient for a top venue?**

There is precedent for negative-result and benchmark papers at top venues (e.g., "Are Sixteen Heads Really Better than One?" at NeurIPS 2019, various NeurIPS/ICML "Datasets and Benchmarks" track acceptances). However, those papers typically either (a) produce a reusable artifact (benchmark suite, dataset) or (b) overturn a widely-held assumption with overwhelming evidence across many settings. This paper's negative result -- that per-head mixed-precision KV cache quantization rarely helps -- is interesting but rests on a narrow empirical base: only one model out of nine benefits, and that model (Qwen2.5-7B) appears to be an outlier rather than a representative of a meaningful class. The finding is thus closer to "we tried something and it usually doesn't work" than to a paradigm-shifting negative result. The paper partially compensates by offering a diagnostic and a cardinality constraint, which elevates it beyond a pure negative-result paper.

**Is the sensitivity taxonomy (Spread/Spike/Flat) novel?**

The three-way categorization is a straightforward descriptive labeling of distribution shapes. Characterizing sensitivity distributions as concentrated-in-one-head (spike), spread-across-multiple-heads (spread), or uniform (flat) does not require deep technical insight -- it is essentially a verbal description of what one observes in the profiling data. The contribution lies more in the systematic documentation across architectures than in the taxonomy itself. As a conceptual contribution, it is modest.

**Is the two-metric diagnostic novel?**

The diagnostic (top-5% concentration >= 0.50 AND t1/t5 <= 0.70) is a decision rule calibrated on nine models with exactly one positive example. This is a threshold-based classifier with N=1 in the positive class -- a sample size that makes the thresholds essentially unfalsifiable within the paper's own data. Any two thresholds that separate one point from eight would work. The paper commendably acknowledges this (calling the thresholds "preliminary"), but it remains the case that the diagnostic's predictive power is undemonstrated on held-out data. Similar profiling-based decision rules exist in HAWQ (Hessian eigenvalue thresholds for layer sensitivity) and mixed-precision NAS literature, though not specifically for KV cache head-level decisions.

**Is the compounding characterization novel given RateQuant Appendix M?**

The paper acknowledges that compounding is a known phenomenon (RateQuant Appendix M). The claimed novelty is the systematic cross-architecture characterization and the cardinality constraint fix. However, the observation that aggressive low-bit quantization compounds nonlinearly is well-understood in the quantization literature broadly. The specific contribution is documenting the U-shaped curve and proposing k-capping, which is a useful but incremental engineering fix rather than a deep insight.

**Is the cardinality constraint a contribution or trivial regularization?**

Adding a constraint $\sum_h \mathbb{1}[b_h=2] \leq k$ to an MCKP formulation is a single linear inequality. It is the kind of fix any practitioner would try after observing that too many 2-bit heads cause problems. The paper argues it "directly addresses the identified failure mode" and is "not a heuristic patch," but it is exactly what it describes: a cap on the number of aggressive quantizations. The insight that the cap works is useful, but the technical novelty is minimal.

**Is solver equivalence surprising or expected?**

When k << H, the constrained problem collapses to "pick the best k heads for 2-bit," at which point greedy and exact optimization trivially agree (sort by marginal benefit, take top-k). The paper's own explanation makes this clear. This is not surprising to anyone familiar with combinatorial optimization; it is a direct consequence of the constraint reducing the problem to a simple ranking. Reporting it as a "finding" overstates its significance.

**Does reporting negative results constitute a contribution?**

Reporting that something does not work is valuable to the community, but only when (a) there was strong prior reason to believe it would work, or (b) the negative result is established with sufficient rigor to be definitive. Here, the paper shows that per-head mixed-precision on hardware-aligned bitwidths rarely helps, but the finding is conditional on symmetric per-channel quantization without per-token scaling. As the paper's own KIVI comparison shows, with asymmetric quantization the entire per-head allocation signal disappears (KIVI+MCKP = KIVI alone on Qwen). This suggests the negative result may be more about the quantization scheme than about per-head allocation in general, which weakens the generality of the finding.

### 2. Related Work Positioning

**Is the related work section adequate?**

The related work section has improved significantly from a typical first draft. It cites approximately 27 references and covers the major categories: uniform KV cache quantization, eviction methods, mixed-precision weights, and rate-distortion allocation. This is now a reasonably comprehensive treatment.

**Key gaps and positioning issues:**

- **No experimental comparison with any prior method at matched conditions.** The paper cites KIVI, KVQuant, GEAR, ZipCache, QServe, SKVQ, RotateKV, MiniKV, AquaKV, and others, but the only experimental comparison is a single paragraph on KIVI (Section 5.1) where KIVI+MCKP = KIVI alone. This is the most significant weakness. For a paper claiming to benchmark per-head allocation, the absence of experimental comparison against the methods it cites is a major gap. The Limitations section acknowledges "no existing tool performs per-head mixed-precision KV cache quantization on hardware-aligned bit-widths," but KVQuant uses sensitivity-weighted non-uniform quantization, and KVTuner/KVmix perform layer-level mixed-precision -- these could serve as baselines at their respective granularities.

- **RateQuant comparison.** The paper acknowledges that running RateQuant's greedy on {2,4,8,16} is unfair because it was designed for {2,...,6}. This honesty is appreciated, but it also raises the question: what would happen if RateQuant were run on its intended bit-width set? If the consecutive set avoids compounding (as the paper implies), then the practical question becomes whether hardware-aligned bitwidths matter enough to justify a separate paper. The paper implicitly argues they do (hardware efficiency), but does not benchmark the alternative.

- **KVTuner (ICML 2025) and KVmix.** Both perform layer-level mixed-precision KV cache quantization with sensitivity-based allocation. The paper cites them in the granularity appendix but does not experimentally compare. Since the paper argues per-head is superior to per-layer, a direct comparison would be the strongest evidence.

- **AquaKV (ICML 2025).** Cited but not compared experimentally. This method uses adapter-based prediction at very low bitwidths (2-2.5 bits), directly relevant to the compounding problem the paper identifies.

- **Missing broader context.** The quantization literature beyond KV cache (GPTQ, AWQ, QuIP/QuIP#, AQLM for weight quantization) is not discussed. While these target weights rather than activations, the mixed-precision allocation principles and compounding phenomena have been studied there. The paper would benefit from situating its compounding observation in this broader context.

**How does the work position against the broader quantization literature?**

The paper correctly identifies that KV cache quantization differs from weight quantization in that errors compound through the residual stream across layers. However, the claim that this compounding is "absent in weight quantization" (related work, paragraph 3) is debatable -- weight quantization errors also propagate through the network, though the dynamics differ. The positioning would be stronger with a more nuanced discussion of where KV cache compounding differs from known error accumulation effects in weight quantization.

### 3. Contribution Significance

**For a top venue (25% acceptance rate): do the contributions meet the bar?**

In my assessment, the contributions are below the acceptance threshold for a top ML venue. The core issue is that the paper's main finding is negative (8/9 models don't benefit), the one model that benefits is an outlier, and the proposed fixes (cardinality constraint, diagnostic) are technically straightforward. The paper is honest and well-executed within its scope, but the scope is narrow.

**What would elevate this paper to acceptance?**

1. **Experimental comparison with KVTuner, KVmix, and/or AquaKV** at matched compression ratios. This would establish whether per-head allocation provides value beyond existing approaches.
2. **Scaling to 70B+ models.** The paper acknowledges this was attempted and killed. Without it, the practical relevance is limited -- most practitioners deploying KV cache quantization are doing so for large models where memory is the binding constraint.
3. **More than N=1 in the positive class.** Finding additional models that exhibit the spread pattern would make the diagnostic meaningful rather than post-hoc.
4. **Integration with a real inference engine** (vLLM, TensorRT-LLM) to demonstrate practical latency/memory tradeoffs, rather than PyTorch-level simulation.
5. **A reusable benchmark or profiling toolkit** released as an artifact would increase the paper's long-term value.

**Is the negative-result framing executed well enough?**

The paper does a good job of being transparent about limitations (N=1 spread, killed 70B, KIVI subsumption). However, the negative result is weakened by the KIVI finding: if asymmetric quantization eliminates the per-head allocation signal, then the entire investigation is relevant only for symmetric-only deployment -- a niche that the paper acknowledges but does not quantify in terms of real-world prevalence.

### 4. Strengths and Weaknesses

**Strengths:**
- Unusually honest framing. The paper does not oversell its results and explicitly acknowledges N=1 spread, KIVI subsumption, and preliminary thresholds. This level of intellectual honesty is rare and commendable.
- Systematic cross-architecture evaluation across nine models (expanded from the initial five) covering diverse GQA ratios, attention mechanisms, and scales.
- The compounding characterization with U-shaped curves is clearly presented and practically useful. The cross-architecture compounding sweep (Figure 2) is the most informative visualization in the paper.
- The cardinality constraint is simple, effective, and solver-agnostic -- a clean engineering solution even if not technically deep.
- Good experimental hygiene: multi-seed stability (3 seeds on Qwen), cross-dataset validation, profiling resolution comparison, per-layer oracle validation.
- The within-family scale contrast (Qwen-7B spread vs. Qwen-14B flat) is a genuinely interesting observation.

**Weaknesses:**
- **N=1 positive result.** The entire technical contribution (cardinality constraint, diagnostic, taxonomy) is validated on a single model where it helps. The diagnostic is a classifier with 1 positive and 8 negative examples -- not meaningful from a statistical standpoint.
- **No experimental comparison with any published method** beyond KIVI (which subsumes the contribution). The related work section cites many methods that could serve as baselines but none are evaluated.
- **KIVI subsumption undermines the contribution.** The paper's own experiment shows KIVI+MCKP = KIVI alone on Qwen. If the most common deployment uses asymmetric quantization (which all modern inference engines support), per-head allocation adds no value. The paper's niche (symmetric-only environments) is not well-motivated.
- **Technical novelty is low.** The cardinality constraint is a single linear inequality. The taxonomy is descriptive. The solver equivalence is a direct consequence of the constraint simplifying the problem. None of these would be considered novel algorithmic contributions at a top venue.
- **Scale limitation.** 7B-14B models only (70B killed). The Qwen-7B/14B contrast suggests spread dilutes at scale, which would further narrow the applicability.
- **Diagnostic thresholds are arbitrary.** Concentration >= 0.50 and t1/t5 <= 0.70 are chosen to fit nine data points with one positive. Any pair of thresholds that separates one point from eight would achieve 9/9 accuracy. The paper acknowledges this but still presents it as a contribution.
- **Budget sweep only on Qwen.** The paper shows 2x/4x/8x only for the one model that benefits, providing no evidence about whether non-spread models might benefit at different compression ratios.
- **Downstream evaluation lacks CI for non-Qwen models.** Only Qwen has multi-seed results; other models are single-seed, making the small accuracy differences (e.g., Gemma-2 +0.2pp) impossible to assess for significance.

### 5. Questions for Authors

1. **KIVI subsumption.** You show that KIVI+MCKP = KIVI alone on Qwen. Can you characterize the set of deployment scenarios where per-channel asymmetric quantization is unavailable? How prevalent are "symmetric-only environments" in practice? If this niche is small, the paper's practical impact is correspondingly limited.

2. **RateQuant on its intended set.** What happens when RateQuant is run on consecutive bitwidths {2,3,4,5,6} on the same models? Does compounding still occur? If not, the implication is that hardware-aligned bitwidths are the problem, not per-head allocation -- and the solution might be to implement 3-bit and 5-bit support rather than to constrain 2-bit.

3. **Diagnostic on new data.** Have you tested the diagnostic on any model not in the training set of nine? With N=1 in the positive class, the thresholds are effectively post-hoc. Even one additional spread model (or a confirmed non-spread model with concentration > 0.50 and t1/t5 < 0.70) would significantly strengthen the claim.

4. **Layer-level baselines.** KVTuner and KVmix both perform layer-level mixed-precision at the same compression ratios you target. How does your per-head allocation compare? If layer-level achieves similar results with less profiling cost, the per-head granularity argument weakens.

5. **Compounding mechanism.** You attribute compounding to "truncation errors from multiple 2-bit heads accumulating through the residual stream." Have you measured this directly (e.g., tracking activation norms or attention pattern distortion layer by layer as k increases)? The current evidence is correlational (more 2-bit heads correlates with higher PPL) rather than mechanistic.

### 6. Score and Confidence

**Overall Score: 3 (Weak Reject)**

**Confidence: 4 (High)**

**One-line summary:** A well-executed and unusually honest empirical study of per-head KV cache quantization that documents an important negative result (8/9 models don't benefit) and proposes a simple cardinality constraint, but whose technical novelty is low, whose positive result rests on a single model, and whose practical relevance is undercut by the finding that asymmetric quantization subsumes the per-head allocation signal.

---

**Note to AC:** This paper is at the boundary between Weak Reject and Weak Accept. The honesty of the framing is genuinely refreshing and the experimental execution is solid within its scope. My concerns are primarily about (1) the N=1 positive result, (2) the lack of baselines against published methods, and (3) the KIVI subsumption finding, which the authors themselves report but which significantly narrows the paper's impact claim. If the authors can address Q1 (symmetric-only prevalence) and Q4 (layer-level comparison) convincingly, I would be willing to raise my score.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71aacf83-25d9-4248-b329-291c7795a492",
  "isSidechain": true,
  "agentId": "ae9b035990daf2b76",
  "requestId": "req_011Cb5W8K7kU5AZ4zbgtLqfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40643e16-bdbe-486d-a9e3-78d07683ae38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "ddcaedf0-2be6-465b-aa21-d4980723c0e4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kR1xMjG19h5KgRQp4oCFo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 46271,
      "output_tokens": 3853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3853,
          "cache_read_input_tokens": 46271,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1169,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
