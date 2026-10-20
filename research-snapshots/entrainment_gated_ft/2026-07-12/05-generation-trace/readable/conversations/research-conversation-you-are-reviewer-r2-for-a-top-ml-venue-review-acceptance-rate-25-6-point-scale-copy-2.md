# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aedb1b6d5c3ff160a.jsonl`
- **Structured JSON:** [`bb35efff37ccacb79ce7.json`](../../sessions/bb/bb35efff37ccacb79ce7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-15T10:20:36.936Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus: **novelty** and **related work**.

## Paper Summary
"The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization"

The paper studies per-head mixed-precision KV cache quantization across 6 models (Qwen2.5-7B/14B/72B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B) with 3 claimed contributions:
1. A cardinality constraint (limiting #2-bit heads) as universal safeguard
2. Systematic negative result: 5/6 models show no benefit from non-uniform allocation
3. Compounding effect characterization with U-shaped PPL-k curve

## Related Work Section (verbatim)
- **KV Cache Quantization**: KIVI (Liu et al. 2024) and KVQuant (Hooper et al. 2024)—uniform bit-width systems.
- **Per-Head Mixed Precision**: RateQuant (Anonymous 2026)—proves greedy optimality on consecutive {2,...,6} via polymatroid. On hardware-aligned {2,4,8,16}, polymatroid breaks. RateQuant acknowledges compounding (Appendix M) but doesn't address it.
- **Quantization-Aware Allocation**: ARKV and related methods—learned/heuristic per-head budgets. None studies *when* non-uniform helps.

Only 3 references total (KIVI, KVQuant, RateQuant).

## Key Results
- Only Qwen2.5-7B benefits from non-uniform (+27.3% PPL). 5/6 models: no benefit.
- Cardinality constraint: prevents catastrophe, makes solver irrelevant.
- Super-additivity: empirical trend, non-monotonic, high variance.
- Qwen family scaling: concentration decreases 7B→14B→72B, suggesting "spread" is small-model artifact.
- BOS correction collapses 3-tier to 2-tier.

## Experiment Design Context (for coverage assessment)
18 imagined experiments covering:
- W1: Qwen14B profiling + constrained MCKP (diagnostic false positive)
- Gemma-2 BOS fix (3-tier collapse)
- L0 auto-discovery, Llama/Mistral full pipeline, compounding sweep, budget sweep
- Hi-res profiling, C4 cross-dataset, RateQuant comparison, oracle comparison
- Cross-calibration, head visualization, downstream eval, 72B profiling-only
- K/V separation, L0 heuristic, multi-seed, runtime benchmark
- W9 compounding scaling (non-monotonic super-additivity)
- Qwen14B downstream (predicted, not run)

Paper covers ~15/18 experiments. Gaps: 14B downstream is predicted, 72B is profile-only, some experiments are condensed.

## Your Task
Provide a detailed review covering:
1. **Novelty assessment**: How novel is each of the 3 contributions? Is the cardinality constraint a genuine contribution or engineering common sense? Is the negative result novel or expected? Is the compounding characterization sufficiently deep?
2. **Related work completeness**: Are there major missing references? Is the positioning against prior work fair?
3. **Contribution significance**: Would this meaningfully advance the field? Who benefits from these findings?
4. **Framing and narrative**: Is the paper well-framed? Does the title match content? Is the "systematic negative result" framing effective?
5. **Strengths** (3-5 bullet points)
6. **Weaknesses** (3-5 bullet points)
7. **Questions for authors** (3-5)
8. **Score** (1-6) with confidence (1-5)

Key considerations:
- The related work section has only 3 references. For a top venue, this is extremely thin. Consider missing work: SqueezeLLM, GPTQ per-group strategies, Atom, QServe, FlexGen, AWQ, AQLM, QuIP#, and attention sink literature (StreamingLLM, H2O).
- The cardinality constraint is essentially "don't put too many heads at 2-bit"—assess whether this rises to the level of a contribution vs. an obvious engineering heuristic.
- The negative result (5/6 don't benefit) is interesting but needs context: is this surprising given that these models have different architectures, or is it expected?
- Super-additivity claim is weakened by non-monotonicity and high variance in Table 5.

Be rigorous. A top venue at 25% acceptance requires strong novelty AND execution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "ba1d877f-a0d5-4be2-880f-05f2f26a99ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T10:20:36.939Z_

```json
{
  "parentUuid": "ba1d877f-a0d5-4be2-880f-05f2f26a99ad",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
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
  "uuid": "1ea3adfa-a8dc-4ffd-8984-61d6ef131830",
  "timestamp": "2026-05-15T10:20:36.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-15T10:20:39.974Z_



I'll conduct a thorough review by reading the paper's key sections to assess novelty, related work, and contribution significance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea3adfa-a8dc-4ffd-8984-61d6ef131830",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BmkRKtNSKkZw6esqmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be2bef3-dbc6-40f2-96d2-b415d7b34430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cgKFJSHBmZpwkmMYpWHU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6974,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-15T10:20:41.397Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NuNXHrkm3S6RZrs1GscxMa`</summary>

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
  "parentUuid": "8be2bef3-dbc6-40f2-96d2-b415d7b34430",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BmkRKtNSKkZw6esqmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ebd4910-45e4-45af-983b-c2f950fe182d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cgKFJSHBmZpwkmMYpWHU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6974,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-15T10:20:41.402Z_

<details><summary>↩ Tool result · `toolu_01NuNXHrkm3S6RZrs1GscxMa`</summary>

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
15	The root cause is not solver suboptimality but a violation of the additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.
17	The additive model predicts $\sim$11 PPL; the actual PPL is $3$--$4\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.
18	
19	This observation points to a minimal intervention: cap the number of 2-bit assignments.
20	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
21	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
22	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
23	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
24	The constraint is beneficial even on flat-distribution architectures: on Gemma-2-9B, unconstrained MCKP assigns 31.5\% of heads to 2-bit, producing a moderate $1.47\times$ degradation; the constraint reduces this to within 0.5\% of uniform.
25	
26	A surprising consequence is that the cardinality constraint renders solver choice irrelevant.
27	Constrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm.
28	A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
29	
30	However, non-uniform allocation does not help universally.
31	On Llama-3.1-8B (8.45 vs.\ 8.47), Yi-1.5-9B (7.22 vs.\ 7.22), Mistral-7B-v0.3 (7.16 vs.\ 7.13), and Gemma-2-9B (within 0.5\% of uniform), constrained MCKP provides no meaningful improvement.
32	The difference traces to the \emph{distribution shape} of head sensitivity, not GQA ratio alone: Qwen's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5 has a single extreme outlier (``spike''); Gemma-2 and Mistral show near-uniform sensitivity (``flat'').
33	
34	This motivates a question prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
35	We propose a joint empirical decision rule based on concentration and distribution shape (\S\ref{sec:heterogeneity}) that separates the one beneficial case from the four non-beneficial ones.
36	Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.
37	
38	Our contributions are:
39	\begin{enumerate}[nosep]
40	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
41	
42	\item We demonstrate that the cardinality constraint serves three roles: preventing catastrophic failure on spread architectures (Qwen: 32.45$\to$11.23), preventing moderate over-allocation on flat architectures (Gemma-2: 8.85$\to$within 0.5\% of uniform), and rendering solver choice irrelevant---constrained greedy and MCKP produce equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
43	
44	\item We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly separates the one architecture where non-uniform allocation helps from the four where it does not, across all five models tested. Yi-1.5-9B serves as a critical test: its concentration exceeds Qwen's, yet its single-outlier spike pattern means MCKP provides no benefit over uniform (\S\ref{sec:heterogeneity}).
45	\end{enumerate}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ebd4910-45e4-45af-983b-c2f950fe182d",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "67697578-7dcc-4440-8575-c6f51ba5abd9",
  "sourceToolAssistantUUID": "1ebd4910-45e4-45af-983b-c2f950fe182d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T10:20:41.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NyZpa4WWxvvgbaGpe7LQRs`</summary>

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
  "parentUuid": "67697578-7dcc-4440-8575-c6f51ba5abd9",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BmkRKtNSKkZw6esqmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1bc87e1-c7f2-4da3-b1cb-d445683bb012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cgKFJSHBmZpwkmMYpWHU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6974,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 7 · 2026-05-15T10:20:41.952Z_

<details><summary>↩ Tool result · `toolu_01NyZpa4WWxvvgbaGpe7LQRs`</summary>

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
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
28	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
29	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
30	
31	\subsection{Compounding Effect}
32	\label{sec:compounding}
33	
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively: truncation errors from multiple 2-bit heads accumulate through the residual stream, and once their count exceeds the network's capacity to compensate, PPL degrades super-linearly.
35	
36	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
37	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
38	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
39	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
40	
41	This compounding is specific to 2-bit quantization and is \emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\times$ at $k{=}64$.
42	A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.
43	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
44	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
45	
46	The relationship between $k$ and PPL is U-shaped (Figure~\ref{fig:compounding}, Appendix~\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.
47	
48	\subsection{Cardinality Constraint}
49	\label{sec:cardinality}
50	
51	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
52	\begin{equation}
53	\label{eq:constraint}
54	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
55	\end{equation}
56	
57	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
58	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
59	
60	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
61	
62	One might expect Layer-0 heads to require explicit protection.
63	On Qwen2.5-7B, however, the profiler assigns very high 2-bit distortion to Layer-0 heads (L0H0: $+$31.9\%, L0H2: $+$23.2\%, L0H3: $+$11.7\% relative to bf16), so no solver would assign them 2-bit under any reasonable budget.
64	Running the solver with and without manual Layer-0 exclusion produces identical allocations; no manual rule is needed.
65	
66	\paragraph{Restoring additivity.}
67	The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.
68	Restricting 2-bit heads to $k \ll H$ pushes the allocation back into a near-additive regime where the profiler's prediction agrees with measured PPL.
69	For Qwen2.5-7B, $k{=}8$ ($\sim$7\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\ref{fig:compounding}).
70	This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (11.23 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
71	
72	\subsection{Solver Equivalence}
73	\label{sec:solver_equiv}
74	
75	\begin{table}[t]
76	\centering
77	\small
78	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
79	\label{tab:solver_equiv}
80	\begin{tabular}{llcccc}
81	\toprule
82	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
83	 & & & 2-bit & 4-bit & 8/16-bit \\
84	\midrule
85	Greedy & None & 32.45 & 68 & 30 & 14 \\
86	MCKP & None & 36.92 & 75 & 33 & 4 \\
87	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
88	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
89	Uniform & --- & 15.45 & 0 & 112 & 0 \\
90	\bottomrule
91	\end{tabular}
92	\end{table}
93	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (Appendix~\ref{sec:profiling_resolution}).}
94	
95	With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (11.23), same bit distribution on Qwen2.5-7B.
96	
97	\paragraph{Empirical observation.}
98	When $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.
99	The constraint restricts the feasible set so that the only decision is which $k$ heads to assign 2-bit; the marginal-benefit ordering determines this uniquely, so greedy's local choice coincides with the global optimum.
100	We verify this across three architectures: Qwen2.5-7B (112/112 heads identical), Llama-3.1-8B (256/256), Mistral-7B-v0.3 (255/256; the single difference is a zero-distortion tie with no PPL impact).
101	Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.
102	Practitioners can therefore use the simpler $O(H \log H)$ greedy algorithm without sacrificing optimality.
103	
104	A per-layer brute-force oracle on Qwen2.5-7B confirms near-optimality: of 8 layers with non-trivial allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL (0.4\% of the total improvement), closing the optimality chain from greedy through MCKP to brute-force.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1bc87e1-c7f2-4da3-b1cb-d445683bb012",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "1a1a60d0-16f3-4817-8ec3-9d36c1d5f1d1",
  "sourceToolAssistantUUID": "b1bc87e1-c7f2-4da3-b1cb-d445683bb012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T10:20:42.069Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Aw7DxoaK3THiwYhkmNJqD1`</summary>

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
  "parentUuid": "1a1a60d0-16f3-4817-8ec3-9d36c1d5f1d1",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BmkRKtNSKkZw6esqmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "697d1cc6-f5a5-496c-91d9-79f418d644fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cgKFJSHBmZpwkmMYpWHU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 9160,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 9160,
          "cache_creation_input_tokens": 6974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6974,
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

_source line 9 · 2026-05-15T10:20:42.074Z_

<details><summary>↩ Tool result · `toolu_01Aw7DxoaK3THiwYhkmNJqD1`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on five architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Yi-1.5-9B} (8:1, 48 $\times$ 4 = 192 KV heads),
11	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
12	\textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention),
13	and \textbf{Gemma-2-9B} (2:1, 42 $\times$ 8 = 336 KV heads, \texttt{head\_dim}=256, attention logit softcapping).
14	This selection spans GQA ratios from 2:1 to 8:1 and covers standard, sliding-window, and softcapped attention.
15	
16	\paragraph{Evaluation.}
17	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
18	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
19	
20	\paragraph{Profiling.}
21	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
22	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
23	Unless marked with $\dagger$, all results use standard-resolution profiling; Appendix~\ref{sec:profiling_resolution} analyzes the effect of resolution.
24	
25	\paragraph{Compression and constraint.}
26	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
27	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2).
28	
29	\paragraph{Baselines.}
30	We compare against:
31	(1)~uniform 4-bit quantization;
32	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
33	(3)~unconstrained MCKP allocation;
34	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
35	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
36	
37	\subsection{Main Results}
38	\label{sec:main_results}
39	
40	\begin{table}[t]
41	\centering
42	\small
43	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure severity tracks heterogeneity shape: catastrophic on Qwen ($3.3\times$ bf16), moderate on Gemma-2 ($1.5\times$), mild on the remaining three (${\sim}1.1\times$). Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok). $^\ddagger$Best $k$ from ablation ($k{=}4$). $^*$BOS-corrected.}
44	\label{tab:main_results}
45	\begin{tabular}{lccccc}
46	\toprule
47	Model & Baseline & Uniform & Uncons. & Ours \\
48	 & (bf16) & (4-bit) & MCKP & (Constr.) \\
49	\midrule
50	Qwen2.5-7B      & 9.81  & 15.45 & 36.92 & \textbf{11.23} \\
51	Yi-1.5-9B$^\dagger$       & 7.02  & 7.22  & 7.56  & 7.22 \\
52	Llama-3.1-8B$^\dagger$    & 8.09  & 8.47  & 8.63  & \textbf{8.45} \\
53	Mistral-7B-v0.3$^\dagger$ & 7.04  & 7.13  & 7.57  & 7.16$^\ddagger$ \\
54	Gemma-2-9B$^{*\dagger}$   & 6.03  & 6.17  & 8.85  & 6.20 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45); hires profiling further improves this to 10.91 (Appendix~\ref{sec:profiling_resolution}).
60	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
61	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
62	
63	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
64	Hires profiling reveals a spike pattern (concentration 0.57, $t_1/t_5{=}0.85$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.
65	
66	On Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\%)---a genuine negative result, as the profiler reports near-zero sensitivity differences across heads.
67	Mistral's sliding-window attention may contribute to this uniformity.
68	
69	On Yi-1.5-9B$^\dagger$, constrained MCKP ($k{=}2$) matches uniform at 7.22 PPL.
70	Despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient to exploit.
71	
72	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17, slightly above ($+$0.4\%).
73	Despite its flat sensitivity distribution (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16)---a moderate failure driven by the solver assigning 31.5\% of heads to 2-bit (vs.\ 4.7--16.4\% in other non-spread models).
74	The constraint reduces 2-bit heads from 106 to 8, confirming that it universally prevents over-allocation regardless of distribution shape.
75	
76	Unconstrained failure severity tracks heterogeneity shape: catastrophic on Qwen ($3.3\times$ bf16), moderate on Gemma-2 ($1.47\times$), mild on the remaining three (${\sim}1.07$--$1.08\times$).
77	The allocation visualization (Figure~\ref{fig:allocation}, Appendix~\ref{sec:allocation_appendix}) and budget sweep (Appendix~\ref{sec:budget_sweep}) provide additional detail.
78	
79	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
80	
81	\subsection{Downstream Evaluation}
82	\label{sec:downstream}
83	
84	\begin{table}[t]
85	\centering
86	\small
87	\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results. $^\dagger$Hires profiling.}
88	\label{tab:downstream}
89	\begin{tabular}{lccccc}
90	\toprule
91	Model & ARC-C & HS & PIQA & WG & Avg \\
92	\midrule
93	Qwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\
94	Yi-1.5-9B$^\dagger$        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\
95	Llama-3.1-8B$^\dagger$     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\
96	Mistral-7B$^\dagger$       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\
97	Gemma-2-9B$^\dagger$       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	On Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\ 0.660), recovering $\sim$73\% of the accuracy lost to quantization.
103	The four non-spread architectures show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts).
104	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate.
105	Cross-dataset stability analysis (Appendix~\ref{sec:cross_dataset}) confirms ${>}96\%$ bit-assignment agreement between WikiText-2 and C4 calibration across all three tested models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "697d1cc6-f5a5-496c-91d9-79f418d644fb",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "a751f21b-2e1c-4871-9fdc-259a046833a9",
  "sourceToolAssistantUUID": "697d1cc6-f5a5-496c-91d9-79f418d644fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T10:20:46.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eokef2k7sPkzEqaATgpaRe`</summary>

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
  "parentUuid": "a751f21b-2e1c-4871-9fdc-259a046833a9",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bn8a5k4vb69XndCcQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbed2892-5061-4310-9ce9-b5be56cc1a1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VjUyVjnSB9g6JtVBhFej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9181,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9181,
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

_source line 11 · 2026-05-15T10:20:46.666Z_

<details><summary>↩ Tool result · `toolu_01Eokef2k7sPkzEqaATgpaRe`</summary>

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
11	Table~\ref{tab:heterogeneity} summarizes the results across five architectures at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling
21	
22	Llama-3.1-8B shows above-threshold concentration ($0.57$) with a pronounced spike ($t_1/t_5{=}0.85$, $t_1/t_2{=}34.8$); its allocation is indistinguishable from uniform ($+$0.36 vs.\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
23	Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.38$) both exhibit flat distributions with low concentration ($0.24$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.16 vs.\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
29	\label{tab:heterogeneity}
30	\begin{tabular}{lcccccc}
31	\toprule
32	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
33	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
34	\midrule
35	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.42 & Spread \\
36	Yi-1.5-9B$^\dagger$ & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
37	Llama-3.1-8B$^\dagger$ & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
38	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.24 & 0.41 & $+$0.10 & $+$0.13 & Flat \\
39	Gemma-2-9B$^{*\dagger}$ & 2:1 & 0.23 & 0.38 & $+$0.14 & $+$0.16 & Flat \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	The per-head heatmap (Figure~\ref{fig:heatmap}, Appendix~\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (34\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.
45	
46	\subsection{Empirical Decision Rule}
47	\label{sec:diagnostic}
48	
49	MCKP benefit requires not just high concentration but a specific \emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.
50	This motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.
51	Given the profiling results from \S\ref{sec:profiling}, compute the top-5\% concentration and $t_1/t_5$ ratio, then select:
52	\begin{itemize}[nosep]
53	\item \textbf{Spread} (concentration $\gtrsim 0.50$, $t_1/t_5 \lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$27.3\% PPL.
54	\item \textbf{Spike} ($t_1/t_5 \gtrsim 0.70$, any concentration): use uniform. A single outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.57, 0.85): no benefit.
55	\item \textbf{Flat} (concentration $\lesssim 0.50$): use uniform. Too little cumulative delta for meaningful reallocation; $t_1/t_5$ is irrelevant. Mistral (0.24) and Gemma-2 (0.23): counterproductive.
56	\end{itemize}
57	
58	Both conditions are needed: Llama's concentration (0.57) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.85$) correctly predicts no benefit.
59	A concentration-only threshold would misclassify two of three high-concentration models (Yi-1.5 at 0.71, Llama at 0.57).
60	Only Qwen exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as illustrative until confirmed on additional architectures.
61	The rule reuses profiling data already required by the solver and adds no overhead.
62	
63	Additional analyses---granularity tradeoff (Appendix~\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\ref{sec:granularity}--\ref{sec:kv_separation}.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbed2892-5061-4310-9ce9-b5be56cc1a1e",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "722910f9-a839-489b-aa57-3f58dd3e159a",
  "sourceToolAssistantUUID": "bbed2892-5061-4310-9ce9-b5be56cc1a1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T10:20:47.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VmmkS6XwWFMZgfPShEGi4b`</summary>

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
  "parentUuid": "722910f9-a839-489b-aa57-3f58dd3e159a",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bn8a5k4vb69XndCcQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf513eb6-0da3-4cfd-a1aa-d229765cef71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VjUyVjnSB9g6JtVBhFej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9181,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9181,
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

_source line 13 · 2026-05-15T10:20:47.067Z_

<details><summary>↩ Tool result · `toolu_01VmmkS6XwWFMZgfPShEGi4b`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 11.23 ($-$27.3\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2) patterns show no benefit.
6	A joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly separates these cases across all five models, though the spread category rests on $N{=}1$ and requires further validation.
7	Extending to 70B+ models, integrating with production inference engines, and investigating per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	The spread category is represented by a single architecture (Qwen2.5-7B); validating on additional high-concentration models is necessary before the decision rule can be applied with high confidence.
12	We evaluate only five 7--9B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
13	Profiling relies on a single sensitivity metric (perplexity-based per-head distortion); gradient-based or activation-norm alternatives remain unexplored.
14	We report no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.
15	We have not verified whether these findings transfer to 70B+ scales, and profiling and primary evaluation use a single dataset (WikiText-2).
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf513eb6-0da3-4cfd-a1aa-d229765cef71",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "63329991-a1c6-4008-87bb-bf982027d2fe",
  "sourceToolAssistantUUID": "cf513eb6-0da3-4cfd-a1aa-d229765cef71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T10:20:48.057Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MGs9vSEZSbXSvyP2dwaewJ`</summary>

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
  "parentUuid": "63329991-a1c6-4008-87bb-bf982027d2fe",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bn8a5k4vb69XndCcQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff49190-edb6-4500-9001-111e29cc004f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VjUyVjnSB9g6JtVBhFej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9181,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9181,
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

_source line 15 · 2026-05-15T10:20:48.064Z_

<details><summary>↩ Tool result · `toolu_01MGs9vSEZSbXSvyP2dwaewJ`</summary>

```text
1	Non-uniform per-head KV cache quantization helps only when head sensitivity exhibits a specific distribution shape---a finding obscured by prior work's focus on aggregate metrics.
2	We study five 7--9B architectures on hardware-aligned bit-widths $\{2,4,8,16\}$ and find that the benefit of per-head allocation depends not on GQA ratio or overall sensitivity magnitude, but on whether heterogeneity is \emph{spread} across multiple heads with cross-bitwidth gradients or concentrated in a single outlier.
3	On the one spread-pattern model (Qwen2.5-7B), a cardinality-constrained solver achieves 11.23 perplexity at $4\times$ compression---a 27.3\% reduction over uniform 4-bit (15.45)---while unconstrained solvers fail catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
4	On the remaining four models, non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.
5	The cardinality constraint prevents catastrophic failure on spread architectures, moderate over-allocation on flat architectures (Gemma-2: unconstrained $1.47\times$ degradation reduced to within 0.5\% of uniform), and renders solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\log H)$ greedy algorithm.
6	We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly separates the beneficial case from the four non-beneficial ones across all five models studied.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff49190-edb6-4500-9001-111e29cc004f",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "231b8a7d-7b71-46f7-811f-857a56c1862b",
  "sourceToolAssistantUUID": "aff49190-edb6-4500-9001-111e29cc004f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T10:20:48.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RZ9EVqhgUaHTNCeJJxPkie`</summary>

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
  "parentUuid": "231b8a7d-7b71-46f7-811f-857a56c1862b",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bn8a5k4vb69XndCcQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc4985fc-e234-43e4-be37-78f9aff40419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173VjUyVjnSB9g6JtVBhFej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9181,
      "cache_read_input_tokens": 16134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9181,
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

_source line 17 · 2026-05-15T10:20:48.165Z_

<details><summary>↩ Tool result · `toolu_01RZ9EVqhgUaHTNCeJJxPkie`</summary>

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
19	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling.}
20	\label{tab:heuristic}
21	\begin{tabular}{lcccc}
22	\toprule
23	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
24	 & & Median & Mean$\pm$Std & Positional \\
25	\midrule
26	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
27	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
28	Mistral-7B-v0.3 & 7.16  & 7.20  & 7.24$\pm$0.07  & 7.21 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL.
34	On Llama ($k{=}2$), all methods cluster within 0.17 PPL; on Mistral ($k{=}4$), all non-uniform strategies are worse than uniform (7.13), with MCKP (7.16) closest.
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
63	\emph{Per-head} allocation (ours) exposes this heterogeneity to the solver and yields a 27.3\% PPL improvement on Qwen, at the cost of $H$ profiling passes; the cardinality constraint developed in \S\ref{sec:cardinality} renders the choice of solver irrelevant, amortizing the search overhead.
64	\emph{Token-level} allocation (ZipCache~\cite{he2024zipcache}, KIVI~\cite{liu2024kivi}) is the finest grain available but introduces runtime overhead from online importance scoring.
65	Importantly, per-head and per-token granularities are orthogonal: a head's bitwidth (static, determined offline) and a token's importance (dynamic, determined online) compose without conflict, so the two can be combined.
66	Per-head therefore occupies the sweet spot for static allocation---fine enough to capture the head-level heterogeneity that drives MCKP benefit on spread architectures, yet free of any per-step runtime cost.
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
180	The limitation noted in Section~\ref{sec:conclusion}---that we report no real-kernel latency benchmarks---remains: the numbers above quantify simulation overhead, not production inference speedup.
181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc4985fc-e234-43e4-be37-78f9aff40419",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "dfaf2ba0-afa3-48c5-87a1-dad73c4d1635",
  "sourceToolAssistantUUID": "cc4985fc-e234-43e4-be37-78f9aff40419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T10:20:50.410Z_

Now let me check the bibliography for the full reference list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfaf2ba0-afa3-48c5-87a1-dad73c4d1635",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BnauN163CG6iojBLDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dbde528-a02f-488e-af72-c42d0b8d00e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qsjTnuzoUJhrC6fmhu6kC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8628,
      "cache_read_input_tokens": 25315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8628,
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

_source line 19 · 2026-05-15T10:20:52.470Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nej1Y8YMaBUZ9VZie2y5Nu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.bbl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dbde528-a02f-488e-af72-c42d0b8d00e1",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BnauN163CG6iojBLDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93606ce1-0308-4894-aeb7-c430dcc509c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qsjTnuzoUJhrC6fmhu6kC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8628,
      "cache_read_input_tokens": 25315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8628,
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

_source line 20 · 2026-05-15T10:20:52.474Z_

<details><summary>↩ Tool result · `toolu_01Nej1Y8YMaBUZ9VZie2y5Nu`</summary>

```text
1	\begin{thebibliography}{31}
2	\providecommand{\natexlab}[1]{#1}
3	
4	\bibitem[{Dong et~al.(2020)Dong, Yao, Cai, Arfeen, Gholami, Mahoney, and
5	  Keutzer}]{dong2020hawqv2}
6	Zhen Dong, Zhewei Yao, Yaohui Cai, Daiyaan Arfeen, Amir Gholami, Michael~W.
7	  Mahoney, and Kurt Keutzer. 2020.
8	\newblock \href {https://arxiv.org/abs/1911.03852} {{HAWQ-V2}: {Hessian} aware
9	  trace-weighted quantization of neural networks}.
10	\newblock In \emph{NeurIPS 2020}.
11	
12	\bibitem[{Dong et~al.(2019)Dong, Yao, Gholami, Mahoney, and
13	  Keutzer}]{dong2019hawq}
14	Zhen Dong, Zhewei Yao, Amir Gholami, Michael~W. Mahoney, and Kurt Keutzer.
15	  2019.
16	\newblock \href {https://arxiv.org/abs/1905.03696} {{HAWQ}: {Hessian} aware
17	  quantization of neural networks with mixed-precision}.
18	\newblock In \emph{ICCV 2019}.
19	
20	\bibitem[{Duanmu et~al.(2024)Duanmu, Yuan, Li, Duan, Zhang, and
21	  Lin}]{duanmu2024skvq}
22	Haojie Duanmu, Zhihang Yuan, Xiuhong Li, Jiangfei Duan, Xingcheng Zhang, and
23	  Dahua Lin. 2024.
24	\newblock \href {https://arxiv.org/abs/2405.06219} {{SKVQ}: Sliding-window key
25	  and value cache quantization for large language models}.
26	\newblock \emph{Preprint}, arXiv:2405.06219.
27	\newblock ArXiv preprint.
28	
29	\bibitem[{Feng et~al.(2025)Feng, Lv, Cao, Xie, and Zhou}]{feng2025adakv}
30	Yuan Feng, Junlin Lv, Yukun Cao, Xike Xie, and S.~Kevin Zhou. 2025.
31	\newblock \href {https://arxiv.org/abs/2407.11550} {{Ada-KV}: Optimizing {KV}
32	  cache eviction by adaptive budget allocation}.
33	\newblock In \emph{NeurIPS 2025}.
34	
35	\bibitem[{Fu et~al.(2025)Fu, Cai, Sid-Lakhdar, Zhao, and Peng}]{fu2025headkv}
36	Yu~Fu, Zefan Cai, Abdelrahman Sid-Lakhdar, Wayne~Xin Zhao, and Richard Peng.
37	  2025.
38	\newblock \href {https://arxiv.org/abs/2410.19258} {Not all heads matter: A
39	  head-level {KV} cache compression method with integrated retrieval and
40	  reasoning}.
41	\newblock In \emph{ICLR 2025}.
42	
43	\bibitem[{Ge et~al.(2024)Ge, Zhang, Liu, Zhang, Han, and Gao}]{ge2024fastgen}
44	Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, and Jianfeng Gao.
45	  2024.
46	\newblock \href {https://arxiv.org/abs/2310.01801} {Model tells you what to
47	  discard: Adaptive {KV} cache compression for {LLMs}}.
48	\newblock In \emph{ICLR 2024}.
49	
50	\bibitem[{Haeri~Boroujeni et~al.(2026)Haeri~Boroujeni, Mehrabi, Woods,
51	  Hillesheim, and Razi}]{haeriboroujeni2026dontwaste}
52	Sayed~Pedram Haeri~Boroujeni, Niloufar Mehrabi, Patrick Woods, Gabriel
53	  Hillesheim, and Abolfazl Razi. 2026.
54	\newblock \href {https://arxiv.org/abs/2604.04722} {Don't waste bits!
55	  {Adaptive} {KV}-cache quantization for lightweight on-device {LLMs}}.
56	\newblock In \emph{CVPR 2026}.
57	
58	\bibitem[{He et~al.(2024)He, Zhang, Wu, Liu, Zhou, and Zhuang}]{he2024zipcache}
59	Yefei He, Luoming Zhang, Weijia Wu, Jing Liu, Hong Zhou, and Bohan Zhuang.
60	  2024.
61	\newblock \href {https://arxiv.org/abs/2405.14256} {{ZipCache}: Accurate and
62	  efficient {KV} cache quantization with salient token identification}.
63	\newblock In \emph{NeurIPS 2024}.
64	
65	\bibitem[{Hooper et~al.(2024)Hooper, Kim, Mohammadzadeh, Mahoney, Shao,
66	  Keutzer, and Gholami}]{hooper2024kvquant}
67	Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael~W. Mahoney,
68	  Yakun~Sophia Shao, Kurt Keutzer, and Amir Gholami. 2024.
69	\newblock \href {https://arxiv.org/abs/2401.18079} {{KVQuant}: Towards 10
70	  million context length {LLM} inference with {KV} cache quantization}.
71	\newblock In \emph{NeurIPS 2024}.
72	
73	\bibitem[{Kang et~al.(2024)Kang, Zhang, Kundu, Jeong, Liu, Krishna, and
74	  Zhao}]{kang2024gear}
75	Hao Kang, Qingru Zhang, Souvik Kundu, Geonhwa Jeong, Zaoxing Liu, Tushar
76	  Krishna, and Tuo Zhao. 2024.
77	\newblock \href {https://arxiv.org/abs/2403.05527} {{GEAR}: An efficient {KV}
78	  cache compression recipe for near-lossless generative inference of {LLM}}.
79	\newblock \emph{Preprint}, arXiv:2403.05527.
80	\newblock ArXiv preprint.
81	
82	\bibitem[{Kim et~al.(2024)Kim, Hooper, Gholami, Dong, Li, Shen, Mahoney, and
83	  Keutzer}]{kim2024squeezellm}
84	Sehoon Kim, Coleman Hooper, Amir Gholami, Zhen Dong, Xiuyu Li, Sheng Shen,
85	  Michael~W. Mahoney, and Kurt Keutzer. 2024.
86	\newblock \href {https://arxiv.org/abs/2306.07629} {{SqueezeLLM}:
87	  Dense-and-sparse quantization}.
88	\newblock In \emph{ICML 2024}.
89	
90	\bibitem[{Lei and Ilager(2026)}]{lei2026arkv}
91	Jianlong Lei and Shashikant Ilager. 2026.
92	\newblock \href {https://arxiv.org/abs/2603.08727} {{ARKV}: Adaptive and
93	  resource-efficient {KV} cache management under limited memory budget for
94	  long-context inference in {LLMs}}.
95	\newblock \emph{Preprint}, arXiv:2603.08727.
96	\newblock ArXiv preprint.
97	
98	\bibitem[{Li et~al.(2025{\natexlab{a}})Li, Liu, Wu, Nie, and
99	  Wang}]{li2025kvmix}
100	Fei Li, Song Liu, Weiguo Wu, Shiqiang Nie, and Jinyu Wang. 2025{\natexlab{a}}.
101	\newblock \href {https://arxiv.org/abs/2506.08018} {{KVmix}: Gradient-based
102	  layer importance-aware mixed-precision quantization for {KV} cache}.
103	\newblock \emph{Preprint}, arXiv:2506.08018.
104	\newblock ArXiv preprint.
105	
106	\bibitem[{Li et~al.(2024)Li, Huang, Yang, Venkitesh, Locatelli, Ye, Cai, Lewis,
107	  and Chen}]{li2024snapkv}
108	Yuhong Li, Yingbing Huang, Bowen Yang, Bharat Venkitesh, Acyr Locatelli,
109	  Hanchen Ye, Tianle Cai, Patrick Lewis, and Deming Chen. 2024.
110	\newblock \href {https://arxiv.org/abs/2404.14469} {{SnapKV}: {LLM} knows what
111	  you are looking for before generation}.
112	\newblock In \emph{NeurIPS 2024}.
113	
114	\bibitem[{Li et~al.(2025{\natexlab{b}})Li, Shen, Tang, Luo, and
115	  Dai}]{li2025kvtuner}
116	Zhongzhi Li, Yuhan Shen, Yixuan Tang, Jian Luo, and Yonggang Dai.
117	  2025{\natexlab{b}}.
118	\newblock \href {https://arxiv.org/abs/2502.04420} {{KVTuner}:
119	  Sensitivity-aware layer-wise mixed-precision {KV} cache quantization for
120	  efficient and nearly lossless {LLM} inference}.
121	\newblock In \emph{ICML 2025}.
122	
123	\bibitem[{Lin et~al.(2025)Lin, Tang, Yang, Zhang, Xiao, Gan, and
124	  Han}]{lin2024qserve}
125	Yujun Lin, Haotian Tang, Shang Yang, Zhekai Zhang, Guangxuan Xiao, Chuang Gan,
126	  and Song Han. 2025.
127	\newblock \href {https://arxiv.org/abs/2405.04532} {{QServe}: {W4A8KV4}
128	  quantization and system co-design for efficient {LLM} serving}.
129	\newblock In \emph{MLSys 2025}.
130	
131	\bibitem[{Liu et~al.(2025)Liu, Li, Yang, Zhao, Zhou, Song, Dai, Yan, Yang, and
132	  Wang}]{liu2025pmkvq}
133	Tengxuan Liu, Shiyao Li, Jiayi Yang, Tianchen Zhao, Feng Zhou, Xiaohui Song,
134	  Guohao Dai, Shengen Yan, Huazhong Yang, and Yu~Wang. 2025.
135	\newblock \href {https://arxiv.org/abs/2505.18610} {{PM-KVQ}: Progressive
136	  mixed-precision {KV} cache quantization for long-cot {LLMs}}.
137	\newblock \emph{Preprint}, arXiv:2505.18610.
138	\newblock ArXiv preprint.
139	
140	\bibitem[{Liu et~al.(2023)Liu, Desai, Liao, Wang, Xie, Xu, Kyrillidis, and
141	  Shrivastava}]{liu2024scissorhands}
142	Zichang Liu, Aditya Desai, Fangshuo Liao, Weitao Wang, Victor Xie, Zhaozhuo Xu,
143	  Anastasios Kyrillidis, and Anshumali Shrivastava. 2023.
144	\newblock \href {https://arxiv.org/abs/2305.17118} {Scissorhands: Exploiting
145	  the persistence of importance hypothesis for {LLM} {KV} cache compression at
146	  test time}.
147	\newblock In \emph{NeurIPS 2023}.
148	
149	\bibitem[{Liu et~al.(2024)Liu, Yuan, Jin, Zhong, Xu, Braverman, Chen, and
150	  Hu}]{liu2024kivi}
151	Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir
152	  Braverman, Beidi Chen, and Xia Hu. 2024.
153	\newblock \href {https://arxiv.org/abs/2402.02750} {{KIVI}: A tuning-free
154	  asymmetric 2bit quantization for {KV} cache}.
155	\newblock In \emph{ICML 2024}.
156	
157	\bibitem[{Michel et~al.(2019)Michel, Levy, and Neubig}]{michel2019sixteen}
158	Paul Michel, Omer Levy, and Graham Neubig. 2019.
159	\newblock \href {https://arxiv.org/abs/1905.10650} {Are sixteen heads really
160	  better than one?}
161	\newblock In \emph{NeurIPS 2019}.
162	
163	\bibitem[{Sharma et~al.(2025)Sharma, Ding, Li, Dani, and
164	  Zhang}]{sharma2025minikv}
165	Akshat Sharma, Hangliang Ding, Jianping Li, Neel Dani, and Minjia Zhang. 2025.
166	\newblock \href {https://arxiv.org/abs/2411.18077} {{MiniKV}: Pushing the
167	  limits of 2-bit {KV} cache via compression and system co-design for efficient
168	  long context inference}.
169	\newblock In \emph{Findings of ACL 2025}.
170	
171	\bibitem[{Shutova et~al.(2025)Shutova, Malinovskii, Egiazarian, Kuznedelev,
172	  Mazur, Surkov, Ermakov, and Alistarh}]{shutova2025aquakv}
173	Alina Shutova, Vladimir Malinovskii, Vage Egiazarian, Denis Kuznedelev, Denis
174	  Mazur, Nikita Surkov, Ivan Ermakov, and Dan Alistarh. 2025.
175	\newblock \href {https://arxiv.org/abs/2501.19392} {Cache me if you must:
176	  Adaptive key-value quantization for large language models}.
177	\newblock In \emph{ICML 2025}.
178	
179	\bibitem[{Su et~al.(2025)Su, Chen, Shen, Wei, Li, Yu, and
180	  Yuan}]{su2025rotatekv}
181	Zunhai Su, Zhe Chen, Wang Shen, Hanyu Wei, Linge Li, Huangqi Yu, and Kehong
182	  Yuan. 2025.
183	\newblock \href {https://arxiv.org/abs/2501.16383} {{RotateKV}: Accurate and
184	  robust 2-bit {KV} cache quantization for {LLMs} via outlier-aware adaptive
185	  rotations}.
186	\newblock In \emph{IJCAI 2025}.
187	
188	\bibitem[{Voita et~al.(2019)Voita, Talbot, Moiseev, Sennrich, and
189	  Titov}]{voita2019analyzing}
190	Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov. 2019.
191	\newblock \href {https://arxiv.org/abs/1905.09418} {Analyzing multi-head
192	  self-attention: Specialized heads do the heavy lifting, the rest can be
193	  pruned}.
194	\newblock In \emph{ACL 2019}.
195	
196	\bibitem[{Wang et~al.(2019)Wang, Liu, Lin, Lin, and Han}]{wang2019haq}
197	Kuan Wang, Zhijian Liu, Yujun Lin, Ji~Lin, and Song Han. 2019.
198	\newblock \href {https://arxiv.org/abs/1811.08886} {{HAQ}: Hardware-aware
199	  automated quantization with mixed precision}.
200	\newblock In \emph{CVPR 2019}.
201	
202	\bibitem[{Xia et~al.(2025)Xia, Wu, Li, Wu, Wang, Wang, Li, Singhal, Shah,
203	  Ariyak, Zhuang, Zhou, Athiwaratkun, Zheng, and Song}]{xia2025kitty}
204	Haojun Xia, Xiaoxia Wu, Jisen Li, Robert Wu, Junxiong Wang, Jue Wang, Chenxi
205	  Li, Aman Singhal, Alay~Dilipbhai Shah, Alpay Ariyak, Donglin Zhuang, Zhongzhu
206	  Zhou, Ben Athiwaratkun, Zhen Zheng, and Shuaiwen~Leon Song. 2025.
207	\newblock \href {https://arxiv.org/abs/2511.18643} {{Kitty}: Accurate and
208	  efficient 2-bit {KV} cache quantization with dynamic channel-wise precision
209	  boost}.
210	\newblock \emph{Preprint}, arXiv:2511.18643.
211	\newblock ArXiv preprint.
212	
213	\bibitem[{Xiao et~al.(2024)Xiao, Tian, Chen, Han, and
214	  Lewis}]{xiao2024streamingllm}
215	Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. 2024.
216	\newblock \href {https://arxiv.org/abs/2309.17453} {Efficient streaming
217	  language models with attention sinks}.
218	\newblock In \emph{ICLR 2024}.
219	
220	\bibitem[{Yang et~al.(2024)Yang, Han, Gao, Hu, Zhang, and
221	  Zhao}]{yang2024pyramidinfer}
222	Dongjie Yang, Xiaodong Han, Yan Gao, Yao Hu, Shilin Zhang, and Hai Zhao. 2024.
223	\newblock \href {https://arxiv.org/abs/2405.12532} {{PyramidInfer}: Pyramid
224	  {KV} cache compression for high-throughput {LLM} inference}.
225	\newblock In \emph{Findings of ACL 2024}.
226	
227	\bibitem[{Zhang et~al.(2025)Zhang, Zeng, Peng, Zhuang, and
228	  Chen}]{zhang2025mixkvq}
229	Tao Zhang, Ziqian Zeng, Hao Peng, Huiping Zhuang, and Cen Chen. 2025.
230	\newblock \href {https://arxiv.org/abs/2512.19206} {{MixKVQ}: Query-aware
231	  mixed-precision {KV} cache quantization for long-context reasoning}.
232	\newblock \emph{Preprint}, arXiv:2512.19206.
233	\newblock ArXiv preprint.
234	
235	\bibitem[{Zhang et~al.(2023)Zhang, Sheng, Zhou, Chen, Zheng, Cai, Song, Tian,
236	  R{\'{e}}, Barrett, Wang, and Chen}]{zhang2023h2o}
237	Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai,
238	  Zhao Song, Yuandong Tian, Christopher R{\'{e}}, Clark Barrett, Zhangyang
239	  Wang, and Beidi Chen. 2023.
240	\newblock \href {https://arxiv.org/abs/2306.14048} {{H2O}: Heavy-hitter oracle
241	  for efficient generative inference of large language models}.
242	\newblock In \emph{NeurIPS 2023}.
243	
244	\bibitem[{Zuo et~al.(2026)Zuo, Zhou, Cong, Xi, and Leung}]{zuo2026ratequant}
245	Fei Zuo, Zikang Zhou, Hao Cong, Xiaoyan Xi, and Ho~Fai Leung. 2026.
246	\newblock \href {https://arxiv.org/abs/2605.06675} {{RateQuant}: Optimal
247	  mixed-precision {KV} cache quantization via rate-distortion theory}.
248	\newblock \emph{Preprint}, arXiv:2605.06675.
249	\newblock ArXiv preprint.
250	
251	\end{thebibliography}
252	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93606ce1-0308-4894-aeb7-c430dcc509c9",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "c337a6df-0088-417d-95c4-3e0f129d705f",
  "sourceToolAssistantUUID": "93606ce1-0308-4894-aeb7-c430dcc509c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T10:20:52.864Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016oTEwCT14wotJU6yjVD6eh`</summary>

```json
{
  "pattern": "docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c337a6df-0088-417d-95c4-3e0f129d705f",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BnauN163CG6iojBLDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96f90978-a99c-4963-9755-0526f37e0d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qsjTnuzoUJhrC6fmhu6kC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8628,
      "cache_read_input_tokens": 25315,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 25315,
          "cache_creation_input_tokens": 8628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8628,
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

_source line 22 · 2026-05-15T10:20:52.882Z_

<details><summary>↩ Tool result · `toolu_016oTEwCT14wotJU6yjVD6eh`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96f90978-a99c-4963-9755-0526f37e0d92",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "f1c559cd-d82e-49ed-bf88-73dbbb27baf1",
  "sourceToolAssistantUUID": "96f90978-a99c-4963-9755-0526f37e0d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T10:20:56.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WvYfxeMMiL7WNQCXL7dXaw`</summary>

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
  "parentUuid": "f1c559cd-d82e-49ed-bf88-73dbbb27baf1",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BnvkxbqJUVG2QX8d8E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1468f721-7ccb-438c-81bb-f2d1520608b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVeej94q1QrA8wRzibdbYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6095,
      "cache_read_input_tokens": 33943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 24 · 2026-05-15T10:20:56.536Z_

<details><summary>↩ Tool result · `toolu_01WvYfxeMMiL7WNQCXL7dXaw`</summary>

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
  "parentUuid": "1468f721-7ccb-438c-81bb-f2d1520608b2",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "e5c22494-5a22-4150-bc05-ca34ee5e4177",
  "sourceToolAssistantUUID": "1468f721-7ccb-438c-81bb-f2d1520608b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T10:21:01.848Z_

Now let me look for the related work section in the paper more carefully - the prompt summary said only 3 references but the actual bibliography has 31 entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c22494-5a22-4150-bc05-ca34ee5e4177",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BoCn7htvTBT7rsFQvT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd32225-c778-40be-92cf-22ca0259b18f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XY6WVeeta7A3WNBw6kqhUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5083,
      "cache_read_input_tokens": 40038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5083,
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

_source line 26 · 2026-05-15T10:21:04.407Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QMJ9eL3dnnrvALXyUqdThu`</summary>

```json
{
  "pattern": "\\\\section\\{Related|related.work|\\\\subsection\\{.*[Rr]elated",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd32225-c778-40be-92cf-22ca0259b18f",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BoCn7htvTBT7rsFQvT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75530dff-5109-4145-8595-34f1d18b7080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XY6WVeeta7A3WNBw6kqhUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5083,
      "cache_read_input_tokens": 40038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5083,
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

_source line 27 · 2026-05-15T10:21:04.429Z_

<details><summary>↩ Tool result · `toolu_01QMJ9eL3dnnrvALXyUqdThu`</summary>

```text
docs/paper/main.fls:237:INPUT ./related_work.tex
docs/paper/main.fls:238:INPUT ./related_work.tex
docs/paper/main.fls:239:INPUT ./related_work.tex
docs/paper/main.fls:240:INPUT ./related_work.tex
docs/paper/main.fls:241:INPUT related_work.tex
docs/paper/related_work.tex:1:\section{Related Work}\label{sec:related_work}
docs/paper/main.tex:23:\input{related_work}
docs/paper/main.log:594:) (./related_work.tex
docs/paper/main.fdb_latexmk:166:  "related_work.tex" 1778823328.36582 4547 9d31c31c8ed32851b0b96059d0569706 ""
docs/paper/main.aux:191:\newlabel{sec:related_work}{{2}{2}{Related Work}{section.2}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75530dff-5109-4145-8595-34f1d18b7080",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "edfcfb4b-857d-4e74-8948-af0473419685",
  "sourceToolAssistantUUID": "75530dff-5109-4145-8595-34f1d18b7080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T10:21:04.890Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DnPDVhC4TZVsMHgB1YRUu3`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edfcfb4b-857d-4e74-8948-af0473419685",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4BoCn7htvTBT7rsFQvT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3146369-b5fb-4b7a-b5fe-374ef869773e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XY6WVeeta7A3WNBw6kqhUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5083,
      "cache_read_input_tokens": 40038,
      "output_tokens": 253,
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
          "output_tokens": 253,
          "cache_read_input_tokens": 40038,
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

_source line 29 · 2026-05-15T10:21:04.909Z_

<details><summary>↩ Tool result · `toolu_01DnPDVhC4TZVsMHgB1YRUu3`</summary>

```text
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3146369-b5fb-4b7a-b5fe-374ef869773e",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "56044cd1-7984-47a8-955e-c6b1e29f9cd5",
  "sourceToolAssistantUUID": "d3146369-b5fb-4b7a-b5fe-374ef869773e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T10:21:07.621Z_

<details open><summary>🔧 Tool call — Read · `toolu_012iyvikBRtwbEipLrBpaDwY`</summary>

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
  "parentUuid": "56044cd1-7984-47a8-955e-c6b1e29f9cd5",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bop8NrkZLzVoc9ERFG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bd1a986-c1d3-4417-bede-ee22ef790695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QhQ3gDZ6FgZ1cPbeRtFi7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 45121,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 635,
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

_source line 31 · 2026-05-15T10:21:07.626Z_

<details><summary>↩ Tool result · `toolu_012iyvikBRtwbEipLrBpaDwY`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, sliding-window adaptation~\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\cite{su2025rotatekv}, 2-bit with adaptive token retention~\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\cite{shutova2025aquakv}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
10	
11	
12	\paragraph{Mixed-Precision Quantization (Weights).}
13	Mixed-precision allocation has a long history at the weight level.
14	HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.
15	These methods establish that non-uniform bit-width allocation is effective when per-component sensitivity is heterogeneous; we transfer this insight from weights to the KV cache at per-head granularity, where heterogeneity is empirically much larger (\S\ref{sec:heterogeneity}).
16	
17	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
18	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.
19	On hardware-aligned $\{2,4,8,16\}$, the 4$\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.
20	Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 11.23 PPL at the same average bit-width (Table~\ref{tab:solver_equiv}).
21	The constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.
22	Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\cite{xia2025kitty}, token-level via a learned on-device controller~\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\cite{lei2026arkv}---at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
23	
24	\paragraph{Attention Head Analysis.}
25	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
26	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bd1a986-c1d3-4417-bede-ee22ef790695",
  "isSidechain": true,
  "promptId": "72a72832-24b4-4443-81c2-ec287c3d9f30",
  "agentId": "aedb1b6d5c3ff160a",
  "type": "user",
  "uuid": "5e88c7ef-49f5-4bc8-bec7-af748005ba29",
  "sourceToolAssistantUUID": "2bd1a986-c1d3-4417-bede-ee22ef790695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T10:22:31.989Z_

Now I have a comprehensive view of the paper. Let me construct the review.

---

## Review: "The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization"

**Reviewer R2 -- Focus: Novelty and Related Work**

---

### 1. Novelty Assessment

**Contribution 1: Cardinality constraint on 2-bit assignments.**

The core technical idea is: cap the number of heads assigned to 2-bit quantization. This is framed as a "minimal sufficient fix" for catastrophic failure in unconstrained MCKP solvers on hardware-aligned bit-widths. While the *diagnosis* of the failure mode (super-additive compounding of 2-bit errors through the residual stream) is a useful observation, the *fix* -- adding a cardinality bound -- is an obvious engineering response once the problem is identified. Capping the count of the most aggressive quantization level is standard practice in mixed-precision compression; the HAWQ line of work already constrains per-layer budgets to avoid catastrophic loss from over-aggressive assignment, and HAQ explicitly enforces hardware-aware constraints. The novelty lies more in documenting that this specific failure mode exists on hardware-aligned bit-widths than in the constraint itself. **Moderate novelty.**

**Contribution 2: Systematic negative result (5/6 models show no benefit).**

This is the most interesting finding, but its value is undercut by several factors: (a) the paper tests only five architectures at one scale (7-9B), all with GQA, so the "systematic" claim is overstated; (b) the result that non-uniform allocation rarely helps over uniform is not especially surprising -- KIVI and KVQuant already achieve strong results with uniform quantization, and the community's general experience is that 4-bit KV cache quantization is near-lossless for most models, leaving little room for mixed-precision gains; (c) the "spread vs. spike vs. flat" taxonomy is fit to N=5 data points with the beneficial category containing N=1 (Qwen2.5-7B only), which the authors acknowledge. A decision rule validated on one positive example is an anecdote, not a diagnostic. **Low-to-moderate novelty.**

**Contribution 3: Compounding effect characterization with U-shaped PPL-k curve.**

The U-shaped curve showing that a few 2-bit heads help but too many hurt is intuitive and well-presented. However, the super-additivity characterization (Table in Section 3.3) is thin: it is shown for one model (Qwen2.5-7B), lacks formal modeling (no quantitative model of compounding is proposed), and the non-monotonic behavior and high variance acknowledged in the appendix weaken the claim. RateQuant already acknowledges compounding in its Appendix M. The contribution is documenting the phenomenon with somewhat more care, but the depth of analysis is insufficient for a standalone contribution. **Low novelty.**

---

### 2. Related Work Completeness

**The task prompt stated the related work section has only 3 references. This is incorrect.** The actual related work section (Section 2, `related_work.tex`) is comprehensive, citing 31 references across five well-structured paragraphs covering:

- Uniform KV cache quantization (KIVI, KVQuant, QServe, ZipCache, GEAR, SKVQ, RotateKV, MiniKV, AQuA-KV)
- KV cache eviction (H2O, SnapKV, FastGen, Scissorhands, StreamingLLM, PyramidInfer, HeadKV, Ada-KV)
- Mixed-precision weight quantization (HAWQ, HAWQ-V2, HAQ, SqueezeLLM)
- Mixed-precision KV rate-distortion (RateQuant, KVmix, KVTuner, PM-KVQ, Kitty, Don't Waste Bits, ARKV, MixKVQ)
- Attention head analysis (Voita et al., Michel et al.)

This is a well-organized related work section for a workshop or short paper. For a top venue, there are a few gaps worth noting:

- **Missing:** AWQ (Lin et al. 2024), GPTQ (Frantar et al. 2023), and SpQR (Dettmers et al. 2023) as foundational mixed-precision/outlier-aware weight quantization methods. While the paper focuses on KV cache, citing these establishes the broader mixed-precision lineage.
- **Missing:** Atom (Zhao et al. 2024) for mixed-precision KV-cache-aware serving with quantization.
- **Missing:** FlexGen (Sheng et al. 2023) for offloading + KV cache compression strategy.
- **AQLM/QuIP#:** Not cited, though these are primarily weight quantization methods and their omission is more defensible.

The positioning against RateQuant is fair and technically specific (polymatroid breakdown on non-consecutive sets). The positioning against HAWQ/HAQ is appropriate. Overall, the related work is **adequate but could be slightly strengthened** with 2-3 more system-level references.

---

### 3. Contribution Significance

The paper's practical impact is limited. The actionable takeaway is: "for most models, just use uniform 4-bit KV cache quantization." This is already the default practice. The one model where non-uniform helps (Qwen2.5-7B) shows a genuine 27.3% PPL improvement, but:

- This improvement is specific to one model family at one scale
- The paper's own scaling analysis (Qwen 7B -> 14B -> 72B) suggests the spread pattern diminishes at larger scales, making this a "small model artifact"
- No production kernel benchmarks are provided (the 8.5% PyTorch-level overhead is acknowledged as an upper bound)
- The downstream task improvements (+2.6 pts average on Qwen) are meaningful but only for the single beneficial case

**Who benefits?** Practitioners who already profile per-head sensitivity will learn that adding a cardinality constraint is important. Researchers studying KV cache quantization get a useful negative result about the limits of non-uniform allocation. The impact is narrow.

---

### 4. Framing and Narrative

**Title:** "The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization" oversells. For 5/6 models, you don't need the constraint because you don't need non-uniform allocation at all. A more accurate title would emphasize the negative finding.

**Narrative tension:** The paper is structured around solving a problem (unconstrained MCKP catastrophe) that it then shows is largely irrelevant (most models don't benefit from non-uniform allocation). This creates an awkward arc: the reader is drawn into an optimization story, only to learn the optimization doesn't matter most of the time. The "systematic negative result" framing is buried; it should be the headline.

**Strengths of framing:** The spread/spike/flat taxonomy is intuitive and well-visualized. The solver equivalence result is clean and practically useful. The honesty about N=1 spread validation is commendable.

**Weakness of framing:** The paper cannot decide whether it is (a) proposing a method (cardinality-constrained MCKP), (b) reporting a negative result, or (c) characterizing a phenomenon (compounding). Each of these individually is thin for a top venue; combining them gives breadth but not depth.

---

### 5. Strengths

- **Thorough empirical coverage**: Five architectures, multiple profiling resolutions, cross-dataset validation, multi-seed stability, oracle comparison, K/V separation ablation, downstream evaluation, budget sweep, aggressive compression analysis. The experimental rigor is high for the scope.

- **Honest reporting of negative results**: The paper does not hide that 4/5 models show no benefit. The limitations section is unusually self-aware (N=1 spread, no production kernels, single evaluation dataset, scale limitations).

- **Clean solver equivalence result**: Demonstrating that constrained greedy = MCKP (with only 1/624 head disagreement across architectures) is a neat finding that simplifies practitioners' choices.

- **Useful spread/spike/flat taxonomy**: Even though N=1 for spread, the conceptual framework for thinking about when non-uniform quantization helps is a useful contribution to the community's mental model.

- **Reproducibility signals are strong**: Detailed profiling protocols, specific k values per model, multi-seed variance reported, cross-dataset agreement percentages. The paper would be straightforward to reproduce.

---

### 6. Weaknesses

- **N=1 validation of the core positive claim**: The only model where non-uniform allocation helps is Qwen2.5-7B. The decision rule is fit to 5 data points with 1 positive example. The thresholds (concentration > 0.50, t1/t5 < 0.70) are inevitably overfit. The paper acknowledges this but does not adequately address it -- e.g., no ablation across Qwen variants beyond the brief 14B/72B profiling-only analysis, no models from other "spread-like" families (e.g., Falcon, MPT, older GPT-NeoX variants).

- **Compounding analysis lacks depth**: The super-additivity claim is supported by a single sweep on Qwen2.5-7B. No mechanistic explanation is offered for *why* 2-bit errors compound (residual stream saturation is hypothesized but not tested -- e.g., by measuring activation norm growth or attention entropy degradation). The non-monotonic behavior and variance in the compounding data are not explained. For a contribution claiming to "characterize" compounding, this is insufficient.

- **No real inference benchmarks**: The paper proposes hardware-aligned bit-widths as the motivation but provides only PyTorch-level simulation latency. Without integration with vLLM, TensorRT-LLM, or SGLang showing actual memory savings and throughput improvements, the practical impact claim is unsupported. The 8.5% mixed-precision overhead (Table 7) is concerning even if characterized as an upper bound.

- **Scale limitation undermines generality**: All primary experiments are at 7-9B scale. The Qwen family scaling analysis (7B -> 14B -> 72B) is suggestive that the spread pattern is a small-model artifact, which, if true, further limits the paper's relevance since production deployment increasingly targets 70B+ models. The 72B experiment is profiling-only with no allocation results.

- **Negative result is not sufficiently contextualized**: The paper doesn't explain *why* most models have flat or spike sensitivity distributions. Is this a consequence of training procedure, architecture choices (GQA ratio, attention variant), or model scale? Without this analysis, the negative result is a collection of data points rather than an insight. The paper also doesn't compare against recent per-head methods like HeadKV or Ada-KV to establish whether the negative result extends to eviction-based approaches.

---

### 7. Questions for Authors

1. **On generality of spread pattern**: The paper shows that the spread pattern appears only in Qwen2.5-7B and that it diminishes at 14B/72B scale. Have you tested any non-Qwen models that exhibit spread? If the phenomenon is Qwen-specific and scale-dependent, can the cardinality constraint claim to be a general contribution?

2. **On compounding mechanism**: You hypothesize that 2-bit errors compound through the residual stream. Can you provide direct evidence -- e.g., measuring the ratio of quantization noise to signal norm across layers as a function of k, or showing that the compounding correlates with specific architectural features (number of residual stream write points, layer normalization placement)?

3. **On practical deployment**: Given the 8.5% PyTorch-level overhead and the absence of production kernel benchmarks, what evidence supports the claim that this approach would be beneficial in practice? Have you considered that the 27.3% PPL improvement on Qwen2.5-7B might not offset the engineering cost of implementing mixed-precision KV cache dispatch in production systems?

4. **On the decision rule**: The concentration and t1/t5 thresholds are derived from 5 data points. How sensitive is the classification to threshold perturbation? For example, if the concentration threshold were 0.55 instead of 0.50, would Llama-3.1-8B (concentration 0.57) be misclassified?

5. **On comparison to existing mixed-precision KV methods**: KVTuner (ICML 2025) operates at layer granularity with hardware-aware constraints. How does your per-head approach compare to KVTuner on the same models and budgets? This comparison is conspicuously absent despite KVTuner being cited.

---

### 8. Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4 (High)**

**Justification**: The paper is competently executed with thorough experiments and honest reporting, but the contributions do not clear the novelty bar for a 25% acceptance rate venue. The cardinality constraint is an incremental engineering fix rather than a conceptual advance. The negative result -- while interesting -- is validated on too few architectures to be "systematic" and lacks the analytical depth to explain *why* the result holds. The compounding characterization is shallow. The single positive example (Qwen2.5-7B at 7B scale, diminishing at 14B/72B) makes the practical impact very narrow. The paper would be a good fit for a workshop or a shorter format where the honest negative result and the diagnostic framework could be appreciated without requiring the depth expected at a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e88c7ef-49f5-4bc8-bec7-af748005ba29",
  "isSidechain": true,
  "agentId": "aedb1b6d5c3ff160a",
  "requestId": "req_011Cb4Bp1rKYRdFjBbvEkYwx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce4c78aa-e567-4e0e-8710-8d1592035cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "af5be026-45b4-485f-8fe9-8a4510800ce5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rceubfi7PiMzNVc86uEuGk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 45756,
      "output_tokens": 3245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3245,
          "cache_read_input_tokens": 45756,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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
