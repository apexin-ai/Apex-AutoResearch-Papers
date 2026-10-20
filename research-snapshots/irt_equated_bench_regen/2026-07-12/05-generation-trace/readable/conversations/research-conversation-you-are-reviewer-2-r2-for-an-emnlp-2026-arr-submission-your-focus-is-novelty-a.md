# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. Evaluate originali

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac01af25fe1457019.jsonl`
- **Structured JSON:** [`5c730bfe56f3bb48093e.json`](../../sessions/5c/5c730bfe56f3bb48093e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-21T17:35:31.869Z_

You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **Novelty and Related Work**. Evaluate originality, positioning against prior art, significance of contributions, and whether the framing accurately represents the advance.

## Scoring Scale (ARR Overall Assessment, 0.5 increments)
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

Acceptance rate: ~21% for Main. Calibrate strictly.

## Paper Summary

**Title:** Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis

**Core claim:** 31% of MMLU items are functionally unstable across temporal model cohorts (2023 vs 2024-H1), detected via Mantel-Haenszel DIF on METABENCH (5,227 models × 12,508 items). Generalizes across 6 benchmarks (17.9–31.3%).

**4 Contributions claimed:**
1. Large-scale temporal instability finding (31%, 6 benchmarks, domain improvement ≤7.6%)
2. Ground truth meta-critique: web-overlap labels measure global exposure not differential functioning; enrichment ≈1.0 against DIF flags is theoretically expected, not a failure
3. Semi-synthetic validation framework: ΔTPR methodology with cross-subject matching (ΔFPR=0.000), portable across benchmarks (GSM8K ΔTPR=+0.818)
4. DIF as diagnostic lens: DIF items carry genuine cross-cohort signal (z=-8 to -49σ vs random removal) but are the least disruptive non-random removal strategy (z=-9.5 vs accuracy-gap z=-157)

**Related Work (Section 2):** 4 subsections:
- Benchmark contamination detection: Shi et al. 2024 (Min-K%), Oren et al. 2024 (perturbation), Li et al. 2024 (n-gram overlap). Paper claims DIF differs by operating at item level across populations rather than model level.
- Benchmark reliability/validity: Mizrahi et al. 2024 (prompt perturbation), Polo et al. 2024 (evaluation framework), "benchmark lottery". Paper claims psychometric approach complements these.
- DIF in educational testing: Holland and Wainer 1993, Mantel and Haenszel 1959, Holland and Thayer 1988. Paper claims contribution is empirical findings not new algorithm.
- Psychometrics for LLM evaluation: Polo et al. 2024 (IRT for efficient testing). Paper claims extension to temporal comparability.

**Key methodological elements:**
- MH-DIF: standard procedure from educational testing, no modification claimed
- Semi-synthetic framework: inject known contamination (incorrect→correct flipping) at varying rates, measure ΔTPR
- Cross-subject matching: condition on scores from other subjects to avoid matching variable contamination
- Enrichment analysis against Li et al. web-overlap labels

**Results highlights:**
- 31.3% C-classified items on MMLU, 17.9-31.3% across 6 benchmarks
- Permutation null: observed 31.3% vs null mean 0.21% (>600σ)
- Semi-synthetic ΔTPR up to +0.674, cross-subject matching eliminates FPR inflation
- Web-overlap enrichment ≈1.0 (orthogonal)
- Rankings stable despite 31% instability (ρ≈0.997)
- GSM1K negative correlation (r=-0.478): DIF ≠ contamination on GSM8K

**Appendices A-H cover:** RL robustness, ConStat evaluation, DVD evaluation, Ensemble fusion, Bifactor IRT, Item generation calibration, Cumulative Bayesian DIF, Item-Focused Trees

**References:** Only 7 references in main text (Holland & Thayer 1988, Holland & Wainer 1993, Li et al. 2024, Mantel & Haenszel 1959, Mizrahi et al. 2024, Oren et al. 2024, Polo et al. 2024, Shi et al. 2024).

## Your Review Task

Provide a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (numbered, specific)
3. **Weaknesses** (numbered, specific, with severity: major/minor)
4. **Questions to Authors** (numbered)
5. **Soundness** (1-5)
6. **Excitement** (1-5)
7. **Reproducibility** (1-5)
8. **Overall Assessment** (use the 0.5-increment scale)
9. **Confidence** (1-5)

Focus specifically on:
- Is applying an existing psychometric method (MH-DIF) to LLM benchmarks sufficiently novel for a top venue?
- Is the related work comprehensive? Missing citations? (Consider: Benchmark contamination work by Golchin & Surdeanu 2024, Deng et al. 2024 on benchmark leakage, Yang et al. 2023 on MMLU contamination, Jacovi et al. 2023 on benchmark lifecycle, Raji et al. 2021 on benchmark misuse. Also IRT-for-LLM work: Lalor et al. 2019, Vania et al. 2021, Rodriguez et al. 2021.)
- Does the "ground truth meta-critique" contribution hold up? Is the argument that enrichment ≈1.0 is "expected" well-supported?
- Is the "diagnostic lens" framing a genuine insight or post-hoc rationalization of a null result?
- How does this compare to concurrent/recent work on benchmark dynamics?
- Are 4 contributions too many or appropriately scoped?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "05a0d164-cfbc-4047-a6d0-7708452fc734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T17:35:31.874Z_

```json
{
  "parentUuid": "05a0d164-cfbc-4047-a6d0-7708452fc734",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
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
  "uuid": "70ffdd94-1a49-4568-baa6-99ec12fa0d64",
  "timestamp": "2026-05-21T17:35:31.874Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T17:35:35.421Z_



I'll start by reading the paper and related materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ffdd94-1a49-4568-baa6-99ec12fa0d64",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7np8RoK8Yyxmb82E4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5957a4d-a9d6-464e-8a75-d173e4231b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTz9rTWTQkWQyRFmwzuLtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 8732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7864,
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

_source line 4 · 2026-05-21T17:35:36.772Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XcQmZH6Edbpxu4FhVPyZJi`</summary>

```json
{
  "pattern": "paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5957a4d-a9d6-464e-8a75-d173e4231b3a",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7np8RoK8Yyxmb82E4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "795d407e-3b35-4f74-a930-1fe524e2bfb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTz9rTWTQkWQyRFmwzuLtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 8732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7864,
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

_source line 5 · 2026-05-21T17:35:36.796Z_

<details><summary>↩ Tool result · `toolu_01XcQmZH6Edbpxu4FhVPyZJi`</summary>

```text
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795d407e-3b35-4f74-a930-1fe524e2bfb2",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "40b8b104-941f-4b00-ab16-fe9daa28db1f",
  "sourceToolAssistantUUID": "795d407e-3b35-4f74-a930-1fe524e2bfb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T17:35:37.729Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RJNSH3pZcMQZwDQzTYvQwY`</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40b8b104-941f-4b00-ab16-fe9daa28db1f",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7np8RoK8Yyxmb82E4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfaa4eb0-a19c-4cdb-b0af-0174e83e0da7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTz9rTWTQkWQyRFmwzuLtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 8732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7864,
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

_source line 7 · 2026-05-21T17:35:37.751Z_

<details><summary>↩ Tool result · `toolu_01RJNSH3pZcMQZwDQzTYvQwY`</summary>

```text
paper/math_commands.tex
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfaa4eb0-a19c-4cdb-b0af-0174e83e0da7",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "1bd20084-ed24-4a79-8778-ec288bcdc88e",
  "sourceToolAssistantUUID": "dfaa4eb0-a19c-4cdb-b0af-0174e83e0da7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T17:35:38.098Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Sqaq5VUZoDyfyc39wXsR8D`</summary>

```json
{
  "pattern": "paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bd20084-ed24-4a79-8778-ec288bcdc88e",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7np8RoK8Yyxmb82E4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6197a6e-9904-433e-be2b-6e20b5c2189a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTz9rTWTQkWQyRFmwzuLtf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 8732,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 8732,
          "cache_creation_input_tokens": 7864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7864,
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

_source line 9 · 2026-05-21T17:35:38.118Z_

<details><summary>↩ Tool result · `toolu_01Sqaq5VUZoDyfyc39wXsR8D`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6197a6e-9904-433e-be2b-6e20b5c2189a",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "8ce347e5-3e41-4671-b47f-0c213ff39c99",
  "sourceToolAssistantUUID": "f6197a6e-9904-433e-be2b-6e20b5c2189a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T17:35:40.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WwvDzq4xhVjpKjmQE1z9RR`</summary>

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
  "parentUuid": "8ce347e5-3e41-4671-b47f-0c213ff39c99",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7oGuzZjfZLYk1TkRP3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ffcfda0-9762-4f37-9112-200c90360633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEJ8oy79VutELTKr7wBPgU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 16596,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 16596,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1243,
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

_source line 11 · 2026-05-21T17:35:40.566Z_

<details><summary>↩ Tool result · `toolu_01WwvDzq4xhVjpKjmQE1z9RR`</summary>

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
21	\title{Temporal Measurement Drift in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
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
  "parentUuid": "0ffcfda0-9762-4f37-9112-200c90360633",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "9bd718dd-1e95-43e0-bb08-03e4e67fb604",
  "sourceToolAssistantUUID": "0ffcfda0-9762-4f37-9112-200c90360633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T17:35:43.477Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W1SCSN1wr5RGM7o8z9CEa2`</summary>

```json
{
  "pattern": "paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd718dd-1e95-43e0-bb08-03e4e67fb604",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7oTjs7XF5kHKBdPvk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14af2dcb-90c0-4c85-bbed-ed2c7c8bc9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrBx6buAnAjVrngD9cJjZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 487,
      "cache_read_input_tokens": 17839,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 487
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 17839,
          "cache_creation_input_tokens": 487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 487,
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

_source line 13 · 2026-05-21T17:35:43.498Z_

<details><summary>↩ Tool result · `toolu_01W1SCSN1wr5RGM7o8z9CEa2`</summary>

```text
paper/sections/related_work.tex
paper/sections/limitations.tex
paper/sections/abstract.tex
paper/sections/introduction.tex
paper/sections/method.tex
paper/sections/appendix.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14af2dcb-90c0-4c85-bbed-ed2c7c8bc9f9",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "590bf37c-640c-4552-9b65-23ae1969bf2d",
  "sourceToolAssistantUUID": "14af2dcb-90c0-4c85-bbed-ed2c7c8bc9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T17:35:46.367Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P2vYojVW1Gwi7pPduGtv2n`</summary>

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
  "parentUuid": "590bf37c-640c-4552-9b65-23ae1969bf2d",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ofy55msd5pZrptX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8366e557-71a6-4276-8d0c-1444ac68a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4uRqFG1N4P9bwJaDUEg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 18326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 15 · 2026-05-21T17:35:46.377Z_

<details><summary>↩ Tool result · `toolu_01P2vYojVW1Gwi7pPduGtv2n`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8366e557-71a6-4276-8d0c-1444ac68a894",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "c1920131-9bdd-4354-b7e4-d43660a68a0a",
  "sourceToolAssistantUUID": "8366e557-71a6-4276-8d0c-1444ac68a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T17:35:46.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TRD7MRTw6JoFmkxUz8p8p9`</summary>

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
  "parentUuid": "c1920131-9bdd-4354-b7e4-d43660a68a0a",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ofy55msd5pZrptX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53bcdfd0-7fc0-4dbb-9557-493eb2072861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4uRqFG1N4P9bwJaDUEg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 18326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 17 · 2026-05-21T17:35:46.838Z_

<details><summary>↩ Tool result · `toolu_01TRD7MRTw6JoFmkxUz8p8p9`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement drift does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The drift is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
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
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that MH-DIF is sensitive to differential item behavior when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the approximately 31\% temporal DIF rate cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}). MH-DIF detects \emph{that} items function differently across cohorts, not \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter: DIF-flagged items concentrate discriminative signal ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and model families show distinctive DIF profiles (Llama-3 gains ${+}53$ median rank positions, Mistral loses $35$).
18	
19	Our contributions are methodological and empirical, not algorithmic:
20	
21	\begin{enumerate}
22	\item \textbf{Semi-synthetic validation framework}: Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
23	
24	\item \textbf{Ground truth meta-critique}: Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Temporal measurement drift at scale}: Approximately 31\% of MMLU items exhibit differential functioning across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$ (45--174$\times$ above random baselines), with knowledge/reasoning benchmarks showing higher DIF rates than procedural ones. DIF-flagged items concentrate discriminative signal ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal) and exhibit a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones (\Cref{sec:temporal,sec:gsm8k,sec:downstream}).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53bcdfd0-7fc0-4dbb-9557-493eb2072861",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "f157a68e-c0e9-415b-9549-87ae78903780",
  "sourceToolAssistantUUID": "53bcdfd0-7fc0-4dbb-9557-493eb2072861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T17:35:47.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P9EmNAp2BAWTnCGDx8Znge`</summary>

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
  "parentUuid": "f157a68e-c0e9-415b-9549-87ae78903780",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ofy55msd5pZrptX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e775e2f-108d-4775-8fd9-d69a4366a74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4uRqFG1N4P9bwJaDUEg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 18326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 19 · 2026-05-21T17:35:47.364Z_

<details><summary>↩ Tool result · `toolu_01P9EmNAp2BAWTnCGDx8Znge`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrated that not all evaluation examples are equally informative. Recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale, TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection, scalability coefficients for detecting bad benchmark items \citep{hardy2026scalability}, ATLAS \citep{li2025atlas} for computerized adaptive testing of LLMs, and competency-focused IRT evaluation in medical domains \citep{luo2025medirt}. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items' measurement properties shift across model generations, potentially flagging anchor degradation before it affects calibration accuracy. Empirical comparison awaits public release of anchor item lists.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. Cross-subject matching---computing the stratification variable from domains other than the one being tested---has psychometric precedent in the DIF literature \citep{nandakumar1993dif,donoghue1993mh}; our adaptation addresses LLM-specific challenges of multi-domain local dependence and simultaneous contamination control at scale. We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Quality and Design.}
14	The Benchmark Health Index~\citep{zhu2026bhi} and Benchmark$^2$~\citep{qian2026benchmark2} assess static benchmark quality; our temporal DIF analysis is complementary, diagnosing \emph{when} measurement properties shift rather than evaluating them at a single snapshot. \citet{maeda2025difllm} predict which item features associate with DIF in educational settings; we instead detect DIF empirically across LLM cohorts at scale. Dynamic benchmarks \citep{kiela2021dynabench, li2024latesteval, white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges that our DIF analysis directly addresses.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e775e2f-108d-4775-8fd9-d69a4366a74c",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "877ada66-f83a-4d80-aae3-c1832ed3d48d",
  "sourceToolAssistantUUID": "1e775e2f-108d-4775-8fd9-d69a4366a74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T17:35:47.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_016LMa2u9b5Ac5on2CwdWiLx`</summary>

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
  "parentUuid": "877ada66-f83a-4d80-aae3-c1832ed3d48d",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ofy55msd5pZrptX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a5818bb-6a28-470e-890a-5e8df0306287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4uRqFG1N4P9bwJaDUEg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 18326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 21 · 2026-05-21T17:35:47.876Z_

<details><summary>↩ Tool result · `toolu_016LMa2u9b5Ac5on2CwdWiLx`</summary>

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
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%. For example, if 2024 models consistently outperform 2023 models on a formal-logic item \emph{after controlling for overall ability}, the pooled odds ratio $\alpha_{\mathrm{MH}} = 0.42$ yields $\Delta_{\mathrm{MH}} = -2.35 \ln(0.42) = 2.04$, classified as ETS~C ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.001$).
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks. Total score matching is sufficient: IRT $\theta$ estimates correlate at $r = 0.9986$ with total scores in our data, confirming that computationally simpler CTT-based stratification introduces no bias relative to IRT ability matching.
33	
34	\paragraph{LLM-specific challenges.} Applying MH-DIF to LLMs introduces assumptions absent in educational testing. First, models trained on overlapping corpora violate local independence; permutation simulation (1,000 iterations $\times$ 8 subjects, Q3 $= 4.6$--$34.2\%$) confirms LD-attributable FPR inflation $< 0.001$ pp under cross-subject matching with ETS~C (\Cref{app:method_details}). Second, fine-tuned variants and merges within model families are not independent examinees; graduated de-duplication shows family structure does not inflate C\% (\Cref{sec:structural}). Third, the ability distribution is non-normal (bimodal from base vs.\ instruction-tuned models), motivating quintile-based rather than parametric stratification. Fourth, MMLU's 57 subjects span multiple latent dimensions, while MH assumes unidimensionality; cross-subject matching and within-subject DIF checks address this (\Cref{sec:structural}).
35	
36	\subsection{Cohort Designs}
37	\label{sec:cohorts}
38	
39	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
40	
41	\subsection{Semi-Synthetic Injection Framework}
42	\label{sec:injection}
43	
44	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
45	
46	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
47	
48	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this by computing the matching variable from all subjects \emph{other than} the one being tested.
49	
50	\begin{proposition}[Zero FPR under single-subject cross-subject matching]
51	\label{prop:fpr}
52	Let $M_i^{(-s)} = \sum_{j \notin s} Y_{ij}$ be the matching variable for examinee $i$ on focal subject $s$. Under single-subject injection (contamination confined to subject $s$), the tested item belongs to $s$ and does not contribute to $M_i^{(-s)}$; injecting contamination into $s$ leaves $M_i^{(-s)}$ unchanged. Therefore $\Delta\mathrm{FPR} = 0$ by construction.
53	\end{proposition}
54	
55	When contamination spans multiple subjects simultaneously, $M_i^{(-s)}$ may absorb signal from other contaminated subjects, potentially inflating FPR. Empirically, this guarantee extends to multi-domain contamination affecting $\leq$9\% of subjects ($k \leq 5$), with graceful degradation beyond this boundary (\Cref{sec:semisynthetic}).
56	
57	Empirically, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
58	
59	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, DIF decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a5818bb-6a28-470e-890a-5e8df0306287",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "8e2d5bea-847b-452a-bef9-7fdb42c34034",
  "sourceToolAssistantUUID": "5a5818bb-6a28-470e-890a-5e8df0306287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T17:35:52.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UvSh3vKaDuxEK7V6sHdBie`</summary>

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
  "parentUuid": "8e2d5bea-847b-452a-bef9-7fdb42c34034",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ozv6h7KCQyLnRgZCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f54a71a-f5b3-40ad-84f2-0f2354b10542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2CDvu5pKaouUu5St2UCqf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7263,
      "cache_read_input_tokens": 18516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7263,
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

_source line 23 · 2026-05-21T17:35:52.287Z_

<details><summary>↩ Tool result · `toolu_01UvSh3vKaDuxEK7V6sHdBie`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Measurement Drift}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$; \Cref{tab:temporal_landscape}). DIF rates are domain-invariant (Kruskal-Wallis $p = 0.78$), but DIF \emph{direction} exhibits domain dependence: STEM items favor 2024 models (55.4\%), Humanities favor 2023 (64.4\%). Item-level regression shows 92.4\% of the DIF signal is item-specific (pseudo $R^2 = 0.0007$). A Simpson's paradox confirms item properties---not accuracy gains---drive DIF: domain accuracy positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$). The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$; ETS~C's dual threshold makes results less sensitive to the number of strata $K$ than significance-only approaches ($K = 5$ per ETS practice~\citep{donoghue1993mh}).
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
54	Three structural controls fail to reduce temporal C\% below 31\% (\Cref{tab:structural_comparison}): matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$), and within-subject DIF (C\% $= 38.1\%$). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\%), making 31\% conservative. Graduated de-duplication ($K{=}10$: 22.7\%; $K{=}20$: 29.1\%) confirms family structure does not inflate C\%. Ability-matched analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\%$ and temporal C\% from 31.3\% to $28.9\%$---consistent matched values ($\sim$28--29\%) despite vastly different unmatched rates, suggesting genuine item-level DIF accounts for $\sim$28--29\% of items. Six alternative explanations (ability confounding, family inflation, $\theta$-conditioning, within-subject effects, ranking impact, local dependence) were tested; none reduces C\% below $\sim$28\% (\Cref{app:structural}).
55	
56	\begin{table}[t]
57	\centering
58	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching.}
59	\label{tab:structural_comparison}
60	\small
61	\resizebox{\columnwidth}{!}{%
62	\begin{tabular}{lcccc}
63	\toprule
64	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
65	\midrule
66	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
67	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
68	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
69	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
70	\bottomrule
71	\end{tabular}}
72	\end{table}
73	
74	\subsection{Semi-Synthetic Framework Validation}
75	\label{sec:semisynthetic}
76	
77	Cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects (4/5 with $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$), while within-subject matching inflates FPR by ${+}0.186$ on average. Multi-subject injection ($k \in \{1, 3, 5, 10, 20\}$ subjects, 5 random draws each) confirms robustness: $\Delta\mathrm{FPR} < 0.007$ for $k \leq 5$ ($\leq$9\% of domains); at $k = 10$ (18\%), $\Delta\mathrm{FPR}$ rises to 0.026--0.069, marking the boundary of matching variable integrity (\Cref{app:method_details,app:fig_matching}).
78	
79	\subsection{Downstream Impact}
80	\label{sec:downstream}
81	
82	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate ordering is preserved despite 31\% measurement drift. DIF-flagged items nonetheless concentrate discriminative signal ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), though a circularity ablation confirms DIF-based removal is the \emph{least} disruptive non-random strategy. Model families show distinctive DIF profiles: Llama-3 derivatives gain ${+}53$ median rank positions, Mistral loses $35$ (\Cref{app:fig_downstream}). Removing C-flagged items disproportionately disadvantages 2024 models (cohort gap $= 96.2$ positions, $40\times$ larger than random removal; $p < 0.001$), confirming that DIF items carry concentrated inter-generational signal.
83	
84	\subsection{Cross-Benchmark Validation}
85	\label{sec:gsm8k}
86	
87	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), each 45--174$\times$ above random baselines. Knowledge/reasoning benchmarks (WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$ versus $17.9$--$18.9\%$ for procedural ones, consistent with knowledge-intensive items being more sensitive to training data composition shifts.
88	
89	\begin{table}[t]
90	\centering
91	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts. All six show substantial DIF (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
92	\label{tab:cross_benchmark}
93	\small
94	\begin{tabular}{lrrrl}
95	\toprule
96	Benchmark & Items & C\% & Rand.\ C\% & Ratio \\
97	\midrule
98	MMLU & 12{,}508 & 31.3 & 0.18 & 174$\times$ \\
99	WinoGrande & 1{,}267 & 30.3 & 0.32 & 95$\times$ \\
100	TruthfulQA & 817 & 29.7 & 0.37 & 80$\times$ \\
101	ARC & 1{,}172 & 26.9 & 0.60 & 45$\times$ \\
102	GSM8K & 1{,}319 & 18.9 & 0.30 & 63$\times$ \\
103	HellaSwag & 10{,}042 & 17.9 & 0.28 & 64$\times$ \\
104	\bottomrule
105	\end{tabular}
106	\end{table}
107	
108	On GSM8K specifically, semi-synthetic injection with external matching confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}). An exploratory GSM1K analysis ($N = 33$) shows a negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$, $p = 0.005$; partial $r = -0.385$, $p = 0.027$), suggesting DIF captures capability change distinct from memorization (\Cref{app:fig_gsm1k}).
109	
110	Even within a 6-month window (2023-H2 vs.\ 2024-H1), DIF remains substantial (MMLU C\% $= 34.35\%$, 181$\times$; TruthfulQA C\% $= 31.33\%$, 51$\times$ above random baselines).
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f54a71a-f5b3-40ad-84f2-0f2354b10542",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "40326950-5ba4-4a8d-86f3-98381ac790d6",
  "sourceToolAssistantUUID": "3f54a71a-f5b3-40ad-84f2-0f2354b10542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T17:35:52.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UdfCHXjUm9u7jgXfCEQrZB`</summary>

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
  "parentUuid": "40326950-5ba4-4a8d-86f3-98381ac790d6",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ozv6h7KCQyLnRgZCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10d06873-0cbf-4a14-ab2f-c9996a470d3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2CDvu5pKaouUu5St2UCqf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7263,
      "cache_read_input_tokens": 18516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7263,
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

_source line 25 · 2026-05-21T17:35:52.776Z_

<details><summary>↩ Tool result · `toolu_01UdfCHXjUm9u7jgXfCEQrZB`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C DIF rate extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) admits two interpretations: web-overlap labels may be the wrong ground truth for a differential method, or DIF may fail to detect contamination. The semi-synthetic dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) partially resolves this by confirming that MH-DIF \emph{can} detect differential item behavior when present; the near-independence therefore reflects a category error in the ground truth rather than a detection failure.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones.
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol triggered whenever $\geq 500$ new models accumulate, using cross-subject matching. We propose graduated thresholds: C\% $< 15\%$ $\to$ monitor; $15\text{--}25\%$ $\to$ flag (label drift-prone and volatile items); $> 25\%$ $\to$ act (rotate or retire flagged items). MMLU's C\% $= 31.3\%$ exceeds the action threshold.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10d06873-0cbf-4a14-ab2f-c9996a470d3c",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "ad1c405e-0a74-48c2-ab73-bf2491aef73b",
  "sourceToolAssistantUUID": "10d06873-0cbf-4a14-ab2f-c9996a470d3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T17:35:53.262Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pm1svBax53TM4S3svtopyK`</summary>

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
  "parentUuid": "ad1c405e-0a74-48c2-ab73-bf2491aef73b",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ozv6h7KCQyLnRgZCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c86b4768-ad76-4cac-9ab1-aea20fafb2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2CDvu5pKaouUu5St2UCqf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7263,
      "cache_read_input_tokens": 18516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7263,
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

_source line 27 · 2026-05-21T17:35:53.269Z_

<details><summary>↩ Tool result · `toolu_01Pm1svBax53TM4S3svtopyK`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A semi-synthetic framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves a validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six METABENCH benchmarks (27,125 items, 5,227 models), MH-DIF reveals 17.9--31.3\% temporal measurement drift (ETS~C) driven by item properties; DIF-flagged items concentrate discriminative signal ($z{=}{-}8\sigma$ to ${-}49\sigma$; $\rho{=}{-}0.597$). LLM benchmarks need psychometric monitoring alongside score reporting.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c86b4768-ad76-4cac-9ab1-aea20fafb2ea",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "1d261046-da60-41ca-b2eb-32746c187617",
  "sourceToolAssistantUUID": "c86b4768-ad76-4cac-9ab1-aea20fafb2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T17:35:53.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LheX3thhYCDT8pNvpMk3F5`</summary>

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
  "parentUuid": "1d261046-da60-41ca-b2eb-32746c187617",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7ozv6h7KCQyLnRgZCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd0c80d8-1111-4db0-bc69-f10f216aafe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2CDvu5pKaouUu5St2UCqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7263,
      "cache_read_input_tokens": 18516,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7263
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 18516,
          "cache_creation_input_tokens": 7263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7263,
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

_source line 29 · 2026-05-21T17:35:53.788Z_

<details><summary>↩ Tool result · `toolu_01LheX3thhYCDT8pNvpMk3F5`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data.
5	
6	\paragraph{Matching boundary and sample size.}
7	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory; replication with larger model samples is warranted.
8	
9	\paragraph{Generalizability.}
10	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd0c80d8-1111-4db0-bc69-f10f216aafe8",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "fd2b4ab8-740f-4225-b6b2-b08896e70aaf",
  "sourceToolAssistantUUID": "dd0c80d8-1111-4db0-bc69-f10f216aafe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T17:35:57.199Z_

Now let me read the references and appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd2b4ab8-740f-4225-b6b2-b08896e70aaf",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7pS8uEyFTm5sq1KwED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba34c45f-8c88-44da-8d82-6c932a398718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HURM313UrMx5j6vribYWb5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6153,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6153,
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

_source line 31 · 2026-05-21T17:35:59.108Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R7KE5Y8uhtMATsqTWyNQxe`</summary>

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
  "parentUuid": "ba34c45f-8c88-44da-8d82-6c932a398718",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7pS8uEyFTm5sq1KwED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "156ec1aa-bd28-402c-98bd-6b4dccbcd4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HURM313UrMx5j6vribYWb5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6153,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6153,
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

_source line 32 · 2026-05-21T17:35:59.120Z_

<details><summary>↩ Tool result · `toolu_01R7KE5Y8uhtMATsqTWyNQxe`</summary>

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
59	  author    = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},
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
73	@misc{zhang2024minkpp,
74	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
75	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
76	  year          = {2024},
77	  eprint        = {2404.02936},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2404.02936}
81	}
82	
83	% ============================================================
84	% IRT Methodology & Equating
85	% ============================================================
86	
87	@inproceedings{rodriguez2021evaluation,
88	  title     = {Evaluation Examples Are Not Equally Informative: How Should That Change {NLP} Leaderboards?},
89	  author    = {Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
90	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
91	  year      = {2021},
92	  pages     = {4486--4503}
93	}
94	
95	@article{donoghue1993mh,
96	  title   = {An Empirical Examination of the {Mantel-Haenszel} Statistic for the Study of Differential Item Functioning},
97	  author  = {Donoghue, John R. and Allen, Nancy L.},
98	  journal = {Applied Measurement in Education},
99	  volume  = {6},
100	  number  = {2},
101	  pages   = {163--179},
102	  year    = {1993}
103	}
104	
105	@misc{hardy2026scalability,
106	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
107	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
108	  year          = {2026},
109	  eprint        = {2603.24999},
110	  archivePrefix = {arXiv},
111	  primaryClass  = {cs.CL},
112	  url           = {https://arxiv.org/abs/2603.24999}
113	}
114	
115	@article{kim2019fpc,
116	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
117	  author  = {Kim, Seonghoon and Kolen, Michael},
118	  journal = {Applied Measurement in Education},
119	  year    = {2019},
120	  doi     = {10.1080/08957347.2019.1660344},
121	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
122	}
123	
124	@inproceedings{lalor2019irt,
125	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
126	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
127	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
128	  year      = {2019},
129	  doi       = {10.18653/v1/D19-1434},
130	  url       = {https://aclanthology.org/D19-1434/}
131	}
132	
133	@inproceedings{vania2021irt,
134	  title     = {Comparing Test Sets with Item Response Theory},
135	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
136	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
137	  year      = {2021},
138	  doi       = {10.18653/v1/2021.acl-long.92},
139	  url       = {https://aclanthology.org/2021.acl-long.92/}
140	}
141	
142	
143	@misc{habba2026growingpains,
144	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
145	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
146	  year          = {2026},
147	  eprint        = {2604.12843},
148	  archivePrefix = {arXiv},
149	  primaryClass  = {cs.CL},
150	  url           = {https://arxiv.org/abs/2604.12843}
151	}
152	
153	@inproceedings{zhou2026psnirt,
154	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
155	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
156	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
157	  year      = {2026},
158	  url       = {https://arxiv.org/abs/2505.15055}
159	}
160	
161	% ============================================================
162	% Dynamic Benchmark Design
163	% ============================================================
164	
165	@inproceedings{white2025livebench,
166	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
167	  author    = {White, Colin},
168	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
169	  year      = {2025},
170	  doi       = {10.48550/arXiv.2406.19314},
171	  url       = {https://arxiv.org/abs/2406.19314}
172	}
173	
174	@misc{kipnis2024metabench,
175	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
176	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
177	  year          = {2024},
178	  eprint        = {2407.12844},
179	  archivePrefix = {arXiv},
180	  primaryClass  = {cs.CL},
181	  url           = {https://arxiv.org/abs/2407.12844}
182	}
183	
184	@inproceedings{hendrycks2021mmlu,
185	  title     = {Measuring Massive Multitask Language Understanding},
186	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
187	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
188	  year      = {2021},
189	  url       = {https://arxiv.org/abs/2009.03300}
190	}
191	
192	@inproceedings{chiang2024chatbot,
193	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
194	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
195	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
196	  year      = {2024},
197	  doi       = {10.48550/arXiv.2403.04132},
198	  url       = {https://arxiv.org/abs/2403.04132}
199	}
200	
201	@inproceedings{li2024latesteval,
202	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
203	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
204	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
205	  year      = {2024},
206	  doi       = {10.48550/arXiv.2312.12343},
207	  url       = {https://arxiv.org/abs/2312.12343}
208	}
209	
210	@inproceedings{kiela2021dynabench,
211	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
212	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
213	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
214	  year      = {2021},
215	  doi       = {10.18653/v1/2021.naacl-main.324},
216	  url       = {https://arxiv.org/abs/2104.14337}
217	}
218	
219	% ============================================================
220	% DIF Statistical Methods
221	% ============================================================
222	
223	@article{belzak2020smallsample,
224	  title   = {Testing Differential Item Functioning in Small Samples},
225	  author  = {Belzak, William},
226	  journal = {Multivariate Behavioral Research},
227	  year    = {2020},
228	  doi     = {10.1080/00273171.2019.1671162},
229	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
230	}
231	
232	@incollection{holland1988mh,
233	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
234	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
235	  booktitle = {Test Validity},
236	  editor    = {Wainer, Howard and Braun, Henry I.},
237	  publisher = {Lawrence Erlbaum Associates},
238	  year      = {1988},
239	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
240	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
241	}
242	
243	@article{shealy1993sibtest,
244	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
245	  author  = {Shealy, Robin and Stout, William},
246	  journal = {Psychometrika},
247	  year    = {1993},
248	  doi     = {10.1007/BF02294572},
249	  url     = {https://link.springer.com/article/10.1007/BF02294572}
250	}
251	
252	@article{clauser1998dif,
253	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
254	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
255	  journal = {Educational Measurement: Issues and Practice},
256	  year    = {1998},
257	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
258	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
259	}
260	
261	@book{zumbo1999handbook,
262	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
263	  author    = {Zumbo, Bruno D.},
264	  year      = {1999},
265	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
266	  address   = {Ottawa},
267	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
268	}
269	
270	@article{meredith1993invariance,
271	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
272	  author  = {Meredith, William},
273	  journal = {Psychometrika},
274	  year    = {1993},
275	  doi     = {10.1007/BF02294825},
276	  url     = {https://link.springer.com/article/10.1007/BF02294825}
277	}
278	
279	@article{vandenberg2000invariance,
280	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
281	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
282	  journal = {Organizational Research Methods},
283	  year    = {2000},
284	  doi     = {10.1177/109442810031002},
285	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
286	}
287	
288	@article{swaminathan1990logistic,
289	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
290	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
291	  journal = {Journal of Educational Measurement},
292	  year    = {1990},
293	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
294	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
295	}
296	
297	@article{teresi2007dif,
298	  title   = {Differential Item Functioning and Health Assessment},
299	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
300	  journal = {Quality of Life Research},
301	  year    = {2007},
302	  doi     = {10.1007/s11136-007-9184-6},
303	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
304	}
305	
306	@book{lord1980irt,
307	  title     = {Applications of Item Response Theory to Practical Testing Problems},
308	  author    = {Lord, Frederic M.},
309	  year      = {1980},
310	  publisher = {Lawrence Erlbaum Associates},
311	  address   = {Hillsdale, NJ}
312	}
313	
314	@article{raju1988area,
315	  title   = {The Area between Two Item Characteristic Curves},
316	  author  = {Raju, Nambury S.},
317	  journal = {Psychometrika},
318	  year    = {1988},
319	  doi     = {10.1007/BF02294403},
320	  url     = {https://link.springer.com/article/10.1007/BF02294403}
321	}
322	
323	@article{muthen1985mimic,
324	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
325	  author  = {Muth{\'e}n, Bengt},
326	  journal = {Journal of Educational Statistics},
327	  year    = {1985},
328	  doi     = {10.2307/1164966}
329	}
330	
331	@article{woods2009mimic,
332	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
333	  author  = {Woods, Carol M.},
334	  journal = {Applied Psychological Measurement},
335	  year    = {2009},
336	  doi     = {10.1177/0146621609331279}
337	}
338	
339	% ============================================================
340	% LLM Evaluation Methodology
341	% ============================================================
342	
343	@article{burnell2023rethink,
344	  title   = {Rethink reporting of evaluation results in {AI}},
345	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
346	  journal = {Science},
347	  year    = {2023},
348	  doi     = {10.1126/science.adf6369},
349	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
350	}
351	
352	@article{chang2024survey,
353	  title   = {A Survey on Evaluation of Large Language Models},
354	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
355	  journal = {ACM Transactions on Intelligent Systems and Technology},
356	  year    = {2024},
357	  doi     = {10.1145/3641289},
358	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
359	}
360	
361	@inproceedings{maiapolo2024tinybenchmarks,
362	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
363	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
364	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
365	  year      = {2024},
366	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
367	}
368	
369	@article{nandakumar1993dif,
370	  author  = {Ratna Nandakumar},
371	  title   = {Simultaneous {DIF} amplification and cancellation: {Shealy}-{Stout}'s test for {DIF}},
372	  journal = {Journal of Educational Measurement},
373	  year    = {1993},
374	  volume  = {30},
375	  number  = {4},
376	  pages   = {293--311}
377	}
378	
379	@inproceedings{carlini2022quantifying,
380	  author    = {Nicholas Carlini and Daphne Ippolito and Matthew Jagielski and Katherine Lee and Florian Tram{\`e}r and Chiyuan Zhang},
381	  title     = {Quantifying Memorization Across Neural Language Models},
382	  booktitle = {International Conference on Learning Representations (ICLR)},
383	  year      = {2023},
384	  url       = {https://arxiv.org/abs/2202.07646}
385	}
386	
387	@inproceedings{tirumala2022memorization,
388	  author    = {Kushal Tirumala and Aram Markosyan and Luke Zettlemoyer and Armen Aghajanyan},
389	  title     = {Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models},
390	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
391	  year      = {2022},
392	  url       = {https://arxiv.org/abs/2205.10770}
393	}
394	
395	% ============================================================
396	% Additional Benchmarks
397	% ============================================================
398	
399	@inproceedings{sakaguchi2021winogrande,
400	  title     = {{WinoGrande}: An Adversarial {Winograd} Schema Challenge at Scale},
401	  author    = {Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
402	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
403	  volume    = {34},
404	  number    = {05},
405	  pages     = {8732--8740},
406	  year      = {2020}
407	}
408	
409	@inproceedings{lin2022truthfulqa,
410	  title     = {{TruthfulQA}: Measuring How Models Mimic Human Falsehoods},
411	  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
412	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
413	  year      = {2022},
414	  pages     = {3214--3252}
415	}
416	
417	@inproceedings{zellers2019hellaswag,
418	  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},
419	  author    = {Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farzaneh, Ali and Choi, Yejin},
420	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
421	  year      = {2019},
422	  pages     = {4791--4800}
423	}
424	
425	@article{clark2018arc,
426	  title   = {Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
427	  author  = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
428	  journal = {arXiv preprint arXiv:1803.05457},
429	  year    = {2018}
430	}
431	
432	% ============================================================
433	% Benchmark Quality Assessment
434	% ============================================================
435	
436	@article{zhu2026bhi,
437	  title   = {Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of {LLMs}},
438	  author  = {Zhu, Longyuan and Hua, Hairan and Miao, Linlin and Zhao, Bing},
439	  journal = {arXiv preprint arXiv:2602.11674},
440	  year    = {2026}
441	}
442	
443	@article{maeda2025difllm,
444	  title   = {Finding Words Associated with {DIF}: Predicting {DIF} using {LLMs} and Explainable {AI}},
445	  author  = {Maeda, Hotaka},
446	  journal = {arXiv preprint arXiv:2502.07017},
447	  year    = {2025}
448	}
449	
450	@misc{qian2026benchmark2,
451	  title         = {{Benchmark}$^2$: Systematic Evaluation of {LLM} Benchmarks},
452	  author        = {Qian, Qi and Huang, Chengsong},
453	  year          = {2026},
454	  eprint        = {2601.03986},
455	  archivePrefix = {arXiv},
456	  primaryClass  = {cs.CL},
457	  url           = {https://arxiv.org/abs/2601.03986}
458	}
459	
460	@misc{luo2025medirt,
461	  title         = {Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks},
462	  author        = {Luo, Zhimeng and Wu, Lixin and Frisch, Adam and He, Daqing},
463	  year          = {2025},
464	  eprint        = {2509.24186},
465	  archivePrefix = {arXiv},
466	  primaryClass  = {cs.CL},
467	  url           = {https://arxiv.org/abs/2509.24186}
468	}
469	
470	@misc{li2025atlas,
471	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
472	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
473	  year          = {2025},
474	  eprint        = {2511.04689},
475	  archivePrefix = {arXiv},
476	  primaryClass  = {cs.CL},
477	  url           = {https://arxiv.org/abs/2511.04689}
478	}
479	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "156ec1aa-bd28-402c-98bd-6b4dccbcd4c9",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "cd14ac11-a91b-4a10-90c8-17f0a713a9f3",
  "sourceToolAssistantUUID": "156ec1aa-bd28-402c-98bd-6b4dccbcd4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T17:35:59.572Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PeRq14nXAkMpTuMUaBRWob`</summary>

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
  "parentUuid": "cd14ac11-a91b-4a10-90c8-17f0a713a9f3",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7pS8uEyFTm5sq1KwED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dc0aecd-e189-4f42-b52c-fd4cffa79abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HURM313UrMx5j6vribYWb5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6153,
      "cache_read_input_tokens": 25779,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 25779,
          "cache_creation_input_tokens": 6153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6153,
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

_source line 34 · 2026-05-21T17:35:59.581Z_

<details><summary>↩ Tool result · `toolu_01PeRq14nXAkMpTuMUaBRWob`</summary>

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
31	\section{Additional Figures}
32	\label{app:figures}
33	
34	\begin{figure}[h]
35	\centering
36	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
37	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
38	\label{app:fig_matching}
39	\end{figure}
40	
41	\begin{figure}[h]
42	\centering
43	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
44	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
45	\label{app:fig_downstream}
46	\end{figure}
47	
48	\begin{figure}[h]
49	\centering
50	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
51	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
52	\label{app:fig_gsm1k}
53	\end{figure}
54	
55	\section{Cross-Benchmark Comparison}
56	\label{app:gsm8k_details}
57	
58	\begin{table}[h]
59	\centering
60	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal measurement drift with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
61	\label{tab:gsm8k_comparison}
62	\small
63	\begin{tabular}{lcc}
64	\toprule
65	Metric & MMLU & GSM8K \\
66	\midrule
67	Items & 12,508 & 1,319 \\
68	Models & 5,227 & 6,702 \\
69	Temporal C\% & 31.3\% & 18.9\% \\
70	Sanity C\% & 0.18\% & 0.3\% \\
71	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
72	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
73	\bottomrule
74	\end{tabular}
75	\end{table}
76	
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dc0aecd-e189-4f42-b52c-fd4cffa79abe",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "fb429097-5601-442d-b232-9deb6351b853",
  "sourceToolAssistantUUID": "5dc0aecd-e189-4f42-b52c-fd4cffa79abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T17:36:03.302Z_

Now let me check the paper's page count and figures to understand scope.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb429097-5601-442d-b232-9deb6351b853",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7prnyHEnJ2PRguLwXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b08378d7-0fdd-49d3-853e-8f141004e582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEG7Euvb4HFEhcooehXVKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10818,
      "cache_read_input_tokens": 31932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10818,
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

_source line 36 · 2026-05-21T17:36:05.348Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DPP9aKhGSPbHqkLi4YwL1s`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/*.tex",
  "description": "Count lines in each section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08378d7-0fdd-49d3-853e-8f141004e582",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7prnyHEnJ2PRguLwXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "073e1121-3acf-4132-a20a-55253ad8a3a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEG7Euvb4HFEhcooehXVKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10818,
      "cache_read_input_tokens": 31932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10818,
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

_source line 37 · 2026-05-21T17:36:05.511Z_

<details><summary>↩ Tool result · `toolu_01DPP9aKhGSPbHqkLi4YwL1s`</summary>

```text
    3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
   76 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex
    4 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
   22 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex
  110 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
   27 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
   10 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
   59 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
   14 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
  325 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "073e1121-3acf-4132-a20a-55253ad8a3a0",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "fdc9ecb0-3f76-4d61-b0fb-1dbdeed93896",
  "sourceToolAssistantUUID": "073e1121-3acf-4132-a20a-55253ad8a3a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T17:36:05.887Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Qbortp81sAWT5xMQfr6A67`</summary>

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
  "parentUuid": "fdc9ecb0-3f76-4d61-b0fb-1dbdeed93896",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7prnyHEnJ2PRguLwXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeefc121-e94d-4792-b22d-19df097c7039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEG7Euvb4HFEhcooehXVKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10818,
      "cache_read_input_tokens": 31932,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10818
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 31932,
          "cache_creation_input_tokens": 10818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10818,
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

_source line 39 · 2026-05-21T17:36:05.916Z_

<details><summary>↩ Tool result · `toolu_01Qbortp81sAWT5xMQfr6A67`</summary>

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
  "parentUuid": "eeefc121-e94d-4792-b22d-19df097c7039",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "6d722436-9676-4052-be60-96a65505b4f1",
  "sourceToolAssistantUUID": "eeefc121-e94d-4792-b22d-19df097c7039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T17:36:08.801Z_

Now I have a thorough understanding of the paper. Let me also check the ROADMAP and any other context files for understanding the project trajectory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d722436-9676-4052-be60-96a65505b4f1",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7qKz6KgJx8vA2chsfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40a7b49d-1576-4dff-952d-092a9f922b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eoZdBj86CYd1jp4mw7m6z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 42750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 794,
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

_source line 41 · 2026-05-21T17:36:09.618Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LNHEHtX5g3DpmyYF21jR1f`</summary>

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
  "parentUuid": "40a7b49d-1576-4dff-952d-092a9f922b1c",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7qKz6KgJx8vA2chsfA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01bf0297-4485-4e00-bea5-61da13671270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eoZdBj86CYd1jp4mw7m6z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 42750,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 794
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 42750,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 794,
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

_source line 42 · 2026-05-21T17:36:09.621Z_

<details><summary>↩ Tool result · `toolu_01LNHEHtX5g3DpmyYF21jR1f`</summary>

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
  "parentUuid": "01bf0297-4485-4e00-bea5-61da13671270",
  "isSidechain": true,
  "promptId": "8a16699c-6447-4352-ba4c-634559e8cb22",
  "agentId": "ac01af25fe1457019",
  "type": "user",
  "uuid": "8726feac-aaae-416e-86e2-ccb243290455",
  "sourceToolAssistantUUID": "01bf0297-4485-4e00-bea5-61da13671270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T17:37:34.634Z_



Now I have all the material needed. Let me compose the review.

---

## Review: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis

**Reviewer 2 (R2) -- Focus: Novelty and Related Work**

---

### 1. Summary

This paper applies the Mantel-Haenszel Differential Item Functioning (MH-DIF) procedure from educational psychometrics to detect temporal measurement drift in LLM benchmarks, finding that 17.9--31.3% of items across six METABENCH benchmarks exhibit large DIF between 2023 and 2024 model cohorts. The paper further argues that web-overlap contamination labels are orthogonal to DIF flags (enrichment ~1.0) and therefore constitute inappropriate ground truth for differential detectors. A semi-synthetic injection framework with cross-subject matching validates detection power while maintaining zero false positive inflation.

---

### 2. Strengths

**S1. Scale and thoroughness of empirical analysis.** 5,227 models x 12,508 MMLU items is, to my knowledge, the largest DIF study on LLM benchmarks. The six-benchmark replication (Table 3) and the gradient from knowledge-intensive to procedural benchmarks is a genuinely informative finding. The paper does not oversell: it correctly notes rankings are preserved (rho ~0.997) and that DIF is diagnostic rather than destructive.

**S2. The global-vs-differential distinction is well-articulated and important.** The conceptual contribution in Section 1 and Figure 1 -- that web-overlap labels measure global exposure while DIF measures differential functioning -- is a clear and useful distinction that the contamination detection community has largely conflated. The empirical confirmation (enrichment = 0.964, phi = 0.012) is clean. This is the paper's strongest intellectual contribution.

**S3. Semi-synthetic validation is carefully designed.** The cross-subject matching protocol with its zero-FPR guarantee (Proposition 1) is a thoughtful methodological contribution. The dose-response curve (Figure 2) and the multi-subject injection boundary analysis (FPR < 0.007 for k <= 5) demonstrate engineering care. The extension to GSM8K with external matching confirms portability.

**S4. Honest about limitations.** The paper explicitly acknowledges that MH-DIF detects *that* items function differently but not *why*, that the GSM1K analysis is exploratory (N=33), and that only uniform DIF is captured (logistic regression reveals additional 24.8% non-uniform DIF). The Limitations section is appropriately scoped.

**S5. Multiple control conditions.** The random-split sanity check (0.18% C), ability-quintile comparison (2.9%), within-family comparison (61.3%), matched-ability analysis reducing to ~28-29% across conditions, and the Simpson's paradox analysis collectively make a convincing case that the 31% figure is not artifactual.

---

### 3. Weaknesses

**W1. (Major) The core method is an off-the-shelf procedure with no algorithmic modification.** The paper repeatedly and honestly states "our contribution is methodological and empirical, not algorithmic" and "we do not modify the MH procedure." MH-DIF with ETS classification is a standard procedure from the 1988 Holland & Thayer paper, and applying it to a new population (LLMs instead of human test-takers) is a transfer, not an invention. The novelty question is whether the *findings* are sufficiently surprising or actionable. Finding that ~31% of MMLU items behave differently across model generations is interesting but arguably expected given the community's extensive documentation of contamination and benchmark saturation. The paper's own conclusion that rankings are preserved (rho ~0.997) somewhat undercuts the urgency. For a top-venue acceptance, I would need to see either (a) a methodological contribution beyond standard MH-DIF, or (b) findings that lead to concrete actionable changes in evaluation practice. The proposed audit protocol (Section 5.4) is a start but remains speculative.

**W2. (Major) Related work has significant gaps despite appearing comprehensive.** The Related Work section is substantially improved over what the summary suggested (it now cites Golchin & Surdeanu 2024, Lalor et al. 2019, Vania et al. 2021, Rodriguez et al. 2021), but several important missing citations weaken the positioning:

- **Deng et al. (2024), "Investigating Data Contamination in Modern Benchmarks for Large Language Models"**: Directly relevant as it studies contamination at item level across benchmarks and would contextualize the ground-truth meta-critique.
- **Yang et al. (2023), "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples"**: Specifically addresses MMLU contamination through rephrasing, directly relevant to whether DIF captures paraphrase-level sensitivity.
- **Jacovi et al. (2023), "Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks"**: Discusses the benchmark lifecycle problem that motivates temporal DIF analysis.
- **Raji et al. (2021), "AI and the Everything in the Whole Wide World Benchmark"**: Foundational critique of benchmark misuse that would strengthen the Discussion.
- **Oren et al. (2024)** is mentioned in the paper summary but does not appear in the bib file -- if this refers to the perturbation-based detection work, it should be cited.

More critically, the paper does not engage with **Maeda (2025)** beyond a single sentence despite it being the most directly comparable work (predicting DIF in educational settings using LLMs). The relationship deserves a paragraph: Maeda predicts *which* items will exhibit DIF; this paper detects DIF empirically. Are the item features Maeda identifies consistent with the difficulty-direction interaction found here?

**W3. (Major) The "ground truth meta-critique" contribution is partially circular.** The argument runs: (1) DIF and web-overlap flags are orthogonal; (2) semi-synthetic injection shows DIF works; (3) therefore the ground truth is wrong, not the detector. But step (2) only shows DIF detects *injected* differential behavior (incorrect-to-correct flipping), not that it detects real-world contamination. The paper acknowledges DIF cannot determine *why* items function differently, which means the "meta-critique" reduces to: "web-overlap labels don't predict DIF flags." This is true but trivially expected if DIF captures *any* source of temporal change (capability improvement, training methodology shifts, RLHF effects) beyond contamination. Framing this as a "validation methodology gap" overstates the claim -- it is more accurately a demonstration that the two methods measure different constructs, which is useful but not a critique of the contamination literature's validation practice unless one believes DIF *should* capture contamination specifically.

**W4. (Minor) The "diagnostic lens" framing feels post-hoc.** The difficulty-direction interaction (rho = -0.597: gains on hard items, erosion on easy ones) and the model-family profiles (Llama-3 +53, Mistral -35) are interesting descriptive findings, but calling them a "diagnostic lens" implies more actionability than is demonstrated. What should a benchmark maintainer *do* with the information that Llama-3 gains rank positions when DIF items are removed? The paper proposes an audit protocol with thresholds (Section 5.4) but does not validate whether acting on these thresholds improves measurement quality.

**W5. (Minor) The contribution count was reduced from 4 to 3 but the scope still feels diffuse.** The paper tries to be simultaneously about: (a) a validation framework, (b) a meta-critique of contamination ground truth, and (c) a large-scale empirical finding. Each of these could be a focused paper. Together, none gets the depth it deserves. The ground-truth meta-critique in particular would benefit from engaging with multiple contamination detection methods (ConStat, DVD, Min-K%) empirically rather than arguing by transitivity from web-overlap labels.

**W6. (Minor) Concurrent work overlap with Growing Pains (Habba et al. 2026).** The paper acknowledges Growing Pains as "complementary" but the relationship is deeper than stated. Both papers use psychometric methods to address temporal comparability of LLM benchmarks; both use the METABENCH-like response matrices; both arrive at the conclusion that item-level analysis is needed. The paper claims DIF could flag anchor degradation for FPC, but this is speculative without empirical demonstration. A reviewer familiar with both papers would want to see a clearer delineation of when to use DIF vs. FPC.

**W7. (Minor) Reference count in main text is thin.** The Related Work section is dense but the main body (Introduction, Method, Experiments) cites very few works beyond the core data sources and the method origin. This creates an impression of insularity.

---

### 4. Questions to Authors

**Q1.** You show enrichment ~1.0 between DIF flags and web-overlap labels and interpret this as the ground truth being wrong. But have you considered that DIF might primarily capture *capability change* rather than *contamination*? If so, why frame the finding as a "meta-critique" of contamination validation rather than simply as evidence that DIF and contamination detection measure different things?

**Q2.** The semi-synthetic injection flips incorrect responses to correct, which is a strong and detectable signal. Have you tested more subtle injection patterns (e.g., partial flipping, or flipping that preserves difficulty ordering) to assess sensitivity under realistic contamination scenarios?

**Q3.** The difficulty-direction interaction (rho = -0.597) is one of the most interesting findings. Can you provide a mechanistic hypothesis? Is this consistent with models improving on hard items through genuine capability gains while losing calibration on easy items through overconfidence or distribution shift?

**Q4.** How sensitive are results to the temporal cohort boundary? You show 2023-H2 vs. 2024-H1 yields C% = 34.35%, which is *higher* than full-year comparison (31.3%). Does this suggest the effect is concentrated in a specific transition period? Have you tried sliding-window analysis?

**Q5.** You note that logistic regression DIF reveals 24.8% additional non-uniform DIF beyond what MH captures. Given that non-uniform DIF (where the direction of DIF reverses across ability levels) has a different interpretation than uniform DIF, wouldn't it be more informative to use logistic regression as the primary method? What is the concordance between the two methods at the item level?

**Q6.** Regarding the relationship with Maeda (2025): do the item features associated with DIF in your analysis (difficulty, discrimination, subject domain) match the features Maeda identifies as predictive of DIF in educational settings?

---

### 5. Soundness: 3.5 / 5

The statistical methodology is correctly applied and the controls are thorough. The main soundness concern is the circular reasoning in the ground-truth meta-critique (W3) and the fact that DIF captures an undifferentiated mixture of contamination, capability change, and methodological shifts without the paper being able to separate these.

### 6. Excitement: 2.5 / 5

The global-vs-differential distinction (S2) is a genuine insight, but the core finding (items behave differently across model generations) is not deeply surprising given prior work on contamination and benchmark dynamics. The method is imported wholesale from educational testing. The actionable implications remain speculative.

### 7. Reproducibility: 4 / 5

METABENCH is public, MH-DIF is a standard procedure, and the paper provides sufficient detail to replicate. Code is promised at an anonymous repository. The semi-synthetic framework is well-specified. Minor deduction for the GSM1K analysis where N=33 limits reproducibility of the correlation finding.

### 8. Overall Assessment: 3.0 (Findings)

The paper makes a solid empirical contribution: the 31% temporal DIF finding is well-established through multiple controls, the global-vs-differential distinction is intellectually valuable, and the semi-synthetic validation framework is carefully designed. However, the novelty is limited by the wholesale adoption of an existing method, the ground-truth meta-critique has circularity issues, the related work has gaps in engaging with concurrent and relevant prior work, and the paper's diffuse scope prevents any single contribution from reaching the depth expected at a top venue. The findings are useful to the community but do not clear the bar for main conference acceptance. This is a natural fit for Findings.

### 9. Confidence: 4 / 5

I am familiar with both the psychometric literature on DIF and the LLM benchmark contamination literature. I have read the paper carefully and checked the methodology against standard references. My main uncertainty is whether concurrent work (particularly Growing Pains) has shifted the novelty landscape in ways I may not fully appreciate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8726feac-aaae-416e-86e2-ccb243290455",
  "isSidechain": true,
  "agentId": "ac01af25fe1457019",
  "requestId": "req_011CbG7qfAG5tqFtDeCZ1KYC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74d44189-c818-4a97-a54a-80b3ceeabe9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "323cfb50-fdc2-4808-8997-11b497c1cdb0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFpBZJDD2kSRGPqY8u6mUR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 43544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 744,
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
