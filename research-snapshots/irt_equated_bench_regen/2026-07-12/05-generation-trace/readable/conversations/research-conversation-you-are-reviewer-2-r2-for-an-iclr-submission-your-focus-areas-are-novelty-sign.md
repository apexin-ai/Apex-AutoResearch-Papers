# Research conversation: You are Reviewer 2 (R2) for an ICLR submission. Your focus areas are **Novelty/Significance** and **Related Work/Positio

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aea3ad15f794d3072.jsonl`
- **Structured JSON:** [`ece1d3884cf095b87d91.json`](../../sessions/ec/ece1d3884cf095b87d91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

66 recorded events

### User

_source line 1 · 2026-05-21T05:32:15.430Z_

You are Reviewer 2 (R2) for an ICLR submission. Your focus areas are **Novelty/Significance** and **Related Work/Positioning**. Produce a detailed, rigorous review.

## Venue & Scoring
ICLR, 1-10 scale: 10=Strong Accept, 8=Accept, 6=Marginally Above threshold, 5=Marginally Below threshold, 3=Reject, 1=Strong Reject.

## Paper Summary
Title: "Empirical Characterization of Measurement Stability in LLM Benchmarks: Challenges and an Open Framework"

The paper applies Differential Item Functioning (DIF) analysis from psychometrics to METABENCH MMLU (5,227 models × 12,508 items). Key contributions claimed:
1. Largest-scale DIF analysis on an LLM benchmark (5,227 models × 12,508 items).
2. Semi-synthetic validation framework (ΔTPR methodology) with cross-subject matching (ΔFPR=0.000).
3. Finding that ≥18-31% of MMLU items are functionally unstable, but this doesn't threaten ranking validity (ρ≈0.997).
4. Ground-truth meta-critique: web-overlap labels can't validate item-level differential detectors.
5. Comparison against ConStat, DVD, IFTs, ensemble fusion — no single method dominates, ensemble doesn't improve over best single signal.
6. Extensive negative results reported transparently: bifactor IRT equating, item generation, RL robustness, Bayesian DIF, ensemble.
7. Practitioner's guide for applying DIF to LLM benchmarks.

## Paper Structure & Content

**Section 2 (Related Work):**
- Benchmark contamination detection: n-gram overlap (?), Min-K% (?), ConStat (?), generation-variance approaches. All share systematic blind spot: validate against web-overlap labels.
- Differential Item Functioning: originated in educational testing (?), MH procedure (?), SIBTEST (?). Recent IRT-based methods for LLM evaluation (?), but systematic DIF at scale unexplored.
- Benchmark validity and stability: contamination-robust evaluation (?), dynamic benchmarks, psychometric modeling. This work provides item-level stability characterization.
- Item-Focused Trees: ? (uses continuous covariates instead of categorical groups).
- NOTE: All citations appear as "?" in the paper — the bibliography is broken/missing.

**Key findings by section:**
- §4.1: MH flags 31.3%, SIBTEST flags 44.7%, Jaccard overlap only 0.48 — instability range is method-dependent (≥18-31%). Random-split sanity C%=0.18%. Within-family Llama-2 vs Llama-3: 61.3% (likely capability gain not contamination). Architecture stratification trivial (99.98% decoder-only). IRT fit devastating (CFI=0.41, 98% models misfit).
- §4.2: Ground-truth meta-critique — DIF enrichment ≈0.96 against Li et al. labels is *expected*, not failure.
- §4.3: ΔTPR framework — clear dose-response, ΔFPR=0.000 under cross-subject matching. But injection mechanism has HIGH mismatch with real contamination on signal type and response pattern (Table 5 self-acknowledges).
- §4.4: GSM8K replication confirms portability. But DIF-C items are systematically harder (0.38 vs 0.61, p<0.001) — difficulty confound.
- §4.5: ρ≈0.997 ranking redundancy. Circularity ablation z=-9.5 (DIF is least disruptive removal). Critical replacement threshold ∼23% < DIF flag rate 31% — fundamental tension.
- §4.6: ConStat has lower FPR (0.067 vs 0.314) and higher AUROC on non-RL (0.78 vs 0.73). DVD weak on variant contamination. IFT overfits. Ensemble fails (0.76 < 0.78 best single).
- §5.1: Four negative results reported (RL robustness, bifactor, item generation, Bayesian DIF).
- §5.2: Acknowledges IRT misspecification, no ground truth, temporal confounding, scalability.
- §4.7: Practitioner's guide with 7 recommendations.
- §6: Conclusion frames primary contribution as ΔTPR framework, positions paper as characterization + open framework.

## Your Task
Produce a thorough review focused on:
1. **Novelty**: Is applying MH/SIBTEST to LLM benchmarks sufficiently novel for ICLR? Is the ΔTPR framework a genuine methodological contribution? How do the negative results contribute?
2. **Significance/Impact**: Will this work change how the community evaluates LLM benchmarks? Is the characterization actionable?
3. **Related work coverage**: Are the right baselines compared? Are important related works missing? Is the positioning honest?
4. **Framing and claims**: Are the claims well-calibrated to the evidence? Is the paper over-claiming or under-claiming?
5. **Audience fit**: Is this the right venue (ICLR)? Would it be better suited for a psychometrics venue, an evaluation workshop, or a different ML venue?

Your review must include:
- Summary (2-3 sentences)
- Strengths (bulleted list)
- Weaknesses (bulleted list, with severity: major/minor)
- Questions for Authors (numbered list)
- Scores: Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (1-10), Confidence (1-5)
- One paragraph justification of overall score

Be rigorous but fair. Do not mention any tier designation. Evaluate the paper on its own merits.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "68832ddc-b629-4ee0-82a0-6c351c599271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T05:32:15.434Z_

```json
{
  "parentUuid": "68832ddc-b629-4ee0-82a0-6c351c599271",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
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
  "uuid": "c69058a1-4f29-4a25-9f01-3aa1738b703a",
  "timestamp": "2026-05-21T05:32:15.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T05:32:20.188Z_



I need to read the actual paper to provide a rigorous review. Let me start by examining the paper structure and content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69058a1-4f29-4a25-9f01-3aa1738b703a",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAdso3GgfyxBoDEYSrS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2693ad9-1031-43ce-bf4c-609872fe31cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5tHRxjkTnprmC3nwuoxHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7372,
      "cache_read_input_tokens": 8549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7372,
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

_source line 4 · 2026-05-21T05:32:22.634Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DtoMhAwqmwTz7pafz9S3GM`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2693ad9-1031-43ce-bf4c-609872fe31cc",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAdso3GgfyxBoDEYSrS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ddeffe9-fd86-499c-a542-6ede14ab0374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5tHRxjkTnprmC3nwuoxHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7372,
      "cache_read_input_tokens": 8549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7372,
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

_source line 5 · 2026-05-21T05:32:22.656Z_

<details><summary>↩ Tool result · `toolu_01DtoMhAwqmwTz7pafz9S3GM`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T205007/best/paper.tex
artifacts/dream_reports/dream_20260520T205007/median/paper.tex
artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
artifacts/dream_reports/dream_20260521T012912/best/paper.tex
artifacts/dream_reports/dream_20260521T012912/median/paper.tex
artifacts/dream_reports/dream_20260521T012912/worst/paper.tex
artifacts/dream_reports/dream_20260521T032826/best/paper.tex
artifacts/dream_reports/dream_20260521T032826/worst/paper.tex
paper/math_commands.tex
paper/main.tex
artifacts/_project/paper/experiments.tex
docs/paper/introduction.tex
paper/sections/introduction.tex
paper/sections/related_work.tex
artifacts/dream_reports/dream_20260521T042647/best/paper.tex
paper/sections/discussion.tex
artifacts/dream_reports/dream_20260521T042647/median/paper.tex
artifacts/dream_reports/dream_20260521T042647/worst/paper.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
paper/sections/appendix.tex
paper/sections/method.tex
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ddeffe9-fd86-499c-a542-6ede14ab0374",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "541bd853-6aa1-4f2d-a621-4451d01828fb",
  "sourceToolAssistantUUID": "4ddeffe9-fd86-499c-a542-6ede14ab0374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T05:32:22.828Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NY4hXcEwsNT9FaZYMJWo33`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "541bd853-6aa1-4f2d-a621-4451d01828fb",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAdso3GgfyxBoDEYSrS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20af288b-8570-4b62-9fbb-df6da3c5768e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5tHRxjkTnprmC3nwuoxHs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7372,
      "cache_read_input_tokens": 8549,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7372
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 215,
          "cache_read_input_tokens": 8549,
          "cache_creation_input_tokens": 7372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7372,
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

_source line 7 · 2026-05-21T05:32:22.842Z_

<details><summary>↩ Tool result · `toolu_01NY4hXcEwsNT9FaZYMJWo33`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20af288b-8570-4b62-9fbb-df6da3c5768e",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "36cdfe43-c416-4e14-ab82-2074544da21b",
  "sourceToolAssistantUUID": "20af288b-8570-4b62-9fbb-df6da3c5768e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:32:26.624Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EBzbe2h2R9w7EevNk5avw8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36cdfe43-c416-4e14-ab82-2074544da21b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAeRZVVkQ3WNWdvYvZY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87db5aac-ad9a-467a-9021-f0d41d7077b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJXCi6b7D3Xd9wsVpx9VS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 15921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 9 · 2026-05-21T05:32:26.634Z_

<details><summary>↩ Tool result · `toolu_01EBzbe2h2R9w7EevNk5avw8`</summary>

```text
1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87db5aac-ad9a-467a-9021-f0d41d7077b2",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "e5e412c0-306b-4576-81d8-f17dde346fa0",
  "sourceToolAssistantUUID": "87db5aac-ad9a-467a-9021-f0d41d7077b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T05:32:27.542Z_

<details open><summary>🔧 Tool call — Read · `toolu_019NkZKaoeXymXT5tXpKyBdM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5e412c0-306b-4576-81d8-f17dde346fa0",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAeRZVVkQ3WNWdvYvZY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd7105e-f68f-449f-9e9c-63cca38ab2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJXCi6b7D3Xd9wsVpx9VS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 15921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 11 · 2026-05-21T05:32:27.549Z_

<details><summary>↩ Tool result · `toolu_019NkZKaoeXymXT5tXpKyBdM`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), and find that 31\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts. This instability does not threaten benchmark validity: Spearman rank correlation between full and stable-item rankings is $\rho \approx 0.997$. Rather, it reveals which capability dimensions shift across model generations. Item-level decomposition shows that domain accuracy improvement explains only 2.4 percentage points (7.6\%) of the instability; 92.4\% is item-specific. We expose a validation methodology gap in the contamination detection literature: web-overlap labels measure global exposure, not differential functioning, and the enrichment between DIF flags and these labels is 0.96 (chance level). A semi-synthetic injection framework with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$); cross-benchmark replication on GSM8K confirms generality ($\Delta\mathrm{TPR} = {+}0.818$). DIF-flagged items concentrate cross-generational discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$, $N = 33$), suggesting that DIF captures genuine capability change rather than memorization. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd7105e-f68f-449f-9e9c-63cca38ab2b5",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "18792d9e-ba57-4a4d-a25f-e505dabb605b",
  "sourceToolAssistantUUID": "bbd7105e-f68f-449f-9e9c-63cca38ab2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T05:32:27.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_0164xjg8oZZhsKbHPoaMMU3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18792d9e-ba57-4a4d-a25f-e505dabb605b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAeRZVVkQ3WNWdvYvZY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b740ddc-3609-4c4d-80fc-3cc709df33f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJXCi6b7D3Xd9wsVpx9VS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 15921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 13 · 2026-05-21T05:32:27.832Z_

<details><summary>↩ Tool result · `toolu_0164xjg8oZZhsKbHPoaMMU3j`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\% ranging from 31\% to 45\% (mean 38.1\%), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena, and the near-chance enrichment (0.96) between DIF flags and web-overlap labels is the expected outcome of this mismatch.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about MMLU's measurement properties.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order. DIF should therefore be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate ranking stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.
18	
19	We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic. Three layers of genuine novelty emerge: (a)~we discover that 31\% temporal instability is robust across thresholds and unrelated to capability improvement, the first large-scale characterization of item-level benchmark stability at 5,227 models; (b)~we expose a fundamental validation methodology gap in the contamination detection literature, showing that web-overlap labels cannot serve as ground truth for item-level differential detectors; and (c)~we provide a reusable semi-synthetic validation framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K with independent contamination validation through the GSM1K held-out set~\citep{zhang2024gsm1k}. We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification, with the instability persisting within every subject domain (mean C\% $= 38.1\%$) and confirmed non-random by random-split control at 0.18\% (\Cref{sec:temporal}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} cannot evaluate item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\Cref{sec:downstream,sec:gsm8k}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b740ddc-3609-4c4d-80fc-3cc709df33f6",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "87afdf90-a268-420c-9c91-07572c259f2b",
  "sourceToolAssistantUUID": "3b740ddc-3609-4c4d-80fc-3cc709df33f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T05:32:32.467Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VNzkVdM37T16wY7mJWdYk7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87afdf90-a268-420c-9c91-07572c259f2b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAenzLipofHW7uPik4Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc9341a5-381f-49ca-beac-dae2f0b71535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzS3s83roZNLNmpvjPPtUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 17434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3293,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 15 · 2026-05-21T05:32:32.473Z_

<details><summary>↩ Tool result · `toolu_01VNzkVdM37T16wY7mJWdYk7`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This distinction is central to our Claim~2 (\Cref{sec:groundtruth}): web-overlap labels cannot serve as ground truth for differential detectors, because most benchmark items are globally exposed to all model cohorts. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, which further motivates behavioral approaches grounded in psychometric theory rather than NLL-based signals.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	Item Response Theory (IRT) provides a principled framework for jointly analyzing test items and examinee ability, and its adoption in LLM evaluation has accelerated. \citet{lalor2019irt} introduced IRT to NLP by fitting item parameters to human and model response data; their analysis revealed that item difficulty and discrimination vary substantially across benchmark questions. \citet{vania2021irt} applied IRT to assess test set discriminability and found that many items in standard NLP benchmarks contribute little information about model differences. Recent extensions include PSN-IRT \citep{zhou2026psnirt}, which fits four-parameter logistic models to characterize benchmark quality at scale, and scalability coefficients \citep{hardy2026scalability} as lightweight item quality pre-filters. TinyBenchmarks \citep{maiapolo2024tinybenchmarks} uses IRT-based item selection to construct representative benchmark subsets that predict full-benchmark scores with far fewer items. ATLAS \citep{li2025atlas} and IRTNet \citep{chen2025irtnet} explore neural extensions of classical IRT for LLM ability estimation, and \citet{choi2026llmjudgeirt} apply IRT to calibrate LLM-as-judge evaluations.
9	
10	The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability across model generations through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. FPC anchors a common ability scale by fixing the item parameters of a shared anchor set, so that models calibrated at different times receive scores on the same metric. Their framework selects 100 anchor items with stable IRT parameters and calibrates new models against this fixed scale, which enables extensible evaluation without full re-calibration. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption. The combination yields a monitored extensible evaluation system: DIF flags anchor items whose functioning has degraded, and the calibration framework triggers re-selection when the stable anchor set shrinks below a validity threshold.
11	
12	\paragraph{DIF Methodology and Measurement Invariance.}
13	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. We do not modify the MH procedure; our contribution is the application context. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
14	
15	\paragraph{Benchmark Design and Concurrent Work.}
16	Our analysis psychometrically characterizes an existing benchmark (MMLU; \citealp{hendrycks2021mmlu}) rather than constructing a new one. Several concurrent efforts address benchmark limitations through design. Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench} and LatestEval \citep{li2024latesteval} generate items adversarially or from recent sources to prevent memorization, and LiveBench \citep{white2025livebench} refreshes items monthly from contemporary material. Chatbot Arena \citep{chiang2024chatbot} and GAIA \citep{mialon2023gaia} sidestep static benchmarks entirely through pairwise human preference or real-world task completion. HELM \citep{liang2023helm} standardizes evaluation across tasks but does not address item-level stability. These approaches mitigate contamination by construction, yet none provides psychometric equating across versions: a model's score on LiveBench v3 is not directly comparable to its score on v1 without an anchoring mechanism such as that of \citet{habba2026growingpains}. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix (5,227 models $\times$ 12,508 items) that makes our analysis possible.
17	
18	\paragraph{LLM Evaluation Methodology.}
19	Broader surveys of LLM evaluation \citep{chang2024survey} identify benchmark saturation and lack of item-level transparency as systemic challenges. \citet{burnell2023rethink} argue that current practices treat benchmarks as monolithic scores, which obscures item-level variation in difficulty, discrimination, and stability. MMLU-Pro \citep{wang2024mmlupro} addresses saturation by increasing item difficulty, and \citet{ott2022benchmark} document how benchmark scores plateau as models improve. These diagnoses converge on a common gap: the absence of tools that operate at the item level rather than the benchmark level. Our DIF analysis fills this role by identifying which items within a benchmark have become unreliable for cross-generation comparison.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc9341a5-381f-49ca-beac-dae2f0b71535",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "81e6f447-b337-4324-9991-a5efb18dc884",
  "sourceToolAssistantUUID": "dc9341a5-381f-49ca-beac-dae2f0b71535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T05:32:32.774Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TNjLJkLVbioGLc7xrG6D2y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e6f447-b337-4324-9991-a5efb18dc884",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAenzLipofHW7uPik4Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee01c0b8-62e6-445e-9a8d-1eae18c3e9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzS3s83roZNLNmpvjPPtUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3293,
      "cache_read_input_tokens": 17434,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 17434,
          "cache_creation_input_tokens": 3293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3293,
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

_source line 17 · 2026-05-21T05:32:32.778Z_

<details><summary>↩ Tool result · `toolu_01TNjLJkLVbioGLc7xrG6D2y`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, a semi-synthetic validation framework, diagnostic checks, and statistical controls.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$), where $K$ equals the number of distinct total scores observed in the combined sample, and computing a common odds ratio across strata. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	DIF requires defining a reference group and a focal group. We construct five cohort comparisons, each designed to isolate a different source of variation.
38	
39	\paragraph{Temporal.} The reference group consists of models released in 2023 ($N = 1{,}080$) and the focal group consists of models released in 2024 ($N = 807$). This is the primary comparison for detecting items whose functioning changed across model generations.
40	
41	\paragraph{Ability-quintile.} Models within the same temporal window are divided by total score into quintiles. The focal group contains the lowest-scoring models (Q1--Q2) and the reference group contains the highest-scoring models (Q4--Q5). This comparison tests whether ability differences alone produce DIF, without temporal confounds.
42	
43	\paragraph{Within-family.} Llama-2 models ($N = 161$) serve as the reference group and Llama-3 models ($N = 308$) as the focal group. This comparison isolates generational changes within a single model family.
44	
45	\paragraph{Within-subject.} DIF is computed separately for each of the 57 MMLU subjects, with the matching variable (total score) restricted to items within the same subject. This design tests whether instability concentrates in specific knowledge domains.
46	
47	\paragraph{Random split.} The 2023 cohort is divided into two equal random halves ($N = 540$ each). This serves as a sanity check: no systematic DIF should appear between two random subsets of the same population (expected C\% $\approx 0$).
48	
49	\subsection{Semi-Synthetic Injection Framework}
50	\label{sec:injection}
51	
52	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
53	
54	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
55	
56	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains, while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
57	
58	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee01c0b8-62e6-445e-9a8d-1eae18c3e9f9",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "08766c67-579f-420f-a18f-83447bbf1953",
  "sourceToolAssistantUUID": "ee01c0b8-62e6-445e-9a8d-1eae18c3e9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T05:32:42.117Z_

<details open><summary>🔧 Tool call — Read · `toolu_0141iG8Zs9615kddtdYtm4ur`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08766c67-579f-420f-a18f-83447bbf1953",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAfA9ZhYK9XxETwEAf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a49fbf16-8eef-4ac3-be33-22135051022c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rVef8Q4MPe5x99F7MX6VW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4446,
      "cache_read_input_tokens": 20727,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 20727,
          "cache_creation_input_tokens": 4446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4446,
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

_source line 19 · 2026-05-21T05:32:42.122Z_

<details><summary>↩ Tool result · `toolu_0141iG8Zs9615kddtdYtm4ur`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark replication on GSM8K appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	Comparing 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models, 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%.
17	
18	Within-subject analysis yields an average of 38.1\% ETS~C items across all five MMLU domains (range: 31--45\%). Despite an ecological correlation of $\rho = 0.307$ ($p = 0.02$) between subject-level C\% and accuracy improvement, item-level logistic regression reveals that domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$; counterfactual C\% $= 29.0\%$). Thus 92.4\% of the instability reflects item-specific changes unrelated to aggregate domain-level gains. The qualitative conclusion is robust across ETS thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, and $10.2\%$ at $\geq 2.5$. \Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\begin{tabular}{lcccc}
26	\toprule
27	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & ETS~C (\%) & FPR (Li clean) & Enrichment \\
28	\midrule
29	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\
30	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
31	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
32	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
33	Within-subject (avg, 5 subjects) & \textit{varies} & 38.1 & -- & -- \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\subsection{Ground Truth Mismatch}
39	\label{sec:groundtruth}
40	
41	The enrichment ratio of DIF flags against the web-overlap labels of \citet{li2024contamination} is 0.96 (\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$, ${+}0.674$ at $p = 1.0$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). An item can be globally contaminated yet function identically if all cohorts have comparable access. The Li et al.\ labels are the wrong ground truth for a differential method: the near-chance enrichment is expected, not evidence of failure.
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
46	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
47	\label{fig:dose_response}
48	\end{figure}
49	
50	\subsection{Structural Analysis}
51	\label{sec:structural}
52	
53	Three progressively refined approaches (matched-ability quintiles, IRT $\theta$-conditioning, within-subject DIF) all fail to reduce the temporal FPR below 0.31. $\theta$-conditioning achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ yet FPR $= 0.312$, and within-subject C\% $= 38.1\%$ exceeds the 25\% bifactor viability threshold. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $p = 2.3 \times 10^{-9}$), but cross-subject matching addresses this bias and temporal C\% persists. \Cref{app:structural} reports full results.
54	
55	\subsection{Semi-Synthetic Framework Validation}
56	\label{sec:semisynthetic}
57	
58	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
59	
60	\subsection{Downstream Impact}
61	\label{sec:downstream}
62	
63	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8$ to $-49$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions (\Cref{app:fig_downstream}). The DIF instability pattern extends beyond MMLU; \Cref{sec:gsm8k} presents a full replication on GSM8K.
64	
65	\subsection{Cross-Benchmark Validation: GSM8K}
66	\label{sec:gsm8k}
67	
68	Replication on GSM8K (1,319 items $\times$ 6,702 models) yields temporal C\% $= 18.9\%$ (sanity check: 0.3\%), with semi-synthetic $\Delta\mathrm{TPR} = {+}0.818$ at $p = 0.7$ (\Cref{app:gsm8k_details}). The GSM1K held-out set~\citep{zhang2024gsm1k} provides independent contamination validation: for $N = 33$ models, the correlation between contamination gap and DIF ranking advantage is $r = -0.478$ ($p = 0.005$; partial $r = -0.385$, $p = 0.027$ after controlling for accuracy). This \emph{negative} correlation contradicts the hypothesis that DIF items benefit contaminated models, and instead suggests that DIF captures genuine capability change distinct from memorization (\Cref{fig:gsm1k}). The result is suggestive at $N = 33$ and warrants replication.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
73	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
74	\label{fig:gsm1k}
75	\end{figure}
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a49fbf16-8eef-4ac3-be33-22135051022c",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "26ce6b0f-80a8-4e51-8357-c5817d28eb9c",
  "sourceToolAssistantUUID": "a49fbf16-8eef-4ac3-be33-22135051022c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T05:32:46.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Voykz7dxZe4nYNVK9bndfD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26ce6b0f-80a8-4e51-8357-c5817d28eb9c",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAfqyxHYCX3P2Nnpx67",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4927521a-cb65-4835-bae6-ecf49f7dd7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ky1L9CdnY8LAj5QyD3qp8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2996,
      "cache_read_input_tokens": 25173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2996,
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

_source line 21 · 2026-05-21T05:32:46.474Z_

<details><summary>↩ Tool result · `toolu_01Voykz7dxZe4nYNVK9bndfD`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability rate is robust across thresholds (10\% at $|\Delta_{\mathrm{MH}}| \geq 2.5$, rising to 49\% at $\geq 1.0$), and three structural controls (\Cref{sec:structural}) confirm it is not a methodological artifact. This means that cross-generation MMLU score comparisons carry uncontrolled item-level variance: nearly one in three items functions differently depending on when the evaluated model was trained. The instability decomposition (\Cref{sec:temporal}) sharpens this interpretation. Domain-level accuracy improvement explains only 2.4 percentage points of the 31.3\% C\% (pseudo $R^2 = 0.0007$), so 92.4\% of the instability is unrelated to aggregate capability gains. The items that change are not simply the ones that newer models answer correctly because they are better at a domain; instead, they change in item-specific ways that domain-level trends do not predict.
8	
9	This instability does not invalidate MMLU as a ranking instrument. Spearman $\rho \approx 0.997$ between full and stable-item rankings confirms that aggregate model ordering is preserved. The instability is diagnostic, not destructive: it identifies which measurement units shift across model generations without rendering the overall score unreliable. Benchmark designers should therefore consider monitoring DIF as a quality diagnostic alongside accuracy metrics. An item pool where C\% grows over successive model cohorts signals that the benchmark's measurement properties are drifting, even if rank ordering remains intact.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	The near-chance enrichment (0.96) between DIF flags and web-overlap labels raises a question that extends beyond our specific analysis. All prior work that validates item-level contamination detectors against web-overlap or $n$-gram labels faces the same methodological gap: these labels measure whether an item exists in publicly accessible training corpora, not whether exposure differentially affects model behavior. Global exposure is a property of the data ecosystem; differential functioning is a property of how model cohorts interact with individual items. Most MMLU items are globally contaminated in the sense that they appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. Validating differential detectors against such labels conflates two distinct phenomena.
15	
16	This observation constitutes a meta-contribution to the contamination detection literature. The enrichment ratio of $\approx 1.0$ is not evidence that DIF fails; it is the expected outcome when a differential method is evaluated against a global-exposure reference. Semi-synthetic injection confirms that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}). The field needs validation methodologies that match the granularity of the detection task: item-level differential detectors require item-level differential ground truth, not item-level global-exposure labels.
17	
18	\subsection{DIF as Diagnostic Lens}
19	\label{sec:disc_diagnostic}
20	
21	\paragraph{Capability diagnostic.} The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps (higher GSM8K minus GSM1K accuracy) benefit \emph{less} from DIF-C items, the opposite of what a pure memorization account would predict. Of the 249 focal-favoring DIF-C items, 171 have discrimination $\alpha < 1$, and the negative correlation concentrates in this low-discrimination subset. This pattern suggests that contamination produces a ``shallow'' performance boost on items that DIF does not flag, while DIF-C items capture genuine capability differences that contamination does not confer. Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for overall accuracy confirms that the effect is not an artifact of general model quality. Several caveats apply: the confidence interval is wide (95\% CI $= [-0.71, -0.16]$), item difficulty as a confound is not fully excluded, and $N = 33$ limits generalizability. This result is suggestive and warrants replication with larger model populations.
22	
23	\paragraph{Structural constraints on DIF applicability.} Systematic experimentation reveals three structural constraints that jointly limit DIF utility in LLM benchmarks. First, 1D IRT model fit is imperfect: MMLU's multi-domain structure produces mild local dependence (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$; \Cref{sec:structural}), which elevates within-subject DIF rates relative to cross-subject baselines. Second, the power analysis (\Cref{sec:validation}) establishes minimum requirements of $N \geq 80$ per cohort and $|\Delta_{\mathrm{MH}}| \geq 1.4$ for reliable detection. Benchmarks with small model populations or modest effect sizes will lack statistical power for DIF analysis. Third, ability differences between temporal cohorts confound the DIF signal: the within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% C\%, elevated above the 31.3\% temporal rate by the large ability gap between model generations. These are structural constraints revealed by our experimentation, not fundamental impossibilities. Higher-level methods (MIMIC models, propensity-score matching, multidimensional IRT) may address individual constraints, and their investigation on LLM benchmark data is a natural next step.
24	
25	\subsection{Limitations}
26	\label{sec:disc_limitations}
27	
28	\paragraph{(a) Ecological vs.\ item-level decomposition.} The ecological correlation between subject-level C\% and accuracy improvement is $\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\%) of 31.3\% C\%. The remaining 92.4\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.
29	
30	\paragraph{(b) Instability attribution.} The 31\% C\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \emph{that} items changed, not \emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.
31	
32	\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.
33	
34	\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.
35	
36	\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\Delta\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.
37	
38	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
39	
40	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
41	
42	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4927521a-cb65-4835-bae6-ecf49f7dd7ce",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "1770ce99-a448-42c9-81a0-c7e3183ad4c8",
  "sourceToolAssistantUUID": "4927521a-cb65-4835-bae6-ecf49f7dd7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T05:32:46.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GRAugdmKVfcX8hDnSgQKUj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1770ce99-a448-42c9-81a0-c7e3183ad4c8",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAfqyxHYCX3P2Nnpx67",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f8331c1-a5ed-44ee-a2fa-176576f2fd7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ky1L9CdnY8LAj5QyD3qp8F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2996,
      "cache_read_input_tokens": 25173,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2996
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 25173,
          "cache_creation_input_tokens": 2996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2996,
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

_source line 23 · 2026-05-21T05:32:46.813Z_

<details><summary>↩ Tool result · `toolu_01GRAugdmKVfcX8hDnSgQKUj`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Applying Mantel-Haenszel DIF analysis to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), we find that 31\% of items are functionally unstable across model generations under ETS Category~C classification. The instability is robust across thresholds (10--49\% at $|\Delta_{\mathrm{MH}}| \in [2.5, 1.0]$), confirmed non-random by a random-split control (0.18\%), and predominantly item-specific: domain accuracy improvement accounts for only 2.4 percentage points of the 31.3\% C\%. This instability does not invalidate MMLU as a ranking instrument ($\rho \approx 0.997$ between full and stable-item rankings) but signals that item-level measurement properties are drifting across model generations.
5	
6	The analysis exposes a validation methodology gap in the contamination detection literature. Web-overlap labels measure whether items exist in publicly accessible training corpora, not whether items function differently across model cohorts. The enrichment between DIF flags and these labels is 0.96 (chance level), the expected outcome when a differential method is evaluated against global-exposure labels. Our semi-synthetic injection framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$, $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) provides a controlled alternative that any item-level detector can use for validation. Cross-benchmark replication on GSM8K ($\Delta\mathrm{TPR} = {+}0.818$) confirms the framework's portability.
7	
8	DIF-flagged items are not noise. They concentrate cross-generational discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$, $N = 33$), consistent with DIF items capturing genuine capability change that contamination does not confer. Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain $+700$ to $+850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions. DIF is a diagnostic lens for understanding what changed across model generations, not a quality filter for removing bad items.
9	
10	LLM benchmarks need psychometric monitoring alongside score reporting. DIF analysis provides a scalable, method-agnostic diagnostic that requires only a binary response matrix and group labels, with no access to model internals or training data.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f8331c1-a5ed-44ee-a2fa-176576f2fd7b",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "bd721462-d6da-4e2a-8c72-d071c19d9ecc",
  "sourceToolAssistantUUID": "4f8331c1-a5ed-44ee-a2fa-176576f2fd7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T05:32:57.836Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UWCni7K88XkeTHYbb1umkP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd721462-d6da-4e2a-8c72-d071c19d9ecc",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAgCJ5VQR5Bn2QGTcQv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "977ed265-98c1-4de6-9d15-a8fac563583a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcVSCr2eaNCXrPTcaeTZ6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3237,
      "cache_read_input_tokens": 28169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 25 · 2026-05-21T05:32:57.848Z_

<details><summary>↩ Tool result · `toolu_01UWCni7K88XkeTHYbb1umkP`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\% $= 38.1\%$ across subjects, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\begin{tabular}{lcccc}
37	\toprule
38	Approach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\
39	\midrule
40	Baseline (external) & Cross-benchmark total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
41	Matched-ability & Within-quintile temporal DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
42	$\theta$-conditioning & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
43	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	\section{Additional Figures}
49	\label{app:figures}
50	
51	\begin{figure}[h]
52	\centering
53	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
54	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
55	\label{app:fig_matching}
56	\end{figure}
57	
58	\begin{figure}[h]
59	\centering
60	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
61	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
62	\label{app:fig_downstream}
63	\end{figure}
64	
65	\section{Cross-Benchmark Comparison}
66	\label{app:gsm8k_details}
67	
68	\begin{table}[h]
69	\centering
70	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
71	\label{tab:gsm8k_comparison}
72	\small
73	\begin{tabular}{lcc}
74	\toprule
75	Metric & MMLU & GSM8K \\
76	\midrule
77	Items & 12,508 & 1,319 \\
78	Models & 5,227 & 6,702 \\
79	Temporal C\% & 31.3\% & 18.9\% \\
80	Sanity C\% & 0.18\% & 0.3\% \\
81	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
82	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	\section{Limitations}
88	\label{app:limitations}
89	
90	\paragraph{(a) Ecological vs.\ item-level decomposition.} The ecological correlation between subject-level C\% and accuracy improvement is $\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\%) of 31.3\% C\%. The remaining 92.4\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.
91	
92	\paragraph{(b) Instability attribution.} The 31\% C\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \emph{that} items changed, not \emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.
93	
94	\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.
95	
96	\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.
97	
98	\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\Delta\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.
99	
100	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
101	
102	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
103	
104	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "977ed265-98c1-4de6-9d15-a8fac563583a",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "27c93330-3a01-4aca-a342-39596c1667e8",
  "sourceToolAssistantUUID": "977ed265-98c1-4de6-9d15-a8fac563583a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T05:32:57.982Z_

<details open><summary>🔧 Tool call — Read · `toolu_0172NHPjksyt4Zy6WsDE8g6D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27c93330-3a01-4aca-a342-39596c1667e8",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAgCJ5VQR5Bn2QGTcQv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ad81cf-5d8c-42fd-ae70-dabcd0657ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcVSCr2eaNCXrPTcaeTZ6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3237,
      "cache_read_input_tokens": 28169,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 28169,
          "cache_creation_input_tokens": 3237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3237,
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

_source line 27 · 2026-05-21T05:32:57.988Z_

<details><summary>↩ Tool result · `toolu_0172NHPjksyt4Zy6WsDE8g6D`</summary>

```text
1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
41	  author        = {Liang, Rongzhen},
42	  year          = {2026},
43	  eprint        = {2601.04895},
44	  archivePrefix = {arXiv},
45	  primaryClass  = {cs.CL},
46	  url           = {https://arxiv.org/abs/2601.04895}
47	}
48	
49	@inproceedings{shi2024mink,
50	  title     = {Detecting Pretraining Data from Large Language Models},
51	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
52	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
53	  year      = {2024},
54	  url       = {https://arxiv.org/abs/2310.16789}
55	}
56	
57	@inproceedings{tao2026selfcritique,
58	  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
59	  author    = {Tao, Yixin},
60	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
61	  year      = {2026},
62	  url       = {https://arxiv.org/abs/2510.09259}
63	}
64	
65	@inproceedings{wang2026fragility,
66	  title     = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
67	  author    = {Wang, Haonan and Li, Haoyang and Ko, Boeun and Zhang, Hongyang},
68	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
69	  year      = {2026},
70	  url       = {https://arxiv.org/abs/2510.02386}
71	}
72	
73	@misc{zhang2024gsm1k,
74	  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75	  author        = {Zhang, Hugh},
76	  year          = {2024},
77	  eprint        = {2405.00332},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2405.00332}
81	}
82	
83	@misc{zhang2024minkpp,
84	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86	  year          = {2024},
87	  eprint        = {2404.02936},
88	  archivePrefix = {arXiv},
89	  primaryClass  = {cs.CL},
90	  url           = {https://arxiv.org/abs/2404.02936}
91	}
92	
93	% ============================================================
94	% IRT Methodology & Equating
95	% ============================================================
96	
97	@misc{hardy2026scalability,
98	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
99	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
100	  year          = {2026},
101	  eprint        = {2603.24999},
102	  archivePrefix = {arXiv},
103	  primaryClass  = {cs.CL},
104	  url           = {https://arxiv.org/abs/2603.24999}
105	}
106	
107	@article{kim2019fpc,
108	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
109	  author  = {Kim, Seonghoon and Kolen, Michael},
110	  journal = {Applied Measurement in Education},
111	  year    = {2019},
112	  doi     = {10.1080/08957347.2019.1660344},
113	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
114	}
115	
116	@inproceedings{lalor2019irt,
117	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
118	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
119	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
120	  year      = {2019},
121	  doi       = {10.18653/v1/D19-1434},
122	  url       = {https://aclanthology.org/D19-1434/}
123	}
124	
125	@inproceedings{vania2021irt,
126	  title     = {Comparing Test Sets with Item Response Theory},
127	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
128	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
129	  year      = {2021},
130	  doi       = {10.18653/v1/2021.acl-long.92},
131	  url       = {https://aclanthology.org/2021.acl-long.92/}
132	}
133	
134	@misc{li2025atlas,
135	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
136	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
137	  year          = {2025},
138	  eprint        = {2511.04689},
139	  archivePrefix = {arXiv},
140	  primaryClass  = {cs.CL},
141	  url           = {https://arxiv.org/abs/2511.04689}
142	}
143	
144	@misc{chen2025irtnet,
145	  title         = {Learning Compact Representations of {LLM} Abilities via Item Response Theory},
146	  author        = {Chen, Jiayi and Wang, Chao and Zhang, Guoqiang and Ye, Peijin and Bai, Lei and Hu, Wenjun and Qu, Yongchao and Hu, Songlin},
147	  year          = {2025},
148	  eprint        = {2510.00844},
149	  archivePrefix = {arXiv},
150	  primaryClass  = {cs.CL},
151	  url           = {https://arxiv.org/abs/2510.00844}
152	}
153	
154	@misc{choi2026llmjudgeirt,
155	  title         = {Diagnosing the Reliability of {LLM}-as-a-Judge via Item Response Theory},
156	  author        = {Choi, Jiseong and Park, Seonho and Cho, Changwon and Park, Hojun and Kim, Bumsoo},
157	  year          = {2026},
158	  eprint        = {2602.00521},
159	  archivePrefix = {arXiv},
160	  primaryClass  = {cs.CL},
161	  url           = {https://arxiv.org/abs/2602.00521}
162	}
163	
164	@misc{habba2026growingpains,
165	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
166	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
167	  year          = {2026},
168	  eprint        = {2604.12843},
169	  archivePrefix = {arXiv},
170	  primaryClass  = {cs.CL},
171	  url           = {https://arxiv.org/abs/2604.12843}
172	}
173	
174	@inproceedings{zhou2026psnirt,
175	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
176	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
177	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
178	  year      = {2026},
179	  url       = {https://arxiv.org/abs/2505.15055}
180	}
181	
182	% ============================================================
183	% Dynamic Benchmark Design
184	% ============================================================
185	
186	@inproceedings{white2025livebench,
187	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
188	  author    = {White, Colin},
189	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
190	  year      = {2025},
191	  doi       = {10.48550/arXiv.2406.19314},
192	  url       = {https://arxiv.org/abs/2406.19314}
193	}
194	
195	@misc{kipnis2024metabench,
196	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
197	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
198	  year          = {2024},
199	  eprint        = {2407.12844},
200	  archivePrefix = {arXiv},
201	  primaryClass  = {cs.CL},
202	  url           = {https://arxiv.org/abs/2407.12844}
203	}
204	
205	@inproceedings{hendrycks2021mmlu,
206	  title     = {Measuring Massive Multitask Language Understanding},
207	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
208	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
209	  year      = {2021},
210	  url       = {https://arxiv.org/abs/2009.03300}
211	}
212	
213	@article{liang2023helm,
214	  title   = {Holistic Evaluation of Language Models},
215	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya},
216	  journal = {Transactions on Machine Learning Research},
217	  year    = {2023},
218	  doi     = {10.1111/nyas.15007},
219	  url     = {https://arxiv.org/abs/2211.09110}
220	}
221	
222	@inproceedings{chiang2024chatbot,
223	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
224	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
225	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
226	  year      = {2024},
227	  doi       = {10.48550/arXiv.2403.04132},
228	  url       = {https://arxiv.org/abs/2403.04132}
229	}
230	
231	@misc{mialon2023gaia,
232	  title         = {{GAIA}: a benchmark for General {AI} Assistants},
233	  author        = {Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
234	  year          = {2023},
235	  eprint        = {2311.12983},
236	  archivePrefix = {arXiv},
237	  primaryClass  = {cs.CL},
238	  url           = {https://arxiv.org/abs/2311.12983}
239	}
240	
241	@inproceedings{li2024latesteval,
242	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
243	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
244	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
245	  year      = {2024},
246	  doi       = {10.48550/arXiv.2312.12343},
247	  url       = {https://arxiv.org/abs/2312.12343}
248	}
249	
250	@inproceedings{kiela2021dynabench,
251	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
252	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
253	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
254	  year      = {2021},
255	  doi       = {10.18653/v1/2021.naacl-main.324},
256	  url       = {https://arxiv.org/abs/2104.14337}
257	}
258	
259	% ============================================================
260	% DIF Statistical Methods
261	% ============================================================
262	
263	@article{belzak2020smallsample,
264	  title   = {Testing Differential Item Functioning in Small Samples},
265	  author  = {Belzak, William},
266	  journal = {Multivariate Behavioral Research},
267	  year    = {2020},
268	  doi     = {10.1080/00273171.2019.1671162},
269	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
270	}
271	
272	@incollection{holland1988mh,
273	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
274	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
275	  booktitle = {Test Validity},
276	  editor    = {Wainer, Howard and Braun, Henry I.},
277	  publisher = {Lawrence Erlbaum Associates},
278	  year      = {1988},
279	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
280	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
281	}
282	
283	@article{shealy1993sibtest,
284	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
285	  author  = {Shealy, Robin and Stout, William},
286	  journal = {Psychometrika},
287	  year    = {1993},
288	  doi     = {10.1007/BF02294572},
289	  url     = {https://link.springer.com/article/10.1007/BF02294572}
290	}
291	
292	@article{clauser1998dif,
293	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
294	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
295	  journal = {Educational Measurement: Issues and Practice},
296	  year    = {1998},
297	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
298	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
299	}
300	
301	@book{zumbo1999handbook,
302	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
303	  author    = {Zumbo, Bruno D.},
304	  year      = {1999},
305	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
306	  address   = {Ottawa},
307	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
308	}
309	
310	@article{meredith1993invariance,
311	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
312	  author  = {Meredith, William},
313	  journal = {Psychometrika},
314	  year    = {1993},
315	  doi     = {10.1007/BF02294825},
316	  url     = {https://link.springer.com/article/10.1007/BF02294825}
317	}
318	
319	@article{vandenberg2000invariance,
320	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
321	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
322	  journal = {Organizational Research Methods},
323	  year    = {2000},
324	  doi     = {10.1177/109442810031002},
325	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
326	}
327	
328	@article{swaminathan1990logistic,
329	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
330	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
331	  journal = {Journal of Educational Measurement},
332	  year    = {1990},
333	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
334	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
335	}
336	
337	@article{teresi2007dif,
338	  title   = {Differential Item Functioning and Health Assessment},
339	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
340	  journal = {Quality of Life Research},
341	  year    = {2007},
342	  doi     = {10.1007/s11136-007-9184-6},
343	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
344	}
345	
346	@book{lord1980irt,
347	  title     = {Applications of Item Response Theory to Practical Testing Problems},
348	  author    = {Lord, Frederic M.},
349	  year      = {1980},
350	  publisher = {Lawrence Erlbaum Associates},
351	  address   = {Hillsdale, NJ}
352	}
353	
354	@article{raju1988area,
355	  title   = {The Area between Two Item Characteristic Curves},
356	  author  = {Raju, Nambury S.},
357	  journal = {Psychometrika},
358	  year    = {1988},
359	  doi     = {10.1007/BF02294403},
360	  url     = {https://link.springer.com/article/10.1007/BF02294403}
361	}
362	
363	@article{muthen1985mimic,
364	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
365	  author  = {Muth{\'e}n, Bengt},
366	  journal = {Journal of Educational Statistics},
367	  year    = {1985},
368	  doi     = {10.2307/1164966}
369	}
370	
371	@article{woods2009mimic,
372	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
373	  author  = {Woods, Carol M.},
374	  journal = {Applied Psychological Measurement},
375	  year    = {2009},
376	  doi     = {10.1177/0146621609331279}
377	}
378	
379	% ============================================================
380	% LLM Evaluation Methodology
381	% ============================================================
382	
383	@article{burnell2023rethink,
384	  title   = {Rethink reporting of evaluation results in {AI}},
385	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
386	  journal = {Science},
387	  year    = {2023},
388	  doi     = {10.1126/science.adf6369},
389	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
390	}
391	
392	@article{chang2024survey,
393	  title   = {A Survey on Evaluation of Large Language Models},
394	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
395	  journal = {ACM Transactions on Intelligent Systems and Technology},
396	  year    = {2024},
397	  doi     = {10.1145/3641289},
398	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
399	}
400	
401	@inproceedings{maiapolo2024tinybenchmarks,
402	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
403	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
404	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
405	  year      = {2024},
406	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
407	}
408	
409	@inproceedings{wang2024mmlupro,
410	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
411	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Xue, Xiang and Chen, Wenhu},
412	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
413	  year      = {2024},
414	  url       = {https://arxiv.org/abs/2406.01574}
415	}
416	
417	@article{ott2022benchmark,
418	  title   = {Mapping global dynamics of benchmark creation and saturation in artificial intelligence},
419	  author  = {Ott, Simon and Barbosa-Silva, Adriano and Blagec, Kathrin and Brauner, Jan and Samwald, Matthias},
420	  journal = {Nature Communications},
421	  year    = {2022},
422	  doi     = {10.1038/s41467-022-34591-0},
423	  url     = {https://www.nature.com/articles/s41467-022-34591-0}
424	}
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9ad81cf-5d8c-42fd-ae70-dabcd0657ec7",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "c13d256d-1817-4416-a6bf-dd0005c0be99",
  "sourceToolAssistantUUID": "f9ad81cf-5d8c-42fd-ae70-dabcd0657ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T05:33:02.067Z_

Now let me check for any additional experiment results or figures that might be referenced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c13d256d-1817-4416-a6bf-dd0005c0be99",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAh1yFAnaTYWrQWR8FK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "592604d6-e464-4eee-8d84-fbde053efb6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZkfRDZb78xTdcQncKtc1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11193,
      "cache_read_input_tokens": 31406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11193,
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

_source line 29 · 2026-05-21T05:33:04.158Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XXmG2wfgzzsJyvVNdHJXyH`</summary>

```json
{
  "pattern": "figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "592604d6-e464-4eee-8d84-fbde053efb6b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAh1yFAnaTYWrQWR8FK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0068a8c5-7fff-4faa-b69d-ed6a57eca80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZkfRDZb78xTdcQncKtc1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11193,
      "cache_read_input_tokens": 31406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11193,
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

_source line 30 · 2026-05-21T05:33:04.182Z_

<details><summary>↩ Tool result · `toolu_01XXmG2wfgzzsJyvVNdHJXyH`</summary>

```text
figures/paper/fig_2_dose_response.pdf
figures/paper/fig_3_within_subject_matching.pdf
figures/paper/fig_A1_subject_heatmap.pdf
figures/paper/fig_A2_q3_distribution.pdf
figures/paper/fig_4_downstream_impact.pdf
figures/paper/fig_1_global_vs_differential.pdf
figures/paper/fig_5_gsm1k_dif_correlation.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0068a8c5-7fff-4faa-b69d-ed6a57eca80c",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "20be9ee5-5de6-4cbf-9dad-151019473345",
  "sourceToolAssistantUUID": "0068a8c5-7fff-4faa-b69d-ed6a57eca80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T05:33:04.639Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015TkRxCL6JPCufAGZB25v8d`</summary>

```json
{
  "pattern": "artifacts/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20be9ee5-5de6-4cbf-9dad-151019473345",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAh1yFAnaTYWrQWR8FK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd1c5df2-667b-4986-b600-6a808a6dbb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZkfRDZb78xTdcQncKtc1Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11193,
      "cache_read_input_tokens": 31406,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 31406,
          "cache_creation_input_tokens": 11193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11193,
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

_source line 32 · 2026-05-21T05:33:04.658Z_

<details><summary>↩ Tool result · `toolu_015TkRxCL6JPCufAGZB25v8d`</summary>

```text
artifacts/_project/data/metabench_summary_646c62.json
artifacts/_project/data/metabench_summary.json
artifacts/metabench_summary.json
artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json
artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json
artifacts/dream_reports/dream_20260520T194223/worst/experiment_data.json
artifacts/_project/data/irt_scale_analysis.json
artifacts/irt_scale_analysis.json
artifacts/_project/data/mmlu_cf_analysis.json
artifacts/mmlu_cf_analysis.json
artifacts/dream_reports/dream_20260520T205007/best/experiment_data.json
artifacts/dream_reports/dream_20260520T205007/median/experiment_data.json
artifacts/dream_reports/dream_20260520T205007/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T012912/best/experiment_data.json
artifacts/dream_reports/dream_20260521T012912/median/experiment_data.json
artifacts/dream_reports/dream_20260521T012912/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T032826/best/experiment_data.json
artifacts/dream_reports/dream_20260521T032826/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T042647/best/experiment_data.json
artifacts/dream_reports/dream_20260521T042647/median/experiment_data.json
artifacts/dream_reports/dream_20260521T042647/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd1c5df2-667b-4986-b600-6a808a6dbb73",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "8e65d4fb-4e86-4ee8-b50e-1eed3ac539c0",
  "sourceToolAssistantUUID": "bd1c5df2-667b-4986-b600-6a808a6dbb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T05:33:08.526Z_

Now let me also check the paper title in the main.tex vs what was provided in the summary, and look at the report for any additional context about the paper's claims and evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e65d4fb-4e86-4ee8-b50e-1eed3ac539c0",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAhWNnxSwz1A8VQDQHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6022dd0d-2988-454d-9a35-c8670741133b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016x1yDrT3p1UUomEVALTcdY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 42599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 795,
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

_source line 34 · 2026-05-21T05:33:08.960Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ThjwDAcZq6xc3n7GGtbJoK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6022dd0d-2988-454d-9a35-c8670741133b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAhWNnxSwz1A8VQDQHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44c4cd9e-810d-4c3a-b376-76169ed31d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016x1yDrT3p1UUomEVALTcdY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 42599,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 42599,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 795,
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

_source line 35 · 2026-05-21T05:33:08.965Z_

<details><summary>↩ Tool result · `toolu_01ThjwDAcZq6xc3n7GGtbJoK`</summary>

```text
1	# Handover — 2026-05-21
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	（无）
7	
8	## 待处理
9	- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）
10	
11	## 近期结论
12	- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu
13	- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu
14	- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif
15	  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)
16	
17	## 趋势
18	成功 5 / 负向 6 / 失败 0 / 共 11
19	
20	## 下一步
21	（无活跃 idea，请通过 ideas.md 添加）
22	
23	## 资源状态
24	（无服务器配置）
25	
26	## 告警
27	（无）
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44c4cd9e-810d-4c3a-b376-76169ed31d5b",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "51d2ddfe-3361-4ad1-ad3e-06a2026ec47d",
  "sourceToolAssistantUUID": "44c4cd9e-810d-4c3a-b376-76169ed31d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T05:33:12.306Z_

Now I have a thorough understanding of the paper. Let me also load the tool needed to submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d2ddfe-3361-4ad1-ad3e-06a2026ec47d",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAhptXP8LahG4JRWdxc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cdd9afb-f472-4d49-814c-545e8a146537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHyS8QT8miemPuuHVgU9Cg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1217,
      "cache_read_input_tokens": 43394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1217,
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

_source line 37 · 2026-05-21T05:33:13.167Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bfgzhyq1NMqK5WWrcEKxkS`</summary>

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
  "parentUuid": "8cdd9afb-f472-4d49-814c-545e8a146537",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAhptXP8LahG4JRWdxc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04703961-7a7d-4a2c-9617-82cdadabc8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHyS8QT8miemPuuHVgU9Cg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1217,
      "cache_read_input_tokens": 43394,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1217
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 43394,
          "cache_creation_input_tokens": 1217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1217,
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

_source line 38 · 2026-05-21T05:33:13.171Z_

<details><summary>↩ Tool result · `toolu_01Bfgzhyq1NMqK5WWrcEKxkS`</summary>

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
  "parentUuid": "04703961-7a7d-4a2c-9617-82cdadabc8b6",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "36eaad21-f345-4007-877e-baba5b028ddd",
  "sourceToolAssistantUUID": "04703961-7a7d-4a2c-9617-82cdadabc8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T05:33:15.851Z_



Now let me check which dream invocation this review is for.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36eaad21-f345-4007-877e-baba5b028ddd",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAi8p3BikQ1UGp66uia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da43ff05-2c7f-43c2-8e8d-0bdb928b534b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GanWahFbwdcV7paxA9V48c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 44611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 40 · 2026-05-21T05:33:17.369Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AewL1aHFoKCctNtzMDwipo`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/ | tail -20",
  "description": "List dream report directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da43ff05-2c7f-43c2-8e8d-0bdb928b534b",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAi8p3BikQ1UGp66uia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06df1d62-5a4c-4ce3-b152-7f4de4e6d877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GanWahFbwdcV7paxA9V48c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 44611,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 44611,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 737,
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

_source line 41 · 2026-05-21T05:33:17.640Z_

<details><summary>↩ Tool result · `toolu_01AewL1aHFoKCctNtzMDwipo`</summary>

```text
total 36
drwxr-xr-x  8 ubuntu ubuntu 4096 May 21 04:26 .
drwxr-xr-x 28 ubuntu ubuntu 4096 May 21 05:21 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 May 20 19:34 dream_20260520T193456
drwxr-xr-x  6 ubuntu ubuntu 4096 May 20 20:32 dream_20260520T194223
drwxr-xr-x  6 ubuntu ubuntu 4096 May 20 21:45 dream_20260520T205007
drwxr-xr-x  6 ubuntu ubuntu 4096 May 21 02:23 dream_20260521T012912
drwxr-xr-x  6 ubuntu ubuntu 4096 May 21 04:00 dream_20260521T032826
drwxr-xr-x  6 ubuntu ubuntu 4096 May 21 05:05 dream_20260521T042647
lrwxrwxrwx  1 ubuntu ubuntu  126 May 21 04:00 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06df1d62-5a4c-4ce3-b152-7f4de4e6d877",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "c7ba4405-48a6-41e6-aa89-aba218f9f581",
  "sourceToolAssistantUUID": "06df1d62-5a4c-4ce3-b152-7f4de4e6d877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T05:33:21.336Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016NPd4Drdj2nbpT3Bzwhk9L`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/",
  "description": "Check latest dream report structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ba4405-48a6-41e6-aa89-aba218f9f581",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAiTnYsg2e4pQNsRgRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fda12c64-a87b-4240-b37d-36020daca881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KupHHz4ubYxFwS7AK5snwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 45348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 43 · 2026-05-21T05:33:21.392Z_

<details><summary>↩ Tool result · `toolu_016NPd4Drdj2nbpT3Bzwhk9L`</summary>

```text
total 24
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 05:05 .
drwxr-xr-x 8 ubuntu ubuntu 4096 May 21 04:26 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 05:19 best
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 05:29 logs
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 05:28 median
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 05:29 worst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda12c64-a87b-4240-b37d-36020daca881",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "aecdd59c-0f91-4a5e-9351-9fabfaade2ae",
  "sourceToolAssistantUUID": "fda12c64-a87b-4240-b37d-36020daca881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T05:33:21.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GkVXuxJkazBVgYAse43hbm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/paper.tex",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aecdd59c-0f91-4a5e-9351-9fabfaade2ae",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAiTnYsg2e4pQNsRgRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ec75f93-350e-497c-b919-3fba9f466561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KupHHz4ubYxFwS7AK5snwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 45348,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 492
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 45348,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 492,
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

_source line 45 · 2026-05-21T05:33:21.839Z_

<details><summary>↩ Tool result · `toolu_01GkVXuxJkazBVgYAse43hbm`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ec75f93-350e-497c-b919-3fba9f466561",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "87a4d9a4-bfa4-4254-b94b-2bfa487923af",
  "sourceToolAssistantUUID": "6ec75f93-350e-497c-b919-3fba9f466561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T05:33:24.541Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018WRHxB1kL4U82wpWMB98ze`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/",
  "description": "Check files in best tier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87a4d9a4-bfa4-4254-b94b-2bfa487923af",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAimtiyfSedt1Zs1XzE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2a8d8ca-9e94-447f-a67f-65810e6e70dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp5nZN9Q24sQHZgX52AkMA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 529,
      "cache_read_input_tokens": 45840,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 45840,
          "cache_creation_input_tokens": 529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 529,
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

_source line 47 · 2026-05-21T05:33:24.618Z_

<details><summary>↩ Tool result · `toolu_018WRHxB1kL4U82wpWMB98ze`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_db82206b.pdf
review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2a8d8ca-9e94-447f-a67f-65810e6e70dc",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "b09cb72e-2f05-47a2-b5e3-a7bf6468c60d",
  "sourceToolAssistantUUID": "b2a8d8ca-9e94-447f-a67f-65810e6e70dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T05:33:27.361Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AS6hYs1E5YCPaQYTJ9V8GD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b09cb72e-2f05-47a2-b5e3-a7bf6468c60d",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAiyrofaSfbRM1SGNXs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9067e43-7ae9-4866-97cb-66b38b10abc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018th5D8NtVDrNSNuCgwPSSn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 197,
      "cache_read_input_tokens": 46369,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 46369,
          "cache_creation_input_tokens": 197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 197,
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

_source line 49 · 2026-05-21T05:33:27.705Z_

<details><summary>↩ Tool result · `toolu_01AS6hYs1E5YCPaQYTJ9V8GD`</summary>

```text
1	narrative_guidance: 'Original framing holds without adjustment. Four claims presented
2	  as stated in paper_framing.md. Headline: "31% temporal instability is robust, not
3	  driven by capability gains (≤7.6%), and the field''s web-overlap ground truth is
4	  fundamentally mismatched for item-level detection." Circularity ablation (plan_020,
5	  done) + GSM1K anti-correlation (plan_004 Step 3, done) form coherent two-pronged
6	  downstream story. Non-uniform DIF robustness check (SIBTEST/logistic regression
7	  on 5-10 representative subjects, not in experiment_plan but required for reviewer
8	  concern #9) confirms <5% items with substantial non-uniform DIF beyond MH flags
9	  (Jaccard ~0.89 between MH and SIBTEST flag sets) — MH adequacy validated for this
10	  99.98% decoder-only population. Appendix experiments (plan_002/003a/003b/003c/005/006/007/008/009)
11	  provide supplementary texture without becoming load-bearing. No claims need softening;
12	  appendix material stays in appendix. ICLR reviewers accept discovery-paper framing;
13	  DIF primer in §3 successfully bridges psychometrics→ML vocabulary gap.
14	
15	  '
16	imagined_experiments:
17	- name: real_data_dif_mmlu
18	  plan_id: plan_001
19	  description: 'MH-DIF on METABENCH MMLU 5,219×12,508 matrix. Temporal cohort (2023
20	    vs 2024-H1), ability-quintile cohort, within-family confound control, domain-specificity,
21	    random sanity. Proxy validation against Li et al. web-overlap labels.
22	
23	    '
24	  expected_results:
25	    temporal_ets_c_pct: 31.3
26	    temporal_fpr_li_clean: 0.318
27	    temporal_enrichment_vs_li: 0.96
28	    ability_ets_c_pct: 2.9
29	    ability_enrichment: 1.19
30	    within_family_llama2v3_c_pct: 61.3
31	    within_family_mistral_mixtral_c_pct: 38.7
32	    domain_spearman_rho: 0.307
33	    domain_spearman_p: 0.02
34	    sanity_random_split_c_pct: 0.18
35	    temporal_ability_jaccard: 0.014
36	    n_ref_temporal: 1253
37	    n_foc_temporal: 656
38	    n_items_tested: 12508
39	    n_ets_c_items: 3918
40	  result_rationale: '[DONE — actual registry data] 31.3% C% reflects genuine temporal
41	    item instability: model generations 2023→2024-H1 differ in training data composition,
42	    RLHF procedures, and data curation practices, all of which change how items function.
43	    Enrichment≈0.96 against Li et al. labels is expected and predicted: web-overlap
44	    labels capture item existence on the internet (global exposure), not whether an
45	    item functions differently across cohorts (differential contamination). DIF detects
46	    the latter; the two measures are orthogonal by construction. Random-split sanity
47	    (0.18%) confirms the 31.3% is not a statistical artifact of the MH procedure.
48	    Domain correlation ρ=0.307 is modest — subjects where models improved more show
49	    slightly more DIF, but item-level decomposition (plan_019, done separately) confirms
50	    this explains at most 7.6% of the instability.
51	
52	    '
53	  tables:
54	  - name: 'Table 1: DIF Detection Summary by Cohort Definition'
55	    columns:
56	    - cohort
57	    - N_ref
58	    - N_foc
59	    - ETS_A_pct
60	    - ETS_B_pct
61	    - ETS_C_pct
62	    - enrichment_Li
63	    rows:
64	    - - temporal
65	      - 1253
66	      - 656
67	      - 52.1
68	      - 16.6
69	      - 31.3
70	      - 0.96
71	    - - ability_quintile
72	      - 1044
73	      - 1044
74	      - 91.8
75	      - 5.3
76	      - 2.9
77	      - 1.19
78	    - - random_sanity
79	      - 955
80	      - 955
81	      - 99.1
82	      - 0.7
83	      - 0.18
84	      - —
85	  - name: 'Table 2: Within-Family Confound Control'
86	    columns:
87	    - family_pair
88	    - N_ref
89	    - N_foc
90	    - C_pct
91	    - overlap_w_temporal_jaccard
92	    rows:
93	    - - Llama-2 vs Llama-3
94	      - 161
95	      - 308
96	      - 61.3
97	      - 0.41
98	    - - Mistral vs Mixtral
99	      - 89
100	      - 112
101	      - 38.7
102	      - 0.34
103	  figures_description:
104	  - 'Fig 1: Δ_MH distribution across 12,508 items for temporal cohort — bimodal with
105	    peaks at 0 and ±2.0'
106	  - 'Fig 2: Domain-level DIF C% vs accuracy improvement scatterplot (57 subjects),
107	    ρ=0.307'
108	  analysis: 'Temporal DIF at 31.3% is the load-bearing finding for Claim 1. The near-zero
109	    random-split sanity check (0.18%) and low ability-cohort C% (2.9%) establish that
110	    the temporal signal is real and specific to time, not ability. Within-family results
111	    (Llama 61.3%, Mistral 38.7%) show DIF persists even within architecture families,
112	    suggesting item instability is not purely a between-family artifact. Enrichment≈0.96
113	    directly motivates the ground truth meta-critique (Claim 2).
114	
115	    '
116	- name: rl_robustness_validation
117	  plan_id: plan_002
118	  description: 'Empirically validate DIF''s robustness to RL-trained models. Three
119	    cohort compositions (SFT-only, +alignment-RL, +reasoning-RL). Traditional detector
120	    comparison (Min-K%, ConStat) on 10-15 reasoning-RL models individually.
121	
122	    '
123	  expected_results:
124	    n_sft_only_models: 2340
125	    n_alignment_rl_models: 477
126	    n_reasoning_rl_models: 13
127	    dif_flag_jaccard_sft_vs_sft_alignrl: 0.912
128	    dif_flag_jaccard_sft_vs_sft_allrl: 0.874
129	    dif_flag_jaccard_alignrl_vs_allrl: 0.935
130	    dif_c_pct_sft_only_cohort: 31.1
131	    dif_c_pct_sft_alignrl_cohort: 31.5
132	    dif_c_pct_sft_allrl_cohort: 31.8
133	    mink_auroc_reasoning_rl: 0.563
134	    constat_auroc_reasoning_rl: 0.614
135	    dif_auroc_cohort_with_rl: 0.831
136	    delong_p_dif_vs_mink: 0.032
137	    delong_p_dif_vs_constat: 0.078
138	    tost_equivalence_p: 0.117
139	    bootstrap_auroc_diff_ci_dif_mink:
140	    - 0.06
141	    - 0.33
142	    bootstrap_auroc_diff_ci_dif_constat:
143	    - -0.02
144	    - 0.28
145	    power_detection_boundary_p: 0.45
146	    power_detection_boundary_delta: 1.4
147	    power_detection_boundary_N: 80
148	  result_rationale: 'DIF''s group-level design conditions on total score, making it
149	    fundamentally insensitive to individual model output distributions. Adding 13
150	    reasoning-RL models to a cohort of N≥80 shifts the score distribution marginally
151	    (~0.3pp in C%) because MH''s quintile-based matching absorbs ability variation.
152	    The high Jaccard (0.87-0.91) reflects that DIF flags are driven by the bulk population,
153	    not the RL tail. Min-K% degrades to near-chance (AUROC=0.56) because RL training
154	    contracts the NLL gap that Min-K% exploits — the per-token likelihood distribution
155	    becomes flatter, destroying the memorization signal. ConStat fares slightly better
156	    (0.61) because perturbation sensitivity is partially preserved under alignment-RL
157	    but substantially reduced under reasoning-RL (GRPO/PPO explicitly optimize for
158	    robust reasoning). TOST at p=0.117 is inconclusive, honestly reflecting the N=13
159	    limitation. This is presented in limitations as "suggestive evidence of RL robustness,
160	    underpowered for formal equivalence."
161	
162	    '
163	  tables:
164	  - name: 'Table A1: DIF Flag Stability Across Cohort Compositions'
165	    columns:
166	    - cohort
167	    - N_total
168	    - C_pct
169	    - Jaccard_vs_SFT
170	    rows:
171	    - - SFT-only
172	      - 2340
173	      - 31.1
174	      - 1.0
175	    - - SFT + alignment-RL
176	      - 2817
177	      - 31.5
178	      - 0.912
179	    - - SFT + all-RL
180	      - 2830
181	      - 31.8
182	      - 0.874
183	  - name: 'Table A2: Per-Model Detector Comparison on Reasoning-RL Models'
184	    columns:
185	    - detector
186	    - AUROC
187	    - 95% CI
188	    - degradation_vs_nonRL
189	    rows:
190	    - - Min-K%
191	      - 0.563
192	      - '[0.41, 0.72]'
193	      - '-0.31'
194	    - - ConStat
195	      - 0.614
196	      - '[0.46, 0.77]'
197	      - '-0.24'
198	    - - DIF (group)
199	      - 0.831
200	      - '[0.74, 0.92]'
201	      - '-0.02'
202	  figures_description:
203	  - 'Fig A1: AUROC comparison across detectors for reasoning-RL models with bootstrap
204	    CIs'
205	  - 'Fig A2: DIF detection power surface as function of exploitation rate p and effect
206	    size δ'
207	  analysis: 'Results confirm the theoretical argument: DIF''s group-level conditioning
208	    makes it robust to RL-induced output distribution changes, while per-model detectors
209	    (Min-K%, ConStat) degrade substantially. However, N=13 reasoning-RL models precludes
210	    formal equivalence testing. Appendix-appropriate: strengthens Claim 1 narrative
211	    without being load-bearing. The power surface shows DIF retains detection for
212	    δ≥1.4 at p≥0.45, covering the operationally relevant regime (large effects with
213	    moderate exploitation).
214	
215	    '
216	- name: constat_perturbation_eval
217	  plan_id: plan_003a
218	  description: 'Independent ConStat-style perturbation evaluation on MMLU. Generate
219	    paraphrases for 200+ items, compare original vs reformulated performance, apply
220	    FDR-controlled detection.
221	
222	    '
223	  expected_results:
224	    n_items_paraphrased: 237
225	    semantic_similarity_mean: 0.918
226	    human_quality_pct: 94.1
227	    constat_tpr_non_rl_contaminated: 0.438
228	    constat_tpr_rl_contaminated: 0.172
229	    constat_fpr_fdr_q005: 0.038
230	    cohens_d_non_rl: 0.871
231	    cohens_d_rl: 0.293
232	    perf_drop_contaminated_non_rl_pct: -13.1
233	    perf_drop_contaminated_rl_pct: -4.2
234	    perf_drop_clean_pct: -2.8
235	    paraphrase_difficulty_shift_mean: 0.04
236	    n_models_evaluated: 48
237	  result_rationale: 'ConStat''s detection mechanism exploits surface-level memorization:
238	    models that memorized exact item phrasings show large performance drops on semantically
239	    equivalent paraphrases. Non-RL models exhibit this cleanly (d=0.87, TPR=0.44)
240	    because their memorization is token-sequence-specific. RL-trained models show
241	    attenuated signal (d=0.29, TPR=0.17) because reward optimization encourages generalization
242	    beyond exact training sequences — the RL objective effectively launders memorization
243	    into robust capability, making it indistinguishable from genuine learning. FPR
244	    at 0.038 confirms FDR control works. The clean-item performance drop (-2.8%) reflects
245	    natural difficulty increase from paraphrasing (slight semantic drift, unfamiliar
246	    phrasing) rather than contamination. This complements DIF: ConStat detects per-model
247	    surface memorization, DIF detects group-level differential functioning regardless
248	    of mechanism.
249	
250	    '
251	  tables:
252	  - name: 'Table A3: ConStat Detection by Model Training Type'
253	    columns:
254	    - model_type
255	    - N_models
256	    - TPR
257	    - FPR
258	    - Cohen_d
259	    - perf_drop_pct
260	    rows:
261	    - - SFT-only
262	      - 22
263	      - 0.438
264	      - 0.038
265	      - 0.871
266	      - -13.1
267	    - - Alignment-RL
268	      - 18
269	      - 0.172
270	      - 0.041
271	      - 0.293
272	      - -4.2
273	    - - Clean (no contamination)
274	      - 8
275	      - —
276	      - 0.038
277	      - —
278	      - -2.8
279	  figures_description:
280	  - 'Fig A3: Performance drop distribution (original vs paraphrase) for contaminated
281	    vs clean items'
282	  - 'Fig A4: ConStat detection power as function of paraphrase semantic distance'
283	  analysis: 'ConStat demonstrates moderate detection of surface memorization in non-RL
284	    models but degrades substantially for RL models. This characterizes ConStat''s
285	    complementary detection niche and motivates ensemble approaches. Appendix-appropriate:
286	    validates one component of the ensemble framework (Claim 2 old, now dropped to
287	    future work) without being needed for current claims.
288	
289	    '
290	- name: dvd_generation_variance_eval
291	  plan_id: plan_003b
292	  description: 'DVD generation variance evaluation on MMLU. 50 responses per item
293	    via temperature sampling on 10-15 open-weight models. Detect bimodal distributions
294	    as contamination signal.
295	
296	    '
297	  expected_results:
298	    n_models: 12
299	    n_items_evaluated: 200
300	    n_generations_per_item: 50
301	    temperature: 0.8
302	    dvd_tpr_verbatim: 0.523
303	    dvd_tpr_variant: 0.138
304	    dvd_fpr: 0.062
305	    bimodality_coeff_contaminated: 0.714
306	    bimodality_coeff_clean: 0.283
307	    gen_variance_contaminated_mean: 0.087
308	    gen_variance_contaminated_sd: 0.131
309	    gen_variance_clean_mean: 0.312
310	    gen_variance_clean_sd: 0.108
311	    auroc_verbatim: 0.813
312	    auroc_variant: 0.571
313	    gpu_hours_used: 52
314	  result_rationale: 'Verbatim memorization produces near-deterministic outputs — the
315	    model has effectively learned a lookup table for memorized items, generating the
316	    correct answer with probability >0.95 regardless of temperature. This creates
317	    bimodal generation distributions (always correct or fully random) with near-zero
318	    variance, easily distinguished from clean items (moderate variance reflecting
319	    genuine uncertainty). Variant contamination does NOT produce this bimodality because
320	    the model learned the underlying concept rather than the exact answer string —
321	    generation variance remains moderate, and DVD cannot distinguish "learned from
322	    training data" from "genuinely knows." This limits DVD to a specific niche: detecting
323	    exact-match verbatim memorization of item text + answer. Complementary to DIF
324	    (group-level, mechanism-agnostic) and ConStat (perturbation-based, per-model).
325	
326	    '
327	  tables:
328	  - name: 'Table A4: DVD Detection by Contamination Type'
329	    columns:
330	    - contamination_type
331	    - N_items
332	    - TPR
333	    - FPR
334	    - bimodality_coeff
335	    - mean_gen_variance
336	    rows:
337	    - - verbatim
338	      - 80
339	      - 0.523
340	      - 0.062
341	      - 0.714
342	      - 0.087
343	    - - variant
344	      - 60
345	      - 0.138
346	      - 0.062
347	      - 0.391
348	      - 0.224
349	    - - clean
350	      - 60
351	      - —
352	      - 0.062
353	      - 0.283
354	      - 0.312
355	  figures_description:
356	  - 'Fig A5: Generation variance distributions for verbatim-contaminated vs clean
357	    items'
358	  - 'Fig A6: Bimodality coefficient histogram across all items, colored by contamination
359	    status'
360	  analysis: 'DVD occupies a narrow but clear detection niche: verbatim exact-match
361	    memorization. Its inability to detect variant contamination is a fundamental limitation
362	    — generation variance cannot distinguish "learned from contaminated data" from
363	    "genuinely competent." This underscores the complementarity argument for ensemble
364	    approaches and the advantage of DIF''s mechanism-agnostic group-level detection.
365	    Appendix-appropriate: useful for characterizing the detection landscape but not
366	    needed for current claims.
367	
368	    '
369	- name: ensemble_fusion
370	  plan_id: plan_003c
371	  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble. Majority voting
372	    and weighted fusion. Coverage analysis by contamination mechanism.
373	
374	    '
375	  expected_results:
376	    dif_alone_tpr: 0.682
377	    constat_alone_tpr: 0.438
378	    dvd_alone_tpr: 0.523
379	    majority_2of3_tpr: 0.731
380	    majority_2of3_fpr: 0.028
381	    majority_2of3_precision: 0.921
382	    weighted_fusion_tpr: 0.778
383	    weighted_fusion_fpr: 0.057
384	    weighted_fusion_precision: 0.883
385	    uniform_weight_tpr: 0.752
386	    uniform_weight_fpr: 0.044
387	    optimal_weights_dif: 0.43
388	    optimal_weights_constat: 0.32
389	    optimal_weights_dvd: 0.25
390	    cv_weight_stability_cv: 0.13
391	    coverage_dif_only_pct: 22.8
392	    coverage_constat_only_pct: 13.6
393	    coverage_dvd_only_pct: 8.1
394	    coverage_multi_signal_pct: 55.5
395	  result_rationale: 'The three detectors exploit orthogonal contamination dimensions:
396	    DIF measures differential group-level item functioning (mechanism-agnostic, requires
397	    cohort comparison), ConStat measures per-model perturbation sensitivity (targets
398	    surface memorization), DVD measures generation variance (targets verbatim memorization).
399	    Their error patterns are weakly correlated because they target different aspects
400	    of contamination. Majority voting suppresses false positives (FPR=0.028) by requiring
401	    convergent evidence from 2+ independent mechanisms. Weighted fusion gains ~5pp
402	    TPR over majority voting at the cost of higher FPR (0.057) by allowing strong
403	    single-signal evidence to override absent signals. Optimal weights favor DIF (0.43)
404	    because it has the broadest coverage (mechanism-agnostic, group-level), followed
405	    by ConStat (0.32) and DVD (0.25). The modest improvement over uniform weights
406	    reflects limited calibration data.
407	
408	    '
409	  tables:
410	  - name: 'Table A5: Ensemble Detection Performance'
411	    columns:
412	    - strategy
413	    - TPR
414	    - FPR
415	    - precision
416	    - F1
417	    rows:
418	    - - DIF only
419	      - 0.682
420	      - 0.036
421	      - 0.892
422	      - 0.773
423	    - - ConStat only
424	      - 0.438
425	      - 0.038
426	      - 0.854
427	      - 0.579
428	    - - DVD only
429	      - 0.523
430	      - 0.062
431	      - 0.809
432	      - 0.635
433	    - - 2-of-3 majority
434	      - 0.731
435	      - 0.028
436	      - 0.921
437	      - 0.815
438	    - - Weighted fusion
439	      - 0.778
440	      - 0.057
441	      - 0.883
442	      - 0.827
443	    - - Uniform weights
444	      - 0.752
445	      - 0.044
446	      - 0.893
447	      - 0.817
448	  figures_description:
449	  - 'Fig A7: Venn diagram of detection coverage by signal type'
450	  - 'Fig A8: ROC curves for individual signals and ensemble strategies'
451	  analysis: 'Ensemble improves coverage but is not needed for current paper claims
452	    (Claim 2 pivoted from ensemble to ground truth meta-critique). Results support
453	    future work direction: multi-signal contamination detection as a practical pipeline.
454	    The 22.8% DIF-only coverage confirms DIF detects contamination modes invisible
455	    to per-model methods. Appendix-appropriate: demonstrates feasibility without being
456	    load-bearing.
457	
458	    '
459	- name: cross_benchmark_gsm8k
460	  plan_id: plan_004
461	  description: 'GSM8K DIF replication (1,319 items × 6,702 models). Semi-synthetic
462	    validation. GSM1K contamination gap correlation (N=33).
463	
464	    '
465	  expected_results:
466	    step1_n_items: 1319
467	    step1_n_ref: 1017
468	    step1_n_foc: 804
469	    step1_standard_c_pct: 18.9
470	    step1_external_c_pct: 47.4
471	    step1_sanity_c_pct: 0.3
472	    step1_standard_external_spearman: 0.926
473	    step2_standard_delta_tpr_p10: 0.818
474	    step2_external_delta_tpr_p10: 0.517
475	    step3_n_models: 33
476	    step3_pearson_r: -0.478
477	    step3_pearson_p: 0.005
478	    step3_spearman_rho: -0.403
479	    step3_spearman_p: 0.02
480	    step3_partial_r: -0.385
481	    step3_partial_p: 0.027
482	    step3_bca_ci_pearson:
483	    - -0.714
484	    - -0.155
485	    step3_bca_ci_spearman:
486	    - -0.687
487	    - -0.031
488	    step3_bca_ci_partial:
489	    - -0.64
490	    - -0.058
491	    step3_permutation_p: 0.014
492	    step3_cook_d_max_model: Deepseek-math-7b-rl
493	    step3_leave_one_out_r_range:
494	    - -0.537
495	    - -0.374
496	  result_rationale: '[DONE — actual registry data] GSM8K temporal DIF at 18.9% (vs
497	    MMLU 31.3%) reflects GSM8K''s more homogeneous construct (single-domain math vs
498	    57-subject MMLU) — fewer dimensions of variation means fewer items whose functioning
499	    changes across generations. Semi-synthetic ΔTPR=+0.818 confirms the detection
500	    framework ports to single-domain benchmarks with high power. Step 3 anti-correlation
501	    (r=−0.478) is the key downstream finding: models with larger GSM8K-GSM1K contamination
502	    gaps show disproportionately LOWER performance on DIF-C items. This is consistent
503	    with contamination producing surface-level gains concentrated on non-DIF items
504	    (memorized items that function uniformly across cohorts), while DIF items capture
505	    genuine capability differences that contamination cannot inflate. All BCa CIs
506	    exclude zero, and leave-one-out analysis confirms robustness to individual influential
507	    models. N=33 is honestly acknowledged as suggestive — the finding is consistent
508	    but a larger matched sample would strengthen it.
509	
510	    '
511	  tables:
512	  - name: 'Table 4: GSM8K DIF Summary'
513	    columns:
514	    - matching
515	    - C_pct
516	    - sanity_pct
517	    - ΔTPR_p10
518	    rows:
519	    - - standard (total score)
520	      - 18.9
521	      - 0.3
522	      - 0.818
523	    - - external (cross-benchmark)
524	      - 47.4
525	      - —
526	      - 0.517
527	  - name: 'Table 5: GSM1K Contamination Gap Correlation'
528	    columns:
529	    - statistic
530	    - value
531	    - p
532	    - 95% BCa CI
533	    rows:
534	    - - Pearson r
535	      - -0.478
536	      - 0.005
537	      - '[-0.714, -0.155]'
538	    - - Spearman ρ
539	      - -0.403
540	      - 0.02
541	      - '[-0.687, -0.031]'
542	    - - Partial r
543	      - -0.385
544	      - 0.027
545	      - '[-0.640, -0.058]'
546	  figures_description:
547	  - 'Fig 5: GSM1K contamination gap vs DIF-C item accuracy scatterplot (N=33) with
548	    regression line and BCa CI band'
549	  - 'Fig 6: Leave-one-out sensitivity — Pearson r under sequential model removal'
550	  analysis: 'GSM8K replication confirms semi-synthetic framework portability (Claim
551	    3). GSM1K anti-correlation provides the fourth layer of Claim 4 (downstream impact).
552	    Under best tier, reviewers treat r=−0.478 as suggestive-but-consistent rather
553	    than attacking it as underpowered — the convergent evidence (all CIs exclude zero,
554	    permutation p=0.014, leave-one-out stable) is sufficient for a discovery paper.
555	    Plan_017 redundancy result (ρ≈0.997) independently supports Claim 4 even if Step
556	    3 is discounted.
557	
558	    '
559	- name: bifactor_irt_equating_pilot
560	  plan_id: plan_005
561	  description: 'Bifactor IRT model on METABENCH MMLU (general + 57 subject factors).
562	    Anchor item selection. Fixed-parameter equating pilot.
563	
564	    '
565	  expected_results:
566	    general_factor_variance_pct: 58.3
567	    subject_specific_variance_mean_pct: 30.8
568	    residual_variance_pct: 10.9
569	    bifactor_rmsea: 0.019
570	    bifactor_cfi: 0.953
571	    bifactor_tli: 0.941
572	    unidim_rmsea: 0.035
573	    unidim_cfi: 0.882
574	    unidim_tli: 0.864
575	    n_anchor_items: 5640
576	    anchor_criteria: no DIF, rpbis>0.20, general loading>0.30
577	    within_subject_dif_after_bifactor_pct: 35.8
578	    within_subject_dif_unidim_pct: 38.1
579	    dif_reduction_from_bifactor_pp: 2.3
580	    equating_rho_general: 0.961
581	    equating_rho_subject_range:
582	    - 0.891
583	    - 0.974
584	    equating_rho_subject_below_095: 8
585	    convergence_em_iterations: 2140
586	    convergence_achieved: true
587	  result_rationale: 'Bifactor correctly identifies MMLU''s multidimensional structure
588	    — 57 subjects create substantial specific factors (31% of variance). However,
589	    DIF persists at 35.8% even after extracting subject-specific variance (only 2.3pp
590	    reduction from 38.1%), confirming that the instability is genuinely item-level,
591	    not an artifact of dimensional confounding. The general factor dominates (58%)
592	    because MMLU subjects share a common "general LLM ability" axis — models good
593	    at one subject tend to be good at others. IRT fit improves substantially (RMSEA
594	    0.035→0.019, CFI 0.88→0.95), validating that multidimensionality was the primary
595	    source of unidimensional misfit, but this improved fit does not resolve DIF. Equating
596	    at ρ=0.961 on the general factor demonstrates feasibility of anchor-based score
597	    maintenance, but 8/57 subjects fall below ρ=0.95 (small-N subjects with <50 items
598	    where anchor selection is constrained). This supports future work on benchmark
599	    maintenance but is appropriately appendix material — the finding that bifactor
600	    doesn''t resolve DIF is itself evidence for Claim 1''s robustness.
601	
602	    '
603	  tables:
604	  - name: 'Table A6: Model Fit Comparison'
605	    columns:
606	    - model
607	    - RMSEA
608	    - CFI
609	    - TLI
610	    - n_params
611	    rows:
612	    - - Unidimensional
613	      - 0.035
614	      - 0.882
615	      - 0.864
616	      - 25016
617	    - - Bifactor (1+57)
618	      - 0.019
619	      - 0.953
620	      - 0.941
621	      - 37524
622	  - name: 'Table A7: DIF Persistence After Bifactor Conditioning'
623	    columns:
624	    - conditioning
625	    - within_subject_C_pct
626	    - reduction_pp
627	    rows:
628	    - - None (unidimensional)
629	      - 38.1
630	      - —
631	    - - Bifactor general+specific
632	      - 35.8
633	      - 2.3
634	  figures_description:
635	  - 'Fig A9: Bifactor general factor loadings across 57 subjects'
636	  - 'Fig A10: Within-subject DIF C% before vs after bifactor conditioning (paired
637	    comparison)'
638	  analysis: 'Bifactor''s 2.3pp DIF reduction (~6% relative) confirms that >90% of
639	    temporal DIF is genuine item-level instability, not dimensional misfit artifact.
640	    This is the strongest possible evidence for Claim 1''s robustness to IRT model
641	    specification concerns. The equating pilot demonstrates feasibility but remains
642	    below the quality bar for a main-body claim — consistent with paper_framing''s
643	    decision to relegate this to appendix. The fit improvement (RMSEA halved) is itself
644	    valuable: it confirms the diagnosis that 98% |Lz|>2 reflects multidimensionality,
645	    not fundamental model invalidity.
646	
647	    '
648	- name: item_generation_calibration
649	  plan_id: plan_006
650	  description: 'LLM-based replacement item generation for DIF-flagged MMLU items.
651	    Prompt-based vs student-simulation difficulty estimation. Holdout validation.
652	
653	    '
654	  expected_results:
655	    n_items_generated: 500
656	    n_target_items: 250
657	    candidates_per_target: 2
658	    difficulty_rho_prompt: 0.362
659	    difficulty_rho_simulation: 0.731
660	    difficulty_rho_best_candidate: 0.793
661	    construct_alignment_expert_pct: 88.7
662	    discrimination_rpbis_rho: 0.514
663	    holdout_within_015_difficulty_pct: 83.6
664	    distractor_quality_plausible_pct: 76.2
665	    simulation_panel_n_models: 30
666	    gpu_hours_used: 164
667	  result_rationale: 'LLMs generate on-topic items reliably (89% construct alignment)
668	    because they understand MMLU subject boundaries and question formats. However,
669	    prompt-based difficulty targeting fails (ρ=0.36) because the generator lacks fine-grained
670	    knowledge of what makes an item hard for OTHER LLMs — difficulty is an emergent
671	    property of item-population interaction, not an intrinsic text feature. Student
672	    simulation (using 30 diverse models as examinees) provides empirical difficulty
673	    estimates that capture actual model behavior, achieving ρ=0.73 — approaching the
674	    r=0.75-0.82 reported in the student simulation literature (arXiv 2601.09953).
675	    Best-candidate selection from 2 options improves to ρ=0.79 by choosing the candidate
676	    closer to target difficulty. Distractor quality (76%) is the weakest link: generating
677	    plausible wrong answers for multiple-choice items requires understanding common
678	    misconceptions, which LLMs model imperfectly. This finding supports the conclusion
679	    that automated item generation is feasible but requires empirical calibration
680	    — prompt-based difficulty targeting alone is insufficient.
681	
682	    '
683	  tables:
684	  - name: 'Table A8: Difficulty Estimation Comparison'
685	    columns:
686	    - method
687	    - ρ_with_target
688	    - MAE_difficulty
689	    - coverage
690	    rows:
691	    - - Prompt-based targeting
692	      - 0.362
693	      - 0.183
694	      - 100%
695	    - - Student simulation (30 models)
696	      - 0.731
697	      - 0.094
698	      - 100%
699	    - - Best of 2 candidates
700	      - 0.793
701	      - 0.078
702	      - 100%
703	  figures_description:
704	  - 'Fig A11: Target vs estimated difficulty scatter (prompt-based vs simulation)'
705	  - 'Fig A12: Holdout validation — generated item difficulty vs empirical difficulty
706	    on new models'
707	  analysis: 'The prompt→simulation gap (ρ=0.36→0.73) is the key practical finding:
708	    empirical calibration is essential for item replacement pipelines. Appendix-appropriate:
709	    supports future benchmark regeneration work but is below the quality bar for a
710	    main-body claim (consistent with paper_framing''s decision to drop regeneration
711	    from claims). The 76% distractor quality suggests human review remains necessary
712	    for production deployment.
713	
714	    '
715	- name: cumulative_bayesian_dif
716	  plan_id: plan_007
717	  description: 'Bayesian cumulative DIF priors across 4 simulated benchmark administrations.
718	    Power accumulation for medium effects (δ=1.0).
719	
720	    '
721	  expected_results:
722	    n_administrations: 4
723	    n_per_admin: 80
724	    delta_simulated: 1.0
725	    individual_power_mean: 0.415
726	    individual_power_range:
727	    - 0.398
728	    - 0.432
729	    cumulative_power_after_2: 0.576
730	    cumulative_power_after_3: 0.718
731	    cumulative_power_after_4: 0.812
732	    fpr_across_accumulations_max: 0.048
733	    bf10_after_1: 2.14
734	    bf10_after_2: 4.83
735	    bf10_after_3: 9.27
736	    bf10_after_4: 16.7
737	    bf10_moderate_evidence_threshold: 3.0
738	    power_at_bf10_gt3_after_2: 0.648
739	    mh_individual_power_at_delta10: 0.383
740	    power_gain_cumulative_vs_individual: +0.303 (after 3)
741	  result_rationale: 'Individual MH tests at N=80, δ=1.0 have insufficient power (~0.42)
742	    — this is the "power gap" identified in phase 2 simulations (pass criterion required
743	    δ≥1.4). Bayesian updating converts individually inconclusive tests into cumulative
744	    evidence: the posterior from each administration constrains the prior for the
745	    next. After 3 administrations, cumulative power crosses 0.70 (the conventional
746	    adequate-power threshold) because the accumulated evidence from 3×80=240 effective
747	    observations exceeds what any single N=80 test provides. The Bayes factor trajectory
748	    (2.1→4.8→9.3→16.7) follows the expected log-linear accumulation under consistent
749	    DIF. FPR remains controlled (≤0.048) because the Bayesian framework naturally
750	    penalizes inconsistent evidence — items with spurious DIF in one administration
751	    but not others see their posterior regress toward the null. This addresses the
752	    practical concern that benchmark monitoring requires repeated measurement, not
753	    one-shot detection.
754	
755	    '
756	  tables:
757	  - name: 'Table A9: Cumulative Bayesian Power by Administration'
758	    columns:
759	    - n_admins
760	    - cumulative_N
761	    - power
762	    - BF10
763	    - FPR
764	    rows:
765	    - - 1
766	      - 80
767	      - 0.415
768	      - 2.14
769	      - 0.042
770	    - - 2
771	      - 160
772	      - 0.576
773	      - 4.83
774	      - 0.044
775	    - - 3
776	      - 240
777	      - 0.718
778	      - 9.27
779	      - 0.046
780	    - - 4
781	      - 320
782	      - 0.812
783	      - 16.7
784	      - 0.048
785	  figures_description:
786	  - 'Fig A13: Cumulative power curve as function of number of administrations (δ=1.0,
787	    N=80 each)'
788	  - 'Fig A14: BF₁₀ trajectory for true-DIF vs null items across 4 administrations'
789	  analysis: 'Simulation-only result (no real data). Confirms theoretical prediction
790	    that Bayesian cumulative DIF closes the power gap for medium effects. The practical
791	    implication: benchmark monitoring programs can detect δ=1.0 DIF after 3 waves
792	    of ~80 models each, even though no single wave has adequate power. Appendix-appropriate:
793	    methodological contribution for future longitudinal monitoring, not needed for
794	    current claims. Underdeveloped for main-body inclusion — needs real multi-wave
795	    data to validate.
796	
797	    '
798	- name: graceful_degradation_analysis
799	  plan_id: plan_008
800	  description: 'Progressive item replacement validity analysis. Ranking stability,
801	    score reliability, construct coverage as function of replacement rate (5-50%).
802	
803	    '
804	  expected_results:
805	    replacement_rates:
806	    - 0.05
807	    - 0.1
808	    - 0.2
809	    - 0.31
810	    - 0.5
811	    rho_at_005: 0.9993
812	    rho_at_010: 0.9984
813	    rho_at_020: 0.9968
814	    rho_at_031: 0.9951
815	    rho_at_050: 0.9912
816	    alpha_full: 0.9937
817	    alpha_at_031: 0.9882
818	    alpha_at_050: 0.9791
819	    construct_coverage_at_031: 57/57
820	    construct_coverage_at_050: 56/57
821	    construct_coverage_threshold_subjects_below_5items: 0.62
822	    validity_threshold_rho_lt_099: 0.453
823	    shr_full: 0.9934
824	    shr_at_031: 0.9881
825	    shr_at_050: 0.9763
826	    replacement_strategy: DIF-flagged items replaced by matched-difficulty anchors
827	  result_rationale: 'MMLU''s massive redundancy (12,508 items, most subjects with
828	    100+ items) provides enormous buffering against item replacement. Ranking stability
829	    at 31% replacement (ρ=0.9951) closely matches plan_017''s DIF removal result (ρ=0.997)
830	    — the slight discrepancy reflects calibration noise in replacement items vs clean
831	    removal. The curve is convex: initial replacement costs almost nothing (ρ=0.9993
832	    at 5%) because replaced items are drawn from the unstable pool (high DIF, contributing
833	    noise rather than signal). The validity threshold (ρ<0.99) is not crossed until
834	    ~45% replacement, demonstrating that even aggressive maintenance preserves benchmark
835	    validity. Construct coverage holds at 57/57 subjects through 31% because DIF items
836	    are distributed across subjects (not clustered in a few), so no subject loses
837	    all its items. Score reliability drops only 0.55pp (0.994→0.988) at 31% because
838	    Cronbach''s α is driven by total item count and inter-item correlation, both of
839	    which remain high after replacement.
840	
841	    '
842	  tables:
843	  - name: 'Table A10: Validity Degradation Under Progressive Replacement'
844	    columns:
845	    - replacement_pct
846	    - ρ_ranking
847	    - α_reliability
848	    - SHR
849	    - construct_coverage
850	    rows:
851	    - - 0
852	      - 1.0
853	      - 0.994
854	      - 0.993
855	      - 57/57
856	    - - 5
857	      - 0.999
858	      - 0.993
859	      - 0.993
860	      - 57/57
861	    - - 10
862	      - 0.998
863	      - 0.992
864	      - 0.992
865	      - 57/57
866	    - - 20
867	      - 0.997
868	      - 0.99
869	      - 0.99
870	      - 57/57
871	    - - 31
872	      - 0.995
873	      - 0.988
874	      - 0.988
875	      - 57/57
876	    - - 50
877	      - 0.991
878	      - 0.979
879	      - 0.976
880	      - 56/57
881	  figures_description:
882	  - 'Fig A15: Validity metrics as function of replacement rate (ρ, α, SHR overlaid)'
883	  - 'Fig A16: Per-subject construct coverage at 31% and 50% replacement'
884	  analysis: 'Directly supports the "instability ≠ invalidity" framing: replacing 31%
885	    of items (all DIF-flagged) preserves >99.5% of ranking information, demonstrating
886	    massive measurement redundancy. The convex degradation curve means benchmark maintainers
887	    have large headroom for item updates. Appendix-appropriate: clean supplementary
888	    result that reinforces Claim 4 (redundancy layer) without adding new claims.
889	
890	    '
891	- name: item_focused_trees
892	  plan_id: plan_009
893	  description: 'Item-Focused Trees with continuous release date covariate. Compare
894	    detection power and flexibility vs categorical MH-DIF.
895	
896	    '
897	  expected_results:
898	    n_models_with_release_date: 3412
899	    ift_significant_items_pct: 33.8
900	    ift_mh_overlap_jaccard: 0.762
901	    ift_only_items_pct: 8.3
902	    mh_only_items_pct: 5.2
903	    natural_breakpoints:
904	    - '2023-03-15'
905	    - '2023-08-22'
906	    - '2024-01-10'
907	    n_terminal_nodes: 4
908	    release_date_variable_importance: 0.71
909	    param_count_importance: 0.14
910	    training_data_size_importance: 0.09
911	    mean_dif_early_2023: 0.82
912	    mean_dif_late_2023: 1.21
913	    mean_dif_early_2024: 1.48
914	    dif_magnitude_release_date_r: 0.391
915	    gradual_drift_items_pct: 8.3
916	    sharp_transition_items_pct: 5.2
917	  result_rationale: 'IFT treats release date as a continuous covariate, revealing
918	    temporal DIF structure that categorical splits can miss. The 76% Jaccard overlap
919	    with MH confirms that the binary 2023/2024-H1 split captures most of the signal
920	    — the categorical approximation is adequate for the primary analysis. The additional
921	    8.3% IFT-only items are "gradual drifters" whose functioning changes smoothly
922	    across the timeline without a single dramatic shift — these are invisible to any
923	    binary split but accumulate meaningful DIF over the full period. Natural breakpoints
924	    (March 2023, August 2023, January 2024) likely correspond to major model release
925	    waves (Llama-2 era, post-ChatGPT proliferation, GPT-4 derivatives). The monotonic
926	    DIF magnitude increase (0.82→1.21→1.48) confirms genuine temporal trend rather
927	    than categorical artifact. Release date dominates variable importance (0.71) over
928	    model size (0.14) — WHEN matters more than HOW BIG, consistent with training data
929	    composition / contamination explaining instability rather than raw capability
930	    scaling.
931	
932	    '
933	  tables:
934	  - name: 'Table A11: IFT vs MH-DIF Detection Comparison'
935	    columns:
936	    - method
937	    - significant_items_pct
938	    - unique_items_pct
939	    - natural_breakpoints
940	    rows:
941	    - - MH categorical
942	      - 31.3
943	      - 5.2
944	      - 2023 vs 2024-H1 (manual)
945	    - - IFT continuous
946	      - 33.8
947	      - 8.3
948	      - Mar-23, Aug-23, Jan-24 (data-driven)
949	  - name: 'Table A12: IFT Variable Importance'
950	    columns:
951	    - covariate
952	    - importance
953	    - interpretation
954	    rows:
955	    - - release_date
956	      - 0.71
957	      - temporal position drives DIF
958	    - - param_count
959	      - 0.14
960	      - larger models show slightly different DIF
961	    - - training_data_size
962	      - 0.09
963	      - marginal contribution
964	  figures_description:
965	  - 'Fig A17: DIF magnitude as continuous function of release date (IFT smoothed curve)'
966	  - 'Fig A18: IFT tree structure showing natural temporal breakpoints'
967	  analysis: 'IFT provides a complementary lens: confirms the temporal DIF finding
968	    is robust to the choice of categorical split point, and reveals gradual drift
969	    items missed by binary comparison. The natural breakpoints are empirically interesting
970	    (potential link to model release waves) but not developed into a claim. Appendix-appropriate:
971	    robustness check that strengthens Claim 1 without adding complexity to the main
972	    narrative.
973	
974	    '
975	- name: architecture_stratified_dif
976	  plan_id: plan_010
977	  description: 'DIF within decoder-only-only subpopulation. Test whether architecture
978	    heterogeneity removal improves IRT fit and reduces spurious DIF.
979	
980	    '
981	  expected_results:
982	    total_models: 5227
983	    decoder_only_models: 5226
984	    decoder_only_pct: 99.98
985	    non_decoder_models: 1
986	    c_pct_full: 31.3
987	    c_pct_decoder_only: 31.3
988	    jaccard_full_vs_decoder: 1.0
989	    irt_rmsea_decoder_only: 0.033
990	    irt_rmsea_full: 0.034
991	    lz_gt2_pct_decoder_only: 97.9
992	    lz_gt2_pct_full: 98.0
993	    delta_mh_correlation_full_vs_decoder: 0.9999
994	  result_rationale: 'METABENCH MMLU is 99.98% decoder-only (5226/5227), reflecting
995	    the empirical reality that virtually all LLMs evaluated on MMLU since 2023 are
996	    autoregressive transformers. The single non-decoder model has zero statistical
997	    influence on any group-level analysis — removing it produces Jaccard=1.0 because
998	    MH chi-squared tests are robust to single-observation perturbations in large samples.
999	    IRT fit does not improve (RMSEA 0.034→0.033) because the misfit (98% |Lz|>2) is
1000	    driven by MMLU''s inherent multidimensionality (57 subjects), not architecture
1001	    heterogeneity. This result definitively dissolves the worst-case reviewer concern
1002	    about architecture confounding. The architecture homogeneity is itself an empirical
1003	    finding: the LLM evaluation ecosystem has converged on decoder-only transformers,
1004	    making architecture-based stratification unnecessary for this population. Future
1005	    benchmarks with more diverse architectures (e.g., state-space models, hybrid architectures)
1006	    would need to revisit this analysis.
1007	
1008	    '
1009	  tables:
1010	  - name: 'Table 3: Architecture Stratification'
1011	    columns:
1012	    - population
1013	    - N
1014	    - C_pct
1015	    - RMSEA
1016	    - '|Lz|>2 pct'
1017	    rows:
1018	    - - Full
1019	      - 5227
1020	      - 31.3
1021	      - 0.034
1022	      - 98.0%
1023	    - - Decoder-only
1024	      - 5226
1025	      - 31.3
1026	      - 0.033
1027	      - 97.9%
1028	  figures_description:
1029	  - 'Fig 3: Architecture composition of METABENCH MMLU (pie chart: 99.98% decoder-only)'
1030	  analysis: 'This is the most decisive robustness check in the paper: the architecture
1031	    confound concern is dissolved empirically rather than argued away theoretically.
1032	    Main-body appropriate as part of Claim 1 robustness (§4). The finding that the
1033	    LLM ecosystem is architecturally homogeneous has broader implications for psychometric
1034	    analyses of LLM benchmarks — the "examinee population" is far more homogeneous
1035	    than human testing populations, which simplifies DIF analysis but raises questions
1036	    about construct validity.
1037	
1038	    '
1039	- name: semi_synthetic_contamination_validation
1040	  plan_id: plan_011
1041	  description: 'Inject known contamination into real METABENCH response matrix. Measure
1042	    DIF detection power under controlled ground truth. Vary injection parameters.
1043	
1044	    '
1045	  expected_results:
1046	    temporal_external_tpr_p0: 0.326
1047	    temporal_external_tpr_p03: 0.548
1048	    temporal_external_tpr_p05: 0.834
1049	    temporal_external_tpr_p07: 0.99
1050	    temporal_external_tpr_p10: 1.0
1051	    temporal_external_fpr: 0.314
1052	    temporal_external_delta_tpr_p05: 0.508
1053	    temporal_external_delta_tpr_p10: 0.674
1054	    cross_subject_delta_fpr: 0.0
1055	    within_subject_fpr_inflation_p10: 0.186
1056	    ability_external_tpr_p10: 0.8
1057	    ability_external_fpr: 0.493
1058	    dose_response_monotonic: true
1059	    matching_variable_contamination_confirmed: true
1060	  result_rationale: '[DONE — actual registry data] Semi-synthetic injection into real
1061	    response matrices provides the controlled ground truth that proxy labels cannot.
1062	    ΔTPR=+0.508 at p=0.5 demonstrates that DIF detects differential contamination
1063	    when the exploitation rate is moderate — this is the core validation for the detection
1064	    claim. The dose-response curve (p=0.3→0.5→0.7→1.0 maps to ΔTPR=0.22→0.51→0.66→0.67)
1065	    confirms detection power scales with contamination intensity, as expected from
1066	    the DIF effect size formula (Δ_MH ∝ log odds ratio of correct response, which
1067	    increases with exploitation probability). Cross-subject matching eliminates FPR
1068	    inflation (ΔFPR=0.000) because the matching variable (total score on OTHER subjects)
1069	    is causally independent of contamination injected into a specific subject. Within-subject
1070	    matching shows FPR inflation (+0.186) because contaminating items in a subject
1071	    inflates total score on that subject, which contaminates the matching variable.
1072	    This distinction is a subtle but general methodological insight: any DIF application
1073	    where the matching variable can be affected by the grouping variable will show
1074	    FPR inflation.
1075	
1076	    '
1077	  tables:
1078	  - name: 'Table 6: Semi-Synthetic Detection Power (Cross-Subject Matching)'
1079	    columns:
1080	    - exploitation_p
1081	    - TPR
1082	    - ΔTPR
1083	    - FPR
1084	    - ΔFPR
1085	    rows:
1086	    - - 0.0
1087	      - 0.326
1088	      - 0.0
1089	      - 0.314
1090	      - 0.0
1091	    - - 0.3
1092	      - 0.548
1093	      - 0.222
1094	      - 0.314
1095	      - 0.0
1096	    - - 0.5
1097	      - 0.834
1098	      - 0.508
1099	      - 0.314
1100	      - 0.0
1101	    - - 0.7
1102	      - 0.99
1103	      - 0.664
1104	      - 0.314
1105	      - 0.0
1106	    - - 1.0
1107	      - 1.0
1108	      - 0.674
1109	      - 0.314
1110	      - 0.0
1111	  - name: 'Table 7: Matching Variable Comparison'
1112	    columns:
1113	    - matching
1114	    - ΔFPR_p10
1115	    - ΔTPR_p05
1116	    - FPR_inflation
1117	    rows:
1118	    - - Within-subject
1119	      - 0.186
1120	      - varies
1121	      - 'YES'
1122	    - - Cross-subject
1123	      - 0.0
1124	      - 0.508
1125	      - 'NO'
1126	  figures_description:
1127	  - 'Fig 4: Dose-response curve — ΔTPR as function of exploitation rate p'
1128	  - 'Fig 7: FPR comparison between within-subject and cross-subject matching across
1129	    injection levels'
1130	  analysis: This is the primary validation for Claim 3 (semi-synthetic framework)
1131	    and provides controlled ground truth addressing the circularity concern in Claim
1132	    2. The cross-subject matching innovation (ΔFPR=0.000) is the key methodological
1133	    contribution — it solves the matching variable contamination problem that plagues
1134	    within-subject DIF when the conditioning variable is endogenous. Main-body material
1135	    for §4.
1136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9067e43-7ae9-4866-97cb-66b38b10abc4",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "72cafeee-8016-4ddc-a294-1416e0585a20",
  "sourceToolAssistantUUID": "b9067e43-7ae9-4866-97cb-66b38b10abc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T05:33:31.794Z_

I now have a comprehensive understanding of the paper. Let me check the dream_id and tier more carefully, then produce and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72cafeee-8016-4ddc-a294-1416e0585a20",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjCpAcHNPZNVKtV2dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "278243b8-4060-4ce1-a552-974d36699a60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsfgMCF7rSso4jPmhw9iJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16346,
      "cache_read_input_tokens": 46566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16346,
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

_source line 51 · 2026-05-21T05:33:35.743Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011gB4EokYYnKusNfH8R6eTX`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/review_report.md | head -1",
  "description": "Check if a review already exists for best tier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "278243b8-4060-4ce1-a552-974d36699a60",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjCpAcHNPZNVKtV2dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18a6edd4-958b-4c5b-af2e-6bf287250c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsfgMCF7rSso4jPmhw9iJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16346,
      "cache_read_input_tokens": 46566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16346,
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

_source line 52 · 2026-05-21T05:33:35.812Z_

<details><summary>↩ Tool result · `toolu_011gB4EokYYnKusNfH8R6eTX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a6edd4-958b-4c5b-af2e-6bf287250c43",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "23c10c3e-68d9-47f3-9784-dd593c5532e2",
  "sourceToolAssistantUUID": "18a6edd4-958b-4c5b-af2e-6bf287250c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T05:33:36.596Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016B46Q4N4QyNzSP6hovkuTk`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/median/ /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/worst/",
  "description": "Check median and worst tier contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23c10c3e-68d9-47f3-9784-dd593c5532e2",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjCpAcHNPZNVKtV2dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fd3bc88-5717-40ab-aaf4-3b6179c3adab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsfgMCF7rSso4jPmhw9iJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16346,
      "cache_read_input_tokens": 46566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16346,
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

_source line 54 · 2026-05-21T05:33:36.649Z_

<details><summary>↩ Tool result · `toolu_016B46Q4N4QyNzSP6hovkuTk`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/median/:
experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_e90a5c14.pdf
review_report.md

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/worst/:
experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_f5f46a62.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fd3bc88-5717-40ab-aaf4-3b6179c3adab",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "f3f35d7f-200e-4fc4-b5b7-6794ba6002f4",
  "sourceToolAssistantUUID": "3fd3bc88-5717-40ab-aaf4-3b6179c3adab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-21T05:33:40.793Z_

The worst tier does not yet have a `review_report.md`. Let me check which tiers already have reviews and determine which tier I should submit for. Let me also read the existing reviews to understand the reviewing context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f35d7f-200e-4fc4-b5b7-6794ba6002f4",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjtdZVRhAf6RqUEfbV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "690bfacb-b459-42e8-b022-07b18168b245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pMqiLjPZWYpNi88CwnJzU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 62912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 56 · 2026-05-21T05:33:41.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SmTedkVz2eMSihcAApqLVj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/review_report.md",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690bfacb-b459-42e8-b022-07b18168b245",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjtdZVRhAf6RqUEfbV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2d1e6b3-ab29-41fc-a958-7eb0e2b066cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pMqiLjPZWYpNi88CwnJzU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 62912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 57 · 2026-05-21T05:33:41.818Z_

<details><summary>↩ Tool result · `toolu_01SmTedkVz2eMSihcAApqLVj`</summary>

```text
1	---
2	dream_id: dream_20260521T042647
3	tier: best
4	overall_score: 6 - Weak Accept
5	timestamp: 2026-05-21T05:19:39.657621+00:00
6	---
7	
8	# Dream Review Report: Temporal Item Instability in LLM Benchmarks
9	
10	**Paper**: "Temporal Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU"
11	
12	**Venue**: ICLR 2026 | **Rating scale**: {0, 2, 4, 6, 8, 10}
13	
14	---
15	
16	## Panel
17	
18	| Reviewer | Focus | Preliminary | Post-Roundtable |
19	|----------|-------|-------------|-----------------|
20	| R1 | Methodology + Experiments | 6 (Weak Accept) | 6 (Weak Accept) |
21	| R2 | Novelty + Related Work | 4 (Weak Reject) | 5 → rounds to 6 under {0,2,4,6,8,10} |
22	
23	**Consolidated Overall Score: 6 — Marginally Above Acceptance Threshold (Weak Accept)**
24	
25	---
26	
27	## 1. Paper Summary
28	
29	The paper applies Mantel–Haenszel Differential Item Functioning (MH-DIF) analysis from educational psychometrics to the METABENCH MMLU response matrix (5,227 models × 12,508 items). It finds that 31.3% of MMLU items exhibit large temporal DIF (ETS Category C, |Δ_MH| ≥ 1.5) between 2023 and 2024-H1 model cohorts. Four claims are advanced: (1) an empirical discovery of temporal item instability robust across thresholds and not driven by capability gains; (2) a meta-critique arguing web-overlap contamination labels measure global exposure, not differential contamination; (3) a semi-synthetic validation framework with cross-subject matching that eliminates FPR inflation; and (4) DIF as a diagnostic lens — DIF items resist contamination-based gains and are the least disruptive items for non-random removal.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2d1e6b3-ab29-41fc-a958-7eb0e2b066cb",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "6d6be262-caf0-404e-b21b-51ef1daf7ffd",
  "sourceToolAssistantUUID": "f2d1e6b3-ab29-41fc-a958-7eb0e2b066cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T05:33:42.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SiRA2RnpiTKeAifCWPkweC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/median/review_report.md",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d6be262-caf0-404e-b21b-51ef1daf7ffd",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAjtdZVRhAf6RqUEfbV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51f03726-1d7c-4cd5-9810-c87922a0cd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pMqiLjPZWYpNi88CwnJzU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 62912,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 62912,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 662,
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

_source line 59 · 2026-05-21T05:33:42.242Z_

<details><summary>↩ Tool result · `toolu_01SiRA2RnpiTKeAifCWPkweC`</summary>

```text
1	---
2	dream_id: dream_20260521T042647
3	tier: median
4	overall_score: borderline accept (6/10)
5	timestamp: 2026-05-21T05:28:53.105365+00:00
6	---
7	
8	# Dream Review Report — Full Roundtable
9	
10	**Paper**: "Temporal Differential Item Functioning Reveals 31% Measurement Instability in MMLU: A Psychometric Audit of 5,227 Language Models"
11	
12	**Review Mode**: Full (2 Reviewers, 4-step roundtable)
13	**Target Venue**: ICLR (1-10 scale)
14	**Date**: 2026-05-21
15	
16	---
17	
18	## Roundtable Summary
19	
20	| Criterion | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
21	|-----------|--------------------------|---------------------------|-----------|
22	| Overall | 6 | 6 | **6** |
23	| Soundness | 3/4 | 3/4 | **3/4** |
24	| Presentation | 3/4 | 3/4 | **3/4** |
25	| Contribution | 3/4 | 2/4 | **2.5/4** |
26	| Confidence | 4/5 | 4/5 | 4/5 |
27	
28	**Consensus verdict**: Marginally above acceptance threshold. Genuine contributions in ground truth meta-critique and cross-subject matching methodology, but technical contribution is thin (unmodified classical method applied to new domain) and the flagship 31% finding lacks mechanistic decomposition. Honest negative result reporting and careful framing elevate the paper above the typical borderline submission. Likely needs a champion AC.
29	
30	---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51f03726-1d7c-4cd5-9810-c87922a0cd43",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "4fd14413-5bc1-4c71-89f3-ad668eba2959",
  "sourceToolAssistantUUID": "51f03726-1d7c-4cd5-9810-c87922a0cd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-21T05:33:45.879Z_

Now I understand the context. The worst tier still needs its review. I'm assigned as R2 (Novelty/Significance + Related Work/Positioning) for this dream round. Let me produce the review for the worst tier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fd14413-5bc1-4c71-89f3-ad668eba2959",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAkH3gt37TvTmhi6fTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a60cdaf8-727c-494e-9337-d9a5d0c24c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbFozr4LDNEacGKqPTuv3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 63574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1388,
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

_source line 61 · 2026-05-21T05:33:48.149Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Upe6AJqhk2wiSyiM3RJa9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60cdaf8-727c-494e-9337-d9a5d0c24c19",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAkH3gt37TvTmhi6fTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a1d208d-8d0e-4d36-a04a-d7e207e5c35d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbFozr4LDNEacGKqPTuv3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 63574,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1388
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 63574,
          "cache_creation_input_tokens": 1388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1388,
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

_source line 62 · 2026-05-21T05:33:48.460Z_

<details><summary>↩ Tool result · `toolu_01Upe6AJqhk2wiSyiM3RJa9P`</summary>

```text
1	narrative_guidance: 'Reframe from "DIF reveals benchmark structural problems" to "Empirical
2	  characterization of measurement stability in LLM benchmarks: challenges and an open
3	  framework." Three pivots, same venue: (1) Lead with semi-synthetic validation framework
4	  (Claim 3) as primary methodological contribution — ΔTPR methodology + cross-subject
5	  matching (ΔFPR=0.000) is genuinely novel, reusable. (2) Reposition Claim 1 as case
6	  study motivating the framework, not headline finding. Report MH AND SIBTEST jointly;
7	  present discrepancy as "characterizing which DIF types matter" rather than defending
8	  a single 31% number. Instability becomes "≥18-31% depending on DIF type and threshold"
9	  — a range, not a point estimate. (3) Drop GSM1K correlation entirely from main paper.
10	  Strengthen circularity ablation and redundancy finding (ρ≈0.997). Ground truth meta-critique
11	  survives intact — make it more prominent. Add "Practitioner''s Guide" section. Target
12	  remains ICLR 2027.
13	
14	  '
15	imagined_experiments:
16	- name: real_data_dif_mmlu
17	  plan_id: plan_001
18	  description: 'MH-DIF on METABENCH MMLU (5,219 models × 12,508 items). Temporal,
19	    ability, within-family cohorts. Proxy validation against Li et al. labels. Domain-specificity
20	    analysis. SIBTEST robustness check added as worst-case critical experiment.
21	
22	    '
23	  expected_results:
24	    temporal_ets_c_pct: 31.3
25	    temporal_fpr_li_clean: 0.318
26	    temporal_enrichment: 0.96
27	    ability_ets_c_pct: 2.9
28	    ability_enrichment: 1.19
29	    within_family_llama2v3_c_pct: 61.3
30	    within_family_mistral_mixtral_c_pct: 38.7
31	    domain_spearman_rho: 0.307
32	    domain_spearman_p: 0.02
33	    sanity_random_split_c_pct: 0.18
34	    temporal_ability_jaccard: 0.014
35	    sibtest_nonuniform_additional_pct: 22.4
36	    mh_sibtest_flag_jaccard: 0.48
37	    sibtest_total_flagged_pct: 44.7
38	    sibtest_only_flags_pct: 13.4
39	    mh_only_flags_pct: 8.9
40	    sibtest_crossing_dif_items: 1674
41	  result_rationale: 'MH结果本身不变（已有实际数据），但SIBTEST揭示了致命弱点：22.4%的items存在MH完全 遗漏的非均匀DIF（non-uniform/crossing
42	    DIF），即不同能力水平的模型在这些items上 表现出相反方向的DIF效应。MH只检测均匀位移，当DIF效应在能力谱上方向翻转时，正负 抵消导致Δ_MH≈0，这些items被MH判为clean。Jaccard=0.48说明两种方法标记的items重叠
43	    不到一半——31%这个数字高度依赖于方法选择。1,674个crossing DIF items意味着MMLU中 存在大量"对弱模型变难但对强模型变易"（或反过来）的items，这种模式与contamination
44	    的差异化机制高度一致（强模型更可能通过训练数据暴露获益），但MH的均匀性假设恰好 将其mask掉。这直接动摇了"31%作为精确估计"的可信度——真实instability可能在18%到
45	    45%之间，取决于使用哪种DIF方法和哪个阈值。within-family分析中Llama-2 vs Llama-3 的61.3% C%进一步证实大量DIF反映的是capability
46	    gain而非contamination。
47	
48	    '
49	  tables:
50	  - name: MH vs SIBTEST Flag Comparison (Temporal Cohort)
51	    columns:
52	    - Method
53	    - C_items
54	    - C_pct
55	    - Unique_flags
56	    - Unique_pct
57	    rows:
58	    - - MH (|Δ_MH|≥1.5)
59	      - 3918
60	      - 31.3
61	      - 1112
62	      - 8.9
63	    - - SIBTEST (β̂≥0.088)
64	      - 5592
65	      - 44.7
66	      - 1674
67	      - 13.4
68	    - - Intersection
69	      - 2806
70	      - 22.4
71	      - —
72	      - —
73	    - - Union
74	      - 6584
75	      - 52.7
76	      - —
77	      - —
78	  - name: SIBTEST Non-uniform DIF by Subject Cluster
79	    columns:
80	    - Subject_Cluster
81	    - N_items
82	    - Crossing_DIF_pct
83	    - MH_missed_pct
84	    rows:
85	    - - STEM_quantitative
86	      - 2841
87	      - 28.3
88	      - 18.7
89	    - - STEM_conceptual
90	      - 1953
91	      - 19.1
92	      - 11.2
93	    - - Humanities
94	      - 3287
95	      - 24.6
96	      - 14.8
97	    - - Social_sciences
98	      - 2614
99	      - 21.0
100	      - 12.1
101	    - - Professional
102	      - 1813
103	      - 17.4
104	      - 9.6
105	  figures_description:
106	  - 'Fig 1: Scatter plot of MH Δ_MH vs SIBTEST β̂ for all 12,508 items. Four quadrants:
107	    MH+/SIBTEST+ (overlap), MH+/SIBTEST- (MH-only), MH-/SIBTEST+ (SIBTEST-only, i.e.
108	    crossing DIF), MH-/SIBTEST- (clean). Large cloud of 1,674 items in MH-/SIBTEST+
109	    quadrant demonstrates substantial crossing DIF invisible to MH. Color-coded by
110	    subject cluster.'
111	  - 'Fig 2: Item characteristic curves for 6 exemplar crossing-DIF items showing DIF
112	    direction reversal at mid-ability range. Reference (2023) and focal (2024-H1)
113	    curves cross, producing near-zero Δ_MH but large SIBTEST β̂. These items literally
114	    changed meaning across cohorts — easy items became hard for weak models but easier
115	    for strong models.'
116	  analysis: 'SIBTEST结果对paper是结构性打击。31%不再是一个可靠的点估计——它是MH特异性的产物。 真实instability范围是18-45%（取决于方法和阈值），这使得任何基于31%的下游推断都变得
117	    模糊。对于worst tier reframe：(1)将MH和SIBTEST结果并列报告，承认"instability范围 ≥18-31%依赖于DIF类型和阈值"而非捍卫单一数字；(2)crossing
118	    DIF的发现本身是有价值的 empirical contribution——"MMLU items不仅在难度上漂移，还在区分功能上发生方向性变化"； (3)这motivates更复杂的DIF方法（logistic
119	    regression DIF, MIMIC）作为future work。 但reviewer会说"如果你自己的robustness check否定了headline
120	    number，为什么我们应该 相信这篇paper的任何具体数字？"
121	
122	    '
123	- name: rl_robustness_validation
124	  plan_id: plan_002
125	  description: '验证DIF对RL训练的鲁棒性。SFT基线、alignment-RL (DPO/ORPO, N=477)、 reasoning-RL
126	    (GRPO/PPO, 10-15 models)。群体级DIF稳定性+个体级传统检测器对比。
127	
128	    '
129	  expected_results:
130	    n_reasoning_rl_models: 13
131	    n_sft_baseline: 312
132	    n_alignment_rl: 477
133	    dif_flag_jaccard_sft_vs_alignrl: 0.71
134	    dif_flag_jaccard_sft_vs_reasonrl_mixed: 0.58
135	    dif_flag_jaccard_alignrl_vs_reasonrl_mixed: 0.62
136	    auroc_dif_sft: 0.82
137	    auroc_dif_alignrl: 0.79
138	    auroc_dif_reasonrl_mixed: 0.64
139	    auroc_constat_sft: 0.74
140	    auroc_constat_alignrl: 0.68
141	    auroc_constat_reasonrl: 0.52
142	    auroc_mink_sft: 0.71
143	    auroc_mink_alignrl: 0.63
144	    auroc_mink_reasonrl: 0.41
145	    delong_dif_vs_constat_sft_p: 0.12
146	    delong_dif_vs_constat_reasonrl_p: 0.08
147	    tost_equivalence_dif_sft_alignrl_p: 0.03
148	    tost_equivalence_dif_sft_reasonrl_p: 0.31
149	    detection_boundary_exploitation_rate: 0.65
150	    bootstrap_ci_auroc_dif_reasonrl:
151	    - 0.41
152	    - 0.84
153	    power_at_p04: 0.18
154	    power_at_p07: 0.51
155	    power_at_p10: 0.64
156	  result_rationale: 'N=13 reasoning-RL模型是致命瓶颈。当13个GRPO/PPO模型混入focal cohort时，cohort
157	    总N仍≥80（满足DIF统计要求），但这些模型的contamination-masking效应使得DIF flag 集合发生实质性漂移（Jaccard从0.71降至0.58）。关键问题：AUROC在reasoning-RL条件下
158	    降至0.64，bootstrap CI极宽[0.41, 0.84]——无法排除DIF在RL场景下接近random的可能。 TOST等价检验失败（p=0.31>>0.05），无法声称DIF对reasoning-RL是等价的。传统检测器
159	    确实退化更多（ConStat 0.74→0.52, Min-K% 0.71→0.41），但DIF的退化也不小 （0.82→0.64），且DeLong检验p=0.08——差异不显著。这意味着"DIF对RL鲁棒"的声明
160	    在统计上站不住脚。power analysis显示detection boundary在p≈0.65——只有>65% exploitation rate的contamination才能被检测到，这在实际中覆盖面有限。
161	    整体结论：DIF比传统方法更robust是趋势性的，但N=13使得任何定量声明都不可信。
162	
163	    '
164	  tables:
165	  - name: Detection Performance by Cohort Composition
166	    columns:
167	    - Detector
168	    - SFT_AUROC
169	    - AlignRL_AUROC
170	    - ReasonRL_AUROC
171	    - Δ_SFT→ReasonRL
172	    rows:
173	    - - DIF (MH)
174	      - 0.82
175	      - 0.79
176	      - 0.64
177	      - -0.18
178	    - - ConStat
179	      - 0.74
180	      - 0.68
181	      - 0.52
182	      - -0.22
183	    - - Min-K%
184	      - 0.71
185	      - 0.63
186	      - 0.41
187	      - -0.3
188	  - name: DIF Flag Stability Across Cohort Compositions
189	    columns:
190	    - Comparison
191	    - Jaccard
192	    - New_flags
193	    - Lost_flags
194	    rows:
195	    - - SFT vs AlignRL
196	      - 0.71
197	      - 412
198	      - 287
199	    - - SFT vs SFT+ReasonRL
200	      - 0.58
201	      - 893
202	      - 614
203	    - - AlignRL vs AlignRL+ReasonRL
204	      - 0.62
205	      - 731
206	      - 508
207	  - name: TOST Equivalence Tests (Δ AUROC ≤ 0.10)
208	    columns:
209	    - Comparison
210	    - Δ_AUROC
211	    - TOST_p
212	    - Equivalent
213	    rows:
214	    - - 'DIF: SFT vs AlignRL'
215	      - 0.03
216	      - 0.03
217	      - 'Yes'
218	    - - 'DIF: SFT vs ReasonRL'
219	      - 0.18
220	      - 0.31
221	      - 'No'
222	    - - 'ConStat: SFT vs ReasonRL'
223	      - 0.22
224	      - 0.44
225	      - 'No'
226	  figures_description:
227	  - 'Fig: Detection power (TPR at FPR=0.10) as function of exploitation rate p∈[0.3,1.0]
228	    for three cohort compositions. SFT curve reaches TPR=0.68 at p=0.5; ReasonRL-mixed
229	    curve only reaches TPR=0.51 at p=0.7. Shaded bootstrap 95% CIs show massive uncertainty
230	    for ReasonRL curve due to N=13.'
231	  analysis: '实验的根本问题是sample size。N=13 reasoning-RL模型不足以支撑任何统计推断—— 这不是"underpowered"可以轻描淡写的，而是使结论完全不可信。worst
232	    tier下reviewer 会直接说"你声称DIF对RL robust但你只有13个RL模型，CI覆盖从random到excellent， 这不是evidence而是noise"。对于reframe：将RL
233	    robustness完全降级到limitations/ future work，不在main claims中出现。承认"RL robustness是open
234	    question，现有 METABENCH中reasoning-RL模型不足以验证"。这反而增强了paper的诚实度。
235	
236	    '
237	- name: constat_perturbation_eval
238	  plan_id: plan_003a
239	  description: 'ConStat-style perturbation testing独立评估。200+ MMLU items语义等价改写， FDR-controlled
240	    detection，与DIF对比。
241	
242	    '
243	  expected_results:
244	    n_items_reformulated: 237
245	    n_models_tested: 48
246	    constat_detection_rate_non_rl: 0.34
247	    constat_detection_rate_rl: 0.11
248	    constat_fdr_controlled_rate: 0.28
249	    constat_fpr: 0.067
250	    constat_auroc_non_rl: 0.78
251	    constat_auroc_rl: 0.54
252	    dif_auroc_same_items: 0.73
253	    dif_constat_overlap_flagged: 0.31
254	    paraphrase_quality_human_eval: 0.82
255	    paraphrase_semantic_sim: 0.91
256	    effect_size_non_rl_mean_d: 0.87
257	    effect_size_rl_mean_d: 0.34
258	  result_rationale: 'ConStat在per-model detection上展现出DIF不具备的粒度优势：它可以指出具体哪个模型 在哪些items上表现异常（FPR=0.067远低于DIF的temporal
259	    baseline 0.31）。在non-RL 模型上AUROC=0.78略高于DIF的0.73（同一items子集），这使得reviewer有理由质疑 "为什么不直接用ConStat而要用这个baseline
260	    FPR=31%的老方法？"。RL条件下ConStat 确实退化严重（0.78→0.54），但DIF在worst tier下也退化（plan_002: 0.82→0.64），
261	    差异不如expected那么戏剧性。关键攻击点：ConStat的FPR（0.067）比DIF temporal的 FPR（0.31）低一个数量级——reviewer会问"你的方法31%的items被flagged作为baseline，
262	    另一个方法只有6.7% false positive，哪个更可信？"。overlap仅0.31说明两种方法 检测的是根本不同的信号——这在worst tier下被解读为"DIF检测的不是contamination
263	    而是别的什么东西"。
264	
265	    '
266	  tables:
267	  - name: ConStat vs DIF Detection Comparison
268	    columns:
269	    - Metric
270	    - ConStat
271	    - DIF (MH)
272	    - Advantage
273	    rows:
274	    - - AUROC (non-RL)
275	      - 0.78
276	      - 0.73
277	      - ConStat +0.05
278	    - - AUROC (RL)
279	      - 0.54
280	      - 0.64
281	      - DIF +0.10
282	    - - FPR
283	      - 0.067
284	      - 0.314
285	      - ConStat ×4.7 better
286	    - - Per-model granularity
287	      - 'Yes'
288	      - 'No'
289	      - ConStat
290	    - - Flag overlap (Jaccard)
291	      - —
292	      - —
293	      - 0.31
294	  figures_description:
295	  - 'Fig: ROC curves for ConStat and DIF on the 237 reformulated items, split by RL/non-RL
296	    model subgroups. ConStat curve dominates DIF in low-FPR regime for non-RL models;
297	    DIF has slight advantage in high-recall regime for RL models.'
298	  analysis: 'ConStat结果对DIF-as-contamination-detector叙事构成直接竞争。在non-RL场景下ConStat 更精确（低FPR）且粒度更细（per-model），这使得DIF在contamination
299	    detection赛道上 处于劣势。但这实际上支持了worst tier的reframe方向：DIF不应该定位为contamination detector，而是benchmark
300	    stability characterization工具——两者检测的是不同信号 （ConStat检测specific model anomaly，DIF检测cross-cohort
301	    item property shift）。 Reframe后ConStat变成complementary baseline而非competing method。
302	
303	    '
304	- name: dvd_generation_variance_eval
305	  plan_id: plan_003b
306	  description: 'DVD generation variance独立评估。10-15个open-weight模型，50 responses/item，
307	    generation variance scores，bimodal distribution检测。
308	
309	    '
310	  expected_results:
311	    n_models_tested: 12
312	    n_items_tested: 500
313	    responses_per_item: 50
314	    dvd_auroc_verbatim: 0.69
315	    dvd_auroc_variant: 0.58
316	    dvd_fpr: 0.089
317	    dvd_bimodal_detection_rate: 0.23
318	    dvd_effect_size_verbatim_d: 0.74
319	    dvd_effect_size_variant_d: 0.41
320	    dvd_dif_overlap_flagged: 0.19
321	    gpu_hours_used: 63
322	    temperature_sensitivity_t07_auroc: 0.69
323	    temperature_sensitivity_t10_auroc: 0.62
324	  result_rationale: 'DVD的per-model generation variance检测在verbatim contamination上表现中等
325	    （AUROC=0.69），variant contamination上较弱（0.58）。与DIF的flag overlap极低 （0.19），再次表明不同方法检测不同类型的信号。DVD的核心假设——contaminated
326	    items 产生bimodal response分布——在实际LLM上只有23%的known-contaminated items表现出 明显bimodality，这是因为现代LLM在temperature=0.7时already
327	    highly consistent， contamination造成的额外consistency增量很小。GPU cost=63hrs使其成为expensive的
328	    detection method（DIF是zero GPU cost）。在worst tier下，DVD结果是"another incomplete signal"——既不强到取代DIF，也不弱到让DIF显得indispensable，陷入
329	    "所有方法都partially work"的尴尬叙事。
330	
331	    '
332	  tables:
333	  - name: DVD Detection by Contamination Type
334	    columns:
335	    - Contamination_Type
336	    - N_items
337	    - AUROC
338	    - Bimodal_pct
339	    - Effect_d
340	    rows:
341	    - - Verbatim
342	      - 127
343	      - 0.69
344	      - 31.5
345	      - 0.74
346	    - - Variant
347	      - 89
348	      - 0.58
349	      - 12.4
350	      - 0.41
351	    - - Clean
352	      - 284
353	      - —
354	      - 4.2
355	      - —
356	  - name: DVD vs DIF Signal Comparison
357	    columns:
358	    - Metric
359	    - DVD
360	    - DIF
361	    - Overlap_Jaccard
362	    rows:
363	    - - Items flagged
364	      - 94
365	      - 157
366	      - 0.19
367	    - - FPR
368	      - 0.089
369	      - 0.314
370	      - —
371	    - - Detection granularity
372	      - per-model
373	      - per-cohort
374	      - —
375	  figures_description:
376	  - 'Fig: Violin plots of generation variance scores for clean vs verbatim-contaminated
377	    vs variant-contaminated items across 12 models. Distributions heavily overlap
378	    for variant contamination, showing DVD''s limited discriminative power for non-verbatim
379	    contamination.'
380	  analysis: 'DVD结果确认了generation variance作为contamination signal的局限性——在variant contamination（更现实的场景）上几乎失效。但这不直接伤害DIF叙事，因为DVD和DIF
381	    检测的是完全不同的信号（Jaccard=0.19）。在worst tier reframe中，DVD结果变成 "motivating example for
382	    why single-signal detection is insufficient"——但由于 ensemble（plan_003c）也不work well，这个motivating
383	    example没有resolution。
384	
385	    '
386	- name: ensemble_fusion
387	  plan_id: plan_003c
388	  description: 'DIF + ConStat + DVD三信号融合。阈值校准，majority voting，weighted fusion， 5-fold
389	    cross-validation。
390	
391	    '
392	  expected_results:
393	    ensemble_2of3_auroc: 0.72
394	    ensemble_weighted_auroc: 0.76
395	    ensemble_fpr: 0.112
396	    best_single_signal_auroc: 0.78
397	    ensemble_vs_best_single_delong_p: 0.38
398	    ensemble_coverage_high_delta: 0.81
399	    ensemble_coverage_low_delta: 0.43
400	    ensemble_coverage_rl: 0.48
401	    cv_fold_variance_auroc: 0.034
402	    uniform_weight_auroc: 0.71
403	    optimized_weight_dif: 0.28
404	    optimized_weight_constat: 0.47
405	    optimized_weight_dvd: 0.25
406	    fpr_above_010_configs: 3
407	    total_configs_tested: 8
408	  result_rationale: 'Ensemble的核心承诺是"coverage handoff"——DIF覆盖high-delta，ConStat覆盖non-RL
409	    medium-delta，DVD覆盖variant。但实际融合结果令人失望：weighted AUROC=0.76低于 ConStat单独的0.78，DeLong
410	    p=0.38表明ensemble没有统计显著地超越最佳单信号。 这是因为三个信号的correlation structure不利于融合：DIF和ConStat在某些items上
411	    产生contradictory signals（DIF flag但ConStat clean，或反过来），majority voting 在这种情况下倾向于conservative（2-of-3需要agreement），而weighted
412	    fusion的 DIF权重被压低到0.28（反映其高baseline FPR降低了fusion中的信息价值）。 FPR=0.112超过了0.10目标阈值（3/8
413	    configurations）。CV fold variance=0.034 说明权重unstable。在worst tier下，ensemble failure是"the
414	    punchline that never lands"——paper承诺了complementary detection但deliver的是noise averaging。
415	    Reviewer会说"如果ensemble不比单方法好，为什么这是一个contribution？"
416	
417	    '
418	  tables:
419	  - name: Ensemble vs Individual Signal Performance
420	    columns:
421	    - Method
422	    - AUROC
423	    - FPR
424	    - Coverage_δ≥1.4
425	    - Coverage_δ<1.0
426	    rows:
427	    - - DIF alone
428	      - 0.73
429	      - 0.314
430	      - 0.79
431	      - 0.22
432	    - - ConStat alone
433	      - 0.78
434	      - 0.067
435	      - 0.61
436	      - 0.48
437	    - - DVD alone
438	      - 0.69
439	      - 0.089
440	      - 0.54
441	      - 0.37
442	    - - Ensemble (2-of-3)
443	      - 0.72
444	      - 0.048
445	      - 0.52
446	      - 0.31
447	    - - Ensemble (weighted)
448	      - 0.76
449	      - 0.112
450	      - 0.81
451	      - 0.43
452	  - name: Cross-Validation Stability
453	    columns:
454	    - Fold
455	    - AUROC
456	    - w_DIF
457	    - w_ConStat
458	    - w_DVD
459	    rows:
460	    - - 1
461	      - 0.79
462	      - 0.31
463	      - 0.44
464	      - 0.25
465	    - - 2
466	      - 0.74
467	      - 0.22
468	      - 0.52
469	      - 0.26
470	    - - 3
471	      - 0.78
472	      - 0.35
473	      - 0.41
474	      - 0.24
475	    - - 4
476	      - 0.72
477	      - 0.19
478	      - 0.53
479	      - 0.28
480	    - - 5
481	      - 0.77
482	      - 0.33
483	      - 0.45
484	      - 0.22
485	  figures_description:
486	  - 'Fig: Coverage heatmap showing which contamination types (verbatim/variant × RL/non-RL
487	    × effect size bins) are detected by each signal and their combinations. Large
488	    gap in variant+RL quadrant where no method exceeds AUROC=0.50.'
489	  analysis: 'Ensemble failure在worst tier叙事中有两种解读：(1)消极——DIF不是一个有价值的 ensemble component，整个multi-signal方向是dead
490	    end；(2)积极（reframe后）—— 这说明contamination detection fundamentally不能通过简单signal combination解决，
491	    需要新方法论。但后者是一个non-result dressed up as insight，reviewer不会buy。 对于reframe：将ensemble完全移到appendix/future
492	    work，main paper不再声称 detection improvement，而是聚焦于characterization和framework贡献。
493	
494	    '
495	- name: cross_benchmark_gsm8k
496	  plan_id: plan_004
497	  description: 'GSM8K DIF复制 + GSM1K ground truth验证。Temporal DIF on 1,319 items × 6,702
498	    models。Semi-synthetic validation。GSM1K correlation with difficulty control。
499	
500	    '
501	  expected_results:
502	    step1_gsm8k_temporal_dif:
503	      n_items: 1319
504	      n_ref: 1017
505	      n_foc: 804
506	      standard_c_pct: 18.9
507	      external_c_pct: 47.4
508	      sanity_c_pct: 0.3
509	    step2_semi_synthetic:
510	      standard_delta_tpr_p10: 0.818
511	      external_delta_tpr_p10: 0.517
512	    step3_gsm1k_correlation:
513	      n_models: 33
514	      pearson_r: -0.478
515	      pearson_p: 0.005
516	      spearman_rho: -0.403
517	      spearman_p: 0.02
518	      partial_r_controlling_accuracy: -0.385
519	      partial_p: 0.027
520	      partial_r_controlling_difficulty: -0.08
521	      partial_p_difficulty: 0.67
522	      partial_r_controlling_accuracy_and_difficulty: 0.03
523	      partial_p_acc_diff: 0.87
524	      difficulty_control_ci_lower: -0.31
525	      difficulty_control_ci_upper: 0.15
526	      permutation_p_difficulty_controlled: 0.64
527	      dif_item_mean_difficulty: 0.38
528	      non_dif_item_mean_difficulty: 0.61
529	      difficulty_dif_correlation: -0.52
530	  result_rationale: 'Step 1和Step 2的结果不变（已有实际数据），关键崩塌发生在Step 3的difficulty control。
531	    原始r=-0.478看似strong，但DIF-C items系统性地更难（mean p-value=0.38 vs 0.61）， difficulty与DIF-C
532	    flag的correlation=-0.52。当控制item difficulty后，partial r从-0.385骤降至-0.08（p=0.67），CI=[-0.31,
533	    0.15]稳固包含零。同时控制accuracy 和difficulty后，r→0.03（essentially zero）。这意味着原始correlation完全由
534	    confound驱动：DIF flags harder items → harder items have larger contamination gaps
535	    (floor effect) → spurious negative correlation。这不是DIF-C items "resist contamination"
536	    而是 "DIF-C items are harder, and harder items have smaller accuracy differences
537	    between GSM8K and GSM1K regardless of contamination"。 N=33的小样本加剧了问题——控制一个confound就吃掉所有degrees
538	    of freedom。 Sub-finding 4（DIF items resist contamination-based gains）在difficulty
539	    control下彻底死亡。
540	
541	    '
542	  tables:
543	  - name: GSM1K Correlation Under Progressive Controls
544	    columns:
545	    - Model
546	    - r
547	    - p
548	    - 95% CI
549	    - Interpretation
550	    rows:
551	    - - Bivariate
552	      - -0.478
553	      - 0.005
554	      - '[-0.71, -0.16]'
555	      - Significant
556	    - - Partial (acc)
557	      - -0.385
558	      - 0.027
559	      - '[-0.64, -0.06]'
560	      - Significant
561	    - - Partial (difficulty)
562	      - -0.08
563	      - 0.67
564	      - '[-0.31, 0.15]'
565	      - Non-significant
566	    - - Partial (acc+difficulty)
567	      - 0.03
568	      - 0.87
569	      - '[-0.22, 0.28]'
570	      - 'Null'
571	  - name: DIF-C vs Non-DIF Item Difficulty
572	    columns:
573	    - Item_Group
574	    - N
575	    - Mean_p_value
576	    - SD
577	    - Mean_discrimination
578	    rows:
579	    - - DIF-C
580	      - 249
581	      - 0.38
582	      - 0.21
583	      - 0.42
584	    - - Non-DIF
585	      - 1070
586	      - 0.61
587	      - 0.24
588	      - 0.39
589	    - - t-test p
590	      - —
591	      - <0.001
592	      - —
593	      - 0.34
594	  figures_description:
595	  - 'Fig: Two panels. Left: scatter of contamination gap vs DIF-C proportion, raw
596	    (r=-0.478, significant). Right: same scatter after residualizing both variables
597	    on item difficulty — correlation vanishes (r=0.03). Illustrates that difficulty
598	    is the confound driving the entire correlation.'
599	  analysis: 'GSM1K correlation collapse是worst tier的defining feature之一。Sub-finding
600	    4 从paper的main body中完全删除。ρ≈0.997 redundancy和circularity ablation（z=-9.5） 不受影响（它们不依赖GSM1K）。Reframe后Claim
601	    4缩减为三个sub-finding：(1)redundancy， (2)DIF≠high-discrimination（circularity ablation），(3)diagnostic
602	    lens（model-specific patterns）。GSM8K的Step 1和Step 2仍然有用——framework portability demonstration
603	    survives，只是downstream validation不work了。
604	
605	    '
606	- name: bifactor_irt_equating_pilot
607	  plan_id: plan_005
608	  description: 'Bifactor IRT equating pilot on MMLU。General factor + 57 subject-specific
609	    factors。Anchor item selection。Fixed-parameter calibration。Score equivalence validation
610	    (target ρ≥0.95)。
611	
612	    '
613	  expected_results:
614	    model_convergence: partial
615	    n_iterations_to_convergence: 8500
616	    convergence_criterion_met: false
617	    rmsea: 0.047
618	    cfi: 0.72
619	    tli: 0.69
620	    srmr: 0.081
621	    general_factor_variance_explained: 0.31
622	    specific_factor_avg_variance: 0.18
623	    residual_variance: 0.51
624	    n_anchor_items_identified: 847
625	    anchor_item_stability_criterion: 0.8
626	    n_items_meeting_stability: 412
627	    equated_rho_full_vs_replaced_10pct: 0.91
628	    equated_rho_full_vs_replaced_20pct: 0.86
629	    equated_rho_full_vs_replaced_31pct: 0.79
630	    score_equivalence_bias_mean: 0.34
631	    score_equivalence_bias_max: 2.17
632	  result_rationale: 'Bifactor模型在5,219×12,508矩阵上面临计算和统计双重困难。模型未完全收敛（8,500 iterations仍未满足criterion），CFI=0.72和TLI=0.69远低于acceptable
633	    fit标准（>0.90）。 这并非意外——MMLU的57 subjects构成的multidimensional structure过于复杂，bifactor
634	    是一个over-simplification（假设1个general factor + 57 orthogonal specific factors， 但实际上subjects之间存在大量cross-loading）。General
635	    factor仅解释31%方差，说明 MMLU的"general intelligence"维度很弱。残差方差51%意味着模型miss了一半的信号。
636	
637	    Anchor item selection结果更差：按stability criterion(across-cohort Δ_MH<0.5) 筛选出847个候选anchor
638	    items，但只有412个满足更严格的equating stability要求。 用这412个anchor做fixed-parameter calibration后，替换10%的items时ρ=0.91（<0.95
639	    target），替换31%时ρ=0.79——远低于目标。Score equivalence bias高达2.17， 意味着某些模型的equated score偏移>2个标准误。
640	
641	    根本原因：IRT equating假设latent trait是well-measured的，但MMLU上1D IRT fundamentally misspecified（98%
642	    models |Lz|>2），bifactor虽然better但仍然 inadequate。Without good person parameter estimates,
643	    equating is garbage-in- garbage-out。
644	
645	    '
646	  tables:
647	  - name: Bifactor Model Fit Indices
648	    columns:
649	    - Index
650	    - Value
651	    - Acceptable
652	    - Good
653	    - Status
654	    rows:
655	    - - RMSEA
656	      - 0.047
657	      - <0.08
658	      - <0.05
659	      - Borderline
660	    - - CFI
661	      - 0.72
662	      - '>0.90'
663	      - '>0.95'
664	      - FAIL
665	    - - TLI
666	      - 0.69
667	      - '>0.90'
668	      - '>0.95'
669	      - FAIL
670	    - - SRMR
671	      - 0.081
672	      - <0.08
673	      - <0.05
674	      - FAIL
675	  - name: Score Equivalence After Item Replacement
676	    columns:
677	    - Replacement_pct
678	    - Spearman_ρ
679	    - Mean_bias
680	    - Max_bias
681	    - Target_met
682	    rows:
683	    - - 5%
684	      - 0.94
685	      - 0.12
686	      - 0.87
687	      - No (ρ<0.95)
688	    - - 10%
689	      - 0.91
690	      - 0.34
691	      - 1.41
692	      - 'No'
693	    - - 20%
694	      - 0.86
695	      - 0.67
696	      - 1.89
697	      - 'No'
698	    - - 31%
699	      - 0.79
700	      - 1.12
701	      - 2.17
702	      - 'No'
703	  figures_description:
704	  - 'Fig: Bifactor path diagram showing general factor loadings (weak, avg=0.31) and
705	    subject-specific loadings. Residual variance dominates, indicating poor model
706	    specification.'
707	  - 'Fig: Score equivalence scatter plot at 31% replacement. Clear systematic bias
708	    for mid-ability models — equating over-credits some model families and under-credits
709	    others.'
710	  analysis: 'Bifactor pilot的失败confirmed paper_framing.md中已经预期的结论："IRT是fundamentally
711	    misspecified for MMLU"。这在worst tier下被reviewer weaponize："如果你承认IRT misspecified，那MH
712	    conditioning on total score是唯一defensible approach—— 但then 31% reflects score-based
713	    rather than ability-based DIF，你没有evidence 这是''真正的''item functioning差异而不是score
714	    distribution artifact"。 Equating pilot失败意味着Claim 3（regeneration）完全dead。对于reframe：将equating
715	    从claims中完全移除，bifactor结果变成limitations section的evidence——"future work 需要multidimensional
716	    IRT才能实现equating"。
717	
718	    '
719	- name: item_generation_calibration
720	  plan_id: plan_006
721	  description: 'LLM生成替换items + student simulation校准。Construct constraints, difficulty
722	    estimation, holdout validation。
723	
724	    '
725	  expected_results:
726	    n_items_generated: 500
727	    n_items_passing_face_validity: 312
728	    face_validity_pass_rate: 0.624
729	    difficulty_correlation_prompt_based: 0.31
730	    difficulty_correlation_student_sim: 0.52
731	    difficulty_correlation_target: 0.75
732	    subject_coverage_pct: 89
733	    cognitive_level_match_pct: 67
734	    holdout_panel_rho: 0.48
735	    discrimination_match_r: 0.29
736	    construct_drift_detected_pct: 18.4
737	    gpu_hours_used: 178
738	  result_rationale: 'Item generation面临两个层面的困难。First, face validity：只有62.4%的generated
739	    items通过human evaluation（incorrect distractors太obvious，或者stem在语义上 偏移了原item的construct）。Second,
740	    calibration：student simulation的difficulty estimation（ρ=0.52）远低于arXiv 2601.09953报告的0.75-0.82，这是因为MMLU
741	    items 的difficulty主要由knowledge specificity驱动（而非reasoning complexity），而LLM student
742	    simulation更擅长估计reasoning difficulty。Discrimination match更差 （r=0.29）——generated
743	    items的区分度系统性偏低，因为LLM倾向于生成"textbook-style" 的clean items而非real exam的nuanced items。
744	
745	    18.4%的construct drift意味着近五分之一的生成items实际上测量的是不同的construct—— 比如原item测试"specific
746	    legal precedent knowledge"但generated item测试 "general legal reasoning"。这在holdout
747	    panel上表现为ρ=0.48——生成的benchmark 与原始benchmark的model ranking correlation很弱。
748	
749	    Combined with plan_005的equating failure，整个regeneration pipeline（Claim 3原版） 在worst
750	    tier下是完全不可行的。
751	
752	    '
753	  tables:
754	  - name: Item Generation Quality Metrics
755	    columns:
756	    - Metric
757	    - Value
758	    - Target
759	    - Status
760	    rows:
761	    - - Face validity pass rate
762	      - 0.624
763	      - '>0.80'
764	      - FAIL
765	    - - Difficulty ρ (prompt-based)
766	      - 0.31
767	      - 0.45+
768	      - FAIL
769	    - - Difficulty ρ (student sim)
770	      - 0.52
771	      - 0.75+
772	      - FAIL
773	    - - Discrimination match r
774	      - 0.29
775	      - '>0.60'
776	      - FAIL
777	    - - Construct drift
778	      - 18.4%
779	      - <5%
780	      - FAIL
781	    - - Holdout ranking ρ
782	      - 0.48
783	      - ≥0.95
784	      - FAIL
785	  figures_description:
786	  - 'Fig: Difficulty calibration scatter — generated item difficulty (student sim
787	    estimated) vs actual difficulty on holdout model panel. Wide scatter (ρ=0.52)
788	    with systematic under-estimation of hard items.'
789	  analysis: 'Item generation失败在worst tier reframe中不造成额外伤害——regeneration（Claim 3 原版）已经在Dream
790	    #3中被pruned to appendix。但这个negative result本身有publication value作为"cautionary tale
791	    about LLM-based item generation for high-stakes benchmarks"——如果space permits可以在Discussion中brief
792	    mention。
793	
794	    '
795	- name: cumulative_bayesian_dif
796	  plan_id: plan_007
797	  description: 'Cumulative Bayesian DIF priors (Sinharay et al., 2006)。4轮successive
798	    administrations模拟。Power improvement from evidence accumulation。
799	
800	    '
801	  expected_results:
802	    individual_admin_power_delta10: 0.41
803	    cumulative_2admin_power_delta10: 0.52
804	    cumulative_3admin_power_delta10: 0.58
805	    cumulative_4admin_power_delta10: 0.63
806	    target_cumulative_3admin_power: 0.7
807	    target_met: false
808	    prior_calibration_error_mean: 0.23
809	    prior_calibration_error_max: 0.67
810	    fpr_inflation_cumulative_4admin: 0.074
811	    bayesian_mh_correlation_flags: 0.81
812	    bayes_factor_median: 3.2
813	    bayes_factor_gt10_pct: 18.4
814	    simulation_n_per_admin: 200
815	    n_items_simulated: 1000
816	    n_administrations: 4
817	  result_rationale: 'Cumulative Bayesian方法的power improvement低于理论预期：3-admin cumulative
818	    power=0.58（vs target 0.70），4-admin才达到0.63。差距来自prior miscalibration： Sinharay et
819	    al.的priors是为human testing设计的（student populations with stable demographics），LLM
820	    "administrations"的cohort composition变化更剧烈 （每轮新模型的ability distribution shift更大），导致informative
821	    priors反而 引入bias。Prior calibration error mean=0.23意味着prior对DIF effect size的 预期系统性偏离了actual，累积后bias不是减少而是compound。
822	
823	    Bayes factors偏弱（median=3.2，只有18.4%的items BF>10），说明evidence accumulation受限于LLM
824	    cohort间的non-stationarity。FPR inflation到0.074 在4-admin后是manageable但concerning——累积更多administrations可能会worse。
825	
826	    与MH flags的correlation=0.81说明Bayesian方法在很大程度上agree with MH， 增量贡献有限——essentially
827	    adding computational complexity for modest gain。
828	
829	    '
830	  tables:
831	  - name: Cumulative Power by Administration
832	    columns:
833	    - N_admins
834	    - Power_δ=0.8
835	    - Power_δ=1.0
836	    - Power_δ=1.4
837	    - FPR
838	    rows:
839	    - - 1
840	      - 0.22
841	      - 0.41
842	      - 0.68
843	      - 0.042
844	    - - 2
845	      - 0.31
846	      - 0.52
847	      - 0.76
848	      - 0.051
849	    - - 3
850	      - 0.37
851	      - 0.58
852	      - 0.81
853	      - 0.063
854	    - - 4
855	      - 0.42
856	      - 0.63
857	      - 0.84
858	      - 0.074
859	  - name: Prior Calibration Analysis
860	    columns:
861	    - Admin_pair
862	    - Prior_mean_error
863	    - Prior_var_error
864	    - BF_median
865	    rows:
866	    - - 1→2
867	      - 0.14
868	      - 0.08
869	      - 4.1
870	    - - 2→3
871	      - 0.21
872	      - 0.13
873	      - 3.4
874	    - - 3→4
875	      - 0.34
876	      - 0.19
877	      - 2.7
878	  figures_description:
879	  - 'Fig: Power curves showing cumulative improvement across 4 administrations at
880	    δ=1.0. Actual curve (solid) systematically below theoretical curve (dashed) due
881	    to prior miscalibration. Gap widens with more administrations.'
882	  analysis: 'Bayesian cumulative DIF在worst tier下确认了paper_framing.md的decision to move
883	    it to appendix。Power improvement不足以justify complexity increase。 Prior miscalibration问题是fundamental——LLM
884	    benchmark "administrations" 不满足Bayesian updating的stationarity assumption。在reframe后，这变成
885	    appendix material："simulation study showing theoretical potential with caveats
886	    about non-stationary populations"。
887	
888	    '
889	- name: graceful_degradation_analysis
890	  plan_id: plan_008
891	  description: 'Benchmark validity under progressive item replacement。Ranking stability,
892	    score reliability, construct coverage at 5/10/20/50% replacement。 Theoretical
893	    bounds + empirical validation on METABENCH。
894	
895	    '
896	  expected_results:
897	    rho_5pct_replacement: 0.993
898	    rho_10pct_replacement: 0.984
899	    rho_20pct_replacement: 0.961
900	    rho_50pct_replacement: 0.887
901	    reliability_original_kr20: 0.967
902	    reliability_5pct: 0.964
903	    reliability_10pct: 0.958
904	    reliability_20pct: 0.943
905	    reliability_50pct: 0.891
906	    construct_coverage_original: 1.0
907	    construct_coverage_5pct: 0.98
908	    construct_coverage_10pct: 0.95
909	    construct_coverage_20pct: 0.87
910	    construct_coverage_50pct: 0.71
911	    theoretical_lower_bound_rho_at_31pct: 0.92
912	    empirical_rho_at_31pct: 0.94
913	    critical_replacement_threshold: 0.23
914	    validity_degradation_rate: nonlinear
915	  result_rationale: 'Graceful degradation分析本身产生reasonable results——rankings在20%替换时
916	    仍robust（ρ=0.961），但construct coverage更fragile（0.87 at 20%）。关键 问题在worst tier context中：这个分析假设replacement
917	    items是well-calibrated的， 但plan_005（equating failure）和plan_006（generation failure）已经证明
918	    实际的replacement items质量远低于预期。所以degradation curves是optimistic lower bound——实际degradation会worse。
919	
920	    Critical replacement threshold=23%意味着替换>23%的items时validity开始 non-linearly degrade。但我们的DIF
921	    flag rate是31%——超过了这个threshold。 Reviewer会指出："你说31%的items unstable，但你也说替换>23%就会degrade
922	    validity——那你的解决方案（替换flagged items）本身就会destroy benchmark validity。 这不是一个solution而是一个dilemma。"
923	
924	    在worst tier reframe中这个dilemma变成feature而非bug："we characterize the replacement feasibility
925	    boundary"——但reviewer可能视其为研究without actionable outcome。
926	
927	    '
928	  tables:
929	  - name: Validity Metrics Under Progressive Replacement
930	    columns:
931	    - Replace_pct
932	    - Rank_ρ
933	    - KR-20
934	    - Coverage
935	    - Max_rank_shift
936	    rows:
937	    - - 0% (original)
938	      - 1.0
939	      - 0.967
940	      - 1.0
941	      - 0
942	    - - 5%
943	      - 0.993
944	      - 0.964
945	      - 0.98
946	      - 23
947	    - - 10%
948	      - 0.984
949	      - 0.958
950	      - 0.95
951	      - 47
952	    - - 20%
953	      - 0.961
954	      - 0.943
955	      - 0.87
956	      - 112
957	    - - 31% (DIF rate)
958	      - 0.94
959	      - 0.927
960	      - 0.79
961	      - 189
962	    - - 50%
963	      - 0.887
964	      - 0.891
965	      - 0.71
966	      - 341
967	  - name: Theoretical vs Empirical Degradation
968	    columns:
969	    - Replace_pct
970	    - Theory_lower_ρ
971	    - Empirical_ρ
972	    - Gap
973	    rows:
974	    - - 10%
975	      - 0.978
976	      - 0.984
977	      - '+0.006'
978	    - - 20%
979	      - 0.944
980	      - 0.961
981	      - '+0.017'
982	    - - 31%
983	      - 0.92
984	      - 0.94
985	      - '+0.020'
986	    - - 50%
987	      - 0.868
988	      - 0.887
989	      - '+0.019'
990	  figures_description:
991	  - 'Fig: Three-panel degradation curves (ranking ρ, KR-20, construct coverage) vs
992	    replacement percentage. Vertical dashed line at 31% (DIF rate) and 23% (critical
993	    threshold). Coverage curve drops steeply after 20%, while ranking ρ degrades more
994	    gracefully.'
995	  analysis: 'Graceful degradation在worst tier reframe中降级为supplementary analysis。 核心insight（replacement
996	    threshold < DIF rate）在appendix中作为"the fundamental tension in DIF-based benchmark
997	    maintenance"讨论，但不作为main claim。ρ≈0.997 的existing finding（plan_017, DIF removal
998	    without replacement）remains the stronger and simpler message for the main paper。
999	
1000	    '
1001	- name: item_focused_trees
1002	  plan_id: plan_009
1003	  description: 'Item-Focused Trees (Tutz & Berger 2016) as alternative to categorical
1004	    cohort DIF。 Release date as continuous covariate。Detection power comparison vs
1005	    categorical DIF。
1006	
1007	    '
1008	  expected_results:
1009	    ift_items_flagged_pct: 27.4
1010	    ift_mh_overlap_jaccard: 0.63
1011	    ift_unique_flags_pct: 8.1
1012	    mh_unique_flags_pct: 11.7
1013	    ift_detection_power_delta14: 0.59
1014	    mh_detection_power_delta14: 0.68
1015	    ift_fpr: 0.088
1016	    mh_fpr_temporal: 0.314
1017	    ift_tree_depth_median: 3
1018	    ift_tree_depth_max: 7
1019	    ift_primary_split_variable: release_date
1020	    ift_secondary_split: model_size
1021	    overfitting_cv_auroc_gap: 0.12
1022	    n_stable_splits: 4
1023	    n_unstable_splits: 8
1024	  result_rationale: 'Item-Focused Trees在worst tier下产生mixed results。优点：FPR=0.088远低于
1025	    MH temporal的0.314，因为trees不需要硬性cohort split——continuous release date 允许更nuanced的grouping。缺点：detection
1026	    power=0.59低于MH的0.68，因为trees 将sample分割成更小的subgroups（每个leaf node N更小）。Jaccard=0.63的overlap
1027	    说明两种方法largely agree但有meaningful disagreement。
1028	
1029	    关键weakness：overfitting。CV AUROC gap=0.12说明trees在training上over-optimize。 12个split中8个是unstable的（bootstrap
1030	    resample后不reproduce）。这使得IFT results在robustness上不如MH（MH虽然crude但statistically principled）。
1031	
1032	    Reviewer在worst tier下会指出："IFT有更好的FPR但更差的power和更差的stability—— 这不是一个improvement而是一个tradeoff，你没有demonstrate哪个tradeoff更
1033	    appropriate for this application。"
1034	
1035	    Primary split on release_date confirms temporal effect is real but secondary split
1036	    on model_size introduces a confound MH doesn''t have——larger models are more recent
1037	    AND better, so tree conflates time and capability。
1038	
1039	    '
1040	  tables:
1041	  - name: IFT vs MH-DIF Comparison
1042	    columns:
1043	    - Metric
1044	    - IFT
1045	    - MH (temporal)
1046	    - Advantage
1047	    rows:
1048	    - - Items flagged %
1049	      - 27.4
1050	      - 31.3
1051	      - IFT (fewer)
1052	    - - FPR
1053	      - 0.088
1054	      - 0.314
1055	      - IFT ×3.6 better
1056	    - - TPR (δ≥1.4)
1057	      - 0.59
1058	      - 0.68
1059	      - MH +0.09
1060	    - - Overlap (Jaccard)
1061	      - —
1062	      - —
1063	      - 0.63
1064	    - - CV stability
1065	      - 0.67
1066	      - N/A (parametric)
1067	      - MH
1068	  - name: IFT Split Stability (Bootstrap)
1069	    columns:
1070	    - Split_depth
1071	    - Variable
1072	    - Bootstrap_reproduce_pct
1073	    - Stable
1074	    rows:
1075	    - - 1
1076	      - release_date
1077	      - 98
1078	      - 'Yes'
1079	    - - 2
1080	      - model_size
1081	      - 72
1082	      - 'Yes'
1083	    - - 3
1084	      - training_data_size
1085	      - 61
1086	      - Borderline
1087	    - - 4
1088	      - subject_category
1089	      - 34
1090	      - 'No'
1091	  figures_description:
1092	  - 'Fig: Example Item-Focused Tree for a representative MMLU subject. First split
1093	    on release_date (2023-06), second on model_size. Deeper splits are unstable —
1094	    dashed lines indicate bootstrap reproduction <50%.'
1095	  analysis: 'IFT在worst tier reframe中有niche价值：它提供release_date作为continuous covariate的evidence，支持"temporal
1096	    instability is real"的narrative。但 overfitting和power loss使其不适合作为primary method。Appendix
1097	    material。
1098	
1099	    '
1100	- name: architecture_stratified_dif
1101	  plan_id: plan_010
1102	  description: 'Architecture-homogeneous DIF。Decoder-only subset。IRT fit diagnostics。
1103	    Compare FPR/TPR vs full-population DIF。
1104	
1105	    '
1106	  expected_results:
1107	    n_decoder_only: 5226
1108	    n_non_decoder: 1
1109	    pct_decoder_only: 99.98
1110	    decoder_only_c_pct: 31.3
1111	    full_population_c_pct: 31.3
1112	    jaccard_decoder_vs_full: 1.0
1113	    removed_model: RWKV-v5-Eagle-7B
1114	    rmsea_decoder_only: 0.089
1115	    rmsea_full: 0.089
1116	    cfi_decoder_only: 0.41
1117	    cfi_full: 0.41
1118	    lz_pct_misfit_decoder_only: 97.8
1119	    lz_pct_misfit_full: 98.1
1120	    irt_fit_improvement: negligible
1121	    temporal_fpr_decoder_only: 0.313
1122	    temporal_tpr_p05_decoder_only: 0.834
1123	  result_rationale: 'METABENCH MMLU is 99.98% decoder-only（5226/5227），移除1个non-decoder模型
1124	    对所有结果的影响为zero（Jaccard=1.000）。Architecture heterogeneity concern dissolved——但这是一个trivial
1125	    result，不是一个victory。
1126	
1127	    关键问题：IRT fit完全没有improve（RMSEA=0.089, CFI=0.41, 97.8% |Lz|>2）。 这confirms MMLU的IRT
1128	    misfit不是由architecture heterogeneity造成的——root cause 是multidimensionality（57 subjects）。在worst
1129	    tier下reviewer的攻击点是： "你证明了architecture不是问题，但IRT misfit仍然devastating。98%的模型misfit
1130	    意味着你的ability estimates是meaningless的——MH conditioning on total score 是唯一defensible
1131	    approach，但total score在multidimensional test上不是ability 的good proxy。So your 31%
1132	    DIF reflects score-distribution artifacts, not genuine differential item functioning。"
1133	
1134	    这是worst tier核心假设#4的manifestation。Defense只能是承认limitation并argue MH is still the
1135	    best available tool（"conditioning on total score is imperfect but standard psychometric
1136	    practice for multidimensional tests"），而非claim results are unaffected。
1137	
1138	    '
1139	  tables:
1140	  - name: Architecture Stratification Results
1141	    columns:
1142	    - Metric
1143	    - Full_pop (N=5227)
1144	    - Decoder-only (N=5226)
1145	    - Δ
1146	    rows:
1147	    - - ETS C%
1148	      - 31.3
1149	      - 31.3
1150	      - 0.0
1151	    - - Jaccard vs full
1152	      - —
1153	      - 1.0
1154	      - —
1155	    - - RMSEA
1156	      - 0.089
1157	      - 0.089
1158	      - 0.0
1159	    - - CFI
1160	      - 0.41
1161	      - 0.41
1162	      - 0.0
1163	    - - '|Lz|>2 %'
1164	      - 98.1
1165	      - 97.8
1166	      - -0.3
1167	    - - FPR (temporal)
1168	      - 0.314
1169	      - 0.313
1170	      - -0.001
1171	  - name: Non-decoder Model Impact
1172	    columns:
1173	    - Model
1174	    - Architecture
1175	    - Effect_on_C%
1176	    - Effect_on_rankings
1177	    rows:
1178	    - - RWKV-v5-Eagle-7B
1179	      - RWKV (linear attention)
1180	      - None
1181	      - None
1182	  figures_description:
1183	  - 'Fig: IRT person-fit (|Lz|) distribution for decoder-only subset — virtually identical
1184	    to full population. Peak at |Lz|≈4-5 with 97.8% above misfit threshold. Architecture
1185	    homogeneity does not rescue IRT fit.'
1186	  analysis: 'Architecture stratification是一个"dissolved concern"——architecture不是问题，
1187	    但IRT misfit仍然是。在worst tier reframe中：(1)architecture section变成一段话 而非一节——"concern
1188	    dissolved, 99.98% decoder-only"；(2)IRT misfit discussion 变得更prominent——"we acknowledge
1189	    1D IRT is fundamentally misspecified for MMLU; total-score conditioning is our
1190	    pragmatic choice; multidimensional IRT is future work"；(3)这个limitation是honest
1191	    but costly——reviewer can use it to question the entire DIF analysis。Practitioner''s
1192	    Guide section mitigates by providing "when/how to use DIF despite IRT limitations"。
1193	
1194	    '
1195	- name: semi_synthetic_contamination_validation
1196	  plan_id: plan_011
1197	  description: 'Semi-synthetic contamination injection into real METABENCH response
1198	    matrix。 500 clean items, 100-200 injected. TPR/FPR under controlled ground truth。
1199	    Vary prevalence (5-30%), exploitation rate (0.4-1.0), focal group size (40-200)。
1200	
1201	    '
1202	  expected_results:
1203	    temporal_external_tpr_p0: 0.326
1204	    temporal_external_tpr_p03: 0.548
1205	    temporal_external_tpr_p05: 0.834
1206	    temporal_external_tpr_p07: 0.99
1207	    temporal_external_tpr_p10: 1.0
1208	    temporal_external_fpr: 0.314
1209	    temporal_external_delta_tpr_p05: 0.508
1210	    temporal_external_delta_tpr_p10: 0.674
1211	    cross_subject_delta_fpr: 0.0
1212	    within_subject_fpr_inflation: 0.186
1213	    reviewer_dismissal_probability: 0.67
1214	    injection_mechanism_realism_score: 2.3
1215	    n_clean_items: 500
1216	    n_injected_items: 150
1217	    exploitation_rate_range:
1218	    - 0.3
1219	    - 1.0
1220	    dose_response_monotonic: true
1221	    prevalence_5pct_tpr: 0.41
1222	    prevalence_10pct_tpr: 0.57
1223	    prevalence_20pct_tpr: 0.73
1224	    prevalence_30pct_tpr: 0.83
1225	  result_rationale: 'Detection metrics本身look strong——ΔTPR=+0.508 at p=0.5, clear dose-response,
1226	    cross-subject matching eliminates FPR inflation（ΔFPR=0.000）。但worst tier 的核心攻击不是metrics而是mechanism
1227	    validity。
1228	
1229	    Reviewer dismissal probability=0.67基于核心假设#6："flipping incorrect→correct doesn''t
1230	    model real contamination mechanisms"。具体攻击：(1)真实contamination 是memorization——模型在training中多次见到item，导致parameterized
1231	    recall，表现为 high confidence on specific items而非simple correctness flip；(2)真实contamination
1232	    影响response pattern而非just accuracy——contaminated model可能在某些distractors 上有异常pattern（always选A），simple
1233	    flip不capture这个；(3)partial contamination is not random——contaminated model更可能在semantically
1234	    similar items上都contaminated （cluster structure），而random sampling的injection忽略了这个structure；
1235	    (4)exploitation rate concept假设contamination是binary（correct with probability p），
1236	    但实际是gradient（模型"部分记住"一个item可能表现为distractor bias而非correctness）。
1237	
1238	    "Injection realism score"=2.3/5（hypothetical expert rating）——method是 sound as
1239	    a statistical framework但ecological validity低。这是worst tier下 ΔTPR被解读为"your framework
1240	    can detect your artificial signal, but does it detect real contamination?"的核心矛盾。
1241	
1242	    Cross-subject matching的ΔFPR=0.000是genuinely novel and survives所有attacks—— 即使injection
1243	    mechanism被dismissed，matching methodology contribution stands。
1244	
1245	    '
1246	  tables:
1247	  - name: Semi-synthetic Detection Power (Cross-subject Matching)
1248	    columns:
1249	    - Exploitation_rate
1250	    - TPR
1251	    - ΔTPR
1252	    - FPR
1253	    - ΔFPR
1254	    rows:
1255	    - - p=0.0 (baseline)
1256	      - 0.326
1257	      - 0.0
1258	      - 0.314
1259	      - 0.0
1260	    - - p=0.3
1261	      - 0.548
1262	      - 0.222
1263	      - 0.314
1264	      - 0.0
1265	    - - p=0.5
1266	      - 0.834
1267	      - 0.508
1268	      - 0.314
1269	      - 0.0
1270	    - - p=0.7
1271	      - 0.99
1272	      - 0.664
1273	      - 0.314
1274	      - 0.0
1275	    - - p=1.0
1276	      - 1.0
1277	      - 0.674
1278	      - 0.314
1279	      - 0.0
1280	  - name: Mechanism Realism Critique
1281	    columns:
1282	    - Aspect
1283	    - Semi-synthetic
1284	    - Real_contamination
1285	    - Mismatch
1286	    rows:
1287	    - - Signal type
1288	      - Binary flip
1289	      - Parametric recall
1290	      - HIGH
1291	    - - Response pattern
1292	      - Only accuracy
1293	      - Distractor bias
1294	      - HIGH
1295	    - - Item correlation
1296	      - Random selection
1297	      - Semantic clusters
1298	      - MEDIUM
1299	    - - Effect gradient
1300	      - p ∈ {0,1}
1301	      - Continuous partial
1302	      - MEDIUM
1303	    - - Ability distribution
1304	      - Real (preserved)
1305	      - Real
1306	      - NONE
1307	  figures_description:
1308	  - 'Fig: Dose-response curve showing ΔTPR vs exploitation rate p, with 95% bootstrap
1309	    CIs. Monotonically increasing, confirming framework sensitivity. But annotation:
1310	    ''Detection power is validated against synthetic signal — transfer to natural
1311	    contamination is assumed, not demonstrated.'''
1312	  analysis: Semi-synthetic validation在worst tier reframe中的定位shift from "validation
1313	    of DIF as contamination detector" to "reusable validation infrastructure that
1314	    any item-level detector can plug into"。ΔTPR methodology和cross-subject matching
1315	    是framework contributions that survive mechanism critique。关键修改：(1)不再 claim "DIF
1316	    can detect real contamination"——而是"DIF can detect differential item functioning
1317	    under synthetic contamination, consistent with but not proof of real-world detection"；(2)explicitly
1318	    acknowledge injection mechanism limitations in Method section而非buried in limitations；(3)frame
1319	    cross-subject matching as primary contribution of this experiment——ΔFPR=0.000
1320	    across all conditions 是genuinely novel practical insight。
1321	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a1d208d-8d0e-4d36-a04a-d7e207e5c35d",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "bf10ec7d-7a23-4c2b-9db0-f17e84149713",
  "sourceToolAssistantUUID": "6a1d208d-8d0e-4d36-a04a-d7e207e5c35d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-21T05:33:53.335Z_

Now I have a thorough understanding of the paper as written in the actual tex files and the worst-tier imagined experiment context. Let me produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf10ec7d-7a23-4c2b-9db0-f17e84149713",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAkjUvE7HQwPLPFQCCX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff42ff37-d893-402b-a318-7454a62573f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9SoHNyK9w8RaxpLd9oUmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20615,
      "cache_read_input_tokens": 64962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20615,
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

_source line 64 · 2026-05-21T05:35:19.260Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01TbpNPCyq6ez1PBKuVX9Fhj`</summary>

```json
{
  "report": "# Reviewer 2 (R2): Novelty/Significance and Related Work/Positioning\n\n## Summary\n\nThis paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis from educational psychometrics to the METABENCH MMLU response matrix (5,227 models x 12,508 items), finding that 31% of items exhibit large DIF between 2023 and 2024 model cohorts. The paper also proposes a semi-synthetic validation framework (ΔTPR methodology with cross-subject matching), critiques the use of web-overlap labels as ground truth for differential detectors, and replicates on GSM8K. While the scale of analysis is impressive and the transparency about negative results is commendable, the paper applies an unmodified classical method to a new domain and the resulting insights, though competently executed, are incremental rather than surprising.\n\n---\n\n## Strengths\n\n- **Honest reporting of negative results.** The paper is admirably transparent about what did not work (bifactor IRT, item generation, Bayesian DIF, ensemble fusion, RL robustness). This is rare and valuable for the community.\n\n- **Ground truth meta-critique is well-argued.** The distinction between global exposure and differential functioning (Section 4.3/5.2) is a genuine conceptual contribution. The observation that web-overlap labels cannot serve as ground truth for differential detectors is correct and has not been stated this clearly before. This should influence how future contamination detection papers validate their methods.\n\n- **Cross-subject matching is a clean methodological insight.** The ΔFPR = 0.000 result under cross-subject matching, and the clear demonstration of why within-subject matching inflates FPR (because the conditioning variable absorbs the injection signal), is a practical and reusable insight that survives scrutiny independently of the other claims.\n\n- **Scale.** The analysis on 5,227 x 12,508 is the largest DIF analysis applied to LLM benchmarks, and the random-split sanity check (0.18% C%) is a convincing null control.\n\n- **Well-structured paper with clear claims.** The four numbered claims in the introduction are explicitly stated and systematically addressed. The mapping between claims and evidence is easy to follow.\n\n- **GSM8K replication.** Extending to a second benchmark with an independent contamination validation mechanism (GSM1K) strengthens the generalizability argument.\n\n---\n\n## Weaknesses\n\n### Major\n\n1. **Limited methodological novelty (Major).** The paper explicitly states \"we do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic.\" MH-DIF is a 1988 method with extensive textbook treatment. Applying an off-the-shelf statistical test to a new dataset, even at unprecedented scale, constitutes an empirical contribution, not a methodological one. The cross-subject matching protocol is sensible but straightforward — it is the standard recommendation when the matching variable may be contaminated (Holland & Thayer 1988 already discuss matching variable selection). The ΔTPR/ΔFPR reporting framework is simply measuring incremental detection rates under injection, which is standard in detection evaluation. For ICLR, I expect either (a) novel methods adapted to the LLM setting, or (b) empirical findings that fundamentally change how the community operates. This paper is closer to (b) but does not quite reach the bar (see weakness #3).\n\n2. **The 31% headline number is method-dependent and potentially inflated (Major).** The paper reports SIBTEST flags 44.7% of items with only 0.48 Jaccard overlap against MH. This means MH and SIBTEST disagree on which items are unstable more often than they agree. The paper acknowledges the instability range is \"≥18-31% depending on DIF type and threshold,\" but the title and abstract still anchor on \"31%.\" The discrepancy between MH and SIBTEST indicates substantial non-uniform (crossing) DIF that MH misses by design — items where the DIF direction reverses across the ability spectrum. If the instrument's core finding is this sensitive to methodological choice, the paper should either (a) present a principled way to reconcile the methods, or (b) reframe the headline entirely around the method-dependence as the finding. The current framing leans heavily on 31% while burying the SIBTEST comparison.\n\n3. **Instability is not actionable (Major).** The paper finds 31% of items are unstable, then shows this does not affect rankings (ρ ≈ 0.997). The DIF analysis identifies *that* items changed but not *why*. The paper cannot distinguish contamination from legitimate capability gains from training methodology changes from data composition shifts. Without causal attribution, the finding is descriptive rather than actionable. A practitioner reading this paper learns \"some items changed\" but cannot decide what to do about it. The practitioner's guide (Section 4.7) offers generic recommendations, but they follow directly from standard psychometric practice and do not require the specific analysis in this paper.\n\n4. **IRT misspecification undermines the theoretical foundation (Major).** CFI = 0.41 and 98% of models showing |Lz| > 2 indicates catastrophic IRT model misfit. MH-DIF conditions on total score as a proxy for ability, but if the latent structure is fundamentally multidimensional (57 MMLU subjects), total score is a poor proxy. The paper acknowledges this but does not adequately address whether the 31% DIF rate is inflated by the fact that total score inadequately captures the true ability differences between cohorts. The ability-quintile control (2.9% C%) is reassuring but does not rule out more subtle forms of ability confounding in the temporal comparison. The IRT misspecification is not a peripheral concern — it strikes at the core assumption of the MH procedure.\n\n5. **Semi-synthetic injection has low ecological validity (Major).** The injection mechanism (flipping incorrect responses to correct at rate p) simulates an idealized contamination scenario that does not resemble how real contamination manifests. Real contamination produces parametric recall, distractor biases, clustered (non-random) item effects, and continuous partial knowledge — none of which the binary flip model captures. The paper self-acknowledges this in Table 5 (\"HIGH mismatch\" on signal type and response pattern), which raises the question: if the injection mechanism is acknowledged to be unrealistic, what exactly does the ΔTPR number validate? The framework demonstrates internal consistency (MH detects the signal it was designed to detect under conditions favorable to detection), but the transfer to naturalistic contamination is assumed, not demonstrated.\n\n### Minor\n\n6. **GSM1K correlation may be confounded by difficulty (Minor).** DIF-C items are systematically harder (mean difficulty 0.38 vs 0.61, p < 0.001). The correlation between contamination gap and DIF ranking advantage (r = -0.478) could be driven entirely by item difficulty as a confound: harder items naturally show smaller accuracy differences between GSM8K and GSM1K regardless of contamination mechanism. The paper reports a partial correlation controlling for accuracy (r = -0.385, p = 0.027) but not controlling for item difficulty. At N = 33, controlling for one additional variable could plausibly eliminate the effect entirely. The paper should report the partial correlation controlling for difficulty.\n\n7. **Broken bibliography (Minor).** All citations render as \"?\" in the compiled paper. While this may be a compilation issue, it makes the paper unreadable in its current form and prevents verifying that citations are correctly placed.\n\n8. **Missing comparison with concurrent work (Minor).** Growing Pains (Habba et al. 2026) is discussed in related work but not empirically compared. Since that paper also addresses temporal comparability through fixed-parameter calibration, a direct empirical comparison (e.g., do their anchor items overlap with the non-DIF items identified here?) would substantially strengthen the positioning.\n\n9. **Audience and venue fit (Minor).** The paper's primary contributions are psychometric characterization of an existing benchmark and a validation methodology critique. The method is applied, not developed. The most natural audience is a measurement or evaluation workshop (e.g., the ICLR Evaluation Workshop, NeurIPS Datasets and Benchmarks), where the empirical findings would be directly actionable and the psychometric framing would be appreciated without requiring algorithmic novelty. At a top ML venue, the bar for \"what should the community do differently as a result of this paper?\" is higher, and the answer here is unclear beyond \"monitor DIF as a diagnostic,\" which is generic psychometric advice.\n\n10. **Circular reasoning concern in downstream impact (Minor).** DIF flags items that differ across cohorts. Removing them and observing that rankings become more stable across cohorts is tautological — by construction, removing the items that differ most will produce more similar rankings. The circularity ablation (z = -9.5 for DIF-based removal being least disruptive among non-random strategies) addresses this partially, but the fundamental circularity remains: DIF items concentrate discriminative information because they are defined as the items that discriminate between cohorts.\n\n---\n\n## Questions for Authors\n\n1. What is the partial correlation between GSM1K contamination gap and DIF ranking advantage after controlling for item difficulty (not just overall accuracy)?\n\n2. The MH-SIBTEST Jaccard is only 0.48. Can you provide a principled recommendation for practitioners about which method to use, or how to interpret the disagreement?\n\n3. If IRT is fundamentally misspecified for MMLU (CFI = 0.41, 98% misfit), what is the theoretical justification for treating total-score-conditioned MH-DIF results as reflecting genuine differential item functioning rather than artifacts of inadequate ability matching?\n\n4. The injection mechanism flips incorrect→correct. Have you considered or tested more realistic injection mechanisms (e.g., boosting confidence on the correct option, introducing distractor biases, or cluster-correlated injection)?\n\n5. You report that 92.4% of instability is item-specific (unrelated to domain accuracy gains). What are the leading alternative explanations for this item-specific instability, and can any of them be tested with the available data?\n\n6. The critical replacement threshold (~23%) is below the DIF flag rate (31%). How should a practitioner interpret the finding that removing all flagged items would exceed the threshold at which benchmark validity begins to degrade?\n\n7. Given that the ensemble (DIF + ConStat + DVD) does not outperform the best single signal (ConStat), what is the argument for using DIF over ConStat for practical contamination detection, given ConStat's substantially lower FPR (0.067 vs 0.314)?\n\n---\n\n## Scores\n\n- **Soundness**: 2/4. The IRT misspecification is not adequately addressed. The semi-synthetic injection lacks ecological validity. The 31% number is method-dependent with inadequate discussion of what this means.\n- **Presentation**: 3/4. Well-organized with clear claims. The negative results are commendably transparent. But the broken bibliography and the burying of SIBTEST disagreement are problems.\n- **Contribution**: 2/4. The ground truth meta-critique and cross-subject matching are genuine contributions. But applying an unmodified 1988 method to a new dataset, combined with findings that are descriptive but not actionable, puts this below the contribution threshold for a top venue.\n- **Overall**: 4/10 (Marginally below acceptance threshold)\n- **Confidence**: 4/5. I am familiar with DIF methodology, IRT, and the LLM contamination detection literature. My main uncertainty is whether the community would value the empirical characterization more than I do.\n\n---\n\n## Justification\n\nThis paper is a competent, large-scale application of classical psychometric methods to LLM benchmark evaluation. The ground truth meta-critique (web-overlap labels cannot validate differential detectors) and the cross-subject matching protocol are genuine contributions that should influence future work. The transparency about negative results is exemplary. However, the paper does not clear the novelty bar for ICLR: the method is unmodified from 1988, the headline finding (31% instability) is method-dependent and not actionable, the IRT misspecification undermines the theoretical foundation without adequate remediation, and the semi-synthetic validation demonstrates internal consistency rather than real-world detection capability. The finding that instability does not affect rankings (ρ ≈ 0.997) is reassuring but also diminishes the practical urgency of the work. The paper would be a strong contribution to a psychometrics venue or an evaluation workshop, where the empirical findings would be directly valued and the lack of algorithmic novelty would not be penalized. At ICLR, the question \"what should the ML community do differently as a result of this paper?\" does not have a sufficiently compelling answer.",
  "project": "irt_equated_bench_regen",
  "tier": "worst",
  "dream_id": "dream_20260521T042647",
  "overall_score": "4 - Marginally Below Acceptance Threshold"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff42ff37-d893-402b-a318-7454a62573f0",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAkjUvE7HQwPLPFQCCX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4fca018-e0a2-4acd-9e2f-6d788ff78c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9SoHNyK9w8RaxpLd9oUmV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20615,
      "cache_read_input_tokens": 64962,
      "output_tokens": 3164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3164,
          "cache_read_input_tokens": 64962,
          "cache_creation_input_tokens": 20615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20615,
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

_source line 65 · 2026-05-21T05:35:20.190Z_

<details><summary>↩ Tool result · `toolu_01TbpNPCyq6ez1PBKuVX9Fhj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/worst/review_report.md\", \"dream_id\": \"dream_20260521T042647\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4fca018-e0a2-4acd-9e2f-6d788ff78c83",
  "isSidechain": true,
  "promptId": "db795a6f-9093-46a2-9a93-2b4ed075da5a",
  "agentId": "aea3ad15f794d3072",
  "type": "user",
  "uuid": "f153c143-b417-4418-86e1-3193e58da23c",
  "sourceToolAssistantUUID": "f4fca018-e0a2-4acd-9e2f-6d788ff78c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-21T05:35:30.709Z_

Review submitted successfully. Here is a summary of what was produced:

**Reviewer 2 (R2) review for worst tier of dream_20260521T042647**, saved to:
`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/worst/review_report.md`

**Overall score: 4/10 (Marginally Below Acceptance Threshold)**

**Key findings of the review:**

- **Strengths identified:** Ground truth meta-critique (web-overlap labels cannot validate differential detectors) is a genuine conceptual contribution; cross-subject matching (ΔFPR=0.000) is a clean methodological insight; unprecedented scale (5,227 x 12,508); exemplary transparency about negative results; clear claim-evidence structure.

- **Major weaknesses identified:**
  1. Limited methodological novelty -- unmodified 1988 method applied to new domain
  2. The 31% headline is method-dependent (SIBTEST gives 44.7%, Jaccard overlap only 0.48)
  3. Findings are descriptive but not actionable (identifies *that* items changed, not *why*)
  4. IRT misspecification (CFI=0.41, 98% misfit) undermines the theoretical foundation of MH-DIF
  5. Semi-synthetic injection has low ecological validity (binary flip vs. real contamination mechanisms)

- **Venue fit concern:** Paper would be stronger at a psychometrics venue or evaluation workshop where empirical characterization is valued without requiring algorithmic novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f153c143-b417-4418-86e1-3193e58da23c",
  "isSidechain": true,
  "agentId": "aea3ad15f794d3072",
  "requestId": "req_011CbFAsVfABtbJb8VokKAPP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "150974d4-e368-443c-b024-0a723ba9a792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "b56c3912-c718-44fa-8fad-b4f0c1958f5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqhxxYfVWJsCZa1mAg1ovh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3295,
      "cache_read_input_tokens": 85577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3295,
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
