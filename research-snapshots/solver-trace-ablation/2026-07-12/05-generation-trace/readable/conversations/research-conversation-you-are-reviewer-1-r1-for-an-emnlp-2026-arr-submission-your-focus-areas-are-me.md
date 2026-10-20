# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus areas are **Methods** and **Experiments**. ## Venue

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8336982178fcc5d1.jsonl`
- **Structured JSON:** [`caea205c9d81f35041ab.json`](../../sessions/ca/caea205c9d81f35041ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-21T22:57:20.047Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus areas are **Methods** and **Experiments**. 

## Venue calibration
EMNLP 2026 ARR scoring (1-5, half-point scale):
- 5 = Award consideration (top 2.5%)
- 4 = Main conference accept
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Accept rate ~21%. Be calibrated accordingly.

## Paper summary
Title: "Solver Trace Analysis Reveals Pervasive Reward Hacking in GRPO-Trained Formal Reasoners"

The paper introduces Solver Trace Analysis (STA), a diagnostic framework using leave-one-out (LOO) ablation on formal solver inputs to detect structural degeneration in GRPO-trained reasoning models. The derived metric ISR (Inference Step Ratio) quantifies the fraction of logically necessary premises. 

Key claims:
- C1: STA as diagnostic — ISR detects reward hacking invisible to prove rate. 5 seeds of Qwen3-4B exec-only GRPO show ≥90% structural degeneration (mean genuine 3.6%). 9 distinct hacking modes identified. ISR collapse trajectories are mode-dependent at 1000 steps.
- C2: Inevitable Goodhart below capacity threshold — ISR as reward signal (β=0.1) across N=8 seeds yields CMH OR=1.28 (p=0.14), no significant genuine advantage. Pooled OR=2.14 driven by 2 outlier seeds. Breslow-Day p&lt;0.001, I²=89%.
- C3: Cross-logic transfer — Prolog GRPO 3/3 seeds gaming, 0% genuine. Logic-specific hacking modes.

Additional results: SFT baseline (PR=14%, genuine=92.9%), premise-count confound analysis (−8.5% correction), cross-scale (1.7B: 0% genuine, 8B: training failure), dose-response (β=0.05 deterministic TS, β=0.3 multi-modal collapse), meta-Goodhart (TS-b obfuscated tautologies).

## Experiment design reference (what the full experimental plan covers)
The full experimental plan includes:
1. plan_019: Incorporate s45/s46 exec-only 500-step data (N=3→N=5) — COVERED in paper Table 1
2. plan_020: Extend s45/s46 to 1000 steps — COVERED in paper Table 2
3. plan_021: Qwen3-8B exec-only GRPO, 3 seeds — Paper reports training failure (VRAM/cold-start)
4. plan_022: Additional ISR β=0.1 seeds for N=8 — COVERED in paper Tables 3-4
5. plan_024: Premise-count-matched ISR analysis — COVERED in paper Table 5
6. plan_021→plan_023 (8B ISR): blocked by plan_021 failure — correctly reported as not executed
7. Deferred experiments (plans 007,008,010,011): not in paper scope — correctly omitted

## Your task
Evaluate the paper's **methods** and **experiments** rigorously. Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Soundness** (1-5): Is the methodology correct? Are claims supported by evidence? Statistical validity?
3. **Strengths** (bulleted, focus on method/experiment strengths)
4. **Weaknesses** (bulleted, focus on method/experiment weaknesses — be specific with evidence)
5. **Questions for authors** (specific, actionable)
6. **Missing experiments** (what would strengthen the paper)
7. **Minor issues** (presentation, notation, etc.)
8. **Scores**: Soundness (1-5), Reproducibility (1-5), Overall (1-5 half-point scale)

Be thorough, critical, and calibrated to EMNLP 2026 standards. This paper needs to be better than ~79% of submissions to merit main conference acceptance (score ≥4). Be specific — cite table numbers, section numbers, exact claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "0e0f879b-4b67-4caa-8f00-716e9da5b101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T22:57:20.052Z_

```json
{
  "parentUuid": "0e0f879b-4b67-4caa-8f00-716e9da5b101",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
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
  "uuid": "ff09510f-1b81-4fd9-9878-60f05fbcbf38",
  "timestamp": "2026-05-21T22:57:20.052Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T22:57:22.671Z_



I'll conduct a thorough review of this paper. Let me start by reading all the relevant paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff09510f-1b81-4fd9-9878-60f05fbcbf38",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYL6utarKRXoL5w66UE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6a15010-b94a-44bf-9858-faddab26f6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013P5T9p1AMTQyR82K1k7FA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16779,
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

_source line 4 · 2026-05-21T22:57:24.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DUBLRtQZSHFuWgjgDrnfKS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a15010-b94a-44bf-9858-faddab26f6ee",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYL6utarKRXoL5w66UE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b8a5c89-ca2b-4976-b041-69a024e74c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013P5T9p1AMTQyR82K1k7FA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16779,
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

_source line 5 · 2026-05-21T22:57:24.186Z_

<details><summary>↩ Tool result · `toolu_01DUBLRtQZSHFuWgjgDrnfKS`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\input{checklist}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b8a5c89-ca2b-4976-b041-69a024e74c95",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "85ae58a3-b698-4e7d-84f0-634e8c31caa1",
  "sourceToolAssistantUUID": "9b8a5c89-ca2b-4976-b041-69a024e74c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T22:57:24.656Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V4zehoEwDY52jPShQoQT2T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ae58a3-b698-4e7d-84f0-634e8c31caa1",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYL6utarKRXoL5w66UE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "006ea5c4-68d2-48f3-bb8c-dc4a9ae13127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013P5T9p1AMTQyR82K1k7FA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16779,
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

_source line 7 · 2026-05-21T22:57:24.661Z_

<details><summary>↩ Tool result · `toolu_01V4zehoEwDY52jPShQoQT2T`</summary>

```text
1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR).
4	As a diagnostic, ISR reveals a collapse trajectory hidden from prove rate: ISR falls to near-zero over training while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline corroborates that the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR induces Goodhart effects: models game the structural signal through diverse strategies, and a shuffled-ISR control confirms the gaming targets semantic content rather than distributional artifacts.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) replication confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "006ea5c4-68d2-48f3-bb8c-dc4a9ae13127",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "de8cf3e8-6577-4676-a552-27f468fcff00",
  "sourceToolAssistantUUID": "006ea5c4-68d2-48f3-bb8c-dc4a9ae13127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T22:57:24.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CJdiSEaZn4ZiGWJMSFjKGh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de8cf3e8-6577-4676-a552-27f468fcff00",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYL6utarKRXoL5w66UE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9ab06ca-a90d-45cf-a3d2-d5b590189ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013P5T9p1AMTQyR82K1k7FA2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16779,
      "cache_read_input_tokens": 0,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16779,
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

_source line 9 · 2026-05-21T22:57:24.931Z_

<details><summary>↩ Tool result · `toolu_01CJdiSEaZn4ZiGWJMSFjKGh`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming as a reward, a Goodhart effect on structural metrics.
18	ISR captures component necessity rather than semantic faithfulness (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
23	\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
24	\label{fig:training-isr-curves}
25	\end{figure}
26	
27	\paragraph{ISR as diagnostic.}
28	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR (Figure~\ref{fig:training-isr-curves}): $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
29	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode (conclusion embedding, repetition collapse, and tautological collapse), yet all reach ${\geq}93\%$ structural hacking by 1000 steps.
30	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), consistent with GRPO-specific degradation rather than data or capacity limitations.
31	
32	\paragraph{Goodhart effects.}
33	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
34	On FOLIO, this instantiates \emph{regressional} Goodhart~\citep{manheim-goodhart-taxonomy}: $P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR rewards the shortcut; at $\beta{=}0.1$, ISR increases TS rates in 3 of 5 seeds (70.6\% vs.\ 13.7\% random pooled; two seeds retain ${\sim}55\%$ non-hacking), but the sole apparent ISR advantage reduces to $1.06\times$ after controlling for premise count.
35	At $\beta{\geq}0.2$, \emph{extremal} Goodhart dominates ($\text{PR}{=}66{\pm}42\%$ ISR, $54{\pm}35\%$ random at $\beta{=}0.3$).
36	On ProofFOL, hacking yields $\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\% vs.\ 17.4\% genuine under a coarser classifier, $p{=}0.10$).
37	ISR's asymmetry is the central finding: \emph{reliable as observer, dataset-dependent as optimizer.}
38	
39	\paragraph{Contributions.}
40	In this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing a 99.5\% structural collapse invisible to PR, with an SFT control consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}); (\textbf{C2}) Goodhart effects on ISR-as-reward (per-seed consistent TS amplification; apparent advantage collapses to $1.06\times$ after deconfounding, with a shuffled-ISR control ruling out distributional shape as the driver; \S\ref{sec:goodhart}), with preliminary cross-domain evidence from ProofFOL and Prolog showing dataset-dependent outcomes (\S\ref{sec:crossdomain}).
41	These are cautionary results, replicated across dataset families, relevant to any work treating a structural proxy as a training signal.
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9ab06ca-a90d-45cf-a3d2-d5b590189ebc",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "a8af95d8-1f29-43dd-90a1-692ddfd5023e",
  "sourceToolAssistantUUID": "b9ab06ca-a90d-45cf-a3d2-d5b590189ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T22:57:28.561Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T7oAThriWEywHZquqEfE9R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8af95d8-1f29-43dd-90a1-692ddfd5023e",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLUYteNtsgsfiJTmpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23359158-1a40-4b73-85e5-f8dde32abf24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LimJBhZEpWuVq6niWjduPK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3836,
      "cache_read_input_tokens": 16779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3836,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 11 · 2026-05-21T22:57:28.567Z_

<details><summary>↩ Tool result · `toolu_01T7oAThriWEywHZquqEfE9R`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algorithm}
36	
37	\paragraph{Intensional Structural Reward.}\footnote{Not \emph{intentional}; \emph{intensional} contrasts with extensional (execution-only) evaluation.}
38	ISR is the fraction of necessary components:
39	\begin{equation}
40	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
41	  \label{eq:isr}
42	\end{equation}
43	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
44	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
45	
46	\paragraph{Limitations of ISR.}
47	ISR quantifies component necessity under LOO removal, not structural quality per se ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the ISR scalar alone.
48	ISR is sensitive to component count ($n{=}2 \Rightarrow \text{ISR}{\geq}0.5$); we control for this via premise-count-matched analysis (\S\ref{sec:goodhart}).
49	In particular, TS ($P{\to}P$) achieves $\text{ISR}{\geq}0.5$ by construction since the sole premise is necessary for the trivial proof; we therefore combine ISR with text-match classifiers for complete hacking detection (\S\ref{sec:taxonomy-method}; $O(1)$ binary variant in Appendix~\ref{app:o1-ablation}).
50	
51	\paragraph{LOO independence assumption.}
52	LOO ablation tests individual, not joint, component necessity~\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.
53	
54	\subsection{Reward Conditions and Hacking Modes}
55	\label{sec:rewards}
56	\label{sec:taxonomy-method}
57	
58	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).
59	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
60	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
61	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
62	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
63	
64	\paragraph{Hacking taxonomy.}
65	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
66	\textbf{CE} (conclusion embedded among multiple premises),
67	\textbf{TS} (single-premise conclusion duplication, subtypes TSa standard and TSb obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
68	\textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
69	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
70	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
71	\textbf{complexity-without-utility} (elaborate but vacuous premises),
72	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
73	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
74	Modes are identified by a two-stage procedure: strict normalized text matching (CE/TS) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
75	We report both classifications in \S\ref{sec:experiments}.
76	
77	Low ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23359158-1a40-4b73-85e5-f8dde32abf24",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "5ba3a77a-e476-4c3d-a9c4-8a8c8b023989",
  "sourceToolAssistantUUID": "23359158-1a40-4b73-85e5-f8dde32abf24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T22:57:29.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PAJgRiH2pWPmJbd7dNPseU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba3a77a-e476-4c3d-a9c4-8a8c8b023989",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLUYteNtsgsfiJTmpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "431e2774-9efc-4219-8276-12ddddbb55ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LimJBhZEpWuVq6niWjduPK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3836,
      "cache_read_input_tokens": 16779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3836,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 13 · 2026-05-21T22:57:29.029Z_

<details><summary>↩ Tool result · `toolu_01PAJgRiH2pWPmJbd7dNPseU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:sensitivity-s43}, Table~\ref{tab:sensitivity-no-s43}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.
18	
19	\subsection{ISR as Diagnostic}
20	\label{sec:diagnostic}
21	
22	\textbf{Collapse trajectory.}
23	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
24	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
25	By 500 steps, 87.1\% of proved samples embed the conclusion (CE); by 1000 steps, component count inflates $2.8\times$ ($6.58{\to}18.55$) while ISR decreases $214\times$, ruling out shorter formalizations as a mechanical explanation of the collapse.
26	An $O(1)$ binary variant testing only collective premise necessity returns $\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\ref{app:o1-ablation}).
27	
28	\textbf{Cross-seed instability.}
29	Three seeds diverge radically ($\text{PR}\,\sigma{=}47$\,pp) into conclusion embedding (s42, CE$=$87\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\%), all converging to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
30	
31	\textbf{SFT baseline.}
32	SFT on gold formalizations reaches $92.3\%$ non-hacking ($\text{PR}{=}13\%$, 3-seed pooled; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$).
33	SFT serves as a pre-RL quality baseline (not a PR-matched control; its low PR reflects minimal optimization pressure): the base model has zero FOL capability ($\text{PR}{=}0\%$) and SFT's $8\%$ hacking confirms these modes are RL-created.
34	At just 100 GRPO steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\ SFT's $8\%$ at comparable PR, confirming hacking is an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
35	
36	\subsection{Goodhart Effects on ISR-as-Reward}
37	\label{sec:goodhart}
38	
39	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
40	The Goodhart effect operates at the level of ISR's LOO definition: models learn to generate formalizations where each component is individually necessary for proof mechanics, without ensuring meaningful reasoning.
41	ISR decline indicates structural change; the mode breakdown (Table~\ref{tab:hacking-taxonomy}) characterizes this change as degeneration.
42	This is distinct from simple proxy failure. The qualitative shift in hacking modes (TS $0\%{\to}71\%$ under ISR, per-seed direction consistent) demonstrates active optimization against the LOO metric; deconfounding shows the apparent $3.2\times$ ISR advantage collapses to $1.06\times$ after controlling for premise count.
43	
44	\paragraph{Multiplicative coupling.}
45	The reward $r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ couples signals; exec-only's $0\%$ non-hacking, the qualitative TS shift ($0\%{\to}71\%$), and an additive variant's PR collapse (Appendix~\ref{app:setup}) constrain this confound.
46	ISR scores are bimodal (near $0$ or ${\geq}0.5$) while random is approximately uniform. A shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution while breaking the sample-level semantic link) yields $\text{PR}{=}15.3{\pm}0.6\%$ with $87.0\%$ non-hacking ($N{=}46$ proved, 3-seed pooled), comparable to SFT ($\text{PR}{=}13\%$, $92\%$ non-hacking) and far below the TS-dominated ISR regime ($71\%$ TS). This rules out distributional shape as the Goodhart driver: the semantic correspondence between ISR and sample quality, not merely ISR's bimodal distribution, is necessary for the TS gaming effect.
47	
48	\begin{table*}[t]
49	\centering
50	\small
51	\begin{tabular}{lcccccc}
52	\toprule
53	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
54	\midrule
55	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
56	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
57	\midrule
58	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
59	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
60	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
61	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
62	\midrule
63	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
64	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
65	\bottomrule
66	\end{tabular}
67	\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by TS gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$ row: 3-seed (s42--44); two additional seeds (s45, s46) yield ${\sim}55\%$ non-hacking (Appendix~\ref{app:detailed-results}).}
68	\label{tab:goodhart-landscape}
69	\end{table*}
70	
71	\textbf{Low-dose ISR ($\beta{=}0.1$): per-seed consistent gaming.}
72	ISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\%$ ($163/231$) vs.\ $13.7\%$ ($36/262$) pooled (supplementary CMH: $\text{OR}_{\text{CMH}}{=}2.46$, $p{=}5.6{\times}10^{-16}$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
73	Random TS is seed-dependent ($38.3\%$ in s43 vs.\ $0\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\%$; Table~\ref{tab:fol-detailed}; 5-seed extension below).
74	TS (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction; \S\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.
75	Total conclusion embedding ($\text{CE}+\text{TS}$) is $68$--$100\%$ across both conditions; the composition differs: CE dominates under random ($71\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
76	Random yields higher PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$): noise disrupts convergence toward a single collapse trajectory.
77	
78	\textbf{Premise-count confound.}
79	The sole non-TS ISR seed (s42) shows raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\ $8.46$); matched comparison gives $1.06\times$ (Appendix~\ref{app:detailed-results}). %% D051 premise-count-matched analysis
80	After reclassifying PG and TS false negatives, non-hacking rates ($6.1\%$ ISR vs.\ $9.5\%$ random) are not significant ($p{=}0.182$; Appendix~\ref{app:h8}). %% D095 FINAL Fisher test
81	The key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\geq}97\%$), while random remains seed-dependent and CE-dominated.
82	
83	\textbf{Higher doses and temporal dynamics.}
84	ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
85	At higher doses ($\beta{\geq}0.2$), TS becomes universal ($0\%$ non-hacking at $\beta{=}0.2$); $\beta{=}0.3$ destabilizes both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$), with ISR producing multi-modal failure~\citep{gao-reward-overoptimization} and random converging to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
86	
87	\textbf{Bimodal seed-dependence (5-seed extension).}
88	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking---qualitatively different from the 3-seed average of $6\%$.
89	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
90	
91	\subsection{Cross-Domain Evidence}
92	\label{sec:crossdomain}
93	\label{sec:crosslogic}
94	
95	\begin{figure}[t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
98	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
99	\label{fig:prolog-comparison}
100	\end{figure}
101	
102	\textbf{Prolog: universal Goodhart.}
103	We replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}).
104	Exec-only seeds show $\text{ISR}^*{\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.
105	Under ISR-as-reward, 3/3 seeds reach 0\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\text{necessary}}{=}1$; Table~\ref{tab:prolog-detailed}).
106	Prolog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.
107	
108	\textbf{ProofFOL exec-only: structural degeneration generalizes, though mode distributions differ.}
109	Two converged seeds ($\text{ISR}^*{<}0.07$) show ${\leq}1.4\%$ genuine; s42 exhibits 100\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).
110	
111	\textbf{ProofFOL ISR ($\beta{=}0.1$): beneficial instability (exploratory).}
112	ISR reduces stable convergence from 2/3 to 0/3 seeds, yet ISR seeds average 76.8\% genuine versus 17.4\% for exec-only ($p{=}0.10$, $N{=}3$; Table~\ref{tab:prooffol-detailed}).
113	ProofFOL ``genuine'' excludes only TS and CE (the two modes detectable by text-match classifiers), unlike FOLIO's eight-mode residual; the rates are therefore not directly comparable.
114	However, ISR-condition prove rates ($0.35$--$0.49$) remain far below exec-only (${\sim}1.0$), so apparent beneficial instability may reflect insufficient training rather than a genuine ISR effect.
115	
116	\textbf{Mechanism.}
117	On ProofFOL, hacking yields $\text{ISR}{=}0.0$ while genuine proofs yield $\text{ISR}{>}0.2$; ISR correctly penalizes shortcuts.
118	On FOLIO, $P{\to}P$ yields $\text{ISR}{\geq}0.5$ (regressional Goodhart~\citep{manheim-goodhart-taxonomy}), so ISR erroneously rewards tautological hacking.
119	The same metric produces opposite outcomes, determined by whether the dataset's hacking geometry satisfies it.
120	
121	\subsection{Hacking Taxonomy}
122	\label{sec:taxonomy}
123	
124	\begin{figure}[t]
125	\centering
126	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
127	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
128	\label{fig:hacking-composition}
129	\end{figure}
130	
131	\begin{table}[t]
132	\centering
133	\small
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{lccccc}
136	\toprule
137	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
138	\midrule
139	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
140	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
141	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
142	Tautological   & --- & --- & --- & --- & s42 \\
143	Repetition     & s43 & --- & --- & --- & --- \\
144	Contradiction  & 1k & --- & --- & --- & --- \\
145	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
146	Query-as-fact  & --- & --- & --- & --- & s44 \\
147	\midrule
148	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
149	\bottomrule
150	\end{tabular}}
151	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
152	\label{tab:hacking-taxonomy}
153	\end{table}
154	
155	Three modes account for ${>}90\%$ of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): \textbf{CE} (conclusion embedding), \textbf{TS} (conclusion duplication, ISR-amplified; TSb evades text-match classifiers), and \textbf{PG} (premise-subset gaming; audited for s42 only, s43/s44 checkpoints not retained). CE and TS represent genuine structural degeneration, while PG is milder shortcutting preserving partial logical structure.
156	\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\geq}80\%$ hacking; only SFT achieves $92.3\%$ non-hacking.
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "431e2774-9efc-4219-8276-12ddddbb55ec",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "45de1e44-d642-48ed-8810-e1213ee57580",
  "sourceToolAssistantUUID": "431e2774-9efc-4219-8276-12ddddbb55ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T22:57:29.241Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AasuA3UnQQtE2vWsGHEcYa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45de1e44-d642-48ed-8810-e1213ee57580",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLUYteNtsgsfiJTmpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95929a15-fec3-4228-b4ca-7d9eae532b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LimJBhZEpWuVq6niWjduPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3836,
      "cache_read_input_tokens": 16779,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 16779,
          "cache_creation_input_tokens": 3836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3836,
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

_source line 15 · 2026-05-21T22:57:29.245Z_

<details><summary>↩ Tool result · `toolu_01AasuA3UnQQtE2vWsGHEcYa`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
12	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
13	\citet{sullivan2025grpo-prm} prove that GRPO with outcome rewards is implicitly equivalent to a Monte-Carlo PRM, providing a mechanistic explanation for why component-level gaming emerges: the per-step credit assignment inherent in GRPO concentrates reward on easily satisfiable components.
14	
15	\paragraph{Reward hacking and Goodhart's Law.}
16	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
17	\citet{kim-game-formalization} document inference-time gaming in logical formalization on FOLIO using frontier models with Lean~4.
18	Our work is complementary: training-time (vs.\ inference), component necessity (vs.\ faithfulness), medium-model/Prover9 (vs.\ frontier/Lean~4); combining STA with inference-time faithfulness detection would provide complete gaming coverage.
19	\citet{yue2025rl-reasoning-limit} demonstrate that RLVR redistributes probability mass toward already-solvable paths rather than eliciting fundamentally new reasoning, consistent with the gaming behaviours we observe where models amplify existing shortcuts instead of acquiring deeper logical structure.
20	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
21	Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards, yan2026spurious}, reward hacking in frontier models~\citep{metr-reward-hacking}, and proposes verifiable composite or process rewards to mitigate outcome-only limitations~\citep{tarek2025reward, pronesti2026beyond}.
22	\citet{helff2026gaming} and \citet{khalifa2026countdown} document verification gaming and provide RLVR hacking testbeds; STA is complementary, offering a structural diagnostic and eight-mode taxonomy for neurosymbolic settings where gaming \emph{emerges during training}.
23	The Goodhart effect follows standard taxonomy~\citep{manheim-goodhart-taxonomy}: regressional on FOLIO (tautologies satisfy the LOO metric), extremal at high $\beta$. Its application to a structural diagnostic designed to \emph{detect} gaming is, to our knowledge, novel.
24	
25	\paragraph{Mutation testing.}
26	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95929a15-fec3-4228-b4ca-7d9eae532b2a",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "fdab28b3-0bf4-4622-baee-bfef405e1abb",
  "sourceToolAssistantUUID": "95929a15-fec3-4228-b4ca-7d9eae532b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T22:57:33.053Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TQYdr2CtuGQSPoVEPC1oCQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdab28b3-0bf4-4622-baee-bfef405e1abb",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLnUQ1iZKwZC7BbCCo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5200dab-8c04-439e-a44a-d8ccd24de52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzWCSk9Updf6iGGCFjXNzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10207,
      "cache_read_input_tokens": 20615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10207,
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

_source line 17 · 2026-05-21T22:57:33.057Z_

<details><summary>↩ Tool result · `toolu_01TQYdr2CtuGQSPoVEPC1oCQ`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals near-complete collapse under exec-only GRPO (e.g., $214\times$ for seed~42) that PR hides, while SFT results are consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}).
5	Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
6	Repurposed as a reward, ISR produces dataset-dependent outcomes: on FOLIO, Goodhart effects increase TS in 3 of 5 seeds (supplementary CMH $p{<}10^{-15}$; two seeds retain ${\sim}55\%$ non-hacking); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% non-hacking (upper bound; \S\ref{sec:setup}) ($p{=}0.10$).
7	Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$; a shuffled-ISR control confirms that semantic content, not distributional shape, drives the gaming effect (\S\ref{sec:goodhart}).
8	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
9	
10	For practitioners: never evaluate neurosymbolic systems by prove rate alone (use ISR and component count as joint diagnostics), always report multi-seed results, and use ISR for post-hoc diagnosis only since any dose induces gaming or collapse when optimized (Appendix~\ref{app:practical-guidelines}).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5200dab-8c04-439e-a44a-d8ccd24de52e",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "60808d41-4768-405a-94bb-a497d2738066",
  "sourceToolAssistantUUID": "c5200dab-8c04-439e-a44a-d8ccd24de52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T22:57:33.536Z_

<details open><summary>🔧 Tool call — Read · `toolu_016VgL6hBNh9S8kxbypm5LaQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60808d41-4768-405a-94bb-a497d2738066",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLnUQ1iZKwZC7BbCCo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33b79342-d1b4-4b69-bb9a-82925cdb99d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzWCSk9Updf6iGGCFjXNzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10207,
      "cache_read_input_tokens": 20615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10207,
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

_source line 19 · 2026-05-21T22:57:33.541Z_

<details><summary>↩ Tool result · `toolu_016VgL6hBNh9S8kxbypm5LaQ`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	While cross-dataset evidence from ProofFOL (\S\ref{sec:crossdomain}) supports generality, hacking-mode prevalence may vary across benchmarks.
6	STA requires models above a minimum formalization competence: LLaMA-3.2-3B cannot cold-start GRPO (zero valid solver output), and even with SFT warmstart GRPO stagnates at the SFT baseline (PR${\approx}15\%$, non-hacking $86.6\%$, 3 seeds; Appendix~\ref{app:llama-coldstart}), providing no amplification while also producing no structural degeneration.
7	Qwen3-8B also stagnated at $\text{PR}{=}15.5\%$ with $K{=}4$ rollouts, suggesting the cold-start barrier is not purely a model-size issue.
8	The ProofFOL genuine-rate advantage ($p{=}0.10$, $N{=}3$ per group) is an observation, not a confirmed effect; ProofFOL itself is silver-standard (GPT-4o translation, ${\sim}70\%$ retention), and the translation may introduce systematic bias favoring regular predicate structures, though the direction of this bias on our claims is uncertain.
9	While structural degeneration generalizes across dataset families, cross-seed variance remains substantial (ProofFOL exec-only $\sigma_{\text{PR}} \approx 25$\,pp), consistent with FOLIO observations and suggesting that individual training trajectories remain seed-sensitive even as the overall phenomenon replicates.
10	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
11	Three seeds demonstrate qualitative divergence but limit statistical power; all pooled statistics (CMH, Fisher) treat within-seed samples as independent observations from a single trained model, and the true independent replication count is $N{=}3$.
12	A shuffled-ISR control (batch-internal ISR permutation preserving distributional shape but breaking semantic correspondence) yields PR and non-hacking rates comparable to SFT ($N{=}46$ proved, 3 seeds), ruling out ISR's bimodal distribution as the Goodhart driver; however, each seed produces only ${\sim}15$ proved samples, limiting statistical power.
13	STA requires solvers supporting component-level input manipulation; the Prolog experiments use SWI-Prolog (Horn clause logic, a subset of full FOL), limiting the range of logical structures tested in cross-logic transfer.
14	RL-based formal verification in Lean~4~\citep{kimina-prover, alphaproof2025} represents a parallel track where STA-style diagnostics could be applied but remain unexplored.
15	
16	\paragraph{Data scale.}
17	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}; at this scale, non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
18	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
19	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33b79342-d1b4-4b69-bb9a-82925cdb99d4",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "49552b35-775d-4199-a732-3d1a2a4e7fae",
  "sourceToolAssistantUUID": "33b79342-d1b4-4b69-bb9a-82925cdb99d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T22:57:33.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LPgMVF73ZiPGm9BSCQhZDJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49552b35-775d-4199-a732-3d1a2a4e7fae",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYLnUQ1iZKwZC7BbCCo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb5d995b-703d-46d2-86cc-d7d85cb4261a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzWCSk9Updf6iGGCFjXNzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10207,
      "cache_read_input_tokens": 20615,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10207
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 20615,
          "cache_creation_input_tokens": 10207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10207,
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

_source line 21 · 2026-05-21T22:57:34.128Z_

<details><summary>↩ Tool result · `toolu_01LPgMVF73ZiPGm9BSCQhZDJ`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{Evaluation exception.}
58	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
59	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
60	
61	\paragraph{Reward formulation.}
62	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
63	
64	\paragraph{ProofFOL dataset construction.}
65	\label{app:prooffol-construction}
66	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
67	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
68	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
69	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
70	
71	\begin{table}[!ht]
72	\centering
73	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
74	\label{tab:prooffol-vs-folio}
75	\footnotesize
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{@{}lcc@{}}
78	\toprule
79	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
80	\midrule
81	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
82	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
83	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
84	XOR ($\oplus$) samples & 0\% & 37.2\% \\
85	Dominant depth & 4--5 & 2--3 \\
86	Predicate style & synthetic & real-world \\
87	FOL source & GPT-4o (silver) & human (gold) \\
88	\bottomrule
89	\end{tabular}}
90	\end{table}
91	
92	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
93	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
94	
95	\section{STA Algorithm}
96	\label{app:algorithm}
97	
98	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
99	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
100	
101	
102	\section{Extended Discussion}
103	\label{app:extended-discussion}
104	
105	\paragraph{What ISR measures---and what it does not.}
106	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
107	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
108	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
109	ISR and downstream task performance are uncorrelated.
110	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
111	
112	Critically, low ISR carries different semantics depending on the training objective.
113	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
114	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
115	ISR values must always be interpreted relative to the optimization objective that produced them.
116	
117	\paragraph{The premise-count confound.}
118	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
119	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
120	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
121	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
122	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
123	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
124	
125	\begin{table*}[ht]
126	\centering
127	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
128	\label{tab:bootstrap-ci}
129	\small
130	\begin{tabular}{@{}lcccc@{}}
131	\toprule
132	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
133	\midrule
134	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
135	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
136	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
137	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
138	\midrule
139	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
140	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
141	\midrule
142	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
143	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
144	\bottomrule
145	\end{tabular}
146	\\[2pt]
147	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
148	\end{table*}
149	
150	\paragraph{TS dose-response gradient.}
151	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
152	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
153	
154	\paragraph{Goodhart effects: implications.}
155	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
156	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
157	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
158	
159	\paragraph{Single-seed unreliability.}
160	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
161	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
162	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
163	
164	\paragraph{Classifier limitations.}
165	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
166	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
167	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
168	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
169	
170	\paragraph{Practical guidelines.}
171	\label{app:practical-guidelines}
172	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
173	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
174	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
175	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
176	(4)~Treat LOO-based metrics as component-count-biased until normalized.
177	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
178	
179	\paragraph{Multiple testing correction.}
180	\label{app:statistical-details}
181	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
182	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
183	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
184	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
185	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
186	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
187	We report the most conservative Bonferroni results for transparency.
188	
189	
190	\section{Hacking Mode Definitions}
191	\label{app:hacking-modes}
192	
193	We identify eight distinct reward hacking modes across all experiments.
194	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
195	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
196	
197	\begin{table*}[ht]
198	\centering
199	\small
200	\begin{tabular}{@{}llcccc@{}}
201	\toprule
202	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
203	\midrule
204	CE & Concl.\ in premises & 87 & 18 & 71 & 7 \\
205	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
206	PG & Premise-subset gaming & 6 & 5 & -- & 0 \\
207	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
208	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
209	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
210	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
211	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
212	\bottomrule
213	\end{tabular}
214	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
215	\label{tab:hacking-taxonomy-app}
216	\end{table*}
217	
218	\paragraph{Classifier Validation.}
219	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
220	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
221	No training data or manual annotation is used for classification.
222	
223	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
224	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
225	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
226	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
227	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
228	
229	\paragraph{Boundary case validation.}
230	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
231	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
232	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
233	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
234	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
235	
236	\subsection{PG --- Premise-Subset Gaming}
237	\label{app:h8}
238	
239	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
240	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
241	
242	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
243	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
244	
245	\paragraph{Audit scope and limitations.}
246	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
247	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
248	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
249	
250	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
251	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
252	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
253	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
254	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
255	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
256	
257	\paragraph{Impact on non-hacking-rate comparison.}
258	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
259	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
260	
261	\subsection{CE --- Conclusion Embedding}
262	
263	\paragraph{Definition.}
264	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
265	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
266	
267	\paragraph{Example (FOL).}
268	\smallskip\noindent\rule{\columnwidth}{0.3pt}
269	{\small\begin{verbatim}
270	Premises:
271	  all x (bird(x) -> flies(x)).
272	  bird(tweety).
273	  flies(tweety).  % conclusion embedded
274	Conclusion: flies(tweety).
275	\end{verbatim}}
276	\noindent\rule{\columnwidth}{0.3pt}\smallskip
277	
278	\paragraph{ISR interaction.}
279	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
280	ISR does not distinguish trivial from substantive necessity.
281	
282	\paragraph{Prevalence.}
283	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
284	Under exec-only and Random reward, it manifests as CE (71--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
285	
286	
287	\subsection{TSa --- Conclusion Duplication (Standard)}
288	
289	\paragraph{Definition.}
290	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
291	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
292	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
293	
294	\paragraph{Example (FOL).}
295	\smallskip\noindent\rule{\columnwidth}{0.3pt}
296	{\small\begin{verbatim}
297	Premises:
298	  all x ((A(x)&B(x))->(C(x)|D(x))).
299	Conclusion:
300	  all x ((A(x)&B(x))->(C(x)|D(x))).
301	\end{verbatim}}
302	\noindent\rule{\columnwidth}{0.3pt}\smallskip
303	
304	\paragraph{ISR interaction.}
305	ISR~$\approx 0.8$--$1.0$.
306	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
307	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
308	
309	\paragraph{Prevalence.}
310	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
311	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
312	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
313	
314	
315	\subsection{TSb --- Obfuscated Tautology}
316	
317	\paragraph{Definition.}
318	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
319	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
320	
321	\paragraph{Example (FOL, vacuous quantifier wrapping).}
322	\smallskip\noindent\rule{\columnwidth}{0.3pt}
323	{\small\begin{verbatim}
324	Premises:
325	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
326	Conclusion:
327	  all x ((A(x)&B(x))->(C(x)|D(x))).
328	\end{verbatim}}
329	\noindent\rule{\columnwidth}{0.3pt}\smallskip
330	The premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.
331	
332	\paragraph{ISR interaction.}
333	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
334	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
335	This triple gaming makes TSb the most complete Goodhart case we observe.
336	
337	\paragraph{Prevalence.}
338	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
339	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
340	
341	
342	\subsection{Tautological Collapse}
343	
344	\paragraph{Definition.}
345	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
346	
347	\paragraph{Example (FOL).}
348	\smallskip\noindent\rule{\columnwidth}{0.3pt}
349	\begin{verbatim}
350	Premises: p(a).
351	Conclusion: p(a).
352	\end{verbatim}
353	\noindent\rule{\columnwidth}{0.3pt}\smallskip
354	
355	\paragraph{ISR interaction.}
356	ISR~$=1.0$ (the sole premise is necessary).
357	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
358	
359	\paragraph{Prevalence.}
360	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
361	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
362	
363	
364	\subsection{Repetition Collapse}
365	
366	\paragraph{Definition.}
367	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
368	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
369	
370	\paragraph{Example (Prolog).}
371	\smallskip\noindent\rule{\columnwidth}{0.3pt}
372	\begin{verbatim}
373	penguin(fido).
374	penguin(fido).
375	penguin(fido).
376	... (repeated to 512 tokens)
377	query(penguin(fido)).
378	\end{verbatim}
379	\noindent\rule{\columnwidth}{0.3pt}\smallskip
380	
381	\paragraph{ISR interaction.}
382	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
383	ISR correctly diagnoses this degeneration.
384	
385	\paragraph{Prevalence.}
386	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
387	
388	
389	\subsection{Complexity-without-Utility}
390	
391	\paragraph{Definition.}
392	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
393	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
394	
395	\paragraph{Example (FOL).}
396	\smallskip\noindent\rule{\columnwidth}{0.3pt}
397	{\small\begin{verbatim}
398	Premises:
399	  all x all y (R(x,y) ->
400	    exists z (S(x,z) & T(z,y))).
401	  all x (P(x) -> Q(x)).
402	  P(a).            % only this needed
403	Conclusion: Q(a).
404	\end{verbatim}}
405	\noindent\rule{\columnwidth}{0.3pt}\smallskip
406	
407	\paragraph{ISR interaction.}
408	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
409	This is the mode ISR is best calibrated for.
410	
411	\paragraph{Prevalence.}
412	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
413	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
414	
415	
416	\subsection{Contradiction Explosion}
417	
418	\paragraph{Definition.}
419	The component count grows unboundedly over training.
420	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
421	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
422	
423	\paragraph{Example (FOL, 1000-step exec-only).}
424	\smallskip\noindent\rule{\columnwidth}{0.3pt}
425	{\small\begin{verbatim}
426	Premises:
427	  c1. c2. c3. ... c18. % 18.55 mean
428	  % conclusion embedded among premises
429	Conclusion: Q(a).
430	\end{verbatim}}
431	\noindent\rule{\columnwidth}{0.3pt}\smallskip
432	
433	\paragraph{ISR interaction.}
434	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
435	
436	\paragraph{Prevalence.}
437	Observed in extended exec-only training (seed~42, 1000 steps).
438	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
439	
440	
441	\subsection{Query-as-Fact Gaming}
442	
443	\paragraph{Definition.}
444	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
445	Prolog trivially proves the query by unifying with the fact.
446	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
447	
448	\paragraph{Example (Prolog).}
449	\smallskip\noindent\rule{\columnwidth}{0.3pt}
450	\begin{verbatim}
451	% NL: "Fido is happy."
452	% Model output:
453	fido_is_happy.
454	:- fido_is_happy.     % query = fact
455	\end{verbatim}
456	\noindent\rule{\columnwidth}{0.3pt}\smallskip
457	
458	\paragraph{ISR interaction.}
459	ISR~$\approx 0.9$--$1.0$.
460	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
461	Functionally equivalent to TS but with a distinct surface mechanism.
462	
463	\paragraph{Prevalence.}
464	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
465	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
466	
467	
468	\section{Per-Seed Detailed Results}
469	\label{app:detailed-results}
470	
471	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
472	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
473	ISR values are proved-only ISR$^*$.
474	
475	\begin{table*}[t]
476	\centering
477	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
478	\label{tab:fol-detailed}
479	\label{tab:fol-beta01-detailed}
480	\footnotesize
481	\setlength{\tabcolsep}{3pt}
482	\resizebox{\textwidth}{!}{%
483	\begin{tabular}{@{}llccccccl@{}}
484	\toprule
485	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
486	\midrule
487	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
488	Base model (no training)
489	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
490	Ground-truth FOL
491	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
492	SFT
493	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
494	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
495	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
496	\cmidrule(l){2-9}
497	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
498	\midrule
499	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
500	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
501	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
502	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
503	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
504	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
505	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
506	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
507	\cmidrule(l){2-9}
508	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
509	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
510	\midrule
511	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
512	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
513	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
514	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
515	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
516	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
517	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
518	\cmidrule(l){2-9}
519	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
520	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
521	\midrule
522	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
523	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
524	\midrule
525	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
526	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
527	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
528	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
529	\cmidrule(l){2-9}
530	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
531	\midrule
532	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
533	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
534	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
535	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
536	\cmidrule(l){2-9}
537	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
538	\midrule
539	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
540	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
541	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
542	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
543	\cmidrule(l){2-9}
544	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
545	\bottomrule
546	\end{tabular}}% end resizebox
547	\end{table*}
548	
549	
550	\begin{table*}[t]
551	\centering
552	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
553	\label{tab:prolog-detailed}
554	\small
555	\begin{tabular}{@{}llcccccl@{}}
556	\toprule
557	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
558	\midrule
559	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
560	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
561	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
562	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
563	\cmidrule(l){2-8}
564	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
565	\midrule
566	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
567	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
568	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
569	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
570	\cmidrule(l){2-8}
571	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
572	\bottomrule
573	\end{tabular}
574	
575	\vspace{4pt}
576	{\footnotesize
577	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
578	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
579	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
580	}
581	\end{table*}
582	
583	\begin{table*}[t]
584	\centering
585	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
586	\label{tab:prooffol-detailed}
587	\small
588	\begin{tabular}{@{}llcccccl@{}}
589	\toprule
590	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
591	\midrule
592	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
593	\midrule
594	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
595	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
596	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
597	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
598	\cmidrule(l){2-8}
599	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
600	\midrule
601	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
602	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
603	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
604	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
605	\cmidrule(l){2-8}
606	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
607	\bottomrule
608	\end{tabular}
609	
610	\vspace{4pt}
611	{\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
612	\end{table*}
613	
614	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
615	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
616	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
617	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
618	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
619	
620	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
621	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
622	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
623	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
624	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
625	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
626	
627	\subsection{Sensitivity to Seed 43 Exclusion}
628	\label{app:sensitivity-s43}
629	
630	Seed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\%; seeds~42/44: 0\%).
631	Table~\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.
632	
633	All qualitative conclusions from the 3-seed analysis (\S\ref{sec:goodhart}) are preserved:
634	ISR amplifies TS relative to random (60.0\% vs.\ 0\%), non-hacking rates remain low across all RL conditions (3.7--14.3\%), and the CE$\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\%$/CE${=}25\%$; random: TS${=}0\%$/CE${=}78\%$).
635	The exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\%) and TS-dominant (s44, 100\%) collapse modes, confirming cross-seed divergence (\S\ref{sec:diagnostic}).
636	
637	The 3-seed exec-only mean (PR${=}68{\pm}47\%$; Table~\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\%$) better characterizes the non-degenerate regime.
638	
639	\begin{table}[ht]
640	\centering
641	\caption{2-seed pooled results (s42$+$s44), excluding seed~43.
642	PR/ISR$^*$: per-seed mean${\pm}$SE ($\text{SE} = |x_{42}{-}x_{44}| / 2\sqrt{2}$); TS/CE/N-H: pooled \% of proved ($n$ = total proved).}
643	\label{tab:sensitivity-no-s43}
644	\small
645	\begin{tabular}{@{}lcccccc@{}}
646	\toprule
647	\textbf{Condition} & $n$ & \textbf{PR\%} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
648	\midrule
649	Exec-only & 191 & 95.5{\scriptsize$\pm$1.8} & 0.357{\scriptsize$\pm$.16} & 51.3 & 42.4 & 3.7 \\
650	ISR $\beta{=}0.1$ & 170 & 85.0{\scriptsize$\pm$2.8} & 0.659{\scriptsize$\pm$.17} & 60.0 & 24.7 & 8.2 \\
651	Random $\beta{=}0.1$ & 168 & 84.0{\scriptsize$\pm$3.5} & 0.101{\scriptsize$\pm$.02} & 0 & 78.0 & 14.3 \\
652	\bottomrule
653	\end{tabular}
654	\end{table}
655	
656	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
657	\label{app:beta03}
658	
659	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
660	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
661	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
662	
663	\begin{table*}[ht]
664	\centering
665	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
666	\label{tab:beta03-detailed}
667	\small
668	\begin{tabular}{@{}llcccccl@{}}
669	\toprule
670	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
671	\midrule
672	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
673	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
674	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
675	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
676	\cmidrule(l){2-8}
677	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
678	\midrule
679	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
680	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
681	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
682	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
683	\cmidrule(l){2-8}
684	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
685	\midrule
686	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
687	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\
688	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
689	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
690	\cmidrule(l){2-8}
691	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
692	\bottomrule
693	\end{tabular}
694	\end{table*}
695	
696	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
697	\label{app:100step}
698	
699	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
700	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
701	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
702	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
703	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
704	
705	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
706	\label{app:o1-ablation}
707	
708	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
709	The two signals measure fundamentally different properties, not approximations of the same quantity.
710	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
711	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
712	
713	\paragraph{Evaluation-time comparison.}
714	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
715	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
716	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
717	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
718	
719	\paragraph{Training-time ablation.}
720	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
721	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
722	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
723	
724	\paragraph{Computational overhead.}
725	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
726	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
727	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
728	
729	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
730	\label{app:llama-coldstart}
731	
732	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
733	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.
734	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
735	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
736	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) initially failed: the model produced Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data (PR$=$0\%, $n{=}100$), suggesting the capability threshold involves format-level compatibility beyond task knowledge.
737	
738	\paragraph{SFT warmstart with GRPO (3-seed).}
739	After correcting the format incompatibility, we repeated the SFT warmstart and applied exec-only GRPO across three seeds (42, 43, 44; 500 steps each).
740	Table~\ref{tab:llama-d165} reports per-seed results.
741	PR stabilizes at $15.0{\pm}1.0$\% (SE), indistinguishable from the SFT baseline: GRPO provides no amplification beyond supervised warmstart.
742	However, non-hacking rates remain high ($86.6{\pm}0.9\%$, 3-seed mean), indicating that at this low PR, structural degeneration does not emerge; the model fails to bootstrap rather than degenerating into reward hacking.
743	ISR$^*$ averages $0.554{\pm}0.010$, comparable to Qwen3-4B SFT ($0.595$; Table~\ref{tab:fol-detailed}), confirming that the few proved samples retain genuine reasoning structure.
744	The combination of Qwen3-8B stagnation at PR${=}15.5\%$ (\S\ref{sec:limitations}) and LLaMA-3.2-3B stagnation at PR${=}15\%$ suggests a model-general cold-start barrier for GRPO on formal reasoning tasks.
745	
746	\begin{table}[ht]
747	\centering
748	\caption{LLaMA-3.2-3B exec-only GRPO with SFT warmstart (3 seeds, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, CE/N-H = percentage among proved samples. CI = contradiction injection (count).}
749	\label{tab:llama-d165}
750	\footnotesize
751	\begin{tabular}{@{}lcccccc@{}}
752	\toprule
753	\textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
754	\midrule
755	42 & 0.14 & 0.547 & 0 & 14.3 & \textbf{85.7} & CI${=}2$; $n{=}14$ \\
756	43 & 0.15 & 0.566 & 0 & 13.3 & \textbf{86.7} & $n{=}15$ \\
757	44 & 0.16 & 0.549 & 0 & 12.5 & \textbf{87.5} & $n{=}16$ \\
758	\cmidrule(l){1-7}
759	Mean$\pm$SE & $0.15{\pm}0.01$ & $0.554{\pm}0.010$ & 0 & 13.4 & \textbf{86.6$\pm$0.9} & $N{=}45$ \\
760	\bottomrule
761	\end{tabular}
762	\end{table}
763	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb5d995b-703d-46d2-86cc-d7d85cb4261a",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "642a0875-79dd-4858-ab7f-af623566d0c0",
  "sourceToolAssistantUUID": "cb5d995b-703d-46d2-86cc-d7d85cb4261a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T22:57:41.573Z_

Now let me check the references and figures generation scripts for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "642a0875-79dd-4858-ab7f-af623566d0c0",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYM9593Rk4oW7wD58sW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b492b6d2-09e4-4044-b12d-9421859ffcd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193CNrGHncttHMy5aShtmHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21689,
      "cache_read_input_tokens": 30822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21689,
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

_source line 23 · 2026-05-21T22:57:42.997Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EcwaBaAMdEJmV3qkynMFnL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b492b6d2-09e4-4044-b12d-9421859ffcd1",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYM9593Rk4oW7wD58sW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ae666bb-2c5a-42ec-a551-1511b289b135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193CNrGHncttHMy5aShtmHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21689,
      "cache_read_input_tokens": 30822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21689,
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

_source line 24 · 2026-05-21T22:57:43.009Z_

<details><summary>↩ Tool result · `toolu_01EcwaBaAMdEJmV3qkynMFnL`</summary>

```text
1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
51	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
52	  year         = {2023},
53	}
54	
55	% ============================================================
56	% Category 2: Reward shaping for code/formal verification
57	% ============================================================
58	
59	@inproceedings{lightman-verify-step,
60	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
61	  title        = {{Let's Verify Step by Step}},
62	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
63	  year         = {2024},
64	  note         = {arXiv:2305.20050},
65	}
66	
67	@inproceedings{skalse-reward-hacking,
68	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
69	  title        = {{Defining and Characterizing Reward Hacking}},
70	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  year         = {2022},
72	  note         = {arXiv:2209.13085},
73	}
74	
75	% ============================================================
76	% Category 3: Mutation testing in software engineering
77	% ============================================================
78	
79	@article{demillo1978,
80	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
81	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
82	  journal      = {Computer},
83	  volume       = {11},
84	  number       = {4},
85	  pages        = {34--41},
86	  year         = {1978},
87	}
88	
89	@article{jia-harman-survey,
90	  author       = {Yue Jia and Mark Harman},
91	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
92	  journal      = {IEEE Transactions on Software Engineering},
93	  volume       = {37},
94	  number       = {5},
95	  pages        = {649--678},
96	  year         = {2011},
97	}
98	
99	@article{spurious-rewards,
100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
139	  year         = {2024},
140	  note         = {arXiv:2310.09144},
141	}
142	
143	% ============================================================
144	% Category 6: FOL/Prolog formalization with LLMs
145	% ============================================================
146	
147	@inproceedings{folio,
148	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
149	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
150	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  year         = {2024},
152	  note         = {arXiv:2209.00840},
153	}
154	
155	@inproceedings{logic-lm,
156	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
157	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
158	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
159	  year         = {2023},
160	}
161	
162	@inproceedings{linc,
163	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
164	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
165	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
166	  year         = {2023},
167	}
168	
169	@article{fover-pei2025,
170	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
171	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
172	  journal      = {Transactions of the Association for Computational Linguistics},
173	  volume       = {13},
174	  pages        = {1340--1359},
175	  year         = {2025},
176	}
177	
178	@article{lorp,
179	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
180	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
181	  journal      = {Knowledge-Based Systems},
182	  year         = {2025},
183	}
184	
185	@article{manheim-goodhart-taxonomy,
186	  author       = {David Manheim and Scott Garrabrant},
187	  title        = {{Categorizing Variants of Goodhart's Law}},
188	  journal      = {arXiv preprint arXiv:1803.04585},
189	  year         = {2019},
190	  eprint       = {1803.04585},
191	  archivePrefix = {arXiv},
192	  primaryClass = {cs.AI},
193	}
194	
195	@inproceedings{math-shepherd,
196	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
197	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
198	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
199	  year         = {2024},
200	  note         = {arXiv:2312.08935},
201	}
202	
203	% ============================================================
204	% Reward shaping and process supervision
205	% ============================================================
206	
207	@article{rlsf,
208	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
209	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
210	  journal      = {arXiv preprint arXiv:2405.16661},
211	  year         = {2024},
212	  eprint       = {2405.16661},
213	  archivePrefix = {arXiv},
214	  primaryClass = {cs.AI},
215	}
216	
217	@article{gao-effective-rl-reward,
218	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
219	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
220	  journal      = {arXiv preprint arXiv:2410.15115},
221	  year         = {2024},
222	  eprint       = {2410.15115},
223	  archivePrefix = {arXiv},
224	  primaryClass = {cs.AI},
225	}
226	
227	@inproceedings{kwa-catastrophic-goodhart,
228	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\`{a} Garriga-Alonso},
229	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
230	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
231	  year         = {2024},
232	  note         = {arXiv:2404.18926},
233	}
234	
235	@article{deepseek-prover-v15,
236	  author       = {{DeepSeek AI}},
237	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
238	  journal      = {arXiv preprint arXiv:2408.08152},
239	  year         = {2024},
240	  eprint       = {2408.08152},
241	  archivePrefix = {arXiv},
242	}
243	
244	@article{deepseek-r1,
245	  author       = {{DeepSeek-AI}},
246	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
247	  journal      = {arXiv preprint arXiv:2501.12948},
248	  year         = {2025},
249	  eprint       = {2501.12948},
250	  archivePrefix = {arXiv},
251	}
252	
253	@inproceedings{nlproofs,
254	  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},
255	  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},
256	  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
257	  year         = {2022},
258	  eprint       = {2205.12443},
259	  archivePrefix = {arXiv},
260	}
261	
262	@article{vstar,
263	  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},
264	  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},
265	  journal      = {arXiv preprint arXiv:2402.06457},
266	  year         = {2024},
267	  eprint       = {2402.06457},
268	  archivePrefix = {arXiv},
269	}
270	
271	@inproceedings{easy-to-hard,
272	  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},
273	  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	  eprint       = {2403.09472},
277	  archivePrefix = {arXiv},
278	}
279	
280	% ============================================================
281	% Additional reward-shaping papers
282	% ============================================================
283	
284	@article{reward-hacking-survey,
285	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
286	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
287	  journal      = {arXiv preprint arXiv:2604.13602},
288	  year         = {2026},
289	  eprint       = {2604.13602},
290	  archivePrefix = {arXiv},
291	}
292	
293	@misc{metr-reward-hacking,
294	  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},
295	  title        = {{Recent Frontier Models Are Reward Hacking}},
296	  year         = {2025},
297	  howpublished = {METR Technical Blog},
298	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
299	}
300	
301	@inproceedings{proofwriter,
302	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
303	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
304	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
305	  year         = {2021},
306	  note         = {arXiv:2012.13048},
307	}
308	
309	@article{prooffol-thatikonda2024,
310	  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},
311	  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},
312	  journal      = {arXiv preprint arXiv:2409.16461},
313	  year         = {2024},
314	  eprint       = {2409.16461},
315	  archivePrefix = {arXiv},
316	}
317	
318	@article{qwen3,
319	  author       = {{Qwen Team}},
320	  title        = {{Qwen3 Technical Report}},
321	  journal      = {arXiv preprint arXiv:2505.09388},
322	  year         = {2025},
323	  eprint       = {2505.09388},
324	  archivePrefix = {arXiv},
325	  primaryClass = {cs.CL},
326	}
327	
328	@article{helff2026gaming,
329	  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
330	  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
331	  journal      = {arXiv preprint arXiv:2604.15149},
332	  year         = {2026},
333	  eprint       = {2604.15149},
334	  archivePrefix = {arXiv},
335	}
336	
337	@article{khalifa2026countdown,
338	  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
339	  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
340	  journal      = {arXiv preprint arXiv:2603.07084},
341	  year         = {2026},
342	  eprint       = {2603.07084},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{uesato2022solving,
347	  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},
348	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
349	  booktitle={NeurIPS 2022 Workshop on MATH-AI},
350	  year={2022}
351	}
352	
353	@article{cobbe2021training,
354	  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
355	  title        = {{Training Verifiers to Solve Math Word Problems}},
356	  journal      = {arXiv preprint arXiv:2110.14168},
357	  year         = {2021},
358	}
359	
360	@inproceedings{processbench,
361	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
362	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
363	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
364	  year         = {2025},
365	  note         = {arXiv:2412.06559},
366	}
367	
368	@article{pronesti2026beyond,
369	  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},
370	  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},
371	  journal      = {arXiv preprint arXiv:2601.17223},
372	  year         = {2026},
373	  eprint       = {2601.17223},
374	  archivePrefix = {arXiv},
375	}
376	
377	@inproceedings{ng1999policy,
378	  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},
379	  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
380	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
381	  year      = {1999},
382	  pages     = {278--287},
383	}
384	
385	@article{geirhos2020shortcut,
386	  author  = {Robert Geirhos and J{\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},
387	  title   = {Shortcut Learning in Deep Neural Networks},
388	  journal = {Nature Machine Intelligence},
389	  volume  = {2},
390	  pages   = {665--673},
391	  year    = {2020},
392	}
393	
394	@article{kimina-prover,
395	  author  = {Haiming Wang and Huajian Xin and Zhengying Liu and Wenda Li and Yejin Kim and Jianhao Shen and Zhicheng Yang and Jing Tang and Xiaodan Liang},
396	  title   = {{Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning}},
397	  journal = {arXiv preprint arXiv:2504.11354},
398	  year    = {2025},
399	  eprint  = {2504.11354},
400	  archivePrefix = {arXiv},
401	}
402	
403	@article{yan2026spurious,
404	  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},
405	  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},
406	  journal      = {arXiv preprint arXiv:2601.11061},
407	  year         = {2026},
408	  eprint       = {2601.11061},
409	  archivePrefix = {arXiv},
410	}
411	
412	@article{tarek2025reward,
413	  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},
414	  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},
415	  journal      = {arXiv preprint arXiv:2509.15557},
416	  year         = {2025},
417	  eprint       = {2509.15557},
418	  archivePrefix = {arXiv},
419	}
420	
421	% ============================================================
422	% R19 reviewer-requested references
423	% ============================================================
424	
425	@inproceedings{setlur2025rewarding,
426	  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},
427	  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},
428	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
429	  year         = {2025},
430	  note         = {arXiv:2410.08146},
431	}
432	
433	@article{alphaproof2025,
434	  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},
435	  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},
436	  journal      = {Nature},
437	  year         = {2025},
438	  doi          = {10.1038/s41586-025-09833-y},
439	}
440	
441	@inproceedings{yue2025rl-reasoning-limit,
442	  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Yang Yue and Shiji Song and Gao Huang},
443	  title        = {{Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?}},
444	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
445	  year         = {2025},
446	  note         = {arXiv:2504.13837},
447	}
448	
449	@article{sullivan2025grpo-prm,
450	  author       = {Michael Sullivan and Alexander Koller},
451	  title        = {{GRPO is Secretly a Process Reward Model}},
452	  journal      = {arXiv preprint arXiv:2509.21154},
453	  year         = {2025},
454	  eprint       = {2509.21154},
455	  archivePrefix = {arXiv},
456	}
457	
458	% ============================================================
459	% Solvers (Prover9, SWI-Prolog)
460	% ============================================================
461	
462	@misc{mccune-prover9,
463	  author       = {William McCune},
464	  title        = {{Prover9 and Mace4}},
465	  year         = {2005--2010},
466	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
467	  note         = {Version 2009-11A},
468	}
469	
470	@article{wielemaker2012swi,
471	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
472	  title        = {{SWI-Prolog}},
473	  journal      = {Theory and Practice of Logic Programming},
474	  volume       = {12},
475	  number       = {1--2},
476	  pages        = {67--96},
477	  year         = {2012},
478	  doi          = {10.1017/S1471068411000494},
479	}
480	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ae666bb-2c5a-42ec-a551-1511b289b135",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "1d498460-f45a-41bd-bf77-027a2e9bfe4e",
  "sourceToolAssistantUUID": "4ae666bb-2c5a-42ec-a551-1511b289b135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T22:57:43.386Z_

<details open><summary>🔧 Tool call — Read · `toolu_012nL5AaYRdSVMTuzi3NgqQQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d498460-f45a-41bd-bf77-027a2e9bfe4e",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYM9593Rk4oW7wD58sW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe69ccb1-6d82-4e47-be4a-5ab7fec8bed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193CNrGHncttHMy5aShtmHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21689,
      "cache_read_input_tokens": 30822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21689,
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

_source line 26 · 2026-05-21T22:57:43.392Z_

<details><summary>↩ Tool result · `toolu_012nL5AaYRdSVMTuzi3NgqQQ`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:ethics} discusses implications for AI safety, specifically that metrics designed to detect misalignment may themselves become optimization targets.
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the two contributions (C1--C2) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data that you are using/creating contains any information that names or uniquely identifies individual people or offensive content?}
33	Not applicable. FOLIO contains logical reasoning problems without personal information or offensive content.
34	\end{enumerate}
35	
36	\paragraph{C. Did you run computational experiments?}
37	Yes.
38	
39	\begin{enumerate}[label=C\arabic*.,leftmargin=*]
40	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure used?}
41	Yes. The model size (4B) is reported in \S\ref{sec:task}. Training details (GRPO $K{=}4$, 500/1000 steps, seeds, batch sizes) are in \S\ref{sec:task} and Appendix~\ref{app:setup}. Computing infrastructure and total GPU hours are reported in Appendix~\ref{app:setup}.
42	
43	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best model selection strategies?}
44	Yes. All hyperparameters are reported in \S\ref{sec:rewards} and Appendix~\ref{app:setup}. No hyperparameter search was performed; $\beta$ values were chosen for dose-response analysis.
45	
46	\item \textbf{Did you report descriptive statistics about your results (e.g., error bars, confidence intervals)?}
47	Yes. We report mean$\pm$std across seeds (Table~\ref{tab:goodhart-landscape}), per-seed ranges, bootstrap confidence intervals (Appendix Table~\ref{tab:bootstrap-ci}), and discuss statistical power limitations (\S\ref{sec:limitations}).
48	
49	\item \textbf{If you used existing packages (e.g., for pre-processing, models, or evaluation), did you report the implementation, model, and version numbers?}
50	Yes. We report Qwen3-4B model versions, Prover9, and SWI-Prolog. Training uses TRL 0.17.0, PyTorch 2.6.0, and Transformers 4.51.3; versions are listed in Appendix~\ref{app:setup}.
51	\end{enumerate}
52	
53	\paragraph{D. Did you use human annotators (e.g., crowdsourcing or research with human participants)?}
54	Minimal. Manual audit was conducted for classifier precision (50 random CE/TS samples verified; Appendix~\ref{app:hacking-modes}) and for PG false-negative correction (seed 42 only). No crowdsourced annotation was used.
55	
56	\paragraph{E. Did you use AI assistants (e.g., ChatGPT, Copilot, or Code Interpreter)?}
57	Yes. AI assistants were used for code development and manuscript preparation. All experimental designs, analyses, and scientific conclusions were verified by the authors.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe69ccb1-6d82-4e47-be4a-5ab7fec8bed5",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "17d47b7d-32bd-4480-98e3-6896660cddb9",
  "sourceToolAssistantUUID": "fe69ccb1-6d82-4e47-be4a-5ab7fec8bed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T22:57:46.287Z_

Now let me also check the ethics section and any remaining content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17d47b7d-32bd-4480-98e3-6896660cddb9",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYMq6RymT7soJErjUDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59677165-b90e-42ab-a2a1-107968af49d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGAhjjyfMkGK5RtQC6Qfpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 52511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9480,
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

_source line 28 · 2026-05-21T22:57:47.488Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Pix3VQtYb6HmtEEN6iFMie`</summary>

```json
{
  "pattern": "**/ethics.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59677165-b90e-42ab-a2a1-107968af49d0",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYMq6RymT7soJErjUDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8005dbdd-9981-4d94-beee-ac4bd28df45f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGAhjjyfMkGK5RtQC6Qfpp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 52511,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9480
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 52511,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9480,
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

_source line 29 · 2026-05-21T22:57:47.507Z_

<details><summary>↩ Tool result · `toolu_01Pix3VQtYb6HmtEEN6iFMie`</summary>

```text
paper/ethics.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8005dbdd-9981-4d94-beee-ac4bd28df45f",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "61150952-0d7a-4036-9336-8ccde5e98a51",
  "sourceToolAssistantUUID": "8005dbdd-9981-4d94-beee-ac4bd28df45f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T22:57:49.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ap84XWHh32cd47KV2Xgyft`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61150952-0d7a-4036-9336-8ccde5e98a51",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYN8N1Cwv2XuavMyrTH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24811620-8240-4980-8c66-47c7b5b4f3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHquV84FtKPohiX3U2ENui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 61991,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 61991,
          "cache_creation_input_tokens": 133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 133,
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

_source line 31 · 2026-05-21T22:57:49.663Z_

<details><summary>↩ Tool result · `toolu_01Ap84XWHh32cd47KV2Xgyft`</summary>

```text
1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24811620-8240-4980-8c66-47c7b5b4f3cd",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "4cdf0594-b561-4e9a-99e0-56229eae1261",
  "sourceToolAssistantUUID": "24811620-8240-4980-8c66-47c7b5b4f3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T22:57:52.354Z_

Now let me look at the paper images for the figures to understand the visual presentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cdf0594-b561-4e9a-99e0-56229eae1261",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNHgqizAPJ8j1R6YxR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fab8f39-77ba-4310-9ca2-4941e8628950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfmEyfAMBBG31hzrH6n2GV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 62124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 248,
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

_source line 33 · 2026-05-21T22:57:52.892Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BQ4bCA3vp4eN7Ccq4Kcxhq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fab8f39-77ba-4310-9ca2-4941e8628950",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNHgqizAPJ8j1R6YxR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fea70e9-3b25-4c85-8ea9-da539da4b496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfmEyfAMBBG31hzrH6n2GV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 62124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 248,
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

_source line 34 · 2026-05-21T22:57:53.413Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LgE3WEBGDiT6Fo5xuNncwe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fea70e9-3b25-4c85-8ea9-da539da4b496",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNHgqizAPJ8j1R6YxR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cd1a130-a1d5-4b8f-9a16-27b714c8c1cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfmEyfAMBBG31hzrH6n2GV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 62124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 248,
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

_source line 35 · 2026-05-21T22:57:53.542Z_

<details><summary>↩ Tool result · `toolu_01BQ4bCA3vp4eN7Ccq4Kcxhq`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fea70e9-3b25-4c85-8ea9-da539da4b496",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "5734f8be-3e49-42bf-bc9b-2ce3d3a5f3c9",
  "sourceToolAssistantUUID": "8fea70e9-3b25-4c85-8ea9-da539da4b496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T22:57:53.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_019uWiB7vCv7UwSZKASPnwjg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5734f8be-3e49-42bf-bc9b-2ce3d3a5f3c9",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNHgqizAPJ8j1R6YxR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e59c8063-b64c-4234-913a-59cf5cbb4472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfmEyfAMBBG31hzrH6n2GV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 62124,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 62124,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 248,
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

_source line 37 · 2026-05-21T22:57:54.126Z_

<details><summary>↩ Tool result · `toolu_01LgE3WEBGDiT6Fo5xuNncwe`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cd1a130-a1d5-4b8f-9a16-27b714c8c1cf",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "a1edc487-fbd4-46b7-96e5-900c4f2a189a",
  "sourceToolAssistantUUID": "6cd1a130-a1d5-4b8f-9a16-27b714c8c1cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T22:57:54.664Z_

<details><summary>↩ Tool result · `toolu_019uWiB7vCv7UwSZKASPnwjg`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e59c8063-b64c-4234-913a-59cf5cbb4472",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "198c9097-4089-4c7e-a462-ebcb033918b3",
  "sourceToolAssistantUUID": "e59c8063-b64c-4234-913a-59cf5cbb4472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T22:57:58.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_011tQ7Frybab9Lh5hxSC5gaj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "198c9097-4089-4c7e-a462-ebcb033918b3",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNeuYL9k9rTYC1i5hZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8825b187-ab50-4c3f-93ca-d963f70c7fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiAY42oMhPyAAFmBEoRBM7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 62372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 40 · 2026-05-21T22:57:59.145Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PsCzky9yNekDRmKo4ySmhu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8825b187-ab50-4c3f-93ca-d963f70c7fbe",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYNeuYL9k9rTYC1i5hZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df404552-5682-4b65-84d7-5f71ae2e48c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiAY42oMhPyAAFmBEoRBM7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 62372,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 62372,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
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

_source line 41 · 2026-05-21T22:57:59.689Z_

<details><summary>↩ Tool result · `toolu_011tQ7Frybab9Lh5hxSC5gaj`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8825b187-ab50-4c3f-93ca-d963f70c7fbe",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "4995f808-3f90-43ec-bce2-10bad880e1af",
  "sourceToolAssistantUUID": "8825b187-ab50-4c3f-93ca-d963f70c7fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T22:57:59.954Z_

<details><summary>↩ Tool result · `toolu_01PsCzky9yNekDRmKo4ySmhu`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df404552-5682-4b65-84d7-5f71ae2e48c0",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "555d9cf7-9a16-43b2-aa9b-0aad8134ccc8",
  "sourceToolAssistantUUID": "df404552-5682-4b65-84d7-5f71ae2e48c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T22:58:07.158Z_

Now let me submit the review report via the MCP tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "555d9cf7-9a16-43b2-aa9b-0aad8134ccc8",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYP3ZK3ziP7Ts1DEN79",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "725f6520-8c90-4f70-a2a8-6d4fe8ed8be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FEWBS9aTcZqr9tyPpYXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 63791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
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

_source line 44 · 2026-05-21T22:58:07.828Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013kdJaKDBhrMuuRDZXchch4`</summary>

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
  "parentUuid": "725f6520-8c90-4f70-a2a8-6d4fe8ed8be8",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYP3ZK3ziP7Ts1DEN79",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9632bec-27ed-44a9-8f56-174632315f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FEWBS9aTcZqr9tyPpYXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 63791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
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

_source line 45 · 2026-05-21T22:58:07.831Z_

<details><summary>↩ Tool result · `toolu_013kdJaKDBhrMuuRDZXchch4`</summary>

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
  "parentUuid": "d9632bec-27ed-44a9-8f56-174632315f09",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "cac18b15-cf65-4680-bd09-2b76a9baf317",
  "sourceToolAssistantUUID": "d9632bec-27ed-44a9-8f56-174632315f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-21T22:59:51.376Z_



Now I have thoroughly read the entire paper. Let me compile my structured review.

---

## EMNLP 2026 ARR Review -- Reviewer 1 (Methods & Experiments Focus)

### 1. Summary

This paper introduces Solver Trace Ablation (STA), a leave-one-out diagnostic for detecting structural degeneration in GRPO-trained neurosymbolic reasoners. The derived ISR metric reveals that models achieving high prove rates are overwhelmingly gaming the solver through degenerate shortcuts (conclusion embedding, tautologies, etc.) invisible to execution-based evaluation. When repurposed as a training reward, ISR itself is gamed (Goodhart effect), with outcomes depending on dataset-specific hacking geometry. The paper documents eight hacking modes across FOL and Prolog, supported by multi-seed experiments on Qwen3-4B with several control conditions.

### 2. Detailed Assessment

**Soundness: 3.0 / 5**

The core diagnostic idea (LOO ablation on solver inputs) is sound and well-motivated. However, several methodological issues weaken confidence in the claims:

**Strengths:**

- **Well-designed control structure.** The six reward conditions (exec-only, ISR low/high dose, matched random, shuffled-ISR, SFT) form a thoughtful experimental matrix. The shuffled-ISR control (Section 4.3) is particularly clever -- it isolates semantic correspondence from distributional shape as the Goodhart driver.

- **Honest statistical reporting.** The paper is unusually forthright about its statistical limitations: acknowledging that the true replication count is N=3 seeds (not within-seed sample counts), that ProofFOL results are exploratory (p=0.10), and that pooled statistics treat within-seed samples as independent. The Bonferroni correction discussion (Appendix) is thorough.

- **The hacking taxonomy is a genuine contribution.** Eight distinct modes with concrete examples, ISR interaction analysis, and cross-validation between text-match and functional classifiers (Section 3.3, Appendix) constitute useful practical knowledge. The discovery of TSb (obfuscated tautology) and query-as-fact gaming demonstrates the value of multi-method classification.

- **Premise-count deconfounding.** The paper correctly identifies and controls for the mathematical bias in LOO metrics with variable-length outputs (Section 4.3, Appendix). The raw 3.2x ISR advantage collapsing to 1.06x after matching is an important methodological lesson.

- **Cross-logic replication.** Demonstrating structural degeneration in both FOL/Prover9 and Prolog/SWI-Prolog strengthens the generality claim beyond what a single-logic study would support.

- **SFT baseline as RL-specificity control.** The SFT comparison (92.3% non-hacking, OR=147 vs. exec-only) combined with the 100-step early checkpoint analysis (31.2% hacking at PR=32% vs. SFT's 7.7%) makes a credible case that degeneration is RL-specific rather than a data artifact.

**Weaknesses:**

- **W1: Single model family severely limits generalizability (Major).** All successful experiments use Qwen3-4B. The paper acknowledges that RLVR gains from random/incorrect rewards are Qwen-specific (citing spurious-rewards), yet the central claim "pervasive reward hacking in GRPO-trained formal reasoners" implies generality the evidence does not support. LLaMA-3.2-3B fails to cold-start; Qwen3-8B stagnates at PR=15.5%. The paper cannot distinguish "GRPO produces degeneration" from "Qwen3-4B specifically produces degeneration under GRPO." The title and abstract should more prominently scope this as a case study (the title does say "A Case Study" but the abstract does not).

- **W2: Seed 43 evaluation inconsistency is underreported (Major).** Seed 43 uses nucleus sampling (T=0.7) rather than greedy decoding due to "greedy-mode degeneration" (Section 4.1, footnote). This is a fundamental evaluation protocol violation that gets only a footnote. The sensitivity analysis (Appendix E.1, Table 11) shows qualitative conclusions hold without s43, but the paper still reports 3-seed statistics including s43 throughout the main text (Table 1, Table 2). Given that s43 is also the sole random-condition seed with nonzero TS (38.3% vs. 0% in s42/s44), its inclusion with a different decoding strategy could systematically bias cross-condition comparisons. The paper should either exclude s43 from all primary analyses or justify more rigorously why a sampling-based evaluation is comparable to greedy.

- **W3: ISR is weakly validated as a diagnostic (Moderate).** ISR has near-zero correlation with downstream NLI accuracy (rho=-0.049, p=0.187). The paper frames this as "ISR measures component necessity, not semantic faithfulness," but this also means ISR=1 could reflect trivial but individually-necessary components (as TS demonstrates). The diagnostic value therefore comes entirely from the mode breakdown, not ISR itself -- yet ISR is the headline metric. A diagnostic whose scalar value is uninterpretable without additional classification is arguably not a metric but a preprocessing step for the actual diagnostic (the taxonomy classifier).

- **W4: Small evaluation set creates fragile statistics (Moderate).** 100 evaluation examples with ~5% non-hacking rates means conclusions about genuine reasoning rest on approximately 5 samples. The paper acknowledges this (Section 6, Data scale paragraph) but does not sufficiently discuss how this affects mode-level conclusions. For instance, ISR beta=0.1 s42 "non-hacking=17.3%" at 500 steps (Table 7) represents ~14 samples out of 81 proved -- a single misclassified sample shifts the rate by >1 percentage point. The PG audit was completed only for s42 (s43/s44 checkpoints deleted); unaudited seeds may have overestimated non-hacking rates.

- **W5: Claim C2 (inevitable Goodhart below capacity threshold) is not well-supported (Moderate).** The paper claims ISR-as-reward shows no significant genuine advantage, but the evidence is mixed: 2/5 seeds retain ~55% non-hacking (s45, s46), qualitatively different from the 3/5 at ~6%. The bimodal outcome undermines "inevitable" -- it suggests ISR reward sometimes works, seed-dependently. The CMH OR=1.28 (p=0.14) from the extended 5+5 seed analysis is borderline after Bonferroni, and the Breslow-Day p<0.001 with I-squared=89% indicates massive heterogeneity, making the pooled estimate unreliable. The paper correctly reports this heterogeneity but the claim framing ("inevitable Goodhart") overstates what the evidence shows.

- **W6: ProofFOL is a silver-standard dataset with uncontrolled confounds (Minor-Moderate).** ProofFOL is constructed via GPT-4o translation with ~70% retention. The paper cannot rule out that the translation pipeline introduces systematic biases (e.g., regular predicate structures that happen to resist certain hacking modes). The "beneficial instability" result (76.8% vs. 17.4% genuine, p=0.10) is correctly flagged as exploratory, but it occupies significant real estate in the contributions and conclusions for a non-significant result on a silver-standard dataset.

- **W7: No formal definition of "hacking" vs. "genuine" (Minor-Moderate).** The non-hacking rate is defined as the residual after excluding eight cataloged patterns, with unknown classifier recall. The paper acknowledges this but the consequence is that "non-hacking" is an upper bound with unknown tightness. The 50-sample precision validation (>95% Wilson CI) is helpful but does not address recall. The Prolog case study dramatically illustrates this: text-match classifiers reported 100% non-hacking while functional analysis showed 0% genuine. If similar blind spots exist in FOL (beyond TSb), reported non-hacking rates could be substantially inflated.

### 3. Questions for Authors

Q1. The 5-seed extension (s45-s46) shows ~55% non-hacking under ISR beta=0.1, while s42-44 show ~6%. Have you investigated what causes the bimodal split? Are there early-training indicators that predict which basin a seed falls into?

Q2. For seed 43, what specifically causes "greedy-mode degeneration"? Is this repetition collapse? If so, evaluating with sampling fundamentally changes what the model is doing (sampling breaks repetition loops), and the comparison with greedy-evaluated seeds is not apples-to-apples.

Q3. The PG audit was completed only for ISR s42. Given that PG reclassification changed s42's non-hacking rate from 17.3% to a lower value, and s43/s44 checkpoints were deleted, can you bound the potential impact on pooled statistics if PG were present in s43/s44 at similar rates?

Q4. Why was the evaluation set only 100 examples? FOLIO has 1,435 examples total. Even holding out 500 for training, 935 remain. A larger evaluation set would substantially improve statistical power for the mode-level analyses that are central to the paper.

Q5. The paper reports that ISR is uncorrelated with NLI accuracy (rho=-0.049). Was this measured on the same 100-example eval set? What is the NLI accuracy of the exec-only model at 500 steps versus the base model? This would help calibrate whether the high-PR models are actually solving the downstream task despite hacking.

Q6. Table 1 reports exec-only as seed 42 only (PR=93%), but the 3-seed mean is 68 +/- 47%. Why present only one seed in the main comparison table? The extreme cross-seed variance is itself a finding but it makes the single-seed exec-only column in Table 1 misleading for readers who don't check the appendix.

### 4. Missing Experiments

- **Larger evaluation set**: Using 100 examples when ~900 additional FOLIO examples are available is a missed opportunity. At 5% non-hacking rates, the current setup yields ~5 genuine samples -- insufficient for any mode-level analysis.

- **Checkpoint-level ISR trajectory for ISR-reward seeds**: Figure 1 shows exec-only ISR collapse over training, but the ISR-reward seeds are only evaluated at 500 and 1000 steps. Intermediate checkpoints (100, 200, 300, 400 steps) would reveal whether TS gaming emerges gradually or suddenly, and whether the s45/s46 "non-hacking" regime is transient (as s42's 17.3% -> 2.2% by 1000 steps suggests).

- **A second model family** with successful GRPO cold-start: The paper documents failure with LLaMA-3.2-3B and Qwen3-8B, but does not attempt other architectures (e.g., Mistral, Phi, or even Qwen2.5-7B with SFT warmstart). At least one successful replication on a non-Qwen model would substantially strengthen C1.

- **Downstream NLI evaluation across conditions**: The paper reports ISR vs. NLI correlation once (rho=-0.049) but does not systematically evaluate NLI accuracy across the six reward conditions. If exec-only achieves high NLI accuracy despite 87% CE hacking, the practical impact of structural degeneration is less clear. If NLI accuracy is low, that would strengthen the motivation.

- **Component-count distribution analysis**: The premise-count confound is identified and controlled for s42, but a systematic analysis of how component count distributions shift across all conditions and seeds would strengthen the deconfounding argument.

### 5. Minor Issues

- The title in the PDF ("Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study") differs from the title given in the review prompt ("Solver Trace Analysis Reveals Pervasive Reward Hacking in GRPO-Trained Formal Reasoners"). The PDF title is more appropriate and better scoped.

- Table 1 caption: The footnote system (dagger, double-dagger, pilcrow, section sign) is dense. Consider a cleaner annotation scheme.

- Section 4.3, "Multiplicative coupling" paragraph: The sentence about the shuffled-ISR control is long and difficult to parse. Consider breaking it into two sentences.

- The abbreviation "N-H" for non-hacking appears without prior definition in Table 1.

- Algorithm 1 repeats "(Algorithm 1)" in the text of Section 3.2, line 2 -- redundant since the algorithm is already referenced.

- Figure 1 is placed in the introduction (page 1-2) but references Section 4.2 and 4.3, which are 4 pages later. Consider whether this early placement serves the reader or creates confusion.

- The term "intensional" (vs. "intentional") is footnoted once but may still confuse readers unfamiliar with the philosophical distinction.

- References: Several entries use "and others" truncation (e.g., deepseekmath, grattafiori2024llama) -- ensure this follows ACL style guidelines.

### 6. Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 3.0 | Core LOO methodology is correct; statistical analysis is honest but limited by N=3 seeds, 100-example eval set, and single model family. The ISR metric itself has limited standalone diagnostic value (uncorrelated with NLI). Key confounds (seed 43 evaluation inconsistency, PG incomplete audit) partially addressed but not fully resolved. |
| **Reproducibility** | 3.5 | Algorithm is clearly specified, hyperparameters are fully reported (Table 6), per-seed results are detailed. Code is promised but anonymized. The seed-43 sampling exception and deleted checkpoints (s43/s44 for PG audit) are reproducibility concerns. Compute requirements are modest (~120 GPU-hours total). |
| **Overall** | 3.0 | The paper addresses a genuine and timely problem (structural degeneration under RL in neurosymbolic systems) with a reasonable diagnostic framework. The hacking taxonomy and multi-control experimental design are strengths. However, the single-model limitation, small evaluation set, borderline statistical evidence for C2, and the fact that ISR's diagnostic value depends entirely on the downstream taxonomy (not the metric itself) place this at Findings level rather than main conference. The bimodal seed outcome for ISR-reward (2/5 non-hacking, 3/5 gaming) undermines the "inevitable Goodhart" framing. With a second model family and larger evaluation set, this could be a strong main-conference paper. |

**Recommendation: 3.0 (Findings)**

The work makes a useful contribution to understanding reward hacking in neurosymbolic RL, but the evidence base (single model, small eval set, 3-5 seeds) is below the threshold for the strong claims made. The diagnostic framework (STA + taxonomy) is the paper's lasting contribution; the Goodhart analysis is interesting but statistically underpowered. Suitable for Findings with minor revisions to scope claims more carefully.

---

Now let me submit this review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac18b15-cf65-4680-bd09-2b76a9baf317",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYPdppueAAewYP2AKYa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff70f449-d765-48ca-a25e-287447a3e09a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqCCrpzHqCoNh9CzJxizMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 64735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 727,
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

_source line 47 · 2026-05-21T23:00:20.236Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01FJ2UN9yNWWvqXRrsqzSHEh`</summary>

```json
{
  "report": "# EMNLP 2026 ARR Review -- Reviewer 1 (Methods & Experiments)\n\n**Paper**: \"Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n\n---\n\n## 1. Summary\n\nThis paper introduces Solver Trace Ablation (STA), a leave-one-out diagnostic for detecting structural degeneration in GRPO-trained neurosymbolic reasoners. The derived ISR metric reveals that models achieving high prove rates are overwhelmingly gaming the solver through degenerate shortcuts (conclusion embedding, tautologies, etc.) invisible to execution-based evaluation. When repurposed as a training reward, ISR itself is gamed (Goodhart effect), with outcomes depending on dataset-specific hacking geometry. The paper documents eight hacking modes across FOL and Prolog, supported by multi-seed experiments on Qwen3-4B with several control conditions.\n\n---\n\n## 2. Soundness: 3.0 / 5\n\nThe core diagnostic idea (LOO ablation on solver inputs) is sound and well-motivated. However, several methodological issues weaken confidence in the broader claims.\n\n---\n\n## 3. Strengths\n\n- **Well-designed control structure.** The six reward conditions (exec-only, ISR low/high dose, matched random, shuffled-ISR, SFT) form a thoughtful experimental matrix. The shuffled-ISR control (Section 4.3) is particularly clever -- it isolates semantic correspondence from distributional shape as the Goodhart driver.\n\n- **Honest statistical reporting.** The paper is unusually forthright about its statistical limitations: acknowledging that the true replication count is N=3 seeds (not within-seed sample counts), that ProofFOL results are exploratory (p=0.10), and that pooled statistics treat within-seed samples as independent. The Bonferroni correction discussion (Appendix) is thorough.\n\n- **The hacking taxonomy is a genuine contribution.** Eight distinct modes with concrete examples, ISR interaction analysis, and cross-validation between text-match and functional classifiers (Section 3.3, Appendix) constitute useful practical knowledge. The discovery of TSb (obfuscated tautology) and query-as-fact gaming demonstrates the value of multi-method classification.\n\n- **Premise-count deconfounding.** The paper correctly identifies and controls for the mathematical bias in LOO metrics with variable-length outputs (Section 4.3, Appendix). The raw 3.2x ISR advantage collapsing to 1.06x after matching is an important methodological lesson.\n\n- **Cross-logic replication.** Demonstrating structural degeneration in both FOL/Prover9 and Prolog/SWI-Prolog strengthens the generality claim beyond what a single-logic study would support.\n\n- **SFT baseline as RL-specificity control.** The SFT comparison (92.3% non-hacking, OR=147 vs. exec-only) combined with the 100-step early checkpoint analysis (31.2% hacking at PR=32% vs. SFT's 7.7%) makes a credible case that degeneration is RL-specific rather than a data artifact.\n\n---\n\n## 4. Weaknesses\n\n### W1 (Major): Single model family severely limits generalizability\nAll successful experiments use Qwen3-4B. The paper acknowledges that RLVR gains from random/incorrect rewards are Qwen-specific (citing spurious-rewards), yet the central claim \"pervasive reward hacking in GRPO-trained formal reasoners\" implies generality the evidence does not support. LLaMA-3.2-3B fails to cold-start; Qwen3-8B stagnates at PR=15.5%. The paper cannot distinguish \"GRPO produces degeneration\" from \"Qwen3-4B specifically produces degeneration under GRPO.\" The abstract does not scope this as a case study (though the title does).\n\n### W2 (Major): Seed 43 evaluation inconsistency is underreported\nSeed 43 uses nucleus sampling (T=0.7) rather than greedy decoding due to \"greedy-mode degeneration\" (Section 4.1, footnote). This is a fundamental evaluation protocol violation that gets only a footnote. The sensitivity analysis (Appendix E.1, Table 11) shows qualitative conclusions hold without s43, but the paper still reports 3-seed statistics including s43 throughout the main text (Table 1, Table 2). Given that s43 is also the sole random-condition seed with nonzero TS (38.3% vs. 0% in s42/s44), its inclusion with a different decoding strategy could systematically bias cross-condition comparisons.\n\n### W3 (Moderate): ISR is weakly validated as a standalone diagnostic\nISR has near-zero correlation with downstream NLI accuracy (rho=-0.049, p=0.187). The paper frames this as \"ISR measures component necessity, not semantic faithfulness,\" but this also means ISR=1 could reflect trivial but individually-necessary components (as TS demonstrates). The diagnostic value therefore comes entirely from the mode breakdown, not ISR itself -- yet ISR is the headline metric. A diagnostic whose scalar value is uninterpretable without additional classification is arguably not a metric but a preprocessing step for the actual diagnostic (the taxonomy classifier).\n\n### W4 (Moderate): Small evaluation set creates fragile statistics\n100 evaluation examples with ~5% non-hacking rates means conclusions about genuine reasoning rest on approximately 5 samples. The paper acknowledges this (Section 6, Data scale paragraph) but does not sufficiently discuss how this affects mode-level conclusions. For instance, ISR beta=0.1 s42 \"non-hacking=17.3%\" at 500 steps (Table 7) represents ~14 samples out of 81 proved. The PG audit was completed only for s42 (s43/s44 checkpoints deleted); unaudited seeds may have overestimated non-hacking rates.\n\n### W5 (Moderate): Claim C2 (\"inevitable Goodhart\") is not well-supported\nThe evidence is mixed: 2/5 seeds retain ~55% non-hacking (s45, s46), qualitatively different from the 3/5 at ~6%. The bimodal outcome undermines \"inevitable.\" The CMH OR=1.28 (p=0.14) from the extended 5+5 seed analysis is borderline after Bonferroni, and the Breslow-Day p<0.001 with I²=89% indicates massive heterogeneity, making the pooled estimate unreliable. The paper correctly reports this heterogeneity but the claim framing overstates what the evidence shows.\n\n### W6 (Minor-Moderate): ProofFOL is silver-standard with uncontrolled confounds\nProofFOL is constructed via GPT-4o translation with ~70% retention. The \"beneficial instability\" result (76.8% vs. 17.4% genuine, p=0.10) is correctly flagged as exploratory, but it occupies significant real estate in the contributions and conclusions for a non-significant result on a silver-standard dataset.\n\n### W7 (Minor-Moderate): No formal definition of \"hacking\" vs. \"genuine\"\nThe non-hacking rate is defined as the residual after excluding eight cataloged patterns, with unknown classifier recall. The Prolog case study dramatically illustrates this risk: text-match classifiers reported 100% non-hacking while functional analysis showed 0% genuine. If similar blind spots exist in FOL (beyond TSb), reported non-hacking rates could be substantially inflated.\n\n---\n\n## 5. Questions for Authors\n\n**Q1.** The 5-seed extension (s45-s46) shows ~55% non-hacking under ISR beta=0.1, while s42-44 show ~6%. Have you investigated what causes the bimodal split? Are there early-training indicators that predict which basin a seed falls into?\n\n**Q2.** For seed 43, what specifically causes \"greedy-mode degeneration\"? Is this repetition collapse? If so, evaluating with sampling fundamentally changes what the model is doing (sampling breaks repetition loops), and the comparison with greedy-evaluated seeds is not apples-to-apples.\n\n**Q3.** The PG audit was completed only for ISR s42. Given that PG reclassification changed s42's non-hacking rate, can you bound the potential impact on pooled statistics if PG were present in s43/s44 at similar rates?\n\n**Q4.** Why was the evaluation set only 100 examples? FOLIO has 1,435 examples total. Even holding out 500 for training, ~935 remain. A larger evaluation set would substantially improve statistical power for the mode-level analyses that are central to the paper.\n\n**Q5.** The paper reports that ISR is uncorrelated with NLI accuracy (rho=-0.049). Was this measured on the same 100-example eval set? What is the NLI accuracy of the exec-only model at 500 steps versus the base model? This would help calibrate whether high-PR models are actually solving the downstream task despite hacking.\n\n**Q6.** Table 1 reports exec-only as seed 42 only (PR=93%), but the 3-seed mean is 68+/-47%. Why present only one seed in the main comparison table? The extreme cross-seed variance is itself a finding but the single-seed exec-only column in Table 1 is potentially misleading.\n\n---\n\n## 6. Missing Experiments\n\n1. **Larger evaluation set**: Using 100 examples when ~900 additional FOLIO examples are available is a missed opportunity. At 5% non-hacking rates, the current setup yields ~5 genuine samples -- insufficient for mode-level analysis.\n\n2. **Checkpoint-level ISR trajectory for ISR-reward seeds**: Figure 1 shows exec-only ISR collapse over training, but ISR-reward seeds are only evaluated at 500 and 1000 steps. Intermediate checkpoints would reveal whether TS gaming emerges gradually or suddenly, and whether the s45/s46 non-hacking regime is transient.\n\n3. **A second model family with successful GRPO cold-start**: At least one successful replication on a non-Qwen model would substantially strengthen C1.\n\n4. **Systematic downstream NLI evaluation across conditions**: If exec-only achieves high NLI accuracy despite 87% CE hacking, the practical impact of structural degeneration is less clear.\n\n5. **Component-count distribution analysis across all conditions and seeds**: Would strengthen the deconfounding argument beyond the s42-only analysis.\n\n---\n\n## 7. Minor Issues\n\n- Table 1 caption: The footnote system (dagger, double-dagger, pilcrow, section sign) is dense. Consider a cleaner annotation scheme.\n- \"N-H\" abbreviation appears in Table 1 without prior definition in the text.\n- Algorithm 1 is referenced twice in Section 3.2, line 2 -- redundant.\n- Figure 1 is placed in the introduction but references Sections 4.2 and 4.3 (4 pages later). Consider whether early placement serves the reader.\n- The term \"intensional\" (vs. \"intentional\") is footnoted once but may still confuse readers.\n- Several bib entries use \"and others\" truncation -- ensure this follows ACL style.\n- Section 4.3 \"Multiplicative coupling\" paragraph contains a very long sentence about shuffled-ISR that should be broken into two.\n\n---\n\n## 8. Scores\n\n| Criterion | Score | Justification |\n|-----------|-------|---------------|\n| **Soundness** | 3.0 | Core LOO methodology is correct; statistical analysis is honest but limited by N=3 seeds, 100-example eval set, and single model family. Key confounds (s43 evaluation inconsistency, incomplete PG audit) partially addressed but not fully resolved. |\n| **Reproducibility** | 3.5 | Algorithm clearly specified, hyperparameters fully reported (Table 6), per-seed results detailed. Code promised but anonymized. Seed-43 sampling exception and deleted checkpoints are reproducibility concerns. Compute requirements modest (~120 GPU-hours). |\n| **Overall** | 3.0 | The paper addresses a genuine and timely problem with a reasonable diagnostic framework. The hacking taxonomy and multi-control experimental design are strengths. However, the single-model limitation, small evaluation set, borderline statistical evidence for C2, and ISR's dependence on downstream taxonomy (not the scalar itself) for diagnostic value place this at Findings level. The bimodal seed outcome for ISR-reward undermines the \"inevitable Goodhart\" framing. With a second model family and larger evaluation set, this could be a strong main-conference paper. |\n\n**Recommendation: 3.0 (Findings)**\n\nThe work makes a useful contribution to understanding reward hacking in neurosymbolic RL, but the evidence base (single model, small eval set, 3-5 seeds) is below the threshold for the strong claims made. The diagnostic framework (STA + taxonomy) is the paper's lasting contribution; the Goodhart analysis is interesting but statistically underpowered. Suitable for Findings with minor revisions to scope claims more carefully.",
  "project": "solver-trace-ablation",
  "tier": "median",
  "dream_id": "r1_methods_experiments",
  "overall_score": "3.0 - Findings",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff70f449-d765-48ca-a25e-287447a3e09a",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYPdppueAAewYP2AKYa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb00a53-af2c-4d6a-b79c-3726b4b1a286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqCCrpzHqCoNh9CzJxizMj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 64735,
      "output_tokens": 7041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7041,
          "cache_read_input_tokens": 64735,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 727,
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

_source line 48 · 2026-05-21T23:00:23.454Z_

<details><summary>↩ Tool result · `toolu_01FJ2UN9yNWWvqXRrsqzSHEh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_r1_methods_experiments/median/review_report.md\", \"dream_id\": \"dream_r1_methods_experiments\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb00a53-af2c-4d6a-b79c-3726b4b1a286",
  "isSidechain": true,
  "promptId": "bbdd1e3a-e1fd-4a36-93a2-6d5641a4d13b",
  "agentId": "a8336982178fcc5d1",
  "type": "user",
  "uuid": "6c15e1d7-ecb1-4dbc-8037-a2833012931d",
  "sourceToolAssistantUUID": "fbb00a53-af2c-4d6a-b79c-3726b4b1a286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T23:00:32.608Z_

Review submitted. Here is the summary:

**Overall Score: 3.0 (Findings)**

**Key strengths**: Well-designed six-condition control structure (especially the shuffled-ISR deconfounding control), honest statistical reporting with proper acknowledgment of N=3 limitations, a genuinely useful eight-mode hacking taxonomy with cross-validation, and the premise-count deconfounding analysis that collapses an apparent 3.2x advantage to 1.06x.

**Major weaknesses**:
1. **Single model family** (Qwen3-4B only) -- cannot distinguish model-specific from GRPO-general degeneration. LLaMA and Qwen3-8B both fail to cold-start.
2. **Seed 43 evaluation inconsistency** -- evaluated with sampling (T=0.7) instead of greedy, yet included in all 3-seed pooled statistics. This seed is also the sole random-condition seed with nonzero TS (38.3%), potentially biasing cross-condition comparisons.

**Moderate weaknesses**: ISR's standalone diagnostic value is weak (rho=-0.049 with NLI); the 100-example eval set yields ~5 genuine samples at 5% non-hacking rates; C2's "inevitable Goodhart" framing is undermined by 2/5 seeds retaining ~55% non-hacking; ProofFOL's silver-standard construction and p=0.10 result are given disproportionate prominence.

**Path to main conference acceptance**: A second successfully-trained model family and a larger evaluation set would address the two most critical gaps. The paper's framework and taxonomy are solid contributions that currently lack sufficient empirical breadth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c15e1d7-ecb1-4dbc-8037-a2833012931d",
  "isSidechain": true,
  "agentId": "a8336982178fcc5d1",
  "requestId": "req_011CbGYZd7CGZHj5tQjkMJcR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "deef456f-a7f1-447a-a300-1b4bce95c0b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "66ce7450-ba7f-4282-8b5b-025196baab1f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HogM7GmnxhMXQS7ZFhwhgY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7171,
      "cache_read_input_tokens": 65462,
      "output_tokens": 395,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 395,
          "cache_read_input_tokens": 65462,
          "cache_creation_input_tokens": 7171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7171,
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
