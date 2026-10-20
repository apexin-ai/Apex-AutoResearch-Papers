# Research conversation: You are Reviewer 1 (R1) for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Rejec

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a30881bec0ec9c539.jsonl`
- **Structured JSON:** [`ee81b65a8f613152a961.json`](../../sessions/ee/ee81b65a8f613152a961.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

69 recorded events

### User

_source line 1 · 2026-05-16T02:53:48.362Z_

You are Reviewer 1 (R1) for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Methods and Experiments**.

## Paper Summary

Title: "Compounding Failures in Per-Head KV Cache Quantization: An Empirical Analysis of When Non-Uniform Allocation Helps"

The paper studies per-head mixed-precision KV cache quantization on hardware-aligned bit-widths {2,4,8,16}. Main findings:
1. 2-bit quantization distortions compound non-additively through the residual stream, causing unconstrained solvers (greedy, MCKP) to over-allocate 2-bit heads and underperform uniform 4-bit across 8 architectures (degradation 1.07×–3.31×).
2. A cardinality constraint (≤k heads at 2-bit, k≤8) prevents compounding and makes solver choice irrelevant (greedy=MCKP, Δ=0.0000).
3. Under 4× compression, only 1/8 architectures (Qwen2.5-7B) benefits from non-uniform allocation. A 2-metric diagnostic (9/9 correct) classifies when profiling is worthwhile.

## Paper Content (Key Sections)

### Method (Section 3)
- Problem: assign bit-width b_h ∈ {2,4,8,16} to each KV head h to minimize PPL subject to memory budget
- Per-head sensitivity profiling: measure distortion delta when one head is quantized while others stay at 16-bit. Uses WikiText-2 calibration. Two resolutions: low-res (16×512) and high-res (64×2048).
- MCKP formulation with cardinality constraint: ∑1[b_h=2] ≤ k
- k selected via small-scale compounding test; k≤8 yields <2.5% degradation across all tested architectures
- Applicability diagnostic: top-5% concentration ≳0.50 AND t1/t5 ≲0.70 → "spread" pattern → non-uniform recommended

### Experiments (Section 5)

**Table 2: Cross-architecture results (4× compression)**
- Qwen2.5-7B: BF16=9.81, Uniform=15.45, Constrained MCKP=10.91 (+27.3% vs uniform)
- Llama-3.1-8B: BF16=8.09, Uniform=8.47, Constrained MCKP=8.45 (+0.2%)
- Mistral-7B-v0.3: BF16=7.04, Uniform=7.13, Constrained MCKP=7.17 (−0.5%)

**Table 1: Compounding sweep (Qwen2.5-7B)**
k=0: PPL=9.81 (1.00×), k=8: 10.05 (1.02×), k=16: 10.42 (1.06×), k=32: 11.60 (1.18×), k=64: 23.22 (2.37×), k=112: 98.75 (10.07×)

**Table 3: Mistral k-ablation** — PPL monotonically increases with k; uniform is optimal

**Table 4: Solver equivalence** — Greedy unconstrained=32.45, MCKP unconstrained=36.92 (both FAIL); Greedy+max_2bit=8: 11.23, MCKP+max_2bit=8: 11.23 (identical, both PASS); Uniform=15.45

**Table 5: Oracle comparison** — MCKP optimal in 5/8 layer groups, max gap=0.014 PPL

**Table 6: Budget sweep (Qwen only)** — 2×: ~0% diff; 4×: 29.4%; 8×: 45.9× (MCKP=57.6 vs uniform=2643.77)

**Table 7: Profiling resolution** — Low-res PPL=11.23, High-res PPL=10.91, Uniform=15.45

**Table 8: L0 exclusion ablation** — Solver auto-discovers L0 sensitivity (identical PPL with/without exclusion)

**Table 9: K/V separation** — Worse than joint (+0.31 PPL) due to K-cache compounding

**Table 10: Heuristic baselines** — MCKP beats L0-random by 5.2% (Qwen), 15.8% (Llama), 5.7% (Mistral)

**Table 11: Cross-dataset calibration** — >96% agreement across 3 architectures (Qwen 96.4%, Llama 97.7%, Mistral 96.5%)

**Table 12: Multi-seed stability** — PPL mean=10.99±0.065 (3 seeds), bit distribution identical

**Table 13: Downstream evaluation (5 architectures)** — Only Qwen shows positive gains (+2.60pp avg). Yi: −0.77pp, Llama: −0.99pp, Mistral: −0.48pp, Gemma-2: +0.14pp. ARC-Challenge shows systematic degradation across non-Spread models.

**Table 14: Runtime** — MCKP throughput 21.8 vs uniform 23.6 tok/s (−8.5% overhead)

### Limitations (stated by authors)
- Only 7B-14B scale (72B attempt killed)
- Multi-seed CI for PPL but not all downstream tasks
- 8.5% throughput overhead
- Diagnostic thresholds from n=9 models

## Experiment Design Reference (from review context)

The following experiments were planned. Check coverage:
1. L0 Exclusion Removal Ablation — covered (Table 8), Qwen-only
2. Llama-3.1-8B Full Pipeline — covered (Table 2)
3. Mistral-7B Full Pipeline — covered (Tables 2, 3)
4. Compounding Sweep — covered (Table 1), Qwen-only in main paper
5. Budget Sweep — covered (Table 6), Qwen-only
6. High-Resolution Profiling — covered (Table 7), Qwen-only
7. C4 Cross-Dataset — covered (Table 11), 3 architectures
8. RateQuant Greedy Comparison — covered (Table 4)
9. Oracle Comparison — covered (Table 5), Qwen-only, only 4 layer groups
10. Cross-Domain Calibration — merged with #7
11. Head Sensitivity Visualization — paper mentions heatmap in abstract area but unclear if multi-architecture visualization included
12. K/V Separation — covered (Table 9), Qwen-only
13. Downstream Task Evaluation — covered (Table 13), 5 architectures but missing some entries for Mistral/Gemma-2
14. 70B Profiling — killed, acknowledged in limitations
15. L0-Only Heuristic — covered (Table 10), 3 architectures
16. Solver Equivalence — covered (Table 4)
17. Multi-Seed Error Bars — covered (Table 12), Qwen-only PPL, no downstream CI
18. Runtime Benchmark — covered (Table 14), Qwen-only

## Your Review Task

Evaluate the paper on:
1. **Methodological soundness**: Is the MCKP + cardinality constraint formulation rigorous? Is the profiling methodology sound? Is the diagnostic well-motivated?
2. **Experimental thoroughness**: Are experiments sufficient to support claims? What's missing?
3. **Statistical rigor**: Are claims backed by proper error bars, confidence intervals, multiple seeds?
4. **Reproducibility**: Is there enough detail to reproduce?
5. **Claim-evidence alignment**: Do the claims match what the evidence actually shows?

Produce your review in this format:
```
## R1 Review: Methods and Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, be specific with table/section references]

### Weaknesses
[Numbered list, be specific. Label each as Major or Minor]

### Questions for Authors
[Numbered list]

### Missing Experiments / Evidence Gaps
[What experiments from the design are missing or incomplete in the paper?]

### Claim-Evidence Alignment Issues
[Where do claims overreach the evidence?]

### Overall Assessment
Score: X/6
Confidence: X/5
[2-3 sentence justification]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "9f2c6d60-aea1-48a3-a3ae-2e73d69a0e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T02:53:48.368Z_

```json
{
  "parentUuid": "9f2c6d60-aea1-48a3-a3ae-2e73d69a0e7e",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
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
  "uuid": "bbb6cdca-3fb9-4a52-b606-6e231bacfc22",
  "timestamp": "2026-05-16T02:53:48.368Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-16T02:53:52.823Z_



I'll conduct a thorough review by examining the paper's method, experiments, and key source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbb6cdca-3fb9-4a52-b606-6e231bacfc22",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWVPNtzg4dqwz1usEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19d6c1b5-d0e6-45d2-b55d-2d954a362f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzEvuqgiBUdBC3rzqn1oWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-16T02:53:53.745Z_

<details open><summary>🔧 Tool call — Read · `toolu_019BxRqF8net4gHAbA3U85GV`</summary>

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
  "parentUuid": "19d6c1b5-d0e6-45d2-b55d-2d954a362f00",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWVPNtzg4dqwz1usEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09beb5ce-d53c-42a9-97bb-f2f5d7180764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzEvuqgiBUdBC3rzqn1oWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-16T02:53:53.757Z_

<details><summary>↩ Tool result · `toolu_019BxRqF8net4gHAbA3U85GV`</summary>

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
  "parentUuid": "09beb5ce-d53c-42a9-97bb-f2f5d7180764",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "d1ef121a-2cb8-4f3e-925a-fd70bfabcd76",
  "sourceToolAssistantUUID": "09beb5ce-d53c-42a9-97bb-f2f5d7180764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T02:53:54.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qm7c1FWeFiNY1FDvaZkErM`</summary>

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
  "parentUuid": "d1ef121a-2cb8-4f3e-925a-fd70bfabcd76",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWVPNtzg4dqwz1usEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b65c909-34b5-4890-8bf6-d2bd7abcfc7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzEvuqgiBUdBC3rzqn1oWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 7 · 2026-05-16T02:53:54.747Z_

<details><summary>↩ Tool result · `toolu_01Qm7c1FWeFiNY1FDvaZkErM`</summary>

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
  "parentUuid": "7b65c909-34b5-4890-8bf6-d2bd7abcfc7b",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "040c6f06-2e21-419c-a36c-959e8b0176bb",
  "sourceToolAssistantUUID": "7b65c909-34b5-4890-8bf6-d2bd7abcfc7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T02:53:54.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_011wWzWgsp2864N9XU3AHkuN`</summary>

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
  "parentUuid": "040c6f06-2e21-419c-a36c-959e8b0176bb",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWVPNtzg4dqwz1usEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b2e21fe-6f20-4241-8f21-4d3a70f7723c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzEvuqgiBUdBC3rzqn1oWk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17297,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 9 · 2026-05-16T02:53:54.820Z_

<details><summary>↩ Tool result · `toolu_011wWzWgsp2864N9XU3AHkuN`</summary>

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
  "parentUuid": "2b2e21fe-6f20-4241-8f21-4d3a70f7723c",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "3f2494e9-8269-4426-88b4-f1dd39f734b2",
  "sourceToolAssistantUUID": "2b2e21fe-6f20-4241-8f21-4d3a70f7723c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T02:54:00.249Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BziTw7X1L6EgxJWzSx2aFx`</summary>

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
  "parentUuid": "3f2494e9-8269-4426-88b4-f1dd39f734b2",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWyBTv9jUaTE6gZ62z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "117f97f6-995f-4152-bb80-62e2a0ffb001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpmASPLYg5KMweXb7CSuGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10919,
      "cache_read_input_tokens": 17297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10919,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 11 · 2026-05-16T02:54:00.259Z_

<details><summary>↩ Tool result · `toolu_01BziTw7X1L6EgxJWzSx2aFx`</summary>

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
  "parentUuid": "117f97f6-995f-4152-bb80-62e2a0ffb001",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "efd6b43a-3cfd-44e1-9d48-639e9cd66a34",
  "sourceToolAssistantUUID": "117f97f6-995f-4152-bb80-62e2a0ffb001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:54:00.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mit7Y51Zr8GBGPoK3Lpaxx`</summary>

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
  "parentUuid": "efd6b43a-3cfd-44e1-9d48-639e9cd66a34",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWyBTv9jUaTE6gZ62z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a00cf052-fbdd-4606-af91-c3a958d2ea98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpmASPLYg5KMweXb7CSuGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10919,
      "cache_read_input_tokens": 17297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10919,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 13 · 2026-05-16T02:54:00.620Z_

<details><summary>↩ Tool result · `toolu_01Mit7Y51Zr8GBGPoK3Lpaxx`</summary>

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
  "parentUuid": "a00cf052-fbdd-4606-af91-c3a958d2ea98",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "4a31c73d-2f97-41ed-9057-e565879eb6d0",
  "sourceToolAssistantUUID": "a00cf052-fbdd-4606-af91-c3a958d2ea98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T02:54:01.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_0176XYm68TdbynUGt26gbXgm`</summary>

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
  "parentUuid": "4a31c73d-2f97-41ed-9057-e565879eb6d0",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VWyBTv9jUaTE6gZ62z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfb2b8c7-3be0-4de0-a1ed-425fd5d698f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpmASPLYg5KMweXb7CSuGB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10919,
      "cache_read_input_tokens": 17297,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 17297,
          "cache_creation_input_tokens": 10919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10919,
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

_source line 15 · 2026-05-16T02:54:01.138Z_

<details><summary>↩ Tool result · `toolu_0176XYm68TdbynUGt26gbXgm`</summary>

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
  "parentUuid": "cfb2b8c7-3be0-4de0-a1ed-425fd5d698f3",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "dcf98b5d-476f-4b15-9f01-0d08c286ad34",
  "sourceToolAssistantUUID": "cfb2b8c7-3be0-4de0-a1ed-425fd5d698f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T02:54:06.086Z_

Now let me examine the experiment scripts and artifacts to check reproducibility and completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcf98b5d-476f-4b15-9f01-0d08c286ad34",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXTHegsLJF6rUo2MAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1940bea2-546a-41f6-bd0f-9f7b886f52cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AirnbKWGex3gRAzcza5FxP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
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

_source line 17 · 2026-05-16T02:54:07.527Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011tRPZtt8TFU5g2aLnrursb`</summary>

```json
{
  "pattern": "**/artifacts/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1940bea2-546a-41f6-bd0f-9f7b886f52cf",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXTHegsLJF6rUo2MAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "511a7bdb-5cd0-4c03-97b3-bcba78642aa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AirnbKWGex3gRAzcza5FxP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
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

_source line 18 · 2026-05-16T02:54:07.661Z_

<details><summary>↩ Tool result · `toolu_011tRPZtt8TFU5g2aLnrursb`</summary>

```text
artifacts/dream_reports/dream_20260514T002109/best/experiment_data.json
artifacts/dream_reports/dream_20260514T002109/median/experiment_data.json
artifacts/dream_reports/dream_20260514T002109/worst/experiment_data.json
artifacts/mistral_k_ablation/data/mistral_k_ablation_results.json
artifacts/llama_k_ablation/data/llama_k_ablation_results.json
artifacts/_project/data/shape_metrics.json
artifacts/shape_metrics.json
artifacts/w2_unconstrained_baselines/data/w2_unconstrained_baselines_results.json
artifacts/w9_compounding_scaling_results.json
artifacts/w9_compounding_scaling/data/w9_compounding_scaling_results.json
artifacts/w2_unconstrained_baselines_results.json
artifacts/w2_unconstrained_v2/data/w2_unconstrained_v2_results.json
artifacts/w3_downstream_eval/data/w3_downstream_yi_results.json
artifacts/w3_downstream_yi_results.json
artifacts/w3_downstream_eval/data/w3_downstream_llama_results.json
artifacts/w3_downstream_llama_results.json
artifacts/w2_unconstrained_v2/data/w2_gemma2_bos_fix_results.json
artifacts/w2_gemma2_bos_fix_results.json
artifacts/w3_downstream_mistral_results.json
artifacts/w3_downstream_eval/data/w3_downstream_mistral_results.json
artifacts/w3_downstream_gemma2_results.json
artifacts/w3_downstream_eval/data/w3_downstream_gemma2_results.json
artifacts/w2_unconstrained_v2_results.json
artifacts/gemma2_constrained_bos_fix_results.json
artifacts/dream_reports/dream_20260515T085855/best/experiment_data.json
artifacts/dream_reports/dream_20260515T085855/median/experiment_data.json
artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json
artifacts/qwen7b_8k_context_eval/data/qwen7b_8k_spotcheck_results.json
artifacts/kivi_baseline_qwen7b_v2/data/kivi_baseline_qwen7b_v2_results.json
artifacts/kivi_mckp_combined_qwen7b/data/kivi_mckp_combined_results.json
artifacts/kivi_mckp_combined_results.json
artifacts/qwen14b_greedy_constrained/data/qwen14b_greedy_constrained_results.json
artifacts/qwen14b_greedy_constrained_results.json
artifacts/_project/data/compounding_curves_data.json
artifacts/compounding_curves_data.json
artifacts/dream_reports/dream_20260516T021448/best/experiment_data.json
artifacts/dream_reports/dream_20260516T021448/median/experiment_data.json
artifacts/dream_reports/dream_20260516T021448/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "511a7bdb-5cd0-4c03-97b3-bcba78642aa2",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "92592f0b-b666-42c1-aa49-e698d2c4fb9b",
  "sourceToolAssistantUUID": "511a7bdb-5cd0-4c03-97b3-bcba78642aa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:54:08.494Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ACBW35pSSLbMWbqFHUpN9B`</summary>

```json
{
  "pattern": "**/artifacts/**/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92592f0b-b666-42c1-aa49-e698d2c4fb9b",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXTHegsLJF6rUo2MAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b26e0e6-be01-4918-8329-370ed6dd05ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AirnbKWGex3gRAzcza5FxP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 28216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5297,
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

_source line 20 · 2026-05-16T02:54:08.533Z_

<details><summary>↩ Tool result · `toolu_01ACBW35pSSLbMWbqFHUpN9B`</summary>

```text
artifacts/compounding_sweep/data/compounding_sweep_results.csv
artifacts/budget_sweep/data/budget_sweep_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b26e0e6-be01-4918-8329-370ed6dd05ec",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "143d3677-80f6-40a6-a961-6e6c49da2ccc",
  "sourceToolAssistantUUID": "3b26e0e6-be01-4918-8329-370ed6dd05ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:54:08.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AoNrfLqVKhaxQZ9smL2Jyu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "143d3677-80f6-40a6-a961-6e6c49da2ccc",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXTHegsLJF6rUo2MAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81d1bfa4-2baa-4bf7-b64d-bf315486704d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AirnbKWGex3gRAzcza5FxP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5297,
      "cache_read_input_tokens": 28216,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 28216,
          "cache_creation_input_tokens": 5297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5297,
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

_source line 22 · 2026-05-16T02:54:08.783Z_

<details><summary>↩ Tool result · `toolu_01AoNrfLqVKhaxQZ9smL2Jyu`</summary>

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
101	  type: quantitative
102	  evidence:
103	  - budget_sweep
104	  decisions: []
105	  deprecated: false
106	- id: C034
107	  location:
108	    section: analysis
109	    paragraph: 0
110	    sentence: 0
111	  text: 'Llama benefit marginal: +0.36 vs +0.38'
112	  type: quantitative
113	  evidence:
114	  - llama_full_pipeline
115	  decisions: []
116	  deprecated: false
117	- id: C038
118	  location:
119	    section: analysis
120	    paragraph: 0
121	    sentence: 0
122	  text: 'Mistral MCKP worse than uniform: +0.13 vs +0.10'
123	  type: quantitative
124	  evidence:
125	  - mistral_k_ablation
126	  decisions: []
127	  deprecated: false
128	- id: C043
129	  location:
130	    section: analysis
131	    paragraph: 0
132	    sentence: 0
133	  text: 'Llama 5.3x: MCKP 57.60 vs uniform 2643.77'
134	  type: quantitative
135	  evidence:
136	  - llama_aggressive_compression
137	  decisions: []
138	  deprecated: false
139	- id: C049
140	  location:
141	    section: analysis
142	    paragraph: 0
143	    sentence: 0
144	  text: 'Mistral 5.3x: 11.91 vs 519.11'
145	  type: quantitative
146	  evidence:
147	  - mistral_aggressive_compression
148	  decisions: []
149	  deprecated: false
150	- id: C056
151	  location:
152	    section: analysis
153	    paragraph: 0
154	    sentence: 0
155	  text: Hires improves MCKP from 11.23 to 10.91
156	  type: quantitative
157	  evidence:
158	  - hires_mckp_reeval
159	  decisions: []
160	  deprecated: false
161	- id: C064
162	  location:
163	    section: analysis
164	    paragraph: 0
165	    sentence: 0
166	  text: Standard detects 37/112, hires 100/112 heads
167	  type: quantitative
168	  evidence:
169	  - exp_e_hires_profile
170	  decisions: []
171	  deprecated: false
172	- id: C073
173	  location:
174	    section: analysis
175	    paragraph: 0
176	    sentence: 0
177	  text: 8/112 assignments change with hires
178	  type: quantitative
179	  evidence:
180	  - exp_e_hires_profile
181	  decisions: []
182	  deprecated: false
183	- id: C083
184	  location:
185	    section: analysis
186	    paragraph: 0
187	    sentence: 0
188	  text: 'KV separation: joint 10.91 vs separated 11.22 (+0.31)'
189	  type: quantitative
190	  evidence:
191	  - kv_separation
192	  decisions: []
193	  deprecated: false
194	- id: C094
195	  location:
196	    section: analysis
197	    paragraph: 0
198	    sentence: 0
199	  text: 21/112 heads show K!=V asymmetry
200	  type: quantitative
201	  evidence:
202	  - kv_separation
203	  decisions: []
204	  deprecated: false
205	- id: C095
206	  location:
207	    section: introduction
208	    paragraph: 0
209	    sentence: 0
210	  text: Unconstrained greedy 32.45 PPL, MCKP 36.92, uniform 15.45 on Qwen at 4x
211	  type: quantitative
212	  evidence:
213	  - ratequant_greedy_comparison
214	  - exp_b_hires_quant
215	  decisions: []
216	  deprecated: false
217	- id: C097
218	  location:
219	    section: introduction
220	    paragraph: 0
221	    sentence: 0
222	  text: Solvers assign 68-75 of 112 heads to 2-bit
223	  type: quantitative
224	  evidence:
225	  - ratequant_greedy_comparison
226	  decisions: []
227	  deprecated: false
228	- id: C100
229	  location:
230	    section: introduction
231	    paragraph: 0
232	    sentence: 0
233	  text: Constrained k=8 yields 11.23 PPL, 27.3% reduction
234	  type: quantitative
235	  evidence:
236	  - budget_sweep
237	  decisions: []
238	  deprecated: false
239	- id: C104
240	  location:
241	    section: introduction
242	    paragraph: 0
243	    sentence: 0
244	  text: 'Solver equivalence: 112/112 Qwen, 256/256 Llama, 255/256 Mistral'
245	  type: quantitative
246	  evidence:
247	  - greedy_cardinality_ablation
248	  decisions: []
249	  deprecated: false
250	- id: C109
251	  location:
252	    section: introduction
253	    paragraph: 0
254	    sentence: 0
255	  text: Llama 8.45 vs 8.47 marginal 0.2%
256	  type: quantitative
257	  evidence:
258	  - llama_hires_pipeline
259	  decisions: []
260	  deprecated: false
261	- id: C115
262	  location:
263	    section: introduction
264	    paragraph: 0
265	    sentence: 0
266	  text: Mistral 7.16 vs 7.13 slightly worse
267	  type: quantitative
268	  evidence:
269	  - mistral_k_ablation
270	  decisions: []
271	  deprecated: false
272	- id: C122
273	  location:
274	    section: introduction
275	    paragraph: 0
276	    sentence: 0
277	  text: 'Heterogeneity diagnostic: Qwen 0.61, Llama 0.57, Mistral 0.22'
278	  type: quantitative
279	  evidence:
280	  - qwen_hires_float32_d048
281	  - llama_hires_bf16_2bitonly
282	  - mistral_hires_pipeline
283	  decisions: []
284	  deprecated: false
285	- id: C123
286	  location:
287	    section: related_work
288	    paragraph: 0
289	    sentence: 0
290	  text: RateQuant proves greedy optimality on consecutive integers {2,...,6} via polymatroid
291	    structure
292	  type: prior_work
293	  evidence:
294	  - zuo2026ratequant Proposition 6
295	  decisions: []
296	  deprecated: true
297	- id: C125
298	  location:
299	    section: related_work
300	    paragraph: 0
301	    sentence: 0
302	  text: Hardware-aligned {2,4,8,16} breaks polymatroid structure
303	  type: analytical
304	  evidence:
305	  - method.tex Sec 3.1
306	  decisions: []
307	  deprecated: true
308	- id: C128
309	  location:
310	    section: related_work
311	    paragraph: 0
312	    sentence: 0
313	  text: Eviction and quantization are complementary, not competing
314	  type: positioning
315	  evidence: []
316	  decisions: []
317	  deprecated: true
318	- id: C132
319	  location:
320	    section: related_work
321	    paragraph: 0
322	    sentence: 0
323	  text: Head importance/pruning is a different phenomenon from quantization sensitivity
324	    heterogeneity
325	  type: positioning
326	  evidence:
327	  - experiments in Sec 5
328	  decisions: []
329	  deprecated: true
330	- id: C137
331	  location:
332	    section: related_work
333	    paragraph: 0
334	    sentence: 0
335	  text: Voita et al. 2019 and Michel et al. 2019 are not in bib
336	  type: citation_gap
337	  evidence: []
338	  decisions:
339	  - Used UNVERIFIED placeholder as instructed
340	  deprecated: true
341	- id: C138
342	  location:
343	    section: abstract
344	    paragraph: 0
345	    sentence: 0
346	  text: Unconstrained greedy 32.45, MCKP 36.92, uniform 15.45
347	  type: quantitative
348	  evidence:
349	  - ratequant_greedy_comparison
350	  - exp_b_hires_quant
351	  decisions: []
352	  deprecated: false
353	- id: C140
354	  location:
355	    section: abstract
356	    paragraph: 0
357	    sentence: 0
358	  text: Constrained 11.23, 27.3% reduction
359	  type: quantitative
360	  evidence:
361	  - budget_sweep
362	  decisions: []
363	  deprecated: false
364	- id: C143
365	  location:
366	    section: abstract
367	    paragraph: 0
368	    sentence: 0
369	  text: Solver equivalence Delta=0.0000 across 3 architectures
370	  type: quantitative
371	  evidence:
372	  - greedy_cardinality_ablation
373	  decisions: []
374	  deprecated: false
375	- id: C147
376	  location:
377	    section: abstract
378	    paragraph: 0
379	    sentence: 0
380	  text: Llama 8.45 vs 8.47 marginal
381	  type: quantitative
382	  evidence:
383	  - llama_hires_pipeline
384	  decisions: []
385	  deprecated: false
386	- id: C152
387	  location:
388	    section: abstract
389	    paragraph: 0
390	    sentence: 0
391	  text: Mistral 7.16 vs 7.13 counterproductive
392	  type: quantitative
393	  evidence:
394	  - mistral_k_ablation
395	  decisions: []
396	  deprecated: false
397	- id: C153
398	  location:
399	    section: conclusion
400	    paragraph: 0
401	    sentence: 0
402	  text: Constrained 11.23 vs uniform 15.45, 27.3% improvement
403	  type: quantitative
404	  evidence:
405	  - budget_sweep
406	  decisions: []
407	  deprecated: false
408	- id: C155
409	  location:
410	    section: conclusion
411	    paragraph: 0
412	    sentence: 0
413	  text: Solver equivalence Delta=0.0000 across 3 architectures
414	  type: quantitative
415	  evidence:
416	  - greedy_cardinality_ablation
417	  decisions: []
418	  deprecated: false
419	- id: C158
420	  location:
421	    section: conclusion
422	    paragraph: 0
423	    sentence: 0
424	  text: Qwen concentration 0.61, Llama 0.57 (8.45 vs 8.47), Mistral 0.22 (7.16 vs
425	    7.13)
426	  type: quantitative
427	  evidence:
428	  - qwen_hires_float32_d048
429	  - llama_hires_pipeline
430	  - mistral_hires_pipeline
431	  decisions: []
432	  deprecated: false
433	- id: C159
434	  location:
435	    section: experiments
436	    paragraph: 0
437	    sentence: 0
438	  text: ''
439	  type: quantitative
440	  evidence:
441	  - c4_rerun_d032
442	  decisions: []
443	  deprecated: false
444	- id: C160
445	  location:
446	    section: experiments
447	    paragraph: 0
448	    sentence: 0
449	  text: Mistral heuristic baselines use budget 0.256 vs MCKP 0.248 (3% more memory),
450	    yet still underperform MCKP
451	  type: quantitative
452	  evidence:
453	  - heuristic_mistral_k4
454	  decisions: []
455	  deprecated: false
456	- id: C161
457	  location:
458	    section: experiments
459	    paragraph: 0
460	    sentence: 0
461	  text: 'Llama cross-dataset: 97.7% agreement (250/256), but 253/256 forced 4-bit
462	    by k=2; C4-cal MCKP 0.18 PPL worse than uniform'
463	  type: quantitative
464	  evidence:
465	  - llama_c4_cross_dataset
466	  decisions: []
467	  deprecated: false
468	- id: C162
469	  location:
470	    section: experiments
471	    paragraph: 0
472	    sentence: 0
473	  text: 'Mistral cross-dataset: 96.5% agreement (247/256); MCKP worse than uniform
474	    in both directions (delta=-0.03 to -0.05)'
475	  type: quantitative
476	  evidence:
477	  - mistral_c4_cross_dataset
478	  decisions: []
479	  deprecated: false
480	- id: C163
481	  location:
482	    section: experiments
483	    paragraph: 0
484	    sentence: 0
485	  text: All three models >96% bit-assignment agreement across C4/WT2 calibration
486	  type: quantitative
487	  evidence:
488	  - c4_rerun_plan010
489	  - llama_c4_cross_dataset
490	  - mistral_c4_cross_dataset
491	  decisions: []
492	  deprecated: false
493	- id: C164
494	  location:
495	    section: experiments
496	    paragraph: 0
497	    sentence: 0
498	  text: Gemma-2 constrained MCKP 6.17 PPL vs uniform 6.15 (BOS-corrected)
499	  type: quantitative
500	  evidence:
501	  - gemma2_hires_constrained_mckp
502	  decisions: []
503	  deprecated: false
504	- id: C165
505	  location:
506	    section: experiments
507	    paragraph: 0
508	    sentence: 0
509	  text: Gemma-2 unconstrained MCKP degrades to 8.85 PPL (1.47x bf16)
510	  type: quantitative
511	  evidence:
512	  - gemma2_unconstrained_mckp
513	  decisions: []
514	  deprecated: false
515	- id: C166
516	  location:
517	    section: experiments
518	    paragraph: 0
519	    sentence: 0
520	  text: Gemma-2 solver assigns 31.5% heads to 2-bit under unconstrained
521	  type: quantitative
522	  evidence:
523	  - gemma2_unconstrained_mckp
524	  decisions: []
525	  deprecated: false
526	- id: C167
527	  location:
528	    section: experiments
529	    paragraph: 0
530	    sentence: 0
531	  text: 'Unconstrained failure gradient: 3.3x (Qwen) -> 1.47x (Gemma-2) -> ~1.07-1.08x
532	    (Yi/Llama/Mistral)'
533	  type: quantitative
534	  evidence:
535	  - w2_unconstrained_baselines
536	  decisions: []
537	  deprecated: false
538	- id: C168
539	  location:
540	    section: experiments
541	    paragraph: 0
542	    sentence: 0
543	  text: Yi-1.5 downstream avg delta -0.5 pts vs uniform
544	  type: quantitative
545	  evidence:
546	  - yi_mistral_downstream_k2
547	  decisions: []
548	  deprecated: false
549	- id: C169
550	  location:
551	    section: experiments
552	    paragraph: 0
553	    sentence: 0
554	  text: Llama downstream avg delta -0.1 pts vs uniform
555	  type: quantitative
556	  evidence:
557	  - llama_downstream_eval
558	  decisions: []
559	  deprecated: false
560	- id: C170
561	  location:
562	    section: experiments
563	    paragraph: 0
564	    sentence: 0
565	  text: Mistral downstream avg delta +0.0 pts
566	  type: quantitative
567	  evidence:
568	  - yi_mistral_downstream_k2
569	  decisions: []
570	  deprecated: false
571	- id: C171
572	  location:
573	    section: experiments
574	    paragraph: 0
575	    sentence: 0
576	  text: Gemma-2 downstream avg delta +0.2 pts (4-task mean of displayed values)
577	  type: quantitative
578	  evidence:
579	  - w3_downstream_eval
580	  decisions: []
581	  deprecated: false
582	- id: C172
583	  location:
584	    section: experiments
585	    paragraph: 0
586	    sentence: 0
587	  text: 'ARC-C most sensitive: Yi -2.1 pts, Llama -0.8 pts'
588	  type: quantitative
589	  evidence:
590	  - yi_mistral_downstream_k2
591	  - llama_downstream_eval
592	  decisions: []
593	  deprecated: false
594	- id: C173
595	  location:
596	    section: method
597	    paragraph: 0
598	    sentence: 0
599	  text: 'Super-additive compounding: 1.56x at k=8, 4.89x at k=64'
600	  type: quantitative
601	  evidence:
602	  - w9_compounding_scaling
603	  decisions: []
604	  deprecated: false
605	- id: C174
606	  location:
607	    section: method
608	    paragraph: 0
609	    sentence: 0
610	  text: 'Random-k control: k=64 random=55.94 vs top-k=22.95'
611	  type: quantitative
612	  evidence:
613	  - w9_compounding_scaling
614	  decisions: []
615	  deprecated: false
616	tables: []
617	figures: []
618	_completeness:
619	  coverage: 49/49
620	  claims: 49
621	  tables: 0
622	  figures: 0
623	  tier_counts:
624	    tier1: 0
625	    tier2: 49
626	    tier3: 0
627	    tierX: 0
628	  last_checked: '2026-05-15T08:39:28.787755+00:00'
629	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81d1bfa4-2baa-4bf7-b64d-bf315486704d",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "d91f4430-99ef-44b3-93bf-508d0d9d5ab2",
  "sourceToolAssistantUUID": "81d1bfa4-2baa-4bf7-b64d-bf315486704d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T02:54:16.160Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019w5UhghynTYHeKzrvU8QLA`</summary>

```json
{
  "pattern": "multi.seed|three.seed|3 seeds|error bar|confidence interval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d91f4430-99ef-44b3-93bf-508d0d9d5ab2",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXzvfi7XVVETGBk4Tc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b4cd8eb-5c15-4820-9bc4-392a3299a5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGcS9cin45xUk2ZryFb6ru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7463,
      "cache_read_input_tokens": 33513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 24 · 2026-05-16T02:54:16.181Z_

<details><summary>↩ Tool result · `toolu_019w5UhghynTYHeKzrvU8QLA`</summary>

```text
docs/paper/experiments.tex:134:On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
docs/paper/conclusion.tex:21:Downstream evaluation covers four 0-shot classification tasks (ARC-C, HellaSwag, PIQA, WinoGrande). For HellaSwag, we report raw accuracy (\texttt{acc}) rather than length-normalized accuracy (\texttt{acc\_norm}). Generation tasks (summarization, translation, long-form QA) are not evaluated, and no confidence intervals are reported for the current single-seed results.
docs/paper/appendix.tex:122:\paragraph{Multi-seed stability.}
docs/paper/main.aux:1279:\@writefile{toc}{\contentsline {paragraph}{Multi-seed stability.}{13}{section*.35}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b4cd8eb-5c15-4820-9bc4-392a3299a5d6",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "87480b37-0c69-45a4-8151-16bbf2a8a8c1",
  "sourceToolAssistantUUID": "6b4cd8eb-5c15-4820-9bc4-392a3299a5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T02:54:17.252Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Udfncr46EUhHDcbCY7JeSy`</summary>

```json
{
  "pattern": "long.context|8k|8K|context length",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87480b37-0c69-45a4-8151-16bbf2a8a8c1",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VXzvfi7XVVETGBk4Tc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e871d38-329d-418a-ba7a-d5a85c27d7aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGcS9cin45xUk2ZryFb6ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7463,
      "cache_read_input_tokens": 33513,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 33513,
          "cache_creation_input_tokens": 7463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7463,
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

_source line 26 · 2026-05-16T02:54:17.308Z_

<details><summary>↩ Tool result · `toolu_01Udfncr46EUhHDcbCY7JeSy`</summary>

```text
docs/paper/experiments.tex:137:Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
docs/paper/main.bbl:70:  million context length {LLM} inference with {KV} cache quantization}.
docs/paper/main.bbl:94:  long-context inference in {LLMs}}.
docs/paper/main.bbl:127:\newblock \href {https://arxiv.org/abs/2405.04532} {{QServe}: {W4A8KV4}
docs/paper/main.bbl:168:  long context inference}.
docs/paper/main.bbl:231:  mixed-precision {KV} cache quantization for long-context reasoning}.
docs/paper/conclusion.tex:26:\paragraph{Long-context.}
docs/paper/conclusion.tex:27:Long-context evaluation extends only to 8K tokens; deployment scenarios at 32K--128K context lengths are not tested.
docs/paper/appendix.tex:182:\section{Long-Context Generalization}
docs/paper/appendix.tex:183:\label{sec:long_context}
docs/paper/appendix.tex:188:\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
docs/paper/appendix.tex:189:\label{tab:long_context}
docs/paper/appendix.tex:192:Model & Method & 2K PPL & 8K PPL \\
docs/paper/appendix.tex:205:Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
docs/paper/appendix.tex:206:On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
docs/paper/appendix.tex:207:Constrained MCKP remains robust ($1.11\times$ at 2K, $1.23\times$ at 8K), recovering 97.7\% of the quantization loss at 8K vs.\ 80.8\% at 2K.
docs/paper/appendix.tex:208:On Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\ 6.04), consistent with the 2K result.
docs/paper/appendix.tex:209:The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
docs/paper/appendix.tex:210:Profiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.
docs/paper/references.bib:12:  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
docs/paper/references.bib:20:  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
docs/paper/references.bib:114:  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
docs/paper/references.bib:134:  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
docs/paper/references.bib:224:  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},
docs/paper/main.aux:949:\@writefile{toc}{\contentsline {paragraph}{Long-context.}{10}{section*.27}\protected@file@percent }
docs/paper/main.aux:1388:\@writefile{toc}{\contentsline {section}{\numberline {L}Long-Context Generalization}{14}{appendix.L}\protected@file@percent }
docs/paper/main.aux:1389:\newlabel{sec:long_context}{{L}{14}{Long-Context Generalization}{appendix.L}{}}
docs/paper/main.aux:1390:\@writefile{lot}{\contentsline {table}{\numberline {8}{\ignorespaces PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096).}}{14}{table.caption.40}\protected@file@percent }
docs/paper/main.aux:1391:\newlabel{tab:long_context}{{8}{14}{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096)}{table.caption.40}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e871d38-329d-418a-ba7a-d5a85c27d7aa",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "00c97475-1e30-45ce-ad12-86610a1d8411",
  "sourceToolAssistantUUID": "6e871d38-329d-418a-ba7a-d5a85c27d7aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:54:22.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_016BD4aJ62jA297joYQaFxfd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c97475-1e30-45ce-ad12-86610a1d8411",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VYdLAwvcH3qyQTDUCu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22a9d457-385f-418c-bdb4-eacfd93cd110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcKbWK33APKNWGiawdZeKG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1971,
      "cache_read_input_tokens": 40976,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1971
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 40976,
          "cache_creation_input_tokens": 1971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1971,
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

_source line 28 · 2026-05-16T02:54:22.247Z_

<details><summary>↩ Tool result · `toolu_016BD4aJ62jA297joYQaFxfd`</summary>

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
  "parentUuid": "22a9d457-385f-418c-bdb4-eacfd93cd110",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "15806b95-8962-4685-a0f3-63df305294ac",
  "sourceToolAssistantUUID": "22a9d457-385f-418c-bdb4-eacfd93cd110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-16T02:54:27.363Z_

Now let me look at the experiment scripts to assess reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15806b95-8962-4685-a0f3-63df305294ac",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VYzTfepi9s4LUQvx4d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9d955b6-2432-45ee-8aeb-18e609d8978e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMHVY7nAxZxX6nZCrMYfgR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5648,
      "cache_read_input_tokens": 42947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5648,
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

_source line 30 · 2026-05-16T02:54:29.260Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q8WzAwoGeHjiMHKvb1bctm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_qwen_hires_constrained.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d955b6-2432-45ee-8aeb-18e609d8978e",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VYzTfepi9s4LUQvx4d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b21f864e-3dee-415a-963a-6864a27007fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMHVY7nAxZxX6nZCrMYfgR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5648,
      "cache_read_input_tokens": 42947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5648,
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

_source line 31 · 2026-05-16T02:54:29.266Z_

<details><summary>↩ Tool result · `toolu_01Q8WzAwoGeHjiMHKvb1bctm`</summary>

```text
1	"""Qwen2.5-7B Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data."""
2	import os
3	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
4	os.environ["HF_DATASETS_OFFLINE"] = "1"
5	
6	import json
7	import time
8	import torch
9	from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
10	from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
11	from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
12	
13	
14	def main():
15	    device = "cuda:0"
16	    model_name = "Qwen/Qwen2.5-7B"
17	    profiles_path = "hires_profiles.json"
18	    output_path = "qwen_hires_constrained_results.json"
19	    budget = 0.25
20	    max_2bit = 8
21	    t0 = time.time()
22	
23	    config = AutoConfig.from_pretrained(model_name)
24	    num_layers = config.num_hidden_layers
25	    num_kv_heads = config.num_key_value_heads
26	    num_q_heads = config.num_attention_heads
27	    gqa_ratio = num_q_heads // num_kv_heads
28	    total_kv_heads = num_layers * num_kv_heads
29	    print(f"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
30	
31	    # Load D048 float32 hires profiling data
32	    print(f"\nLoading profiles from {profiles_path}...")
33	    with open(profiles_path) as f:
34	        raw = json.load(f)
35	    profiles_raw = raw["profiles"] if "profiles" in raw else raw
36	    print(f"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer")
37	
38	    profiles = enforce_monotonicity(profiles_raw)
39	
40	    # Constrained MCKP
41	    print(f"\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
42	    mckp_result = solve_mckp_constrained(
43	        profiles, budget, mode="quant_only",
44	        max_2bit=max_2bit, l0_exclude_2bit=True)
45	
46	    bit_counts = {}
47	    for key, (atype, param) in mckp_result["allocation"].items():
48	        b = int(param) if atype == "quant" else 16
49	        bit_counts[b] = bit_counts.get(b, 0) + 1
50	    print(f"Bit distribution: {bit_counts}")
51	    print(f"Total distortion: {mckp_result['total_distortion']:.6f}")
52	    print(f"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}")
53	
54	    # Load model for eval
55	    print(f"\nLoading model in bf16 to {device}...")
56	    tokenizer = AutoTokenizer.from_pretrained(model_name)
57	    model = AutoModelForCausalLM.from_pretrained(
58	        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
59	    )
60	    model = model.to(device)
61	    model.eval()
62	    mem_gb = torch.cuda.memory_allocated(device) / 1e9
63	    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")
64	
65	    # BF16 baseline WikiText-2
66	    print("\nEvaluating bf16 baseline on WikiText-2...")
67	    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
68	    print(f"BF16 WikiText-2 PPL: {baseline_wt2:.4f}")
69	
70	    # MCKP eval
71	    print("\nEvaluating constrained MCKP allocation on WikiText-2...")
72	    orig_fwds = patch_attention(model, mckp_result["allocation"])
73	    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
74	    restore_attention(model, orig_fwds)
75	    print(f"MCKP PPL: {mckp_wt2:.4f}")
76	
77	    # Uniform 4-bit eval
78	    print("\nEvaluating uniform 4-bit on WikiText-2...")
79	    uniform_result = uniform_quantization_baseline(profiles, bits=4)
80	    orig_fwds = patch_attention(model, uniform_result["allocation"])
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b21f864e-3dee-415a-963a-6864a27007fe",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "25d87236-9672-47d7-b9a1-1a955c894ba0",
  "sourceToolAssistantUUID": "b21f864e-3dee-415a-963a-6864a27007fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T02:54:29.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_01138FKnwWvvyw844BcUkxJX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_kivi_baseline.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d87236-9672-47d7-b9a1-1a955c894ba0",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VYzTfepi9s4LUQvx4d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c9ac267-a4fb-41b9-b0b1-0b652b32b33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMHVY7nAxZxX6nZCrMYfgR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5648,
      "cache_read_input_tokens": 42947,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 42947,
          "cache_creation_input_tokens": 5648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5648,
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

_source line 33 · 2026-05-16T02:54:29.831Z_

<details><summary>↩ Tool result · `toolu_01138FKnwWvvyw844BcUkxJX`</summary>

```text
1	"""KIVI baseline PPL evaluation on WikiText-2.
2	
3	Re-implements KIVI's per-channel asymmetric KV cache quantization
4	for compatibility with transformers 4.57+ and all model architectures.
5	
6	KIVI scheme:
7	  K: asymmetric min-max quantization per channel (head_dim), grouped along token dim
8	  V: asymmetric min-max quantization per token, grouped along head_dim
9	  Last `residual_length` tokens kept in fp16.
10	
11	Reference: https://github.com/jy-yuan/KIVI
12	"""
13	
14	import argparse
15	import importlib
16	import json
17	import math
18	import torch
19	import torch.nn.functional as F
20	from transformers import AutoModelForCausalLM, AutoTokenizer
21	
22	
23	def kivi_quantize_k(k, bits, group_size):
24	    """Asymmetric per-channel quantization for K cache (KIVI scheme).
25	
26	    K shape: (B, nh, T, D)
27	    Groups along T (token dim) with group_size.
28	    For each (B, nh, *, D) group of group_size tokens, compute min/max.
29	    """
30	    B, nh, T, D = k.shape
31	    if T == 0:
32	        return k
33	    max_int = 2 ** bits - 1
34	    pad = (group_size - T % group_size) % group_size
35	    if pad > 0:
36	        k = F.pad(k, (0, 0, 0, pad))
37	    T_padded = k.shape[2]
38	    k = k.reshape(B, nh, T_padded // group_size, group_size, D)
39	    mn = k.min(dim=3, keepdim=True)[0]
40	    mx = k.max(dim=3, keepdim=True)[0]
41	    scale = ((mx - mn) / max_int).clamp(min=1e-10)
42	    k = ((k - mn) / scale).clamp(0, max_int).round() * scale + mn
43	    k = k.reshape(B, nh, T_padded, D)
44	    if pad > 0:
45	        k = k[:, :, :T_padded - pad, :]
46	    return k
47	
48	
49	def kivi_quantize_v(v, bits, group_size):
50	    """Asymmetric per-token quantization for V cache (KIVI scheme).
51	
52	    V shape: (B, nh, T, D)
53	    Groups along D (head_dim) with group_size.
54	    For each (B, nh, T, *) group of group_size channels, compute min/max.
55	    """
56	    B, nh, T, D = v.shape
57	    if T == 0:
58	        return v
59	    max_int = 2 ** bits - 1
60	    pad = (group_size - D % group_size) % group_size
61	    if pad > 0:
62	        v = F.pad(v, (0, pad))
63	    D_padded = v.shape[3]
64	    v = v.reshape(B, nh, T, D_padded // group_size, group_size)
65	    mn = v.min(dim=4, keepdim=True)[0]
66	    mx = v.max(dim=4, keepdim=True)[0]
67	    scale = ((mx - mn) / max_int).clamp(min=1e-10)
68	    v = ((v - mn) / scale).clamp(0, max_int).round() * scale + mn
69	    v = v.reshape(B, nh, T, D_padded)
70	    if pad > 0:
71	        v = v[:, :, :, :D_padded - pad]
72	    return v
73	
74	
75	def _get_rotary_fn(model):
76	    model_type = model.config.model_type
77	    module_name = f"transformers.models.{model_type}.modeling_{model_type}"
78	    module = importlib.import_module(module_name)
79	    return module.apply_rotary_pos_emb
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c9ac267-a4fb-41b9-b0b1-0b652b32b33c",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "9c01876a-3958-4acf-9d6d-c06b378917ab",
  "sourceToolAssistantUUID": "5c9ac267-a4fb-41b9-b0b1-0b652b32b33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T02:54:34.729Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HLYLjzDZxqinoPC5Nzxtr4`</summary>

```json
{
  "pattern": "**/solver.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c01876a-3958-4acf-9d6d-c06b378917ab",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VZYqphQ19ZCJT1LeDZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "811f014d-641c-4494-b4c0-1e0af05d4342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3xEYEX2jQvVJtv3qaLo2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 48595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 35 · 2026-05-16T02:54:34.749Z_

<details><summary>↩ Tool result · `toolu_01HLYLjzDZxqinoPC5Nzxtr4`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "811f014d-641c-4494-b4c0-1e0af05d4342",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "88d6c3c7-2822-4f0b-be0f-b11b59cdc7eb",
  "sourceToolAssistantUUID": "811f014d-641c-4494-b4c0-1e0af05d4342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T02:54:35.299Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013GsFXijrGoNtuUF8hgbFes`</summary>

```json
{
  "pattern": "**/eval_ppl.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d6c3c7-2822-4f0b-be0f-b11b59cdc7eb",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VZYqphQ19ZCJT1LeDZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e4f822c-329e-4e10-b7a3-3e98a81c5fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3xEYEX2jQvVJtv3qaLo2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 48595,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 48595,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2771,
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

_source line 37 · 2026-05-16T02:54:35.326Z_

<details><summary>↩ Tool result · `toolu_013GsFXijrGoNtuUF8hgbFes`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e4f822c-329e-4e10-b7a3-3e98a81c5fbf",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "86cb6fd6-a69b-439e-b9fe-bc6879e1e3c3",
  "sourceToolAssistantUUID": "6e4f822c-329e-4e10-b7a3-3e98a81c5fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T02:54:40.603Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01D7qwPGq2uvERqXgbTGqwcA`</summary>

```json
{
  "pattern": "from solver|from eval_ppl|import solver|import eval_ppl",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86cb6fd6-a69b-439e-b9fe-bc6879e1e3c3",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VZxGyUbEcZtKz5vNUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e70de63-13f2-4a22-ba87-253f917784c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHZh5EfmqNZ7qBUAP5MyyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 51366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 247,
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

_source line 39 · 2026-05-16T02:54:40.719Z_

<details><summary>↩ Tool result · `toolu_01D7qwPGq2uvERqXgbTGqwcA`</summary>

```text
&lt;persisted-output>
Output too large (30.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809/tool-results/toolu_01D7qwPGq2uvERqXgbTGqwcA.txt

Preview (first 2KB):
run_llama_8k_eval.py:21:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_llama_8k_eval.py:22:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_phi3_longcontext_8k.py:17:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_phi3_longcontext_8k.py:18:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
experiment_plan.yaml:5:  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.
run_yi_longcontext_8k.py:16:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_yi_longcontext_8k.py:17:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_llama_hires_bf16_2bitonly.py:15:from eval_ppl import patch_attention, restore_attention
run_yi15_full_pipeline.py:17:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_yi15_full_pipeline.py:18:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_mistral_8k_eval.py:21:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_mistral_8k_eval.py:22:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_llama8b_8k_eval.py:27:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_llama8b_8k_eval.py:28:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_w3_downstream_eval.py:21:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
run_w3_downstream_eval.py:22:from eval_ppl import patch_attention, restore_attention
run_qwen_longcontext_8k.py:16:from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
run_qwen_longcontext_8k.py:17:from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e70de63-13f2-4a22-ba87-253f917784c5",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "0fc33414-a671-48d5-9bf6-e5a73183a005",
  "sourceToolAssistantUUID": "2e70de63-13f2-4a22-ba87-253f917784c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T02:54:41.243Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ErH51WexwKb1htBZG86riy`</summary>

```json
{
  "pattern": "requirements\\.txt|pyproject\\.toml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fc33414-a671-48d5-9bf6-e5a73183a005",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VZxGyUbEcZtKz5vNUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e43cfbf-8f66-4986-9183-67f17edfd12a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHZh5EfmqNZ7qBUAP5MyyT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 51366,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 51366,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 247,
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

_source line 41 · 2026-05-16T02:54:41.338Z_

<details><summary>↩ Tool result · `toolu_01ErH51WexwKb1htBZG86riy`</summary>

```text
Found 13 files
AGENTS.md
.claude/CLAUDE.md
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_reviewer_20260515T225409_281572.jsonl
logs/chats/worker_ssh_spread_candidate_model_check_20260515T220524.jsonl
logs/workers/worker_ssh_spread_candidate_model_check_20260515T220524.log
logs/workers/worker_ops_disk_cleanup_westd_20260515T163311.log
logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_director.jsonl
logs/chats/archive/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_20260515T125712_172749.jsonl
logs/workers/worker_code_kivi_baseline_prep_20260515T110703.log
logs/workers/worker_util_disk_cleanup_scan_20260514T134956.log
logs/workers/worker_transfer_scp_figures_to_local_20260514T074635.log
logs/chats/worker_transfer_pdf_figures_v2_20260514T073538.jsonl
logs/workers/worker_transfer_pdf_figures_v2_20260514T073538.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e43cfbf-8f66-4986-9183-67f17edfd12a",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "37301c42-4df7-478c-8b16-31e94de9644c",
  "sourceToolAssistantUUID": "3e43cfbf-8f66-4986-9183-67f17edfd12a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T02:54:47.460Z_

The `solver.py` and `eval_ppl.py` files are referenced in the scripts but not present in the local repository (likely deployed only on the compute server). Let me check if there's any information about them in checkpoints or documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37301c42-4df7-478c-8b16-31e94de9644c",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VaPpsts71NQZQQLSP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b491b539-867b-4762-b138-f5ca9d271084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twe8P24w5FSVLVtPFrnkqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 51613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1548,
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

_source line 43 · 2026-05-16T02:54:47.884Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XyNhNHQpj7VZbF6pFx7bvH`</summary>

```json
{
  "pattern": "**/checkpoints/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b491b539-867b-4762-b138-f5ca9d271084",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VaPpsts71NQZQQLSP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a79fe14d-18da-4479-afd4-c27588d86645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twe8P24w5FSVLVtPFrnkqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 51613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1548,
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

_source line 44 · 2026-05-16T02:54:47.909Z_

<details><summary>↩ Tool result · `toolu_01XyNhNHQpj7VZbF6pFx7bvH`</summary>

```text
checkpoints/mvp_001_PREPARING_20260513T173141.json
checkpoints/mvp_001_PENDING_20260513T190131.json
checkpoints/mvp_001_QUEUED_20260513T190134.json
checkpoints/mvp_001_ALLOCATED_20260513T190138.json
checkpoints/mvp_001_RUNNING_20260513T190207.json
checkpoints/sanity_001_PREPARING_20260513T194717.json
checkpoints/sanity_001_PENDING_20260513T194722.json
checkpoints/sanity_001_QUEUED_20260513T194727.json
checkpoints/sanity_001_ALLOCATED_20260513T194730.json
checkpoints/sanity_001_RUNNING_20260513T194820.json
checkpoints/mvp_001_RUNNING_20260513T194947.json
checkpoints/sanity_001_RUNNING_20260513T194948.json
checkpoints/mvp_002_PREPARING_20260513T195852.json
checkpoints/sanity_002_PREPARING_20260513T195852.json
checkpoints/mvp_002_PENDING_20260513T195902.json
checkpoints/sanity_002_PENDING_20260513T195902.json
checkpoints/mvp_002_QUEUED_20260513T195905.json
checkpoints/sanity_002_QUEUED_20260513T195906.json
checkpoints/mvp_002_ALLOCATED_20260513T195910.json
checkpoints/sanity_002_ALLOCATED_20260513T195911.json
checkpoints/mvp_002_RUNNING_20260513T195929.json
checkpoints/sanity_002_RUNNING_20260513T195931.json
checkpoints/mvp_002_RUNNING_20260513T203317.json
checkpoints/sanity_002_RUNNING_20260513T203320.json
checkpoints/mvp_003_PREPARING_20260513T205603.json
checkpoints/sanity_003_PREPARING_20260513T205603.json
checkpoints/mvp_003_PENDING_20260513T205611.json
checkpoints/sanity_003_PENDING_20260513T205611.json
checkpoints/mvp_003_QUEUED_20260513T205616.json
checkpoints/sanity_003_QUEUED_20260513T205616.json
checkpoints/mvp_003_ALLOCATED_20260513T205622.json
checkpoints/sanity_003_ALLOCATED_20260513T205622.json
checkpoints/mvp_003_RUNNING_20260513T205641.json
checkpoints/sanity_003_RUNNING_20260513T205643.json
checkpoints/mvp_003_RUNNING_20260513T213102.json
checkpoints/sanity_003_RUNNING_20260513T213103.json
checkpoints/mvp_001_DONE_20260513T213525.json
checkpoints/mvp_002_DONE_20260513T213525.json
checkpoints/mvp_003_DONE_20260513T213526.json
checkpoints/sanity_001_DONE_20260513T213527.json
checkpoints/sanity_002_DONE_20260513T213528.json
checkpoints/sanity_003_DONE_20260513T213528.json
checkpoints/sanity_004_QUEUED_20260513T215110.json
checkpoints/sanity_004_ALLOCATED_20260513T215124.json
checkpoints/sanity_004_RUNNING_20260513T215128.json
checkpoints/sanity_004_RUNNING_20260513T215148.json
checkpoints/sanity_004_DONE_20260513T215238.json
checkpoints/mvp_004_QUEUED_20260513T215513.json
checkpoints/mvp_004_ALLOCATED_20260513T215516.json
checkpoints/mvp_004_RUNNING_20260513T221547.json
checkpoints/mvp_004_RUNNING_20260513T221550.json
checkpoints/mvp_004_DONE_20260513T221601.json
checkpoints/p0_2_cliff_1.5B_QUEUED_20260513T222400.json
checkpoints/p0_2_cliff_1.5B_ALLOCATED_20260513T222403.json
checkpoints/p0_2_cliff_1.5B_RUNNING_20260513T222410.json
checkpoints/p0_2_cliff_1.5B_RUNNING_20260513T222413.json
checkpoints/p0_2_cliff_1.5B_DONE_20260513T222422.json
checkpoints/p0_2_cliff_7B_QUEUED_20260513T222437.json
checkpoints/p0_2_cliff_7B_ALLOCATED_20260513T222440.json
checkpoints/p0_1_ppl_fast_QUEUED_20260513T222517.json
checkpoints/p0_1_ppl_fast_ALLOCATED_20260513T222523.json
checkpoints/p0_1_ppl_fast_RUNNING_20260513T222640.json
checkpoints/p0_2_cliff_7B_RUNNING_20260513T222642.json
checkpoints/p0_1_ppl_fast_RUNNING_20260513T231843.json
checkpoints/p0_1_ppl_fast_DONE_20260513T231900.json
checkpoints/p0_2_cliff_7B_RUNNING_20260513T231900.json
checkpoints/p0_2_cliff_7B_DONE_20260513T231911.json
checkpoints/exp_a_targeted_hybrid_QUEUED_20260513T232911.json
checkpoints/exp_a_targeted_hybrid_ALLOCATED_20260513T232914.json
checkpoints/exp_a_targeted_hybrid_RUNNING_20260513T232920.json
checkpoints/exp_a_targeted_hybrid_RUNNING_20260513T232924.json
checkpoints/exp_a_targeted_hybrid_DONE_20260513T232936.json
checkpoints/exp_b_hires_quant_PREPARING_20260513T235431.json
checkpoints/exp_b_hires_quant_QUEUED_20260513T235501.json
checkpoints/exp_b_hires_quant_ALLOCATED_20260513T235504.json
checkpoints/exp_b_hires_quant_RUNNING_20260513T235510.json
checkpoints/exp_b_hires_quant_DONE_20260513T235515.json
checkpoints/exp_c_constrained_mckp_PREPARING_20260514T000149.json
checkpoints/exp_c_constrained_mckp_QUEUED_20260514T001413.json
checkpoints/exp_c_constrained_mckp_RUNNING_20260514T001423.json
checkpoints/exp_c_constrained_mckp_RUNNING_20260514T001433.json
checkpoints/exp_c_constrained_mckp_DONE_20260514T001436.json
checkpoints/exp_c_no2bit_PREPARING_20260514T001607.json
checkpoints/exp_c_no2bit_QUEUED_20260514T001910.json
checkpoints/exp_c_no2bit_RUNNING_20260514T001921.json
checkpoints/exp_d_no_l0_exclusion_PREPARING_20260514T002054.json
checkpoints/exp_e_hires_profile_PREPARING_20260514T002058.json
checkpoints/exp_c_no2bit_RUNNING_20260514T002233.json
checkpoints/exp_c_no2bit_DONE_20260514T002240.json
checkpoints/exp_d_no_l0_exclusion_PENDING_20260514T002511.json
checkpoints/exp_d_no_l0_exclusion_PENDING_20260514T002522.json
checkpoints/exp_d_no_l0_exclusion_DONE_20260514T002529.json
checkpoints/compounding_sweep_PREPARING_20260514T002718.json
checkpoints/exp_e_hires_profile_QUEUED_20260514T003505.json
checkpoints/exp_e_hires_profile_RUNNING_20260514T003509.json
checkpoints/compounding_sweep_PENDING_20260514T004220.json
checkpoints/compounding_sweep_PENDING_20260514T004231.json
checkpoints/compounding_sweep_DONE_20260514T004235.json
checkpoints/compounding_sweep_k10_12_PREPARING_20260514T004917.json
checkpoints/ratequant_greedy_comparison_PREPARING_20260514T004920.json
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a79fe14d-18da-4479-afd4-c27588d86645",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "2ab70785-0c24-4c86-a0c1-6b53ac4bbfe9",
  "sourceToolAssistantUUID": "a79fe14d-18da-4479-afd4-c27588d86645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T02:54:48.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_015jb98WUFXFxMeH2Jk4K6Yz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab70785-0c24-4c86-a0c1-6b53ac4bbfe9",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VaPpsts71NQZQQLSP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd9903c0-ba64-4f23-8018-4e1743b80717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twe8P24w5FSVLVtPFrnkqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 51613,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 51613,
          "cache_creation_input_tokens": 1548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1548,
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

_source line 46 · 2026-05-16T02:54:48.598Z_

<details><summary>↩ Tool result · `toolu_015jb98WUFXFxMeH2Jk4K6Yz`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim:
4	  - 2
5	  description: 'Remove L0 exclusion constraint from solver, keep only max_2bit=8.
6	    Verify solver still assigns 8-bit to Layer 0 heads purely from profiling data.
7	    Strengthens narrative: "solver automatically discovers sensitivity structure."
8	
9	    '
10	  priority: P0
11	  gpu_budget_hours: 1
12	  deps: []
13	  registry_id: exp_d_no_l0_exclusion
14	  model: Qwen2.5-7B
15	  eval: WikiText-2
16	- id: plan_002
17	  claim:
18	  - 1
19	  - 2
20	  description: 'Replicate full pipeline on Llama-3.1-8B (GQA ratio 4:1 vs Qwen 7:1).
21	    Profile all KV heads, run constrained MCKP, evaluate PPL. Tests generalizability
22	    across different GQA ratios and architectures. Fallback if HF token unavailable:
23	    Yi-1.5-9B (non-gated, similar scale).
24	
25	    '
26	  priority: P0
27	  gpu_budget_hours: 4
28	  deps: []
29	  registry_id: llama_full_pipeline
30	  model: Llama-3.1-8B
31	  fallback_model: Yi-1.5-9B
32	  eval: WikiText-2
33	- id: plan_003
34	  claim:
35	  - 1
36	  - 2
37	  description: 'Replicate full pipeline on Mistral-7B-v0.3. Different architecture
38	    family to establish cross-architecture validity.
39	
40	    '
41	  priority: P0
42	  gpu_budget_hours: 4
43	  deps: []
44	  registry_id: mistral_full_pipeline
45	  model: Mistral-7B-v0.3
46	  eval: WikiText-2
47	- id: plan_004
48	  claim:
49	  - 3
50	  description: 'Compounding effect characterization: sweep max_2bit from 0 to 112
51	    (steps: 0, 4, 8, 16, 24, 48, 75, 112) on Qwen2.5-7B. Plot PPL vs max_2bit to map
52	    the compounding threshold. Establishes the principled basis for cardinality constraint
53	    selection.
54	
55	    '
56	  priority: P0
57	  gpu_budget_hours: 3
58	  deps: []
59	  registry_id: compounding_sweep
60	  model: Qwen2.5-7B
61	  eval: WikiText-2
62	- id: plan_005
63	  claim:
64	  - 2
65	  description: 'Budget sweep: test constrained MCKP at compression ratios 2×, 4×,
66	    8× (budget = 0.5, 0.25, 0.125) on Qwen2.5-7B. Compare each against uniform baseline
67	    at same budget.
68	
69	    '
70	  priority: P0
71	  gpu_budget_hours: 3
72	  deps: []
73	  registry_id: budget_sweep
74	  model: Qwen2.5-7B
75	  eval: WikiText-2
76	- id: plan_006
77	  claim:
78	  - 1
79	  - 2
80	  description: 'High-resolution profiling: 64 seq × 2048 tokens (vs current 16×512).
81	    Rerun MCKP with hires profiles on Qwen2.5-7B. Tests whether better profiling discovers
82	    mid-layer heterogeneity and improves solver allocation beyond current results.
83	
84	    '
85	  priority: P0
86	  gpu_budget_hours: 3
87	  deps: []
88	  registry_id: exp_e_hires_profile
89	  model: Qwen2.5-7B
90	  eval: WikiText-2
91	- id: plan_007
92	  claim:
93	  - 1
94	  - 2
95	  - 3
96	  description: 'Evaluate on C4 perplexity (in addition to WikiText-2) for Qwen2.5-7B.
97	    Cross-dataset evaluation to show results are not WikiText-2 specific.
98	
99	    '
100	  priority: P0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd9903c0-ba64-4f23-8018-4e1743b80717",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "a25a2600-6cd3-44e8-86d7-81983a5fbe21",
  "sourceToolAssistantUUID": "fd9903c0-ba64-4f23-8018-4e1743b80717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-16T02:54:54.645Z_

Now let me check the provenance for potential number inconsistencies between the provenance file and the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25a2600-6cd3-44e8-86d7-81983a5fbe21",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vaw3LjTfdmsG5ZkjPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9026736e-a5bf-467c-85c0-5946dce5d3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyVTLPXCVS1HeTicL7EorR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3768,
      "cache_read_input_tokens": 53161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3768,
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

_source line 48 · 2026-05-16T02:54:56.001Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JpAaDkmVifFfNf4wbCZcRa`</summary>

```json
{
  "pattern": "10\\.91|11\\.23|27\\.3|29\\.4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9026736e-a5bf-467c-85c0-5946dce5d3b6",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vaw3LjTfdmsG5ZkjPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85440fab-64c4-4a64-8dc3-4e9fb8e98976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyVTLPXCVS1HeTicL7EorR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3768,
      "cache_read_input_tokens": 53161,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 53161,
          "cache_creation_input_tokens": 3768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3768,
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

_source line 49 · 2026-05-16T02:54:56.036Z_

<details><summary>↩ Tool result · `toolu_01JpAaDkmVifFfNf4wbCZcRa`</summary>

```text
docs/paper/analysis.tex:15:Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
docs/paper/analysis.tex:68:\item \textbf{Spread} (concentration $\geq 0.50$ \emph{and} $t_1/t_5 \leq 0.70$): non-uniform recommended. Qwen-7B (0.61, $t_1/t_5{=}0.57$): $-$29.4\% PPL.
docs/paper/related_work.tex:24:Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.
docs/paper/experiments.tex:53:Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
docs/paper/experiments.tex:65:On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
docs/paper/experiments.tex:88:Within the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).
docs/paper/conclusion.tex:4:On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
docs/paper/method.tex:71:This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (10.91 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
docs/paper/method.tex:88:Greedy & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
docs/paper/method.tex:89:MCKP & $k{\leq}8$ & 10.91 & 8 & 100 & 4 \\
docs/paper/method.tex:96:With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (10.91), same bit distribution on Qwen2.5-7B.
docs/paper/abstract.tex:2:The sole exception is Qwen2.5-7B, where a cardinality-constrained solver achieves 10.91 perplexity at $4\times$ compression---a 29.4\% reduction over uniform 4-bit (15.45)---while unconstrained solvers degrade catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
docs/paper/appendix.tex:26:Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
docs/paper/appendix.tex:33:On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL.
docs/paper/appendix.tex:63:\emph{Per-head} allocation (ours) exposes this heterogeneity to the solver and yields a 29.4\% PPL improvement on Qwen, at the cost of $H$ profiling passes; the cardinality constraint developed in \S\ref{sec:cardinality} renders the choice of solver irrelevant, amortizing the search overhead.
docs/paper/appendix.tex:81:4$\times$ & 15.45 & 11.23 & $+$4.22 \\
docs/paper/appendix.tex:89:At 4$\times$, constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement; hires profiling further reduces this to 10.91 (Appendix~\ref{sec:profiling_resolution}).
docs/paper/appendix.tex:96:On Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
docs/paper/appendix.tex:115:High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
docs/paper/appendix.tex:129:Float32 profiling (64 $\times$ 2048 tokens) yields an identical constrained allocation and PPL within seed variance (10.89 vs.\ 10.91, $\Delta = 0.02 < \sigma = 0.06$), confirming that bfloat16 precision is sufficient for the profiling step.
docs/paper/appendix.tex:142:Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
docs/paper/introduction.tex:21:On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 10.91 PPL---a 29.4\% reduction over uniform 4-bit.
docs/paper/introduction.tex:40:\item We identify 2-bit distortion compounding as a major contributing factor in the degradation observed under unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a single cardinality constraint on 2-bit assignments suffices to prevent it, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85440fab-64c4-4a64-8dc3-4e9fb8e98976",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "4faaa0a2-a2de-4df9-a876-d5b55016aefb",
  "sourceToolAssistantUUID": "85440fab-64c4-4a64-8dc3-4e9fb8e98976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-16T02:55:01.577Z_

I notice an interesting inconsistency: the paper uses both 11.23 (standard-resolution) and 10.91 (high-resolution) throughout. The provenance file (C006, C010, C100, C140, C153) refers to 11.23 while the main claims in the final paper body use 10.91. Let me check the Table 4 footnote more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4faaa0a2-a2de-4df9-a876-d5b55016aefb",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VbUt1cg5gG9X59jBRG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf8e57a6-2939-4ca3-ab47-5c62ac50c4af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AM38nTq6CpqEhyvqCxYmpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 51 · 2026-05-16T02:55:02.972Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BGD47wSsxjBb1bfq855eLo`</summary>

```json
{
  "pattern": "footnote|high.res|standard.res|low.res",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf8e57a6-2939-4ca3-ab47-5c62ac50c4af",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VbUt1cg5gG9X59jBRG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "397fea46-388f-41d9-9620-135d218ef048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AM38nTq6CpqEhyvqCxYmpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 56929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 52 · 2026-05-16T02:55:02.991Z_

<details><summary>↩ Tool result · `toolu_01BGD47wSsxjBb1bfq855eLo`</summary>

```text
79:\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
94:\footnotetext{Constrained results use high-resolution profiling; unconstrained rows use standard-resolution profiling to illustrate the failure mode (the exact PPL is irrelevant---any unconstrained allocation fails catastrophically).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "397fea46-388f-41d9-9620-135d218ef048",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "e104b041-57ca-49cd-9cf2-0ba2c4818ea1",
  "sourceToolAssistantUUID": "397fea46-388f-41d9-9620-135d218ef048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T02:55:03.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_011tD8VHA85G7KR5GFPZJrpU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": 110,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e104b041-57ca-49cd-9cf2-0ba2c4818ea1",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VbUt1cg5gG9X59jBRG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30a7ece1-a13d-4a54-8fb0-1d6f9eb1ac06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AM38nTq6CpqEhyvqCxYmpu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 56929,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 56929,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1917,
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

_source line 54 · 2026-05-16T02:55:03.668Z_

<details><summary>↩ Tool result · `toolu_011tD8VHA85G7KR5GFPZJrpU`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a7ece1-a13d-4a54-8fb0-1d6f9eb1ac06",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "5840e68c-b00b-4aaf-a197-c4e9cbe423b8",
  "sourceToolAssistantUUID": "30a7ece1-a13d-4a54-8fb0-1d6f9eb1ac06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-16T02:55:09.697Z_

Now let me check the downstream evaluation more carefully -- the review context mentions Table 13 showing different numbers than what I see in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5840e68c-b00b-4aaf-a197-c4e9cbe423b8",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vc3jwuW6uDUWLpBFDF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31a0240e-b8fd-457c-a221-5b313a4bf73b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWFGnZZ2Nnma9s13zRX3S9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 58846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1403,
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

_source line 56 · 2026-05-16T02:55:10.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MV6N6LwQDgbmds7wYTMrFh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 113,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a0240e-b8fd-457c-a221-5b313a4bf73b",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vc3jwuW6uDUWLpBFDF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27d76986-fda9-44a9-a876-da1601b617c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWFGnZZ2Nnma9s13zRX3S9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 58846,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1403
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 58846,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1403,
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

_source line 57 · 2026-05-16T02:55:10.223Z_

<details><summary>↩ Tool result · `toolu_01MV6N6LwQDgbmds7wYTMrFh`</summary>

```text
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
  "parentUuid": "27d76986-fda9-44a9-a876-da1601b617c0",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "6c910b1c-8e26-4924-aee8-5291ce894fa9",
  "sourceToolAssistantUUID": "27d76986-fda9-44a9-a876-da1601b617c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T02:55:16.833Z_

Let me also check the downstream numbers in the review context vs. the paper. The review context mentions Table 13 with "Qwen +2.60pp avg" but the paper shows +1.9. Let me also verify the KIVI comparison section and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c910b1c-8e26-4924-aee8-5291ce894fa9",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VcXZ29Vy4fJcY5GhoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "824b1dae-966b-4edd-88cf-abb140282f94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Qp83SYhmZFrH6AqjM6hNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 60249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 59 · 2026-05-16T02:55:17.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ABZdLFjybWKj3eDqCFwePp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 84,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "824b1dae-966b-4edd-88cf-abb140282f94",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VcXZ29Vy4fJcY5GhoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67d5f665-c83e-4ad7-8281-4abb2bd427d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Qp83SYhmZFrH6AqjM6hNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 60249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 60 · 2026-05-16T02:55:17.968Z_

<details><summary>↩ Tool result · `toolu_01ABZdLFjybWKj3eDqCFwePp`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67d5f665-c83e-4ad7-8281-4abb2bd427d9",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "a83fbc29-e40e-4a82-b7e4-43120df8f737",
  "sourceToolAssistantUUID": "67d5f665-c83e-4ad7-8281-4abb2bd427d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T02:55:18.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J6ho7N8nTEDSHCsrNifiLv`</summary>

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
  "parentUuid": "a83fbc29-e40e-4a82-b7e4-43120df8f737",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5VcXZ29Vy4fJcY5GhoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da22d9dc-e0fe-4632-a08d-b85bb2952e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Qp83SYhmZFrH6AqjM6hNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 60249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 62 · 2026-05-16T02:55:18.409Z_

<details><summary>↩ Tool result · `toolu_01J6ho7N8nTEDSHCsrNifiLv`</summary>

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
  "parentUuid": "da22d9dc-e0fe-4632-a08d-b85bb2952e58",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "72a90cbe-42c1-4888-8a6a-80f1d5ceb78e",
  "sourceToolAssistantUUID": "da22d9dc-e0fe-4632-a08d-b85bb2952e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-16T02:55:23.884Z_

Now I have enough information to write a comprehensive review. Let me also quickly verify the diagnostic claim of 9/9 models -- I see 9 models evaluated in Table 14 of the analysis section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72a90cbe-42c1-4888-8a6a-80f1d5ceb78e",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vd91UPW7ZZM6cumcyS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0205d5a2-485f-4ea7-9302-c39575ac2d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Q4qjDJmXuFD1qxTffeLQp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 61374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3033,
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

_source line 64 · 2026-05-16T02:55:24.603Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01D5t3jpjQPAWMV3WLq4S7K6`</summary>

```json
{
  "pattern": "9/9|nine.*model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0205d5a2-485f-4ea7-9302-c39575ac2d91",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vd91UPW7ZZM6cumcyS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee0ede08-6e22-4dcf-bcfe-ae14be24dc0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Q4qjDJmXuFD1qxTffeLQp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 61374,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 61374,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3033,
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

_source line 65 · 2026-05-16T02:55:24.632Z_

<details><summary>↩ Tool result · `toolu_01D5t3jpjQPAWMV3WLq4S7K6`</summary>

```text
docs/paper/analysis.tex:11:Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
docs/paper/analysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
docs/paper/conclusion.tex:6:An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine evaluated models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
docs/paper/conclusion.tex:12:The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
docs/paper/abstract.tex:1:Across nine models spanning 1.4B--14B parameters and seven architecture families (MHA through GQA 8:1), we find that per-head non-uniform KV cache quantization on hardware-aligned bit-widths $\{2,4,8,16\}$ provides negligible improvement over uniform 4-bit for eight of nine models.
docs/paper/abstract.tex:6:We characterize sensitivity heterogeneity across all nine models using concentration and distribution shape ($t_1/t_5$ ratio), identifying three patterns (spread, spike, flat) that correctly predict allocation benefit (9/9); the thresholds are preliminary, as only one model exhibits the spread pattern.
docs/paper/introduction.tex:35:We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that correctly classifies all nine evaluated models (9/9), including a within-family scale contrast.
docs/paper/introduction.tex:42:[Omitted long matching line]
docs/paper/introduction.tex:44:\item We provide an empirical characterization of head sensitivity heterogeneity across nine models, revealing three distribution shapes (spread, spike, flat) that predict allocation benefit. Concentration and $t_1/t_5$ ratio correctly classify all nine models (9/9), though the spread pattern is observed in only one model ($N{=}1$, Qwen2.5-7B); the suggested thresholds should be treated as preliminary (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee0ede08-6e22-4dcf-bcfe-ae14be24dc0b",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "1a207957-5833-45bf-be75-923362020603",
  "sourceToolAssistantUUID": "ee0ede08-6e22-4dcf-bcfe-ae14be24dc0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-16T02:55:31.308Z_

Now let me check a key detail: CodeLlama-7B appears in Table 14 (heterogeneity) with "---" for PPL deltas -- was it actually evaluated with constrained MCKP?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a207957-5833-45bf-be75-923362020603",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vdb7cEU9fmvdEcYGgY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdb0325a-bc44-4643-8e6d-526732ee38de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgjTJ6MRuCMcAcQTtMaHSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 64407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 812,
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

_source line 67 · 2026-05-16T02:55:31.638Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Y2fnppGXmS7WWj8PRXUYXm`</summary>

```json
{
  "pattern": "CodeLlama",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb0325a-bc44-4643-8e6d-526732ee38de",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Vdb7cEU9fmvdEcYGgY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d55cb6b6-1e7c-4b82-b7c3-75ee49a1effc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgjTJ6MRuCMcAcQTtMaHSx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 64407,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 812
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 64407,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 812,
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

_source line 68 · 2026-05-16T02:55:31.657Z_

<details><summary>↩ Tool result · `toolu_01Y2fnppGXmS7WWj8PRXUYXm`</summary>

```text
docs/paper/analysis.tex:23:CodeLlama-7B reinforces this: the highest concentration tested ($0.80$) with an extreme spike ($t_1/t_5{=}0.81$, L1H1 contributes $81\%$ of top-5 delta, $11.3\times$ the second-ranked head) confirms that even very high concentration yields no benefit when dominated by a single outlier. %exp_id=codellama_hires_profiling
docs/paper/analysis.tex:53:CodeLlama-7B & 1:1 & 0.80 & 0.81 & --- & --- & Spike \\
docs/paper/analysis.tex:69:\item \textbf{Spike} ($t_1/t_5 > 0.70$ \emph{and} concentration $\geq 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90), CodeLlama (0.80, 0.81), and Llama (0.57, 0.85): no benefit.
docs/paper/analysis.tex:73:Both conditions are needed: CodeLlama ($0.80$), Llama ($0.57$), and Yi-1.5 ($0.71$) all exceed the concentration threshold yet show no MCKP benefit; their spike shapes ($t_1/t_5 \geq 0.70$) correctly override.
docs/paper/analysis.tex:75:The rule correctly classifies all nine evaluated models (9/9), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and two MHA architectures (CodeLlama-7B spike, Pythia-1.4B flat).
docs/paper/conclusion.tex:5:Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.
docs/paper/introduction.tex:32:The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5, CodeLlama, and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Phi-3-medium, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d55cb6b6-1e7c-4b82-b7c3-75ee49a1effc",
  "isSidechain": true,
  "promptId": "1a07757b-162d-45e7-9136-009268fc7328",
  "agentId": "a30881bec0ec9c539",
  "type": "user",
  "uuid": "2cd49b24-d371-4176-8688-c72f9ec29195",
  "sourceToolAssistantUUID": "d55cb6b6-1e7c-4b82-b7c3-75ee49a1effc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-16T02:56:52.147Z_

I now have a complete picture. CodeLlama-7B is claimed as part of the 9/9 diagnostic but has "---" for the actual PPL evaluation (only profiled, not fully evaluated with MCKP). This is a notable gap. Let me now write the review.

---

## R1 Review: Methods and Experiments

### Summary
The paper identifies 2-bit distortion compounding as a failure mode in per-head KV cache quantization with hardware-aligned bit-widths, proposes a cardinality constraint to prevent it, and characterizes when non-uniform allocation is beneficial via a two-metric diagnostic. The primary positive result is on a single model (Qwen2.5-7B); eight other models show no benefit. The paper is commendably honest about this, but the experimental design is heavily Qwen-centric, with most ablations performed on only one architecture.

### Strengths

1. **Clear problem identification with strong evidence.** The compounding phenomenon is convincingly demonstrated through the U-shaped curve (Table 1/Figure in Appendix A) and the cross-architecture compounding sweep (Figure 2, Section 5.2), showing that the additive distortion assumption breaks down specifically at 2-bit.

2. **Rigorous solver equivalence verification.** The claim of greedy=MCKP is verified at the per-head allocation level (112/112, 256/256, 255/256) across three architectures, not merely at the PPL level, and the per-layer brute-force oracle (Appendix, Section on Profiling Resolution) closes the optimality chain with a maximum gap of 0.018 PPL.

3. **Honest framing of the negative result.** The paper clearly states that only 1/9 models benefits (N=1 spread), qualifies all diagnostic thresholds as "preliminary," and acknowledges the KIVI composability limitation (KIVI+MCKP = KIVI alone on Qwen) in Section 5.1. This is unusually frank for the genre.

4. **Multi-seed stability.** The 3-seed calibration stability analysis (mean PPL 10.99 +/- 0.06, 90.2% allocation agreement) and cross-dataset stability (>96% agreement on 3 architectures, Table in Appendix Section G) strengthen reproducibility claims.

5. **Cross-architecture compounding curves (Figure 2/Section 5.2).** Testing compounding on all three sensitivity-pattern archetypes (Qwen/Llama/Mistral) with sweeps up to k=256 provides convincing evidence that the cardinality constraint operates in a universally safe regime.

6. **Wide architectural coverage.** Eight models spanning MHA, GQA 2:1 through 8:1, sliding-window, and softcapped attention provide reasonable diversity for an empirical study.

### Weaknesses

1. **[Major] Qwen-centric ablation design.** The following experiments are conducted only on Qwen2.5-7B: budget sweep (Table in Appendix E), profiling resolution comparison (Appendix I), multi-seed stability (Appendix I), KV separation (Appendix J), runtime benchmark (Appendix K), per-layer oracle validation (Appendix I). Since Qwen is the only "spread" model and the only one that benefits, these ablations cannot confirm generalizability. The cardinality constraint is claimed universal, yet its optimal k is tuned per-model with no principled selection rule beyond "small sweep on calibration data."

2. **[Major] Diagnostic rule validated on training set only.** The 9/9 classification accuracy is computed on the same models used to derive the thresholds (concentration >= 0.50, t1/t5 <= 0.70). With only 1 positive example and 8 negatives, any threshold between the positive (0.61, 0.57) and the nearest negative (Llama: 0.57, 0.85) would achieve 9/9. The claim of "correctly classifies all nine models" overstates what is effectively curve-fitting with zero held-out validation. The authors acknowledge this (N=1, "preliminary"), but it is still prominently repeated in the abstract, introduction, and conclusion.

3. **[Major] CodeLlama-7B counted in 9/9 without end-to-end evaluation.** Table 14 shows "---" for both uniform and constrained PPL on CodeLlama. The diagnostic classification relies on profiling data alone, without actually verifying that constrained MCKP provides no benefit. This weakens the claimed 9/9 accuracy---it is really 8/8 verified + 1 inferred from profiling shape.

4. **[Major] Downstream evaluation lacks confidence intervals for 4/5 models.** Only Qwen has multi-seed error bars in Table (Section 5.3). The remaining models (Yi, Llama, Mistral, Gemma-2) are single-seed, with deltas as small as +/-0.1pp, well within typical evaluation noise. The claim that non-spread models show "near-neutral" change is not statistically distinguishable from zero.

5. **[Minor] Inconsistent quantization scheme comparison with KIVI.** The KIVI comparison (Section 5.1) reveals that per-head symmetric quantization produces uniform 4-bit PPL of 15.45 on Qwen vs. KIVI's 9.91. The paper correctly identifies this as a scheme difference, but the practical implication---that the entire paper's contribution is irrelevant when per-channel asymmetric quantization is available---is understated. The stated use case ("symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support") is asserted without citation or evidence of such hardware constraints in 2025+.

6. **[Minor] Budget sweep at 8x is uninformative.** At 8x compression, both methods produce catastrophic PPL (907 vs. 14759). Claiming "an order of magnitude better" at PPL=907 has no practical utility---neither is usable. The intermediate 5.3x result (Appendix F) is more informative but only covers Llama/Mistral, not Qwen.

7. **[Minor] Runtime benchmark methodology.** The 8.5% overhead is measured with PyTorch-level per-head quantize/dequantize, which the authors acknowledge is not production-realistic. Without kernel-level benchmarks, the throughput claim provides limited guidance for practitioners.

8. **[Minor] Long-context evaluation limited to 8K.** The dramatic result (Qwen uniform 11.15x at 8K) is compelling but only covers 2 models and stops at 8K tokens, far below production context lengths (32K-128K). The claim of "amplification with longer sequences" is an extrapolation.

### Questions for Authors

1. For the cardinality constraint k selection: is there a principled stopping criterion beyond the minimum of the U-shaped curve? Could you characterize the relationship between k and model properties (head count, GQA ratio) to enable k selection without a compounding sweep?

2. The KIVI+MCKP composability experiment shows no additive benefit. Have you tested whether KIVI with per-head mixed-precision (e.g., some heads at 4-bit KIVI, others at 2-bit KIVI) could recover the benefit?

3. For the compounding sweep (Figure 2), are the k heads selected by the same sensitivity ranking? If so, does the compounding onset depend on which heads are selected (top-k most sensitive vs. top-k least sensitive)?

4. The super-additivity coefficients (1.56x at k=8, 4.89x at k=64) are measured on Qwen. What are the corresponding values for Llama and Mistral?

5. Why does the constrained MCKP produce PPL slightly worse than uniform on Gemma-2 (+0.03) and Phi-3-medium (+0.01)? If the solver knows uniform is feasible, it should not produce worse results unless the cardinality constraint forces unnecessary 2-bit assignments.

### Missing Experiments / Evidence Gaps

1. **Multi-seed downstream evaluation for non-Qwen models.** The current single-seed results cannot support claims about near-zero deltas being meaningful.

2. **CodeLlama end-to-end constrained MCKP evaluation.** Required to honestly claim 9/9.

3. **Held-out validation of the diagnostic rule.** At minimum, one additional model not used for threshold derivation should be tested. The Qwen-14B and Pythia additions are not truly independent since Qwen-14B is the same family and Pythia's flat pattern is trivially classified.

4. **Compounding sweep on non-Qwen models.** The cross-architecture compounding (Figure 2) uses all-heads-sorted-by-sensitivity sweeps, but the U-shaped budget optimization curve (Figure 1) showing the optimal k is only demonstrated on Qwen. How do we know k=2 is optimal for Llama/Mistral without their own U-shaped curves?

5. **Oracle comparison on non-Qwen models.** The per-layer brute-force oracle validates the additive distortion assumption, but only on Qwen. If the assumption holds better on flat/spike models (as expected), showing this explicitly would strengthen the argument.

6. **Runtime benchmark on a model where MCKP helps.** Currently measured only on Qwen, but the "is it worth the overhead?" question needs the answer to be on the same model where there is a PPL benefit.

### Claim-Evidence Alignment Issues

1. **"Solver choice irrelevant" claim.** The claim is empirically verified on 3 architectures under constrained allocation. However, the theoretical argument (Section 3.4) requires "no ties in the top-k marginal benefit ranking." This condition is not verified for all 9 models---only the 3 explicitly checked. On Mistral, 1/256 differs, attributed to a "zero-distortion tie with no PPL impact," but this edge case slightly undercuts the universality framing.

2. **"9/9 correct diagnostic."** As noted, one model (CodeLlama) lacks end-to-end evaluation, and the rule is fit on all data with no holdout. A more accurate claim would be "8/8 verified, consistent with 9/9 under profiling-based inference."

3. **"29.4% reduction" headline number.** The paper uses the high-resolution profiling result (10.91) in the main tables and abstract, which is the best-case Qwen number. The standard-resolution result (11.23, still a 27.3% reduction) and the multi-seed mean (10.99) are buried in appendices. The headline number is technically correct (a single seed under hires profiling) but not the most representative.

4. **Cross-dataset stability "96% agreement."** On Llama, 253/256 heads are forced to 4-bit by the k=2 constraint. The paper acknowledges this inflates agreement (Appendix G), but the headline ">96% on all three architectures" benefits from this inflation. On Qwen (where all heads are variable), the 96.4% agreement is genuinely informative.

5. **"Non-uniform allocation provides no meaningful benefit" for 8/9 models.** On Llama, constrained MCKP achieves 8.45 vs. uniform 8.47 (a 0.02 improvement). While this is negligible practically, the direction is positive. The "no benefit" framing is defensible but borders on overstating---more precisely, the benefit is within noise without multi-seed validation.

### Overall Assessment
Score: 4/6
Confidence: 4/5

The paper makes a useful empirical contribution by identifying and fixing 2-bit compounding in per-head KV cache quantization. The methodology is sound (MCKP + cardinality constraint is a clean formulation), the compounding characterization is thorough, and the honest framing that only 1/9 models benefits is refreshing. However, the experimental design is too Qwen-centric for a paper claiming cross-architecture generality: most ablations run on only one model, the diagnostic is fit without holdout, CodeLlama's classification is unverified end-to-end, and downstream results lack error bars on 4/5 models. The practical impact is further limited by the KIVI composability result showing the contribution is subsumed by existing per-channel methods. A solid empirical analysis paper that needs broader ablation coverage and statistical rigor to reach the acceptance bar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cd49b24-d371-4176-8688-c72f9ec29195",
  "isSidechain": true,
  "agentId": "a30881bec0ec9c539",
  "requestId": "req_011Cb5Ve75uuboraU1stE8PT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d3c7511-cba2-4d83-91fc-8fce3002f530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "f6b0b3c4-17a1-4fb2-92fd-0f4f71a4e809",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ98y3GH7zQ7kEuLNLwF3b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 65219,
      "output_tokens": 2988,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2988,
          "cache_read_input_tokens": 65219,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 866,
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
