# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. Produce a structur

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab5e8c9ac0a3c94bd.jsonl`
- **Structured JSON:** [`a67aa9f8a5540c18ac6d.json`](../../sessions/a6/a67aa9f8a5540c18ac6d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-21T15:07:31.320Z_

You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. Produce a structured review following the ARR format with scores at the end.

## Venue Calibration (EMNLP 2026 via ARR)
- Overall Assessment scale: 5=Award (top 2.5%), 4.5=Borderline Award, 4=Conference accept, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)
- Accept rate: ~21% for Main conference
- Auto-reject signals: anonymity violation, over page limit, missing Limitations section, hallucinated citations

## Paper Summary
**Title:** "Temporal Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis"

**Core idea:** Apply Mantel-Haenszel DIF analysis from psychometrics to the METABENCH response matrix (5,227 models × 12,508 MMLU items), splitting models into 2023 (reference, N=1,080) vs 2024-H1 (focal, N=807) temporal cohorts. Main finding: 31.3% of MMLU items show large DIF (ETS C class, |Δ_MH|≥1.5).

**4 Claims:**
1. **Empirical discovery at unprecedented scale**: 31.3% temporal instability, robust to threshold choice, multiple testing, architecture; replicated across 6 benchmarks (17.9–31.3%).
2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 against Li et al. labels is expected, not failure.
3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000) provides reusable infrastructure for validating any item-level detector. Portable across benchmarks (GSM8K ΔTPR=+0.818).
4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=−8 to −49σ vs random) but are the least disruptive non-random removal strategy. Simpson's paradox: domain improvement marginally predicts DIF (OR=1.55) but reverses (OR=0.73) after controlling for item properties.

**Structure (7 pages + appendices A–F):**
- §1 Introduction
- §2 Related Work (3 paragraphs: LLM Benchmark Contamination, Differential Item Functioning, LLM Benchmark Analysis)
- §3 Method
- §4 Experiments
- §5 Discussion and Limitations
- §6 Conclusion
- References: 15 entries (Holland & Thayer 1988, Holland & Wainer 1993, Mantel & Haenszel 1959, Zieky 1993, Perlitz et al. 2024, Shi et al. 2024, Blebea et al. 2024, Dodge et al. 2021, Li et al. 2024, Kiela et al. 2021, Liang et al. 2023, Ivison et al. 2024, Polo et al. 2024, Sinharay et al. 2006, Tutz & Berger 2016, Zhang et al. 2024)
- Appendices A–F

**Related Work Section (§2) covers:**
1. **LLM Benchmark Contamination**: Min-K% (Shi et al. 2024), ConStat (Blebea et al. 2024), n-gram overlap (Dodge et al. 2021; Li et al. 2024). The paper argues these all rely on web-overlap or memorization-based labels as validation ground truth, measuring global exposure rather than differential functioning.
2. **Differential Item Functioning**: MH-DIF (Holland & Thayer 1988; Mantel & Haenszel 1959) as standard in educational testing. ETS classification (Zieky 1993). Paper claims empirical findings at unprecedented scale, not methodological innovation.
3. **LLM Benchmark Analysis**: Item difficulty distributions (Polo et al. 2024), benchmark saturation (Kiela et al. 2021), evaluation methodology (Liang et al. 2023), Growing Pains anchor items (Ivison et al. 2024). Paper positions itself as complementing this by identifying which anchor items may be degrading.

**Key methodological elements:**
- MH-DIF is a classical psychometric method (1959/1988) — no modification claimed
- Cross-subject matching for semi-synthetic validation: innovation is using scores on OTHER subjects as the matching variable to avoid FPR inflation from injected contamination
- Simpson's paradox decomposition via logistic regression
- Proposition 1 (mentioned in review context but may be implicit in paper): ΔFPR=0 for cross-subject matching — described as algebraically straightforward by some potential reviewers
- Cumulative Bayesian DIF (Sinharay et al. 2006) applied to LLM context in appendix

**Experiment Design Reference:**
The paper was originally conceived as a "benchmark regeneration" project (using IRT equating to replace contaminated items) but pivoted to "DIF as diagnostic lens" after bifactor IRT failed to converge. The ensemble detection approach (DIF + ConStat + DVD) was also dropped. The final framing is: DIF reveals measurement properties of benchmarks, not contamination per se.

**Key tensions for novelty assessment:**
- MH-DIF is a well-known method being applied without modification to a new domain (LLM benchmarks). Is this sufficient novelty for a top venue?
- The cross-subject matching trick (ΔFPR=0) is described as "follows straightforwardly from independence" — is this a genuine contribution or obvious?
- The "instability ≠ invalidity" framing is conceptually interesting but potentially tautological (if rankings don't change, the instability is by definition non-threatening to validity)
- 6-benchmark replication provides breadth but may be seen as repetitive rather than adding insight
- Simpson's paradox finding is genuinely surprising and potentially the most novel analytical contribution
- The paper doesn't compare directly with ConStat/DVD (only conceptual argument + literature numbers)

**Potentially missing related work:**
Consider whether these areas are adequately covered:
- Other DIF methods beyond MH (Lord's χ², Raju's area, logistic regression DIF, SIBTEST)
- Recent work on benchmark contamination detection (beyond the 3 methods cited)
- Item Response Theory applications to LLM evaluation (any recent papers?)
- Test equating literature (relevant given the abandoned equating pilot)
- Benchmark dynamics / temporal analysis work
- Data contamination in foundation models (broader literature)
- Oren et al. 2023 or similar semi-synthetic contamination benchmarks
- Deng et al. 2023, Golchin & Surdeanu 2023, or other contamination detection papers
- Benchmark design and renewal work (e.g., dynamic benchmarking)

## Your Review Task

Evaluate the **novelty**, **positioning**, and **related work completeness**. Specifically assess:

1. **Novelty of contribution**: Is applying an unmodified classical method (MH-DIF) to a new domain (LLM benchmarks) sufficient for EMNLP 2026? How does this compare to typical novelty expectations?
2. **Framing and positioning**: Is the pivot from "contamination detection" to "diagnostic lens" well-executed? Does the paper clearly differentiate from existing contamination detection work?
3. **Related work completeness**: Are there important missing citations? Is the existing literature fairly represented?
4. **Cross-subject matching**: Is this genuinely novel, or is it an obvious application of standard matching principles?
5. **Contribution balance**: Which of the 4 claims is the strongest/weakest contribution? Is the paper trying to claim too much?
6. **Comparison with existing methods**: Is the conceptual-only comparison with ConStat/DVD sufficient, or should direct empirical comparison be required?
7. **Impact and significance**: Will this work change how the community thinks about benchmark evaluation? Is the "instability ≠ invalidity" message impactful?

Produce your review in this format:

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list, each with brief explanation]

### Weaknesses
[Numbered list, each with brief explanation]

### Questions for Authors
[Numbered list]

### Minor Issues
[Numbered list]

### Missing References
[Any important missing citations]

### Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall Assessment: X.X (with label from the scale)
- Confidence: X/5
```

Be rigorous but fair. Calibrate to EMNLP 2026 standards where ~21% of submissions are accepted to Main and another ~15-20% to Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "70469d5f-5684-4186-81a3-b8047e1f0a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T15:07:31.324Z_

```json
{
  "parentUuid": "70469d5f-5684-4186-81a3-b8047e1f0a47",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
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
  "uuid": "458ebc27-2cfa-4503-a437-a3865832f844",
  "timestamp": "2026-05-21T15:07:31.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T15:07:38.001Z_



I'll start by reading the paper and its supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458ebc27-2cfa-4503-a437-a3865832f844",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWC3J7x48KPAFhnCJP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd22601-abcd-4180-a43d-ad677e722bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGbf75oCcYe2N1ym6YwviF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8599,
      "cache_read_input_tokens": 8686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8599,
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

_source line 4 · 2026-05-21T15:07:39.917Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GLL6mCTfh4LdTsKs954VhM`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd22601-abcd-4180-a43d-ad677e722bdf",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWC3J7x48KPAFhnCJP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7383de8c-391e-4e6a-aa35-6dc66335bead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGbf75oCcYe2N1ym6YwviF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8599,
      "cache_read_input_tokens": 8686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8599,
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

_source line 5 · 2026-05-21T15:07:39.939Z_

<details><summary>↩ Tool result · `toolu_01GLL6mCTfh4LdTsKs954VhM`</summary>

```text
paper/main.tex
paper/sections/appendix.tex
paper/sections/limitations.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/math_commands.tex
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/abstract.tex
paper/sections/discussion.tex
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7383de8c-391e-4e6a-aa35-6dc66335bead",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "b5f9c6a4-a187-4529-b295-01ae5f8e8f03",
  "sourceToolAssistantUUID": "7383de8c-391e-4e6a-aa35-6dc66335bead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T15:07:40.244Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0111xNbPopxbuAehEzJweyZL`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f9c6a4-a187-4529-b295-01ae5f8e8f03",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWC3J7x48KPAFhnCJP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c93dadc-721f-4e10-967d-b3ed6b1a0e5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGbf75oCcYe2N1ym6YwviF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8599,
      "cache_read_input_tokens": 8686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8599,
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

_source line 7 · 2026-05-21T15:07:40.254Z_

<details><summary>↩ Tool result · `toolu_0111xNbPopxbuAehEzJweyZL`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c93dadc-721f-4e10-967d-b3ed6b1a0e5b",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "01d7448d-f9c4-4b44-ad07-6cd6809c947a",
  "sourceToolAssistantUUID": "1c93dadc-721f-4e10-967d-b3ed6b1a0e5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T15:07:43.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ezi5m3tZ22kxhthUEJJFzw`</summary>

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
  "parentUuid": "01d7448d-f9c4-4b44-ad07-6cd6809c947a",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83e1569e-22c0-4458-ac17-d14ebcdce8f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 9 · 2026-05-21T15:07:43.236Z_

<details><summary>↩ Tool result · `toolu_01Ezi5m3tZ22kxhthUEJJFzw`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83e1569e-22c0-4458-ac17-d14ebcdce8f2",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "9ad02f0c-f774-4db6-8d00-6ba867b2a8cf",
  "sourceToolAssistantUUID": "83e1569e-22c0-4458-ac17-d14ebcdce8f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T15:07:43.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ly3WQS3ak8Q7qPB4VSHjdz`</summary>

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
  "parentUuid": "9ad02f0c-f774-4db6-8d00-6ba867b2a8cf",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "243ef897-4572-4dd0-8b4c-074521cd93cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 11 · 2026-05-21T15:07:43.660Z_

<details><summary>↩ Tool result · `toolu_01Ly3WQS3ak8Q7qPB4VSHjdz`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C; MMLU 95\% bootstrap CI: [29.4\%, 38.1\%]) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures temporal construct shift rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "243ef897-4572-4dd0-8b4c-074521cd93cb",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "96586f46-8137-45ff-8716-f6f9a7fa236b",
  "sourceToolAssistantUUID": "243ef897-4572-4dd0-8b4c-074521cd93cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T15:07:44.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YKeFQEu2hqQKXYJW5N8o1J`</summary>

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
  "parentUuid": "96586f46-8137-45ff-8716-f6f9a7fa236b",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d482f065-ac6c-4b6e-bb12-8932bb116df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 13 · 2026-05-21T15:07:44.740Z_

<details><summary>↩ Tool result · `toolu_01YKeFQEu2hqQKXYJW5N8o1J`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that MH-DIF is sensitive to differential item behavior when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}). MH-DIF detects \emph{that} items function differently across cohorts, not \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter. DIF-flagged items concentrate discriminative signal: removing them degrades ranking discriminability more than random removal ($z = -8\sigma$ to $-49\sigma$ across 21 conditions). Model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions under stable-item evaluation, while Mistral-based models lose a median of $35$; 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$.
18	
19	Our contributions are empirical and methodological, not algorithmic:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$ (45--174$\times$ above random baselines), with knowledge/reasoning benchmarks showing higher instability than procedural ones (\Cref{sec:temporal,sec:gsm8k}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal, Jaccard overlap with high-discrimination items $= 0.12$) and exhibit a structured difficulty--direction interaction ($\rho = -0.597$): capability gains concentrate on hard items while easy items erode (\Cref{sec:downstream}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d482f065-ac6c-4b6e-bb12-8932bb116df5",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "a250cec5-34a7-46b1-ab9b-e656cf1288c4",
  "sourceToolAssistantUUID": "d482f065-ac6c-4b6e-bb12-8932bb116df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T15:07:45.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_019J9rXAfXHfGZqqP9Uawf2G`</summary>

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
  "parentUuid": "a250cec5-34a7-46b1-ab9b-e656cf1288c4",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8e17269-67c6-4047-ae08-2660bbff314a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 15 · 2026-05-21T15:07:45.171Z_

<details><summary>↩ Tool result · `toolu_019J9rXAfXHfGZqqP9Uawf2G`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrated that not all evaluation examples are equally informative. Recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale, TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection, and scalability coefficients for detecting bad benchmark items \citep{hardy2026scalability}. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. Cross-subject matching---computing the stratification variable from domains other than the one being tested---has psychometric precedent in the DIF literature \citep{nandakumar1993dif,donoghue1993mh}; our adaptation addresses LLM-specific challenges of multi-domain local dependence and simultaneous contamination control at scale. We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Quality and Design.}
14	The Benchmark Health Index~\citep{liu2026bhi} assesses static benchmark quality; our temporal DIF analysis is complementary, diagnosing \emph{when} measurement properties shift rather than evaluating them at a single snapshot. \citet{maeda2025difllm} predict which item features associate with DIF in educational settings; we instead detect DIF empirically across LLM cohorts at scale. Dynamic benchmarks \citep{kiela2021dynabench, li2024latesteval, white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges that our DIF analysis directly addresses.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8e17269-67c6-4047-ae08-2660bbff314a",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "d4209562-9901-47cd-94db-8e48e172ed85",
  "sourceToolAssistantUUID": "a8e17269-67c6-4047-ae08-2660bbff314a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T15:07:45.701Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JNwFKTnsAWgnQYMFFMVkfP`</summary>

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
  "parentUuid": "d4209562-9901-47cd-94db-8e48e172ed85",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3770d51-c2be-4967-a295-5fe9466fd2e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 17 · 2026-05-21T15:07:45.707Z_

<details><summary>↩ Tool result · `toolu_01JNwFKTnsAWgnQYMFFMVkfP`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
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
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
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
37	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
38	
39	\subsection{Semi-Synthetic Injection Framework}
40	\label{sec:injection}
41	
42	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
43	
44	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
45	
46	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \emph{other than} the one being tested.
47	
48	\begin{proposition}[Zero FPR under cross-subject matching]
49	\label{prop:fpr}
50	Let $M_i^{(-s)} = \sum_{j \notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Since the tested item belongs to $s$, it does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\Delta\mathrm{FPR} = 0$ by construction.
51	\end{proposition}
52	
53	Empirically, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
54	
55	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3770d51-c2be-4967-a295-5fe9466fd2e4",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "b36ec1f5-4420-4e68-8a27-fd1d2d809536",
  "sourceToolAssistantUUID": "d3770d51-c2be-4967-a295-5fe9466fd2e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T15:07:45.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_0197F2VGJAxEV2nN8szV6Pb6`</summary>

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
  "parentUuid": "b36ec1f5-4420-4e68-8a27-fd1d2d809536",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvWrbXiH5VNi93QREvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6ec4064-6aae-4467-a827-8797a33fd293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2EmLVYy7bJkAmkVmJRW5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 17285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1207,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 19 · 2026-05-21T15:07:45.802Z_

<details><summary>↩ Tool result · `toolu_0197F2VGJAxEV2nN8szV6Pb6`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $N = 1{,}000$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$); within-subject matching on 5 subjects yields 38.1\% as a robustness check (\Cref{tab:temporal_landscape}). While DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), DIF direction exhibits systematic domain dependence: STEM items disproportionately favor 2024 models (55.4\%), while Humanities items favor 2023 models (64.4\%), suggesting model generations improve differentially across knowledge dimensions. Item-level logistic regression shows domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of instability is item-specific. Odds ratio regression reveals a Simpson's paradox: domain accuracy improvement positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$ per 10 pp, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$; LR $\chi^2 = 647$), confirming that item properties---not accuracy gains---drive DIF classification. The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{lcccc}
27	\toprule
28	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & FPR (clean) & Enrich. \\
29	\midrule
30	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
31	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
32	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
33	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
34	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\subsection{Ground Truth Mismatch}
40	\label{sec:groundtruth}
41	
42	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method. This near-independence extends to behavioral contamination detectors: the enrichment ratio of $0.964$ and Jaccard overlap of $0.206$ between DIF flags and web-overlap labels imply that any detector validated against these labels---including ConStat~\citep{dekoninck2024constat}---is evaluated on a ground truth orthogonal to differential functioning.
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
47	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
48	\label{fig:dose_response}
49	\end{figure}
50	
51	\subsection{Structural Analysis}
52	\label{sec:structural}
53	
54	Three structural controls fail to reduce temporal C\% below 31\%: matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$, FPR $= 0.312$), and within-subject DIF (C\% $= 38.1\%$, exceeding the 25\% bifactor viability threshold). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% estimate conservative. Graduated de-duplication ($K{=}10$: 22.7\% vs.\ random 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%) confirms family structure does not inflate C\%. Ability-matched within-family analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\% \pm 1.6\%$ (Cohen's $d = -0.99$, overlap $= 0.18$), while temporal matching reduces C\% from 31.3\% to $28.9\% \pm 0.1\%$ ($d = -0.17$, overlap $= 0.76$). The matched C\% values ($\sim$28--29\%) are consistent with each other despite vastly different unmatched rates (61.3\% vs.\ 31.3\%), suggesting that genuine item-level DIF accounts for $\sim$28--29\% of items, with the Llama comparison carrying 33 pp of additional ability confound (54\% reduction) versus only 2.4 pp for temporal cohorts (7.7\% reduction). In total, six alternative explanations were tested and ruled out: ability confounding, model family inflation, IRT $\theta$-conditioning, within-subject effects, aggregate ranking impact, and local item dependence---none reduces C\% below $\sim$28\%, confirming item-level differential functioning. Full details in \Cref{app:structural}.
55	
56	\subsection{Semi-Synthetic Framework Validation}
57	\label{sec:semisynthetic}
58	
59	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
60	
61	\subsection{Downstream Impact}
62	\label{sec:downstream}
63	
64	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions (mean ${+}121$), while Mistral-based models lose a median of $35$ (mean $-54$); individual extremes reach ${+}793$ and $-542$ (\Cref{app:fig_downstream}). Overall, 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$. These shifts exhibit systematic cohort directionality: removing C-flagged items disproportionately disadvantages 2024 models (mean rank drop $= 73.6$ positions) while 2023 models rise (mean $\Delta\mathrm{rank} = -22.6$), yielding a cohort gap of $96.2$ positions---$40\times$ larger than under random removal of equal count ($2.4$; $t(19) > 4$, $p < 0.001$). This what-if demonstration confirms that DIF items carry concentrated inter-generational discriminative signal; it does not recommend using DIF-cleaned scores for evaluation. \Cref{sec:gsm8k} demonstrates that this instability pattern extends across all six METABENCH benchmarks.
65	
66	\subsection{Cross-Benchmark Validation}
67	\label{sec:gsm8k}
68	
69	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag) to 31.3\% (MMLU), each 45--174$\times$ above its random-split baseline---none attributable to sampling noise. A task-type dichotomy emerges: knowledge and reasoning benchmarks (MMLU, WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$, while procedural benchmarks (GSM8K, HellaSwag~\citep{zellers2019hellaswag}) show C\% $= 17.9$--$18.9\%$, consistent with knowledge-intensive items being more sensitive to shifts in training data composition across model generations.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts. All six show substantial instability (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
74	\label{tab:cross_benchmark}
75	\small
76	\begin{tabular}{lrrrl}
77	\toprule
78	Benchmark & Items & C\% & Rand.\ C\% & Ratio \\
79	\midrule
80	MMLU & 12{,}508 & 31.3 & 0.18 & 174$\times$ \\
81	WinoGrande & 1{,}267 & 30.3 & 0.32 & 95$\times$ \\
82	TruthfulQA & 817 & 29.7 & 0.37 & 80$\times$ \\
83	ARC & 1{,}172 & 26.9 & 0.60 & 45$\times$ \\
84	GSM8K & 1{,}319 & 18.9 & 0.30 & 63$\times$ \\
85	HellaSwag & 10{,}042 & 17.9 & 0.28 & 64$\times$ \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	On GSM8K specifically, semi-synthetic injection with external matching confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}). An exploratory GSM1K analysis ($N = 33$) shows a negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$, $p = 0.005$; partial $r = -0.385$, $p = 0.027$), suggesting DIF captures capability change distinct from memorization (\Cref{app:fig_gsm1k}).
91	
92	Even within a 6-month window (2023-H2 vs.\ 2024-H1), DIF remains substantial (MMLU C\% $= 34.35\%$, 181$\times$; TruthfulQA C\% $= 31.33\%$, 51$\times$ above random baselines).
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6ec4064-6aae-4467-a827-8797a33fd293",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "3855f809-3fb5-4981-8e9d-73628a5e6bbe",
  "sourceToolAssistantUUID": "c6ec4064-6aae-4467-a827-8797a33fd293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T15:07:51.768Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XKiED2AwV87JbnyZjgjybz`</summary>

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
  "parentUuid": "3855f809-3fb5-4981-8e9d-73628a5e6bbe",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXG7eBCVHQLcy2kzXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "343bbddf-cace-41f0-a0d3-51ca4105a4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gcb36EZ5bMmdsvVo7eodnX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11788,
      "cache_read_input_tokens": 18492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11788,
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

_source line 21 · 2026-05-21T15:07:51.891Z_

<details><summary>↩ Tool result · `toolu_01XKiED2AwV87JbnyZjgjybz`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations. The statistical machinery of DIF---originally designed for demographic fairness testing~\citep{holland1988mh}---transfers to temporal cohort comparisons unchanged, requiring only a binary response matrix and cohort labels.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) exposes a category error: web-overlap labels measure global exposure shared by nearly all MMLU items, so evaluating a differential method against them conflates two phenomena.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. Yen's Q3 confirms local dependence does not drive DIF ($r = 0.09$, $p = 0.50$).
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol: (1)~MH-DIF audits whenever $\geq 500$ new models accumulate, using cross-subject matching; (2)~C\% $> 20\%$ triggers item review, with consecutively flagged items labeled ``unstable'' and flip-flopping items tagged ``volatile''; (3)~graduated responses from flag-and-annotate to item rotation. MMLU's C\% $= 31.3\%$ already exceeds this threshold ($\chi^2$ $p = 0.32$).
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "343bbddf-cace-41f0-a0d3-51ca4105a4db",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "fe07c8cd-7b52-41ea-bc4e-90c968cab783",
  "sourceToolAssistantUUID": "343bbddf-cace-41f0-a0d3-51ca4105a4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T15:07:51.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AgB3yhw5jNQ5mkFBo7Hptc`</summary>

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
  "parentUuid": "fe07c8cd-7b52-41ea-bc4e-90c968cab783",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXG7eBCVHQLcy2kzXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "272b3bb4-82d5-4f7a-9797-7d56b10a9508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gcb36EZ5bMmdsvVo7eodnX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11788,
      "cache_read_input_tokens": 18492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11788,
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

_source line 23 · 2026-05-21T15:07:51.986Z_

<details><summary>↩ Tool result · `toolu_01AgB3yhw5jNQ5mkFBo7Hptc`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	MH-DIF analysis of six METABENCH benchmarks (27,125 items, 5,227 models) reveals 17.9--31.3\% temporal item instability (ETS~C); a Simpson's paradox confirms item properties, not accuracy gains, drive DIF. Web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework validates detection power ($\Delta\mathrm{FPR} = 0.000$). DIF-flagged items concentrate discriminative information ($z{=}{-}8\sigma$ to ${-}49\sigma$) with a difficulty--direction interaction ($\rho{=}{-}0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring alongside score reporting.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "272b3bb4-82d5-4f7a-9797-7d56b10a9508",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "30176ae6-b6de-4d25-b135-1152a8831e9f",
  "sourceToolAssistantUUID": "272b3bb4-82d5-4f7a-9797-7d56b10a9508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T15:07:52.448Z_

<details open><summary>🔧 Tool call — Read · `toolu_0179rxJ9eAUeZTPwFUZXCv4L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30176ae6-b6de-4d25-b135-1152a8831e9f",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXG7eBCVHQLcy2kzXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f462f550-94e1-4d7c-9ed9-770beb5aeaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gcb36EZ5bMmdsvVo7eodnX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11788,
      "cache_read_input_tokens": 18492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11788,
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

_source line 25 · 2026-05-21T15:07:52.455Z_

<details><summary>↩ Tool result · `toolu_0179rxJ9eAUeZTPwFUZXCv4L`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragraph{Contamination vs.\ capability change.}
13	DIF analysis detects \emph{that} items function differently across cohorts but cannot determine \emph{why}. The differential signal may reflect contamination, capability change, training methodology shifts, or interactions among these factors. We present evidence that DIF captures something distinct from memorization (negative GSM1K correlation, semi-synthetic dose-response), but a definitive causal decomposition remains out of reach without access to model training data.
14	
15	\paragraph{Benchmark scope.}
16	We analyze six METABENCH benchmarks (MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag; 27,125 total items), all multiple-choice or short-answer benchmarks scored as binary correct/incorrect. The generalizability to open-ended generation benchmarks (e.g., AlpacaEval, MT-Bench), coding benchmarks (e.g., HumanEval), or benchmarks with non-binary scoring remains untested. The binary response format is a prerequisite for MH-DIF; extending to continuous or partial-credit scoring would require polytomous DIF methods.
17	
18	\paragraph{Temporal cohort definition.}
19	We define cohorts by calendar year of model release (2023 vs.\ 2024), a coarse grouping that aggregates models with diverse training pipelines, data mixtures, and post-training procedures. Finer-grained cohort definitions (e.g., by training data cutoff, model family, or alignment method) might reveal more targeted patterns of item instability but would reduce per-cohort sample sizes and statistical power.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f462f550-94e1-4d7c-9ed9-770beb5aeaa9",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "c5dea50f-d429-43e6-ac91-3a9236d6774b",
  "sourceToolAssistantUUID": "f462f550-94e1-4d7c-9ed9-770beb5aeaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T15:07:52.982Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Ds6VFfTNKiXBxbacGJSCu`</summary>

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
  "parentUuid": "c5dea50f-d429-43e6-ac91-3a9236d6774b",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXG7eBCVHQLcy2kzXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc153eb3-2a63-471f-9065-be7100165eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gcb36EZ5bMmdsvVo7eodnX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11788,
      "cache_read_input_tokens": 18492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11788,
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

_source line 27 · 2026-05-21T15:07:52.987Z_

<details><summary>↩ Tool result · `toolu_016Ds6VFfTNKiXBxbacGJSCu`</summary>

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
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
40	\midrule
41	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
42	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
43	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
44	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\section{Additional Figures}
50	\label{app:figures}
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
55	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
56	\label{app:fig_matching}
57	\end{figure}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
62	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
63	\label{app:fig_downstream}
64	\end{figure}
65	
66	\begin{figure}[h]
67	\centering
68	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
69	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
70	\label{app:fig_gsm1k}
71	\end{figure}
72	
73	\section{Cross-Benchmark Comparison}
74	\label{app:gsm8k_details}
75	
76	\begin{table}[h]
77	\centering
78	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
79	\label{tab:gsm8k_comparison}
80	\small
81	\begin{tabular}{lcc}
82	\toprule
83	Metric & MMLU & GSM8K \\
84	\midrule
85	Items & 12,508 & 1,319 \\
86	Models & 5,227 & 6,702 \\
87	Temporal C\% & 31.3\% & 18.9\% \\
88	Sanity C\% & 0.18\% & 0.3\% \\
89	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
90	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc153eb3-2a63-471f-9065-be7100165eac",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "02821ba4-c7f7-4229-a03b-47acfa5098a4",
  "sourceToolAssistantUUID": "cc153eb3-2a63-471f-9065-be7100165eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T15:07:53.516Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NS9B6pzd1hqWzBGeDSy3nb`</summary>

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
  "parentUuid": "02821ba4-c7f7-4229-a03b-47acfa5098a4",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXG7eBCVHQLcy2kzXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07e89405-7661-435c-9474-3e7c98b365fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gcb36EZ5bMmdsvVo7eodnX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11788,
      "cache_read_input_tokens": 18492,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 18492,
          "cache_creation_input_tokens": 11788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11788,
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

_source line 29 · 2026-05-21T15:07:53.520Z_

<details><summary>↩ Tool result · `toolu_01NS9B6pzd1hqWzBGeDSy3nb`</summary>

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
97	@inproceedings{rodriguez2021evaluation,
98	  title     = {Evaluation Examples Are Not Equally Informative: How Should That Change {NLP} Leaderboards?},
99	  author    = {Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
100	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
101	  year      = {2021},
102	  pages     = {4486--4503}
103	}
104	
105	@article{donoghue1993mh,
106	  title   = {An Empirical Examination of the {Mantel-Haenszel} Statistic for the Study of Differential Item Functioning},
107	  author  = {Donoghue, John R. and Allen, Nancy L.},
108	  journal = {Applied Measurement in Education},
109	  volume  = {6},
110	  number  = {2},
111	  pages   = {163--179},
112	  year    = {1993}
113	}
114	
115	@misc{hardy2026scalability,
116	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
117	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
118	  year          = {2026},
119	  eprint        = {2603.24999},
120	  archivePrefix = {arXiv},
121	  primaryClass  = {cs.CL},
122	  url           = {https://arxiv.org/abs/2603.24999}
123	}
124	
125	@article{kim2019fpc,
126	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
127	  author  = {Kim, Seonghoon and Kolen, Michael},
128	  journal = {Applied Measurement in Education},
129	  year    = {2019},
130	  doi     = {10.1080/08957347.2019.1660344},
131	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
132	}
133	
134	@inproceedings{lalor2019irt,
135	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
136	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
137	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
138	  year      = {2019},
139	  doi       = {10.18653/v1/D19-1434},
140	  url       = {https://aclanthology.org/D19-1434/}
141	}
142	
143	@inproceedings{vania2021irt,
144	  title     = {Comparing Test Sets with Item Response Theory},
145	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
146	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
147	  year      = {2021},
148	  doi       = {10.18653/v1/2021.acl-long.92},
149	  url       = {https://aclanthology.org/2021.acl-long.92/}
150	}
151	
152	@misc{li2025atlas,
153	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
154	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
155	  year          = {2025},
156	  eprint        = {2511.04689},
157	  archivePrefix = {arXiv},
158	  primaryClass  = {cs.CL},
159	  url           = {https://arxiv.org/abs/2511.04689}
160	}
161	
162	@misc{chen2025irtnet,
163	  title         = {Learning Compact Representations of {LLM} Abilities via Item Response Theory},
164	  author        = {Chen, Jiayi and Wang, Chao and Zhang, Guoqiang and Ye, Peijin and Bai, Lei and Hu, Wenjun and Qu, Yongchao and Hu, Songlin},
165	  year          = {2025},
166	  eprint        = {2510.00844},
167	  archivePrefix = {arXiv},
168	  primaryClass  = {cs.CL},
169	  url           = {https://arxiv.org/abs/2510.00844}
170	}
171	
172	@misc{choi2026llmjudgeirt,
173	  title         = {Diagnosing the Reliability of {LLM}-as-a-Judge via Item Response Theory},
174	  author        = {Choi, Jiseong and Park, Seonho and Cho, Changwon and Park, Hojun and Kim, Bumsoo},
175	  year          = {2026},
176	  eprint        = {2602.00521},
177	  archivePrefix = {arXiv},
178	  primaryClass  = {cs.CL},
179	  url           = {https://arxiv.org/abs/2602.00521}
180	}
181	
182	@misc{habba2026growingpains,
183	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
184	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
185	  year          = {2026},
186	  eprint        = {2604.12843},
187	  archivePrefix = {arXiv},
188	  primaryClass  = {cs.CL},
189	  url           = {https://arxiv.org/abs/2604.12843}
190	}
191	
192	@inproceedings{zhou2026psnirt,
193	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
194	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
195	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
196	  year      = {2026},
197	  url       = {https://arxiv.org/abs/2505.15055}
198	}
199	
200	% ============================================================
201	% Dynamic Benchmark Design
202	% ============================================================
203	
204	@inproceedings{white2025livebench,
205	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
206	  author    = {White, Colin},
207	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
208	  year      = {2025},
209	  doi       = {10.48550/arXiv.2406.19314},
210	  url       = {https://arxiv.org/abs/2406.19314}
211	}
212	
213	@misc{kipnis2024metabench,
214	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
215	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
216	  year          = {2024},
217	  eprint        = {2407.12844},
218	  archivePrefix = {arXiv},
219	  primaryClass  = {cs.CL},
220	  url           = {https://arxiv.org/abs/2407.12844}
221	}
222	
223	@inproceedings{hendrycks2021mmlu,
224	  title     = {Measuring Massive Multitask Language Understanding},
225	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
226	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
227	  year      = {2021},
228	  url       = {https://arxiv.org/abs/2009.03300}
229	}
230	
231	@article{liang2023helm,
232	  title   = {Holistic Evaluation of Language Models},
233	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya},
234	  journal = {Transactions on Machine Learning Research},
235	  year    = {2023},
236	  doi     = {10.1111/nyas.15007},
237	  url     = {https://arxiv.org/abs/2211.09110}
238	}
239	
240	@inproceedings{chiang2024chatbot,
241	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
242	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
243	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
244	  year      = {2024},
245	  doi       = {10.48550/arXiv.2403.04132},
246	  url       = {https://arxiv.org/abs/2403.04132}
247	}
248	
249	@misc{mialon2023gaia,
250	  title         = {{GAIA}: a benchmark for General {AI} Assistants},
251	  author        = {Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
252	  year          = {2023},
253	  eprint        = {2311.12983},
254	  archivePrefix = {arXiv},
255	  primaryClass  = {cs.CL},
256	  url           = {https://arxiv.org/abs/2311.12983}
257	}
258	
259	@inproceedings{li2024latesteval,
260	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
261	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
262	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
263	  year      = {2024},
264	  doi       = {10.48550/arXiv.2312.12343},
265	  url       = {https://arxiv.org/abs/2312.12343}
266	}
267	
268	@inproceedings{kiela2021dynabench,
269	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
270	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
271	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
272	  year      = {2021},
273	  doi       = {10.18653/v1/2021.naacl-main.324},
274	  url       = {https://arxiv.org/abs/2104.14337}
275	}
276	
277	% ============================================================
278	% DIF Statistical Methods
279	% ============================================================
280	
281	@article{belzak2020smallsample,
282	  title   = {Testing Differential Item Functioning in Small Samples},
283	  author  = {Belzak, William},
284	  journal = {Multivariate Behavioral Research},
285	  year    = {2020},
286	  doi     = {10.1080/00273171.2019.1671162},
287	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
288	}
289	
290	@incollection{holland1988mh,
291	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
292	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
293	  booktitle = {Test Validity},
294	  editor    = {Wainer, Howard and Braun, Henry I.},
295	  publisher = {Lawrence Erlbaum Associates},
296	  year      = {1988},
297	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
298	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
299	}
300	
301	@article{shealy1993sibtest,
302	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
303	  author  = {Shealy, Robin and Stout, William},
304	  journal = {Psychometrika},
305	  year    = {1993},
306	  doi     = {10.1007/BF02294572},
307	  url     = {https://link.springer.com/article/10.1007/BF02294572}
308	}
309	
310	@article{clauser1998dif,
311	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
312	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
313	  journal = {Educational Measurement: Issues and Practice},
314	  year    = {1998},
315	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
316	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
317	}
318	
319	@book{zumbo1999handbook,
320	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
321	  author    = {Zumbo, Bruno D.},
322	  year      = {1999},
323	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
324	  address   = {Ottawa},
325	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
326	}
327	
328	@article{meredith1993invariance,
329	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
330	  author  = {Meredith, William},
331	  journal = {Psychometrika},
332	  year    = {1993},
333	  doi     = {10.1007/BF02294825},
334	  url     = {https://link.springer.com/article/10.1007/BF02294825}
335	}
336	
337	@article{vandenberg2000invariance,
338	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
339	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
340	  journal = {Organizational Research Methods},
341	  year    = {2000},
342	  doi     = {10.1177/109442810031002},
343	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
344	}
345	
346	@article{swaminathan1990logistic,
347	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
348	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
349	  journal = {Journal of Educational Measurement},
350	  year    = {1990},
351	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
352	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
353	}
354	
355	@article{teresi2007dif,
356	  title   = {Differential Item Functioning and Health Assessment},
357	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
358	  journal = {Quality of Life Research},
359	  year    = {2007},
360	  doi     = {10.1007/s11136-007-9184-6},
361	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
362	}
363	
364	@book{lord1980irt,
365	  title     = {Applications of Item Response Theory to Practical Testing Problems},
366	  author    = {Lord, Frederic M.},
367	  year      = {1980},
368	  publisher = {Lawrence Erlbaum Associates},
369	  address   = {Hillsdale, NJ}
370	}
371	
372	@article{raju1988area,
373	  title   = {The Area between Two Item Characteristic Curves},
374	  author  = {Raju, Nambury S.},
375	  journal = {Psychometrika},
376	  year    = {1988},
377	  doi     = {10.1007/BF02294403},
378	  url     = {https://link.springer.com/article/10.1007/BF02294403}
379	}
380	
381	@article{muthen1985mimic,
382	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
383	  author  = {Muth{\'e}n, Bengt},
384	  journal = {Journal of Educational Statistics},
385	  year    = {1985},
386	  doi     = {10.2307/1164966}
387	}
388	
389	@article{woods2009mimic,
390	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
391	  author  = {Woods, Carol M.},
392	  journal = {Applied Psychological Measurement},
393	  year    = {2009},
394	  doi     = {10.1177/0146621609331279}
395	}
396	
397	% ============================================================
398	% LLM Evaluation Methodology
399	% ============================================================
400	
401	@article{burnell2023rethink,
402	  title   = {Rethink reporting of evaluation results in {AI}},
403	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
404	  journal = {Science},
405	  year    = {2023},
406	  doi     = {10.1126/science.adf6369},
407	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
408	}
409	
410	@article{chang2024survey,
411	  title   = {A Survey on Evaluation of Large Language Models},
412	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
413	  journal = {ACM Transactions on Intelligent Systems and Technology},
414	  year    = {2024},
415	  doi     = {10.1145/3641289},
416	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
417	}
418	
419	@inproceedings{maiapolo2024tinybenchmarks,
420	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
421	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
422	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
423	  year      = {2024},
424	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
425	}
426	
427	@inproceedings{wang2024mmlupro,
428	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
429	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Xue, Xiang and Chen, Wenhu},
430	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
431	  year      = {2024},
432	  url       = {https://arxiv.org/abs/2406.01574}
433	}
434	
435	@article{ott2022benchmark,
436	  title   = {Mapping global dynamics of benchmark creation and saturation in artificial intelligence},
437	  author  = {Ott, Simon and Barbosa-Silva, Adriano and Blagec, Kathrin and Brauner, Jan and Samwald, Matthias},
438	  journal = {Nature Communications},
439	  year    = {2022},
440	  doi     = {10.1038/s41467-022-34591-0},
441	  url     = {https://www.nature.com/articles/s41467-022-34591-0}
442	}
443	
444	@article{nandakumar1993dif,
445	  author  = {Ratna Nandakumar},
446	  title   = {Simultaneous {DIF} amplification and cancellation: {Shealy}-{Stout}'s test for {DIF}},
447	  journal = {Journal of Educational Measurement},
448	  year    = {1993},
449	  volume  = {30},
450	  number  = {4},
451	  pages   = {293--311}
452	}
453	
454	@inproceedings{carlini2022quantifying,
455	  author    = {Nicholas Carlini and Daphne Ippolito and Matthew Jagielski and Katherine Lee and Florian Tram{\`e}r and Chiyuan Zhang},
456	  title     = {Quantifying Memorization Across Neural Language Models},
457	  booktitle = {International Conference on Learning Representations (ICLR)},
458	  year      = {2023},
459	  url       = {https://arxiv.org/abs/2202.07646}
460	}
461	
462	@inproceedings{tirumala2022memorization,
463	  author    = {Kushal Tirumala and Aram Markosyan and Luke Zettlemoyer and Armen Aghajanyan},
464	  title     = {Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models},
465	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
466	  year      = {2022},
467	  url       = {https://arxiv.org/abs/2205.10770}
468	}
469	
470	% ============================================================
471	% Additional Benchmarks
472	% ============================================================
473	
474	@inproceedings{sakaguchi2021winogrande,
475	  title     = {{WinoGrande}: An Adversarial {Winograd} Schema Challenge at Scale},
476	  author    = {Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
477	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
478	  volume    = {34},
479	  number    = {05},
480	  pages     = {8732--8740},
481	  year      = {2020}
482	}
483	
484	@inproceedings{lin2022truthfulqa,
485	  title     = {{TruthfulQA}: Measuring How Models Mimic Human Falsehoods},
486	  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
487	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
488	  year      = {2022},
489	  pages     = {3214--3252}
490	}
491	
492	@inproceedings{zellers2019hellaswag,
493	  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},
494	  author    = {Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farzaneh, Ali and Choi, Yejin},
495	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
496	  year      = {2019},
497	  pages     = {4791--4800}
498	}
499	
500	@article{clark2018arc,
501	  title   = {Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
502	  author  = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
503	  journal = {arXiv preprint arXiv:1803.05457},
504	  year    = {2018}
505	}
506	
507	% ============================================================
508	% Benchmark Quality Assessment
509	% ============================================================
510	
511	@article{liu2026bhi,
512	  title   = {Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of {LLMs}},
513	  author  = {Liu, Yifan and others},
514	  journal = {arXiv preprint arXiv:2602.11674},
515	  year    = {2026}
516	}
517	
518	@article{maeda2025difllm,
519	  title   = {Finding Words Associated with {DIF}: Predicting {DIF} using {LLMs} and Explainable {AI}},
520	  author  = {Maeda, Hotaka},
521	  journal = {arXiv preprint arXiv:2502.07017},
522	  year    = {2025}
523	}
524	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07e89405-7661-435c-9474-3e7c98b365fc",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "f3b99842-2e33-4271-806e-48a3dd554d52",
  "sourceToolAssistantUUID": "07e89405-7661-435c-9474-3e7c98b365fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T15:07:59.630Z_

Now let me check the figures directory and any additional artifacts to understand the full scope of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b99842-2e33-4271-806e-48a3dd554d52",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXqkTnKkVxiyCUL1ra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75bd358f-8c25-449a-a3ba-747c910aa483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwKGK2e7KWvETikYLYtqpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14402,
      "cache_read_input_tokens": 30280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14402,
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

_source line 31 · 2026-05-21T15:08:01.875Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FBgDummbzyotDJfRcUbPNp`</summary>

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
  "parentUuid": "75bd358f-8c25-449a-a3ba-747c910aa483",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXqkTnKkVxiyCUL1ra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20f4c056-b04a-4239-b358-60c3f2cd7acb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwKGK2e7KWvETikYLYtqpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14402,
      "cache_read_input_tokens": 30280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14402,
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

_source line 32 · 2026-05-21T15:08:01.897Z_

<details><summary>↩ Tool result · `toolu_01FBgDummbzyotDJfRcUbPNp`</summary>

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
  "parentUuid": "20f4c056-b04a-4239-b358-60c3f2cd7acb",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "d7c1de54-07d5-4d75-bcc5-cf3701b9661c",
  "sourceToolAssistantUUID": "20f4c056-b04a-4239-b358-60c3f2cd7acb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T15:08:02.272Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AbEK8SpTexi8kFJHnkTuLm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7c1de54-07d5-4d75-bcc5-cf3701b9661c",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvXqkTnKkVxiyCUL1ra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22c4a08f-324d-42fd-9c5a-08b59c9d2b62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwKGK2e7KWvETikYLYtqpQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14402,
      "cache_read_input_tokens": 30280,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 30280,
          "cache_creation_input_tokens": 14402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14402,
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

_source line 34 · 2026-05-21T15:08:02.277Z_

<details><summary>↩ Tool result · `toolu_01AbEK8SpTexi8kFJHnkTuLm`</summary>

```text
1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	\usepackage{amsthm}
5	\newtheorem{proposition}{Proposition}
6	
7	% Mark sections of captions for referring to divisions of figures
8	\newcommand{\figleft}{{\em (Left)}}
9	\newcommand{\figcenter}{{\em (Center)}}
10	\newcommand{\figright}{{\em (Right)}}
11	\newcommand{\figtop}{{\em (Top)}}
12	\newcommand{\figbottom}{{\em (Bottom)}}
13	\newcommand{\captiona}{{\em (a)}}
14	\newcommand{\captionb}{{\em (b)}}
15	\newcommand{\captionc}{{\em (c)}}
16	\newcommand{\captiond}{{\em (d)}}
17	
18	% Highlight a newly defined term
19	\newcommand{\newterm}[1]{{\bf #1}}
20	
21	
22	% Figure reference, lower-case.
23	\def\figref#1{figure~\ref{#1}}
24	% Figure reference, capital. For start of sentence
25	\def\Figref#1{Figure~\ref{#1}}
26	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
27	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
28	% Section reference, lower-case.
29	\def\secref#1{section~\ref{#1}}
30	% Section reference, capital.
31	\def\Secref#1{Section~\ref{#1}}
32	% Reference to two sections.
33	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
34	% Reference to three sections.
35	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
36	% Reference to an equation, lower-case.
37	\def\eqref#1{equation~\ref{#1}}
38	% Reference to an equation, upper case
39	\def\Eqref#1{Equation~\ref{#1}}
40	% A raw reference to an equation---avoid using if possible
41	\def\plaineqref#1{\ref{#1}}
42	% Reference to a chapter, lower-case.
43	\def\chapref#1{chapter~\ref{#1}}
44	% Reference to an equation, upper case.
45	\def\Chapref#1{Chapter~\ref{#1}}
46	% Reference to a range of chapters
47	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
48	% Reference to an algorithm, lower-case.
49	\def\algref#1{algorithm~\ref{#1}}
50	% Reference to an algorithm, upper case.
51	\def\Algref#1{Algorithm~\ref{#1}}
52	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
53	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
54	% Reference to a part, lower case
55	\def\partref#1{part~\ref{#1}}
56	% Reference to a part, upper case
57	\def\Partref#1{Part~\ref{#1}}
58	\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}
59	
60	\def\ceil#1{\lceil #1 \rceil}
61	\def\floor#1{\lfloor #1 \rfloor}
62	\def\1{\bm{1}}
63	\newcommand{\train}{\mathcal{D}}
64	\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
65	\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}
66	
67	\def\eps{{\epsilon}}
68	
69	
70	% Random variables
71	\def\reta{{\textnormal{$\eta$}}}
72	\def\ra{{\textnormal{a}}}
73	\def\rb{{\textnormal{b}}}
74	\def\rc{{\textnormal{c}}}
75	\def\rd{{\textnormal{d}}}
76	\def\re{{\textnormal{e}}}
77	\def\rf{{\textnormal{f}}}
78	\def\rg{{\textnormal{g}}}
79	\def\rh{{\textnormal{h}}}
80	\def\ri{{\textnormal{i}}}
81	\def\rj{{\textnormal{j}}}
82	\def\rk{{\textnormal{k}}}
83	\def\rl{{\textnormal{l}}}
84	% rm is already a command, just don't name any random variables m
85	\def\rn{{\textnormal{n}}}
86	\def\ro{{\textnormal{o}}}
87	\def\rp{{\textnormal{p}}}
88	\def\rq{{\textnormal{q}}}
89	\def\rr{{\textnormal{r}}}
90	\def\rs{{\textnormal{s}}}
91	\def\rt{{\textnormal{t}}}
92	\def\ru{{\textnormal{u}}}
93	\def\rv{{\textnormal{v}}}
94	\def\rw{{\textnormal{w}}}
95	\def\rx{{\textnormal{x}}}
96	\def\ry{{\textnormal{y}}}
97	\def\rz{{\textnormal{z}}}
98	
99	% Random vectors
100	\def\rvepsilon{{\mathbf{\epsilon}}}
101	\def\rvtheta{{\mathbf{\theta}}}
102	\def\rva{{\mathbf{a}}}
103	\def\rvb{{\mathbf{b}}}
104	\def\rvc{{\mathbf{c}}}
105	\def\rvd{{\mathbf{d}}}
106	\def\rve{{\mathbf{e}}}
107	\def\rvf{{\mathbf{f}}}
108	\def\rvg{{\mathbf{g}}}
109	\def\rvh{{\mathbf{h}}}
110	\def\rvu{{\mathbf{i}}}
111	\def\rvj{{\mathbf{j}}}
112	\def\rvk{{\mathbf{k}}}
113	\def\rvl{{\mathbf{l}}}
114	\def\rvm{{\mathbf{m}}}
115	\def\rvn{{\mathbf{n}}}
116	\def\rvo{{\mathbf{o}}}
117	\def\rvp{{\mathbf{p}}}
118	\def\rvq{{\mathbf{q}}}
119	\def\rvr{{\mathbf{r}}}
120	\def\rvs{{\mathbf{s}}}
121	\def\rvt{{\mathbf{t}}}
122	\def\rvu{{\mathbf{u}}}
123	\def\rvv{{\mathbf{v}}}
124	\def\rvw{{\mathbf{w}}}
125	\def\rvx{{\mathbf{x}}}
126	\def\rvy{{\mathbf{y}}}
127	\def\rvz{{\mathbf{z}}}
128	
129	% Elements of random vectors
130	\def\erva{{\textnormal{a}}}
131	\def\ervb{{\textnormal{b}}}
132	\def\ervc{{\textnormal{c}}}
133	\def\ervd{{\textnormal{d}}}
134	\def\erve{{\textnormal{e}}}
135	\def\ervf{{\textnormal{f}}}
136	\def\ervg{{\textnormal{g}}}
137	\def\ervh{{\textnormal{h}}}
138	\def\ervi{{\textnormal{i}}}
139	\def\ervj{{\textnormal{j}}}
140	\def\ervk{{\textnormal{k}}}
141	\def\ervl{{\textnormal{l}}}
142	\def\ervm{{\textnormal{m}}}
143	\def\ervn{{\textnormal{n}}}
144	\def\ervo{{\textnormal{o}}}
145	\def\ervp{{\textnormal{p}}}
146	\def\ervq{{\textnormal{q}}}
147	\def\ervr{{\textnormal{r}}}
148	\def\ervs{{\textnormal{s}}}
149	\def\ervt{{\textnormal{t}}}
150	\def\ervu{{\textnormal{u}}}
151	\def\ervv{{\textnormal{v}}}
152	\def\ervw{{\textnormal{w}}}
153	\def\ervx{{\textnormal{x}}}
154	\def\ervy{{\textnormal{y}}}
155	\def\ervz{{\textnormal{z}}}
156	
157	% Random matrices
158	\def\rmA{{\mathbf{A}}}
159	\def\rmB{{\mathbf{B}}}
160	\def\rmC{{\mathbf{C}}}
161	\def\rmD{{\mathbf{D}}}
162	\def\rmE{{\mathbf{E}}}
163	\def\rmF{{\mathbf{F}}}
164	\def\rmG{{\mathbf{G}}}
165	\def\rmH{{\mathbf{H}}}
166	\def\rmI{{\mathbf{I}}}
167	\def\rmJ{{\mathbf{J}}}
168	\def\rmK{{\mathbf{K}}}
169	\def\rmL{{\mathbf{L}}}
170	\def\rmM{{\mathbf{M}}}
171	\def\rmN{{\mathbf{N}}}
172	\def\rmO{{\mathbf{O}}}
173	\def\rmP{{\mathbf{P}}}
174	\def\rmQ{{\mathbf{Q}}}
175	\def\rmR{{\mathbf{R}}}
176	\def\rmS{{\mathbf{S}}}
177	\def\rmT{{\mathbf{T}}}
178	\def\rmU{{\mathbf{U}}}
179	\def\rmV{{\mathbf{V}}}
180	\def\rmW{{\mathbf{W}}}
181	\def\rmX{{\mathbf{X}}}
182	\def\rmY{{\mathbf{Y}}}
183	\def\rmZ{{\mathbf{Z}}}
184	
185	% Elements of random matrices
186	\def\ermA{{\textnormal{A}}}
187	\def\ermB{{\textnormal{B}}}
188	\def\ermC{{\textnormal{C}}}
189	\def\ermD{{\textnormal{D}}}
190	\def\ermE{{\textnormal{E}}}
191	\def\ermF{{\textnormal{F}}}
192	\def\ermG{{\textnormal{G}}}
193	\def\ermH{{\textnormal{H}}}
194	\def\ermI{{\textnormal{I}}}
195	\def\ermJ{{\textnormal{J}}}
196	\def\ermK{{\textnormal{K}}}
197	\def\ermL{{\textnormal{L}}}
198	\def\ermM{{\textnormal{M}}}
199	\def\ermN{{\textnormal{N}}}
200	\def\ermO{{\textnormal{O}}}
201	\def\ermP{{\textnormal{P}}}
202	\def\ermQ{{\textnormal{Q}}}
203	\def\ermR{{\textnormal{R}}}
204	\def\ermS{{\textnormal{S}}}
205	\def\ermT{{\textnormal{T}}}
206	\def\ermU{{\textnormal{U}}}
207	\def\ermV{{\textnormal{V}}}
208	\def\ermW{{\textnormal{W}}}
209	\def\ermX{{\textnormal{X}}}
210	\def\ermY{{\textnormal{Y}}}
211	\def\ermZ{{\textnormal{Z}}}
212	
213	% Vectors
214	\def\vzero{{\bm{0}}}
215	\def\vone{{\bm{1}}}
216	\def\vmu{{\bm{\mu}}}
217	\def\vtheta{{\bm{\theta}}}
218	\def\va{{\bm{a}}}
219	\def\vb{{\bm{b}}}
220	\def\vc{{\bm{c}}}
221	\def\vd{{\bm{d}}}
222	\def\ve{{\bm{e}}}
223	\def\vf{{\bm{f}}}
224	\def\vg{{\bm{g}}}
225	\def\vh{{\bm{h}}}
226	\def\vi{{\bm{i}}}
227	\def\vj{{\bm{j}}}
228	\def\vk{{\bm{k}}}
229	\def\vl{{\bm{l}}}
230	\def\vm{{\bm{m}}}
231	\def\vn{{\bm{n}}}
232	\def\vo{{\bm{o}}}
233	\def\vp{{\bm{p}}}
234	\def\vq{{\bm{q}}}
235	\def\vr{{\bm{r}}}
236	\def\vs{{\bm{s}}}
237	\def\vt{{\bm{t}}}
238	\def\vu{{\bm{u}}}
239	\def\vv{{\bm{v}}}
240	\def\vw{{\bm{w}}}
241	\def\vx{{\bm{x}}}
242	\def\vy{{\bm{y}}}
243	\def\vz{{\bm{z}}}
244	
245	% Elements of vectors
246	\def\evalpha{{\alpha}}
247	\def\evbeta{{\beta}}
248	\def\evepsilon{{\epsilon}}
249	\def\evlambda{{\lambda}}
250	\def\evomega{{\omega}}
251	\def\evmu{{\mu}}
252	\def\evpsi{{\psi}}
253	\def\evsigma{{\sigma}}
254	\def\evtheta{{\theta}}
255	\def\eva{{a}}
256	\def\evb{{b}}
257	\def\evc{{c}}
258	\def\evd{{d}}
259	\def\eve{{e}}
260	\def\evf{{f}}
261	\def\evg{{g}}
262	\def\evh{{h}}
263	\def\evi{{i}}
264	\def\evj{{j}}
265	\def\evk{{k}}
266	\def\evl{{l}}
267	\def\evm{{m}}
268	\def\evn{{n}}
269	\def\evo{{o}}
270	\def\evp{{p}}
271	\def\evq{{q}}
272	\def\evr{{r}}
273	\def\evs{{s}}
274	\def\evt{{t}}
275	\def\evu{{u}}
276	\def\evv{{v}}
277	\def\evw{{w}}
278	\def\evx{{x}}
279	\def\evy{{y}}
280	\def\evz{{z}}
281	
282	% Matrix
283	\def\mA{{\bm{A}}}
284	\def\mB{{\bm{B}}}
285	\def\mC{{\bm{C}}}
286	\def\mD{{\bm{D}}}
287	\def\mE{{\bm{E}}}
288	\def\mF{{\bm{F}}}
289	\def\mG{{\bm{G}}}
290	\def\mH{{\bm{H}}}
291	\def\mI{{\bm{I}}}
292	\def\mJ{{\bm{J}}}
293	\def\mK{{\bm{K}}}
294	\def\mL{{\bm{L}}}
295	\def\mM{{\bm{M}}}
296	\def\mN{{\bm{N}}}
297	\def\mO{{\bm{O}}}
298	\def\mP{{\bm{P}}}
299	\def\mQ{{\bm{Q}}}
300	\def\mR{{\bm{R}}}
301	\def\mS{{\bm{S}}}
302	\def\mT{{\bm{T}}}
303	\def\mU{{\bm{U}}}
304	\def\mV{{\bm{V}}}
305	\def\mW{{\bm{W}}}
306	\def\mX{{\bm{X}}}
307	\def\mY{{\bm{Y}}}
308	\def\mZ{{\bm{Z}}}
309	\def\mBeta{{\bm{\beta}}}
310	\def\mPhi{{\bm{\Phi}}}
311	\def\mLambda{{\bm{\Lambda}}}
312	\def\mSigma{{\bm{\Sigma}}}
313	
314	% Tensor
315	\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
316	\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
317	\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
318	\def\tA{{\tens{A}}}
319	\def\tB{{\tens{B}}}
320	\def\tC{{\tens{C}}}
321	\def\tD{{\tens{D}}}
322	\def\tE{{\tens{E}}}
323	\def\tF{{\tens{F}}}
324	\def\tG{{\tens{G}}}
325	\def\tH{{\tens{H}}}
326	\def\tI{{\tens{I}}}
327	\def\tJ{{\tens{J}}}
328	\def\tK{{\tens{K}}}
329	\def\tL{{\tens{L}}}
330	\def\tM{{\tens{M}}}
331	\def\tN{{\tens{N}}}
332	\def\tO{{\tens{O}}}
333	\def\tP{{\tens{P}}}
334	\def\tQ{{\tens{Q}}}
335	\def\tR{{\tens{R}}}
336	\def\tS{{\tens{S}}}
337	\def\tT{{\tens{T}}}
338	\def\tU{{\tens{U}}}
339	\def\tV{{\tens{V}}}
340	\def\tW{{\tens{W}}}
341	\def\tX{{\tens{X}}}
342	\def\tY{{\tens{Y}}}
343	\def\tZ{{\tens{Z}}}
344	
345	
346	% Graph
347	\def\gA{{\mathcal{A}}}
348	\def\gB{{\mathcal{B}}}
349	\def\gC{{\mathcal{C}}}
350	\def\gD{{\mathcal{D}}}
351	\def\gE{{\mathcal{E}}}
352	\def\gF{{\mathcal{F}}}
353	\def\gG{{\mathcal{G}}}
354	\def\gH{{\mathcal{H}}}
355	\def\gI{{\mathcal{I}}}
356	\def\gJ{{\mathcal{J}}}
357	\def\gK{{\mathcal{K}}}
358	\def\gL{{\mathcal{L}}}
359	\def\gM{{\mathcal{M}}}
360	\def\gN{{\mathcal{N}}}
361	\def\gO{{\mathcal{O}}}
362	\def\gP{{\mathcal{P}}}
363	\def\gQ{{\mathcal{Q}}}
364	\def\gR{{\mathcal{R}}}
365	\def\gS{{\mathcal{S}}}
366	\def\gT{{\mathcal{T}}}
367	\def\gU{{\mathcal{U}}}
368	\def\gV{{\mathcal{V}}}
369	\def\gW{{\mathcal{W}}}
370	\def\gX{{\mathcal{X}}}
371	\def\gY{{\mathcal{Y}}}
372	\def\gZ{{\mathcal{Z}}}
373	
374	% Sets
375	\def\sA{{\mathbb{A}}}
376	\def\sB{{\mathbb{B}}}
377	\def\sC{{\mathbb{C}}}
378	\def\sD{{\mathbb{D}}}
379	% Don't use a set called E, because this would be the same as our symbol
380	% for expectation.
381	\def\sF{{\mathbb{F}}}
382	\def\sG{{\mathbb{G}}}
383	\def\sH{{\mathbb{H}}}
384	\def\sI{{\mathbb{I}}}
385	\def\sJ{{\mathbb{J}}}
386	\def\sK{{\mathbb{K}}}
387	\def\sL{{\mathbb{L}}}
388	\def\sM{{\mathbb{M}}}
389	\def\sN{{\mathbb{N}}}
390	\def\sO{{\mathbb{O}}}
391	\def\sP{{\mathbb{P}}}
392	\def\sQ{{\mathbb{Q}}}
393	\def\sR{{\mathbb{R}}}
394	\def\sS{{\mathbb{S}}}
395	\def\sT{{\mathbb{T}}}
396	\def\sU{{\mathbb{U}}}
397	\def\sV{{\mathbb{V}}}
398	\def\sW{{\mathbb{W}}}
399	\def\sX{{\mathbb{X}}}
400	\def\sY{{\mathbb{Y}}}
401	\def\sZ{{\mathbb{Z}}}
402	
403	% Entries of a matrix
404	\def\emLambda{{\Lambda}}
405	\def\emA{{A}}
406	\def\emB{{B}}
407	\def\emC{{C}}
408	\def\emD{{D}}
409	\def\emE{{E}}
410	\def\emF{{F}}
411	\def\emG{{G}}
412	\def\emH{{H}}
413	\def\emI{{I}}
414	\def\emJ{{J}}
415	\def\emK{{K}}
416	\def\emL{{L}}
417	\def\emM{{M}}
418	\def\emN{{N}}
419	\def\emO{{O}}
420	\def\emP{{P}}
421	\def\emQ{{Q}}
422	\def\emR{{R}}
423	\def\emS{{S}}
424	\def\emT{{T}}
425	\def\emU{{U}}
426	\def\emV{{V}}
427	\def\emW{{W}}
428	\def\emX{{X}}
429	\def\emY{{Y}}
430	\def\emZ{{Z}}
431	\def\emSigma{{\Sigma}}
432	
433	% entries of a tensor
434	% Same font as tensor, without \bm wrapper
435	\newcommand{\etens}[1]{\mathsfit{#1}}
436	\def\etLambda{{\etens{\Lambda}}}
437	\def\etA{{\etens{A}}}
438	\def\etB{{\etens{B}}}
439	\def\etC{{\etens{C}}}
440	\def\etD{{\etens{D}}}
441	\def\etE{{\etens{E}}}
442	\def\etF{{\etens{F}}}
443	\def\etG{{\etens{G}}}
444	\def\etH{{\etens{H}}}
445	\def\etI{{\etens{I}}}
446	\def\etJ{{\etens{J}}}
447	\def\etK{{\etens{K}}}
448	\def\etL{{\etens{L}}}
449	\def\etM{{\etens{M}}}
450	\def\etN{{\etens{N}}}
451	\def\etO{{\etens{O}}}
452	\def\etP{{\etens{P}}}
453	\def\etQ{{\etens{Q}}}
454	\def\etR{{\etens{R}}}
455	\def\etS{{\etens{S}}}
456	\def\etT{{\etens{T}}}
457	\def\etU{{\etens{U}}}
458	\def\etV{{\etens{V}}}
459	\def\etW{{\etens{W}}}
460	\def\etX{{\etens{X}}}
461	\def\etY{{\etens{Y}}}
462	\def\etZ{{\etens{Z}}}
463	
464	% The true underlying data generating distribution
465	\newcommand{\pdata}{p_{\rm{data}}}
466	% The empirical distribution defined by the training set
467	\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
468	\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
469	% The model distribution
470	\newcommand{\pmodel}{p_{\rm{model}}}
471	\newcommand{\Pmodel}{P_{\rm{model}}}
472	\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
473	% Stochastic autoencoder distributions
474	\newcommand{\pencode}{p_{\rm{encoder}}}
475	\newcommand{\pdecode}{p_{\rm{decoder}}}
476	\newcommand{\precons}{p_{\rm{reconstruct}}}
477	
478	\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution
479	
480	\newcommand{\E}{\mathbb{E}}
481	\newcommand{\Ls}{\mathcal{L}}
482	\newcommand{\R}{\mathbb{R}}
483	\newcommand{\emp}{\tilde{p}}
484	\newcommand{\lr}{\alpha}
485	\newcommand{\reg}{\lambda}
486	\newcommand{\rect}{\mathrm{rectifier}}
487	\newcommand{\softmax}{\mathrm{softmax}}
488	\newcommand{\sigmoid}{\sigma}
489	\newcommand{\softplus}{\zeta}
490	\newcommand{\KL}{D_{\mathrm{KL}}}
491	\newcommand{\Var}{\mathrm{Var}}
492	\newcommand{\standarderror}{\mathrm{SE}}
493	\newcommand{\Cov}{\mathrm{Cov}}
494	% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
495	% But then they seem to use $L^2$ for vectors throughout the site, and so does
496	% wikipedia.
497	\newcommand{\normlzero}{L^0}
498	\newcommand{\normlone}{L^1}
499	\newcommand{\normltwo}{L^2}
500	\newcommand{\normlp}{L^p}
501	\newcommand{\normmax}{L^\infty}
502	
503	\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.
504	
505	\DeclareMathOperator*{\argmax}{arg\,max}
506	\DeclareMathOperator*{\argmin}{arg\,min}
507	
508	\DeclareMathOperator{\sign}{sign}
509	\DeclareMathOperator{\Tr}{Tr}
510	\let\ab\allowbreak
511	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22c4a08f-324d-42fd-9c5a-08b59c9d2b62",
  "isSidechain": true,
  "promptId": "312b929a-ff15-4578-9f20-fa426006cee1",
  "agentId": "ab5e8c9ac0a3c94bd",
  "type": "user",
  "uuid": "ba6b8726-ce75-4c71-ae6e-67e164c08dbe",
  "sourceToolAssistantUUID": "22c4a08f-324d-42fd-9c5a-08b59c9d2b62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T15:09:43.332Z_

I have now read the complete paper. Let me compile the review.

```
## R2 Review: Novelty and Related Work

### Summary
This paper applies the classical Mantel-Haenszel DIF procedure from educational psychometrics to LLM benchmarks at large scale (5,227 models, 27,125 items across 6 benchmarks), finding that 17.9--31.3% of items exhibit large temporal instability between 2023 and 2024 model cohorts. The authors argue this instability is diagnostic rather than destructive (ranking correlation ~0.997), expose a validation methodology gap in existing contamination detection work, and propose a semi-synthetic injection framework with cross-subject matching. The paper is well-executed empirically and thorough in its controls, but the core methodological novelty is limited: MH-DIF is applied without modification, and the conceptual insights, while useful, are incremental.

### Strengths

1. **Scale and thoroughness of empirical analysis.** The application of MH-DIF to 5,227 models across 6 benchmarks with 27,125 total items is unprecedented for this type of psychometric analysis in NLP. The six alternative explanations tested and ruled out (ability confounding, model family inflation, IRT theta-conditioning, within-subject effects, ranking impact, local item dependence) demonstrate exceptional rigor. The random-split control yielding only 0.18% C items is a convincing null baseline.

2. **The ground truth meta-critique is a genuine and valuable contribution.** The observation that web-overlap labels measure global exposure rather than differential functioning, supported by the enrichment ratio of 0.964, Jaccard of 0.206, and phi of 0.012, is a substantive critique of the contamination detection validation paradigm. This conceptual distinction (Figure 1) is clearly articulated and could influence how future contamination detectors are evaluated.

3. **Simpson's paradox finding.** The reversal of the odds ratio from 1.55 to 0.73 after controlling for item properties is genuinely surprising and represents the most novel analytical contribution. It demonstrates that item properties, not aggregate accuracy gains, drive DIF classification---a non-obvious finding that adds real insight.

4. **The difficulty-direction interaction is scientifically interesting.** The correlation of rho = -0.597 showing capability gains on hard items but erosion on easy items suggests DIF captures genuine temporal construct shift rather than noise. This finding has implications for understanding how model generations evolve.

5. **Related work is now comprehensive and well-structured.** The revised Related Work (Section 2) covers four clearly delineated paragraphs: Contamination Detection, IRT in LLM Evaluation, DIF Methodology and Measurement Invariance, and Benchmark Quality and Design. The paper cites alternative DIF methods (logistic regression DIF, SIBTEST, Lord's chi-squared, Raju area method, MIMIC models), recent IRT-for-LLM work (PSN-IRT, TinyBenchmarks, Growing Pains), dynamic benchmarks, and memorization literature. The positioning relative to Growing Pains (complementary: they assume anchor stability, this paper diagnoses which anchors violate that assumption) is crisp and accurate.

6. **Cross-benchmark replication adds credibility.** The task-type dichotomy (knowledge/reasoning C% >= 26.9% vs. procedural C% <= 18.9%) is interpretable and adds a structural insight beyond raw numbers. The 6-month window robustness check (C% = 34.35% for MMLU) further strengthens the finding.

### Weaknesses

1. **The core method is entirely borrowed.** MH-DIF (1959/1988), ETS classification (Zieky 1993), and the stratification procedure are standard psychometric tools applied without any modification. The paper explicitly states "We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals." For EMNLP 2026, this creates a significant novelty concern. While "old method, new domain" papers have been accepted at top venues, the methodological adaptation must typically be non-trivial or the empirical findings transformative. The empirical findings here are interesting but not transformative---the instability does not change rankings, and the paper itself argues the instability is "diagnostic, not destructive."

2. **Proposition 1 (ΔFPR = 0) is trivially true and should not be called a "proposition."** If the matching variable excludes the tested subject, then by construction injecting contamination into that subject cannot affect the matching variable. This is a simple observation about disjoint sets, not a result requiring proof. Presenting it as a formal proposition inflates the perceived methodological contribution. The cross-subject matching idea itself has psychometric precedent (Nandakumar 1993, Donoghue & Allen 1993), as the paper acknowledges. The LLM-specific adaptation (multi-domain, simultaneous contamination) is reasonable but not deep.

3. **The "instability does not equal invalidity" message is self-limiting.** The paper's main empirical finding (31% items are unstable) is immediately followed by the reassurance that rankings are unaffected (rho ~= 0.997). While intellectually honest, this undercuts the practical significance of the finding. If one-third of items can be removed without affecting rankings, the natural question is: "so what?" The paper answers this with the "diagnostic lens" framing, but the practical implications remain vague. The recommended audit protocol (Section 5.4) is generic and under-developed.

4. **No direct empirical comparison with existing contamination detectors.** The paper argues conceptually that ConStat, DVD, etc. are orthogonal to DIF because they validate against web-overlap labels. But this conceptual argument does not substitute for running these methods on the same data and showing the overlap statistics directly. The paper has the METABENCH matrix---it should be feasible to run ConStat and report the item-level agreement. The current approach amounts to arguing by proxy (if method X validates against labels Y, and DIF is independent of Y, then DIF is independent of X). This is logically sound but not as convincing as direct evidence.

5. **Temporal cohort definition is coarse and potentially conflated.** The 2023 vs. 2024 split aggregates models with vastly different architectures, training data, alignment procedures, and scales. The paper acknowledges this in Limitations but does not adequately address what the temporal DIF signal actually means. Is it contamination? Capability change? Data mixture shifts? RLHF effects? The paper says DIF detects "that" not "why," but this agnosticism is a weakness when the claimed contribution is diagnostic utility. A diagnostic tool that cannot distinguish contamination from capability change has limited practical value for the stated use case of benchmark maintenance.

6. **The GSM1K correlation (N=33) is underpowered and over-interpreted.** A sample of 33 models with r = -0.478 and wide confidence intervals [-0.71, -0.16] is exploratory at best. The paper does flag this in Limitations, but the finding is given substantial discussion space in Sections 4.7 and 5.3 relative to its evidential weight.

7. **Missing head-to-head with Growing Pains (Habba et al. 2026).** This concurrent work addresses score comparability through fixed-parameter calibration and is the closest related contribution. The paper positions itself as complementary (DIF diagnoses which anchor items are unstable, Growing Pains assumes anchor stability), but a direct comparison---e.g., do Growing Pains' anchor items pass DIF tests?---would substantially strengthen the positioning. As written, the complementarity claim is conceptual rather than demonstrated.

### Questions for Authors

1. **Can you run ConStat on the METABENCH matrix and report item-level agreement with DIF flags?** The conceptual argument about orthogonality to web-overlap labels is compelling, but direct evidence would be far more convincing.

2. **What is the temporal DIF rate when controlling for training data cutoff date rather than model release date?** Release date and training data cutoff are different; models released in 2024 may have been trained on data available in 2023. Does finer temporal definition change C%?

3. **For the difficulty-direction interaction (rho = -0.597), is this driven by ceiling/floor effects?** Easy items may show erosion simply because high-performing 2024 models are already near ceiling, making any noise-induced incorrect response look like DIF. Hard items may show gains for symmetric reasons. Have you controlled for this?

4. **Can you demonstrate that the DIF audit protocol (Section 5.4) would have identified a known problem item in retrospect?** The protocol is currently prescriptive without validation. A case study showing that DIF-flagged items have identifiable quality issues (ambiguous wording, outdated facts, etc.) would be very persuasive.

5. **How sensitive is the 31% figure to the choice of K=5 strata?** The paper reports K=5 following ETS practice, but LLM ability distributions may differ fundamentally from human test-taker distributions. Results at K=10, K=20 would strengthen robustness.

6. **Could the within-family Llama-2 vs. Llama-3 comparison (C% = 61.3% unmatched) partly reflect training data overlap rather than ability confounding?** Llama-3 was trained on significantly more data including newer web crawls. The matched C% of 28.3% is still high---is this residual DIF or residual confounding?

### Minor Issues

1. The abstract is dense to the point of being impenetrable on first reading. It tries to compress all four claims, multiple statistics, and the Simpson's paradox into a single paragraph. Consider restructuring to lead with the main finding and implications.

2. Proposition 1 is stated informally (no proper mathematical statement of assumptions and conclusion). If retained, it should either be formalized properly or downgraded to a remark/observation.

3. The paper uses "FPR" inconsistently: sometimes it refers to false positive rate of DIF detection in the semi-synthetic setting, sometimes to the rate of DIF-C classification among web-overlap "clean" items in the observational setting. These are different quantities and should be distinguished more clearly.

4. Table 1 reports "FPR (clean)" as 0.318 for the temporal cohort, but this is not really a false positive rate---it is the DIF-C rate among items classified as "clean" by web-overlap labels. Calling it FPR presupposes that web-overlap labels define ground truth, which contradicts the paper's own argument.

5. The 92.4% "item-specific instability" figure from logistic regression (pseudo R-squared = 0.0007) is an unusual way to decompose variance. Pseudo R-squared values near zero for domain-level predictors do not necessarily imply item-level specificity---they may simply indicate that the model is poorly specified.

6. Several references appear to be from 2026 (Liang 2026 DVD, Tao 2026 Self-Critique, Wang 2026 Fragility, Habba 2026 Growing Pains, etc.). This seems plausible for an ARR 2026 submission but reviewers should verify these are not hallucinated citations. The arxiv IDs should be checked.

### Missing References

The Related Work section has been significantly strengthened and now covers most relevant areas. However, a few notable gaps remain:

- **Oren et al. (2024), "Proving Test Set Contamination in Black Box Language Models"**: A directly relevant contamination detection method using exchangeability tests, operating at the dataset level rather than item level. Should be cited alongside Min-K% and ConStat.

- **Deng et al. (2024), "Investigating Data Contamination in Modern Benchmarks for Large Language Models"**: Provides another perspective on benchmark contamination at scale.

- **Srivastava et al. (2023), BIG-bench**: As a major multi-task benchmark, it would be natural to discuss whether DIF analysis applies to other large-scale benchmarks beyond METABENCH.

- **Polo et al. (2024), METABENCH paper** or the original Open LLM Leaderboard papers should be cited for the provenance of the model response data.

- **Embretson & Reise (2000) or de Ayala (2009)**: Standard IRT textbook references. The paper cites Lord (1980) but more modern treatments would strengthen the psychometric grounding.

- **Penfield & Camilli (2007), "Differential Item Functioning" in the Handbook of Statistics**: A comprehensive DIF review that could supplement the current methodological citations.

These are not critical omissions---the paper's Related Work is already among the stronger sections---but addressing them would further demonstrate command of the cross-disciplinary literature.

### Scores
- Soundness: 4/5
- Excitement: 3/5
- Reproducibility: 4/5
- Overall Assessment: 3.5 (Borderline Conference)
- Confidence: 4/5
```

**Rationale for scores:**

**Soundness (4/5):** The empirical methodology is rigorous with extensive controls. The six alternative explanations systematically tested, the random-split null baseline, and the cross-benchmark replication are all well-executed. Deductions for the overstated Proposition 1, the inconsistent use of "FPR," and the underpowered GSM1K analysis.

**Excitement (3/5):** The paper provides a useful empirical characterization of LLM benchmark measurement properties and a genuinely valuable conceptual contribution (global vs. differential exposure). However, the core novelty is limited---an unmodified classical method applied to a new domain, yielding a finding (31% instability) that the paper itself argues does not threaten validity. The Simpson's paradox and difficulty-direction interaction are the most exciting elements but are secondary to the main narrative.

**Reproducibility (4/5):** METABENCH data is public, the method is standard (MH-DIF with ETS classification), and the paper commits to releasing code. The cohort definitions and experimental parameters are clearly specified. Minor deduction because some results depend on the Li et al. contamination labels whose coverage is 73.8%.

**Overall Assessment (3.5 - Borderline Conference):** The paper sits at the boundary between a solid Findings paper and a borderline Main conference accept. The scale of the empirical analysis, the ground truth meta-critique, and the Simpson's paradox are genuine contributions. Against these, the lack of methodological novelty (unmodified MH-DIF), the self-limiting "instability is not invalidity" message, and the absence of direct comparison with existing detectors are significant limitations. The paper would be strengthened substantially by (a) a head-to-head with ConStat/DVD on the same data, (b) a deeper investigation of what the temporal DIF signal actually captures, and (c) a validated case study of the audit protocol. In its current form, the paper is a well-executed empirical study with useful but incremental insights, better suited for Findings than Main at EMNLP 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6b8726-ce75-4c71-ae6e-67e164c08dbe",
  "isSidechain": true,
  "agentId": "ab5e8c9ac0a3c94bd",
  "requestId": "req_011CbFvYUhxU9c9vqFdvbt7v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed821907-2a31-467f-a6fc-b10f5f44de0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ce551a50-54ba-4aaa-8fff-25f5094463ff",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNgdE5KtncTXtQabsNdLxa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8149,
      "cache_read_input_tokens": 44682,
      "output_tokens": 3572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3572,
          "cache_read_input_tokens": 44682,
          "cache_creation_input_tokens": 8149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8149,
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
