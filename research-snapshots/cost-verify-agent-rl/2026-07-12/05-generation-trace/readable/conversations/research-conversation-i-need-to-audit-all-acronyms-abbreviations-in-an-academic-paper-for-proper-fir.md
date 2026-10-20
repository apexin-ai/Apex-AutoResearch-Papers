# Research conversation: I need to audit all acronyms/abbreviations in an academic paper for proper first-use definitions. Read all the main text

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac217588467cbf2b7.jsonl`
- **Structured JSON:** [`e8edf70c2005f425d299.json`](../../sessions/e8/e8edf70c2005f425d299.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-24T18:24:43.238Z_

I need to audit all acronyms/abbreviations in an academic paper for proper first-use definitions. Read all the main text .tex files of this paper and list every acronym/abbreviation used, noting whether it's defined at first use with "Full Name (ACRONYM)" format.

The paper files are at:
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/

Read these files in order:
1. main.tex (abstract, limitations)
2. introduction.tex
3. related_work.tex
4. method.tex
5. theoretical_analysis.tex
6. experiments.tex
7. discussion.tex
8. conclusion.tex

For each file, list ALL acronyms/abbreviations found (including method names like GRPO, PPO, RLHF, HCAPO, GiGPO; dataset names like ALFWorld; model names like Qwen3; metric/concept abbreviations like OOD, SFT, ID, NaN, POMDP, CI, NS, etc.).

For each acronym, note:
- Where it first appears (which file, approximate context)
- Whether the full form is given at first use
- If it appears in the abstract, whether it's also defined there

Be very thorough - check every single abbreviation including common ones like RL, LLM, OOD, ID, SFT, GRPO, PPO, RLHF, DPO, NaN, POMDP, CI, etc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "da13591f-8050-49f2-96ee-187c183be763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T18:24:44.643Z_

I'll audit all acronyms and abbreviations in the paper. Let me start by reading all the LaTeX files in order.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da13591f-8050-49f2-96ee-187c183be763",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2fd14d1-838d-4e4f-aa06-e11bca0ea9f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 3 · 2026-05-24T18:24:45.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MrT6U3iZC2ev9jV26LJh1v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fd14d1-838d-4e4f-aa06-e11bca0ea9f5",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d77f3b83-3dbe-434d-82e2-db3af574762a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 4 · 2026-05-24T18:24:45.132Z_

<details><summary>↩ Tool result · `toolu_01MrT6U3iZC2ev9jV26LJh1v`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
18	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
19	\setlength{\intextsep}{5pt plus 2pt minus 2pt}
20	
21	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Correction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Reinforcement learning for multi-turn LLM agents requires credit assignment across long interaction trajectories. The dominant training paradigm decomposes these trajectories into fixed-size windows optimized independently via Group Relative Policy Optimization (GRPO), yet this ubiquitous design choice has received little scrutiny. We identify a structural credit assignment pathology driven by two distinct mechanisms: \textit{policy information loss}, which truncates cross-window context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes a substantial fraction of gradient updates for locally correct actions to carry incorrect sign. A partial factorial experiment (3 of 4 cells) isolates each mechanism: removing sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables out-of-distribution (OOD) generalization. Direct sign measurement confirms the theoretical prediction, with credit agreement dropping to near-random levels. Episode-level GRPO, which treats the full trajectory as a single optimization sample, addresses both failure modes, yielding 17.2\% mean OOD success versus 6.7\% SFT baseline. However, a systematic multi-seed evaluation reveals that avoiding collapse is necessary but not sufficient: 73\% of seeds stabilize, yet only 36\% achieve statistically significant OOD transfer. Cross-scale verification at 8B parameters and cross-environment validation on ScienceWorld provide preliminary evidence that the pathology extends beyond our primary setting.
30	\end{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{method}
35	\input{theoretical_analysis}
36	\input{experiments}
37	\input{discussion}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	
42	Our experiments span two environments (ALFWorld, ScienceWorld) and two scales (1.7B, 8B); additional environments and scales would strengthen generality, and the 8B and ScienceWorld results are single-seed. Among 11 seeds at 1.7B, only 36\% achieve statistically significant OOD generalization; the mechanism driving seed-dependent transfer remains open. We do not reproduce concurrent methods (HCAPO, Turn-PPO, GiGPO); comparisons rely on published results and post-hoc consistency analysis.
43	
44	\bibliography{references}
45	
46	\clearpage
47	\input{appendix}
48	
49	\end{document}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d77f3b83-3dbe-434d-82e2-db3af574762a",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "514066b2-b18b-46b2-8195-e374265616d7",
  "sourceToolAssistantUUID": "d77f3b83-3dbe-434d-82e2-db3af574762a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T18:24:45.350Z_

<details open><summary>🔧 Tool call — Read · `toolu_012dt6ANfdLC9Wz44i7bgm8B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514066b2-b18b-46b2-8195-e374265616d7",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb3d2f37-9fd4-4429-b1ab-3e8ac5a64792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 6 · 2026-05-24T18:24:45.362Z_

<details><summary>↩ Tool result · `toolu_012dt6ANfdLC9Wz44i7bgm8B`</summary>

```text
1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=0.85\textwidth]{fig_overview.pdf}
4	\caption{Step-independent windowing (left) partitions the trajectory into fixed windows, each optimized independently. This introduces two failure mechanisms: M1 (information loss) truncates context at window boundaries, and M2 (sign misattribution) assigns all windows the same advantage sign based on episode outcome. Episode-level training (right) treats the full trajectory as a single sample, eliminating both mechanisms.}
5	\label{fig:overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:introduction}
10	
11	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern (decomposing trajectories into fixed-size windows, each optimized independently) and frequently report training instability without diagnosing its root cause.
12	
13	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies (dense reward shaping, discount tuning) fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2025}, HCAPO~\cite{hcapo2026}) address the credit assignment challenge through improved step-level mechanisms, validating that sign correctness is the critical factor. Our contribution is orthogonal: we formally diagnose \textit{why} the default windowing fails.
14	
15	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the advantage sign reflects episode success rather than local action quality. Our theoretical analysis shows that a substantial fraction of gradient updates for locally correct actions carry incorrect sign (Section~\ref{sec:theory}), a prediction confirmed by direct measurement (Section~\ref{sec:sign_verification}). Sign errors, amplified by the M1--M2 feedback loop, cause progressive degradation rather than merely slow convergence. Our primary contribution is diagnostic: we identify, formalize, and empirically validate a previously uncharacterized pathology in the dominant training paradigm. Episode-level GRPO (not a new method, but the original GRPO design) addresses both mechanisms by treating the full trajectory as a single optimization sample, achieving substantial OOD improvement where step-independent collapses to 0\%, with preliminary evidence of persistence at 8B scale.
16	
17	Our contributions:
18	\begin{enumerate}[nosep,leftmargin=*]
19	\item \textbf{Dual mechanism diagnosis.} We formalize \textit{information loss} and \textit{sign misattribution} as distinct failure modes with different temporal behaviors (constant ceiling versus cumulative degradation) and derive closed-form expressions for the probability of incorrect gradient direction.
20	\item \textbf{Controlled empirical separation.} A partial factorial experiment isolates each mechanism: removing sign misattribution converts collapse into bounded learning; removing information loss enables OOD generalization. Direct sign measurement confirms the theoretical prediction at near-random credit agreement.
21	\item \textbf{Systematic evaluation and generality.} Episode-level training addresses both mechanisms, but an 11-seed evaluation reveals that avoiding collapse is necessary but not sufficient---only 36\% of seeds achieve significant OOD transfer. Cross-scale (8B) and cross-environment (ScienceWorld) evidence provides preliminary support for generality.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb3d2f37-9fd4-4429-b1ab-3e8ac5a64792",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "badf3e70-6407-45a2-8055-e9a89c919119",
  "sourceToolAssistantUUID": "bb3d2f37-9fd4-4429-b1ab-3e8ac5a64792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T18:24:45.534Z_

<details open><summary>🔧 Tool call — Read · `toolu_016akfJWNEewLS6w7QqNLpjg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "badf3e70-6407-45a2-8055-e9a89c919119",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52026bbc-1e87-4060-98c7-db82d40ce032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 8 · 2026-05-24T18:24:45.548Z_

<details><summary>↩ Tool result · `toolu_016akfJWNEewLS6w7QqNLpjg`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL for multi-turn LLM agents.}
5	GRPO~\cite{shao2024deepseekmath}, PPO~\cite{schulman2017ppo}, and RLHF methods~\cite{ouyang2022instructgpt,rafailov2023dpo} have been extended to multi-turn agents~\cite{yao2023react,ragen2025} via step-independent windowing. RAGEN~\cite{ragen2025} introduced this decomposition as a practical solution to memory constraints, partitioning trajectories into fixed-size windows each optimized as independent GRPO samples. Subsequent work builds on this foundation: DigiRL~\cite{digiRL2024} applies online RL to web agents with autonomous reward, SPEAR~\cite{spear2025} addresses entropy collapse through progressive reward scaling, and SelfGuide~\cite{selfguide2026} uses self-generated rewards. These systems inherit the step-independent design without examining its credit assignment implications---our work identifies this shared choice as a structural failure point.
6	
7	\paragraph{Credit assignment in RL.}
8	The credit assignment problem---determining which actions contributed to an outcome---is fundamental to RL~\cite{sutton1988td,williams1992reinforce}. Classical solutions include temporal difference learning, eligibility traces, and generalized advantage estimation~\cite{schulman2016gae} (Appendix~\ref{app:classical_connection}). Step-independent GRPO inherits the worst of outcome-vs-process supervision~\cite{lightman2024lets}: all windows receive episode-level credit regardless of individual action quality. Recent methods address this at different granularities: ArCHer~\cite{zhou2024archer} and VinePPO~\cite{kazemnejad2024vineppo} improve value estimation, PRIME~\cite{prime2025} and VAPO~\cite{vapo2025} refine credit granularity, while GiGPO~\cite{feng2025gigpo}, Turn-PPO~\cite{turnppo2025}, GAGPO~\cite{gagpo2026}, and HCAPO~\cite{hcapo2026} propose step- or turn-level advantage computation that preserves sign correctness. Our framework provides a unified explanation for \textit{why} these finer-grained methods succeed: they eliminate M2 (sign misattribution) while operating within the windowed framework. IRC~\cite{irc2026}, MC-GRPO~\cite{mcgrpo2026}, GRPO-$\lambda$~\cite{grpolambda2025}, and OAR~\cite{oar2026} independently corroborate our sign-level diagnosis from complementary perspectives.
9	
10	\paragraph{GRPO collapse phenomena.}
11	Training instability under GRPO has been documented across multiple settings. RAGEN-2~\cite{ragen2_2026} and GRPO-Collapse~\cite{grpocollapse2025} report reward variance collapse where all rollouts converge to similar returns, zeroing out advantages. RC-GRPO~\cite{rcgrpo2026} and EDGE-GRPO~\cite{edgegrpo2025} propose variance-preserving modifications. Our dual-mechanism framework subsumes these observations: reward variance collapse is a special case of the reward saturation phenomenon we analyze in Section~\ref{sec:theory}, arising when $\sigma \to 0$ in GRPO normalization. The M1--M2 vicious cycle---where information loss depresses success rate, amplifying sign errors, which further degrade performance---provides a causal mechanism for the empirically observed death spirals.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52026bbc-1e87-4060-98c7-db82d40ce032",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "09306b36-2b68-4bd7-8c7b-8f40ed8bb896",
  "sourceToolAssistantUUID": "52026bbc-1e87-4060-98c7-db82d40ce032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T18:24:45.779Z_

<details open><summary>🔧 Tool call — Read · `toolu_012tkZWTJZr39NBiBqMA7TrZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09306b36-2b68-4bd7-8c7b-8f40ed8bb896",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5c59a70-440e-4ccb-a3e9-8a2ce2eab570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 10 · 2026-05-24T18:24:45.785Z_

<details><summary>↩ Tool result · `toolu_012tkZWTJZr39NBiBqMA7TrZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP)~\cite{kaelbling1998planning} where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$ (our experiments use a penalty variant with $r_- = -0.1$ per invalid action; Section~\ref{sec:setup}). GRPO~\cite{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but structurally alters credit assignment.
24	
25	\subsection{Dual Mechanism Analysis}
26	\label{sec:dual_mechanism}
27	
28	Two mechanisms jointly cause training failure under step-independent optimization.
29	
30	\subsubsection{Mechanism 1: Policy Information Loss}
31	\label{sec:m1_information_loss}
32	
33	Step-independent training truncates context at both inference and training time. The policy $\pi_\phi(a_t \mid h_{\text{window}_k})$ conditions on only the local $h$-step history, losing access to earlier observations. With $h{=}2$, a window at step~8 has no access to the outcome of an exploration action at step~4, so the policy cannot learn strategies spanning more than $h$ steps. This imposes a \textit{constant} performance ceiling: no amount of optimization can recover absent information.
34	
35	\subsubsection{Mechanism 2: Advantage Sign Misattribution}
36	\label{sec:m2_sign_misattribution}
37	
38	Group normalization under step-independent training produces advantages whose sign reflects the \textit{episode} outcome, not local action quality:
39	\begin{equation}
40	\text{sign}(\hat{A}_k) \approx \text{sign}(R_{\text{episode}} - \mu)
41	\label{eq:sign_correlation}
42	\end{equation}
43	In failed episodes ($R_{\text{episode}} = 0$), all windows receive negative advantages when $\mu > 0$, including windows with locally correct actions. Conversely, successful episodes reinforce all windows, including those with suboptimal actions. Unlike M1's constant ceiling, sign misattribution is \textit{cumulative}: each wrong-sign gradient step further erodes policy competence. The discount factor $\gamma^{(N-k)}$ introduces magnitude decay across positions, but sign errors are strictly more harmful: magnitude decay slows convergence, while sign errors cause active divergence.
44	
45	\subsection{Episode-Level Training}
46	\label{sec:episode_level}
47	
48	Episode-level training addresses both mechanisms by treating the complete trajectory as a single GRPO sample. The full history $h_t$ is available at every step (eliminating M1), and a single advantage $\hat{A}$ applies uniformly to all tokens (eliminating M2). Uniform reinforcement of successful trajectories preserves good sub-strategies; window-level sign errors actively destroy them. This is GRPO's original design; step-independent windowing is the deviation.
49	
50	\subsection{Partial Factorial Design}
51	\label{sec:factorial_design}
52	
53	To separate the two mechanisms, we design a $2 \times 2$ partial factorial varying observation scope and advantage granularity: \textbf{Cell~A} (truncated $h{=}2$ + step-level advantage; both mechanisms active), \textbf{Cell~B} (truncated $h{=}2$ + episode-level advantage; only M1 active), \textbf{Cell~D} (full trajectory + episode-level advantage; neither active), and \textbf{Cell~C} (full trajectory + step-level advantage; only M2 active). Cell~C encountered persistent numerical instability across six hyperparameter configurations (Appendix~\ref{app:cell_c}); we therefore evaluate a partial 3-of-4 factorial. Comparing A vs.\ B isolates sign misattribution; comparing B vs.\ D isolates information loss.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5c59a70-440e-4ccb-a3e9-8a2ce2eab570",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "4d2252dd-701e-4b3b-bdb9-fd6f65ff27bd",
  "sourceToolAssistantUUID": "b5c59a70-440e-4ccb-a3e9-8a2ce2eab570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T18:24:46.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XgoBm8MBeBcgAZ96eRPSiF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d2252dd-701e-4b3b-bdb9-fd6f65ff27bd",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12d7cc40-12d3-4391-a4af-3c93d542b8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 12 · 2026-05-24T18:24:46.116Z_

<details><summary>↩ Tool result · `toolu_01XgoBm8MBeBcgAZ96eRPSiF`</summary>

```text
1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{fig_theory_curve.pdf}
4	\caption{Upper bound on the probability of correct gradient sign vs.\ episode success rate $p$ (Proposition~2). At typical agent task success rates ($p < 0.2$, shaded), the majority of gradient updates carry incorrect sign regardless of group size $K$.}
5	\label{fig:theory_curve}
6	\end{figure}
7	
8	\section{Theoretical Analysis}
9	\label{sec:theory}
10	
11	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
12	
13	\textbf{Definition 1} (Locally correct action). \textit{An action $a_t$ is \textbf{locally correct} if it would receive positive advantage under an oracle that observes the full episode history $h_t$ and has access to the true action-value function. Equivalently,\footnote{This equivalence is approximate; it holds exactly when all trajectories within an episode are equally likely under the reference policy, and approximately under the mild assumption that policy drift remains small during early training.} window $k$ contains locally correct actions if replacing them (holding all other windows fixed) would decrease the probability of episode success.}
14	
15	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
16	
17	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_k < 0$---including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
18	
19	The key distinction is temporal. Information loss (M1) imposes a constant ceiling determined by $h$; sign misattribution (M2) is cumulative---each wrong-sign gradient step erodes policy competence below that ceiling. A wrong-sign gradient moves the optimizer \textit{away} from good policies; a reduced-magnitude gradient from discounting ($\gamma^{(N-k)}$) still points toward good policies. Sign errors produce active divergence; magnitude errors merely slow convergence (Appendix~\ref{app:sign_fundamental}).
20	
21	\textbf{Proposition 2.}\label{prop:correct_sign} \textit{Let $p$ denote the episode success rate and $K$ the number of rollouts per group. Under step-independent training with binary episode reward, the fraction of gradient updates with correct sign is upper bounded by:}
22	\begin{equation}
23	P(\text{correct} \mid \text{update}) \leq \frac{p}{1 - (1-p)^{K}}
24	\label{eq:correct_conditional}
25	\end{equation}
26	
27	\textit{Derivation.} Three mutually exclusive cases determine gradient direction for a window with locally correct actions: (1)~episode succeeded (probability $p$): correct sign; (2)~episode failed but group contains a success (probability $(1{-}p)[1{-}(1{-}p)^{K-1}]$): wrong sign; (3)~entire group failed (probability $(1{-}p)^K$): zero gradient. Conditioning on non-zero gradient (Cases 1 and 2) yields Equation~\ref{eq:correct_conditional}. The bound is tight when episode success implies all constituent windows are locally correct; in practice, successful episodes may contain suboptimal windows, so the true fraction of correctly signed updates may be lower.
28	
29	At $p{=}12.5\%$, $K{=}8$, this yields an upper bound of 19.1\% on correctly signed gradient updates (Figure~\ref{fig:theory_curve}). In the large-$K$ limit, $P(\text{correct} \mid \text{update}) \to p$: ${\sim}87.5\%$ of updates for locally correct windows point in the wrong direction.
30	
31	\paragraph{Severity scales with task difficulty.} Sign misattribution becomes \textit{more} severe as the task gets harder (Equation~\ref{eq:correct_conditional}): at $p{=}50\%$, $P(\text{correct} \mid \text{update}) \leq 50.2\%$; at $p{=}5\%$, at most 14.9\% of updates are correct. Multi-turn agent tasks with low baseline success rates are precisely where credit assignment matters most, yet where step-independent training produces the worst gradient signal. Increasing $K$ does not help: more updates occur (fewer all-fail groups), but each remains equally likely to carry the wrong sign.
32	
33	\paragraph{Reward saturation.} When all $K$ rollouts receive the same binary reward, $\sigma = 0$ and $\hat{A}_k = 0$, producing zero gradient. At $p{=}12.5\%$, $K{=}8$, the all-fail probability is $(1{-}p)^K \approx 34.4\%$; combined with the negligible all-success case ($p^K < 10^{-7}$), roughly one-third of batches yield no gradient at all. This compounds sign misattribution: of the ${\sim}66\%$ of batches that produce a gradient, at most 19.1\% have the correct sign. The effective learning rate is at most $0.66 \times 0.19 \approx 12.5\%$ of nominal---well below the regime where convergence guarantees hold.
34	
35	\paragraph{Cumulative divergence.} Sign misattribution produces a systematic gradient bias. Let $\theta^*$ denote an optimal policy parameterization. At each update, the expected gradient under step-independent training is:
36	\begin{equation}
37	\mathbb{E}[\nabla_\theta \mathcal{L}] = P_c \cdot g_+ + (1 - P_c) \cdot g_-
38	\label{eq:biased_gradient}
39	\end{equation}
40	where $P_c = P(\text{correct} \mid \text{update})$, $g_+$ points toward $\theta^*$, and $g_-$ points away. At the observed step-5 snapshot, $|\hat{A}_{\text{correct}}|/|\hat{A}_{\text{wrong}}| \approx 1.32$; whether this ratio holds across training stages remains to be verified. The cumulative divergence argument holds whenever this ratio is finite, regardless of its exact value. When $P_c < 0.5$ (which holds for $p < 0.5$; Equation~\ref{eq:correct_conditional}), the expected gradient points weakly away from good policies. The cumulative effect of this directional bias, amplified by the M1--M2 positive feedback loop (Section~\ref{sec:dual_mechanism}), drives progressive policy degradation: information loss (M1) caps $p$; lower $p$ increases wrong-sign frequency under M2, which further depresses $p$, producing the empirically observed collapse.
41	
42	\paragraph{Extension to ternary reward.} Our experimental setting uses ternary reward ($r \in \{-0.1, 0, 1\}$) rather than binary. Under ternary reward with penalty rate $\alpha$ (fraction of actions receiving $r_-$), binary reward ($\alpha{=}0$) yields the tightest bound on sign misattribution. Increasing $\alpha$ introduces within-group variance among failed episodes that partially breaks the sign-outcome coupling: windows with valid actions in failed episodes may obtain positive advantage when penalty-induced variance shifts the group mean downward. The measured 52\% credit agreement at $\alpha{\approx}0.3$ is consistent with this monotonic relaxation from the binary worst case. A binomial test confirms that the binary upper bound (19.1\%) and the empirical rate (52.1\%) measure different quantities ($z = 45.9$, $p < 10^{-100}$); both are far below the level required for reliable policy improvement (Appendix~\ref{app:nonbinary_extension}).
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12d7cc40-12d3-4391-a4af-3c93d542b8c2",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "5deb54ce-6600-48e4-b169-783190458982",
  "sourceToolAssistantUUID": "12d7cc40-12d3-4391-a4af-3c93d542b8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T18:24:46.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01217BELTZ9UJxeGujCzHwRT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5deb54ce-6600-48e4-b169-783190458982",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7cf225de-fc8f-4571-89ae-9e7aea213365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 14 · 2026-05-24T18:24:46.281Z_

<details><summary>↩ Tool result · `toolu_01217BELTZ9UJxeGujCzHwRT`</summary>

```text
1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{fig_training_dynamics.pdf}
4	\caption{(a)~Training dynamics across factorial conditions. Cell~A collapses; Cell~B shows bounded learning; Cell~D improves monotonically. (b)~Window size $h$ vs.\ success rate (single seed). Hatched bars indicate collapsed conditions ($0\%$).}
5	\label{fig:hsweep}
6	\end{figure*}
7	
8	\section{Experiments}
9	\label{sec:experiments}
10	
11	Step-independent training collapses while episode-level training succeeds; a partial factorial design separates the two mechanisms; and window size $h$ modulates severity.
12	
13	\subsection{Setup}
14	\label{sec:setup}
15	
16	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. The environment provides ternary reward: $R \in \{r_-, 0, r_+\}$, where $r_- = -0.1$ per invalid action, $0$ for valid but unsuccessful actions, and $r_+$ for task success. Our theoretical analysis (Section~\ref{sec:theory}) assumes the simplified binary case ($R \in \{0, r_+\}$), which yields an upper bound on sign misattribution severity; Section~\ref{sec:sign_verification} validates this bound under both reward structures. The base policy is Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5\% in-distribution). At this baseline success rate, Proposition~2 predicts the majority of gradient updates carry incorrect sign. All conditions use RAGEN~\cite{ragen2025} (v0.1, commit \texttt{3a6b48b})\footnote{Our implementation extends RAGEN v0.1 with episode-level training support. Code available upon acceptance.} with GRPO~\cite{shao2024deepseekmath} ($K{=}8$; full hyperparameters in Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary). Seed counts are noted per condition.
17	
18	\subsection{Partial Factorial Mechanism Separation}
19	\label{sec:factorial_experiments}
20	
21	We implement the partial factorial design from Section~\ref{sec:factorial_design} (3 of 4 cells; Cell~C excluded due to NaN instability) with two seeds per condition. Cell~C (full observation, step-level advantage) would isolate M2 without M1, but we encountered persistent training instability in this configuration (Appendix~\ref{app:cell_c}). Cell~C's NaN divergence, qualitatively different from Cell~A's gradual collapse, suggests that information loss may have an unintended stabilizing effect on gradient variance, and that the M1--M2 interaction may be non-additive (Section~\ref{sec:discussion}).
22	
23	\subsection{Results}
24	\label{sec:results}
25	
26	Cell~A collapses in two phases (Table~\ref{tab:main_results}): task success drops to 0\% while action validity initially remains high, then continued sign misattribution destroys even basic formatting. % exp_id: hsweep_h2_seed1, hsweep_h2_seed2
27	Cell~B eliminates sign misattribution while retaining information loss: training success improves, but OOD generalization (5.97\%) remains near the SFT baseline (6.72\%), confirming that removing M2 alone bounds learning without causing degradation.% exp_id: factorial_h2_episodeadv_seed1, factorial_h2_episodeadv_seed2
28	Cell~D is the only condition that substantially exceeds the SFT baseline, with monotonic OOD improvement across both seeds.% exp_id: exp029_episode_level, exp029_seed3_ood_v2
29	The A$\to$B comparison isolates M2; the B$\to$D comparison isolates M1. Both mechanisms are necessary to explain the full failure pattern (Figure~\ref{fig:hsweep}a).
30	
31	\begin{table}[t]
32	\centering
33	\caption{1.7B results on ALFWorld (best checkpoint per seed, 2 seeds each). Full seed-level breakdown in Table~\ref{tab:seed_variability} and Appendix~\ref{tab:additional_baselines}.}
34	\label{tab:main_results}
35	\resizebox{\columnwidth}{!}{%
36	\begin{tabular}{@{}llccc@{}}
37	\toprule
38	\textbf{Condition} & \textbf{Mechanisms} & \textbf{Best Step} & \textbf{In-Dist (\%)} & \textbf{OOD (\%)} \\
39	\midrule
40	SFT baseline & --- & --- & 12.50 & 6.72 \\
41	Cell A ($h{=}2$, step) & M1+M2 & 5 & 0 & 0 \\
42	Cell B ($h{=}2$, episode) & M1 only & 5 & 18.75 & 5.97 \\
43	Cell D (full, episode) & neither & 5 & \textbf{34.38} & \textbf{17.16} \\
44	\bottomrule
45	\end{tabular}}
46	% exp_id: hsweep_h2_seed1, factorial_h2_episodeadv_seed1, exp029_episode_level, exp029_seed3_v2
47	\end{table}
48	
49	\paragraph{Additional conditions.} Dense reward, REINFORCE++, and discount-factor sweep experiments all confirm that sign misattribution, not reward sparsity or discounting, drives the failure (Appendix~\ref{app:additional}).
50	
51	\paragraph{Window-size sweep.} Varying window size reveals a credit assignment threshold between $h{=}10$ and $h{=}20$ that separates collapse from recovery (Figure~\ref{fig:hsweep}b; single seed). Below this threshold, all conditions collapse to 0\%; above it, success rate increases monotonically with window size. This single-seed observation suggests a threshold effect; multi-seed verification is needed to confirm its location and robustness.% exp_id: h_sweep_series, exp029_seed1
52	\label{sec:results_hsweep}
53	
54	\subsection{Sign Misattribution Verification}
55	\label{sec:sign_verification}
56	
57	We distinguish three metrics that each capture a different aspect of credit assignment quality:
58	
59	\textit{(1) Sign-episode correlation}: whether advantage sign tracks episode outcome (success/failure). Under pure binary reward (penalty${=}0$), this correlation is near-perfect at 99.6\% ($270/271$ non-zero windows across three evaluation iterations; Figure~\ref{fig:sign_misattribution}), directly confirming M2: advantage sign is almost entirely determined by episode outcome, not local action quality.\footnote{The single discordant window (1/271) arises when a low-return successful episode is grouped with higher-return successes; GRPO normalization assigns negative advantage despite positive return. This is a group-composition edge case, not a violation of the theoretical mechanism.} This is by construction under binary reward, since all windows in a successful episode share the same positive return.% exp_id: binary_credit_agreement_iter0
60	
61	\textit{(2) Credit agreement rate}: whether advantage sign matches local action quality, operationalized through action validity as a proxy for local correctness (Definition~1). Under step-independent training with penalty reward ($h{=}2$, $n{=}3{,}000$ windows), only 52.07\% of windows with valid actions receive positive advantage, marginally above random chance ($p{=}0.025$ vs.\ 50\%; Cohen's $h = 2\arcsin\sqrt{0.5207} - 2\arcsin\sqrt{0.5} \approx 0.041$, below the 0.2 small-effect threshold), confirming that credit agreement is effectively at chance, consistent with the theoretical prediction of near-random sign assignment. This near-random credit agreement shows that advantage sign carries almost no information about local action quality. Under pure binary reward, credit agreement drops further to 28\% ($n{=}271$), below random chance---advantage sign systematically punishes valid actions in failed episodes. Penalty reward partially breaks sign-episode correlation by introducing within-group variance, but the resulting signal remains too weak for meaningful credit assignment. This operationalization is conservative: successful episodes may contain suboptimal windows, making our validity label an upper bound on true local correctness. Even under this generous criterion, credit agreement remains near-random, strengthening the diagnosis.% exp_id: 7b_cell_a_h2
62	
63	\textit{(3) $P(\text{correct} \mid \text{update})$}: the theoretical upper bound from Proposition~2 ($\leq$19.1\% at $p{=}12.5\%$, $K{=}8$). This bounds the fraction of non-zero gradient updates with correct sign, a different quantity from the credit agreement rate, which conditions on action validity rather than gradient participation. The two metrics are complementary: Proposition~2 bounds worst-case gradient quality; credit agreement measures empirical signal strength.
64	
65	Combined with $\gamma{=}1.0$ collapse (Appendix~\ref{app:additional}), these measurements are consistent with sign misattribution as a primary factor in training failure, though the credit agreement effect is substantively small ($+$2pp above random).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_sign_misattribution.pdf}
70	\caption{Sign-episode correlation (binary reward) vs.\ credit agreement rate (penalty reward). Under binary reward, advantage sign tracks episode outcome near-perfectly, confirming M2. Under penalty reward, credit agreement drops to near-random chance (dashed line).}
71	\label{fig:sign_misattribution}
72	\end{figure}
73	
74	\subsection{Episode-Level Training: Seed Variability}
75	\label{sec:seed_variability}
76	
77	Episode-level GRPO addresses the dual-mechanism failure, but training outcomes remain seed-dependent. We systematically evaluate $N{=}11$ random seeds under identical hyperparameters, revealing a $2{\times}2$ structure: \textit{training stability} (collapsed vs.\ non-collapsed) $\times$ \textit{OOD generalization} (stagnant vs.\ generalized).
78	
79	We define \textbf{collapsed} seeds as those where in-distribution success declines $>$50\% from peak and remains below baseline for $\geq$3 consecutive steps. \textbf{Non-collapsed} seeds are the complement. Among non-collapsed seeds, we further distinguish \textbf{generalized} (Fisher exact $p{<}0.01$ vs.\ SFT on the 134-task OOD set) from \textbf{stagnant} (not significant vs.\ SFT). Table~\ref{tab:seed_variability} reports results for each seed at its best-performing checkpoint.
80	
81	\begin{table}[t]
82	\centering
83	\caption{Episode-level GRPO across 11 seeds (134 OOD tasks, best checkpoint per seed). C=Collapsed, S=Stagnant, G=Generalized (Fisher exact $p{<}0.01$ vs.\ SFT). Wilson 95\% CI. SFT baseline: 6.72\%.}
84	\label{tab:seed_variability}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{@{}llcccc@{}}
87	\toprule
88	\textbf{Seed} & \textbf{Step} & \textbf{Cat.} & \textbf{OOD (\%)} & \textbf{95\% CI} & \textbf{vs SFT} \\
89	\midrule
90	seed2048$^\ddagger$ & 5 & C & 8.21 & [4.6, 14.2] & NS \\
91	seed42$^\ddagger$ & 5 & C & 12.69 & [8.0, 19.4] & NS \\
92	seed8 & 5 & C & 11.94 & [7.5, 18.5] & NS \\
93	\midrule
94	seed200 & 5 & S & 10.45 & [6.3, 16.8] & NS \\
95	seed300 & 5 & S & 10.45 & [6.3, 16.8] & NS \\
96	seed100 & 5 & S & 11.19 & [6.9, 17.6] & NS \\
97	seed100 & 10 & S & 12.69 & [8.0, 19.4] & NS \\
98	seed2$^\ddagger$ & 15 & S & 15.67 & [10.5, 22.8] & $p{=}0.03$ \\
99	\midrule
100	seed1 & 5 & G$^\dagger$ & 23.88 & [17.4, 31.8] & $p{<}0.001$ \\
101	seed5 & 10 & G & 29.10 & [22.1, 37.3] & $p{<}0.001$ \\
102	seed6 & 15 & G & 29.10 & [22.1, 37.3] & $p{<}0.001$ \\
103	seed4 & 15 & G & 30.60 & [23.5, 38.7] & $p{<}0.001$ \\
104	\bottomrule
105	\end{tabular}}
106	\begin{flushleft}
107	\small $^\dagger$ RAGEN built-in eval; checkpoint unavailable for re-evaluation. \\
108	\small $^\ddagger$ OOD evaluated via RAGEN built-in eval; not independently re-evaluated under D134 protocol. \\
109	\small All results are single-run evaluations at $\tau{=}0.4$; see Limitations for eval variance discussion.
110	\end{flushleft}
111	\end{table}
112	
113	\begin{figure}[t]
114	\centering\vspace{-3pt}
115	\includegraphics[width=0.95\columnwidth]{fig_seed_variability.pdf}\vspace{-5pt}
116	\caption{OOD success rate across 11 episode-level GRPO seeds (Wilson 95\% CI). Seeds partition into \textit{Generalized} ($p{<}0.01$ vs.\ SFT), \textit{Stagnant} (stable, NS), and \textit{Collapsed} ($\times$). Avoiding collapse is necessary but not sufficient.}
117	\label{fig:seed_variability}\vspace{-8pt}
118	\end{figure}
119	
120	Three outcomes emerge (Table~\ref{tab:seed_variability}, Figure~\ref{fig:seed_variability}): ${\sim}$27\% collapse with response length inflation (Appendix~\ref{app:response_length}), ${\sim}$36\% stagnate near SFT, and ${\sim}$36\% generalize. Stable training is necessary but not sufficient; the mechanism driving seed-dependent transfer remains open (Section~\ref{sec:discussion}).% exp_id: exp029 multi-seed series
121	
122	\subsection{Cross-Scale and Cross-Environment Verification}
123	\label{sec:cross_scale}
124	
125	A single-seed 8B experiment confirms both failure and fix persist at scale: Cell~A collapses within two steps while Cell~D reaches 90.3\% OOD (Appendix~\ref{app:8b_results}); restricting to $h{=}2$ confirms severe information loss. The pathology is environment-general: step-independent training on ScienceWorld~\cite{wang2022scienceworld} also collapses to 0\% across all 15 steps with comparable M1 gap.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5, scienceworld_grpo_cell_a, sw_info_loss_bjb1
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf225de-fc8f-4571-89ae-9e7aea213365",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "137d63d7-24dc-44b2-a8a3-7983cbfcf731",
  "sourceToolAssistantUUID": "7cf225de-fc8f-4571-89ae-9e7aea213365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T18:24:46.595Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LSosgnGnLV7XDHvmss6dRY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "137d63d7-24dc-44b2-a8a3-7983cbfcf731",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e5f69a4-3b68-46b9-93d5-dbd770ae78ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 16 · 2026-05-24T18:24:46.608Z_

<details><summary>↩ Tool result · `toolu_01LSosgnGnLV7XDHvmss6dRY`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Generality and mechanism interaction.}
5	Sign misattribution arises whenever step-level windowing, sparse binary reward, and group-relative normalization co-occur (Section~\ref{sec:theory}), though verified only on GRPO with ALFWorld and ScienceWorld. M1 and M2 interact: M1 lowers $p$, amplifying wrong-sign updates under M2 (Appendix~\ref{app:why_defaults}). Cell~C's NaN instability (vs.\ Cell~A's gradual collapse) suggests M1 may unintentionally stabilize training. Multi-seed evaluation reveals bimodal OOD transfer pointing to initialization sensitivity (Appendix~\ref{app:early_signal}).
6	
7	\paragraph{Concurrent methods.}
8	HCAPO~\cite{hcapo2026} (91.4\%, 7B) and GiGPO~\cite{feng2025gigpo} (90.2\%) succeed with $h{=}2$ by eliminating M2 through finer-grained credit---consistent with M2 as the primary bottleneck at sufficient scale (post-hoc analysis; see Limitations).
9	
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e5f69a4-3b68-46b9-93d5-dbd770ae78ee",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "c7cdf2cf-5d39-49b8-b2c8-73c78a2d378e",
  "sourceToolAssistantUUID": "6e5f69a4-3b68-46b9-93d5-dbd770ae78ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T18:24:46.664Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YJwf5doDtUMxnFmSmZ5eeo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7cdf2cf-5d39-49b8-b2c8-73c78a2d378e",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMry7saaW56v9Kw3Y61w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "129149cc-2bbc-46ea-81e0-bce12107be10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SmVVD6FDMdcfKmBbaHNCGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39894,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39894,
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

_source line 18 · 2026-05-24T18:24:46.679Z_

<details><summary>↩ Tool result · `toolu_01YJwf5doDtUMxnFmSmZ5eeo`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training fails through two mechanisms: information loss imposes a constant performance ceiling while sign misattribution causes cumulative degradation. Episode-level GRPO validates the diagnosis by addressing both, though only 36\% of seeds achieve significant OOD generalization. This finding applies to GRPO-style methods under step-level windowing, sparse reward, and group-relative normalization (Section~\ref{sec:dual_mechanism}), verified on GRPO in ALFWorld and ScienceWorld.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "129149cc-2bbc-46ea-81e0-bce12107be10",
  "isSidechain": true,
  "promptId": "3a87a2d4-8f82-4454-a231-484e795a1123",
  "agentId": "ac217588467cbf2b7",
  "type": "user",
  "uuid": "897eed23-8e98-4f29-88e4-1966df7d5cdf",
  "sourceToolAssistantUUID": "129149cc-2bbc-46ea-81e0-bce12107be10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T18:25:09.760Z_

Now I'll compile a comprehensive acronym audit based on all the files I've read. Let me analyze each acronym systematically:

## Comprehensive Acronym Audit for Paper

### **ACRONYMS FOUND AND ANALYSIS**

#### **1. LLM (Large Language Model)**
- **First appearance**: main.tex, abstract, line 29
- **Definition at first use**: ❌ NO - appears as "multi-turn LLM agents" without expansion
- **Also in abstract**: YES
- **Status**: NOT PROPERLY DEFINED at first use

#### **2. GRPO (Group Relative Policy Optimization)**
- **First appearance**: main.tex, abstract, line 29
- **Definition at first use**: ✅ YES - "Group Relative Policy Optimization (GRPO)"
- **Status**: PROPERLY DEFINED

#### **3. OOD (Out-of-Distribution)**
- **First appearance**: main.tex, abstract, line 29
- **Definition at first use**: ✅ YES - "out-of-distribution (OOD)"
- **Status**: PROPERLY DEFINED

#### **4. SFT (Supervised Fine-Tuning)**
- **First appearance**: main.tex, abstract, line 29
- **Definition at first use**: ✅ YES - "6.7% SFT baseline"
  - Actually, checking more carefully: appears as "SFT baseline" in abstract without explicit definition
  - Later defined in experiments.tex section 13 line 16: "SFT baseline: 12.5%"
- **Status**: NOT DEFINED at first use (abstract), defined later in experiments

#### **5. M1 (Mechanism 1 - Policy Information Loss)**
- **First appearance**: introduction.tex, line 5
- **Definition at first use**: ✅ YES - "M1 (information loss)" 
- **Status**: PROPERLY DEFINED

#### **6. M2 (Mechanism 2 - Advantage Sign Misattribution)**
- **First appearance**: introduction.tex, line 5
- **Definition at first use**: ✅ YES - "M2 (sign misattribution)"
- **Status**: PROPERLY DEFINED

#### **7. RL (Reinforcement Learning)**
- **First appearance**: main.tex, abstract, line 29
- **Definition at first use**: ❌ NO - "Reinforcement learning for multi-turn LLM agents" - no parenthetical expansion
- **Status**: NOT DEFINED (though widely understood)

#### **8. PPO (Proximal Policy Optimization)**
- **First appearance**: related_work.tex, line 4
- **Definition at first use**: ❌ NO - "PPO~\cite{schulman2017ppo}"
- **Status**: NOT PROPERLY DEFINED

#### **9. RLHF (Reinforcement Learning from Human Feedback)**
- **First appearance**: related_work.tex, line 4
- **Definition at first use**: ❌ NO - "RLHF methods~\cite{ouyang2022instructgpt,rafailov2023dpo}"
- **Status**: NOT PROPERLY DEFINED

#### **10. RAGEN (from context, appears to be an agent RL system)**
- **First appearance**: related_work.tex, line 5
- **Definition at first use**: ❌ NO - "RAGEN~\cite{ragen2025}" - no expansion given
- **Status**: NOT DEFINED

#### **11. DigiRL**
- **First appearance**: related_work.tex, line 5
- **Definition at first use**: ❌ NO - "DigiRL~\cite{digiRL2024}" - no expansion
- **Status**: NOT DEFINED

#### **12. SPEAR**
- **First appearance**: related_work.tex, line 5
- **Definition at first use**: ❌ NO - "SPEAR~\cite{spear2025}" - no expansion
- **Status**: NOT DEFINED

#### **13. SelfGuide**
- **First appearance**: related_work.tex, line 5
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **14. GAE (Generalized Advantage Estimation)**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - "generalized advantage estimation~\cite{schulman2016gae}" mentioned but GAE acronym not explicitly expanded
- **Status**: NOT DEFINED (mentioned as full text)

#### **15. ArCHer**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **16. VinePPO**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **17. PRIME**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **18. VAPO**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **19. GiGPO**
- **First appearance**: introduction.tex, line 13
- **Definition at first use**: ❌ NO - "GiGPO~\cite{feng2025gigpo}"
- **Status**: NOT DEFINED

#### **20. GAGPO**
- **First appearance**: introduction.tex, line 13
- **Definition at first use**: ❌ NO - "GAGPO~\cite{gagpo2026}"
- **Status**: NOT DEFINED

#### **21. Turn-PPO**
- **First appearance**: introduction.tex, line 13
- **Definition at first use**: ❌ NO - "Turn-PPO~\cite{turnppo2025}"
- **Status**: NOT DEFINED

#### **22. HCAPO**
- **First appearance**: introduction.tex, line 13
- **Definition at first use**: ❌ NO - "HCAPO~\cite{hcapo2026}"
- **Status**: NOT DEFINED

#### **23. IRC**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - "IRC~\cite{irc2026}"
- **Status**: NOT DEFINED

#### **24. MC-GRPO**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - "MC-GRPO~\cite{mcgrpo2026}"
- **Status**: NOT DEFINED

#### **25. GRPO-λ (GRPO-Lambda)**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - "GRPO-$\lambda$~\cite{grpolambda2025}"
- **Status**: NOT DEFINED

#### **26. OAR**
- **First appearance**: related_work.tex, line 8
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **27. RAGEN-2**
- **First appearance**: related_work.tex, line 11
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **28. GRPO-Collapse**
- **First appearance**: related_work.tex, line 11
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **29. RC-GRPO**
- **First appearance**: related_work.tex, line 11
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **30. EDGE-GRPO**
- **First appearance**: related_work.tex, line 11
- **Definition at first use**: ❌ NO - citation only
- **Status**: NOT DEFINED

#### **31. POMDP (Partially Observable Markov Decision Process)**
- **First appearance**: method.tex, section 4, line 7
- **Definition at first use**: ✅ YES - "partially observable Markov decision process (POMDP)~\cite{kaelbling1998planning}"
- **Status**: PROPERLY DEFINED

#### **32. ALFWorld**
- **First appearance**: experiments.tex, section 13, line 16
- **Definition at first use**: ❌ NO - "We evaluate on ALFWorld~\cite{shridhar2021alfworld}"
- **Status**: NOT DEFINED (though explained via citation context as "text-based household environment")

#### **33. ScienceWorld**
- **First appearance**: experiments.tex, line 125
- **Definition at first use**: ❌ NO - "ScienceWorld~\cite{wang2022scienceworld}"
- **Status**: NOT DEFINED

#### **34. Qwen3**
- **First appearance**: experiments.tex, section 13, line 16
- **Definition at first use**: ❌ NO - "The base policy is Qwen3-1.7B"
- **Status**: NOT DEFINED

#### **35. NaN (Not a Number)**
- **First appearance**: experiments.tex, line 21
- **Definition at first use**: ❌ NO - "Cell~C excluded due to NaN instability"
- **Status**: NOT DEFINED (though it's a standard computing term)

#### **36. OOD (repeated for experiments context)**
- **Status**: Already defined in abstract

#### **37. ID (In-Distribution)**
- **First appearance**: experiments.tex, line 16
- **Definition at first use**: ❌ NO - appears as "in-distribution" in text but "In-Dist" in table headers without definition
- **Status**: NOT EXPLICITLY DEFINED with acronym

#### **38. CI (Confidence Interval)**
- **First appearance**: experiments.tex, line 83
- **Definition at first use**: ❌ NO - "Wilson 95\% CI"
- **Status**: NOT DEFINED

#### **39. NS (Not Significant)**
- **First appearance**: experiments.tex, line 83
- **Definition at first use**: ❌ NO - appears in table as "NS"
- **Status**: NOT DEFINED

#### **40. DPO (Direct Preference Optimization)**
- **First appearance**: related_work.tex, line 4
- **Definition at first use**: ❌ NO - appears in citations as "rafailov2023dpo" without explicit expansion
- **Status**: NOT DEFINED

---

### **SUMMARY TABLE**

| Acronym | First File | First Use Defined? | Status |
|---------|------------|-------------------|--------|
| LLM | main.tex (abstract) | ❌ NO | MISSING DEFINITION |
| GRPO | main.tex (abstract) | ✅ YES | OK |
| OOD | main.tex (abstract) | ✅ YES | OK |
| SFT | main.tex (abstract) | ❌ NO | Missing in abstract, defined later |
| RL | main.tex (abstract) | ❌ NO | MISSING DEFINITION |
| M1 | introduction.tex | ✅ YES | OK |
| M2 | introduction.tex | ✅ YES | OK |
| PPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| RLHF | related_work.tex | ❌ NO | MISSING DEFINITION |
| RAGEN | related_work.tex | ❌ NO | MISSING DEFINITION |
| DigiRL | related_work.tex | ❌ NO | MISSING DEFINITION |
| SPEAR | related_work.tex | ❌ NO | MISSING DEFINITION |
| SelfGuide | related_work.tex | ❌ NO | MISSING DEFINITION |
| ArCHer | related_work.tex | ❌ NO | MISSING DEFINITION |
| VinePPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| PRIME | related_work.tex | ❌ NO | MISSING DEFINITION |
| VAPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| GiGPO | introduction.tex | ❌ NO | MISSING DEFINITION |
| GAGPO | introduction.tex | ❌ NO | MISSING DEFINITION |
| Turn-PPO | introduction.tex | ❌ NO | MISSING DEFINITION |
| HCAPO | introduction.tex | ❌ NO | MISSING DEFINITION |
| IRC | related_work.tex | ❌ NO | MISSING DEFINITION |
| MC-GRPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| GRPO-λ | related_work.tex | ❌ NO | MISSING DEFINITION |
| OAR | related_work.tex | ❌ NO | MISSING DEFINITION |
| RAGEN-2 | related_work.tex | ❌ NO | MISSING DEFINITION |
| GRPO-Collapse | related_work.tex | ❌ NO | MISSING DEFINITION |
| RC-GRPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| EDGE-GRPO | related_work.tex | ❌ NO | MISSING DEFINITION |
| POMDP | method.tex | ✅ YES | OK |
| ALFWorld | experiments.tex | ❌ NO | MISSING DEFINITION |
| ScienceWorld | experiments.tex | ❌ NO | MISSING DEFINITION |
| Qwen3 | experiments.tex | ❌ NO | MISSING DEFINITION |
| NaN | experiments.tex | ❌ NO | MISSING DEFINITION |
| ID | experiments.tex | ❌ NO | MISSING DEFINITION |
| CI | experiments.tex | ❌ NO | MISSING DEFINITION |
| NS | experiments.tex | ❌ NO | MISSING DEFINITION |
| DPO | related_work.tex | ❌ NO | MISSING DEFINITION |

---

### **CRITICAL ISSUES**

**High Priority (Abstract acronyms not defined at first use):**
1. **LLM** - Used in abstract line 29 without expansion
2. **SFT** - Used in abstract line 29 as "6.7% SFT baseline" without definition
3. **RL** - Used in abstract line 29 without expansion

**Medium Priority (Common method names/concepts not defined):**
- PPO, RLHF, DPO, GiGPO, GAGPO, Turn-PPO, HCAPO (concurrent methods mentioned in abstract/intro)
- RAGEN (the framework being extended, mentioned in intro)
- ALFWorld, ScienceWorld (datasets used in experiments)

**Low Priority (Less critical but should have definitions):**
- NaN, CI, NS, ID (statistical/computational terms)
- Qwen3 (model name)
- Various concurrent method variants

**RECOMMENDATIONS:**
1. Define LLM, RL, SFT in the abstract as "Reinforcement Learning (RL)" and "Large Language Model (LLM)" and "Supervised Fine-Tuning (SFT)"
2. Add brief glossary/definitions for all method names cited in intro/related work
3. Define dataset acronyms (ALFWorld, ScienceWorld) at first mention
4. Define statistical abbreviations (CI, NS, ID) when first used in tables

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897eed23-8e98-4f29-88e4-1966df7d5cdf",
  "isSidechain": true,
  "agentId": "ac217588467cbf2b7",
  "requestId": "req_011CbMryNfKoHRavt7hctx3p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2430a937-a1c8-4016-8746-7ac3db697141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/director_fd480a9c",
  "sessionId": "49a1b433-ab87-4540-bf0c-d46597468d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-knitting-wren",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013UXK8Sj71kBf41R7Vpytoh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12915,
      "cache_read_input_tokens": 39894,
      "output_tokens": 3822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3822,
          "cache_read_input_tokens": 39894,
          "cache_creation_input_tokens": 12915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12915,
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
