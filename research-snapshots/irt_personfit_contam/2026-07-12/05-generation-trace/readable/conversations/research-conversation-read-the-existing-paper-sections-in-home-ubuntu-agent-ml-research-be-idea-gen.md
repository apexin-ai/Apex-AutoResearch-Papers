# Research conversation: Read the existing paper sections in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/pap

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a12720cf21d3875b5.jsonl`
- **Structured JSON:** [`ffa11eee566e22a21ec8.json`](../../sessions/ff/ffa11eee566e22a21ec8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-20T23:57:16.539Z_

Read the existing paper sections in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/ to understand the paper's narrative, terminology, and style. Read the introduction section fully, and skim any other available sections (abstract, related work, method, results/experiments). Report back: (1) the exact three contributions as stated in the introduction, (2) key terminology and notation used, (3) the paper's narrative arc/framing, (4) any specific phrasing patterns or style choices I should match.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "07bc743c-7319-4126-91bf-a67ef5b09b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T23:57:18.543Z_

I'll help you understand the paper's narrative and style. Let me start by exploring the paper sections directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07bc743c-7319-4126-91bf-a67ef5b09b5e",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6JPqHNA6BRHf97bkK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f504e4f7-5638-4e9f-8779-54694984df93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kfot1eDEzy4gYLu7PMmuKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 24831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 554,
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

_source line 3 · 2026-05-20T23:57:18.649Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0199iLWyNuhGiBYVCLHk1LSq`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections -type f -name \"*.tex\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f504e4f7-5638-4e9f-8779-54694984df93",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6JPqHNA6BRHf97bkK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7a8400f-1741-4ebb-831b-42f2dd97fdfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kfot1eDEzy4gYLu7PMmuKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 24831,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 554
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 122,
          "cache_read_input_tokens": 24831,
          "cache_creation_input_tokens": 554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 554,
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

_source line 4 · 2026-05-20T23:57:18.809Z_

<details><summary>↩ Tool result · `toolu_0199iLWyNuhGiBYVCLHk1LSq`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7a8400f-1741-4ebb-831b-42f2dd97fdfa",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "e5618405-0a78-4d94-a668-28ec448fb9cf",
  "sourceToolAssistantUUID": "f7a8400f-1741-4ebb-831b-42f2dd97fdfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T23:57:23.588Z_

Now let me read the introduction section fully and skim the other key sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5618405-0a78-4d94-a668-28ec448fb9cf",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6U2GkCWF4Kau6M6BC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c52085b-9a34-467d-9365-b0cdb6f275c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hVqQhqSKCd3cTXrkLsLAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 25385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
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

_source line 6 · 2026-05-20T23:57:24.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PJp8Ux1rN9jqcFndFp7rQg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c52085b-9a34-467d-9365-b0cdb6f275c1",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6U2GkCWF4Kau6M6BC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "056c8615-8af8-40e6-936c-628513d08d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hVqQhqSKCd3cTXrkLsLAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 25385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
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

_source line 7 · 2026-05-20T23:57:24.118Z_

<details><summary>↩ Tool result · `toolu_01PJp8Ux1rN9jqcFndFp7rQg`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally: any model trained on broad web-crawled data may have encountered evaluation items during pretraining or fine-tuning \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus itself \citep{dodge2021, magar2022}.
9	Membership inference approaches such as Min-K\%++ require token-level probabilities \citep{minkprob2024, deng2024}.
10	Time Travel probing relies on crafted prompts that elicit memorized completions \citep{golchin2024, oren2024}.
11	Performance-based methods compare results across original and rephrased test variants \citep{constat2024}, and in-context learning approaches require output logits \citep{codec2026}.
12	These methods form a detection frontier ordered by information access: training data, model weights, logits, token probabilities, rephrased retests, and finally binary patterns.
13	No existing method operates at the bottom of this frontier.
14	We ask: \emph{what can be detected from binary response patterns alone?}
15	
16	The need for minimal-information detection grows more pressing as models evolve.
17	\citet{wang2025fragility} show that all ten log-probability-based detection methods they evaluate perform at chance level on reasoning models trained with reinforcement learning (RL).
18	RL fine-tuning reshapes internal token distributions while preserving the same correct/incorrect outcomes, and probability-based detectors cannot distinguish contaminated from clean models under these conditions.
19	Binary response patterns are structurally invariant to such distributional changes, as they record what a model answered rather than how its internal distributions shifted (empirical verification on post-RL models remains future work).
20	
21	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce anomalous response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
22	This connection points to a mature body of work in psychometrics.
23	Person-fit statistics, developed over four decades for cheating detection in educational testing \citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}, quantify exactly this type of response aberrance.
24	The standardized statistic $\ell_z^*$ \citep{snijders2001} measures how well an individual's response pattern conforms to Item Response Theory (IRT) model predictions, with extreme negative values indicating patterns consistent with preknowledge.
25	Despite this natural correspondence, to our knowledge no prior work has applied person-fit statistics to LLM benchmark contamination detection.
26	
27	We introduce IRT-FIT, a framework that applies IRT person-fit analysis at the minimal-information operating point, requiring only binary responses and pre-calibrated item parameters \citep{psnirt2026}.
28	We compute $\ell_z^*$ for each (model, benchmark) pair and define $\Delta\ell_z^*$ as a difference-in-differences estimator for within-model contamination detection.
29	In controlled experiments (QLoRA fine-tuning on MMLU), 15\% contamination produces $|\text{Cohen's } d| = 3.58$ ($n{=}3$ clean seeds).
30	Our closed-form power function relates benchmark size to detection sensitivity ($R^2 = 0.957$), and shows that 80\% power at 15\% contamination requires $n \geq 7{,}958$ items.
31	A 4PL versus 3PL ablation reveals a mean $+27.3$ percentage-point power gain on MMLU \citep{hendrycks2021mmlu}, confirming that the upper-asymptote parameter is essential for LLM evaluation contexts.
32	Across 12 models and 5 benchmarks, $\ell_z^*$ flags 57 of 60 model-benchmark cells for response-pattern anomalies (BH-FDR $\alpha{=}0.05$), versus only 4 flagged by an accuracy $z$-score baseline.
33	This $14\times$ gap shows that $\ell_z^*$ captures response-pattern structure lost in aggregate accuracy.
34	We further identify a $\theta$-shift boundary condition: re-estimating ability on contaminated data can degrade sensitivity (non-monotonic dose-response under free $\theta$), but fixing $\theta$ to pre-contamination values restores monotonicity (signal ratio 3.12).
35	
36	Our contributions are:
37	\begin{enumerate}[leftmargin=*,nosep]
38	\item We propose IRT-FIT, a person-fit framework for contamination detection at the minimal-information operating point (binary responses only), validated through controlled contamination ($|\text{Cohen's } d| = 3.58$ at 15\% contamination).
39	\item We derive a closed-form power function ($R^2 = 0.957$) linking benchmark size to detection sensitivity, identify the $\theta$-shift boundary condition, and show that 4PL parameterization yields $+27.3$pp power gain over 3PL.
40	\item We report three empirical findings from real LLM response data: universal 4PL model misfit (57/60 cells flagged), the inadequacy of accuracy-based anomaly detection (4/60 cells), and a simulation-to-reality gap that motivates the $\Delta\ell_z^*$ design.
41	\end{enumerate}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "056c8615-8af8-40e6-936c-628513d08d3b",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "e186672b-ea06-4f29-bc42-c9a56883f4af",
  "sourceToolAssistantUUID": "056c8615-8af8-40e6-936c-628513d08d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T23:57:24.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WSKTpkJwBGgxkLiwdFc3uy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e186672b-ea06-4f29-bc42-c9a56883f4af",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6U2GkCWF4Kau6M6BC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a700ee4a-0dbe-4df1-8c67-16a78180db54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hVqQhqSKCd3cTXrkLsLAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 25385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
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

_source line 9 · 2026-05-20T23:57:24.208Z_

<details><summary>↩ Tool result · `toolu_01WSKTpkJwBGgxkLiwdFc3uy`</summary>

```text
1	% abstract
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a700ee4a-0dbe-4df1-8c67-16a78180db54",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "fc6705da-6f75-48d6-8553-8ad0802d5c1f",
  "sourceToolAssistantUUID": "a700ee4a-0dbe-4df1-8c67-16a78180db54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T23:57:24.410Z_

<details open><summary>🔧 Tool call — Read · `toolu_015WNtCRNCoFJo9m6KWHUzKL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc6705da-6f75-48d6-8553-8ad0802d5c1f",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6U2GkCWF4Kau6M6BC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7c21fa7-8ebd-4822-8e01-578ad89eae79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hVqQhqSKCd3cTXrkLsLAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 25385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
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

_source line 11 · 2026-05-20T23:57:24.417Z_

<details><summary>↩ Tool result · `toolu_015WNtCRNCoFJo9m6KWHUzKL`</summary>

```text
1	\section{Background and Related Work}\label{sec:background}
2	
3	\subsection{IRT and Person-Fit Statistics}\label{sec:irt_background}
4	
5	Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\theta$ and item-level parameters \citep{lord1980, embretson2000}.
6	The four-parameter logistic (4PL) model, formalized in \S\ref{sec:framework} (Eq.~\ref{eq:4pl}), extends the classical three-parameter model \citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \citep{barton1981}.
7	This parameter matters for LLMs: \citet{psnirt2026} find that 46\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.
8	
9	Given calibrated item parameters, person-fit statistics measure whether an examinee's \emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.
10	The key intuition is that a test-taker with ability $\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.
11	\citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.
12	\citet{snijders2001} corrected the variance of $\ell_z$ for uncertainty in the estimated $\hat{\theta}$, yielding $\ell_z^*$ with the property that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.
13	Negative values indicate \emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \emph{over-consistent} patterns (responses too predictable given the model).
14	We defer the formal definition to \S\ref{sec:framework}.
15	
16	In psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.
17	\citet{karabatsos2003} compared 36 person-fit statistics and found $\ell_z$ among the most powerful for detecting cheating.
18	\citet{sinharay2017} showed that $\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.
19	\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.
20	Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.
21	
22	\subsection{Benchmark Contamination Detection}\label{sec:contamination_related}
23	
24	Contamination detection methods vary in what information they require from the model under test.
25	Table~\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.
26	At the high end, corpus-search methods match benchmark items against pretraining data \citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.
27	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \citep{minkprob2024, deng2024}.
28	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, oren2024}.
29	Performance-based methods such as ConStat \citep{constat2024} and CoDeC \citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.
30	\citet{sainz2023} propose overlapping-split analysis using time-stamped data.
31	
32	A critical limitation unites all log-probability methods: \citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\%++) no better than random across 10 methods and 4 benchmarks.
33	RL reshapes output distributions without altering which items a model answers correctly, so token-level statistics lose signal while binary correctness patterns are structurally preserved.
34	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
35	
36	IRT-\textsc{Fit} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.
37	Recent work applies IRT to LLM evaluation for ability estimation \citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \citep{atlas2025}, and benchmark diagnostics \citep{psnirt2026}, but none use \emph{person-fit} statistics for contamination detection.
38	Our work bridges this gap.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7c21fa7-8ebd-4822-8e01-578ad89eae79",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "62ec1bc7-192c-4db3-a971-a4f724471ddd",
  "sourceToolAssistantUUID": "c7c21fa7-8ebd-4822-8e01-578ad89eae79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T23:57:24.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01133JMed7WfCN9Y8ecpDA9i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ec1bc7-192c-4db3-a971-a4f724471ddd",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6U2GkCWF4Kau6M6BC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41f5c410-50cd-4a43-a7a6-9dc8d2e79170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016hVqQhqSKCd3cTXrkLsLAU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 25385,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 334,
          "cache_read_input_tokens": 25385,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1513,
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

_source line 13 · 2026-05-20T23:57:24.638Z_

<details><summary>↩ Tool result · `toolu_01133JMed7WfCN9Y8ecpDA9i`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{The \textsc{IRT-Fit} Framework}
5	\label{sec:framework}
6	
7	Our method takes as input a binary response matrix $\mathbf{X} \in \{0,1\}^{M \times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \citep{psnirt2026}.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).
14	
15	The framework proceeds in three steps.
16	\textbf{Step~1}: Estimate each model's ability $\hat{\theta}$ via maximum likelihood on each benchmark separately.
17	\textbf{Step~2}: Compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\hat{\theta}$.
18	The statistic extends the original $\ell_z$ \citep{drasgow1985} by correcting for estimation uncertainty in $\hat{\theta}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis.
19	\textbf{Step~3}: For within-model contamination detection, compute $\Delta\ell_z^* = \ell_z^*(\text{target}) - \ell_z^*(\text{reference})$ between a target benchmark and a reference benchmark from the same model.
20	The entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.
21	
22	\paragraph{Validity under assumption violations.}
23	IRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.
24	When these assumptions fail, $\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies inflate the variance of response patterns beyond what the IRT model predicts.
25	However, this bias is approximately constant across benchmarks for a given model, because the same latent capabilities and the same dependency structure drive responses.
26	The $\Delta\ell_z^*$ statistic functions as a difference-in-differences (DiD) estimator: the shared bias cancels in the subtraction, isolating the contamination-specific signal.
27	We calibrate significance thresholds via a nonparametric bootstrap over the null distribution of $\Delta\ell_z^*$ rather than relying on the asymptotic $\mathcal{N}(0,1)$ reference, which accommodates residual model misspecification.
28	Universal misfit (all models showing $|\ell_z^*| > 1.96$) is therefore a finding about benchmark properties, not an artifact; $\Delta\ell_z^*$ bypasses absolute thresholds entirely.
29	
30	\subsection{Detection Power Characterization}
31	\label{sec:power_theory}
32	
33	We derive the statistical power of $\ell_z^*$ as a function of benchmark size $n$ and contamination fraction $\pi$.
34	
35	\paragraph{Contamination model.}
36	A fraction $\pi$ of items are forced correct regardless of ability.
37	The expected response becomes:
38	\begin{equation}
39	  \mathbb{E}[x_i \mid \theta_0, \pi] = P_i(\theta_0) + \pi \cdot Q_i(\theta_0)
40	  \label{eq:contam_response}
41	\end{equation}
42	where $Q_i(\theta) = 1 - P_i(\theta)$.
43	The contaminated response inflates the MLE: $\mathbb{E}[\hat{\theta}] > \theta_0$ for $\pi > 0$, because the score equation $\sum_i (\mathbb{E}[x_i] - P_i(\theta))\,h_i(\theta) = 0$ shifts the solution upward.
44	
45	\paragraph{Proposition 1 ($\sqrt{n}$ scaling).}
46	The noncentrality parameter $\delta(\theta_0, \pi)$ of $\ell_z^*$ under contamination satisfies $\delta \propto \sqrt{n}$.
47	The numerator accumulates $n$ per-item residuals ($O(n)$) while the denominator grows as $\sqrt{\mathrm{Var}^*} = O(\sqrt{n})$ from the \citet{snijders2001} variance formula, so
48	\begin{equation}
49	  \delta(\theta_0, \pi) = \sqrt{n}\;\cdot\;\delta_1(\theta_0, \pi)
50	  \label{eq:sqrt_n}
51	\end{equation}
52	where $\delta_1$ is the per-item noncentrality that depends only on item parameters and $(\theta_0, \pi)$.
53	
54	\paragraph{Proposition 2 (marginal power).}
55	Integrating over $\theta_0 \sim \mathcal{N}(0,1)$ via Gauss--Hermite quadrature ($K{=}30$ nodes) yields the marginal power under two-sided testing at level $\alpha$:
56	\begin{equation}
57	  \mathrm{Power}(n, \pi) = \sum_{k=1}^{K} w_k \left[\Phi\!\left(\frac{-z_\alpha - \delta_k}{\sigma_k}\right) + 1 - \Phi\!\left(\frac{z_\alpha - \delta_k}{\sigma_k}\right)\right]
58	  \label{eq:power}
59	\end{equation}
60	where $\delta_k$ and $\sigma_k$ are the conditional mean shift and standard deviation of $\ell_z^*$ at the $k$-th quadrature node, $w_k$ are the quadrature weights, and $z_\alpha = 1.96$.
61	Two-sided testing is essential: at moderate contamination ($\pi < 80\%$), $\ell_z^*$ is negative (aberrant pattern), but at high contamination ($\pi > 85\%$), $\ell_z^*$ turns positive (over-consistent pattern) as the inflated $\hat{\theta}$ renders near-perfect accuracy expected.
62	The crossover occurs at $\pi^* \approx 81$--$85\%$ across benchmarks.
63	Practitioners can determine minimum benchmark sizes from Equation~\ref{eq:power}: for example, 80\% power at 15\% contamination requires $n \geq 7{,}958$ items.
64	
65	\subsection{$\theta$-Shift Analysis}
66	\label{sec:theta_shift}
67	
68	Contamination creates an identification problem: higher accuracy raises $\hat{\theta}_{\text{MLE}}$, which in turn ``explains away'' the aberrant responses and attenuates the $\ell_z^*$ signal.
69	We term this the \emph{$\theta$-shift mechanism}.
70	As $\pi$ increases, $\hat{\theta}$ absorbs a larger share of the contamination signal into a legitimate ability increase, so the free-$\theta$ dose-response curve becomes non-monotonic: $|\Delta\ell_z^*|$ can decrease at higher contamination levels.
71	
72	The solution is \emph{$\theta$-fixed analysis}: anchor ability at a pre-contamination baseline $\theta_{\text{fixed}}$ estimated from clean conditions or cross-validated from held-out benchmarks.
73	With $\theta$ fixed, the $\ell_z^*$ statistic captures the full residual between observed and expected performance, and the dose-response curve becomes monotonically increasing.
74	In our controlled experiments (\S\ref{sec:ctrl_contam}), fixed-$\theta$ estimation yields a monotonic signal ratio of 3.12 between 50\% and 15\% contamination, whereas free-$\theta$ estimation produces an inverted ratio of 0.44.
75	
76	For practical deployment, $\theta_{\text{fixed}}$ can be obtained through two strategies: (1) cross-benchmark estimation, where $\theta$ is estimated from benchmarks presumed clean and applied to the target benchmark; or (2) temporal anchoring, where $\theta$ from an earlier evaluation serves as the reference for subsequent evaluations of the same model.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41f5c410-50cd-4a43-a7a6-9dc8d2e79170",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "6b0886f5-374c-4b55-9544-b9f56bb92112",
  "sourceToolAssistantUUID": "41f5c410-50cd-4a43-a7a6-9dc8d2e79170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T23:57:26.986Z_

Now let me skim the experiments, results, and discussion sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0886f5-374c-4b55-9544-b9f56bb92112",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6u59u4Hh2SMXk9q2X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e9d0937-387e-4970-b0ef-7a62cfcc9ac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017upa1K8FmNzbDUFPK3YzTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5543,
      "cache_read_input_tokens": 26898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5543,
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

_source line 15 · 2026-05-20T23:57:27.861Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HYbh3TqdiCgFNFZG4R9QyV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e9d0937-387e-4970-b0ef-7a62cfcc9ac0",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6u59u4Hh2SMXk9q2X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0b83833-11f0-474e-a5eb-9a7da8bbaa1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017upa1K8FmNzbDUFPK3YzTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5543,
      "cache_read_input_tokens": 26898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5543,
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

_source line 16 · 2026-05-20T23:57:27.881Z_

<details><summary>↩ Tool result · `toolu_01HYbh3TqdiCgFNFZG4R9QyV`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\input{sections/sec_setup}
5	\input{sections/sec_simulation}
6	\input{sections/sec_ctrl_contam}
7	\input{sections/sec_empirical}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0b83833-11f0-474e-a5eb-9a7da8bbaa1f",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "ed713c95-0e42-4e61-8e75-57a1d891a990",
  "sourceToolAssistantUUID": "f0b83833-11f0-474e-a5eb-9a7da8bbaa1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T23:57:28.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nrfy5CUWPrEoALy5zu3jTc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed713c95-0e42-4e61-8e75-57a1d891a990",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6u59u4Hh2SMXk9q2X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c449dac5-bb85-47b3-ae34-242a4e4a9834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017upa1K8FmNzbDUFPK3YzTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5543,
      "cache_read_input_tokens": 26898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5543,
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

_source line 18 · 2026-05-20T23:57:28.041Z_

<details><summary>↩ Tool result · `toolu_01Nrfy5CUWPrEoALy5zu3jTc`</summary>

```text
1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}8.01$, $s_2{=}5.94$, $s_3{=}8.08$ (mean$\,{=}\,7.35\pm1.21$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.58$; at 50\%, $|d|{=}1.56$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal exceeds the clean-clean $\Delta\ell_z^*$ noise floor (0.70) by a factor of 6.2$\times$.
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity.}
14	Under free-$\theta$ estimation, dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.34$ at 15\% versus ${-}1.90$ at 50\%.
15	The 50\% condition produces a \emph{weaker} signal than 15\% because contamination inflates $\hat{\theta}_{\text{MLE}}$, which absorbs part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	
17	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
18	Anchoring at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates) restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}2.68$ (15\%) and $8.36$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
19	
20	\paragraph{Finding 4: Memorization fingerprint.}
21	Splitting by seen/unseen items reveals a characteristic fingerprint: at 15\% contamination, memorized items yield $\ell_z^*{\approx}0$ (consistent with the model's inflated $\hat{\theta}$), while unseen items produce $\ell_z^*{=}3.1$, evidence of genuine aberrance on the non-memorized portion.
22	
23	\paragraph{Finding 5: Memorization fraction.}
24	The fraction of contaminated items that the model memorizes is 0.38 (15\%) and 0.29 (50\%).
25	SFT generalizes beyond the memorized items, as fewer than half the injected items show rote recall.
26	
27	\begin{figure*}[t]
28	  \centering
29	  \includegraphics[width=\textwidth]{fig_3_ctrl_contam.pdf}
30	  \caption{Controlled contamination on MMLU. \textbf{(a)} $\ell_z^*$ under free-$\theta$ and fixed-$\theta$ estimation for five conditions (3 clean seeds, 2 contaminated). Free-$\theta$ is non-monotonic; fixed-$\theta$ restores monotonicity. \textbf{(b)} Accuracy split by seen/unseen items with memorization fractions. \textbf{(c)} $\theta$-shift mechanism: contamination inflates $\hat{\theta}_{\text{MLE}}$, absorbing aberrance signal. $\theta_{\text{fixed}}$ computed as mean of $n{=}3$ clean seed $\hat{\theta}$ estimates ($-0.0966$).}
31	  \label{fig:ctrl_contam}
32	\end{figure*}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c449dac5-bb85-47b3-ae34-242a4e4a9834",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "86853bd4-c3fd-4e7a-af5c-f79d93585b45",
  "sourceToolAssistantUUID": "c449dac5-bb85-47b3-ae34-242a4e4a9834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:57:28.313Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uj6JbBQftxrwvoTdL2k5bP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86853bd4-c3fd-4e7a-af5c-f79d93585b45",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj6u59u4Hh2SMXk9q2X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48fc895f-0027-4abd-82f8-50ea53d3e11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017upa1K8FmNzbDUFPK3YzTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5543,
      "cache_read_input_tokens": 26898,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5543
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 265,
          "cache_read_input_tokens": 26898,
          "cache_creation_input_tokens": 5543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5543,
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

_source line 20 · 2026-05-20T23:57:28.330Z_

<details><summary>↩ Tool result · `toolu_01Uj6JbBQftxrwvoTdL2k5bP`</summary>

```text
1	\subsection{Empirical Findings}
2	\label{sec:empirical}
3	
4	We apply $\ell_z^*$ to 12 models across five benchmarks (60 model-benchmark cells).
5	After Benjamini--Hochberg FDR correction ($\alpha=0.05$), 57 of 60 cells are flagged as significant.
6	The three unflagged cells (Yi-Lightning$\times$ARC-C, 360GPT2-Pro$\times$HumanEval, Yi-Lightning$\times$HumanEval) all involve small benchmarks ($n \leq 295$), consistent with the power analysis in \S\ref{sec:simulation}.
7	By contrast, an accuracy $z$-score baseline flags only 4 of 60 cells: $\ell_z^*$ captures 14$\times$ more anomalies by exploiting response-pattern structure that accuracy aggregation discards.
8	This near-universal misfit indicates that real LLM response patterns systematically deviate from 4PL IRT predictions, regardless of architecture or training paradigm.
9	
10	\paragraph{12-model case study.}
11	Figure~\ref{fig:heatmap} presents the $\ell_z^*$ heatmap across 12 models and five benchmarks.
12	93.3\% of flagged cells exhibit positive $\ell_z^*$ (over-consistency): models answer too many hard items correctly relative to their estimated ability.
13	Gemini-1.5-Flash on MMLU represents an extreme case: 100\% accuracy (14{,}042/14{,}042 items correct), $\hat{\theta}=0.78$, and $\ell_z^*{=}{+}34.75$, with 50 of 57 MMLU subjects flagged individually.
14	Ward hierarchical clustering on the $\ell_z^*$ profile matrix reveals heterogeneous contamination typologies; Gemini-1.5-Flash isolates as a distinct outlier, while other models form clusters that correspond to selective versus uniform misfit.
15	Ten of 12 models are flagged on all five benchmarks simultaneously.
16	
17	\paragraph{IRT parameter estimation gap.}
18	Refitting 3PL parameters via MML-EM on the v1 leaderboard ($N{=}178$ models) recovers difficulty moderately ($r_b = 0.663$) but fails on discrimination ($r_a = 0.127$).
19	Classical IRT calibration requires sample sizes that current leaderboards cannot provide; neural calibration methods such as PSN-IRT \citep{psnirt2026} remain essential.
20	Comparing 4PL and 3PL $\ell_z^*$ on real data yields $r=0.225$ and RMSE$\,{=}\,68.41$, a confirmation that the guessing-slip parameters ($c$, $d$) captured by 4PL substantially alter person-fit assessment.
21	This simulation-to-reality gap constitutes an informative negative result: it quantifies the boundary conditions under which classical IRT calibration degrades.
22	
23	\begin{figure}[t]
24	  \centering
25	  \includegraphics[width=\columnwidth]{fig_4_model_heatmap.pdf}
26	  \caption{$\ell_z^*$ heatmap for 12 models across five benchmarks. Positive values (red) indicate over-consistent response patterns. Gemini-1.5-Flash on MMLU ($\ell_z^*{=}{+}34.75$) is an extreme outlier. Ward clustering (left dendrogram) reveals distinct contamination typologies.}
27	  \label{fig:heatmap}
28	\end{figure}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48fc895f-0027-4abd-82f8-50ea53d3e11f",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "0a4860a0-f0da-461c-91d5-2f2c713eaa89",
  "sourceToolAssistantUUID": "48fc895f-0027-4abd-82f8-50ea53d3e11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T23:57:31.460Z_

Now let me check the setup and simulation sections to get a complete picture:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a4860a0-f0da-461c-91d5-2f2c713eaa89",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj7B2baGLApTzxL4kuc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "819eb8bd-c20e-4f63-9ff7-fe93c072115e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0185FU42R7qdBXwzpbdYV7PY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2521,
      "cache_read_input_tokens": 32441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2521,
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

_source line 22 · 2026-05-20T23:57:32.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_01My3kYUt9N9AopeGWfd4Eec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "819eb8bd-c20e-4f63-9ff7-fe93c072115e",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj7B2baGLApTzxL4kuc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c1f30ad-4110-49a7-9793-0619e403fb86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0185FU42R7qdBXwzpbdYV7PY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2521,
      "cache_read_input_tokens": 32441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2521,
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

_source line 23 · 2026-05-20T23:57:32.306Z_

<details><summary>↩ Tool result · `toolu_01My3kYUt9N9AopeGWfd4Eec`</summary>

```text
1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	
10	\paragraph{Controlled contamination.}
11	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
12	
13	\paragraph{Simulation.}
14	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c1f30ad-4110-49a7-9793-0619e403fb86",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "4995e544-4d73-4405-a7c9-73c331ad7dc7",
  "sourceToolAssistantUUID": "2c1f30ad-4110-49a7-9793-0619e403fb86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T23:57:32.605Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GXYWjjGqVnuKadh3uZt2jV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4995e544-4d73-4405-a7c9-73c331ad7dc7",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj7B2baGLApTzxL4kuc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ac30803-55bd-4816-b3b6-3ac610cfd80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0185FU42R7qdBXwzpbdYV7PY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2521,
      "cache_read_input_tokens": 32441,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2521
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 187,
          "cache_read_input_tokens": 32441,
          "cache_creation_input_tokens": 2521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2521,
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

_source line 25 · 2026-05-20T23:57:32.616Z_

<details><summary>↩ Tool result · `toolu_01GXYWjjGqVnuKadh3uZt2jV`</summary>

```text
1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $lz^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$lz^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $lz^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the closed-form power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.9572$.
20	Practitioners can determine detection feasibility from a benchmark's item count alone.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4pl_ablation}).
24	Against supervised baselines, $lz^*$ outperforms logistic regression and random forest at low contamination ($+$0.10 AUROC at 5\%, $+$0.05 at 10\%) without training data; ML classifiers surpass $lz^*$ only above 25\% contamination.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ac30803-55bd-4816-b3b6-3ac610cfd80f",
  "isSidechain": true,
  "promptId": "dbe94312-cd7e-4853-abeb-102073e1e1e6",
  "agentId": "a12720cf21d3875b5",
  "type": "user",
  "uuid": "5f299069-de0d-4333-890f-429c89f54a47",
  "sourceToolAssistantUUID": "6ac30803-55bd-4816-b3b6-3ac610cfd80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T23:57:58.205Z_

Perfect! I now have a comprehensive understanding of the paper. Let me compile my findings:

## Paper Analysis Report

### 1. THREE EXACT CONTRIBUTIONS (from Introduction, lines 36-41)

The paper explicitly states three contributions:

1. **IRT-FIT Framework**: "We propose IRT-FIT, a person-fit framework for contamination detection at the minimal-information operating point (binary responses only), validated through controlled contamination (|Cohen's d| = 3.58 at 15% contamination)."

2. **Theoretical Power Function & Boundary Conditions**: "We derive a closed-form power function (R² = 0.957) linking benchmark size to detection sensitivity, identify the θ-shift boundary condition, and show that 4PL parameterization yields +27.3pp power gain over 3PL."

3. **Three Empirical Findings**: "We report three empirical findings from real LLM response data: universal 4PL model misfit (57/60 cells flagged), the inadequacy of accuracy-based anomaly detection (4/60 cells), and a simulation-to-reality gap that motivates the Δℓz* design."

---

### 2. KEY TERMINOLOGY AND NOTATION

**Core Statistics:**
- **ℓz*** (person-fit statistic): standardized likelihood residual measuring response-pattern conformance to IRT predictions (~N(0,1) under null)
- **Δℓz*** (difference-in-differences estimator): ℓz*(target benchmark) - ℓz*(reference benchmark) for within-model detection
- **θ** (ability/latent trait): model's underlying capability; **θ̂_MLE** is the estimated value; **θ_fixed** is anchored baseline

**IRT Model Parameters (4PL):**
- **ai** (discrimination): how sharply item difficulty changes with ability
- **bi** (difficulty): point where P_i(θ) = 0.5
- **ci** (lower asymptote/guessing): baseline correct probability even at very low ability
- **di** (upper asymptote/slip): asymptotic error probability at very high ability
- **Pi(θ)** (item response function): probability a model with ability θ answers item i correctly

**Key Concepts:**
- **θ-shift mechanism**: contamination inflates θ̂_MLE, attenuating ℓz* signal (non-monotonic dose-response under free-θ)
- **Model misfit**: |ℓz*| > 1.96 (BH-FDR corrected) indicating aberrant response patterns
- **Contamination frontier**: ordering of detection methods by information access (from high to low: training data → model weights → logits → token probabilities → rephrased retests → binary patterns)

---

### 3. PAPER'S NARRATIVE ARC AND FRAMING

**Core Narrative:**
The paper frames contamination detection as a psychometric problem, not primarily an NLP/ML problem. The narrative arc is:

1. **Problem Setup** (Intro, lines 3-14): Benchmark contamination is widespread and all existing detection methods require privileged information beyond binary responses. This creates a gap at the minimal-information frontier.

2. **Motivation** (Intro, lines 16-25): Modern RL-based models break probability-based detectors, but binary response patterns are invariant to distributional shifts. Contaminated models behave like cheaters on tests—a 40-year-old psychometrics problem already solved.

3. **Solution Transfer** (Intro, lines 27-34): Apply IRT person-fit analysis (developed for educational testing) to LLM evaluation. The key insight is the analogy: contaminated LLM ≈ test-taker with item preknowledge.

4. **Evidence Three-Fold** (Results sections):
   - **Controlled validation**: QLoRA-fine-tuning with injected contamination produces massive effect sizes (d=3.58 at 15%)
   - **Theoretical power analysis**: Derive closed-form power function showing benchmark size requirements
   - **Real-world misfit**: Universal 4PL model violations across 12 models/5 benchmarks (57/60 cells)

5. **Critical Boundary Discovery** (Method & Results): The θ-shift mechanism reveals that free-θ estimation breaks the method (non-monotonic dose-response), but fixing θ to pre-contamination values restores signal (3.12× improvement in signal ratio).

**Framing Devices:**
- Psychometrics as the authoritative framework ("mature body of work in psychometrics")
- "Minimal-information frontier" as organizing principle
- Binary responses as structurally invariant (immune to RL-induced distributional shifts)
- Person-fit statistics as "exactly" the right tool ("quantify exactly this type of response aberrance")

---

### 4. SPECIFIC PHRASING PATTERNS AND STYLE CHOICES

**Characteristic Patterns:**

1. **Formal statistical language with psychometric grounding:**
   - "Person-fit statistics measure whether an examinee's *pattern* of correct and incorrect responses is consistent with the IRT model"
   - "Extreme negative values indicating patterns consistent with preknowledge"
   - Uses citations to foundational 40-year-old work (Drasgow 1985, Snijders 2001) to establish legitimacy

2. **Effect size reporting with precision:**
   - Always reports Cohen's d, R², and specific counts (e.g., "57 of 60 cells", "14× gap")
   - Includes ± confidence intervals or variability measures (e.g., "7.35±1.21", "mean 0.679")
   - Uses exact model names and versions (Qwen2.5-7B-Instruct, QLoRA rank=16)

3. **Methodological clarity through structured subsections:**
   - "Step 1... Step 2... Step 3..." (linear progression in Method)
   - "Finding 1... Finding 2... Finding 3..." (organized numbered discoveries)
   - Clear paragraph headers with bold descriptors

4. **Theory-practice bridging:**
   - Derives theoretical power functions then validates via simulation/empirical data
   - Explicitly acknowledges assumption violations (local independence) and explains how design (Δℓz*) mitigates them
   - Frames negative/unexpected results as "informative" (e.g., "simulation-to-reality gap")

5. **Quantitative emphasis in prose:**
   - Embeds numbers and equations inline (e.g., "15% contamination produces |Cohen's d| = 3.58")
   - Uses hyphenation for compound modifiers (e.g., "log-probability-based detectors", "item-level parameters")
   - Reports crossover thresholds precisely (e.g., "π* ≈ 81–85%")

6. **Analogical reasoning:**
   - "contaminated LLM is functionally analogous to a test-taker with item preknowledge"
   - "treating each model as an examinee"
   - These bridge LLM/NLP domain to psychometrics

7. **Negative value conventions:**
   - ℓz* < 0 = aberrant (unexpected errors or successes)
   - ℓz* > 0 = over-consistent (too predictable)
   - This distinction is critical and used consistently throughout

8. **Temporal/causal language:**
   - "As π increases, ĥ absorbs a larger share..."
   - "Contamination reshapes... while preserving..."
   - Describes mechanisms and their consequences causally

9. **High-level framing statements:**
   - Opening sentences often establish stakes ("poses a growing threat")
   - Uses "we ask" to pose research questions ("We ask: *what can be detected from binary response patterns alone?*")
   - Closes sections with "we defer the formal definition to §X" or "future work" for scope management

10. **Technical precision in limitations:**
    - Acknowledges IRT assumption violations explicitly in "Validity under assumption violations" subsection
    - Explains *why* violations don't break the method (bias cancellation in DiD design)
    - Uses bootstrap-based thresholds rather than asymptotic theory when assumptions fail

---

### Summary for Matching Style

When writing new sections, prioritize:
- **Psychometric language** over pure ML framing
- **Exact quantitative reporting** with effect sizes and error bars
- **Structured, numbered findings** with clear progression
- **Theory validated by simulation then empirics** (never empirics alone)
- **Explicit handling of design assumptions** with mechanistic explanations
- **Binary-response patterns** as the fundamental unit of analysis
- **Citations to classical psychometrics** (Drasgow, Snijders, Meijer) for authority

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f299069-de0d-4333-890f-429c89f54a47",
  "isSidechain": true,
  "agentId": "a12720cf21d3875b5",
  "requestId": "req_011CbEj7V5JKMMRwcNdNTfvf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "005005e2-db19-41ee-aa39-172c6abd0195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "e2f28d49-45c6-45fa-a8b7-c841d7c83d3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018MZaknKtjz4iwxD9or9aV3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 34962,
      "output_tokens": 2087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2087,
          "cache_read_input_tokens": 34962,
          "cache_creation_input_tokens": 1526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1526,
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
