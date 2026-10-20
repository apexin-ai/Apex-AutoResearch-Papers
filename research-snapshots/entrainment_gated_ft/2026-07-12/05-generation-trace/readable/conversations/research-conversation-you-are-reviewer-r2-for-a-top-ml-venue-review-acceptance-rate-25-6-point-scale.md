# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac2238362768c5015.jsonl`
- **Structured JSON:** [`a590824fd88b138e932f.json`](../../sessions/a5/a590824fd88b138e932f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-15T10:13:46.072Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **novelty and related work**.

## Paper Summary
"When Does Non-Uniform KV Cache Quantization Help?" — A 9-page paper studying per-head mixed-precision KV cache quantization across 6 transformer architectures (Qwen2.5-7B/14B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B). Three contributions:
1. **Cardinality constraint** (max_2bit ≤ k) as universal fix — prevents compounding degradation on all 6 architectures, makes greedy = MCKP (Δ=0.0000).
2. **Sensitivity distribution taxonomy** — Spread/Spike/Flat shapes predict whether MCKP exploits heterogeneity.
3. **Empirical decision rule** — joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70) classifies 5/5 non-borderline architectures correctly; 6th (Qwen-14B) is boundary case with modest 7.9% benefit.

## Key Details
- Method: Per-head 2-bit distortion delta profiling (one head at 2-bit, rest at 4-bit). Two summary stats: top-5% concentration (c₅) and t₁/t₅ ratio. MCKP with cardinality constraint on 2-bit assignments.
- Hardware-aligned bit-widths: {2, 4, 8, 16} (non-consecutive)
- Budget: 0.25 (4× compression)
- Eval: WikiText-2 PPL + 4 downstream tasks (ARC-C, HellaSwag, PIQA, WinoGrande)
- Key finding: Constraint is universal (works on all 6 models). Diagnostic is architecture-dependent. Only Qwen-7B shows strong benefit (+27.3%); 14B shows modest benefit (+7.9%); others show ≤0.2% or negative.

## Paper Structure (9 pages)
- Abstract, Intro (2 pages), Method (1 page — profiling, MCKP, constraint, decision rule), Experiments (5 pages — 14B profiling, k-ablation, unconstrained vs constrained, Gemma-2 BOS fix, decision rule validation, cross-arch summary, downstream, compounding, solver equivalence), Analysis (1 page), Conclusion with limitations (1 page).
- No Related Work section at all.
- No references/bibliography visible in the PDF.

## Your Task
Produce a structured review covering:

### 1. Novelty Assessment
- **Cardinality constraint**: How novel is adding a cardinality constraint to MCKP? This is a standard technique in combinatorial optimization. The contribution is more "we discovered this is needed" than "we invented a new method."
- **Sensitivity profiling**: Per-head sensitivity analysis is used in KIVI, KVQuant, RateQuant, and other prior work. What's new here is the taxonomy (Spread/Spike/Flat) and the two-metric decision rule.
- **Decision rule**: Fitting a 2-threshold rule to 6 data points — is this a "contribution" or just a pattern observation? The thresholds are acknowledged as soft boundaries. With N=6 architectures and N=1 strong positive, how generalizable can this be?
- **Overall**: Is this a methods paper, an empirical study, or both? The method itself (constraint + MCKP) is thin; the value is in the systematic empirical investigation.

### 2. Related Work / Positioning
- **CRITICAL**: The paper has NO Related Work section and NO bibliography/references visible. For a venue like EMNLP/NeurIPS/ICML, this is a major formatting issue. 
- The intro mentions "greedy R-D solver of RateQuant" and "integer-programming formulations (MCKP)" but doesn't cite them.
- Missing comparisons with: KIVI (per-channel KV quantization), GEAR (low-rank + quantization), KVQuant (per-head sensitivity-aware), QServe (W4A8KV4 serving), SqueezeLLM, QuIP#, and other recent KV cache compression methods.
- The paper doesn't position itself against token-level KV cache compression (eviction, H2O, SnapKV, etc.) — mentioned only in future work.
- No discussion of how the profiling cost compares to alternatives.

### 3. Significance / Impact
- Who would use this? Practitioners deploying LLMs who want to know if mixed-precision KV cache quantization is worth the profiling overhead.
- Is the cardinality constraint alone sufficient as a contribution? It's useful but arguably incremental — it's one hyperparameter added to existing solvers.
- The diagnostic is interesting but N=6 is thin for a "framework."
- The honest treatment of limitations is commendable but also highlights how narrow the positive evidence is (N=1 strong, N=1 boundary, N=4 non-beneficial).

### 4. Writing Quality
- Clear and well-organized
- Tables are informative
- The "boundary case" treatment of 14B is mature scientific writing
- Missing: figures (only tables), related work, references

### 5. Key Weaknesses (be specific)
- No Related Work section
- No bibliography/references
- Novelty is primarily empirical — the method contributions are incremental
- N=1 strong positive severely limits the generalizability claim
- No comparison with ANY existing method beyond uniform baseline
- The paper essentially argues "our method sometimes helps, mostly doesn't" — hard to accept at a top venue

### 6. Key Strengths
- Systematic and thorough empirical study
- Honest about limitations (refreshingly so for an ML paper)
- Practical takeaway (use the constraint, check two metrics)
- Good taxonomy of sensitivity distributions

### 7. Preliminary Score and Confidence
Give: Score (1-6), Confidence (1-5), and 2-3 sentence justification.

Output your full review in markdown format. Be thorough but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "66ab6cc4-f5a6-431c-ad92-cf4059bd6837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T10:13:46.076Z_

```json
{
  "parentUuid": "66ab6cc4-f5a6-431c-ad92-cf4059bd6837",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
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
  "uuid": "0cd45c00-2c11-49c7-b71f-998bf054ebd1",
  "timestamp": "2026-05-15T10:13:46.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-15T10:13:49.214Z_



I'll start by reading the paper files to give a thorough, evidence-based review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd45c00-2c11-49c7-b71f-998bf054ebd1",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFTpc7eDCKoRRdnNGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a356f53-3f8c-44f0-83ab-26f8b5cf3161",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iQ4W4uDYfnA6Y7bbiiAhC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7344,
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

_source line 4 · 2026-05-15T10:13:50.081Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QYQC9vmfGi56b13312FJqD`</summary>

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
  "parentUuid": "7a356f53-3f8c-44f0-83ab-26f8b5cf3161",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFTpc7eDCKoRRdnNGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05d9fd7b-e628-459a-ac99-87b6359b94cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iQ4W4uDYfnA6Y7bbiiAhC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7344,
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

### Tool result

_source line 5 · 2026-05-15T10:13:50.088Z_

<details><summary>↩ Tool result · `toolu_01QYQC9vmfGi56b13312FJqD`</summary>

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
  "parentUuid": "05d9fd7b-e628-459a-ac99-87b6359b94cd",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "524359ae-a293-48f3-adf0-0593275f4c5a",
  "sourceToolAssistantUUID": "05d9fd7b-e628-459a-ac99-87b6359b94cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T10:13:51.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JXm5dFR4QizySMkDd5ZN5b`</summary>

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
  "parentUuid": "524359ae-a293-48f3-adf0-0593275f4c5a",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFTpc7eDCKoRRdnNGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "528ca612-961c-42da-aff7-9da5d6170d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iQ4W4uDYfnA6Y7bbiiAhC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7344,
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

### Tool result

_source line 7 · 2026-05-15T10:13:51.005Z_

<details><summary>↩ Tool result · `toolu_01JXm5dFR4QizySMkDd5ZN5b`</summary>

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
  "parentUuid": "528ca612-961c-42da-aff7-9da5d6170d20",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "67a4c5a4-a453-4087-b51a-f3e75c507f41",
  "sourceToolAssistantUUID": "528ca612-961c-42da-aff7-9da5d6170d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T10:13:51.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SP8qjwwoT6sU8tahdeF2Vc`</summary>

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
  "parentUuid": "67a4c5a4-a453-4087-b51a-f3e75c507f41",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFTpc7eDCKoRRdnNGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b31f014f-c5dc-4e71-9150-7f16fea765eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iQ4W4uDYfnA6Y7bbiiAhC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 9160,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7344
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 242,
          "cache_read_input_tokens": 9160,
          "cache_creation_input_tokens": 7344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7344,
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

_source line 9 · 2026-05-15T10:13:51.268Z_

<details><summary>↩ Tool result · `toolu_01SP8qjwwoT6sU8tahdeF2Vc`</summary>

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
  "parentUuid": "b31f014f-c5dc-4e71-9150-7f16fea765eb",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "be8a48b0-f81e-4ee2-8bc6-40cadd3b5561",
  "sourceToolAssistantUUID": "b31f014f-c5dc-4e71-9150-7f16fea765eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T10:13:55.126Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ABTVRU5HtcxjC1kCeVJVTn`</summary>

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
  "parentUuid": "be8a48b0-f81e-4ee2-8bc6-40cadd3b5561",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFrCziVCNnz7RceC76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15098bac-5632-41e3-9f04-40eb7af8e500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xyct57gx66MEXGWUoJhnCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6489,
      "cache_read_input_tokens": 16504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6489,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 11 · 2026-05-15T10:13:55.133Z_

<details><summary>↩ Tool result · `toolu_01ABTVRU5HtcxjC1kCeVJVTn`</summary>

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
  "parentUuid": "15098bac-5632-41e3-9f04-40eb7af8e500",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "4961b8d8-a6fa-4e0b-b89e-9dd93c0c1ceb",
  "sourceToolAssistantUUID": "15098bac-5632-41e3-9f04-40eb7af8e500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T10:13:55.605Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EQyJyPfHUHE35xyuNCj3Bw`</summary>

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
  "parentUuid": "4961b8d8-a6fa-4e0b-b89e-9dd93c0c1ceb",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFrCziVCNnz7RceC76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50164c2d-26ec-41c8-9b9f-eaedf47a10ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xyct57gx66MEXGWUoJhnCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6489,
      "cache_read_input_tokens": 16504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6489,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 13 · 2026-05-15T10:13:55.609Z_

<details><summary>↩ Tool result · `toolu_01EQyJyPfHUHE35xyuNCj3Bw`</summary>

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
  "parentUuid": "50164c2d-26ec-41c8-9b9f-eaedf47a10ba",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "ed929b74-6a86-4f32-b167-ec4db507c4e2",
  "sourceToolAssistantUUID": "50164c2d-26ec-41c8-9b9f-eaedf47a10ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T10:13:55.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_013DYEt78xHrAF9rCVzf3JMe`</summary>

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
  "parentUuid": "ed929b74-6a86-4f32-b167-ec4db507c4e2",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BFrCziVCNnz7RceC76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a999b29a-b239-430a-8bf9-0ecd22e61832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xyct57gx66MEXGWUoJhnCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6489,
      "cache_read_input_tokens": 16504,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6489
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 16504,
          "cache_creation_input_tokens": 6489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6489,
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

_source line 15 · 2026-05-15T10:13:55.977Z_

<details><summary>↩ Tool result · `toolu_013DYEt78xHrAF9rCVzf3JMe`</summary>

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
  "parentUuid": "a999b29a-b239-430a-8bf9-0ecd22e61832",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "7cc22073-c298-4dd3-b76f-2d1ed8499b07",
  "sourceToolAssistantUUID": "a999b29a-b239-430a-8bf9-0ecd22e61832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T10:14:00.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_011PHS732eE5xm7wyd7iwueE`</summary>

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
  "parentUuid": "7cc22073-c298-4dd3-b76f-2d1ed8499b07",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGCbb8FMzqP4CTJ2YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e751ef47-ff6c-4af5-ac50-3ac7d5709150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rSJuZAQV9oqYvXRgvppFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6336,
      "cache_read_input_tokens": 22993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6336,
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

_source line 17 · 2026-05-15T10:14:00.375Z_

<details><summary>↩ Tool result · `toolu_011PHS732eE5xm7wyd7iwueE`</summary>

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
  "parentUuid": "e751ef47-ff6c-4af5-ac50-3ac7d5709150",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "e6f88909-27eb-4261-8ec9-13c3aab25a50",
  "sourceToolAssistantUUID": "e751ef47-ff6c-4af5-ac50-3ac7d5709150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T10:14:01.136Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014RNZjNvr1u3DjcHBBYhEWN`</summary>

```json
{
  "pattern": "docs/paper/main.bbl",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f88909-27eb-4261-8ec9-13c3aab25a50",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGCbb8FMzqP4CTJ2YW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a45528a-93a4-48ae-9a3e-cfb720596bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rSJuZAQV9oqYvXRgvppFm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6336,
      "cache_read_input_tokens": 22993,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6336
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 22993,
          "cache_creation_input_tokens": 6336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6336,
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

_source line 19 · 2026-05-15T10:14:01.157Z_

<details><summary>↩ Tool result · `toolu_014RNZjNvr1u3DjcHBBYhEWN`</summary>

```text
docs/paper/main.bbl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a45528a-93a4-48ae-9a3e-cfb720596bdf",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "120dc196-840b-43a1-8d5d-076687bb1b6b",
  "sourceToolAssistantUUID": "2a45528a-93a4-48ae-9a3e-cfb720596bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T10:14:05.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WpaRJZrE77CViSYHmarPYT`</summary>

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
  "parentUuid": "120dc196-840b-43a1-8d5d-076687bb1b6b",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGae9XipHisbi3MCho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "605322cd-eb50-4cd3-8e52-64795fb35b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBB7gfWQKBzh51GxDPDMqa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5122,
      "cache_read_input_tokens": 29329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5122,
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

_source line 21 · 2026-05-15T10:14:05.357Z_

<details><summary>↩ Tool result · `toolu_01WpaRJZrE77CViSYHmarPYT`</summary>

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
  "parentUuid": "605322cd-eb50-4cd3-8e52-64795fb35b71",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "5977d116-12a3-45cf-8b8f-c0621b6a7371",
  "sourceToolAssistantUUID": "605322cd-eb50-4cd3-8e52-64795fb35b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T10:14:05.855Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016szDuNgGhtbimxgEKo4ScR`</summary>

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
  "parentUuid": "5977d116-12a3-45cf-8b8f-c0621b6a7371",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGae9XipHisbi3MCho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc19f35-fb5b-4b13-b5b9-3787c0e8a791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBB7gfWQKBzh51GxDPDMqa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5122,
      "cache_read_input_tokens": 29329,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 29329,
          "cache_creation_input_tokens": 5122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5122,
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

_source line 23 · 2026-05-15T10:14:05.875Z_

<details><summary>↩ Tool result · `toolu_016szDuNgGhtbimxgEKo4ScR`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc19f35-fb5b-4b13-b5b9-3787c0e8a791",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "2210eede-64f9-4d44-81a6-cfa714c0d118",
  "sourceToolAssistantUUID": "bcc19f35-fb5b-4b13-b5b9-3787c0e8a791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T10:14:09.518Z_

Now let me check the main.tex to see if references are properly included and look at the paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2210eede-64f9-4d44-81a6-cfa714c0d118",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGvahzAvdWdoSbXfHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62d3227f-55a4-4b51-a87c-41bf54f1b80a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011LoTTQ2LgrKB4cPkxqfX8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6082,
      "cache_read_input_tokens": 34451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6082,
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

_source line 25 · 2026-05-15T10:14:10.959Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VCPLm6w91LiHc8PPW2EM4d`</summary>

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
  "parentUuid": "62d3227f-55a4-4b51-a87c-41bf54f1b80a",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BGvahzAvdWdoSbXfHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bac9c6f8-9e49-4f44-9403-5231cc182548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011LoTTQ2LgrKB4cPkxqfX8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6082,
      "cache_read_input_tokens": 34451,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 34451,
          "cache_creation_input_tokens": 6082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6082,
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

_source line 26 · 2026-05-15T10:14:10.985Z_

<details><summary>↩ Tool result · `toolu_01VCPLm6w91LiHc8PPW2EM4d`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac9c6f8-9e49-4f44-9403-5231cc182548",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "f0f82de0-c720-4548-9e6c-eafe08ef923a",
  "sourceToolAssistantUUID": "bac9c6f8-9e49-4f44-9403-5231cc182548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T10:14:13.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_019bDT7BhMqZ9VeCZhzAM9Si`</summary>

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
  "parentUuid": "f0f82de0-c720-4548-9e6c-eafe08ef923a",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BHJTqcZkm5j4835aD9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1cbf25f-09b4-4942-bf77-881764440565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nyDEgap2Sku2kqBsCpPo8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 40533,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 40533,
          "cache_creation_input_tokens": 141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 141,
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

_source line 28 · 2026-05-15T10:14:13.601Z_

<details><summary>↩ Tool result · `toolu_019bDT7BhMqZ9VeCZhzAM9Si`</summary>

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
  "parentUuid": "b1cbf25f-09b4-4942-bf77-881764440565",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "5cb15c15-db40-4ea4-9764-2eb0d3174775",
  "sourceToolAssistantUUID": "b1cbf25f-09b4-4942-bf77-881764440565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T10:14:16.302Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KZZ1oF7eER4BeQxTfCuhix`</summary>

```json
{
  "pattern": "docs/paper/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb15c15-db40-4ea4-9764-2eb0d3174775",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BHVmUzjm1NzhFRhX69",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89aa2ead-095e-4ff5-9644-a03136306327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2kdTzno59raDBjDTFXCr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 40674,
      "output_tokens": 101,
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
          "output_tokens": 101,
          "cache_read_input_tokens": 40674,
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

_source line 30 · 2026-05-15T10:14:16.320Z_

<details><summary>↩ Tool result · `toolu_01KZZ1oF7eER4BeQxTfCuhix`</summary>

```text
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89aa2ead-095e-4ff5-9644-a03136306327",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "a88fc46e-719b-4ec1-bcd1-c4b8906533ac",
  "sourceToolAssistantUUID": "89aa2ead-095e-4ff5-9644-a03136306327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T10:14:19.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GnKx2AxdbRTp8f9Ey1vdcS`</summary>

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
  "parentUuid": "a88fc46e-719b-4ec1-bcd1-c4b8906533ac",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BHhL1mtidhu2Ewod7j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40d178f3-6702-48ec-9272-0d10f0d369d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3sB7MHi4KVLevHcrSXNas",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 122,
      "cache_read_input_tokens": 41064,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 41064,
          "cache_creation_input_tokens": 122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 122,
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

_source line 32 · 2026-05-15T10:14:19.888Z_

<details><summary>↩ Tool result · `toolu_01GnKx2AxdbRTp8f9Ey1vdcS`</summary>

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
  "parentUuid": "40d178f3-6702-48ec-9272-0d10f0d369d4",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "be57d1b4-dc97-477d-9607-ba06dfba7422",
  "sourceToolAssistantUUID": "40d178f3-6702-48ec-9272-0d10f0d369d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T10:14:24.134Z_

Good -- the paper does have a Related Work section and bibliography. The initial task description was partially incorrect about "NO Related Work section" and "NO bibliography." Let me now also check the PDF to see if there's a compilation issue that might have caused references to be missing in the rendered PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be57d1b4-dc97-477d-9607-ba06dfba7422",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BHxmSxQ913odw9gmDv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0795c06-bece-4bd0-bfe5-58f2995a5093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBcuV9rcGZxnuwyEFFonFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 41186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 34 · 2026-05-15T10:14:24.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_017bD7epWToeqkX5Y7VHqjMw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.log",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0795c06-bece-4bd0-bfe5-58f2995a5093",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BHxmSxQ913odw9gmDv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2b01144-51ea-4bfc-844a-7fb377e754ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBcuV9rcGZxnuwyEFFonFo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 41186,
      "output_tokens": 163,
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
          "output_tokens": 163,
          "cache_read_input_tokens": 41186,
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

### Tool result

_source line 35 · 2026-05-15T10:14:24.725Z_

<details><summary>↩ Tool result · `toolu_017bD7epWToeqkX5Y7VHqjMw`</summary>

```text
1	This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  15 MAY 2026 09:35
2	entering extended mode
3	 restricted \write18 enabled.
4	 %&-line parsing enabled.
5	**main.tex
6	(./main.tex
7	LaTeX2e <2025-11-01>
8	L3 programming layer <2026-01-19>
9	(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
10	Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
11	(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo
12	File: size11.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
13	)
14	\c@part=\count275
15	\c@section=\count276
16	\c@subsection=\count277
17	\c@subsubsection=\count278
18	\c@paragraph=\count279
19	\c@subparagraph=\count280
20	\c@figure=\count281
21	\c@table=\count282
22	\abovecaptionskip=\skip49
23	\belowcaptionskip=\skip50
24	\bibindent=\dimen148
25	) (./acl.sty
26	Conference Style for ACL
27	(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
28	Package: xcolor 2024/09/29 v3.02 LaTeX color extensions (UK)
29	
30	(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg
31	File: color.cfg 2016/01/02 v1.6 sample color configuration
32	)
33	Package xcolor Info: Driver file: pdftex.def on input line 274.
34	
35	(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def
36	File: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex
37	)
38	(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx)
39	Package xcolor Info: Model `cmy' substituted by `cmy0' on input line 1349.
40	Package xcolor Info: Model `hsb' substituted by `rgb' on input line 1353.
41	Package xcolor Info: Model `RGB' extended on input line 1365.
42	Package xcolor Info: Model `HTML' substituted by `rgb' on input line 1367.
43	Package xcolor Info: Model `Hsb' substituted by `hsb' on input line 1368.
44	Package xcolor Info: Model `tHsb' substituted by `hsb' on input line 1369.
45	Package xcolor Info: Model `HSB' substituted by `hsb' on input line 1370.
46	Package xcolor Info: Model `Gray' substituted by `gray' on input line 1371.
47	Package xcolor Info: Model `wave' substituted by `hsb' on input line 1372.
48	)
49	(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
50	Package: lineno 2025/05/13 line numbers on paragraphs v5.5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b01144-51ea-4bfc-844a-7fb377e754ae",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "e8a6eaa6-7eec-4689-b878-49d700d62cc2",
  "sourceToolAssistantUUID": "c2b01144-51ea-4bfc-844a-7fb377e754ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T10:14:28.117Z_

Now I have enough information to write the review. Let me also quickly check Qwen-14B references since the task summary mentions it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8a6eaa6-7eec-4689-b878-49d700d62cc2",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BJK5pf81ffVJz7trLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3712fb0f-4c6d-434c-b14b-0a8f49c04ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc73mZ7Dp88fm8dFdEeu9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 42647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 37 · 2026-05-15T10:14:29.033Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0191VS5XWW8zvztwesE7GzJm`</summary>

```json
{
  "pattern": "14B|Qwen2\\.5-14",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3712fb0f-4c6d-434c-b14b-0a8f49c04ef2",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BJK5pf81ffVJz7trLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffc89317-2bb3-4bc9-92fa-3d84f015b7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc73mZ7Dp88fm8dFdEeu9z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 42647,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 42647,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1119,
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

_source line 38 · 2026-05-15T10:14:29.070Z_

<details><summary>↩ Tool result · `toolu_0191VS5XWW8zvztwesE7GzJm`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffc89317-2bb3-4bc9-92fa-3d84f015b7b5",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "a62f372a-dd9d-437f-bd95-d156d91f66bf",
  "sourceToolAssistantUUID": "ffc89317-2bb3-4bc9-92fa-3d84f015b7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T10:14:34.165Z_

The paper does not mention Qwen2.5-14B -- the task summary's mention of 14B and "6 architectures" appears inaccurate. The paper covers 5 architectures (7-9B scale). Now let me produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a62f372a-dd9d-437f-bd95-d156d91f66bf",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BJdkV61UiX2vLKzMst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96d8987d-948c-408f-9749-687349f93d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ge3FnJCmFLQjjFFvo3z7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 43766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 189,
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

_source line 40 · 2026-05-15T10:14:34.613Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RgMsbBocPMWfzTtTNAW4wM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96d8987d-948c-408f-9749-687349f93d44",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BJdkV61UiX2vLKzMst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0309f46a-e0ba-40f6-892e-91e71dd1b481",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ge3FnJCmFLQjjFFvo3z7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 43766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 189,
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

_source line 41 · 2026-05-15T10:14:34.615Z_

<details><summary>↩ Tool result · `toolu_01RgMsbBocPMWfzTtTNAW4wM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0309f46a-e0ba-40f6-892e-91e71dd1b481",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "ac2238362768c5015",
  "type": "user",
  "uuid": "051b53a0-bca5-448b-b318-042972d63c63",
  "sourceToolAssistantUUID": "0309f46a-e0ba-40f6-892e-91e71dd1b481",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T10:16:09.562Z_



Now I have a thorough understanding of the paper. Let me produce the review.

---

## Review: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"

**Reviewer R2 — Focus: Novelty and Related Work**

---

### 1. Summary

This paper studies per-head mixed-precision KV cache quantization across five 7-9B transformer architectures using hardware-aligned bit-widths {2, 4, 8, 16}. The main contributions are: (1) identifying that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, and proposing a cardinality constraint on 2-bit assignments as a fix; (2) a taxonomy of head sensitivity distributions (Spread/Spike/Flat); and (3) a joint empirical decision rule (concentration + t1/t5 ratio) for predicting when non-uniform allocation is beneficial. Only Qwen2.5-7B (Spread) shows a strong benefit (27.3% PPL reduction); the other four architectures show negligible or negative results.

---

### 2. Novelty Assessment

**Cardinality constraint on 2-bit assignments.** Adding a cardinality constraint to MCKP is a textbook technique in combinatorial optimization. The contribution is the *diagnostic insight* — that 2-bit distortion compounds super-additively through the residual stream — rather than a novel algorithm. The paper frames this honestly ("a minimal intervention: cap the number of 2-bit assignments"), and the empirical demonstration of the compounding effect (Section 3.3, with the 1.56x-to-4.89x super-additivity progression) is well-executed. However, from a methods standpoint, the constraint is a single hyperparameter added to an existing formulation. The observation that constrained greedy equals MCKP is a natural consequence of k << H with a unique marginal-benefit ordering, not a deep theoretical result.

**Sensitivity profiling and taxonomy.** Per-head sensitivity analysis is established in prior work (KVQuant, KIVI, RateQuant, HeadKV). The novelty here is the Spread/Spike/Flat taxonomy and the two summary statistics (top-5% concentration, t1/t5 ratio). This is a useful conceptual framework, but it is descriptive rather than predictive: with N=5 architectures and N=1 exhibiting the beneficial "Spread" pattern, the taxonomy is an observation fitted post-hoc, not a validated diagnostic. The paper acknowledges this ("the spread category rests on N=1"), which is commendable, but the acknowledgment does not resolve the generalizability concern.

**Empirical decision rule.** Fitting a two-threshold rule (concentration > 0.50 AND t1/t5 < 0.70) to 5 data points with 1 positive case is pattern-matching, not a contribution that can be meaningfully evaluated for robustness. Any two-dimensional threshold can separate 1 point from 4 with 100% accuracy. The paper would need at minimum 10-15 architectures, with multiple Spread cases, to argue this is a generalizable decision rule rather than a description of Qwen2.5-7B.

**Overall positioning.** This is primarily an empirical study with a thin methods contribution. The value lies in the systematic investigation and the negative results (4 of 5 models show no benefit). The paper is honest about this, which I appreciate, but at a top venue this creates a tension: the method is incremental, the positive evidence is narrow, and the diagnostic is preliminary.

---

### 3. Related Work / Positioning

**Correction to the review prompt:** Contrary to the initial task description, the paper *does* include a Related Work section (Section 2, `related_work.tex`) and a bibliography with 31 references. The Related Work covers uniform KV quantization (KIVI, KVQuant, QServe, ZipCache, GEAR, SKVQ, RotateKV, MiniKV, AquaKV), eviction methods (H2O, SnapKV, FastGen, Scissorhands, StreamingLLM, PyramidInfer, HeadKV, Ada-KV), weight-level mixed-precision (HAWQ, HAWQ-V2, HAQ, SqueezeLLM), KV-level mixed-precision at various granularities (KVmix, KVTuner, PM-KVQ, Kitty, Don't Waste Bits, ARKV, MixKVQ), rate-distortion formulation (RateQuant), and attention head analysis (Voita et al., Michel et al.).

The related work section is reasonably comprehensive for its length. Several observations:

- **Good differentiation from RateQuant.** The paper clearly explains why RateQuant's polymatroid-based greedy optimality breaks on non-consecutive bit-widths, and positions the cardinality constraint as "the minimal fix that restores the additive regime." This is the strongest positioning claim.

- **Good coverage of granularity spectrum.** The Granularity Tradeoff discussion (Appendix D) places per-head allocation between layer-level (KVmix, KVTuner) and token-level (ZipCache, KIVI), arguing it occupies "the sweet spot for static allocation." This is a useful framing.

- **Missing direct experimental comparison.** While the related work *discusses* many methods, the experimental section only compares against uniform 4-bit, unconstrained greedy/MCKP, and simple heuristics. No head-to-head comparison with KIVI, KVQuant, KVTuner, AquaKV, or any other published method. For a venue like EMNLP/NeurIPS/ICML, this is a significant gap. The paper argues implicitly that uniform 4-bit is the natural baseline, but reviewers will want to see how constrained MCKP compares to at least one established method (e.g., KIVI's per-channel quantization or KVTuner's layer-level mixed-precision).

- **Missing comparison with token-level methods.** The paper mentions token-level allocation as "orthogonal" and composable, but does not demonstrate this composition empirically. A comparison showing constrained MCKP + token-level eviction vs. token-level eviction alone would significantly strengthen the paper.

- **No profiling cost comparison.** The paper profiles H x |B| = 112 x 4 = 448 forward passes on Qwen. How does this compare to the profiling cost of alternatives like KVQuant's sensitivity analysis or KVTuner's gradient-based approach? The runtime benchmark (Appendix K) addresses inference cost but not profiling overhead.

---

### 4. Significance / Impact

**Practical utility.** The cardinality constraint is immediately useful to practitioners who already use MCKP-style solvers (e.g., those building on RateQuant). It is a one-line fix that prevents catastrophic failure. This is a real contribution, albeit a narrow one.

**Negative results as contribution.** The paper's most valuable finding may be the negative one: non-uniform per-head allocation does not help on 4 of 5 tested architectures at 4x compression. This challenges the implicit assumption in prior work that finer-grained allocation always helps. However, negative-result papers face a higher bar at top venues, and the paper's framing as a "method + diagnostic" paper rather than a "negative result" paper creates a mismatch between the claimed contributions and the evidence.

**Who benefits?** Practitioners deploying LLMs who want to decide whether mixed-precision KV cache quantization is worth the profiling overhead. The decision rule, even in its preliminary form, provides actionable guidance: profile a few heads, check two metrics, and skip non-uniform allocation if the model is Spike or Flat. This is useful but does not require a full paper at a top venue.

**Scale limitations.** All experiments are at 7-9B scale. The paper acknowledges this, but the findings may not transfer to 70B+ models where memory pressure is more acute and head sensitivity distributions may differ. The aggressive compression results (Appendix F, 5.3x) show that non-uniform allocation becomes much more important at higher compression, suggesting the 4x operating point may be too conservative to reveal the method's value.

---

### 5. Writing Quality

**Strengths:**
- Clear, well-organized prose. The logical flow from compounding diagnosis to constraint to taxonomy to decision rule is easy to follow.
- Tables are informative and well-labeled. The main results table (Table 1) is compact and communicates the key finding at a glance.
- The "boundary case" / "critical counterexample" treatment of Yi-1.5-9B is mature scientific writing — using it as a falsification test for concentration-only thresholds.
- The limitations section is thorough and honest, which is refreshingly rare.

**Weaknesses:**
- The paper includes 3 figures (compounding curve, allocation visualization, heatmap), all in the appendix. The main body is entirely tables. At least the heatmap (Figure 1) should be in the main body — it is the most visually compelling evidence for the Spread/Spike/Flat taxonomy.
- Some redundancy: the 27.3% improvement figure appears at least 8 times across the paper. A single mention in the abstract and a reference in the main results would suffice.
- The abstract mentions "five 7-9B architectures" but the conclusion says "five models" — these are consistent, but the task prompt's mention of "6 architectures" and "Qwen2.5-14B" does not match the paper content. (This appears to be an error in the review prompt, not in the paper.)

---

### 6. Key Weaknesses (Specific)

**W1. N=1 positive case.** The entire method contribution rests on Qwen2.5-7B being the sole "Spread" architecture. With one positive example, it is impossible to distinguish the decision rule from overfitting. The threshold values (0.50, 0.70) are calibrated to separate this single point.

**W2. No comparison with existing methods.** The paper compares only against uniform 4-bit and its own unconstrained variants. At minimum, a comparison with KVTuner (layer-level mixed-precision, ICML 2025) and KIVI (per-channel uniform 2-bit) is needed. Without this, it is unclear whether the 11.23 PPL on Qwen is competitive with or surpassed by existing approaches.

**W3. Narrow operating point.** Nearly all experiments use 4x compression on WikiText-2 PPL. The aggressive compression results (Appendix F) suggest the method is much more valuable at 5.3x, where it gives 45x improvement on Llama — but this receives only one paragraph in the appendix. The paper would be substantially stronger if the main results included multiple compression ratios.

**W4. No real-kernel latency benchmarks.** The paper acknowledges this, but the runtime benchmark (Appendix K) shows constrained MCKP is 8.5% *slower* in decode than uniform, with a caveat that this is a PyTorch simulation upper bound. Without production kernel numbers, the practical value of the 27.3% PPL improvement is unclear — if it comes at a latency cost, practitioners may prefer simpler approaches.

**W5. Profiling cost not quantified.** 448 forward passes (or 1792 for hires) on calibration data is non-trivial. The paper should report wall-clock profiling time and compare to the cost of alternatives.

**W6. Decision rule is not validated out-of-sample.** The rule is fit on all 5 architectures and evaluated on the same 5. There is no held-out validation. Adding even 2-3 additional architectures (e.g., Phi-3, Falcon, or a Qwen2.5 variant at a different scale) as held-out test cases would substantially strengthen the claim.

---

### 7. Key Strengths (Specific)

**S1. Systematic and thorough empirical investigation.** The paper covers 5 architectures spanning different GQA ratios, attention mechanisms (standard, sliding-window, softcapped), and sensitivity distributions. The appendices (cross-dataset stability, profiling resolution, KV separation, budget sweep, solver equivalence, heuristic baselines) are comprehensive.

**S2. Honest treatment of negative results.** The paper does not oversell. It explicitly states that non-uniform allocation "does not help universally" and that the spread category rests on N=1. The limitations section is one of the most thorough I have seen.

**S3. Useful diagnostic framework.** Even in its preliminary form, the Spread/Spike/Flat taxonomy provides practitioners with a mental model for understanding when mixed-precision allocation is worth pursuing. The Yi-1.5-9B counterexample (high concentration but spike pattern, so no benefit) is a genuinely useful insight.

**S4. Solver equivalence result.** The demonstration that constrained greedy = MCKP across all tested architectures is practically valuable. Practitioners can use a simple O(H log H) algorithm without worrying about solver choice. The brute-force oracle validation closes the optimality chain convincingly.

**S5. Compounding analysis.** The identification and characterization of 2-bit distortion compounding (Section 3.3) is the most technically interesting part of the paper. The U-shaped curve, the super-additivity progression (1.56x at k=8 to 4.89x at k=64), and the random-vs-top-k control are well-designed experiments.

**S6. Comprehensive related work.** The related work section covers 31 references across uniform quantization, eviction, weight-level mixed-precision, KV-level mixed-precision at multiple granularities, and rate-distortion allocation. The positioning against RateQuant is particularly well-done.

---

### 8. Minor Issues

- The exp_id comments (e.g., `%exp_id=qwen_constrained_mckp`) should be removed before submission.
- Table 6 (heterogeneity) would benefit from a visual indicator (e.g., checkmark/cross) in an additional "MCKP helps?" column.
- The Gemma-2 BOS-correction asterisk is mentioned in several tables but explained only briefly; a clearer explanation would help.

---

### 9. Questions for Authors

1. Have you tested on any architecture where the decision rule predicts "Spread" but that is not Qwen2.5-7B? Without a second positive case, the rule is unfalsifiable.
2. At 5.3x compression, constrained MCKP shows dramatic improvements even on Llama and Mistral. Why not make this the primary operating point?
3. How does constrained MCKP compare to KIVI (asymmetric 2-bit) and KVTuner (layer-level mixed-precision) on the same models and budgets?
4. What is the wall-clock time for profiling at standard and hires resolution?

---

### 10. Preliminary Score and Confidence

**Score: 4 (Weak Accept)**

**Confidence: 4 (High)**

**Justification:** The paper presents a systematic and honest empirical investigation of an important practical question. The compounding analysis is insightful, the cardinality constraint is a useful (if incremental) fix, and the Spread/Spike/Flat taxonomy provides a useful conceptual framework. The related work section is comprehensive and the positioning against RateQuant is well-done. However, the method novelty is thin (one hyperparameter added to an existing formulation), the positive evidence is extremely narrow (N=1 Spread architecture), the decision rule is preliminary and unvalidated out-of-sample, and there are no comparisons with any established method beyond uniform baselines. The paper is above the bar for a workshop paper or Findings track but sits at the boundary for a main conference. The honest treatment of limitations and the quality of the negative-result analysis tip it toward a weak accept, conditional on authors addressing the missing baselines (W2) and the narrow operating point (W3) in revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "051b53a0-bca5-448b-b318-042972d63c63",
  "isSidechain": true,
  "agentId": "ac2238362768c5015",
  "requestId": "req_011Cb4BK4P4hT5yopoz8SRt5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef825bef-1cb9-4b84-b8da-f537f2ba4c74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8223gg1A2igzMpqx6tkZH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 43955,
      "output_tokens": 3842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3842,
          "cache_read_input_tokens": 43955,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 829,
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
