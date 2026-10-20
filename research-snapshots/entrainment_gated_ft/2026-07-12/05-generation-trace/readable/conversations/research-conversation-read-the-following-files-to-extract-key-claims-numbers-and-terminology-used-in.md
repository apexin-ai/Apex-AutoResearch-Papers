# Research conversation: Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa1bc34633d90da83.jsonl`
- **Structured JSON:** [`6ab87df378196c986e99.json`](../../sessions/6a/6ab87df378196c986e99.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-14T11:01:44.373Z_

Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the Conclusion section is consistent with them.

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/ — list all files in this directory
2. Read the abstract and introduction files if they exist (likely abstract.tex, introduction.tex or similar)
3. Read any results/experiments section if it exists

For each file, extract:
- Exact numbers cited (percentages, improvements, specific values)
- Key terminology and how concepts are named
- Any claims about the method

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "3053d5d2-8a55-4684-ab0a-c30d18aaa17c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T11:01:45.956Z_

I'll help you extract key claims, numbers, and terminology from the paper. Let me start by exploring the paper directory structure and then reading the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3053d5d2-8a55-4684-ab0a-c30d18aaa17c",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6imBVdH9xdpNZ5c1U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3072302f-38d3-45a8-ab44-134498cda130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmR94aHhdcBXNRFkrywe1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27291,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27291,
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

_source line 3 · 2026-05-14T11:01:46.064Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TtiaJQxkntg6FCMmS26rDu`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3072302f-38d3-45a8-ab44-134498cda130",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6imBVdH9xdpNZ5c1U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6a3bb667-3cb1-445a-bcdb-4df1140cd09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmR94aHhdcBXNRFkrywe1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27291,
      "cache_read_input_tokens": 0,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27291,
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

_source line 4 · 2026-05-14T11:01:46.224Z_

<details><summary>↩ Tool result · `toolu_01TtiaJQxkntg6FCMmS26rDu`</summary>

```text
total 136
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 10:47 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 13 17:17 ..
-rw-r--r-- 1 ubuntu ubuntu  1519 May 14 11:01 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 11615 May 14 07:32 acl.sty
-rw-r--r-- 1 ubuntu ubuntu 45186 May 14 07:32 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  7337 May 14 10:13 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  9849 May 14 11:00 experiments.tex
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 07:43 figures
-rw-r--r-- 1 ubuntu ubuntu  5673 May 14 10:20 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  8563 May 14 10:44 method.tex
-rw-r--r-- 1 ubuntu ubuntu  6092 May 14 09:14 references.bib
-rw-r--r-- 1 ubuntu ubuntu  2071 May 14 09:02 references.bib.prev
-rw-r--r-- 1 ubuntu ubuntu  4793 May 14 10:45 related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a3bb667-3cb1-445a-bcdb-4df1140cd09e",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "b2797ef5-798a-4a2b-9b37-b4eb1b155202",
  "sourceToolAssistantUUID": "6a3bb667-3cb1-445a-bcdb-4df1140cd09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T11:01:47.763Z_

Now let me read the key files: abstract.tex, introduction.tex, experiments.tex, method.tex, and analysis.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2797ef5-798a-4a2b-9b37-b4eb1b155202",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "511e16cf-bfa1-49f2-832f-849bb228c55d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 6 · 2026-05-14T11:01:48.315Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qm4RxMBTb2TEBTBuAEZdGJ`</summary>

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
  "parentUuid": "511e16cf-bfa1-49f2-832f-849bb228c55d",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c3053c4e-916a-401f-ba8b-d4b0a031d527",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 7 · 2026-05-14T11:01:48.322Z_

<details><summary>↩ Tool result · `toolu_01Qm4RxMBTb2TEBTBuAEZdGJ`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce identical bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm.
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that predicts, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3053c4e-916a-401f-ba8b-d4b0a031d527",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "89755190-e845-4eef-b2bb-409fdc466bdd",
  "sourceToolAssistantUUID": "c3053c4e-916a-401f-ba8b-d4b0a031d527",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T11:01:49.142Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vxnq9dGUAbeVBuu1QA1Pf2`</summary>

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
  "parentUuid": "89755190-e845-4eef-b2bb-409fdc466bdd",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38453094-5692-4e36-bb37-bbff909b9d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 9 · 2026-05-14T11:01:49.153Z_

<details><summary>↩ Tool result · `toolu_01Vxnq9dGUAbeVBuu1QA1Pf2`</summary>

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
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	
31	However, non-uniform allocation does not help universally.
32	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
33	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
34	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
35	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
36	
37	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
38	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
39	On our three architectures, the metric cleanly separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform).
40	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
41	
42	Our contributions are:
43	\begin{enumerate}[nosep]
44	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
45	
46	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce identical per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
47	
48	\item We propose a heterogeneity-based diagnostic framework that predicts whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
49	\end{enumerate}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38453094-5692-4e36-bb37-bbff909b9d07",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "59566ccf-c132-4ad6-bc93-3821e58efecf",
  "sourceToolAssistantUUID": "38453094-5692-4e36-bb37-bbff909b9d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T11:01:49.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L6u1GL6AViS9geT31Ftapq`</summary>

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
  "parentUuid": "59566ccf-c132-4ad6-bc93-3821e58efecf",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70e3d0e7-0eb2-4e58-acc5-8744ea9d160d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 387,
          "cache_read_input_tokens": 27291,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1355,
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

_source line 11 · 2026-05-14T11:01:49.400Z_

<details><summary>↩ Tool result · `toolu_01L6u1GL6AViS9geT31Ftapq`</summary>

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
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
35	The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
36	When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
37	As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
42	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
43	\label{fig:compounding}
44	\end{figure}
45	
46	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
47	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
48	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
49	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
50	
51	This compounding is specific to 2-bit quantization.
52	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
53	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
54	
55	Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
56	The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
57	
58	\subsection{Cardinality Constraint}
59	\label{sec:cardinality}
60	
61	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
62	\begin{equation}
63	\label{eq:constraint}
64	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
65	\end{equation}
66	
67	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
68	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
69	
70	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
71	
72	A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
73	On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
74	These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
75	We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
76	No manual exclusion rule is needed; the profiler signal is sufficient.
77	
78	\subsection{Solver Equivalence}
79	\label{sec:solver_equiv}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\footnotemark}
85	\label{tab:solver_equiv}
86	\begin{tabular}{llcccc}
87	\toprule
88	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
89	 & & & 2-bit & 4-bit & 8/16-bit \\
90	\midrule
91	Greedy & None & 32.45 & 68 & 30 & 14 \\
92	MCKP & None & 36.92 & 75 & 33 & 4 \\
93	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
94	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
95	Uniform & --- & 15.45 & 0 & 112 & 0 \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
100	
101	With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
102	Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
103	We verify this at the per-head level across three models:
104	
105	\begin{itemize}[nosep]
106	\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
107	\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
108	\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
109	\end{itemize}
110	
111	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
112	Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
113	The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
114	
115	The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70e3d0e7-0eb2-4e58-acc5-8744ea9d160d",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "0d7452ef-1495-43f1-8a76-8cd4ed4e9325",
  "sourceToolAssistantUUID": "70e3d0e7-0eb2-4e58-acc5-8744ea9d160d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T11:01:49.406Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rayi36ucuj8b198puWLjsz`</summary>

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
  "parentUuid": "0d7452ef-1495-43f1-8a76-8cd4ed4e9325",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa38fc59-5611-47d6-8a2b-e20db404f8ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 387,
          "cache_read_input_tokens": 27291,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1355,
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

_source line 13 · 2026-05-14T11:01:49.422Z_

<details><summary>↩ Tool result · `toolu_01Rayi36ucuj8b198puWLjsz`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	Calibration uses 64 sequences of 2048 tokens from WikiText-2 train.
21	
22	\paragraph{Compression and constraint.}
23	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
24	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
25	
26	\paragraph{Baselines.}
27	We compare against:
28	(1)~uniform 4-bit quantization;
29	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
30	(3)~unconstrained MCKP allocation;
31	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
32	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
33	
34	\subsection{Main Results}
35	\label{sec:main_results}
36	
37	\begin{table}[t]
38	\centering
39	\small
40	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$); Table~\ref{tab:heuristic} uses $k{=}16$ for fair comparison with heuristic baselines under the same constraint.}
41	\label{tab:main_results}
42	\begin{tabular}{lcccccc}
43	\toprule
44	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
45	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
46	\midrule
47	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23} \\
48	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
49	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
50	\bottomrule
51	\end{tabular}
52	\end{table}
53	
54	Table~\ref{tab:main_results} summarizes the main results.
55	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
56	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
57	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
58	The constraint eliminates this failure mode entirely.
59	
60	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
61	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
62	
63	On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\%).
64	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
65	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
66	
67	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
68	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
73	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
74	\label{fig:allocation}
75	\end{figure}
76	
77	\subsection{Budget Sweep}
78	\label{sec:budget_sweep}
79	
80	\begin{table}[t]
81	\centering
82	\small
83	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
84	\label{tab:budget_sweep}
85	\begin{tabular}{cccc}
86	\toprule
87	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
88	\midrule
89	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
90	4$\times$ & 15.45 & 11.23 & $+$4.21 \\
91	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
96	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
97	
98	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
99	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
100	
101	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
102	Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
103	
104	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
105	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
106	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
107	
108	\subsection{Heuristic Baselines}
109	\label{sec:heuristic}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use the same $k$ per model ($k{=}8$ for Qwen, $k{=}16$ for Llama/Mistral).}
115	\label{tab:heuristic}
116	\begin{tabular}{lcccc}
117	\toprule
118	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
119	 & & Median & Mean$\pm$Std & Positional \\
120	\midrule
121	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
122	Llama-3.1-8B    & 8.45  & 10.04 & 10.48$\pm$1.03 & 9.94 \\
123	Mistral-7B-v0.3 & 7.32  & 7.59  & 7.56$\pm$0.09  & 7.48 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
129	
130	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
131	
132	On Llama, the gap is larger: MCKP achieves 8.45 vs.\ L0-random median 10.04.
133	The high variance of L0-random on this architecture (std$=$1.03) indicates that 2-bit assignment is position-sensitive on 256-head models, making random selection unreliable.
134	The naive positional heuristic (9.94) performs better than random but still 1.49 PPL worse than MCKP, confirming that depth alone is an imperfect proxy for head sensitivity.
135	
136	On Mistral, the gap is small (7.32 vs.\ 7.59), consistent with the low heterogeneity observed in \S\ref{sec:main_results}.
137	The low L0-random variance (std$=$0.09) further confirms that head sensitivities are nearly uniform, so the choice of which heads receive 2-bit has little impact.
138	All non-uniform strategies (MCKP 7.32, naive 7.48, L0-random 7.56) are worse than uniform 4-bit (7.13) on this architecture, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
139	
140	\subsection{Downstream Evaluation}
141	\label{sec:downstream}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
147	\label{tab:downstream}
148	\begin{tabular}{lcccc}
149	\toprule
150	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
151	 & (bf16) & (4-bit) & (Ours) & Uniform \\
152	\midrule
153	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
154	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
155	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
156	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
157	\midrule
158	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
164	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
165	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
166	
167	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa38fc59-5611-47d6-8a2b-e20db404f8ae",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "3400b8f0-e77a-4cf9-a189-502cc5a18244",
  "sourceToolAssistantUUID": "aa38fc59-5611-47d6-8a2b-e20db404f8ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T11:01:49.488Z_

<details open><summary>🔧 Tool call — Read · `toolu_014pfFpvbHYSEYdGJE9rSvtk`</summary>

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
  "parentUuid": "3400b8f0-e77a-4cf9-a189-502cc5a18244",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M6raENHf5kvSz3h4wW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22d832db-6140-4c2f-b22e-61947ca564a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 387,
          "cache_read_input_tokens": 27291,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1355,
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

_source line 15 · 2026-05-14T11:01:49.501Z_

<details><summary>↩ Tool result · `toolu_014pfFpvbHYSEYdGJE9rSvtk`</summary>

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
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression.}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3 & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a practical decision procedure for practitioners:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	
64	\subsection{Aggressive Compression Amplifies Benefit}
65	\label{sec:aggressive}
66	
67	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
68	At more aggressive compression ratios, the picture changes.
69	
70	At $5.3\times$ compression (budget ratio 0.1875, average 3 bits), constrained MCKP provides large improvements on both architectures.
71	On Llama, constrained MCKP achieves 57.60 PPL vs.\ uniform 2-bit at 2643.77---a $45\times$ reduction.
72	On Mistral, the gap is comparable: 11.91 vs.\ 519.11 ($44\times$).
73	The consistency of this ratio across architectures ($45\times$ vs.\ $44\times$) indicates that the constrained allocation's protection mechanism is architecture-independent.
74	
75	At $8\times$ compression (budget ratio 0.125), the benefit narrows.
76	Llama: 2372.33 vs.\ 2643.77 (both catastrophic).
77	Mistral: 399.90 vs.\ 519.11 ($1.3\times$ better, but neither is usable).
78	
79	The mechanism is clear: $5.3\times$ compression forces extensive use of 2-bit heads, and constrained allocation protects the sensitive heads from 2-bit assignment.
80	At $4\times$, the budget is generous enough that uniform 4-bit already works well for low-heterogeneity models.
81	At $8\times$, the budget is too constrained for any allocation to preserve quality.
82	The intermediate regime ($5.3\times$) is where constrained allocation provides the largest relative benefit.
83	
84	\subsection{Profiling Resolution}
85	\label{sec:profiling_resolution}
86	
87	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
88	
89	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
90	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
91	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
92	
93	The additional signal changes 8 of 112 head assignments.
94	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
95	
96	\subsection{KV Separation Ablation}
97	\label{sec:kv_separation}
98	
99	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
100	
101	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
102	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
103	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
104	
105	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
106	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
107	
108	Joint allocation is sufficient under the current constraint formulation.
109	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22d832db-6140-4c2f-b22e-61947ca564a2",
  "isSidechain": true,
  "promptId": "041662c8-a838-4bbf-a14e-98e8b8a8b38a",
  "agentId": "aa1bc34633d90da83",
  "type": "user",
  "uuid": "2f57174a-7934-4fb2-b697-9ceb0a54326e",
  "sourceToolAssistantUUID": "22d832db-6140-4c2f-b22e-61947ca564a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-14T11:02:21.924Z_

Perfect! I've extracted the key claims, numbers, and terminology from the paper. Here's a comprehensive report:

## EXTRACTED KEY CLAIMS, NUMBERS, AND TERMINOLOGY

### **ABSTRACT (abstract.tex)**

**Exact Numbers:**
- Unconstrained greedy: **32.45 PPL** (Qwen2.5-7B, 4× compression)
- Unconstrained MCKP: **36.92 PPL** (Qwen2.5-7B, 4× compression)
- Uniform 4-bit baseline: **15.45 PPL** (Qwen2.5-7B, 4× compression)
- Constrained allocation (OUR METHOD): **11.23 PPL** (Qwen2.5-7B, 4× compression)
- **27.3% reduction** over uniform 4-bit
- Cardinality constraint: **k=8** (7% of heads on Qwen2.5-7B's 112 KV heads)
- Llama-3.1-8B: **8.45 vs 8.47 PPL** (marginal 0.2% improvement)
- Mistral-7B-v0.3: **7.16 vs 7.13 PPL** (slightly counterproductive)
- Heterogeneity diagnostic: top-5% concentration **0.59–0.66** (beneficial, Qwen), **0.34–0.59** (marginal, Llama), **0.42** (counterproductive, Mistral)

**Key Terminology:**
- "2-bit distortion compounding"
- "Per-head mixed-precision quantization"
- "Hardware-aligned bit-widths {2, 4, 8, 16}"
- "Cardinality constraint"
- "Heterogeneity diagnostic"
- "Constrained greedy" and "constrained MCKP"

**Key Claims:**
1. Non-additivity of distortions when many 2-bit heads are used simultaneously
2. Cardinality constraint is "minimal sufficient fix"
3. Constraint makes solver choice irrelevant (identical allocations across solvers)
4. Simple O(H log H) greedy algorithm suffices when constrained

---

### **INTRODUCTION (introduction.tex)**

**Exact Numbers (same as abstract plus context):**
- Qwen2.5-7B at 4× compression: **68–75 heads assigned to 2-bit** (unconstrained)
- Layer-0 distortion on Qwen: L0H0 increases PPL by **31.9%** (9.81→12.94), L0H2 by **23.2%**, L0H3 by **11.7%**
- Additive model predicts **~11 PPL** but actual is **3–4× higher** (32–37 PPL)
- Unconstrained greedy: **32.45 PPL**; MCKP: **36.92 PPL**
- Constrained allocation: **11.23 PPL** with k=8 (7% of 112 heads)
- **27.3% reduction** compared to uniform 4-bit
- Per-head solvers across 3 architectures: **Δ=0.0000** (identical allocations)
- Llama-3.1-8B: **8.45 vs 8.47** (0.2% improvement)
- Mistral-7B-v0.3: **7.16 vs 7.13** (slightly worse)
- Top-5% concentration: Qwen **0.59–0.66**, Llama **0.34–0.59**, Mistral **0.42**

**Key Terminology:**
- "Per-head mixed-precision quantization"
- "Rate-distortion optimization"
- "Polymatroid structure"
- "Multiple-choice knapsack (MCKP)"
- "2-bit distortion compounding"
- "Additive distortion assumption"
- "Head sensitivity heterogeneity"
- "Concentration of per-head distortion"

**Key Claims:**
1. Greedy is optimal for consecutive bit-widths but fails for {2,4,8,16}
2. Root cause is "2-bit distortion compounding," not solver suboptimality
3. Distortion from 2-bit heads compounds **non-additively** through residual stream
4. Single cardinality constraint is sufficient remedy
5. Constraint makes greedy and MCKP equivalent (all 112 heads identical on Qwen, all 256 on Llama, 255/256 on Mistral)
6. Benefit depends on "head sensitivity heterogeneity"

---

### **METHOD (method.tex)**

**Exact Numbers:**
- Bit-widths: **{2, 4, 8, 16}**
- Qwen2.5-7B: **112 KV heads** (28 layers × 4 heads)
- Llama-3.1-8B: **256 KV heads** (32 layers × 8 heads)
- Mistral-7B-v0.3: **256 KV heads** (32 layers × 8 heads)
- Calibration: **64 sequences × 2048 tokens** from WikiText-2 train
- Per-head distortions at 4-bit and above: **typically below 0.1 PPL**
- Unconstrained greedy on Qwen: **68 heads to 2-bit**, achieves **32.45 PPL**
- Unconstrained MCKP on Qwen: **75 heads to 2-bit**, achieves **36.92 PPL**
- Uniform 4-bit baseline: **15.45 PPL**
- Standard-resolution profiling detects non-zero d_h(2) in **37 of 112 heads**
- Layer-0 head examples: L0H0 **31.9%** increase, L0H2 **23.2%**, L0H3 **11.7%**
- Constraint parameter k: **k=8** for Qwen2.5-7B (7% of 112 heads)
- U-shaped curve minimum: k=8 achieves **11.23 PPL**
- At k=75: **35.35 PPL** (compounding effect)
- At k=0 (uniform 4-bit): **15.45 PPL**

**Key Terminology:**
- "Multiple-choice knapsack (MCKP)"
- "Budget ratio R" (e.g., 0.25 for 4× compression)
- "Per-head distortion function d_h(b)"
- "Polymatroid structure"
- "Additive distortion assumption"
- "Cardinality constraint"
- "Compounding effect"
- "Residual stream"

**Key Claims:**
1. Profiling measures PPL increase when head is quantized to each bit-width
2. Additive assumption holds for 4-bit and 8-bit (distortions typically <0.1 PPL)
3. At 2-bit, distortions are "orders of magnitude larger"
4. When many 2-bit heads simultaneously quantize, errors accumulate through residual stream
5. Cardinality constraint is "single linear inequality, compatible with any solver"
6. Layer-0 heads don't require explicit protection—profiler signal is sufficient

---

### **EXPERIMENTS (experiments.tex)**

**Exact Numbers (Main Results Table):**
- **Qwen2.5-7B:**
  - Baseline (bf16): **9.81 PPL**
  - Uniform 4-bit: **15.45 PPL**
  - Unconstrained greedy: **32.45 PPL**
  - Unconstrained MCKP: **36.92 PPL**
  - Ours (constrained): **11.23 PPL** (standard profiling)
  - Hires profiling: **10.91 PPL**

- **Llama-3.1-8B:**
  - Baseline (bf16): **8.09 PPL**
  - Uniform 4-bit: **8.47 PPL**
  - Ours (constrained, hires): **8.45 PPL**

- **Mistral-7B-v0.3:**
  - Baseline (bf16): **7.04 PPL**
  - Uniform 4-bit: **7.13 PPL**
  - Ours (constrained, hires): **7.16 PPL**

**Budget Sweep (Qwen2.5-7B):**
- 2× compression: Uniform **10.10 PPL**, Constrained **10.66 PPL** (−0.56)
- 4× compression: Uniform **15.45 PPL**, Constrained **11.23 PPL** (+4.21)
- 8× compression: Uniform **14,759 PPL**, Constrained **907 PPL** (+13,852 gap)

**Heuristic Baselines (4× compression):**
- **Qwen2.5-7B:** MCKP **11.23**, L0-random median **11.52**, naive positional **12.23**
- **Llama-3.1-8B:** MCKP **8.45**, L0-random median **10.04**, naive positional **9.94**
- **Mistral-7B-v0.3:** MCKP **7.32**, L0-random median **7.59**, naive positional **7.48**

**Downstream Evaluation (Qwen2.5-7B, 4× compression):**
- ARC-Challenge: Uniform **0.482** → MCKP **0.514** (+3.2 pts)
- HellaSwag: Uniform **0.728** → MCKP **0.768** (+4.0 pts)
- PIQA: Uniform **0.766** → MCKP **0.779** (+1.3 pts)
- WinoGrande: Uniform **0.662** → MCKP **0.682** (+2.0 pts)
- Average: **0.660 → 0.686** (+2.6 pts, **73% of accuracy lost by uniform recovered**)

**Key Terminology:**
- "Grouped-query attention (GQA) ratio" (7:1 for Qwen, 4:1 for Llama/Mistral)
- "WikiText-2 test split" (298,938 tokens)
- "0-shot prompting"
- "Unconstrained allocation"
- "Layer-0 protection"

**Key Claims:**
1. On Qwen: constrained MCKP achieves **27.3% reduction** over uniform
2. Unconstrained methods fail "catastrophically"
3. On Llama/Mistral: unconstrained results omitted (only tested on Qwen)
4. Llama shows "low sensitivity heterogeneity"
5. Mistral's sliding-window attention may contribute to uniformity
6. Downstream gains transfer (73% accuracy recovery on downstream tasks)

---

### **ANALYSIS (analysis.tex)**

**Exact Numbers:**

**Heterogeneity Table:**
- **Qwen2.5-7B (7:1 GQA):** Top-5% concentration **0.59–0.66**, Δ PPL uniform **+5.64**, ours **+1.42** (27.3% improvement)
- **Llama-3.1-8B (4:1 GQA):** Top-5% concentration **0.34–0.59**, Δ PPL uniform **+0.38**, ours **+0.36** (marginal)
- **Mistral-7B-v0.3 (4:1 GQA):** Top-5% concentration **0.42**, Δ PPL uniform **+0.10**, ours **+0.13** (counterproductive)

**Aggressive Compression (5.3× compression, 3 bits average):**
- **Llama:** Constrained MCKP **57.60 PPL** vs. uniform 2-bit **2643.77** (**45× reduction**)
- **Mistral:** Constrained **11.91** vs. uniform 2-bit **519.11** (**44× reduction**)
- Consistency ratio: **45× vs 44×** across architectures

**8× Compression:**
- **Llama:** **2372.33 vs 2643.77** (both catastrophic)
- **Mistral:** **399.90 vs 519.11** (1.3× better, neither usable)

**Profiling Resolution:**
- Standard (16 seq × 512 tok): **11.23 PPL**
- High-res (64 seq × 2048 tok): **10.91 PPL** (−0.32 absolute, −1.10 relative to bf16)
- Standard detects non-zero d_h(2) in **37 of 112 heads**
- High-res detects **100 of 112** (2.7× more)
- Changes **8 of 112** head assignments

**K/V Separation Ablation:**
- Joint allocation: **10.91 PPL**
- Separated K/V: **11.22 PPL** (+0.31 worse)
- Heads with K≠V asymmetry: **21 of 112**
- All asymmetries: K receiving lower bit-width than V

**Key Terminology:**
- "Top-5% concentration metric"
- "Head sensitivity heterogeneity"
- "Per-head 2-bit distortions d_h(2)"
- "Layer-0 concentration"
- "Protection mechanism"
- "Diagnostic framework"
- "K cache" vs "V cache" (key vs value)

**Key Claims:**
1. High heterogeneity (>0.50) → non-uniform beneficial (27.3% Qwen)
2. Moderate (0.30–0.50) → marginal (0.2% Llama)
3. Low/near-zero → counterproductive (Mistral)
4. Diagnostic adds "no computational overhead"
5. At 5.3× compression, constraint provides "large improvements" (45–44× better)
6. At 4×: budget generous enough for low-heterogeneity models
7. At 8×: budget too constrained for any allocation
8. High-res profiling detects 2.7× more heads with non-zero distortion
9. K caches more compressible than V (K encodes position, V carries content)

---

## SUMMARY FOR CONCLUSION CONSISTENCY CHECK

**Critical Numbers to Maintain Consistency:**
- Main result: **11.23 PPL** (Qwen, 4×, constrained)
- Improvement: **27.3%** over uniform 4-bit (**15.45 PPL**)
- Unconstrained failure: **32.45 (greedy)** and **36.92 (MCKP) PPL**
- Cardinality constraint: **k≤8** (7% of 112 heads)
- Solver equivalence: **Δ=0.0000** exact match across architectures
- Downstream recovery: **73%** of accuracy lost

**Critical Terminology to Use Consistently:**
- "2-bit distortion compounding" (the core problem)
- "Cardinality constraint on 2-bit assignments" (the fix)
- "Per-head mixed-precision quantization"
- "Hardware-aligned bit-widths {2,4,8,16}"
- "Heterogeneity diagnostic" (top-5% concentration metric)
- "Architectures tested" (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3)

This comprehensive extraction should help ensure your Conclusion section aligns with all claims, numbers, and terminology throughout the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f57174a-7934-4fb2-b697-9ceb0a54326e",
  "isSidechain": true,
  "agentId": "aa1bc34633d90da83",
  "requestId": "req_011Cb2M77JzsxXVb23crVSR6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "200e758f-a5e9-454c-b21b-0efd4dbc8cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KPFXzYDYpNWxmiTPbTkopn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 28646,
      "output_tokens": 3936,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3936,
          "cache_read_input_tokens": 28646,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12126,
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
