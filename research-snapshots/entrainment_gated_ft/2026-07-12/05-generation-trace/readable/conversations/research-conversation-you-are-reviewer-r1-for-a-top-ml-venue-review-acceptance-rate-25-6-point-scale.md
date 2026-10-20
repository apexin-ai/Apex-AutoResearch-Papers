# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6cf4a90443b1fe89.jsonl`
- **Structured JSON:** [`58b57301304c9055899d.json`](../../sessions/58/58b57301304c9055899d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-15T10:13:14.593Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **methods and experiments**.

## Paper Summary
"When Does Non-Uniform KV Cache Quantization Help?" — A 9-page paper studying per-head mixed-precision KV cache quantization across 6 transformer architectures (Qwen2.5-7B/14B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B). Three contributions:
1. **Cardinality constraint** (max_2bit ≤ k) as universal fix — prevents compounding degradation on all 6 architectures, makes greedy = MCKP (Δ=0.0000).
2. **Sensitivity distribution taxonomy** — Spread/Spike/Flat shapes predict whether MCKP exploits heterogeneity.
3. **Empirical decision rule** — joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70) classifies 5/5 non-borderline architectures correctly; 6th (Qwen-14B) is boundary case with modest 7.9% benefit.

## Key Tables/Results
- Table 1: Qwen-14B top-10 sensitive heads (L0 dominance diluted)
- Table 2: k-ablation for 14B — optimal k=12, PPL 7.18 vs 7.80 uniform (7.9% improvement), shallow U-shape
- Table 3: Solver equivalence (greedy=MCKP at k=12, Δ=0.0000)
- Table 4: Unconstrained vs constrained 14B — 1.56× unconstrained → 1.10× constrained
- Table 5: Gemma-2 BOS-fixed — baseline 6.03, uniform 6.17, MCKP 6.19 (−0.35%)
- Table 6: Gemma-2 k-ablation — monotonic increase (flat distribution, no benefit)
- Table 7: Decision rule validation — 5/5 non-borderline correct, 14B boundary type-II error
- Table 8: Cross-architecture summary (6 models)
- Table 9: 14B downstream — avg +0.7pp, all 4 tasks positive but within single-run noise
- Table 10: Compounding super-additivity — random-k vs top-k, ratio 1.01→2.44 monotonic
- Table 11: Solver equivalence — greedy≠MCKP unconstrained, greedy=MCKP constrained

## Experiment Design Reference (from review_context.yaml)
The imagined experiment plan included these experiments:
1. Qwen2.5-14B hires profiling (W1) — 384 heads, concentration 0.47, t₁/t₅ 0.72, "diluted spread"
2. Qwen2.5-14B constrained MCKP + k ablation — optimal k=12, 7.9% improvement, gap recovery 47.7%
3. Qwen2.5-14B unconstrained — 1.56× degradation, 58 heads at 2-bit
4. Qwen2.5-14B downstream — avg +0.7pp, within noise (no multi-seed CI)
5. Gemma-2-9B BOS-fixed constrained — baseline 6.03, MCKP 6.19, −0.35%
6. Decision rule revalidation with 6 models — 5/6 hard accuracy, 5/5 non-borderline
7. W9 compounding super-additivity — observation only, single model, high variance at k=64
8. Paper narrative integration — 14B as boundary case study

Paper covers all 8 experiments. The review context notes that the 14B downstream results lack multi-seed CI, and the compounding observation is single-model.

## Your Task
Produce a structured review covering:

### 1. Method Soundness (Section 2)
- Is the per-head profiling protocol (single-head 2-bit while others at 4-bit) well-motivated? What are its limitations?
- Is the MCKP formulation correct? Any issues with the additive distortion assumption?
- Is the cardinality constraint well-justified? Is the k-selection procedure (sweep) practical?
- Is the decision rule (concentration + t₁/t₅) well-defined? Thresholds seem ad-hoc — how robust?

### 2. Experimental Rigor
- **Coverage**: 6 architectures is decent but all are 7-14B range, no >30B models. Only WikiText-2 for calibration/eval.
- **Statistical significance**: No error bars, no multi-seed runs. 14B downstream +0.7pp is within noise. The paper acknowledges this but still claims "consistent positive."
- **Baselines**: Only uniform 4-bit baseline. No comparison with other mixed-precision methods (KIVI, GEAR, etc.)
- **Evaluation**: Only PPL + 4 downstream tasks. No generation quality, no long-context eval.
- **BOS bug**: Gemma-2 had a BOS handling bug that was fixed — does this inspire confidence or concern?
- **Solver equivalence Δ=0.0000**: Suspicious — is this exact equality or rounded? What does this imply about the search space?

### 3. Reproducibility
- Hyperparameters stated? Code available? Hardware details?

### 4. Key Weaknesses (be specific)
- N=1 Spread architecture (Qwen-7B is the only strong positive)
- Compounding analysis on single model only
- No comparison with existing mixed-precision methods
- Decision rule thresholds are post-hoc fit to 6 data points

### 5. Key Strengths
- Practical contribution (constraint is simple to implement)
- Honest treatment of boundary case
- Systematic cross-architecture study

### 6. Preliminary Score and Confidence
Give: Score (1-6), Confidence (1-5), and 2-3 sentence justification.

Output your full review in markdown format. Be thorough but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "8993f3b0-6afb-4024-b643-cccd11702e43",
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

_source line 2 · 2026-05-15T10:13:14.598Z_

```json
{
  "parentUuid": "8993f3b0-6afb-4024-b643-cccd11702e43",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
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
  "uuid": "aade7fc0-bd5d-488a-be72-3c1d64de8eaf",
  "timestamp": "2026-05-15T10:13:14.598Z",
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

_source line 3 · 2026-05-15T10:13:17.624Z_



I'll start by reading the paper sections to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aade7fc0-bd5d-488a-be72-3c1d64de8eaf",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BD9DrRQKgTUXoAkGrv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6dfd42-217e-43f6-9475-1b5203de6b57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ueKBUi7wJqtvmvptqmaTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7362,
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

_source line 4 · 2026-05-15T10:13:19.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ABaxwpeST2qKubz6HUrR4a`</summary>

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
  "parentUuid": "5c6dfd42-217e-43f6-9475-1b5203de6b57",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BD9DrRQKgTUXoAkGrv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35da2c75-af40-4f6a-b3ef-d663f3cd13b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ueKBUi7wJqtvmvptqmaTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7362,
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

_source line 5 · 2026-05-15T10:13:19.035Z_

<details><summary>↩ Tool result · `toolu_01ABaxwpeST2qKubz6HUrR4a`</summary>

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
  "parentUuid": "35da2c75-af40-4f6a-b3ef-d663f3cd13b5",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "faebf284-9bc1-4d24-99ab-265fdb45d2f2",
  "sourceToolAssistantUUID": "35da2c75-af40-4f6a-b3ef-d663f3cd13b5",
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

_source line 6 · 2026-05-15T10:13:19.925Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GF4K6VXfJpmzy8MwnpFGpQ`</summary>

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
  "parentUuid": "faebf284-9bc1-4d24-99ab-265fdb45d2f2",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BD9DrRQKgTUXoAkGrv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aac5576c-5433-4451-a4c6-5af16bd3a00c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ueKBUi7wJqtvmvptqmaTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7362,
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

_source line 7 · 2026-05-15T10:13:19.931Z_

<details><summary>↩ Tool result · `toolu_01GF4K6VXfJpmzy8MwnpFGpQ`</summary>

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
  "parentUuid": "aac5576c-5433-4451-a4c6-5af16bd3a00c",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "d9b5296a-9c84-4466-abf3-fbdb4275fd96",
  "sourceToolAssistantUUID": "aac5576c-5433-4451-a4c6-5af16bd3a00c",
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

_source line 8 · 2026-05-15T10:13:20.496Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lv9bwBEiWqoNw6YFuJKmqL`</summary>

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
  "parentUuid": "d9b5296a-9c84-4466-abf3-fbdb4275fd96",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BD9DrRQKgTUXoAkGrv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2101b2f7-899f-4ddd-88c8-14cb467bb1dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ueKBUi7wJqtvmvptqmaTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7362,
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

_source line 9 · 2026-05-15T10:13:20.500Z_

<details><summary>↩ Tool result · `toolu_01Lv9bwBEiWqoNw6YFuJKmqL`</summary>

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
  "parentUuid": "2101b2f7-899f-4ddd-88c8-14cb467bb1dd",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "1a4f9fa1-a709-454e-849d-65cef3a50fed",
  "sourceToolAssistantUUID": "2101b2f7-899f-4ddd-88c8-14cb467bb1dd",
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

_source line 10 · 2026-05-15T10:13:20.615Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsbVjKMGhWdDRouAFvLKh9`</summary>

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
  "parentUuid": "1a4f9fa1-a709-454e-849d-65cef3a50fed",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BD9DrRQKgTUXoAkGrv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "925c1a4d-4fde-4853-a260-ae25f47cd618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ueKBUi7wJqtvmvptqmaTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7362,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7362,
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

_source line 11 · 2026-05-15T10:13:20.619Z_

<details><summary>↩ Tool result · `toolu_01RsbVjKMGhWdDRouAFvLKh9`</summary>

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
  "parentUuid": "925c1a4d-4fde-4853-a260-ae25f47cd618",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "78e3e962-7827-43e9-ba0e-3554ca7e9b50",
  "sourceToolAssistantUUID": "925c1a4d-4fde-4853-a260-ae25f47cd618",
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

_source line 12 · 2026-05-15T10:13:24.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WPjeTtY7dpHoQLoBXUns3F`</summary>

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
  "parentUuid": "78e3e962-7827-43e9-ba0e-3554ca7e9b50",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDbp1bEd1ewBXNnqDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60b502d2-baa8-4807-b492-0e00d97ed33b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172sGsehavX9f4Bj1Yq6dCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6869,
      "cache_read_input_tokens": 16522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6869,
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

_source line 13 · 2026-05-15T10:13:24.503Z_

<details><summary>↩ Tool result · `toolu_01WPjeTtY7dpHoQLoBXUns3F`</summary>

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
  "parentUuid": "60b502d2-baa8-4807-b492-0e00d97ed33b",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "3f6c3b18-8f00-4655-8218-61722355fdbe",
  "sourceToolAssistantUUID": "60b502d2-baa8-4807-b492-0e00d97ed33b",
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

_source line 14 · 2026-05-15T10:13:24.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01URrfaHfFukWn8ToqX5Zf6n`</summary>

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
  "parentUuid": "3f6c3b18-8f00-4655-8218-61722355fdbe",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDbp1bEd1ewBXNnqDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7f54a38-8fe4-4915-9fd4-861337f220a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172sGsehavX9f4Bj1Yq6dCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6869,
      "cache_read_input_tokens": 16522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6869,
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

_source line 15 · 2026-05-15T10:13:24.986Z_

<details><summary>↩ Tool result · `toolu_01URrfaHfFukWn8ToqX5Zf6n`</summary>

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
  "parentUuid": "e7f54a38-8fe4-4915-9fd4-861337f220a3",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "6073f3eb-9a09-4089-a51e-c3bbff6e5c18",
  "sourceToolAssistantUUID": "e7f54a38-8fe4-4915-9fd4-861337f220a3",
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

_source line 16 · 2026-05-15T10:13:25.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VePNFLvkemVDGFz7rcq6CM`</summary>

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
  "parentUuid": "6073f3eb-9a09-4089-a51e-c3bbff6e5c18",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDbp1bEd1ewBXNnqDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13a01a18-5625-4029-bafd-f2c32a041506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172sGsehavX9f4Bj1Yq6dCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6869,
      "cache_read_input_tokens": 16522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6869,
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

_source line 17 · 2026-05-15T10:13:25.562Z_

<details><summary>↩ Tool result · `toolu_01VePNFLvkemVDGFz7rcq6CM`</summary>

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
  "parentUuid": "13a01a18-5625-4029-bafd-f2c32a041506",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "6cc2d0ab-4049-494c-a3ea-b7aa6efbb8a9",
  "sourceToolAssistantUUID": "13a01a18-5625-4029-bafd-f2c32a041506",
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

_source line 18 · 2026-05-15T10:13:25.943Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Dair7kPrkG8GSuLcdvBEY`</summary>

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
  "parentUuid": "6cc2d0ab-4049-494c-a3ea-b7aa6efbb8a9",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDbp1bEd1ewBXNnqDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f16fb795-2a5d-404a-9fab-a8ca9a5913f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172sGsehavX9f4Bj1Yq6dCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6869,
      "cache_read_input_tokens": 16522,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 16522,
          "cache_creation_input_tokens": 6869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6869,
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

_source line 19 · 2026-05-15T10:13:25.949Z_

<details><summary>↩ Tool result · `toolu_013Dair7kPrkG8GSuLcdvBEY`</summary>

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
  "parentUuid": "f16fb795-2a5d-404a-9fab-a8ca9a5913f9",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "adecd238-b0c2-478d-a82b-7f9a5212be47",
  "sourceToolAssistantUUID": "f16fb795-2a5d-404a-9fab-a8ca9a5913f9",
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

_source line 20 · 2026-05-15T10:13:31.428Z_

Now let me read the related work and references sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adecd238-b0c2-478d-a82b-7f9a5212be47",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDzvZdm8W67nabQRLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bccbc690-db0f-4964-8bdd-1cb41e131008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016woWJE7a1pmcmWubq4HLS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11313,
      "cache_read_input_tokens": 23391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11313,
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

_source line 21 · 2026-05-15T10:13:33.021Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014Se8QDsys9jEs3pJtudjLH`</summary>

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
  "parentUuid": "bccbc690-db0f-4964-8bdd-1cb41e131008",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDzvZdm8W67nabQRLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d72f673c-574a-477f-86f1-9834eb18e8a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016woWJE7a1pmcmWubq4HLS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11313,
      "cache_read_input_tokens": 23391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11313,
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

_source line 22 · 2026-05-15T10:13:33.040Z_

<details><summary>↩ Tool result · `toolu_014Se8QDsys9jEs3pJtudjLH`</summary>

```text
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72f673c-574a-477f-86f1-9834eb18e8a0",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "a0773926-8919-4a5f-9d11-917f10f1f0db",
  "sourceToolAssistantUUID": "d72f673c-574a-477f-86f1-9834eb18e8a0",
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

_source line 23 · 2026-05-15T10:13:33.235Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DvNdoSJ3ZY6ULKUigqhAyC`</summary>

```json
{
  "pattern": "docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0773926-8919-4a5f-9d11-917f10f1f0db",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BDzvZdm8W67nabQRLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2391752-6ae0-43bc-9342-904e3834f328",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016woWJE7a1pmcmWubq4HLS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11313,
      "cache_read_input_tokens": 23391,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 23391,
          "cache_creation_input_tokens": 11313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11313,
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

_source line 24 · 2026-05-15T10:13:33.246Z_

<details><summary>↩ Tool result · `toolu_01DvNdoSJ3ZY6ULKUigqhAyC`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2391752-6ae0-43bc-9342-904e3834f328",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "d0c07be4-3f11-4579-a51c-9a8a201b562e",
  "sourceToolAssistantUUID": "a2391752-6ae0-43bc-9342-904e3834f328",
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

_source line 25 · 2026-05-15T10:13:36.476Z_

<details open><summary>🔧 Tool call — Read · `toolu_0199dQJzXe7bFv4Dd53j8umW`</summary>

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
  "parentUuid": "d0c07be4-3f11-4579-a51c-9a8a201b562e",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BEXAVdvhGu5ZpThj7h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61a4229f-3bf7-4616-a613-942effe2d813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyrgfoK2etVaivthLq68Cy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 34704,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 34704,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 377,
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

_source line 26 · 2026-05-15T10:13:36.481Z_

<details><summary>↩ Tool result · `toolu_0199dQJzXe7bFv4Dd53j8umW`</summary>

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
  "parentUuid": "61a4229f-3bf7-4616-a613-942effe2d813",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "f16dc44f-0176-47f8-ae9d-1ee9c9007e02",
  "sourceToolAssistantUUID": "61a4229f-3bf7-4616-a613-942effe2d813",
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

_source line 27 · 2026-05-15T10:13:40.398Z_

Now let me check for additional details on the Qwen-14B experiment mentioned in the task description, and the 6th architecture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f16dc44f-0176-47f8-ae9d-1ee9c9007e02",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BEkoHBcgcjXcmu2A7P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8695eb3-0075-42f0-a1a0-928eff027680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXmLtYPssqdZeq9W5xHbtm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 35081,
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

_source line 28 · 2026-05-15T10:13:41.367Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rw85KxVAru3PLeqx4hQ43G`</summary>

```json
{
  "pattern": "14B|Qwen2\\.5-14B|qwen.*14",
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
  "parentUuid": "c8695eb3-0075-42f0-a1a0-928eff027680",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BEkoHBcgcjXcmu2A7P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a78cc33b-9b3e-4e9e-8b63-f49ea2566cf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXmLtYPssqdZeq9W5xHbtm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 35081,
      "output_tokens": 180,
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
          "output_tokens": 180,
          "cache_read_input_tokens": 35081,
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

_source line 29 · 2026-05-15T10:13:41.388Z_

<details><summary>↩ Tool result · `toolu_01Rw85KxVAru3PLeqx4hQ43G`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a78cc33b-9b3e-4e9e-8b63-f49ea2566cf6",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "7d5966dd-4904-4a63-b022-d96447cf8be6",
  "sourceToolAssistantUUID": "a78cc33b-9b3e-4e9e-8b63-f49ea2566cf6",
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

_source line 30 · 2026-05-15T10:13:44.824Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Bi8X8xXKGVTrt4QFYSKWtt`</summary>

```json
{
  "pattern": "14B|six|sixth|6 model|6 arch",
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
  "parentUuid": "7d5966dd-4904-4a63-b022-d96447cf8be6",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BF7s47sNqgSJyK5Ru9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4dc6c13-1291-4e7f-8b98-8efb81b1c18d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5ECHfgHd5jTHEuUDvUzH2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 195,
      "cache_read_input_tokens": 36542,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 36542,
          "cache_creation_input_tokens": 195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 195,
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

_source line 31 · 2026-05-15T10:13:44.836Z_

<details><summary>↩ Tool result · `toolu_01Bi8X8xXKGVTrt4QFYSKWtt`</summary>

```text
docs/paper/related_work.tex:25:Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
docs/paper/main.bbl:157:\bibitem[{Michel et~al.(2019)Michel, Levy, and Neubig}]{michel2019sixteen}
docs/paper/main.bbl:159:\newblock \href {https://arxiv.org/abs/1905.10650} {Are sixteen heads really
docs/paper/references.bib:183:@inproceedings{michel2019sixteen,
docs/paper/main.aux:234:\citation{voita2019analyzing,michel2019sixteen}
docs/paper/main.aux:863:\bibcite{michel2019sixteen}{{20}{2019}{{Michel et~al.}}{{Michel, Levy, and Neubig}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4dc6c13-1291-4e7f-8b98-8efb81b1c18d",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "ba947196-5bb1-43cf-a633-f351c04aaa21",
  "sourceToolAssistantUUID": "b4dc6c13-1291-4e7f-8b98-8efb81b1c18d",
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

_source line 32 · 2026-05-15T10:13:49.636Z_

The paper as written covers 5 architectures (not 6), and does not include Qwen2.5-14B. The task description mentions 6 architectures and 14B results, but the actual paper text covers only 5 models (Qwen2.5-7B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-2-9B). Let me verify what tables are actually in the paper versus what's described in the task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba947196-5bb1-43cf-a633-f351c04aaa21",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BFNnjizcdp7btoo5d2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11fbfd24-874d-4947-90e9-52df8c84d669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Txh1F8ULNCVNiL8Gsb7y1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 36737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 374,
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

_source line 33 · 2026-05-15T10:13:50.932Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UWmGzDudw5tAqsVopGgHRo`</summary>

```json
{
  "pattern": "\\\\begin\\{table|\\\\label\\{tab:|Table~\\\\ref",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11fbfd24-874d-4947-90e9-52df8c84d669",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BFNnjizcdp7btoo5d2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80f7ca27-22d9-46d3-b5e6-9e221ad7becb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Txh1F8ULNCVNiL8Gsb7y1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 36737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 374,
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

_source line 34 · 2026-05-15T10:13:50.949Z_

<details><summary>↩ Tool result · `toolu_01UWmGzDudw5tAqsVopGgHRo`</summary>

```text
docs/paper/analysis.tex:11:Table~\ref{tab:heterogeneity} summarizes the results across five architectures at $4\times$ compression.
docs/paper/analysis.tex:25:\begin{table}[t]
docs/paper/analysis.tex:29:\label{tab:heterogeneity}
docs/paper/related_work.tex:20:Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 11.23 PPL at the same average bit-width (Table~\ref{tab:solver_equiv}).
docs/paper/experiments.tex:40:\begin{table}[t]
docs/paper/experiments.tex:44:\label{tab:main_results}
docs/paper/experiments.tex:79:MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
docs/paper/experiments.tex:84:\begin{table}[t]
docs/paper/experiments.tex:88:\label{tab:downstream}
docs/paper/method.tex:70:This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (11.23 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
docs/paper/method.tex:75:\begin{table}[t]
docs/paper/method.tex:79:\label{tab:solver_equiv}
docs/paper/method.tex:95:With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (11.23), same bit distribution on Qwen2.5-7B.
docs/paper/appendix.tex:16:\begin{table}[t]
docs/paper/appendix.tex:20:\label{tab:heuristic}
docs/paper/appendix.tex:71:\begin{table}[t]
docs/paper/appendix.tex:75:\label{tab:budget_sweep}
docs/paper/appendix.tex:87:Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
docs/paper/appendix.tex:155:\begin{table}[ht]
docs/paper/appendix.tex:158:\label{tab:runtime}
docs/paper/appendix.tex:170:Table~\ref{tab:runtime} reports end-to-end latency for three KV cache configurations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80f7ca27-22d9-46d3-b5e6-9e221ad7becb",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "ddc7d0ef-9f79-47e7-8aef-012491a6baef",
  "sourceToolAssistantUUID": "80f7ca27-22d9-46d3-b5e6-9e221ad7becb",
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

_source line 35 · 2026-05-15T10:13:55.970Z_

The paper as written has 5 models, not 6. The task description's references to Qwen2.5-14B and "Table 1-11" appear to be from the review context (experiment plan) rather than the actual paper. I'll review the paper as it actually exists. Let me also check the Gemma-2 BOS bug details and the compounding analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddc7d0ef-9f79-47e7-8aef-012491a6baef",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BFq72K3EN49AW7tst6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80c4f4e2-b654-4af2-a922-e657bba28638",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkA88TZVwj6ujSs9EDFXyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 37111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1046,
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

_source line 36 · 2026-05-15T10:13:56.776Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017Kscjj2QACPXxMM87SVZT9`</summary>

```json
{
  "pattern": "BOS|bos|beginning.of.sequence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c4f4e2-b654-4af2-a922-e657bba28638",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BFq72K3EN49AW7tst6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fc2d39e-a274-446d-97bb-eb2afe0f5c4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkA88TZVwj6ujSs9EDFXyK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 37111,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 37111,
          "cache_creation_input_tokens": 1046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1046,
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

_source line 37 · 2026-05-15T10:13:56.799Z_

<details><summary>↩ Tool result · `toolu_017Kscjj2QACPXxMM87SVZT9`</summary>

```text
docs/paper/experiments.tex:43:\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure severity tracks heterogeneity shape: catastrophic on Qwen ($3.3\times$ bf16), moderate on Gemma-2 ($1.5\times$), mild on the remaining three (${\sim}1.1\times$). Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok). $^\ddagger$Best $k$ from ablation ($k{=}4$). $^*$BOS-corrected.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fc2d39e-a274-446d-97bb-eb2afe0f5c4f",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "9a604556-0877-47a5-932d-ae18681f0879",
  "sourceToolAssistantUUID": "0fc2d39e-a274-446d-97bb-eb2afe0f5c4f",
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

_source line 38 · 2026-05-15T10:14:00.545Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YNkTXU5nusb4qm1EAAtbo1`</summary>

```json
{
  "pattern": "super.additi|compounding|random.*seed|top-k.*random|ratio.*monot",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a604556-0877-47a5-932d-ae18681f0879",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BGFvmFLgew6P3Eysto",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab46f9ff-638d-48d1-b597-53331cd0cea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqQPRX3tsFQ8puZ9Wr94Hw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 38157,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 38157,
          "cache_creation_input_tokens": 426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 426,
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

_source line 39 · 2026-05-15T10:14:00.573Z_

<details><summary>↩ Tool result · `toolu_01YNkTXU5nusb4qm1EAAtbo1`</summary>

```text
docs/paper/related_work.tex:19:On hardware-aligned $\{2,4,8,16\}$, the 4$\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.
docs/paper/experiments.tex:27:The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2).
docs/paper/experiments.tex:34:(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
docs/paper/experiments.tex:60:Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
docs/paper/conclusion.tex:3:Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
docs/paper/method.tex:19:Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
docs/paper/method.tex:32:\label{sec:compounding}
docs/paper/method.tex:39:The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
docs/paper/method.tex:41:This compounding is specific to 2-bit quantization and is \emph{super-additive}: quantizing the top-$k$ most sensitive heads to 2-bit simultaneously produces PPL $1.56\times$ the sum of their individual distortions at $k{=}8$, growing to $4.89\times$ at $k{=}64$.
docs/paper/method.tex:42:A random-$k$ control confirms that sensitivity ordering matters: at $k{=}64$, random selection yields 55.94 PPL vs.\ 22.95 for top-$k$, because random draws are more likely to include high-distortion heads that amplify compounding.
docs/paper/method.tex:46:The relationship between $k$ and PPL is U-shaped (Figure~\ref{fig:compounding}, Appendix~\ref{sec:compounding_appendix}): at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond $k{=}8$, compounding drives PPL upward.
docs/paper/method.tex:51:The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
docs/paper/method.tex:57:The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
docs/paper/method.tex:67:The additive objective treats per-head distortions as independent, but 2-bit compounding violates this once many 2-bit heads coexist.
docs/paper/method.tex:69:For Qwen2.5-7B, $k{=}8$ ($\sim$7\% of heads) is few enough that compounding contributes negligibly, consistent with the U-shaped curve minimum (Figure~\ref{fig:compounding}).
docs/paper/method.tex:101:Without the constraint, greedy cascades into excessive 2-bit allocation, as each additional 2-bit head looks locally beneficial but contributes to compounding.
docs/paper/abstract.tex:3:On the one spread-pattern model (Qwen2.5-7B), a cardinality-constrained solver achieves 11.23 perplexity at $4\times$ compression---a 27.3\% reduction over uniform 4-bit (15.45)---while unconstrained solvers fail catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
docs/paper/appendix.tex:4:\label{sec:compounding_appendix}
docs/paper/appendix.tex:8:\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
docs/paper/appendix.tex:9:\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
docs/paper/appendix.tex:10:\label{fig:compounding}
docs/paper/appendix.tex:19:\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling.}
docs/paper/appendix.tex:124:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
docs/paper/introduction.tex:40:\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab46f9ff-638d-48d1-b597-53331cd0cea2",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "60303505-cc18-4084-9a25-0ce8d8e454dd",
  "sourceToolAssistantUUID": "ab46f9ff-638d-48d1-b597-53331cd0cea2",
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

_source line 40 · 2026-05-15T10:14:03.373Z_

Now I have a thorough understanding of the paper. Let me also check for any Gemma-2 BOS discussion and the exact solver equivalence delta.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60303505-cc18-4084-9a25-0ce8d8e454dd",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BGXthZtJNH7hXc71ar",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c532526b-7fcc-43ff-b483-e890d7a9ae06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ks5kNH74gpVjnB5i8NA3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 38583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 41 · 2026-05-15T10:14:04.751Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Gheasx4Ve9PSeq951bseBX`</summary>

```json
{
  "pattern": "0\\.0000|exact.*equal|solver.*equiv|greedy.*MCKP.*identical",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c532526b-7fcc-43ff-b483-e890d7a9ae06",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BGXthZtJNH7hXc71ar",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d044207c-9a3c-4855-8e0e-17729d769181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ks5kNH74gpVjnB5i8NA3g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 38583,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 38583,
          "cache_creation_input_tokens": 1926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1926,
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

_source line 42 · 2026-05-15T10:14:04.780Z_

<details><summary>↩ Tool result · `toolu_01Gheasx4Ve9PSeq951bseBX`</summary>

```text
docs/paper/related_work.tex:20:Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 11.23 PPL at the same average bit-width (Table~\ref{tab:solver_equiv}).
docs/paper/conclusion.tex:4:On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 11.23 ($-$27.3\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
docs/paper/method.tex:70:This explains the constrained--unconstrained gap in Table~\ref{tab:solver_equiv}: constrained greedy operates inside the additive regime (11.23 PPL, matching the ${\approx}11$ additive estimate), while unconstrained solvers extrapolate outside it and miss true PPL by $3\text{--}4\times$.
docs/paper/method.tex:73:\label{sec:solver_equiv}
docs/paper/method.tex:78:\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
docs/paper/method.tex:79:\label{tab:solver_equiv}
docs/paper/method.tex:95:With the cardinality constraint, greedy and MCKP produce identical results (Table~\ref{tab:solver_equiv}): same PPL (11.23), same bit distribution on Qwen2.5-7B.
docs/paper/method.tex:98:When $k \ll H$ and the top-$k$ heads ranked by marginal benefit $d_h(4) - d_h(2)$ contain no ties, constrained greedy and MCKP produce identical per-head allocations.
docs/paper/abstract.tex:5:The cardinality constraint prevents catastrophic failure on spread architectures, moderate over-allocation on flat architectures (Gemma-2: unconstrained $1.47\times$ degradation reduced to within 0.5\% of uniform), and renders solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\log H)$ greedy algorithm.
docs/paper/introduction.tex:27:Constrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm.
docs/paper/introduction.tex:28:A per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
docs/paper/introduction.tex:42:\item We demonstrate that the cardinality constraint serves three roles: preventing catastrophic failure on spread architectures (Qwen: 32.45$\to$11.23), preventing moderate over-allocation on flat architectures (Gemma-2: 8.85$\to$within 0.5\% of uniform), and rendering solver choice irrelevant---constrained greedy and MCKP produce equivalent allocations across all tested architectures (\S\ref{sec:solver_equiv}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d044207c-9a3c-4855-8e0e-17729d769181",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "79634afa-5f9b-44ca-a5ab-d0b97b885a7b",
  "sourceToolAssistantUUID": "d044207c-9a3c-4855-8e0e-17729d769181",
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

_source line 43 · 2026-05-15T10:14:07.190Z_

Now let me submit my review via the MCP tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79634afa-5f9b-44ca-a5ab-d0b97b885a7b",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BGqvAiKmjRGPydYgVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba651a3c-6234-4ad5-9895-7208a95938b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXUBspzzz5X2vL3mSnydsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1265,
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

_source line 44 · 2026-05-15T10:14:07.774Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ChN6K8XtVnT8HoVPLhegy5`</summary>

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
  "parentUuid": "ba651a3c-6234-4ad5-9895-7208a95938b2",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BGqvAiKmjRGPydYgVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79c09595-a5f3-4b56-9f0d-1fd2c98fd612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXUBspzzz5X2vL3mSnydsj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 40509,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 40509,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1265,
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

_source line 45 · 2026-05-15T10:14:07.777Z_

<details><summary>↩ Tool result · `toolu_01ChN6K8XtVnT8HoVPLhegy5`</summary>

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
  "parentUuid": "79c09595-a5f3-4b56-9f0d-1fd2c98fd612",
  "isSidechain": true,
  "promptId": "09ffac6b-c077-4f44-bafc-43c2a14cddfd",
  "agentId": "a6cf4a90443b1fe89",
  "type": "user",
  "uuid": "a98d969d-4805-43f5-9e10-37235c4b0376",
  "sourceToolAssistantUUID": "79c09595-a5f3-4b56-9f0d-1fd2c98fd612",
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

_source line 46 · 2026-05-15T10:15:54.579Z_



Now I have thoroughly read all sections of the paper. Let me compose the full review.

---

# Review: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"

## Reviewer R1 — Methods and Experiments

---

### 1. Method Soundness

**Per-head profiling protocol (Section 2.2).** The single-head perturbation approach (quantize one head to target bit-width, keep all others at bf16, measure PPL delta) is a standard sensitivity analysis and is well-motivated as a tractable approximation. The paper is transparent about its key limitation: it measures marginal distortions in isolation, so it cannot capture interaction effects between simultaneously quantized heads. This is precisely the gap that causes the additive objective to fail for 2-bit assignments. The paper correctly identifies this gap and addresses it with the cardinality constraint rather than attempting a more complex (and likely intractable) joint profiling scheme. This is a reasonable engineering decision, though it means the method is fundamentally reactive -- the constraint patches the failure mode post-hoc rather than building a distortion model that accounts for interactions.

**Limitation:** The profiling cost scales as O(H x |B|) forward passes. For the models tested (112-336 KV heads, 4 bit-widths), this is manageable. At 70B+ scale (potentially 1000+ KV heads), it becomes expensive. The paper does not discuss profiling cost or amortization strategies.

**MCKP formulation (Eq. 1).** The formulation is correct as stated. The additive distortion assumption is explicitly acknowledged as the weak point, and the compounding analysis in Section 2.3 provides empirical evidence for when and why it breaks. The paper deserves credit for directly confronting the assumption violation rather than ignoring it.

However, the paper claims the constraint "restores additivity" (Section 2.4, "Restoring additivity" paragraph) without providing a rigorous test. The evidence is that constrained PPL (11.23) is close to the additive prediction (~11), but this is a single data point on a single model. On the four non-spread models, the additive prediction was never far off to begin with (because 2-bit distortions are small), so the constraint is untested in the regime where it matters most -- multiple spread-pattern architectures with varying degrees of compounding.

**Cardinality constraint (Eq. 2).** The constraint is simple, well-motivated by the compounding analysis, and easy to implement. The k-selection via sweep is practical but raises questions:
- The sweep requires solving the constrained problem for each candidate k and evaluating calibration PPL -- this multiplies the already-expensive profiling by the number of k candidates. The paper does not state how many k values are swept.
- The U-shape of the k-PPL curve is shown only for Qwen2.5-7B (Figure 2). For the other models, the k values are stated but the curves are not shown. Are they all U-shaped? On flat/spike models, is there any meaningful variation with k?
- k is model-specific and varies from 2 to 8 across the 5 tested models. There is no guidance for selecting k on a new model without running the full sweep.

**Decision rule (Section 4.2).** The joint condition (concentration >= ~0.50 AND t1/t5 <= ~0.70) is the most novel analytical contribution, but it has serious limitations the paper only partially acknowledges:

- The thresholds are fit to 5 data points. With 2 free parameters and 5 observations, the rule is under-determined. Any number of threshold pairs could achieve perfect separation on 5 points.
- The "soft" threshold notation (using "approximately greater/less than" symbols) obscures that these are arbitrary cutoffs. The paper does not provide sensitivity analysis: what happens at concentration = 0.48? At t1/t5 = 0.72?
- The spread category has N=1 (only Qwen2.5-7B). The paper acknowledges this but still frames the rule as a "diagnostic" -- which implies predictive utility that has not been validated out-of-sample.
- The metrics (top-5% concentration, t1/t5 ratio) both derive from the 2-bit distortion vector. Why top-5%? Why t1/t5 rather than t1/t3 or Gini coefficient? These design choices appear post-hoc and are not justified against alternatives.

Credit: The paper honestly states "the suggested thresholds should be treated as illustrative until confirmed on additional architectures" (Section 4.2). This candor is appreciated.

---

### 2. Experimental Rigor

**Coverage.** Five architectures (Qwen2.5-7B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-2-9B) spanning GQA ratios 2:1 to 8:1, standard/sliding-window/softcapped attention. This is a reasonable range for 7-9B models. The critical gap is the absence of models above 14B -- the paper's conclusions about sensitivity distribution shapes may not hold at larger scales where head counts increase and per-head redundancy patterns change. The Limitations section acknowledges this.

**Statistical significance.** This is the most significant experimental weakness:
- Main PPL results (Table 1) report single runs with no error bars. The 3-seed stability analysis (mean 10.99 +/- 0.06) is reported only in the appendix and only for Qwen2.5-7B hires profiling.
- Downstream results (Table 3 in the paper, labeled tab:downstream) show per-task deltas ranging from -3.2 to +4.0 points. Without confidence intervals, it is impossible to assess whether any of these are statistically significant. The -0.8 to -1.0 average degradation on Yi/Llama could easily be noise.
- The paper acknowledges the downstream results are "within noise" for non-spread models but still reports them in the main text, which may give readers a false impression of systematic effects.
- The compounding super-additivity analysis (Section 2.3) reports specific ratios (1.56x at k=8, 4.89x at k=64) without error bars, and on a single model only.

**Baselines.** This is a notable gap:
- The paper compares against uniform 4-bit, unconstrained greedy (RateQuant-style), unconstrained MCKP, L0-random heuristic, and naive positional heuristic.
- There is **no comparison with any existing mixed-precision KV cache quantization method** (KIVI, GEAR, KVQuant, ZipCache, KVmix, KVTuner, etc.), despite citing many of them in Related Work. The paper argues these operate at different granularities (layer-level, token-level), but a practitioner choosing a KV cache compression method needs to know how per-head allocation compares to these alternatives in absolute terms.
- The Related Work mentions KVmix and KVTuner as layer-level methods but does not benchmark against them, even though they are the most directly comparable (static mixed-precision allocation, just at coarser granularity).

**Evaluation metrics.** Only WikiText-2 PPL and 4 downstream tasks (ARC-C, HellaSwag, PIQA, WinoGrande) under 0-shot. No generation quality evaluation (BLEU, ROUGE, human judgment), no long-context evaluation (despite KV cache being most relevant at long sequences), no needle-in-a-haystack or similar retrieval tasks. The cross-dataset analysis (Appendix C, WikiText-2 vs. C4) is a useful addition that partially addresses calibration overfitting concerns.

**BOS correction on Gemma-2.** The paper marks Gemma-2 results with an asterisk (*) indicating "BOS-corrected" but provides no explanation in the text of what the BOS bug was, how it was discovered, or what the correction entailed. This lack of transparency is concerning -- readers cannot assess whether the fix was principled or whether it might have introduced other artifacts. The fact that a bug was found and fixed suggests the experimental pipeline may have other undetected issues.

**Solver equivalence.** The paper reports constrained greedy and MCKP produce "identical allocations" (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral). This is presented as an empirical observation and explained intuitively (when k << H and there are no ties, the top-k selection is deterministic). The explanation is reasonable, but the paper should note this is a structural property of the specific constraint form (cardinality on a single bit-width) combined with the small k values used. With larger k or more complex constraints, equivalence would likely break.

**Runtime benchmark (Appendix H).** The paper includes a PyTorch-level latency comparison showing 8.5% decode overhead for mixed-precision vs. uniform. The honest caveat that this is simulation-level and not production-kernel performance is appreciated, but the absence of real kernel benchmarks is a limitation that weakens the practical contribution. A 27% PPL improvement is irrelevant if it cannot be realized at acceptable latency.

---

### 3. Reproducibility

**Positive:**
- Model names and sizes are fully specified.
- Profiling parameters are stated (standard: 16 seq x 512 tok; hires: 64 seq x 2048 tok; WikiText-2 train).
- Compression target (4x, budget ratio 0.25) and k values per model are given.
- The MCKP formulation is standard and easily implementable.
- Bit-width set {2, 4, 8, 16} is clearly specified.

**Gaps:**
- No code release mentioned or referenced.
- Quantization implementation details are sparse: what quantization scheme is used (symmetric/asymmetric, per-channel/per-token, group size)? The paper says "hardware-aligned bit-widths" but does not specify the quantization format.
- Hardware details for main experiments are not stated in the main text. The runtime appendix mentions "NVIDIA RTX PRO 6000 (96 GB)" but it is unclear if all experiments used this GPU.
- The heuristic baselines use a "slightly higher budget (0.256 vs. 0.248)" -- this 3% budget difference is unexplained and could confound comparisons.

---

### 4. Key Weaknesses

**W1: N=1 for the beneficial case.** The entire positive result rests on a single architecture (Qwen2.5-7B). Four out of five models show no benefit from non-uniform allocation. The paper is honest about this but still frames the work around the positive case. A skeptical reading is: "non-uniform per-head KV cache quantization helps on 1 out of 5 tested architectures, and we don't know why that one is special beyond post-hoc descriptive statistics."

**W2: Compounding analysis is single-model.** The super-additivity ratios, the U-shaped k-PPL curve, and the "restoring additivity" argument are all demonstrated only on Qwen2.5-7B. It is unclear whether the compounding dynamics generalize -- perhaps Qwen's architecture has specific properties (e.g., its 7:1 GQA ratio concentrating information in fewer KV heads) that make it unusually susceptible.

**W3: No comparison with existing mixed-precision methods.** The paper positions itself against RateQuant (unconstrained greedy) and uniform baselines, but ignores the substantial body of work on mixed-precision KV cache quantization at other granularities. Without these comparisons, the practical value of the contribution is difficult to assess.

**W4: Decision rule thresholds are post-hoc.** Two free parameters, five data points, one positive example. The rule cannot be validated on the data it was derived from. The soft threshold notation masks the arbitrariness. No ablation on threshold sensitivity is provided.

**W5: Evaluation is narrow.** WikiText-2 only for PPL; 4 downstream tasks with no error bars; no long-context evaluation; no generation quality metrics. KV cache compression matters most at long context lengths, which is precisely the setting not evaluated.

**W6: Missing quantization implementation details.** The paper does not specify the quantization scheme (symmetric vs. asymmetric, per-channel vs. per-token, group quantization). These choices significantly affect both the absolute PPL numbers and the relative benefit of mixed-precision allocation. Without these details, the results cannot be reproduced and may not generalize to other quantization implementations.

---

### 5. Key Strengths

**S1: Practical and simple contribution.** The cardinality constraint is a single linear inequality that can be added to any existing MCKP solver. It requires no architectural changes, no training, and adds negligible computational overhead. The solver equivalence result further simplifies deployment by showing greedy is sufficient.

**S2: Honest treatment of negative results.** The paper does not oversell. Four out of five models show no benefit, and this is clearly stated. The boundary between beneficial and non-beneficial cases is the central analytical question, not a footnote. The Limitations section is thorough and self-aware.

**S3: Systematic cross-architecture study.** Testing five architectures with varying GQA ratios and attention mechanisms provides a more complete picture than single-model studies. The sensitivity taxonomy (spread/spike/flat) is descriptively useful even if the decision rule thresholds are not yet validated.

**S4: Clear identification of failure mode.** The compounding analysis (Section 2.3) provides a clear mechanistic explanation for why unconstrained solvers fail on hardware-aligned bit-widths. The distinction between the additive prediction (~11 PPL) and actual outcome (32-37 PPL) is compelling and actionable.

**S5: Cross-dataset stability.** The >96% bit-assignment agreement between WikiText-2 and C4 calibration (Appendix C) is a useful robustness check that many quantization papers omit.

---

### 6. Minor Issues

- The abstract mentions "five 7-9B architectures" but the paper also discusses budget sweeps and aggressive compression only on Qwen, making the "five architecture" framing somewhat misleading -- the depth of analysis is heavily skewed toward Qwen.
- Table 1 caption mentions "best constrained result per model in bold" but only Qwen and Llama are bolded. Gemma-2 at 6.20 is not bolded (correctly, since uniform 6.17 is better), but the inconsistency between "best constrained" and "best overall" is slightly confusing.
- The claim that the constraint "renders solver choice irrelevant" (abstract, introduction, conclusion) is stated very strongly for a result verified on 5 models. It would be more accurate to say "renders solver choice irrelevant in all tested cases."
- Section 2.3 reports random-k control "at k=64" but does not state how many random seeds were used for this control.

---

### 7. Questions for Authors

1. What quantization scheme (symmetric/asymmetric, group size, per-channel/per-token) is used? Would the results change under different quantization implementations?
2. Can you provide the k-PPL sweep curves for all 5 models, not just Qwen? Is the U-shape universal or Qwen-specific?
3. Why was t1/t5 chosen over other distribution shape metrics (Gini, entropy, kurtosis)? Was any comparison performed?
4. The Gemma-2 "BOS-corrected" results are unexplained. What was the bug and how was it fixed?
5. Have you tested on any model >14B? Even a single data point at 70B would substantially strengthen the paper.

---

### 8. Preliminary Score and Confidence

**Score: 4 (Weak Accept)**

**Confidence: 4 (High)**

**Justification:** The paper identifies a real and practically important failure mode (2-bit compounding in unconstrained per-head KV cache quantization), proposes a simple and effective fix (cardinality constraint), and conducts a systematic cross-architecture study with commendable honesty about negative results. These strengths place it above the acceptance threshold. However, the positive result rests on N=1 architecture, the decision rule is fit to 5 points with 2 free parameters, there are no comparisons with existing mixed-precision methods, statistical rigor is lacking (no error bars on main results), and evaluation is narrow (WikiText-2 PPL, no long-context). The contribution is genuine but incremental -- the constraint is a one-line fix, and the analytical framework (taxonomy + decision rule) is descriptive rather than predictive at the current evidence level. A revision adding 2-3 more spread-pattern models and comparisons with KVmix/KVTuner would strengthen the paper substantially.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a98d969d-4805-43f5-9e10-37235c4b0376",
  "isSidechain": true,
  "agentId": "a6cf4a90443b1fe89",
  "requestId": "req_011Cb4BH4xV9XV3KefcUCzXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6e429cf-7f37-4733-8b72-37e12c696004",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "985fc034-0a8d-4fd1-9c98-0614ebb79af1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6xJeAGqyt7R2b9sDuZH18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 41774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
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
