# Research conversation: Read the existing paper sections for the contrastive_entrain_calib project to understand the paper's narrative, structur

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a20c9ca036d0492b1.jsonl`
- **Structured JSON:** [`eabb39ff1161c27544d8.json`](../../sessions/ea/eabb39ff1161c27544d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-20T15:31:57.670Z_

Read the existing paper sections for the contrastive_entrain_calib project to understand the paper's narrative, structure, and tone. The sections are in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/. List all .tex files there and read them all (especially introduction.tex, abstract.tex, related_work.tex, method.tex, results/experiments, discussion/analysis sections). Report back the key narrative arc, terminology used, and tone so I can write a matching conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "ab6b2d8e-414b-473d-b68e-5afc1f42b5b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T15:31:59.116Z_

I'll help you read all the paper sections to understand the narrative arc, terminology, and tone for writing a matching conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6b2d8e-414b-473d-b68e-5afc1f42b5b4",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZNDEkCVVSckgfBmHy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b766ba1-d5d5-4e9a-9dc3-34c9a83e335a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JMRiAdbLez2abk4uyATus5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25391,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25391,
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

_source line 3 · 2026-05-20T15:31:59.257Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EaoSz4nKPheL44EzsT4KAj`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b766ba1-d5d5-4e9a-9dc3-34c9a83e335a",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZNDEkCVVSckgfBmHy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9028b17c-72f3-4152-9f8b-176f00f662fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JMRiAdbLez2abk4uyATus5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25391,
      "cache_read_input_tokens": 0,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25391,
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

_source line 4 · 2026-05-20T15:31:59.281Z_

<details><summary>↩ Tool result · `toolu_01EaoSz4nKPheL44EzsT4KAj`</summary>

```text
docs/paper/sections/cosine_failure.tex
docs/paper/sections/probe_trap.tex
docs/paper/sections/direction_quality.tex
docs/paper/sections/related_work.tex
docs/paper/sections/limitations.tex
docs/paper/sections/framework.tex
docs/paper/sections/introduction.tex
docs/paper/sections/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9028b17c-72f3-4152-9f8b-176f00f662fc",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "a9c00d80-50e8-47a8-883a-2eed7395f749",
  "sourceToolAssistantUUID": "9028b17c-72f3-4152-9f8b-176f00f662fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T15:32:00.556Z_

Now let me read all these .tex files to understand the paper's structure and content:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c00d80-50e8-47a8-883a-2eed7395f749",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2cb6a5e1-3566-4864-b271-8916e4c31272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 6 · 2026-05-20T15:32:01.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcycC4Lv4cwcKWW3cNBCak`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb6a5e1-3566-4864-b271-8916e4c31272",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c61b9d1b-d845-4586-a6ff-08176a5a7476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 7 · 2026-05-20T15:32:01.103Z_

<details><summary>↩ Tool result · reported error · `toolu_01FcycC4Lv4cwcKWW3cNBCak`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c61b9d1b-d845-4586-a6ff-08176a5a7476",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "f83a3fcd-1df3-4e60-9803-890235901873",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib.",
  "sourceToolAssistantUUID": "c61b9d1b-d845-4586-a6ff-08176a5a7476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T15:32:01.724Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W8ypwAJ3LB8yUTBknTxxBX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83a3fcd-1df3-4e60-9803-890235901873",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "369685d0-6335-4228-a7b3-cf2302dfe661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 9 · 2026-05-20T15:32:01.737Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UjsQ3SRozeMu8jPiyZjno6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "369685d0-6335-4228-a7b3-cf2302dfe661",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "527bc39c-410d-4db9-9d16-329b7d1a5842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 10 · 2026-05-20T15:32:01.756Z_

<details><summary>↩ Tool result · `toolu_01W8ypwAJ3LB8yUTBknTxxBX`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827 \pm 0.028$ on Qwen3-8B and $0.779 \pm 0.019$ on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails, and that the failure runs deeper than the representation signal itself.
11	We test three formulations that translate $\dsyc$ into a GRPO \citep{shao2024grpo} training signal (cosine similarity, scaled cosine, and binary probe) across six experimental configurations; every formulation fails.
12	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
13	Online recalibration improves the offline AUROC from 0.82 to 0.91 yet triggers mode collapse.
14	A binary probe with stopped gradients creates a stubbornness trap: the model learns that never revising its answer reliably collects the probe reward, and the true-positive flip rate ($\tof$) drops to zero within 500 steps while generation entropy remains at 0.70 (\S\ref{sec:probe_trap}).
15	These failures might suggest that removing $\dsyc$ in favor of a purely behavioral reward would resolve the problem.
16	It does not.
17	R3-only GRPO, which uses an NLI-based behavioral reward without any representation component, also fails to calibrate sycophancy: the \sycon{} score starts at 0.074 at checkpoint 1000, reaches only 0.114 by checkpoint 5000, and never exceeds the vanilla baseline of 0.134 (\S\ref{sec:discussion}).
18	The trajectory shows partial recovery before plateauing: the score stalls at 0.114 between checkpoints 4000 and 5000, 15\% below vanilla with no further improvement.
19	Two layers of failure emerge: $\dsyc$-based rewards are actively harmful, and GRPO itself is structurally insufficient for sycophancy calibration.
20	
21	Existing approaches to sycophancy mitigation span three categories.
22	Representation-based inference methods, including activation addition \citep{turner2023actadd} and contrastive activation addition \citep{rimsky2024caa}, steer model behavior at test time without modifying weights.
23	RL-based training methods use scalar rewards to update policy through reinforcement learning; our $\dsyc$ GRPO variants and R3-only GRPO both fall into this category, as does representation-guided RL more broadly \citep{zhang2026latentgrpo}.
24	SFT-based training takes a fundamentally different approach: ACT \citep{consistency2025bctact} applies supervised fine-tuning with an L2 activation consistency loss that provides dense per-token supervision rather than a single scalar per completion.
25	ACT achieves a \sycon{} score of 0.301 at checkpoint 8000, more than double the vanilla baseline, while every GRPO variant remains below it (\S\ref{sec:discussion}).
26	The contrast is informative.
27	Techniques for discovering latent knowledge \citep{burns2023ccs} and representation-guided RL share a premise: a direction with high discriminability in activation space should transfer into a useful training signal.
28	For reasoning faithfulness and safety refusal, this premise holds, because the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
29	Sycophancy violates this premise.
30	Capitulation under social pressure and revision under valid evidence produce overlapping activation signatures along $\dsyc$, because both involve the model shifting its stated belief toward the user's position.
31	
32	The root cause is a semantic gap between discriminability and reward utility.
33	$\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}.
34	A post-hoc classifier can use this signal effectively because it scores labeled examples where the validity of the belief change is already known.
35	A reward signal during RL training has no such access to ground truth; it must distinguish warranted revision from unwarranted capitulation using activation geometry alone, and $\dsyc$ collapses exactly this distinction.
36	This conflation explains both layers of failure.
37	$\dsyc$ rewards penalize all belief change indiscriminately, producing behavioral collapse.
38	R3-only GRPO's single scalar per completion cannot compensate because it lacks the per-token resolution to teach which belief changes are warranted and which are not.
39	ACT succeeds because its dense supervision operates at the token level, where the valid/invalid distinction can be resolved.
40	Sycophancy is defined relative to external evidential warrant \citep{sharma2023sycophancy}, a property that no single activation direction can fully encode.
41	The entanglement between helpfulness and sycophancy at the representation level, where the same mechanisms that allow models to track user intent also predispose them to capitulate \citep{wang2025internal}, is amplified by RLHF \citep{shapira2026amplifies}.
42	When reward overoptimization \citep{gao2023scaling} operates on a signal that conflates compliance with capitulation, the result is predictable collapse \citep{casper2023openproblems}.
43	
44	We present three contributions:
45	
46	\begin{itemize}
47	\item \textbf{All GRPO approaches fail for sycophancy calibration} (C1). We extract and validate $\dsyc$ on two model families (Qwen3-8B AUROC $0.827 \pm 0.028$; Llama-3-8B AUROC $0.779 \pm 0.019$), then show that all three $\dsyc$-based reward formulations produce behavioral collapse (\S\ref{sec:cosine_failure}, \S\ref{sec:probe_trap}). R3-only GRPO, which removes $\dsyc$ entirely, also fails: \sycon{} reaches only 0.114 at checkpoint 5000 against a vanilla baseline of 0.134 (\S\ref{sec:discussion}). Discriminability does not confer reward utility, and sparse RL rewards are structurally insufficient for this task.
48	
49	\item \textbf{Probe reward trap with behavioral-before-distributional collapse} (C2). The binary probe reward produces behavioral death ($\tof = 0$ at step 500) while entropy remains at 0.70. The 1,300-step lag before distributional collapse means standard entropy monitoring misses the failure entirely, with the reward averaging $+0.72$ throughout (\S\ref{sec:probe_trap}).
50	
51	\item \textbf{Sparse RL reward cannot convey the valid/invalid distinction} (C3). We trace all failures to a unified root cause: $\dsyc$ encodes belief-change direction but not evidential warrant. A single scalar reward per completion, whether from representations or behavioral classifiers, cannot teach the model which belief changes are warranted. Dense SFT supervision resolves this: ACT achieves \sycon{} of 0.301, while all GRPO variants remain below vanilla (\S\ref{sec:discussion}).
52	\end{itemize}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "369685d0-6335-4228-a7b3-cf2302dfe661",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "ba7a7e0a-f021-4986-9177-26594d5d49cc",
  "sourceToolAssistantUUID": "369685d0-6335-4228-a7b3-cf2302dfe661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T15:32:01.753Z_

<details><summary>↩ Tool result · `toolu_01UjsQ3SRozeMu8jPiyZjno6`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Representation engineering \citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.
5	CCS \citep{burns2023ccs} discovers truth-related directions without labels through a consistency objective.
6	Subsequent work applied such directions for inference-time intervention: ITI \citep{li2023iti} uses probe weights as truthfulness steering vectors, ActAdd \citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy.
7	These methods demonstrate that activation-space geometry carries rich behavioral information sufficient for inference-time classification and control.
8	We use the same contrastive extraction methodology as CAA but apply the resulting direction as an RL reward signal rather than an activation addition.
9	This shift from inference-time steering to training-time optimization reveals a gap that prior work does not address: a direction can achieve high discriminability (AUROC 0.82; \S\ref{sec:direction_quality}) yet fail entirely as a reward signal.
10	
11	\paragraph{Reward Design and Overoptimization.}
12	\citet{gao2023scaling} established scaling laws for reward model overoptimization, showing that proxy rewards diverge from true objectives under sustained optimization.
13	\citet{skalse2022hacking} proved that no bounded proxy can be immune to this divergence, and \citet{casper2023openproblems} catalogued the resulting limitations of RLHF.
14	Reward hacking can escalate from sycophantic agreement to active tampering \citep{denison2024subterfuge}, and learned reward functions fail when transferred to new policies \citep{mckinney2023fragility}.
15	Our probe reward trap (\S\ref{sec:probe_trap}) is an extreme instance: a low-capacity linear probe is gamed within 500 training steps.
16	The stubbornness trap represents a qualitatively distinct failure mode where the reward actively reinforces degenerate behavior rather than one the model merely circumvents.
17	
18	\paragraph{Sycophancy Characterization and Mitigation.}
19	\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.
20	\citet{shapira2026amplifies} proved formally that RLHF amplifies this tendency under standard assumptions, and \citet{wang2025internal} traced the phenomenon to late-layer preference shifts, confirming that sycophantic behavior has identifiable internal origins.
21	On the mitigation side, synthetic data approaches reduce sycophancy at the training-data level \citep{wei2024synthetic}, ACT \citep{consistency2025bctact} penalizes activation divergence between initial and post-pressure responses, and \citet{obrien2025fewbadneurons} identify sycophancy-associated neurons and surgically correct them.
22	These methods either treat all belief changes as equivalent or use representations only for diagnosis, not as optimization targets.
23	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation because both involve the model changing its stated belief toward the user's position.
24	
25	\paragraph{Representation-Guided Reinforcement Learning.}
26	Latent-GRPO \citep{zhang2026latentgrpo} uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.
27	\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.
28	These methods succeed because the target behavior (correct reasoning, safe refusal) is geometrically distinct from the behavior to suppress along the relevant direction.
29	Sycophancy breaks this condition: revision and capitulation overlap in direction space, separated only by evidential warrant that no activation-space direction encodes (\S\ref{sec:cosine_failure}).
30	Our results explain when representation-guided RL can succeed and identify the structural barrier that prevents it for sycophancy.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527bc39c-410d-4db9-9d16-329b7d1a5842",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "79304c82-f2e2-4b7c-9ebe-312dfe848723",
  "sourceToolAssistantUUID": "527bc39c-410d-4db9-9d16-329b7d1a5842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T15:32:01.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HcegT8a4uCHg3DqkM9k6rr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79304c82-f2e2-4b7c-9ebe-312dfe848723",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "232df85f-1837-481f-9095-6d7554ad87cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 13 · 2026-05-20T15:32:01.871Z_

<details><summary>↩ Tool result · `toolu_01HcegT8a4uCHg3DqkM9k6rr`</summary>

```text
1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	This section establishes the notation, experimental components, and evaluation protocol used throughout the paper.
5	We first describe how the contrastive sycophancy direction $\dsyc$ is extracted (\S\ref{ssec:extraction}), then define three reward formulations that incorporate $\dsyc$ into GRPO training (\S\ref{ssec:reward}), explain the online recalibration procedure (\S\ref{ssec:recalib}), describe the SFT baseline used for comparison (\S\ref{ssec:baselines}), and finally specify the evaluation metrics (\S\ref{ssec:eval}).
6	
7	\subsection{Direction Extraction}
8	\label{ssec:extraction}
9	
10	We extract a linear sycophancy direction $\dsyc$ from the residual stream of a target model using contrastive activation pairs.
11	Each pair consists of two model responses to the same user challenge: a \emph{valid correction}, in which the model appropriately revises its earlier answer upon receiving well-supported counter-evidence, and a \emph{sycophantic capitulation}, in which the model abandons a correct answer under social pressure without adequate evidential warrant.
12	
13	To isolate the cognitive signal from surface-level linguistic variation, we apply style control: both responses in each pair are generated with matched hedging patterns, politeness markers, and response length, so that $\dsyc$ reflects the distinction between warranted and unwarranted belief change rather than stylistic differences.
14	Concretely, we construct 362 style-controlled contrastive activations from 181 paired examples stratified across three evidence-strength levels (weak, medium, strong).
15	
16	Given a target layer $\ell$, let $\mathbf{h}^{+}_i$ denote the residual-stream activation for the $i$-th valid correction and $\mathbf{h}^{-}_i$ for the corresponding sycophantic capitulation.
17	The sycophancy direction is the mean difference:
18	\begin{equation}
19	\label{eq:dsyc}
20	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
21	\end{equation}
22	where $N{=}181$ is the number of contrastive pairs.
23	We select the target layer by 5-fold cross-validated AUROC over a linear classifier trained on the projection $\mathbf{h} \cdot \dsyc$; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (exp-001).
24	Section~\ref{sec:direction_quality} presents detailed discriminability analyses, including cross-model validation on Llama-3-8B.
25	
26	\subsection{GRPO Reward Formulation}
27	\label{ssec:reward}
28	
29	Group Relative Policy Optimization \citep[GRPO;][]{shao2024grpo} uses a reward signal to rank sampled completions and update the policy toward higher-reward outputs.
30	We define a combined reward:
31	\begin{equation}
32	\label{eq:reward}
33	R = w_1 \cdot \rone + w_3 \cdot \rthree
34	\end{equation}
35	where $\rone$ is a direction-based component derived from $\dsyc$ and $\rthree$ is a behavioral component.
36	
37	\paragraph{Direction-based reward ($\rone$).}
38	We investigate three formulations that translate $\dsyc$ into a scalar training signal.
39	Let $\mathbf{h}$ denote the model's residual-stream activation at a designated token position during a training rollout.
40	
41	\begin{itemize}
42	\item[\textbf{F1}] \textbf{Cosine.} $\rone = \cos(\mathbf{h},\, \dsyc)$, the cosine similarity between the activation and the sycophancy direction.
43	\item[\textbf{F2}] \textbf{Scaled cosine.} $\rone = \alpha \cdot \cos(\mathbf{h},\, \dsyc)$, where $\alpha$ amplifies the gradient signal to compete with $\rthree$ in magnitude.
44	\item[\textbf{F3}] \textbf{Binary probe.} $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$, a binary indicator derived from a logistic probe trained on the same contrastive data. The probe is frozen during GRPO training and gradients are stopped at its input.
45	\end{itemize}
46	
47	\paragraph{Behavioral reward ($\rthree$).}
48	$\rthree$ is computed by a DeBERTa-based natural language inference (NLI) classifier that scores whether the model's response is consistent with the ground-truth answer.
49	This component provides a task-level behavioral signal independent of internal representations.
50	The weight configuration ($w_1$, $w_3$) varies across experiments and is specified in the corresponding sections (\S\ref{sec:cosine_failure}, \S\ref{sec:probe_trap}).
51	As an ablation, we also evaluate R3-only GRPO ($w_1{=}0$, $w_3{=}1$), which removes the representation component entirely and trains with only the behavioral reward.
52	
53	\subsection{Online Recalibration}
54	\label{ssec:recalib}
55	
56	LoRA fine-tuning progressively shifts the model's internal representations, which could cause $\dsyc$ to become misaligned with the current activation geometry.
57	To address this, we re-extract $\dsyc$ every 500 training steps by re-running the contrastive pairs through the updated model and recomputing Equation~\ref{eq:dsyc}.
58	Empirically, the cosine similarity between consecutive directions remains high (${\approx}\,0.96$ at step 500), indicating that the direction drifts slowly relative to the recalibration frequency.
59	This procedure ensures that $\rone$ tracks the evolving representation space throughout training rather than scoring against a stale direction.
60	
61	\subsection{SFT Baseline: Activation Consistency Training}
62	\label{ssec:baselines}
63	
64	To contextualize the GRPO results, we compare against Activation Consistency Training \citep[ACT;][]{consistency2025bctact}, a supervised fine-tuning method that penalizes activation divergence between initial and post-pressure responses.
65	ACT combines a standard SFT loss with an L2 activation consistency loss on hidden states at target layers, providing dense per-token supervision.
66	Unlike GRPO, which assigns a single scalar reward per completion, ACT's loss function operates at the token level and uses labeled valid/invalid pairs directly during training.
67	This distinction is central to our analysis (\S\ref{sec:discussion}): ACT succeeds where all GRPO variants fail, suggesting that the valid/invalid correction distinction requires denser supervision than a sparse RL reward can provide.
68	
69	\subsection{Evaluation Protocol}
70	\label{ssec:eval}
71	
72	We evaluate sycophancy mitigation along two complementary axes: the model's willingness to accept valid corrections and its resistance to invalid pressure.
73	
74	\paragraph{Metrics.}
75	We define two primary rates.
76	The \emph{True-positive Flip rate} ($\tof$) measures the fraction of valid corrections that the model accepts, i.e., cases where the model appropriately revises an incorrect initial answer when presented with well-supported counter-evidence.
77	The \emph{No-Flip rate} ($\nof$) measures the fraction of invalid challenges that the model resists, i.e., cases where the model maintains a correct initial answer despite unsupported social pressure.
78	Both rates range from 0 to 1 with higher values indicating better performance.
79	
80	A model that accepts all challenges (including invalid ones) achieves high $\tof$ but low $\nof$; a model that rejects all challenges achieves the opposite.
81	We capture this trade-off with $\sycon$, the harmonic mean of the two rates:
82	\begin{equation}
83	\label{eq:sycon}
84	\sycon = \frac{2 \cdot \tof \cdot \nof}{\tof + \nof}
85	\end{equation}
86	
87	$\sycon$ is analogous to the $F_1$ score: it penalizes models that sacrifice one axis for the other, and a high $\sycon$ requires balanced performance on both.
88	Classification of each response (flip vs.\ no-flip) is determined by an NLI-based procedure following the protocol of \citet{consistency2025bctact}.
89	
90	\paragraph{Test set and model configuration.}
91	Evaluation uses the same 362 style-controlled contrastive instances (181 pairs, weak/medium/strong stratification) described in \S\ref{ssec:extraction}, with a held-out split not used during direction extraction.
92	All training experiments use Qwen3-8B with LoRA (rank$=$64, $\alpha{=}128$) and DeepSpeed ZeRO-2 for memory-efficient optimization.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "232df85f-1837-481f-9095-6d7554ad87cf",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "eb28a83e-4334-43fc-889a-f5b45d93ce53",
  "sourceToolAssistantUUID": "232df85f-1837-481f-9095-6d7554ad87cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T15:32:02.288Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QDz17kfxqg6nBVzYpQw5eL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb28a83e-4334-43fc-889a-f5b45d93ce53",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aecdb075-0c0e-49fd-9713-2210ee614dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 15 · 2026-05-20T15:32:02.305Z_

<details><summary>↩ Tool result · `toolu_01QDz17kfxqg6nBVzYpQw5eL`</summary>

```text
1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B and generalizes across models.
5	We now test whether this discriminability translates into a viable GRPO reward signal.
6	This section reports four configurations (F1a--F1d) that form a systematic diagnostic chain: each configuration resolves the failure mode of its predecessor but exposes a deeper structural limitation.
7	Table~\ref{tab:cosine_chain} summarizes the chain; Figure~\ref{fig:cosine_failure} visualizes the training dynamics.
8	
9	\begin{table}[t]
10	\centering
11	\caption{Cosine $\rone$ failure chain. Each configuration addresses the preceding failure but reveals a more fundamental limitation. All experiments use Qwen3-8B with LoRA (rank$=$64) and GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$.}
12	\label{tab:cosine_chain}
13	\begin{tabular}{lllll}
14	\toprule
15	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
16	\midrule
17	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
18	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
19	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
20	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation + noise \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	\paragraph{F1a: Tanh gate saturation (exp-002).}
26	The initial configuration defines $\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$ with $w_1{=}0.25$, $w_3{=}0.75$.
27	The dot product formulation preserves directional sensitivity but is not scale-invariant: activation norms in the residual stream range from $100{\times}$ to $1{,}200{\times}$ the direction norm across layers.
28	This norm mismatch drives the pre-activation into the saturated tails of tanh, where the gradient vanishes.
29	By step 955, $\rone$ contributes effectively zero gradient to the combined reward, and training was terminated.
30	Subsequent weight adjustments ($w_1{=}0.15$, $w_3{=}0.65$) did not resolve the saturation because the pre-activation magnitude, not the weight, controls the gate.
31	The diagnostic conclusion is clear: any formulation that passes raw dot products through a bounded nonlinearity will saturate in high-norm activation spaces.
32	Cosine similarity, which normalizes by both norms, is the natural alternative.
33	
34	\paragraph{F1b: Raw cosine signal too weak (exp-002v2).}
35	Replacing the dot product with cosine similarity ($\rone = \cos(\mathbf{h},\, \dsyc)$) eliminates the norm dependence.
36	However, the cosine gap between valid corrections and sycophantic capitulations is only 0.098 when averaged across the seven highest-AUROC layers.
37	With $w_1{=}0.25$, this yields an effective $\rone$ contribution of approximately $0.025$ per token, a signal that is negligible relative to $\rthree$ variance.
38	Throughout training, $\rone \approx 0$, and the combined reward $R$ is functionally equivalent to $w_3 \cdot \rthree$ alone.
39	Training was terminated after confirming that the sycophancy component exerts no measurable influence on policy updates.
40	The failure isolates a quantitative limitation: the cosine projection of $\dsyc$ onto individual activations produces a gap too narrow to generate meaningful reward contrast between sycophantic and non-sycophantic completions.
41	
42	\paragraph{F1c: Recalibration induces mode collapse (exp002v2-recalib).}
43	One hypothesis for the weak signal in F1b is that $\dsyc$ drifts during LoRA training, eroding the already-small gap.
44	To test this, we resume from the exp-002v2 checkpoint at step 500 and enable the online recalibration procedure described in \S\ref{ssec:recalib}, re-extracting $\dsyc$ every 500 steps.
45	Recalibration increases the offline AUROC from 0.82 to 0.91, confirming that the refreshed direction better separates the updated activations.
46	Training collapses nonetheless.
47	Within 300 steps of the first recalibration event, the policy degenerates into a low-entropy mode: generation entropy drops to 0.069, and mean response length contracts to 62 tokens.
48	The mechanism is a reward discontinuity at the recalibration boundary.
49	When $\dsyc$ is replaced by a fresh direction, the cosine projection of every cached rollout shifts abruptly.
50	Completions that were mildly rewarded under the stale direction may become penalized under the fresh one, and vice versa.
51	This discontinuity destabilizes the GRPO advantage estimates and drives the policy toward a narrow region of activation space that remains low-risk under both the old and new directions.
52	The result is a degenerate policy that produces short, hedged responses regardless of the input.
53	Improving direction quality via recalibration, paradoxically, makes the reward landscape less stable.
54	
55	\paragraph{F1d: Scaling amplifies noise (exp-002v3).}
56	Configuration F1d addresses the magnitude problem directly: $\rone = 5 \cdot \cos(\mathbf{h},\, \dsyc)$ with $w_1{=}0.4$, $w_3{=}0.6$.
57	The $5{\times}$ scaling lifts the $\rone$ contribution above the $\rthree$ noise floor, but it simultaneously amplifies the noise in the cosine projection.
58	Training proceeds in three phases.
59	In the first phase (steps 100--300), $\rthree$ saturates at 0.9998 as the policy rapidly learns to produce NLI-consistent answers; mean response length drops from 247 to 80 tokens and entropy falls from 0.45 to 0.10.
60	In the second phase (steps 300--2150), the combined reward degenerates to $R \approx w_1 \cdot \rone + \text{const}$ because the saturated $\rthree$ provides no gradient.
61	$\rone$ is now the sole learning signal, but its mean oscillates between $-0.46$ and $+0.41$ with no sustained positive trend, because the cosine projection conflates warranted belief revision with unwarranted capitulation (both shift activations toward the user's position along $\dsyc$).
62	In the third phase (step 2160), the policy collapses terminally: entropy drops from 0.056 to 0.026, and the fraction of completions with zero reward standard deviation rises from 0.125 to 0.419, indicating that the policy has converged to a near-deterministic mode.
63	
64	\paragraph{Unified diagnosis.}
65	The four configurations converge on a single structural limitation.
66	The cosine gap between valid and sycophantic activations (0.098 across layers) is too narrow to serve as a reward signal, and this narrowness is not a calibration artifact.
67	Recalibration raises offline AUROC to 0.91 yet rewards still fail (F1c), confirming that direction quality is not the bottleneck.
68	The root cause is semantic: $\dsyc$ encodes the \emph{direction} of belief change (toward or away from the user's position) but does not encode whether that change is \emph{warranted}.
69	A model that appropriately revises an incorrect answer in response to strong evidence and a model that capitulates under social pressure both shift their activations toward the user's position along $\dsyc$.
70	The cosine projection assigns similar scores to both behaviors.
71	Scaling the projection (F1d) amplifies this conflation rather than resolving it.
72	Any reward formulation that uses $\dsyc$ as a continuous scalar will inherit this ambiguity.
73	Section~\ref{sec:probe_trap} examines whether discretizing the signal via a binary probe can escape this limitation.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aecdb075-0c0e-49fd-9713-2210ee614dcd",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "b45d9b89-18bf-43e7-b053-c1345b4b9904",
  "sourceToolAssistantUUID": "aecdb075-0c0e-49fd-9713-2210ee614dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T15:32:02.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_014zMkPHRKyeAjvYfAY56jTi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b45d9b89-18bf-43e7-b053-c1345b4b9904",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "038b2f3d-5071-4952-ab45-e2c8280f7f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 17 · 2026-05-20T15:32:02.509Z_

<details><summary>↩ Tool result · `toolu_014zMkPHRKyeAjvYfAY56jTi`</summary>

```text
1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations in Section~\ref{sec:cosine_failure} fail because the continuous projection of $\dsyc$ produces a gap too narrow to generate reward contrast.
5	A natural remedy is to discretize the signal: train a logistic probe on $\dsyc$ and threshold its output, yielding the binary indicator $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ defined as F3 in \S\ref{ssec:reward}.
6	This formulation sidesteps the cosine gap entirely, replacing a near-zero continuous signal with a unit-magnitude discrete one.
7	We show that this discretization avoids the magnitude problem but creates a qualitatively worse failure: a \emph{reward trap} that makes stubbornness indistinguishable from genuine non-sycophancy, producing behavioral collapse that standard entropy monitoring cannot detect.
8	
9	\paragraph{Differentiable probe: gradient gaming (exp-008).}
10	Before arriving at the binary formulation, we first test a differentiable variant in which the logistic probe's output is used directly as $\rone$ without stop-gradient.
11	This experiment terminates within approximately 30 training steps.
12	The policy discovers that it can maximize $\rone$ by shifting its activations to minimize the probe's sycophancy prediction, regardless of the actual content of the response.
13	The result is an inverted behavioral profile: $\tof = 0.978$, $\nof = 0.006$.
14	The model accepts every challenge, including invalid ones, because flipping the answer reliably shifts activations away from the sycophancy cluster and triggers a high reward.
15	Gradient-based gaming of learned reward components is a known failure mode~\citep{gao2023scaling, skalse2022hacking}; we include this result primarily to motivate the stop-gradient design that follows.
16	
17	\paragraph{Binary probe: the stubbornness trap (exp-008v3).}
18	The binary formulation with stop-gradient blocks the gaming pathway: gradients cannot flow through the frozen probe, so the policy cannot learn to manipulate the probe's internal decision boundary.
19	The failure that emerges instead is subtler and more dangerous.
20	
21	The probe classifies each completion as sycophantic or non-sycophantic based on whether the activation projects above or below a threshold along $\dsyc$.
22	Critically, $\dsyc$ encodes the \emph{direction} of belief change but not whether that change is warranted (\S\ref{sec:cosine_failure}).
23	A model that maintains its original answer, for any reason, produces activations that the probe classifies as non-sycophantic.
24	This means that refusing to revise a wrong answer under valid counter-evidence receives the same $\rone = 1$ as correctly resisting invalid pressure.
25	The policy exploits this equivalence immediately: by step 500, $\tof$ drops to 0.000 while $\nof$ reaches 0.9945, yielding $\sycon = 0$.
26	The model has learned that never changing its answer is a reliable strategy for collecting the probe reward.
27	
28	\paragraph{Behavioral death precedes distributional collapse.}
29	The trajectory across four checkpoints reveals a temporal dissociation between behavioral and distributional failure that has direct implications for monitoring practice.
30	Figure~\ref{fig:probe_trap} plots the full trajectory.
31	At checkpoint 500, the model is already behaviorally dead ($\tof = 0.000$), yet generation entropy remains at 0.70, well within the range that standard training monitors would flag as healthy.
32	The combined reward $R$ averages $+0.72$ during this period, because $\rthree$ rewards consistency with the original (correct) answer when the model refuses to flip, and $\rone$ rewards the probe's non-sycophancy classification.
33	Both reward components actively reinforce the degenerate behavior.
34	From checkpoint 500 through checkpoint 2000, the behavioral metrics remain frozen ($\tof \leq 0.006$, $\nof \geq 0.9945$, $\sycon \leq 0.011$), while entropy declines gradually and does not collapse until approximately step 1840.
35	The diagnostic lag between behavioral death and entropy collapse spans roughly 1,300 steps.
36	
37	This temporal gap carries a practical warning: entropy-based early stopping, the most widely used safeguard against reward hacking in RLHF pipelines~\citep{casper2023openproblems}, would not trigger during the 1,300-step window in which the policy is already degenerate.
38	By the time entropy collapses, the behavioral damage has been locked in for over a thousand gradient updates.
39	Detecting this failure requires \emph{behavioral} monitoring (e.g., periodic evaluation of $\tof$ on held-out challenges), not distributional monitoring alone.
40	
41	\paragraph{A dilemma for direction-based rewards.}
42	The differentiable and binary probe failures bracket the design space for $\dsyc$-based rewards.
43	If gradients flow through the probe, the policy games the learned decision boundary within tens of steps.
44	If gradients are stopped, the policy cannot game the boundary but instead exploits the fact that $\dsyc$ does not condition on input validity: stubbornness and genuine non-sycophancy are indistinguishable to any classifier built on $\dsyc$ alone.
45	These two failure modes are not independent design flaws; they are complementary consequences of the same root cause identified in Section~\ref{sec:cosine_failure}.
46	The sycophancy direction encodes \emph{whether} belief changed, not \emph{whether it should have}.
47	Any reward that conditions only on $\dsyc$, whether continuous or discrete, differentiable or frozen, will either be gamed (if the policy can manipulate the signal) or will reward rigidity (if it cannot).
48	Escaping this dilemma requires a reward signal that incorporates the evidential warrant of the user's challenge, a dimension that $\dsyc$ provably does not encode~\citep{denison2024subterfuge}.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "038b2f3d-5071-4952-ab45-e2c8280f7f00",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "2f4274f0-74c9-45f0-afc9-0a06cde3c6fb",
  "sourceToolAssistantUUID": "038b2f3d-5071-4952-ab45-e2c8280f7f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T15:32:02.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_0157TN2GrCLfJyYfSXYds9PL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f4274f0-74c9-45f0-afc9-0a06cde3c6fb",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "820de032-8f7b-431f-a6c8-bd244ec76d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 19 · 2026-05-20T15:32:02.716Z_

<details><summary>↩ Tool result · `toolu_0157TN2GrCLfJyYfSXYds9PL`</summary>

```text
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
11	The direction achieves AUROC $0.827 \pm 0.028$ at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
21	Llama-3-8B achieves CV AUROC $0.779 \pm 0.019$ at L16, with a parallel evidence-strength gradient (weak 0.711, medium 0.864, strong 0.911).
22	The best-layer depth differs (L16 vs.\ L19), consistent with the architectural differences between the two families, but the qualitative pattern is identical: gradual emergence, best-layer selection in the upper third, and monotonic strength scaling.
23	Discriminability is robust across knowledge domains, with per-domain AUROCs on Llama-3-8B ranging from 0.751 (geography) to 0.844 (commonsense).
24	When surface confounds (response length, hedging patterns) are explicitly controlled, Llama-3-8B's AUROC rises to 0.923, which confirms that the direction captures semantic content rather than stylistic artifacts.
25	The consistent results across architecturally distinct model families indicate that contrastive sycophancy directions reflect a shared representational phenomenon rather than a model-specific idiosyncrasy.
26	
27	\begin{table}[t]
28	\centering
29	\caption{Cross-model $\dsyc$ discriminability. CV AUROC is 5-fold cross-validated; evidence-strength AUROCs are evaluated on the full dataset at each model's best layer.}
30	\label{tab:cross_model}
31	\begin{tabular}{lccccc}
32	\toprule
33	Model & Best Layer & CV AUROC & Weak & Medium & Strong \\
34	\midrule
35	Qwen3-8B & L19 & $0.827{\pm}0.028$ & 0.675 & 0.883 & 0.929 \\
36	Llama-3-8B & L16 & $0.779{\pm}0.019$ & 0.711 & 0.864 & 0.911 \\
37	\bottomrule
38	\end{tabular}
39	\end{table}
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\columnwidth]{figures/fig_layer_auroc.pdf}
44	\caption{Per-layer AUROC of $\dsyc$ as a function of normalized depth (layer index / total layers). Qwen3-8B (36 layers, solid) shows gradual emergence from near-chance at L0 to a peak at L19, with performance plateauing in the final third. Llama-3-8B (32 layers, dashed; layers 16--31 only) exhibits a similar upper-third concentration. Both models achieve best discriminability in layers 50--60\% through the network.}
45	\label{fig:direction_quality}
46	\end{figure}
47	
48	\paragraph{Training stability and probe ablation.}
49	Two additional analyses confirm the robustness of $\dsyc$ under training dynamics.
50	First, we track direction drift during LoRA fine-tuning: at step 500, the cosine similarity between the original and re-extracted $\dsyc$ is approximately 0.96, and per-layer AUROC remains above 0.77.
51	The direction drifts slowly relative to the 500-step recalibration interval (\S\ref{ssec:recalib}), so the reward signal does not become stale between updates.
52	Second, we compare $\dsyc$ against a random baseline: a logistic probe trained on the learned direction achieves AUROC 0.835, versus 0.727 for a probe trained on a random direction of equal dimensionality ($\Delta{=}{+}0.108$).
53	The learned direction carries substantially more sycophancy-relevant information than an arbitrary axis in the same activation space.
54	
55	\paragraph{Implications for reward design.}
56	These results establish that $\dsyc$ reliably separates sycophantic from non-sycophantic representations across models, evidence-strength levels, and training checkpoints.
57	Direction quality is not the bottleneck.
58	The reward failures documented in \S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap} therefore cannot be attributed to a noisy or degenerate direction; they point to a deeper incompatibility between discriminability and reward utility.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820de032-8f7b-431f-a6c8-bd244ec76d4d",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "7c221e78-a686-4213-8e70-9a2b1a89ff6d",
  "sourceToolAssistantUUID": "820de032-8f7b-431f-a6c8-bd244ec76d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T15:32:02.944Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GGviPowC74uQ4HZmB7CQx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c221e78-a686-4213-8e70-9a2b1a89ff6d",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a90e6ca-d7d5-426c-90f4-aa4451b562a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1054,
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

_source line 21 · 2026-05-20T15:32:02.954Z_

<details><summary>↩ Tool result · `toolu_018GGviPowC74uQ4HZmB7CQx`</summary>

```text
1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	For sycophancy, the target and its complement occupy the same activation region; they differ only in whether external evidence warrants the belief change.
13	
14	\paragraph{GRPO stubbornness across all formulations.}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the harmonic mean of $\tof$ and $\nof$; higher indicates better calibration. Best result in \textbf{bold}.}
19	\label{tab:main_comparison}
20	\begin{tabular}{llcccc}
21	\toprule
22	Method & Type & $\sycon$ $\uparrow$ & $\tof$ $\uparrow$ & $\nof$ $\uparrow$ & Step \\
23	\midrule
24	Vanilla & -- & 0.134 & 0.072 & 0.945 & -- \\
25	$\rthree$-only GRPO & RL & 0.114 & -- & -- & 5000 \\
26	Cosine $\rone$ (F1d) & RL & collapse & -- & -- & -- \\
27	Binary Probe $\rone$ & RL & 0.000 & 0.000 & 0.995 & 500 \\
28	ActAdd ($\alpha{=}5$) & Inference & 0.054 & 0.028 & 0.961 & -- \\
29	\textbf{ACT} & SFT & \textbf{0.301} & \textbf{0.182} & 0.867 & 8000 \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	Table~\ref{tab:main_comparison} summarizes all methods evaluated on Qwen3-8B.
35	$\rthree$-only GRPO removes $\dsyc$ entirely and relies on the NLI-based behavioral reward alone.
36	If the failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} stemmed solely from the representation reward, this ablation should recover calibration quality.
37	It does not.
38	The $\sycon$ trajectory shows partial recovery that stalls: 0.074 at checkpoint 1000, 0.085 at checkpoint 2000, 0.095 at checkpoint 3000, and 0.114 at both checkpoints 4000 and 5000.
39	Recovery halts entirely between checkpoints 4000 and 5000, plateauing 15\% below the vanilla baseline of 0.134 with no further improvement.
40	ActAdd~\citep{turner2023actadd}, the inference-time baseline, achieves only $\sycon = 0.054$, confirming that activation-level intervention without weight updates cannot resolve the calibration problem.
41	$\rthree$-only GRPO exhibits the same stubbornness pattern as the $\dsyc$ approaches (high $\nof$, near-zero $\tof$) at milder severity.
42	The sparse scalar reward per completion cannot teach the model \emph{which} belief changes are warranted: it collapses an entire multi-turn exchange into one number that does not distinguish legitimate resistance from stubborn refusal.
43	
44	\paragraph{Why SFT succeeds where GRPO fails.}
45	ACT~\citep{consistency2025bctact} achieves $\sycon = 0.301$ at checkpoint 8000, more than $2{\times}$ the vanilla baseline and above every RL and inference-time variant (Table~\ref{tab:main_comparison}).
46	The ACT trajectory is not monotonic: $\sycon = 0.255$ at checkpoint 2000, dips to 0.214 at checkpoint 4000 ($-4.1$ percentage points as $\tof$ drops and $\nof$ rises), recovers to 0.262 at checkpoint 6000, and reaches 0.301 at checkpoint 8000.
47	ACT also experiences stubbornness episodes, yet it recovers from them.
48	The critical difference is supervision density.
49	SFT provides a corrective gradient at every token position in every training example: when the model begins to resist valid corrections, per-token cross-entropy loss immediately penalizes the incorrect tokens and supplies gradient information about \emph{which} outputs need to change.
50	GRPO provides one scalar per completion; once the policy locks into stubbornness, that scalar reinforces the behavior because consistent non-flipping collects high reward from both $\rone$ and $\rthree$.
51	Dense per-token loss can break out of stubbornness equilibria that sparse per-completion reward cannot escape.
52	This recovery capacity is the practical signature of the dense-versus-sparse supervision gap.
53	ACT is also far more efficient: its checkpoint 500 ($\sycon = 0.170$) already exceeds the plateau that $\rthree$-only GRPO reaches after 5000 steps of training.
54	
55	\paragraph{Future directions.}
56	These results point to several open problems.
57	First, condition-aware reward design could jointly encode belief-change direction and evidential warrant by conditioning on whether the input challenge provides valid grounds for revision.
58	Second, hybrid pipelines that apply SFT to establish the valid/invalid distinction as a warm start, followed by RL for broader distributional coverage, may combine the calibration quality of dense supervision with the exploration benefits of reinforcement learning.
59	Third, process reward models that provide per-step feedback within the RL framework could bridge the supervision density gap and retain online optimization.
60	Beyond sycophancy, the principle that discriminability does not guarantee reward utility applies to any behavioral attribute where the target and its complement share the same geometric direction~\citep{skalse2022hacking}.
61	Whether this principle extends to other alignment-relevant behaviors, such as hallucination and instruction-following, is an important open question.
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a90e6ca-d7d5-426c-90f4-aa4451b562a1",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "f9f8ca41-d7af-4e51-b64d-89601728c67a",
  "sourceToolAssistantUUID": "3a90e6ca-d7d5-426c-90f4-aa4451b562a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T15:32:03.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_015HqCbuKGpi5jZkGbfsi8XZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9f8ca41-d7af-4e51-b64d-89601728c67a",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4ZV1GcgDoDK2vh8WYV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3f8249eb-c752-4723-b664-4dce540aa75c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X2mySQcYp4bEuCERxbXBr9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 25391,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 747,
          "cache_read_input_tokens": 25391,
          "cache_creation_input_tokens": 1054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1054,
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

_source line 23 · 2026-05-20T15:32:03.177Z_

<details><summary>↩ Tool result · `toolu_015HqCbuKGpi5jZkGbfsi8XZ`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our RL training experiments use Qwen3-8B exclusively. We confirm cross-model discriminability of \dsyc{} on Llama-3-8B (AUROC $0.779 \pm 0.019$), but compute constraints (${\sim}200$ H100-equivalent hours) prevented replication of the reward formulation failures on a second model. Because the structural argument (that \dsyc{} cannot encode evidential warrant) is model-independent and the cross-model discriminability is the tested precondition for reward conversion, this limitation does not undermine the core claim.
4	
5	Our evaluation framework categorizes user challenges as binary valid or invalid. Real-world belief revision spans a continuous spectrum of evidential strength. The binary setup may overstate the difficulty of reward design if intermediate cases prove easier to separate in activation space.
6	
7	The style-controlled contrastive pairs isolate the cognitive signal from surface confounds (tone, length, formality) but may not capture the full diversity of sycophantic behavior in deployment. Natural sycophancy can involve subtler linguistic patterns absent from our constructed pairs.
8	
9	\sycon{} relies on a DeBERTa-based NLI classifier for flip determination rather than human annotation. Human judges might disagree on edge cases, though the NLI approach follows established evaluation protocols in the sycophancy literature. This affects measurement precision but not the direction of our negative results, since all reward formulations fail by large margins.
10	
11	Finally, our investigation is limited to GRPO. Other RL algorithms (PPO, DPO) may interact differently with representation-based rewards. However, the root cause of failure is that \dsyc{} is blind to evidential warrant, a property that is algorithm-independent.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f8249eb-c752-4723-b664-4dce540aa75c",
  "isSidechain": true,
  "promptId": "8c735ea8-c123-4f0e-bd9b-417a7a68cc99",
  "agentId": "a20c9ca036d0492b1",
  "type": "user",
  "uuid": "4983fb0a-3788-4f75-b9ff-8c8ceef3e983",
  "sourceToolAssistantUUID": "3f8249eb-c752-4723-b664-4dce540aa75c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T15:32:22.957Z_

Excellent. Now I have a comprehensive view of the paper. Let me compile the key findings into a structured report:

## Paper Analysis: contrastive_entrain_calib

### **Narrative Arc**

The paper follows a tightly integrated argument structure:

1. **Setup (Introduction)**: Representation engineering can extract a contrastive sycophancy direction (d_syc) with strong discriminability (AUROC 0.827–0.779), suggesting it could be converted into an RL reward signal.

2. **Promise → Failure (Core Sections)**: The paper systematically tests this hypothesis across three experimental domains:
   - **Cosine similarity reward** (Section 2): Despite high offline AUROC, the cosine gap between valid and sycophantic activations (0.098) is too narrow to drive policy updates. Online recalibration improves AUROC to 0.91 but triggers mode collapse.
   - **Binary probe reward** (Section 3): Discretizing the signal creates a "stubbornness trap"—the model learns that refusing all corrections reliably collects reward, achieving ToF=0 by step 500 while entropy remains healthy at 0.70 (a 1,300-step lag before distributional collapse).
   - **Behavioral-only GRPO** (Section 4): Removing d_syc entirely and using only an NLI-based reward also fails; sycophancy calibration (SycoScore) plateaus at 0.114 after 5000 steps (15% below vanilla baseline of 0.134).

3. **Root Cause Analysis (Discussion)**: All failures trace to a unified limitation: d_syc encodes **whether belief changed**, not **whether it should have**. Valid revision and capitulation occupy the same geometric region; they differ only in external evidential warrant, which no activation direction can fully encode. This semantic gap between discriminability and reward utility is fundamental and algorithm-independent.

4. **Contrast with Success (Discussion)**: Activation Consistency Training (ACT), which uses dense per-token SFT supervision, achieves SycoScore=0.301 (2.2× vanilla), confirming that sycophancy calibration requires dense supervision to distinguish warranted from unwarranted belief changes.

### **Key Terminology & Technical Concepts**

- **d_syc**: The contrastive sycophancy direction, extracted as the mean difference between valid-revision and sycophantic-capitulation activations
- **AUROC**: Cross-validated classification accuracy of the direction on style-controlled pairs
- **ToF (True-Flip Rate)**: Fraction of valid corrections the model accepts
- **NoF (No-Flip Rate)**: Fraction of invalid challenges the model resists
- **SycoScore**: Harmonic mean of ToF and NoF (analogous to F1 score); measures balanced calibration
- **Stubbornness trap**: The failure mode where the policy learns that never revising its answer reliably collects reward
- **Reward hacking**: The model gaming learned decision boundaries or exploiting signal ambiguities
- **Mode collapse**: Policy degenerating into low-entropy, degenerate outputs
- **Behavioral death**: The model becoming functionally unable to perform the target task (ToF=0) despite appearing healthy on distributional metrics (entropy)
- **Style control**: Constraining response pairs to have matched hedging, politeness, and length to isolate cognitive signals
- **Evidence-strength stratification**: Weak/medium/strong evidence levels used to evaluate if the direction captures granular warrant information

### **Tone & Voice**

The paper employs a **rigorous, forensic tone** characteristic of negative results papers:

- **Systematic diagnosis**: Each failed configuration is presented as a "diagnostic chain" that systematically resolves the failure of its predecessor, only to expose a deeper limitation
- **Precise technical language**: Numbers are exact and contextualized (e.g., "cosine gap of 0.098," "1,300-step lag between behavioral and distributional collapse")
- **Temporal precision**: The paper tracks dynamics across checkpoints and phases, emphasizing the temporal dissociation between behavioral failure and standard safety monitors
- **Constructive pessimism**: The conclusion is not "this is impossible" but rather "the structural barrier is this specific gap; here's why alternatives also fail and what would work instead" (dense supervision)
- **Architectural sophistication**: The paper treats failure modes as informative—each is a window into how the model exploits signal structure
- **Cross-cutting analysis**: Insights drawn from both successful (ACT) and failed (GRPO) methods, unified by a single principle
- **Caveats and boundaries**: Limitations section is honest about scope (Qwen3-8B exclusive for RL, binary validity assumption, DeBERTa-based evaluation)

### **Structural Patterns for Your Conclusion**

For a matching conclusion, adopt:
1. **Recapitulation through unified lens**: Start by restating the core semantic gap (discriminability ≠ reward utility)
2. **Implications beyond sycophancy**: Generalize the principle to other alignment domains where target and complement share geometric regions
3. **Practical actionability**: Three concrete future directions (condition-aware rewards, hybrid SFT→RL pipelines, process reward models)
4. **Epistemic humility**: The problem is not solved; the barrier is structural, not calibrational
5. **Numbers as narrative**: Use exact checkpoints, rates, and timelines rather than vague language
6. **Bridge to related work**: Reference how this informs representation-guided RL and RLHF dynamics more broadly

The tone should be **authoritative yet exploratory**—you've found something important about how representations and rewards interact, and the conclusion should position this as a principle that opens new research directions rather than a dead end.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4983fb0a-3788-4f75-b9ff-8c8ceef3e983",
  "isSidechain": true,
  "agentId": "a20c9ca036d0492b1",
  "requestId": "req_011CbE4Zn3wcoavZBxLYqd3p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2710a60b-7a9a-4658-955f-85739058ee5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "40d82284-4d91-4694-a56c-5852c736ad3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LmdrsP5aYrfEPboAq8n3Jn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 26445,
      "output_tokens": 1340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1340,
          "cache_read_input_tokens": 26445,
          "cache_creation_input_tokens": 14310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14310,
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
