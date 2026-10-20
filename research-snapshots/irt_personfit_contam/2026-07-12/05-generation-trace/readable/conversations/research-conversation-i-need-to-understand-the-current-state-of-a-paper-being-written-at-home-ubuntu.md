# Research conversation: I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/pr

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a457d51ccc9db3c1c.jsonl`
- **Structured JSON:** [`d78e0ce6ef69b1a366f0.json`](../../sessions/d7/d78e0ce6ef69b1a366f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-20T23:35:26.562Z_

I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. 

Please read these files if they exist:
1. The main paper .tex file (look for main.tex or similar)
2. sections/experiments.tex or sections/results.tex 
3. sections/introduction.tex
4. sections/method.tex or sections/methodology.tex
5. Any existing discussion.tex

Search breadth: medium. I need to understand the paper's narrative flow and notation conventions to write a Discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "f1d66930-d741-435b-b54a-f25652f22687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T23:35:27.904Z_

I'll help you understand the current state of the paper. Let me start by exploring the paper directory structure and then read the key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1d66930-d741-435b-b54a-f25652f22687",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRjgQFEyZ4AnYVg1UF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25ceabc5-f583-4224-953c-9ba95ff2c943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01We9uJWfs5b4VyEdGFb8Bb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25398,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-20T23:35:28.346Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R7b2Zq1QxMG67LcNhsk7bN`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper -type f -name \"*.tex\" | head -20",
  "description": "Find all .tex files in the paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25ceabc5-f583-4224-953c-9ba95ff2c943",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRjgQFEyZ4AnYVg1UF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8302536f-9fa7-4a12-9dde-fb098161bd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01We9uJWfs5b4VyEdGFb8Bb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25398,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-20T23:35:28.493Z_

<details><summary>↩ Tool result · `toolu_01R7b2Zq1QxMG67LcNhsk7bN`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8302536f-9fa7-4a12-9dde-fb098161bd9e",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "bb2d9926-9c34-4fd0-bc2a-51c72faacab0",
  "sourceToolAssistantUUID": "8302536f-9fa7-4a12-9dde-fb098161bd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T23:35:28.652Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N3uKtgdcZWLPJXwdSy3H3U`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/",
  "description": "List contents of paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb2d9926-9c34-4fd0-bc2a-51c72faacab0",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRjgQFEyZ4AnYVg1UF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21322329-0928-46f5-af2c-f77e1bc0d93d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01We9uJWfs5b4VyEdGFb8Bb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25398,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 6 · 2026-05-20T23:35:28.707Z_

<details><summary>↩ Tool result · `toolu_01N3uKtgdcZWLPJXwdSy3H3U`</summary>

```text
total 92
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 22:49 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 20 23:34 ..
-rw-r--r--  1 ubuntu ubuntu 11615 May 20 22:24 acl.sty
-rw-r--r--  1 ubuntu ubuntu 45186 May 20 22:24 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu   884 May 20 22:24 main.tex
-rw-r--r--  1 ubuntu ubuntu 15106 May 20 22:49 references.bib
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 23:33 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21322329-0928-46f5-af2c-f77e1bc0d93d",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "001c12dc-1387-4f65-9504-7c382a704450",
  "sourceToolAssistantUUID": "21322329-0928-46f5-af2c-f77e1bc0d93d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T23:35:29.883Z_

Great! Now let me read the key files to understand the paper's structure and narrative:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "001c12dc-1387-4f65-9504-7c382a704450",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2b9402c-f045-4891-bf27-7745156cfa0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 8 · 2026-05-20T23:35:30.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JPwU5Bnr5mJiEXbAVYo72w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b9402c-f045-4891-bf27-7745156cfa0f",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25ea3d21-a80d-416e-af44-893d25651064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 9 · 2026-05-20T23:35:30.752Z_

<details><summary>↩ Tool result · `toolu_01JPwU5Bnr5mJiEXbAVYo72w`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	
17	\graphicspath{{../figures/paper/}}
18	
19	\title{Detecting Benchmark Contamination in Large Language Models \\
20	via Item Response Theory Person-Fit Statistics}
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
32	\input{sections/background}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/discussion}
36	
37	\section*{Limitations}
38	\input{sections/limitations}
39	
40	\bibliography{references}
41	
42	\appendix
43	\input{sections/appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25ea3d21-a80d-416e-af44-893d25651064",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "b8a58de0-cc94-45bd-93fa-988c64071869",
  "sourceToolAssistantUUID": "25ea3d21-a80d-416e-af44-893d25651064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T23:35:30.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QVEWaPyPgzDeABNm2Tuq5H`</summary>

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
  "parentUuid": "b8a58de0-cc94-45bd-93fa-988c64071869",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1de4b3d9-c4c9-40ba-8a77-f167122f87e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 11 · 2026-05-20T23:35:30.984Z_

<details><summary>↩ Tool result · `toolu_01QVEWaPyPgzDeABNm2Tuq5H`</summary>

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
  "parentUuid": "1de4b3d9-c4c9-40ba-8a77-f167122f87e6",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "7065cd4c-9a11-468f-983b-32ac84bb532f",
  "sourceToolAssistantUUID": "1de4b3d9-c4c9-40ba-8a77-f167122f87e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T23:35:31.183Z_

<details open><summary>🔧 Tool call — Read · `toolu_013s1D4vHvyksKUHimL2EK9o`</summary>

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
  "parentUuid": "7065cd4c-9a11-468f-983b-32ac84bb532f",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d8fc7c5-7828-4bd9-a2a6-e7dcf4a15100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 13 · 2026-05-20T23:35:31.190Z_

<details><summary>↩ Tool result · `toolu_013s1D4vHvyksKUHimL2EK9o`</summary>

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
  "parentUuid": "6d8fc7c5-7828-4bd9-a2a6-e7dcf4a15100",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "3a0793fa-99de-4dd0-bc52-08ed54eb2c61",
  "sourceToolAssistantUUID": "6d8fc7c5-7828-4bd9-a2a6-e7dcf4a15100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T23:35:31.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FvynubPf8pbfYqQfDiLyM3`</summary>

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
  "parentUuid": "3a0793fa-99de-4dd0-bc52-08ed54eb2c61",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ab4c0ca-aff6-4302-96fd-55c21d3ce4cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 15 · 2026-05-20T23:35:31.615Z_

<details><summary>↩ Tool result · `toolu_01FvynubPf8pbfYqQfDiLyM3`</summary>

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
  "parentUuid": "1ab4c0ca-aff6-4302-96fd-55c21d3ce4cc",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "fd658f81-14f8-4838-a45b-70ea42c7878f",
  "sourceToolAssistantUUID": "1ab4c0ca-aff6-4302-96fd-55c21d3ce4cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T23:35:31.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GN24vUR3AzhCk4MyKrcbCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd658f81-14f8-4838-a45b-70ea42c7878f",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhRtt3YcXVB8ByWyPne",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2739943a-3e9d-45e4-81f8-1e882289e7ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 17 · 2026-05-20T23:35:31.718Z_

<details><summary>↩ Tool result · `toolu_01GN24vUR3AzhCk4MyKrcbCx`</summary>

```text
1	% discussion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2739943a-3e9d-45e4-81f8-1e882289e7ac",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "da944f7c-2f37-4f40-85c4-565cc5539cd5",
  "sourceToolAssistantUUID": "2739943a-3e9d-45e4-81f8-1e882289e7ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T23:35:33.314Z_

The discussion section is empty. Let me also read the background and the individual experiment subsections to get the full narrative:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da944f7c-2f37-4f40-85c4-565cc5539cd5",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhS7pQxyUj1NnQMRkB1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab257865-8982-45b4-acf7-869372e0cc91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
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

_source line 19 · 2026-05-20T23:35:34.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HMHsHWm6t4fpYxkAridanD`</summary>

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
  "parentUuid": "ab257865-8982-45b4-acf7-869372e0cc91",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhS7pQxyUj1NnQMRkB1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b6221e6-67d4-4c40-9023-5c28be20ac8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
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

_source line 20 · 2026-05-20T23:35:34.250Z_

<details><summary>↩ Tool result · `toolu_01HMHsHWm6t4fpYxkAridanD`</summary>

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
  "parentUuid": "3b6221e6-67d4-4c40-9023-5c28be20ac8d",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "2c1b1933-3b02-4637-aba3-6a36a7635c71",
  "sourceToolAssistantUUID": "3b6221e6-67d4-4c40-9023-5c28be20ac8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T23:35:34.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_017x1K4RZYrLNhYLfqSjuLgc`</summary>

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
  "parentUuid": "2c1b1933-3b02-4637-aba3-6a36a7635c71",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhS7pQxyUj1NnQMRkB1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3387b4b2-647a-4eef-a9ba-c65bb03bc95a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
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

_source line 22 · 2026-05-20T23:35:34.387Z_

<details><summary>↩ Tool result · `toolu_017x1K4RZYrLNhYLfqSjuLgc`</summary>

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
  "parentUuid": "3387b4b2-647a-4eef-a9ba-c65bb03bc95a",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "a42994cd-73aa-4f27-8848-752444897caf",
  "sourceToolAssistantUUID": "3387b4b2-647a-4eef-a9ba-c65bb03bc95a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T23:35:34.585Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XFKYD3o7j7KdLavqVs7PPo`</summary>

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
  "parentUuid": "a42994cd-73aa-4f27-8848-752444897caf",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhS7pQxyUj1NnQMRkB1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8aa96b73-a55b-48d1-9735-cd8e79519e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
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

_source line 24 · 2026-05-20T23:35:34.595Z_

<details><summary>↩ Tool result · `toolu_01XFKYD3o7j7KdLavqVs7PPo`</summary>

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
  "parentUuid": "8aa96b73-a55b-48d1-9735-cd8e79519e3c",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "23b1f739-ae9c-4046-94fd-d3b3980b644b",
  "sourceToolAssistantUUID": "8aa96b73-a55b-48d1-9735-cd8e79519e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T23:35:34.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ef7nks2ffZnWtpDXZQJN1E`</summary>

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
  "parentUuid": "23b1f739-ae9c-4046-94fd-d3b3980b644b",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhS7pQxyUj1NnQMRkB1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c79e8b7a-91eb-4507-97ce-4c8b57820782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 352,
          "cache_read_input_tokens": 27332,
          "cache_creation_input_tokens": 4825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4825,
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

_source line 26 · 2026-05-20T23:35:34.796Z_

<details><summary>↩ Tool result · `toolu_01Ef7nks2ffZnWtpDXZQJN1E`</summary>

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
  "parentUuid": "c79e8b7a-91eb-4507-97ce-4c8b57820782",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "6311c89e-ddcd-4618-99a9-bd7505770a4d",
  "sourceToolAssistantUUID": "c79e8b7a-91eb-4507-97ce-4c8b57820782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T23:35:35.995Z_

Let me also check the abstract, limitations, and conclusion sections to fully understand the scope:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6311c89e-ddcd-4618-99a9-bd7505770a4d",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSLzRaVQFKMxxRNoFs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99faa451-e575-48ca-bb81-416164042a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
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

_source line 28 · 2026-05-20T23:35:36.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Thk2YPb4fxAauogPmodUPD`</summary>

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
  "parentUuid": "99faa451-e575-48ca-bb81-416164042a36",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSLzRaVQFKMxxRNoFs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5acf30ac-bc95-49c8-81f4-2ed50ebddc77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
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

_source line 29 · 2026-05-20T23:35:36.884Z_

<details><summary>↩ Tool result · `toolu_01Thk2YPb4fxAauogPmodUPD`</summary>

```text
1	% abstract
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5acf30ac-bc95-49c8-81f4-2ed50ebddc77",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "3ff8a37c-60ab-41a1-bd53-b26f8b467136",
  "sourceToolAssistantUUID": "5acf30ac-bc95-49c8-81f4-2ed50ebddc77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T23:35:37.081Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HEMC6iBrE7KCUNS5VqwdbY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff8a37c-60ab-41a1-bd53-b26f8b467136",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSLzRaVQFKMxxRNoFs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "663c71bc-fc80-4482-a36e-ea0f61060154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
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

_source line 31 · 2026-05-20T23:35:37.085Z_

<details><summary>↩ Tool result · `toolu_01HEMC6iBrE7KCUNS5VqwdbY`</summary>

```text
1	% limitations
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "663c71bc-fc80-4482-a36e-ea0f61060154",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "9611c4b7-5418-40b1-afe4-e81b3b903dd4",
  "sourceToolAssistantUUID": "663c71bc-fc80-4482-a36e-ea0f61060154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T23:35:37.294Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EA3W6WSkxgLMVZq2yG1JEd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9611c4b7-5418-40b1-afe4-e81b3b903dd4",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSLzRaVQFKMxxRNoFs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45876a2c-66e0-4bf9-bf39-cc88b6f73d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
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

_source line 33 · 2026-05-20T23:35:37.300Z_

<details><summary>↩ Tool result · `toolu_01EA3W6WSkxgLMVZq2yG1JEd`</summary>

```text
1	% conclusion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45876a2c-66e0-4bf9-bf39-cc88b6f73d24",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "74447d5a-f772-4f24-ab27-f7c42c2a0cc0",
  "sourceToolAssistantUUID": "45876a2c-66e0-4bf9-bf39-cc88b6f73d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T23:35:37.586Z_

<details open><summary>🔧 Tool call — Read · `toolu_015f3j9kER1VC2KSqdAnjJiy`</summary>

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
  "parentUuid": "74447d5a-f772-4f24-ab27-f7c42c2a0cc0",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSLzRaVQFKMxxRNoFs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7550d5ef-53fc-4cb8-9e8e-615d1f013cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4335
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 338,
          "cache_read_input_tokens": 32157,
          "cache_creation_input_tokens": 4335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4335,
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

_source line 35 · 2026-05-20T23:35:37.591Z_

<details><summary>↩ Tool result · `toolu_015f3j9kER1VC2KSqdAnjJiy`</summary>

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
  "parentUuid": "7550d5ef-53fc-4cb8-9e8e-615d1f013cfe",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "5e6b7d86-3075-459d-bb02-99533e845da1",
  "sourceToolAssistantUUID": "7550d5ef-53fc-4cb8-9e8e-615d1f013cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T23:35:38.911Z_

Now let me search for the referenced paper_provenance.yaml to understand the claims structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e6b7d86-3075-459d-bb02-99533e845da1",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSYwGJdwznUb9zDZZs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f33b2fcc-d504-4516-9db6-a4273b1c32a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Biexiwndvuz1fzmsxWraej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 36492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 37 · 2026-05-20T23:35:39.534Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EE8gNWKFqehY2A2FGaSxUs`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"paper_provenance.yaml\" -o -name \"writing_plan.yaml\" 2>/dev/null",
  "description": "Find provenance and writing plan files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f33b2fcc-d504-4516-9db6-a4273b1c32a5",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSYwGJdwznUb9zDZZs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b621d381-3fce-4121-87dc-8dcb43e9191d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Biexiwndvuz1fzmsxWraej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 36492,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 154,
          "cache_read_input_tokens": 36492,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 38 · 2026-05-20T23:35:39.765Z_

<details><summary>↩ Tool result · `toolu_01EE8gNWKFqehY2A2FGaSxUs`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_provenance.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b621d381-3fce-4121-87dc-8dcb43e9191d",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "eb02b151-4f9f-42b4-96f5-089f720d1173",
  "sourceToolAssistantUUID": "b621d381-3fce-4121-87dc-8dcb43e9191d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T23:35:41.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BVgWsENnRwQKDb2kdz8PJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_provenance.yaml",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb02b151-4f9f-42b4-96f5-089f720d1173",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSi4hH1AQC5fJwCoV4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b74013b-8914-419b-83d7-ccc63547c518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018J1ZYgRq9inn7JpYcf6xaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 40 · 2026-05-20T23:35:41.162Z_

<details><summary>↩ Tool result · `toolu_01BVgWsENnRwQKDb2kdz8PJ5`</summary>

```text
1	paper:
2	  title: ''
3	  version: 11
4	  generated_at: '2026-05-20T23:34:38.275117+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: sec_setup
9	    paragraph: 0
10	    sentence: 0
11	  text: MMLU has 14,042 items, HellaSwag 10,042, GSM8K 1,319, ARC-Challenge 295, HumanEval
12	    164
13	  type: data
14	  evidence:
15	  - exp_id: phase_b_personfit
16	  - exp_id: exp-extended-sim
17	  decisions: []
18	  deprecated: false
19	- id: C003
20	  location:
21	    section: sec_setup
22	    paragraph: 0
23	    sentence: 0
24	  text: 4PL IRT parameters calibrated by PSN-IRT from large-scale leaderboard dataset
25	  type: method
26	  evidence:
27	  - exp_id: phase_b_personfit
28	    metric: item_params_source
29	  decisions: []
30	  deprecated: false
31	- id: C006
32	  location:
33	    section: sec_setup
34	    paragraph: 0
35	    sentence: 0
36	  text: 12 models from PSN-IRT v2 leaderboard dataset
37	  type: data
38	  evidence:
39	  - exp_id: phase_b_personfit
40	    metric: n_models=12
41	  decisions: []
42	  deprecated: false
43	- id: C010
44	  location:
45	    section: sec_setup
46	    paragraph: 0
47	    sentence: 0
48	  text: QLoRA rank=16 alpha=32 on Qwen2.5-7B-Instruct, 5 conditions (3 clean seeds
49	    + 2 contaminated)
50	  type: method
51	  evidence:
52	  - exp_id: exp-ctrl-contam-pilot
53	  decisions: []
54	  deprecated: false
55	- id: C015
56	  location:
57	    section: sec_setup
58	    paragraph: 0
59	    sentence: 0
60	  text: 2000 replicates per condition, 11 contamination levels
61	  type: method
62	  evidence:
63	  - exp_id: exp-extended-sim
64	    metric: n_sims=2000, levels=11
65	  decisions: []
66	  deprecated: false
67	- id: C016
68	  location:
69	    section: sec_simulation
70	    paragraph: 0
71	    sentence: 0
72	  text: 'Bootstrap lz* null: mean bias 0.041, std 1.003 on MMLU'
73	  type: quantitative
74	  evidence:
75	  - exp_id: exp-empirical-null
76	    metric: bias_by_benchmark.mmlu=0.041
77	  decisions: []
78	  deprecated: false
79	- id: C018
80	  location:
81	    section: sec_simulation
82	    paragraph: 0
83	    sentence: 0
84	  text: KS rejection rates by benchmark size
85	  type: quantitative
86	  evidence:
87	  - exp_id: exp-empirical-null
88	    metric: ks_reject_by_benchmark
89	  decisions: []
90	  deprecated: false
91	- id: C021
92	  location:
93	    section: sec_simulation
94	    paragraph: 0
95	    sentence: 0
96	  text: MMLU two-sided power 97.8% at 15%
97	  type: quantitative
98	  evidence:
99	  - exp_id: exp-extended-sim
100	    metric: mmlu_15pct=0.978
101	  decisions: []
102	  deprecated: false
103	- id: C025
104	  location:
105	    section: sec_simulation
106	    paragraph: 0
107	    sentence: 0
108	  text: Theory R2=0.9572
109	  type: quantitative
110	  evidence:
111	  - exp_id: exp-power-theory
112	    metric: R2_two_sided=0.9572
113	  decisions: []
114	  deprecated: false
115	- id: C030
116	  location:
117	    section: sec_simulation
118	    paragraph: 0
119	    sentence: 0
120	  text: 4PL vs 3PL mean +27.3pp MMLU
121	  type: quantitative
122	  evidence:
123	  - exp_id: exp-4pl-ablation
124	  decisions: []
125	  deprecated: false
126	- id: C036
127	  location:
128	    section: sec_simulation
129	    paragraph: 0
130	    sentence: 0
131	  text: lz* +0.10 AUROC at 5% vs ML
132	  type: quantitative
133	  evidence:
134	  - exp_id: exp-ml-classifier-baseline
135	  decisions: []
136	  deprecated: false
137	- id: C037
138	  location:
139	    section: sec_ctrl_contam
140	    paragraph: 0
141	    sentence: 0
142	  text: 'Clean seeds lz*: s1=8.01, s2=5.94, s3=8.08 (mean=7.35+/-1.21)'
143	  type: quantitative
144	  evidence:
145	  - exp_id: exp-ctrl-contam-pilot
146	    metric: clean_seeds, baseline_n3
147	  decisions: []
148	  deprecated: false
149	- id: C039
150	  location:
151	    section: sec_ctrl_contam
152	    paragraph: 0
153	    sentence: 0
154	  text: contam_15% |Cohen's d|=3.58, contam_50% |d|=1.56 (ddof=1, n=3)
155	  type: quantitative
156	  evidence:
157	  - exp_id: exp-ctrl-contam-pilot
158	    metric: cohens_d_n3
159	  decisions: []
160	  deprecated: false
161	- id: C042
162	  location:
163	    section: sec_ctrl_contam
164	    paragraph: 0
165	    sentence: 0
166	  text: Clean-clean noise floor 0.70, contam signal 5.7x above
167	  type: quantitative
168	  evidence:
169	  - exp_id: exp-clean-control-delta
170	    metric: clean_vs_clean_mean_abs
171	  decisions: []
172	  deprecated: false
173	- id: C046
174	  location:
175	    section: sec_ctrl_contam
176	    paragraph: 0
177	    sentence: 0
178	  text: 'Free-theta non-monotonic: Delta_lz=-4.34 (15%), -1.90 (50%)'
179	  type: quantitative
180	  evidence:
181	  - exp_id: exp-ctrl-contam-pilot
182	    metric: H3.theta_free
183	  decisions: []
184	  deprecated: false
185	- id: C051
186	  location:
187	    section: sec_ctrl_contam
188	    paragraph: 0
189	    sentence: 0
190	  text: 'Fixed-theta: 2.68 (15%), 8.36 (50%), ratio=3.12'
191	  type: quantitative
192	  evidence:
193	  - exp_id: exp-ctrl-contam-pilot
194	    metric: H3.theta_fixed
195	  decisions: []
196	  deprecated: false
197	- id: C057
198	  location:
199	    section: sec_ctrl_contam
200	    paragraph: 0
201	    sentence: 0
202	  text: 'Memorization fraction: 0.38 (15%), 0.29 (50%)'
203	  type: quantitative
204	  evidence:
205	  - exp_id: exp-ctrl-contam-pilot
206	    metric: H4_memorization_fraction
207	  decisions: []
208	  deprecated: false
209	- id: C058
210	  location:
211	    section: sec_empirical
212	    paragraph: 0
213	    sentence: 0
214	  text: 57/60 cells flagged after BH-FDR correction
215	  type: quantitative
216	  evidence:
217	  - exp_id: exp-fdr-correction
218	    metric: flagged_bh_fdr=57/60
219	  decisions: []
220	  deprecated: false
221	- id: C060
222	  location:
223	    section: sec_empirical
224	    paragraph: 0
225	    sentence: 0
226	  text: Accuracy z-score flags 4/60 vs lz* 57/60 (14x)
227	  type: quantitative
228	  evidence:
229	  - exp_id: exp-accuracy-zscore-baseline
230	    metric: z_flagged=4, lz_flagged=57
231	  decisions: []
232	  deprecated: false
233	- id: C063
234	  location:
235	    section: sec_empirical
236	    paragraph: 0
237	    sentence: 0
238	  text: 93.3% positive lz* cells
239	  type: quantitative
240	  evidence:
241	  - exp_id: exp-cross-benchmark-analysis
242	    metric: pct_positive_cells=93.3
243	  decisions: []
244	  deprecated: false
245	- id: C067
246	  location:
247	    section: sec_empirical
248	    paragraph: 0
249	    sentence: 0
250	  text: 'Gemini-1.5 MMLU: acc=100%, theta=0.78, lz*=+34.75'
251	  type: quantitative
252	  evidence:
253	  - exp_id: phase_b_personfit
254	    metric: gemini15_mmlu
255	  decisions: []
256	  deprecated: false
257	- id: C072
258	  location:
259	    section: sec_empirical
260	    paragraph: 0
261	    sentence: 0
262	  text: 50/57 MMLU subjects flagged for Gemini
263	  type: quantitative
264	  evidence:
265	  - exp_id: exp-domain-analysis
266	    metric: gemini_subjects_flagged=50/57
267	  decisions: []
268	  deprecated: false
269	- id: C078
270	  location:
271	    section: sec_empirical
272	    paragraph: 0
273	    sentence: 0
274	  text: 10/12 models flagged on all 5 benchmarks
275	  type: quantitative
276	  evidence:
277	  - exp_id: exp-cross-benchmark-analysis
278	    metric: n_models_all5_flagged=10
279	  decisions: []
280	  deprecated: false
281	- id: C085
282	  location:
283	    section: sec_empirical
284	    paragraph: 0
285	    sentence: 0
286	  text: 'MML-EM refit: b_r=0.663, a_r=0.127, N=178'
287	  type: quantitative
288	  evidence:
289	  - exp_id: exp-v1-irt-refit-expanded
290	  decisions: []
291	  deprecated: false
292	- id: C093
293	  location:
294	    section: sec_empirical
295	    paragraph: 0
296	    sentence: 0
297	  text: '4PL vs 3PL real data: r=0.225, RMSE=68.41'
298	  type: quantitative
299	  evidence:
300	  - exp_id: exp-4pl-real-data-degradation
301	    metric: correlation_4pl_vs_3pl
302	  decisions: []
303	  deprecated: false
304	- id: C094
305	  location:
306	    section: sec_ctrl_contam
307	    paragraph: 0
308	    sentence: 0
309	  text: Contamination signal exceeds noise floor by 6.2x
310	  type: quantitative
311	  evidence: []
312	  decisions: []
313	  deprecated: false
314	- id: C095
315	  location:
316	    section: sec_ctrl_contam
317	    paragraph: 0
318	    sentence: 0
319	  text: Δθ=0.29 at 15% contamination
320	  type: quantitative
321	  evidence: []
322	  decisions: []
323	  deprecated: false
324	- id: C096
325	  location:
326	    section: sec_method
327	    paragraph: 0
328	    sentence: 0
329	  text: '4PL IRT model: P_i(θ) = c_i + (d_i - c_i) sigmoid(a_i(θ - b_i))'
330	  type: definition
331	  evidence:
332	  - exp_id: exp_001
333	    metric: model_specification
334	  decisions: []
335	  deprecated: false
336	- id: C098
337	  location:
338	    section: sec_method
339	    paragraph: 0
340	    sentence: 0
341	  text: lz* ~ N(0,1) under null hypothesis (Snijders 2001 correction)
342	  type: theoretical
343	  evidence:
344	  - exp_id: exp_002
345	    metric: null_calibration
346	  decisions: []
347	  deprecated: false
348	- id: C101
349	  location:
350	    section: sec_method
351	    paragraph: 0
352	    sentence: 0
353	  text: Δlz* functions as difference-in-differences estimator cancelling shared IRT
354	    misfit bias
355	  type: methodological
356	  evidence:
357	  - exp_id: exp_002
358	    metric: bootstrap_null
359	  decisions: []
360	  deprecated: false
361	- id: C105
362	  location:
363	    section: sec_method
364	    paragraph: 0
365	    sentence: 0
366	  text: Noncentrality parameter δ ∝ √n
367	  type: theoretical
368	  evidence:
369	  - exp_id: exp_002
370	    metric: power_scaling
371	  decisions: []
372	  deprecated: false
373	- id: C110
374	  location:
375	    section: sec_method
376	    paragraph: 0
377	    sentence: 0
378	  text: Marginal power via Gauss-Hermite quadrature K=30
379	  type: theoretical
380	  evidence:
381	  - exp_id: exp_002
382	    metric: power_function
383	  decisions: []
384	  deprecated: false
385	- id: C116
386	  location:
387	    section: sec_method
388	    paragraph: 0
389	    sentence: 0
390	  text: lz* sign crossover at π* ≈ 81-85% across benchmarks
391	  type: quantitative
392	  evidence:
393	  - exp_id: exp_002
394	    metric: crossover_fraction
395	  decisions: []
396	  deprecated: false
397	- id: C123
398	  location:
399	    section: sec_method
400	    paragraph: 0
401	    sentence: 0
402	  text: 80% power at 15% contamination requires n ≥ 7,958 items
403	  type: quantitative
404	  evidence:
405	  - exp_id: exp_002
406	    metric: min_benchmark_size
407	  decisions: []
408	  deprecated: false
409	- id: C131
410	  location:
411	    section: sec_method
412	    paragraph: 0
413	    sentence: 0
414	  text: 'θ-shift mechanism: free-θ non-monotonic, fixed-θ monotonic'
415	  type: methodological
416	  evidence:
417	  - exp_id: exp_003
418	    metric: theta_shift
419	  decisions: []
420	  deprecated: false
421	- id: C140
422	  location:
423	    section: sec_method
424	    paragraph: 0
425	    sentence: 0
426	  text: Fixed-θ signal ratio 3.12 (50%/15%), free-θ inverted ratio 0.44
427	  type: quantitative
428	  evidence:
429	  - exp_id: exp_003
430	    metric: dose_response_ratio
431	  decisions: []
432	  deprecated: false
433	- id: C141
434	  location:
435	    section: sec_background
436	    paragraph: 0
437	    sentence: 0
438	  text: 46% of MMLU items have d < 0.95, ceiling effects pervasive
439	  type: quantitative
440	  evidence:
441	  - exp_id: exp_001
442	    metric: d_parameter_distribution
443	  decisions: []
444	  deprecated: false
445	- id: C143
446	  location:
447	    section: sec_background
448	    paragraph: 0
449	    sentence: 0
450	  text: lz* ~ N(0,1) under null (Snijders 2001)
451	  type: theoretical
452	  evidence:
453	  - exp_id: exp_002
454	    metric: null_calibration
455	  decisions: []
456	  deprecated: false
457	- id: C146
458	  location:
459	    section: sec_background
460	    paragraph: 0
461	    sentence: 0
462	  text: 'Wang et al: all 10 log-prob MIA methods no better than random on RL models'
463	  type: literature
464	  evidence:
465	  - exp_id: lit_wang2025
466	    metric: rl_robustness
467	  decisions: []
468	  deprecated: false
469	- id: C150
470	  location:
471	    section: sec_background
472	    paragraph: 0
473	    sentence: 0
474	  text: Binary correctness patterns structurally preserved under RL post-training
475	  type: theoretical
476	  evidence:
477	  - exp_id: lit_wang2025
478	    metric: structural_argument
479	  decisions: []
480	  deprecated: false
481	- id: C155
482	  location:
483	    section: sec_background
484	    paragraph: 0
485	    sentence: 0
486	  text: No prior work uses person-fit statistics for LLM contamination detection
487	  type: novelty
488	  evidence:
489	  - exp_id: lit_review
490	    metric: gap_analysis
491	  decisions: []
492	  deprecated: false
493	- id: C156
494	  location:
495	    section: sec_introduction
496	    paragraph: 0
497	    sentence: 0
498	  text: 15% contamination produces |Cohen's d| = 3.58 (n=3 clean seeds)
499	  type: quantitative
500	  evidence:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b74013b-8914-419b-83d7-ccc63547c518",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "8b81d656-7601-42a5-ac21-93a395936713",
  "sourceToolAssistantUUID": "7b74013b-8914-419b-83d7-ccc63547c518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T23:35:41.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RpRxc9JJy54CPxfdNUZyk3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b81d656-7601-42a5-ac21-93a395936713",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSi4hH1AQC5fJwCoV4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48060ead-6106-4dac-86c2-d2cbe509a6df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018J1ZYgRq9inn7JpYcf6xaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 42 · 2026-05-20T23:35:41.708Z_

<details><summary>↩ Tool result · `toolu_01RpRxc9JJy54CPxfdNUZyk3`</summary>

```text
1	meta:
2	  title: "IRT-FIT: Detecting LLM Benchmark Contamination via Person-Fit Statistics at the Minimal-Information Operating Point"
3	  venue: EMNLP 2026 Main (ARR Jun 15 cycle)
4	  format: Long paper, 8-page main text + unlimited references
5	  template: acl2023  # ACL rolling review standard template; Worker 下载 https://github.com/acl-org/acl-style-files
6	  template_note: "EMNLP 2026 通过 ARR 统一审稿，使用 ACL 标准模板。若 2026 版模板已发布，Worker 应优先使用。"
7	  created_at: "2026-05-20T20:00:00Z"
8	  verify_refs: true
9	  director_approved_at: "2026-05-20T20:10:00Z"
10	  score_target: "3.0-3.25 (Findings / Borderline Conference)"
11	
12	# ============================================================
13	# DIRECTOR ACTION ITEMS (Dream 审稿 + Reviewer 复核定稿)
14	# ============================================================
15	action_items:
16	  critical:
17	    - id: AI-1
18	      desc: "4PL 参数来源：PSN-IRT (Lee et al., AAAI 2026)，不是 py-irt 或 ltm。lz* 由项目自实现 (numpy/scipy)"
19	      target_section: sec_method
20	      status: pending
21	
22	  method:
23	    - id: AI-6
24	      desc: "IRT 假设违反的显式讨论：≥1 段解释 lz* 在 local independence/unidimensionality 违反下的诊断价值。核心论点：Δlz* 作为 DiD 设计，系统性偏差在差分中被消除"
25	      target_section: sec_method
26	      status: pending
27	    - id: AI-7
28	      desc: "Δlz* 设计 + bootstrap null 校准：universal misfit 是 finding 不是 artifact，Δlz* bypasses absolute thresholds"
29	      target_section: sec_method
30	      status: pending
31	
32	  results:
33	    - id: AI-8
34	      desc: "Type-I error 专段：bootstrap null mean bias 0.041, std 1.003, KS reject rate 8.3%"
35	      target_section: sec_simulation
36	      status: pending
37	    - id: AI-9
38	      desc: "Clean-clean Δlz* baseline drift：n=3 seeds lz* 分布，0.70 noise floor，contam signal 5.7× above"
39	      target_section: sec_ctrl_contam
40	      status: pending
41	    - id: AI-10
42	      desc: "Binary-only baseline 对比：lz* 57/60 vs accuracy z-score 4/60 (14×)。模拟中 lz* ≥ ML classifiers at 5-10%"
43	      target_section: sec_empirical
44	      status: pending
45	
46	  discussion:
47	    - id: AI-11
48	      desc: "单模型 ctrl-contam 泛化性限制：仅 Qwen2.5-7B × MMLU。Future work: multi-family"
49	      target_section: sec_limitations
50	      status: pending
51	    - id: AI-12
52	      desc: "QLoRA low-rank bias：memorization ~38% 可能是 QLoRA lower bound，full FT 可能更强信号"
53	      target_section: sec_limitations
54	      status: pending
55	    - id: AI-13
56	      desc: "Post-RL 措辞约束：不写 'robust to post-RL'。写 'structurally invariant to RL distributional changes — empirical verification is future work'"
57	      target_section: [sec_introduction, sec_discussion]
58	      status: pending
59	
60	  urgent_corrections:
61	    - id: UC-1
62	      desc: "57/60 vs 4/60 是 universal misfit 证据 (Claim 3a)，不是 contamination detection 证据。用于论证 lz* 捕获 accuracy 聚合后丢失的 response-pattern 信息。Contamination detection 优势用: 模拟 AUROC +0.10@5%, ctrl-contam |d|=3.58, lz*≥ML classifiers at 5-10%"
63	      target_section: [sec_empirical, sec_simulation]
64	      status: pending
65	    - id: UC-2
66	      desc: "KS 校准率分层报告：MMLU 8.3%, HellaSwag 8.3% (well-calibrated); HumanEval 75%, ARC-C 58.3% (poorly calibrated); 总体 40% (24/60)。不能只引用 8.3%。按 benchmark size 分层 + 说明 large benchmarks well-calibrated"
67	      target_section: sec_simulation
68	      status: pending
69	    - id: UC-3
70	      desc: "QLoRA bias 框架为 'results may be conservative' 而非 limitation。rank=16 限制 memorization → 38% 是保守下界 → full FT 信号预期更强 → 强化结论。~50 词 Limitations"
71	      target_section: sec_limitations
72	      status: pending
73	
74	  missing_refs:
75	    - "Drasgow, Levine & Williams (1985) — person-fit foundations"
76	    - "Karabatsos (2003) — already in map, need verify"
77	    - "Meijer & Sijtsma (2001) — person-fit survey"
78	    - "Oren et al. (2024) — proving test set contamination"
79	    - "Polo et al. (2024) — tinyBenchmarks"
80	    - "Magar & Schwartz (2022) — data contamination"
81	    - "Deng et al. (2024) — contamination detection"
82	    - "Burnham et al. (2024) — IRT for AI"
83	    - "Jacobs et al. (2024) — psychometrics and AI"
84	
85	# ============================================================
86	# PAPER OUTLINE
87	# ============================================================
88	paper_outline:
89	  abstract:
90	    word_budget: 200
91	    dependencies: [sec_experiments, sec_method]
92	    key_elements:
93	      - problem statement (contamination + privileged access gap)
94	      - minimal-information operating point framing
95	      - "3 result highlights: (1) ctrl-contam |d|=3.58@15%, (2) power function R²=0.957, (3) universal misfit finding"
96	      - scope precision (SFT contamination, not pretraining exposure)
97	    constraints:
98	      - no "state-of-the-art" (no SOTA comparison done)
99	      - no "significantly" without statistical test
100	      - numbers must match sec_experiments exactly
101	
102	  sec_introduction:
103	    label: "Introduction"
104	    word_budget: 700
105	    dependencies: []
106	    subsections: []
107	    key_elements:
108	      - "P1: Problem — contamination threatens evaluation integrity, structural cause (training corpora ∩ public benchmarks)"
109	      - "P2: Existing methods critique — ALL require privileged access. Detection frontier ranking: binary < rephrased retest < token probs < logits < weights"
110	      - "P3: RL-robustness motivation — Wang et al. shows all 10 log-prob methods ≈ random on RL models. Binary patterns structurally immune to RL distributional shifts"
111	      - "P4: Cross-domain insight — contaminated LLM ≡ examinee with item preknowledge. Person-fit literature: decades of cheating detection. Gap: 0/N papers connect person-fit to LLM contamination"
112	      - "P5: Our approach — IRT-FIT at minimal-information operating point. Key results preview (numbers from experiments)"
113	      - "P6: 3 contributions (method+characterization+empirical findings), escalating scope"
114	    narrative_strategy:
115	      story_type: "跨界迁移型 (unused in 0/8 peer papers — our differentiator)"
116	      hook: "ConStat definitional pivot: 'All prior methods require privileged access. We ask: what can be detected from binary response patterns alone?'"
117	      techniques:
118	        - "Wang's negative-result-first: prove existing methods fail → create urgency"
119	        - "PSN-IRT's numbered findings for scannability"
120	
121	  sec_background:
122	    label: "Background and Related Work"
123	    word_budget: 650
124	    dependencies: []
125	    subsections:
126	      - id: sec_irt_background
127	        label: "IRT and Person-Fit Statistics"
128	        word_budget: 350
129	        key_elements:
130	          - "4PL model equation: P(X=1|θ) = c + (d-c)·sigmoid(a(θ-b))"
131	          - "d parameter importance for LLMs (ceiling effects, 46% MMLU items d<0.95)"
132	          - "lz* definition + N(0,1) null + interpretation (negative=aberrant, positive=over-consistent)"
133	          - "Snijders (2001) variance correction"
134	          - "Person-fit for cheating detection in psychometrics (Karabatsos 2003, Sinharay 2017)"
135	        constraints:
136	          - self-contained for ML reviewers unfamiliar with psychometrics
137	          - avoid jargon without definition
138	          - IRT 形式化定义（4PL 公式 + lz* 公式）保留正文，推导细节移至 Appendix
139	          - 正文只保留直觉解释 + 核心公式
140	
141	      - id: sec_contamination_related
142	        label: "Benchmark Contamination Detection"
143	        word_budget: 300
144	        key_elements:
145	          - "Detection frontier table reference (Table 1)"
146	          - "5 method families: time-based partition, MIA/Min-K%++, Time Travel, ConStat, CoDeC"
147	          - "Wang et al. RL-robustness failure"
148	          - "Position IRT-FIT at bottom of frontier (minimum information access)"
149	          - "IRT for LLM evaluation (PSN-IRT, ATLAS) — related but not person-fit"
150	
151	  sec_method:
152	    label: "Method"
153	    word_budget: 600
154	    dependencies: [sec_background]
155	    subsections:
156	      - id: sec_framework
157	        label: "IRT-FIT Framework"
158	        word_budget: 200
159	        key_elements:
160	          - "Input: binary response matrix X (models × items) + calibrated 4PL parameters"
161	          - "Step 1: θ estimation (MLE per benchmark)"
162	          - "Step 2: lz* computation per (model, benchmark) cell"
163	          - "Step 3: Δlz* for within-model contamination detection"
164	          - "Item parameter source: PSN-IRT calibrated 4PL (cite psnirt2026)"
165	          - "No training data needed — unsupervised, per-cell statistic"
166	
167	      - id: sec_power_characterization
168	        label: "Detection Power Characterization"
169	        word_budget: 220
170	        key_elements:
171	          - "Power as function of n_items and contamination level"
172	          - "Theoretical derivation from Snijders (2001) variance formula: δ ∝ √n"
173	          - "Two-sided detection: partial contamination → aberrant (lz*<<0), full → over-consistent (lz*>>0)"
174	          - "Crossover point at ~81-85% contamination"
175	          - "Upper bound vs adjusted power (memorization fraction from ctrl-contam)"
176	          - "Minimum items guideline for practitioners"
177	
178	      - id: sec_theta_shift
179	        label: "θ-Shift and θ-Fixed Analysis"
180	        word_budget: 180
181	        key_elements:
182	          - "θ-shift mechanism: contamination → higher accuracy → higher θ_MLE → absorbs aberrance signal"
183	          - "θ-fixed solution: use pre-contamination θ baseline"
184	          - "Dose-response: free-θ non-monotonic, fixed-θ restores monotonicity (ratio=2.93)"
185	          - "Practical implication: cross-validated θ or external θ anchor"
186	
187	  sec_experiments:
188	    label: "Experiments"
189	    word_budget: 1000
190	    dependencies: [sec_method]
191	    subsections:
192	      - id: sec_setup
193	        label: "Experimental Setup"
194	        word_budget: 150
195	        key_elements:
196	          - "Benchmarks: MMLU (14042), HellaSwag (10042), GSM8K (1319), ARC-C (295), HumanEval (164)"
197	          - "Item parameters: PSN-IRT 4PL calibrated (cite psnirt2026)"
198	          - "12-model PSN-IRT dataset for empirical analysis"
199	          - "Controlled contamination: Qwen2.5-7B-Instruct, QLoRA SFT (r=16, α=32)"
200	          - "Conditions: clean×2(+s3), contam_15%, contam_50%"
201	          - "Simulation: 2000 replicates per condition, 11 contamination levels"
202	
203	      - id: sec_simulation
204	        label: "Simulation Validation"
205	        word_budget: 230
206	        key_elements:
207	          - "4PL null check: lz* ~ N(0,1) confirmed (all benchmarks KS pass)"
208	          - "Power results: MMLU@15%=97.9% (two-sided=97.8%), refer to Figure 2"
209	          - "Power scales with √n_items (theory R²=0.957)"
210	          - "Two-sided detection eliminates inverted-U: >93% all levels for MMLU"
211	          - "4PL vs 3PL ablation: mean +14-27pp power gain (refer to appendix Figure A1)"
212	          - "ML classifier comparison: lz* outperforms LR/RF at 5-10% contamination (+0.05-0.10 AUROC) without training data"
213	          - "Report bootstrap CIs (our differentiator vs 6/8 peers)"
214	        exp_ids: [sim_001, exp-extended-sim, exp-power-theory, exp-4pl-ablation, exp-ml-classifier-baseline, exp-clean-control-delta]
215	
216	      - id: sec_ctrl_contam
217	        label: "Controlled Contamination"
218	        word_budget: 300
219	        key_elements:
220	          - "Design: QLoRA SFT injection on Qwen2.5-7B-Instruct × MMLU"
221	          - "5 conditions: clean_s1 (seed=42), clean_s2 (seed=123), clean_s3 (seed=456), contam_15%, contam_50%"
222	          - "Clean baseline: report individual seeds s1=8.01, s2=5.94, s3=8.08 (mean=7.35±1.21); note s2 ~26% lower (seed-specific training dynamics)"
223	          - "Key Finding 1: contam_15% |Cohen's d|=3.58, contam_50% |d|=1.56 (ddof=1, n=3)"
224	          - "Key Finding 2: free-θ dose-response non-monotonic (contam_50 Δlz*=-1.90 < contam_15 Δlz*=-4.34)"
225	          - "Key Finding 3: θ-fixed restores monotonicity (Δlz*_fixed: 15%=+2.68, 50%=+8.36, ratio=3.12)"
226	          - "Key Finding 4: seen/unseen split — contam_15 seen lz*≈0 vs unseen=3.1 (memorization fingerprint)"
227	          - "Key Finding 5: memorization_fraction=0.38 (15%), 0.29 (50%) — SFT generalization effect"
228	          - "θ-shift mechanism quantification: Δθ=0.30 (15%), 0.47 (50%)"
229	          - "Present as numbered findings (PSN-IRT style)"
230	          - "Appendix: seed sensitivity (~30 words) — s2 outlier discussion"
231	        exp_ids: [exp-ctrl-contam-pilot]
232	
233	      - id: sec_empirical
234	        label: "Empirical Findings from Real LLM Data"
235	        word_budget: 320
236	        key_elements:
237	          - "Finding (a): Universal 4PL misfit — 57/60 cells flagged after BH-FDR (not artifact: bootstrap null well-calibrated)"
238	          - "Finding (b): 12-model case study — Gemini-1.5 MMLU acc=100%, θ=0.78, lz*=+34.75; selective vs uniform misfit profiles; Ward clustering typology; domain analysis (50/57 MMLU subjects flagged)"
239	          - "Finding (c): IRT parameter estimation gap — MML-EM refit N=178, b_r=0.66 (partial), a_r=0.13 (failure). Classical IRT sample requirements vs neural IRT"
240	          - "4PL vs 3PL on real data: r=0.225, RMSE=68.41 (d parameter essential for high-ability models)"
241	          - "Accuracy z-score baseline: 4/60 flagged vs lz* 57/60 — lz* captures pattern information beyond accuracy"
242	          - "Negative results framed as contributions: simulation-reality gap is informative"
243	        exp_ids: [phase_b_personfit, exp-two-sided, exp-fdr-correction, exp-empirical-null, exp-cross-benchmark-analysis, exp-accuracy-zscore-baseline, exp-4pl-real-data-degradation, exp-v1-irt-refit-expanded, exp-domain-analysis]
244	
245	  sec_discussion:
246	    label: "Discussion"
247	    word_budget: 200
248	    dependencies: [sec_experiments]
249	    key_elements:
250	      - "Simulation-reality gap interpretation: well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions"
251	      - "Δlz* design as practical solution: within-model comparison leverages well-calibrated null"
252	      - "Scalability: 13K+ v1 per-item data publicly available, binary-only → retrospective audit feasible"
253	      - "Scope: SFT contamination / leaderboard gaming, not pretraining exposure"
254	      - "Future work: large-scale leaderboard audit (pending estimation advances), multi-model-family ctrl-contam, post-RL validation"
255	
256	  sec_conclusion:
257	    label: "Conclusion"
258	    word_budget: 150
259	    dependencies: [sec_discussion]
260	    key_elements:
261	      - "Summary: minimal-information operating point, 3 findings"
262	      - "Impact: any evaluation that records binary responses can retrospectively check for contamination"
263	      - "No overclaiming (no SOTA, no 'significantly' without test)"
264	
265	  sec_limitations:
266	    label: "Limitations"
267	    word_budget: 250
268	    dependencies: [sec_experiments]
269	    page_count: false  # doesn't count toward 8-page limit
270	    key_elements:
271	      - "Single model family for ctrl-contam (Qwen2.5-7B); multi-family planned"
272	      - "IRT parameters from PSN-IRT (not self-calibrated); dependency on external calibration"
273	      - "SFT-only contamination; post-RL (exp-post-rl) deferred"
274	      - "Power limited by benchmark size (ARC-C 295 items → d=0.45)"
275	      - "Universal misfit means absolute lz* thresholds not applicable → requires Δlz* design"
276	      - "MML-EM refit failure → large-scale audit requires neural IRT advances"
277	
278	# ============================================================
279	# VISUALIZATION PLAN
280	# ============================================================
281	visualization_plan:
282	  - fig_id: fig_1_response_pattern
283	    tool: matplotlib
284	    type: conceptual_illustration
285	    description: "Dual-panel motivation figure showing contaminated vs clean response patterns"
286	    placement: "Section 1 (Introduction) or top of Section 3 (Method)"
287	    aspect_ratio: "2:1 (wide, two-column)"
288	    data_source: "synthetic: 4PL model simulation using PSN-IRT MMLU parameters"
289	    narrative_intent: >
290	      Show the psychometric intuition: a contaminated LLM produces an "impossible" response pattern —
291	      answering hard items correctly (memorized from training) while missing easier items it should get right.
292	      This is exactly what person-fit statistics detect: aberrance relative to IRT model predictions.
293	      The figure should make an ML reviewer immediately understand why psychometric cheating detection applies.
294	    design_notes: >
295	      Two panels side by side. X-axis: items sorted by difficulty (b parameter, easy→hard).
296	      Y-axis: response (0/1). Left panel: "Clean Model" — responses follow expected ICC curve
297	      (probability decreasing with difficulty). Right panel: "Contaminated Model" — same ability level
298	      but some hard items answered correctly (highlighted in red), producing an aberrant pattern.
299	      Overlay the expected probability curve (ICC) as a smooth line. Mark the memorized items distinctly.
300	      Bottom annotation: lz* values for each pattern (clean ≈ 0, contaminated << 0).
301	      Color: blue=clean, red=contaminated/memorized. Style: academic, minimal, no clutter.
302	      Pattern: "dual-panel contrast" from distilled-writing skill.
303	
304	  - fig_id: fig_2_power_function
305	    tool: matplotlib
306	    type: line_plot
307	    description: "Detection power as function of contamination level across 5 benchmarks with theoretical overlay"
308	    placement: "Section 5.2 (Simulation Validation)"
309	    aspect_ratio: "4:3 (single column)"
310	    data_source: "registry: exp-extended-sim (two_sided_power), exp-power-theory (theoretical curve)"
311	    narrative_intent: >
312	      Demonstrate that detection power is predictable from benchmark properties. The theoretical curve
313	      (R²=0.957) means practitioners can determine detection feasibility for ANY benchmark by knowing
314	      only its size. Two-sided detection eliminates the inverted-U artifact. MMLU (14K items) achieves
315	      >93% power at all contamination levels; smaller benchmarks need higher contamination for reliable detection.
316	    design_notes: >
317	      X-axis: contamination level (0-100%). Y-axis: two-sided detection power (0-1).
318	      5 lines for 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval), differentiated by
319	      color + marker. Theoretical √n curve as dashed overlay for MMLU. Horizontal dashed line at 0.80
320	      power threshold. Legend with benchmark names + n_items count.
321	      Key data points to highlight: MMLU@15%=97.8%, ARC-C shows lowest power (n=295).
322	      Style: clean line plot, no excessive gridlines. 95% CI bands if available from simulation.
323	      Pattern: "scaling curve with threshold" from standard ML plots.
324	
325	  - fig_id: fig_3_ctrl_contam
326	    tool: matplotlib
327	    type: multi_panel
328	    description: "Controlled contamination results: θ-free vs θ-fixed Δlz* and seen/unseen split"
329	    placement: "Section 5.3 (Controlled Contamination)"
330	    aspect_ratio: "2:1 (wide, two-column)"
331	    data_source: "registry: exp-ctrl-contam-pilot (metrics.H2, metrics.H3, metrics.theta_fixed_analysis, metrics.accuracy)"
332	    narrative_intent: >
333	      Three key messages: (1) contamination at 15% produces strong detection signal (|d|=3.58);
334	      (2) θ-shift confound causes non-monotonic dose-response under free-θ, but θ-fixed restores
335	      monotonicity — this is a methodological contribution; (3) seen/unseen split reveals the clearest
336	      contamination fingerprint: memorized items produce "normal" lz* while unseen items show extreme
337	      aberrance.
338	    design_notes: >
339	      3 panels (a,b,c). (a) Bar chart: Δlz* for 4 conditions (clean_s1, clean_s2, contam_15, contam_50)
340	      under free-θ (dark bars) vs fixed-θ (light bars). Error bars from clean baseline variance.
341	      Highlight the non-monotonic→monotonic transition. (b) Grouped bars: seen vs unseen lz* for contam_15
342	      and contam_50. Seen lz*≈0 (memorized items look normal) vs unseen lz*=3.1 (genuine aberrance).
343	      (c) θ-shift visualization: θ values across conditions showing contamination→θ↑.
344	      Colors: blue=clean, orange=contam_15, red=contam_50. Consistent across panels.
345	      Annotate Cohen's d values. Pattern: "condition comparison with mechanism decomposition."
346	
347	  - fig_id: fig_4_model_heatmap
348	    tool: matplotlib
349	    type: heatmap
350	    description: "12-model × 5-benchmark lz* heatmap with Ward clustering dendrogram"
351	    placement: "Section 5.4 (Empirical Findings)"
352	    aspect_ratio: "3:4 (portrait, single column)"
353	    data_source: "registry: phase_b_personfit, exp-cross-benchmark-analysis, exp-fdr-correction"
354	    narrative_intent: >
355	      Show the landscape of LLM response pattern anomalies: (1) universal misfit — nearly all cells
356	      colored (57/60 flagged), establishing that LLM responses fundamentally differ from classical
357	      test-takers; (2) heterogeneous profiles — some models show uniform positive lz* (over-consistent,
358	      possible contamination), others show mixed or negative patterns; (3) Ward clustering reveals
359	      contamination typologies (Gemini-1.5 isolated as extreme outlier).
360	    design_notes: >
361	      Heatmap with diverging colormap (blue=negative lz*, white=0, red=positive lz*).
362	      Rows: 12 models, ordered by Ward clustering with dendrogram on left.
363	      Columns: 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval).
364	      Cell annotations: lz* values (rounded to integer for readability).
365	      Mark 3 unflagged cells with hatching or border.
366	      Gemini-1.5 MMLU cell should be maximally red (lz*=+34.75).
367	      Colorbar with symmetric range. Model names on right y-axis.
368	      Pattern: "annotated heatmap with hierarchical clustering."
369	
370	# ============================================================
371	# TABLE PLAN
372	# ============================================================
373	table_plan:
374	  - table_id: tab_1_detection_frontier
375	    type: comparison
376	    placement: "Section 2.2 (Background)"
377	    columns: [Method, "Info Required", "Post-RL Robust", "Per-Model", "Training-Free"]
378	    data_source: "paper_framing.md (method landscape), literature_map.yaml"
379	    description: >
380	      Detection frontier ranking all methods by information access level.
381	      Rows: n-gram overlap, Min-K%/MIA, Time Travel, ConStat, CoDeC, Self-Critique, accuracy z-score, IRT-FIT (ours).
382	      Shows IRT-FIT requires minimum information (binary patterns only) while being
383	      structurally RL-robust (binary patterns invariant to token distributional shifts).
384	      Checkmarks/crosses for properties. IRT-FIT row highlighted.
385	
386	  - table_id: tab_2_simulation_power
387	    type: results
388	    placement: "Section 5.2 (Simulation)"
389	    columns: [Benchmark, n_items, "Power@5%", "Power@15%", "Power@25%", "Power@50%", "Power@100%"]
390	    data_source: "registry: exp-extended-sim (two_sided_power)"
391	    description: >
392	      Two-sided detection power across 5 benchmarks and key contamination levels.
393	      Bold best per column. Shows power scales with benchmark size.
394	      Bottom row: theoretical prediction from power function.
395	      Include 95% CI from simulation (our differentiator vs peers who report no variance).
396	
397	  - table_id: tab_3_ctrl_contam
398	    type: results
399	    placement: "Section 5.3 (Controlled Contamination)"
400	    columns: [Condition, Accuracy, "θ_MLE", "lz*(free-θ)", "lz*(fixed-θ)", "Δlz*(free)", "Δlz*(fixed)", "Cohen's d"]
401	    data_source: "registry: exp-ctrl-contam-pilot (metrics)"
402	    description: >
403	      Controlled contamination summary. 4 rows: clean_s1, clean_s2, contam_15, contam_50.
404	      Shows accuracy improvement, θ-shift, lz* under both estimation strategies,
405	      Δlz* relative to clean baseline, and effect sizes.
406	      Highlight: contam_15 |d|=3.58, θ-fixed ratio=2.93.
407	
408	  - table_id: tab_a1_full_lz_profiles
409	    type: appendix
410	    placement: "Appendix"
411	    columns: [Model, MMLU, HellaSwag, GSM8K, ARC-C, HumanEval, "Flagged/5"]
412	    data_source: "registry: phase_b_personfit, exp-fdr-correction"
413	    description: "Full 12-model lz* values with BH-FDR corrected flagging indicators."
414	
415	  - table_id: tab_a2_ml_classifier
416	    type: appendix
417	    placement: "Appendix"
418	    columns: [Method, "AUROC@5%", "AUROC@10%", "AUROC@25%", "AUROC@50%", "Training Data"]
419	    data_source: "registry: exp-ml-classifier-baseline"
420	    description: "ML classifier baseline comparison: lz* vs LR/RF at different contamination levels."
421	
422	  - table_id: tab_a3_4pl_ablation
423	    type: appendix
424	    placement: "Appendix"
425	    columns: [Benchmark, "4PL Power", "3PL Power", "Δ Power", "4PL FAR", "3PL FAR"]
426	    data_source: "registry: exp-4pl-ablation"
427	    description: "4PL vs 3PL(d=1) detection power and false alarm rate comparison at 25% contamination."
428	
429	  - table_id: tab_a4_irt_refit
430	    type: appendix
431	    placement: "Appendix"
432	    columns: [Method, N_models, "a_r (Pearson)", "b_r (Pearson)", Notes]
433	    data_source: "registry: exp-v1-irt-refit-pilot, exp-v1-irt-refit-expanded"
434	    description: "MML-EM IRT refit results from v1 leaderboard data. Documents estimation failure (a_r=0.13)."
435	
436	# ============================================================
437	# LITERATURE STRATEGY
438	# ============================================================
439	literature_strategy:
440	  total_target: 30-35
441	  current_count: 10
442	  current_verified: 0
443	
444	  micro_clusters:
445	    - cluster_name: irt-foundations
446	      target_count: 5
447	      current_verified: 0
448	      search_queries:
449	        - "item response theory textbook Lord Novick"
450	        - "four-parameter logistic model IRT"
451	        - "IRT model comparison 2PL 3PL 4PL"
452	      must_cite:
453	        - "Lord 1980 (Applications of IRT)"
454	        - "Embretson & Reise 2000 (Item Response Theory for Psychologists)"
455	        - "Barton & Lord 1981 (4PL model)"
456	
457	    - cluster_name: person-fit
458	      target_count: 6
459	      current_verified: 0
460	      current_in_map: 3  # sinharay2017, karabatsos2003, hong2021lzm
461	      search_queries:
462	        - "person-fit statistics lz lz* Drasgow"
463	        - "Snijders 2001 person-fit correction"
464	        - "appropriateness measurement person-fit IRT"
465	        - "item preknowledge detection person-fit cheating"
466	      must_cite:
467	        - "Drasgow et al. 1985 (original lz statistic - Appropriateness Measurement)"
468	        - "Snijders 2001 (lz* correction - Asymptotic Distribution)"
469	        - "Meijer & Sijtsma 2001 (person-fit review)"
470	
471	    - cluster_name: contamination-detection
472	      target_count: 10
473	      current_verified: 0
474	      current_in_map: 3  # constat2024, minkprob2024, codec2026
475	      search_queries:
476	        - "benchmark contamination detection LLM"
477	        - "data contamination large language models"
478	        - "membership inference attack language model"
479	        - "Time Travel probing benchmark contamination"
480	        - "n-gram overlap contamination GPT"
481	      must_cite:
482	        - "Oren et al. 2024 (Time Travel Probing - ICLR 2024 Spotlight)"
483	        - "Golchin & Surdeanu 2024 (Time Travel original)"
484	        - "Dodge et al. 2021 (C4 documentation, training data contamination)"
485	        - "Jacovi et al. 2023 or similar contamination survey"
486	        - "Sainz et al. 2023 (NLP evaluation contamination survey)"
487	
488	    - cluster_name: irt-llm
489	      target_count: 4
490	      current_verified: 0
491	      current_in_map: 2  # psnirt2026, atlas2025
492	      search_queries:
493	        - "item response theory large language model evaluation"
494	        - "IRT LLM benchmark psychometric"
495	        - "computerized adaptive testing LLM"
496	      must_cite:
497	        - "PSN-IRT (AAAI 2026 Oral) - already in map"
498	        - "ATLAS (adaptive testing LLM) - already in map"
499	
500	    - cluster_name: post-rl-contamination
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48060ead-6106-4dac-86c2-d2cbe509a6df",
  "isSidechain": true,
  "promptId": "31e35546-d5bc-4421-b240-8a865eeba806",
  "agentId": "a457d51ccc9db3c1c",
  "type": "user",
  "uuid": "31ab0d27-69fe-458c-9b91-fb3b88eeaf51",
  "sourceToolAssistantUUID": "48060ead-6106-4dac-86c2-d2cbe509a6df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T23:36:11.901Z_

Perfect! Now I have a comprehensive understanding of the paper. Let me create a detailed summary for you:

## Paper State Summary: IRT-FIT (Benchmark Contamination Detection)

**File Locations:**
- Main paper: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`
- Sections: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/`

---

### PAPER NARRATIVE OVERVIEW

**Title:** "Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics"

**Venue:** EMNLP 2026 (8-page main text + references)

**Core Narrative Arc:**
1. **Problem** (Introduction): LLMs may be trained on benchmark items, inflating evaluation scores. All prior detection methods require "privileged access" (training data, logits, probabilities). The paper asks: *what can be detected from binary response patterns alone?*

2. **Key Insight** (Cross-domain bridge): A contaminated LLM is functionally equivalent to a test-taker who memorized answers—both produce anomalous response patterns. This is exactly what **person-fit statistics** (40+ years of psychometric cheating detection) measure.

3. **Method** (IRT-FIT Framework):
   - Input: binary responses + pre-calibrated 4PL item parameters (from PSN-IRT)
   - Step 1: Estimate ability θ via MLE per benchmark
   - Step 2: Compute person-fit statistic **ℓz***, which measures pattern aberrance
   - Step 3: Use **Δℓz*** (difference-in-differences across benchmarks) to detect contamination
   - Key insight: Δℓz* cancels systematic IRT misfit bias common across benchmarks

4. **Theoretical Characterization**: Derives a closed-form power function showing detection sensitivity scales with √(benchmark size). At 80% power, detecting 15% contamination requires ≥7,958 items (e.g., MMLU works, ARC-C doesn't).

5. **θ-Shift Boundary Condition**: Contamination inflates ability estimates, which "explain away" aberrant patterns. Solution: anchor ability (θ-fixed) to pre-contamination baselines. Restores monotonic dose-response (3.12× signal ratio).

---

### KEY EXPERIMENTAL FINDINGS

**Simulation Validation (Well-Calibrated):**
- Null: ℓz* ~ N(0,1) with mean bias 0.041, std 1.003
- Power at 15% contamination: 97.8% (MMLU), scales with √n
- Theoretical power function: R² = 0.957
- 4PL vs 3PL ablation: +27.3pp power gain (upper asymptote parameter critical)

**Controlled Contamination (QLoRA on Qwen2.5-7B × MMLU):**
- 15% contamination: |Cohen's d| = 3.58 (3 clean seeds as baseline)
- Signal exceeds noise floor by 6.2×
- Free-θ non-monotonic; fixed-θ monotonic (ratio = 3.12)
- Memorization fraction: 0.38 (15%), 0.29 (50%)—SFT generalizes beyond exact memorization

**Empirical Real-Data Findings (12 models × 5 benchmarks):**
- 57/60 model-benchmark cells flagged (BH-FDR α=0.05)
- 93.3% positive ℓz* (over-consistency—models answer hard items too correctly)
- Accuracy z-score flags only 4/60 (14× less sensitive)
- Gemini-1.5-Flash MMLU: 100% accuracy, ℓz*=+34.75 (extreme outlier)
- IRT parameter estimation gap: MML-EM refit fails on discrimination (r_a=0.127)

---

### NOTATION CONVENTIONS & KEY VARIABLES

**Core Notation:**
- **θ**: latent ability parameter (estimated via MLE per model-benchmark)
- **ℓz***: standardized log-likelihood residual (Snijders 2001), distributed N(0,1) under null
  - Negative values → aberrant pattern (unexpected errors on easy items)
  - Positive values → over-consistent pattern (too-predictable correct responses)
- **Δℓz***: difference-in-differences statistic (target benchmark - reference benchmark)
- **4PL model**: P_i(θ) = c_i + (d_i - c_i) / (1 + exp(-a_i(θ - b_i)))
  - a_i: discrimination, b_i: difficulty, c_i: guessing (lower asymptote), d_i: slip (upper asymptote)

**Experiment Parameters:**
- Benchmarks: MMLU (14,042 items), HellaSwag (10,042), GSM8K (1,319), ARC-C (295), HumanEval (164)
- Contamination levels: 0%, 3%, 5%, 10%, 15%, 25%, 50%, 60%, 75%, 90%, 100%
- Controlled contamination: QLoRA rank=16, α=32 on Qwen2.5-7B-Instruct

---

### CURRENT STATE OF PAPER SECTIONS

| Section | Status | Notes |
|---------|--------|-------|
| **main.tex** | ✓ Complete | Structure in place, all includes defined |
| **Introduction** | ✓ Complete | 700 words; establishes motivation, problem statement, contributions |
| **Background** | ✓ Complete | 650 words; IRT foundations + person-fit literature + contamination methods |
| **Method** | ✓ Complete | 600 words; framework, power theory, θ-shift analysis |
| **Experiments** | ✓ Complete | 1000 words total; 4 subsections: setup, simulation, ctrl-contam, empirical |
| **Discussion** | ❌ **EMPTY** | Placeholder only (1 line: "% discussion") |
| **Limitations** | ❌ **EMPTY** | Placeholder only (1 line) |
| **Conclusion** | ❌ **EMPTY** | Placeholder only (1 line) |
| **Abstract** | ❌ **EMPTY** | Placeholder only (1 line) |

---

### WRITING PLAN GUIDANCE FOR DISCUSSION

From `writing_plan.yaml`, the **Discussion** should:
- **Word budget:** 200 words
- **Key elements:**
  1. Interpret simulation-reality gap (well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions)
  2. Position Δℓz* design as practical solution (within-model comparison leverages well-calibrated null)
  3. Discuss scalability (13K+ v1 binary data public, retrospective audit feasible)
  4. Clarify scope: SFT contamination & leaderboard gaming (NOT pretraining exposure)
  5. Future work: large-scale audit, multi-model-family ctrl-contam, post-RL validation

---

### CRITICAL ACTION ITEMS (from writing_plan)

**AI-11 to AI-13 (Discussion-relevant):**
- AI-11: Discuss limitation of single model family (Qwen only); future multi-family work
- AI-12: Frame QLoRA low-rank bias as "results conservative" (38% memorization is lower bound)
- AI-13: **Precise wording on post-RL:** Do NOT claim "robust to post-RL." Instead: "structurally invariant to RL distributional changes — empirical verification is future work"

**UC-1 (Critical correction):**
- The 57/60 flagging is evidence of **universal misfit** (LLM responses deviate from IRT), NOT direct contamination detection proof
- Use for: arguing ℓz* captures response-pattern info beyond accuracy
- Actual contamination detection evidence: simulation AUROC +0.10@5%, controlled |d|=3.58, ℓz*≥ML at 5-10%

---

### NARRATIVE FLOW FOR YOUR DISCUSSION WRITING

1. **Paragraph 1 (Sim-Reality Interpretation):**
   - Bootstrap null calibrated (mean bias 0.041, std 1.003) ✓
   - Yet 57/60 real cells flagged → this is NOT artifact
   - Instead: **LLMs fundamentally violate IRT assumptions** (local independence, unidimensionality)
   - **Key insight:** Δℓz* design exploits this — shared bias cancels, leaving contamination signal

2. **Paragraph 2 (Practical Deployment & Scalability):**
   - Design pragmatism: Δℓz* doesn't require absolute lz* thresholds
   - Cross-benchmark or temporal anchoring for θ_fixed
   - Leaderboard audit feasible: binary responses widely recorded, retrospective application possible

3. **Paragraph 3 (Scope & Limitations):**
   - Scope: SFT contamination & leaderboard gaming (quantifiable injection)
   - NOT pretraining: can't detect incidental overlap in massive corpora
   - Controlled study single family (Qwen) → future: GPT family, open-weight ensemble

4. **Paragraph 4 (Future Work):**
   - Post-RL validation (empirical), multi-model ctrl-contam, large-scale audit with RL-era models

---

### REFERENCE TO KEY FIGURES & TABLES

- **Figure 2** (Power function): Theoretical vs simulated across 5 benchmarks
- **Figure 3** (Controlled contamination): Free-θ non-monotonic → fixed-θ restores (panel a), seen/unseen split (panel b)
- **Figure 4** (12-model heatmap): Gemini-1.5 extreme outlier, Ward clustering typologies
- **Table 1** (Detection frontier): Method × information access (background section)

---

This is your complete narrative map. The discussion should synthesize the simulation-to-reality gap (why universal misfit ≠ artifact), position Δℓz* as the practical solution, and frame scope precisely around SFT contamination rather than pretraining exposure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ab0d27-69fe-458c-9b91-fb3b88eeaf51",
  "isSidechain": true,
  "agentId": "a457d51ccc9db3c1c",
  "requestId": "req_011CbEhSrN1eEpA34kMdqscQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55f6e008-3461-4c18-afab-5a02a8bb83eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "65f14483-aca3-41bd-bcbf-df203e375789",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fm3pPgsAQt96pJgXGLkaWG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15034,
      "cache_read_input_tokens": 38005,
      "output_tokens": 2557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2557,
          "cache_read_input_tokens": 38005,
          "cache_creation_input_tokens": 15034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15034,
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
