# Research conversation: You are Reviewer R2 for an EMNLP 2026 ARR submission. Your focus: **Novelty, Framing, and Related Work** (Excitement, po

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a16ad29a4bc1edec4.jsonl`
- **Structured JSON:** [`b7f867a12ea5ca04616b.json`](../../sessions/b7/b7f867a12ea5ca04616b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-21T17:48:16.335Z_

You are Reviewer R2 for an EMNLP 2026 ARR submission. Your focus: **Novelty, Framing, and Related Work** (Excitement, positioning, contribution clarity).

## Venue calibration
EMNLP 2026 ARR scoring: 5=Award (top 2.5%), 4=Conference (Main), 3=Findings, 2=Resubmit, 1=Do not resubmit. Accept rate ~21%. Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper summary
**Title:** "Large-Scale Item-Level Stability Analysis of LLM Benchmarks"

The paper applies the Mantel-Haenszel (MH) statistic as a nonparametric group-comparison test to METABENCH (5,227 models × 12,508 MMLU items) to characterize item-level behavioral stability between 2023 and 2024-H1 temporal cohorts. 

**Core claims:**
1. 31.3% of MMLU items show behavioral heterogeneity between temporal cohorts, but ~52% of this is cohort composition artifact (permutation null = 16.4%), leaving ~14.9% effective signal.
2. Cross-benchmark replication shows effective rates from 2.3% (HellaSwag) to 14.9% (MMLU) — MMLU is an outlier.
3. A semi-synthetic validation framework with cross-subject matching eliminates false-positive inflation (ΔFPR ≈ 0.003).
4. Three independent detection methods (MH-DIF, ConStat, DVD) flag nearly disjoint item sets (pairwise Jaccard 0.06-0.19), suggesting a field-wide construct validity challenge.
5. DIF flags are cohort-dependent (reasoning-RL models destabilize: Jaccard=0.43).
6. Both unidimensional and bifactor IRT are severely misspecified for MMLU (CFI<0.72, RMSEA>0.08).
7. Item removal is not viable remediation (reliability drops to 0.85 at 31% replacement).

**Framing:** The paper frames item-level stability as an operational metric for benchmark maintenance: "characterize, monitor, but do not remediate."

**Paper structure (8 pages + appendix):**
- Intro (1 page), Related Work (0.5 pages), Method (1 page), Experiments (4.5 pages with 15 sub-experiments), Discussion (0.7 pages), Limitations (0.5 pages), Conclusion (0.3 pages)
- 20 tables, 12 references

**Related work cited:**
- LLM contamination: Li et al. 2024 (web overlap), Oren et al. 2024 (test set contamination), Shi et al. 2024 (Min-K%), Dekoninck et al. 2024 (ConStat)
- DIF: Holland & Thayer 1988 (MH), Sinharay et al. 2006 (Bayesian DIF), Tutz & Berger 2016 (IFT)
- Benchmark stability: Raju et al. 2024 (growing pains), Polo et al. 2024 (tinyBenchmarks)
- Data: Perlitz et al. 2024 (METABENCH), Zhang et al. 2024 (GSM1K), Mantel & Haenszel 1959

**Key experimental results that shape the narrative:**
- Permutation null: 16.4% mean C% from cohort composition alone
- Semi-synthetic: ΔTPR=0.26 at p=0.5 (moderate), cross-subject matching ΔFPR=0.003 (strong)
- RL robustness: Jaccard=0.43 when adding 13 reasoning-RL models (flags are cohort-dependent)
- Method disagreement: DIF/ConStat/DVD pairwise Jaccard 0.06-0.19; ensemble killed (AUROC 0.58)
- IRT: Both models fail; bifactor doesn't converge
- GSM8K: Effective C%=3.7% (near noise floor); GSM1K correlation non-significant
- Item generation: All methods fail targets (best ρ=0.47 vs. 0.75 target)
- Cumulative Bayesian DIF: Power 0.61 after 4 administrations, below 0.70 target
- Graceful degradation: Removal not viable at 31%

## Your review task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Novelty assessment** — Is applying MH-DIF to LLM benchmarks novel? Is the contribution primarily methodological, empirical, or conceptual? How does it advance beyond existing work (Raju et al., Li et al., Oren et al.)?
3. **Framing critique** — Is "large-scale item-level stability analysis" a well-defined contribution? Is the reframing from DIF to "nonparametric group-comparison test" convincing or does it undermine the theoretical foundation? Is "characterize, monitor, don't remediate" a satisfying conclusion for an 8-page paper?
4. **Related work gaps** — What important work is missing? Consider: measurement invariance literature, IRT-based DIF beyond MH, LLM evaluation methodology (HELM, Open LLM Leaderboard), benchmark contamination detection (beyond the 3 cited), psychometrics applied to LLMs.
5. **Contribution clarity** — Are the contributions clearly stated? Is it clear what the reader should take away? Does the breadth (15 experiments) dilute the message?
6. **Strengths** (bulleted)
7. **Weaknesses** (bulleted, with severity)
8. **Questions for authors**
9. **Preliminary scores**: Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Overall (1-5 half-point scale)

Be rigorous. Pay special attention to:
- Whether 12 references is sufficient for a paper spanning psychometrics + NLP + benchmark evaluation
- Whether the "construct validity crisis" framing is earned by the evidence or overclaimed
- Whether the paper's honest reporting of negative results (failed experiments) is a strength or signals an incomplete research program
- Whether the "monitoring over remediation" recommendation is actionable
- Whether MMLU-as-outlier undermines generalizability claims
- The paper effectively reports that most of its experiments fail or produce weak results — is this publishable as characterization?

Format your review as structured markdown.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "a503f5b4-31b4-40f1-a28f-dc15a5ea29e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T17:48:16.338Z_

```json
{
  "parentUuid": "a503f5b4-31b4-40f1-a28f-dc15a5ea29e5",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
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
  "uuid": "e5b08a0e-521c-407d-854c-6f5d52cd9a3b",
  "timestamp": "2026-05-21T17:48:16.338Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T17:48:19.056Z_



I'll start by reading the paper and key project files to ground my review in the actual text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b08a0e-521c-407d-854c-6f5d52cd9a3b",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mAZohEhvrFwEkPrr3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c9c7531-893a-4ac1-9665-8dc11dfa8cb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v4HACPv9LGziUBKaogR3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8025,
      "cache_read_input_tokens": 8732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8025,
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

_source line 4 · 2026-05-21T17:48:20.977Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TtbXEJJFQtmz8s4bANpixV`</summary>

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
  "parentUuid": "7c9c7531-893a-4ac1-9665-8dc11dfa8cb4",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mAZohEhvrFwEkPrr3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "804337bb-b9a1-4d16-b2c7-5049d3938a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v4HACPv9LGziUBKaogR3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8025,
      "cache_read_input_tokens": 8732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8025,
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

_source line 5 · 2026-05-21T17:48:20.997Z_

<details><summary>↩ Tool result · `toolu_01TtbXEJJFQtmz8s4bANpixV`</summary>

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
  "parentUuid": "804337bb-b9a1-4d16-b2c7-5049d3938a2d",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "53acafff-188c-49bc-9690-74aeade04e7c",
  "sourceToolAssistantUUID": "804337bb-b9a1-4d16-b2c7-5049d3938a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T17:48:24.383Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BHtMP5eBnC39pqUAc16u7X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53acafff-188c-49bc-9690-74aeade04e7c",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mAZohEhvrFwEkPrr3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f48e136-3b5d-4231-a380-7de71f33ebe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v4HACPv9LGziUBKaogR3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8025,
      "cache_read_input_tokens": 8732,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 8732,
          "cache_creation_input_tokens": 8025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8025,
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

_source line 7 · 2026-05-21T17:48:24.396Z_

<details><summary>↩ Tool result · reported error · `toolu_01BHtMP5eBnC39pqUAc16u7X`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen. Did you mean main.aux?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f48e136-3b5d-4231-a380-7de71f33ebe2",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "f66b02a6-ee01-40f6-bcee-bf7a10bcb300",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen. Did you mean main.aux?",
  "sourceToolAssistantUUID": "9f48e136-3b5d-4231-a380-7de71f33ebe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T17:48:26.800Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YbUePBgxJdxNSzGswPE2P4`</summary>

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
  "parentUuid": "f66b02a6-ee01-40f6-bcee-bf7a10bcb300",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mmH7XBovtiVcDzrdG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9607978-5f3d-4114-a19c-0e3ab2e15bef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFynQCdFTKMaNcmtdmpZzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 16757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1522,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 9 · 2026-05-21T17:48:26.824Z_

<details><summary>↩ Tool result · `toolu_01YbUePBgxJdxNSzGswPE2P4`</summary>

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
  "parentUuid": "e9607978-5f3d-4114-a19c-0e3ab2e15bef",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "27d6b6d5-4e43-4c78-90d9-b3161e771bb2",
  "sourceToolAssistantUUID": "e9607978-5f3d-4114-a19c-0e3ab2e15bef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T17:48:27.390Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HNUFgQ1tbdk2BNiQrTkWcL`</summary>

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
  "parentUuid": "27d6b6d5-4e43-4c78-90d9-b3161e771bb2",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mmH7XBovtiVcDzrdG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0544d018-07dc-4ea0-9f13-f8398a09b6ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFynQCdFTKMaNcmtdmpZzx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 16757,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 16757,
          "cache_creation_input_tokens": 1522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1522,
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

_source line 11 · 2026-05-21T17:48:27.415Z_

<details><summary>↩ Tool result · `toolu_01HNUFgQ1tbdk2BNiQrTkWcL`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0544d018-07dc-4ea0-9f13-f8398a09b6ff",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "24a841be-e3a0-46eb-a523-3321d0cccaae",
  "sourceToolAssistantUUID": "0544d018-07dc-4ea0-9f13-f8398a09b6ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T17:48:30.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WnEA4ZZtJp1uCRHUm9GWz4`</summary>

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
  "parentUuid": "24a841be-e3a0-46eb-a523-3321d0cccaae",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mzB1LkDbRDomf5CJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "899f406a-839a-4671-887c-ebf820e9d323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Fws7M2fR4soKdJj1irCG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 331,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-21T17:48:30.182Z_

<details><summary>↩ Tool result · `toolu_01WnEA4ZZtJp1uCRHUm9GWz4`</summary>

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
  "parentUuid": "899f406a-839a-4671-887c-ebf820e9d323",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "8877fd56-99c3-4fc4-a972-216649291f55",
  "sourceToolAssistantUUID": "899f406a-839a-4671-887c-ebf820e9d323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T17:48:30.567Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MvpLW7nzGsJXDYG6WhpbUm`</summary>

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
  "parentUuid": "8877fd56-99c3-4fc4-a972-216649291f55",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mzB1LkDbRDomf5CJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e04ef199-67a9-4d00-ba75-0ed7d559ce4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Fws7M2fR4soKdJj1irCG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 331,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-21T17:48:30.577Z_

<details><summary>↩ Tool result · `toolu_01MvpLW7nzGsJXDYG6WhpbUm`</summary>

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
  "parentUuid": "e04ef199-67a9-4d00-ba75-0ed7d559ce4b",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "dfb48735-4051-442f-9a46-43212273e80a",
  "sourceToolAssistantUUID": "e04ef199-67a9-4d00-ba75-0ed7d559ce4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T17:48:31.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_011r6zq2YyFC5ynSVg94rCLp`</summary>

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
  "parentUuid": "dfb48735-4051-442f-9a46-43212273e80a",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mzB1LkDbRDomf5CJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4beae487-a26b-433f-aaa7-9e3114ef1c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Fws7M2fR4soKdJj1irCG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 331,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 17 · 2026-05-21T17:48:31.046Z_

<details><summary>↩ Tool result · `toolu_011r6zq2YyFC5ynSVg94rCLp`</summary>

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
  "parentUuid": "4beae487-a26b-433f-aaa7-9e3114ef1c10",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "6a0f4f3d-fc05-4692-8cbe-f10fdcc28d43",
  "sourceToolAssistantUUID": "4beae487-a26b-433f-aaa7-9e3114ef1c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T17:48:32.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EzR9yTSCPCZT7R2K3b3ePH`</summary>

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
  "parentUuid": "6a0f4f3d-fc05-4692-8cbe-f10fdcc28d43",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mzB1LkDbRDomf5CJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89fce97b-f5dc-444e-a385-898873d3cc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Fws7M2fR4soKdJj1irCG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 331,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 19 · 2026-05-21T17:48:32.020Z_

<details><summary>↩ Tool result · `toolu_01EzR9yTSCPCZT7R2K3b3ePH`</summary>

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
  "parentUuid": "89fce97b-f5dc-444e-a385-898873d3cc61",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "31601178-5790-402e-b800-144aab0a3f6b",
  "sourceToolAssistantUUID": "89fce97b-f5dc-444e-a385-898873d3cc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T17:48:32.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NckkNyWBHBChm5xhSgPYMR`</summary>

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
  "parentUuid": "31601178-5790-402e-b800-144aab0a3f6b",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8mzB1LkDbRDomf5CJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "389e6318-54ce-4d12-a674-79596d566c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Fws7M2fR4soKdJj1irCG5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 18279,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 18279,
          "cache_creation_input_tokens": 331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 331,
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

_source line 21 · 2026-05-21T17:48:32.219Z_

<details><summary>↩ Tool result · `toolu_01NckkNyWBHBChm5xhSgPYMR`</summary>

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
  "parentUuid": "389e6318-54ce-4d12-a674-79596d566c0a",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "6d40c0cf-0fd6-4328-b80b-c165ebf7239e",
  "sourceToolAssistantUUID": "389e6318-54ce-4d12-a674-79596d566c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T17:48:35.638Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HkukGzYcU7WpYkVYB5ySKn`</summary>

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
  "parentUuid": "6d40c0cf-0fd6-4328-b80b-c165ebf7239e",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nLmVxJAAPhypNVwFn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be1ece4c-7567-464c-81e0-cc85dce36531",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B42rUrPHCdo1gF1N85rzAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15900,
      "cache_read_input_tokens": 18610,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 18610,
          "cache_creation_input_tokens": 15900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15900,
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

_source line 23 · 2026-05-21T17:48:35.643Z_

<details><summary>↩ Tool result · `toolu_01HkukGzYcU7WpYkVYB5ySKn`</summary>

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
  "parentUuid": "be1ece4c-7567-464c-81e0-cc85dce36531",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "7fbcaf7e-138d-49d1-ad4d-f1ad3f85331c",
  "sourceToolAssistantUUID": "be1ece4c-7567-464c-81e0-cc85dce36531",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T17:48:39.593Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UnfitpuxUvmgVd33TktTHQ`</summary>

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
  "parentUuid": "7fbcaf7e-138d-49d1-ad4d-f1ad3f85331c",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nbNqLB44XFtZw6qnk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b3407f2-a7d1-4be2-985a-52ad168b7933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JvwvsFA2d7rtj3GJvxnZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4560,
      "cache_read_input_tokens": 34510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4560,
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

_source line 25 · 2026-05-21T17:48:39.599Z_

<details><summary>↩ Tool result · `toolu_01UnfitpuxUvmgVd33TktTHQ`</summary>

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
  "parentUuid": "8b3407f2-a7d1-4be2-985a-52ad168b7933",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "745f47b2-933d-4c58-a0ad-eb0f8172e5d4",
  "sourceToolAssistantUUID": "8b3407f2-a7d1-4be2-985a-52ad168b7933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T17:48:39.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_0125M6PSwzQU9WAZxCukk94y`</summary>

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
  "parentUuid": "745f47b2-933d-4c58-a0ad-eb0f8172e5d4",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nbNqLB44XFtZw6qnk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "994c7aa9-034d-4330-a9b0-a1d04a9f9f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JvwvsFA2d7rtj3GJvxnZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4560,
      "cache_read_input_tokens": 34510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4560,
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

_source line 27 · 2026-05-21T17:48:39.954Z_

<details><summary>↩ Tool result · `toolu_0125M6PSwzQU9WAZxCukk94y`</summary>

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
  "parentUuid": "994c7aa9-034d-4330-a9b0-a1d04a9f9f1d",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "0108ecf7-2a89-4f90-b850-96078c4be6fe",
  "sourceToolAssistantUUID": "994c7aa9-034d-4330-a9b0-a1d04a9f9f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T17:48:40.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YPxAgb4cJ5WZiDCf3bLNeZ`</summary>

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
  "parentUuid": "0108ecf7-2a89-4f90-b850-96078c4be6fe",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nbNqLB44XFtZw6qnk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dc2281e-1c42-4b8a-90f0-e7d285ccab8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JvwvsFA2d7rtj3GJvxnZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4560,
      "cache_read_input_tokens": 34510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4560,
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

_source line 29 · 2026-05-21T17:48:40.460Z_

<details><summary>↩ Tool result · `toolu_01YPxAgb4cJ5WZiDCf3bLNeZ`</summary>

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
  "parentUuid": "8dc2281e-1c42-4b8a-90f0-e7d285ccab8b",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "302fcae9-6de0-48a6-8809-5df6a6097239",
  "sourceToolAssistantUUID": "8dc2281e-1c42-4b8a-90f0-e7d285ccab8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T17:48:41.113Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PaAfAR8N8HnwWHY9TZEjuA`</summary>

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
  "parentUuid": "302fcae9-6de0-48a6-8809-5df6a6097239",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nbNqLB44XFtZw6qnk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "032e9f01-742e-427a-a17e-1a665192b9de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JvwvsFA2d7rtj3GJvxnZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4560,
      "cache_read_input_tokens": 34510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4560,
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

_source line 31 · 2026-05-21T17:48:41.120Z_

<details><summary>↩ Tool result · `toolu_01PaAfAR8N8HnwWHY9TZEjuA`</summary>

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
  "parentUuid": "032e9f01-742e-427a-a17e-1a665192b9de",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "264799d7-52f4-4d60-99fd-099aaacfbc3b",
  "sourceToolAssistantUUID": "032e9f01-742e-427a-a17e-1a665192b9de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T17:48:43.418Z_

Now I have a thorough understanding of the paper. Let me count the references and check a few more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264799d7-52f4-4d60-99fd-099aaacfbc3b",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nzn14dTWmRSbXCqqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7bc2217-16e9-4c5c-aaa5-58e60c1065d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXBpyUtwcEAPuwerqeb2Kz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3739,
      "cache_read_input_tokens": 39070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3739,
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

_source line 33 · 2026-05-21T17:48:45.383Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V1pynPtpFKpLDubHLGq5m6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -c '@' references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7bc2217-16e9-4c5c-aaa5-58e60c1065d0",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8nzn14dTWmRSbXCqqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2faee025-7c0d-4550-b486-6589af051408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXBpyUtwcEAPuwerqeb2Kz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3739,
      "cache_read_input_tokens": 39070,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 39070,
          "cache_creation_input_tokens": 3739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3739,
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

_source line 34 · 2026-05-21T17:48:45.453Z_

<details><summary>↩ Tool result · `toolu_01V1pynPtpFKpLDubHLGq5m6`</summary>

```text
51
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2faee025-7c0d-4550-b486-6589af051408",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "c2cf4c44-89c1-4fb4-a796-36d0739590bc",
  "sourceToolAssistantUUID": "2faee025-7c0d-4550-b486-6589af051408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T17:48:47.830Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0195f2kc1NgXJWEXQob2enPQ`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2cf4c44-89c1-4fb4-a796-36d0739590bc",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8oK5LSCE9dpSg2zFvB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6edc905f-3a28-47b0-8c94-16101899be4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXe1BZrrWRo2Ufh4Y115tt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 42809,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 42809,
          "cache_creation_input_tokens": 153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 153,
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

_source line 36 · 2026-05-21T17:48:47.852Z_

<details><summary>↩ Tool result · `toolu_0195f2kc1NgXJWEXQob2enPQ`</summary>

```text
paper/sections/related_work.tex:5:[Omitted long matching line]
paper/sections/related_work.tex:8:[Omitted long matching line]
paper/sections/related_work.tex:11:[Omitted long matching line]
paper/sections/related_work.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:4:We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
paper/sections/experiments.tex:9:[Omitted long matching line]
paper/sections/experiments.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:18:[Omitted long matching line]
paper/sections/experiments.tex:42:[Omitted long matching line]
paper/sections/experiments.tex:87:[Omitted long matching line]
paper/sections/method.tex:9:[Omitted long matching line]
paper/sections/method.tex:16:The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
paper/sections/introduction.tex:4:[Omitted long matching line]
paper/sections/introduction.tex:6:[Omitted long matching line]
paper/sections/introduction.tex:15:[Omitted long matching line]
paper/sections/introduction.tex:24:\item \textbf{Ground truth meta-critique}: Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap (\Cref{sec:groundtruth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6edc905f-3a28-47b0-8c94-16101899be4c",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "268e6328-886e-4b64-a957-774a29d9b513",
  "sourceToolAssistantUUID": "6edc905f-3a28-47b0-8c94-16101899be4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T17:48:51.462Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01E6qUpd1pdBjkzH9rrgEUGg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -oP '\\\\cite[pt]?\\{[^}]+\\}' sections/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//' | sort -u | wc -l",
  "description": "Count unique citation keys used in the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268e6328-886e-4b64-a957-774a29d9b513",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8oVUubnNemWr13VmML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8999be46-066d-4fe3-b05e-ea290d79b62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkf8LJXCgdjjCCVvzv2VqL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 42962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 792,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 38 · 2026-05-21T17:48:51.536Z_

<details><summary>↩ Tool result · `toolu_01E6qUpd1pdBjkzH9rrgEUGg`</summary>

```text
50
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8999be46-066d-4fe3-b05e-ea290d79b62c",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "82e7cb52-6cdc-49ba-98c6-21d81b507e3b",
  "sourceToolAssistantUUID": "8999be46-066d-4fe3-b05e-ea290d79b62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T17:48:54.194Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JDTvzi7byithb9XUSgCeqd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -oP '\\\\cite[pt]?\\{[^}]+\\}' sections/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//' | sort -u",
  "description": "List all unique citation keys used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82e7cb52-6cdc-49ba-98c6-21d81b507e3b",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8omAirPGLwzod9oUZh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df3a670-5d49-49cf-93e9-8579e442bcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUNGbGsQts2Yrwhtmzr13N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 195,
      "cache_read_input_tokens": 43754,
      "output_tokens": 175,
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
          "output_tokens": 175,
          "cache_read_input_tokens": 43754,
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

_source line 40 · 2026-05-21T17:48:54.294Z_

<details><summary>↩ Tool result · `toolu_01JDTvzi7byithb9XUSgCeqd`</summary>

```text
balloccu2024leak
belzak2020smallsample
burnell2023rethink
carlini2022quantifying
chang2024survey
chiang2024chatbot
clark2018arc
clauser1998dif
dekoninck2024constat
donoghue1993mh
golchin2024timetravel
habba2026growingpains
hardy2026scalability
hendrycks2021mmlu
holland1988mh
kiela2021dynabench
kipnis2024metabench
lalor2019irt
li2024contamination
li2024latesteval
li2025atlas
liang2026dvd
lin2022truthfulqa
lord1980irt
luo2025medirt
maeda2025difllm
maiapolo2024tinybenchmarks
meredith1993invariance
muthen1985mimic
nandakumar1993dif
qian2026benchmark2
raju1988area
rodriguez2021evaluation
sakaguchi2021winogrande
shealy1993sibtest
shi2024mink
swaminathan1990logistic
tao2026selfcritique
teresi2007dif
tirumala2022memorization
vandenberg2000invariance
vania2021irt
wang2026fragility
white2025livebench
woods2009mimic
zellers2019hellaswag
zhang2024minkpp
zhou2026psnirt
zhu2026bhi
zumbo1999handbook
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9df3a670-5d49-49cf-93e9-8579e442bcf6",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "80d4c1fa-1c90-4050-a311-cba98843d2e1",
  "sourceToolAssistantUUID": "9df3a670-5d49-49cf-93e9-8579e442bcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T17:48:56.989Z_

The paper actually cites 50 unique references, not 12. The summary I was given was inaccurate on that count. Let me also check the paper's page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80d4c1fa-1c90-4050-a311-cba98843d2e1",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8oxtRjb8tfkGyL4p4c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d74a088-414d-4d5f-995a-14c67ef7d770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193GfcNcNT4Mv3bgwYZgw6n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 43949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 551,
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

_source line 42 · 2026-05-21T17:48:57.802Z_

<details open><summary>🔧 Tool call — Read · `toolu_017hgPJ74D4hiMYUuHMjNHdL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.log",
  "limit": 50,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d74a088-414d-4d5f-995a-14c67ef7d770",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8oxtRjb8tfkGyL4p4c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "460f8e7f-1dd4-4a11-95c0-422d7497d7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193GfcNcNT4Mv3bgwYZgw6n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 43949,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 551
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 43949,
          "cache_creation_input_tokens": 551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 551,
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

_source line 43 · 2026-05-21T17:48:57.808Z_

<details><summary>↩ Tool result · `toolu_017hgPJ74D4hiMYUuHMjNHdL`</summary>

```text
0	This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  21 MAY 2026 17:20
1	entering extended mode
2	 restricted \write18 enabled.
3	 %&-line parsing enabled.
4	**main.tex
5	(./main.tex
6	LaTeX2e <2025-11-01>
7	L3 programming layer <2026-01-19>
8	(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
9	Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
10	(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo
11	File: size11.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
12	)
13	\c@part=\count275
14	\c@section=\count276
15	\c@subsection=\count277
16	\c@subsubsection=\count278
17	\c@paragraph=\count279
18	\c@subparagraph=\count280
19	\c@figure=\count281
20	\c@table=\count282
21	\abovecaptionskip=\skip49
22	\belowcaptionskip=\skip50
23	\bibindent=\dimen148
24	) (./acl.sty
25	Conference Style for ACL
26	(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
27	Package: xcolor 2024/09/29 v3.02 LaTeX color extensions (UK)
28	
29	(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg
30	File: color.cfg 2016/01/02 v1.6 sample color configuration
31	)
32	Package xcolor Info: Driver file: pdftex.def on input line 274.
33	
34	(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def
35	File: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex
36	)
37	(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx)
38	Package xcolor Info: Model `cmy' substituted by `cmy0' on input line 1349.
39	Package xcolor Info: Model `hsb' substituted by `rgb' on input line 1353.
40	Package xcolor Info: Model `RGB' extended on input line 1365.
41	Package xcolor Info: Model `HTML' substituted by `rgb' on input line 1367.
42	Package xcolor Info: Model `Hsb' substituted by `hsb' on input line 1368.
43	Package xcolor Info: Model `tHsb' substituted by `hsb' on input line 1369.
44	Package xcolor Info: Model `HSB' substituted by `hsb' on input line 1370.
45	Package xcolor Info: Model `Gray' substituted by `gray' on input line 1371.
46	Package xcolor Info: Model `wave' substituted by `hsb' on input line 1372.
47	)
48	(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
49	Package: lineno 2025/05/13 line numbers on paragraphs v5.5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "460f8e7f-1dd4-4a11-95c0-422d7497d7b4",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "c2a37b2a-4fab-4249-b8ea-b7f1987ae6da",
  "sourceToolAssistantUUID": "460f8e7f-1dd4-4a11-95c0-422d7497d7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T17:49:02.693Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TWjeNYsRar3Z4VYVjGGfZZ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -i \"output written\" main.log",
  "description": "Check PDF page count from log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a37b2a-4fab-4249-b8ea-b7f1987ae6da",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8pEBBTeYgpcvKzZPKv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dab5451-685e-454f-9aeb-ac39f9bb5c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THPupuodJCdZNgQGk8cm1v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 44500,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 44500,
          "cache_creation_input_tokens": 1120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1120,
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

_source line 45 · 2026-05-21T17:49:02.749Z_

<details><summary>↩ Tool result · `toolu_01TWjeNYsRar3Z4VYVjGGfZZ`</summary>

```text
Output written on main.pdf (13 pages, 573978 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dab5451-685e-454f-9aeb-ac39f9bb5c42",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "a652e8d4-1cc5-4e9b-a3a6-7f06f8ccdf49",
  "sourceToolAssistantUUID": "7dab5451-685e-454f-9aeb-ac39f9bb5c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-21T17:49:08.361Z_

13 pages total (8 main + appendix + references). Now let me look at the math_commands.tex and check the paper's figures for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a652e8d4-1cc5-4e9b-a3a6-7f06f8ccdf49",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8pk1YgZELoarxfrz8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70c1cbb0-7bfd-4686-8cb5-0931a309470c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzbVj2enhXS3VVETz84amZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 45620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 148,
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

_source line 47 · 2026-05-21T17:49:08.922Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dkc5tW8dvvKyAwv2u2xdKs`</summary>

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
  "parentUuid": "70c1cbb0-7bfd-4686-8cb5-0931a309470c",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8pk1YgZELoarxfrz8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eba3ca7-694e-4b34-a394-e7fcfd7cf17d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzbVj2enhXS3VVETz84amZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 45620,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 45620,
          "cache_creation_input_tokens": 148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 148,
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

_source line 48 · 2026-05-21T17:49:08.946Z_

<details><summary>↩ Tool result · `toolu_01Dkc5tW8dvvKyAwv2u2xdKs`</summary>

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
  "parentUuid": "0eba3ca7-694e-4b34-a394-e7fcfd7cf17d",
  "isSidechain": true,
  "promptId": "d0ba33c0-595c-4517-b734-342c6ac271e1",
  "agentId": "a16ad29a4bc1edec4",
  "type": "user",
  "uuid": "fc7e2ddf-0066-4fd0-bcbc-f859d7a4bff3",
  "sourceToolAssistantUUID": "0eba3ca7-694e-4b34-a394-e7fcfd7cf17d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T17:51:16.628Z_

Now I have a comprehensive view of the paper. Let me write the review.

---

## Review: "Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"

**Reviewer R2 — Focus: Novelty, Framing, and Related Work**

---

### 1. Summary

This paper applies the Mantel-Haenszel Differential Item Functioning (MH-DIF) procedure with ETS severity classification to the METABENCH response matrix (5,227 models across 12,508 MMLU items and 5 additional benchmarks) to quantify temporal measurement drift between 2023 and 2024 model cohorts. The key finding is that 17.9-31.3% of items across six benchmarks exhibit large DIF (ETS Category C), far exceeding random baselines, yet this drift does not meaningfully alter aggregate model rankings. A semi-synthetic injection framework with cross-subject matching validates that MH-DIF can detect differential item behavior while maintaining zero false-positive inflation, and a ground-truth meta-critique demonstrates that web-overlap contamination labels are near-independent of DIF flags, exposing a category error in prevailing validation methodology.

---

### 2. Novelty Assessment

**Type of contribution.** This is primarily an *empirical* contribution with a *methodological* secondary contribution (the semi-synthetic validation framework and the cross-subject matching protocol). The MH-DIF procedure itself is not novel -- it dates to Holland & Thayer (1988) and is the standard workhorse in educational testing. The paper explicitly acknowledges this: "We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals."

**Novelty of the application.** Applying MH-DIF to LLM benchmarks at scale (5,227 "examinees") is genuinely novel and timely. Prior work applying IRT to LLMs (Lalor et al. 2019, Vania et al. 2021, Rodriguez et al. 2021) focused on item difficulty/discrimination estimation, not DIF across temporal cohorts. The closest concurrent work (Habba et al. 2026 "Growing Pains") addresses score comparability via fixed-parameter calibration but does not perform DIF analysis. The paper correctly identifies a complementarity: Growing Pains assumes anchor item stability, while DIF analysis tests that assumption.

**Advancement beyond existing work.**
- vs. contamination detectors (Li et al., Shi et al., Dekoninck et al.): The paper's most novel conceptual contribution is the *global vs. differential* distinction and the empirical demonstration that web-overlap labels are near-independent of DIF flags. This is a genuine insight that reframes how the field should think about validation of contamination detectors.
- vs. benchmark quality assessment (Zhu et al. BHI, Qian et al. Benchmark^2): These assess static quality; the temporal dimension is new.
- vs. Hardy et al. (2026): Scalability coefficients focus on item quality detection, not temporal invariance testing.

**Concern.** The novelty is concentrated in the *application context* and the *meta-critique of ground truth*. The semi-synthetic framework, while well-executed, is relatively straightforward (flip incorrect-to-correct at controlled rates, measure TPR/FPR). The cross-subject matching idea has psychometric precedent (Nandakumar 1993, Donoghue 1993), which the authors acknowledge. The question is whether application novelty alone is sufficient for a top venue, given that the method is off-the-shelf and the primary finding ("31% of items show DIF") has limited actionability (see Section 4).

**Verdict.** Moderate novelty. The ground-truth meta-critique is the most conceptually novel element. The empirical scale is impressive. The methodological novelty is thin.

---

### 3. Framing Critique

**"Large-Scale Item-Level Stability Analysis" vs. the actual title.** The submitted title ("Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models") is better than the briefing title. "Psychometric audit" is an appropriate framing for what the paper does. However, "5,227 Models" in the title somewhat overpromises -- the models are drawn from the Open LLM Leaderboard and are overwhelmingly decoder-only (99.98%). The "5,227" figure includes many fine-tuned variants and merges of the same base models, which the paper addresses through de-duplication controls but which still inflates the impression of breadth.

**Reframing from DIF to "nonparametric group-comparison test."** The paper does *not* actually do this reframing -- it uses the DIF terminology faithfully throughout. The abstract and introduction correctly ground the work in psychometrics and explain MH-DIF in its native framework. This is a strength. The paper could have been tempted to rebrand the method for an NLP audience, and wisely did not.

**"Characterize, monitor, don't remediate."** This is the most significant framing concern. The paper's final recommendation is a monitoring protocol with graduated thresholds (C% < 15% = monitor, 15-25% = flag, > 25% = act). But the "act" action is vague ("rotate or retire flagged items"), and the paper itself shows why remediation is difficult: DIF-flagged items concentrate discriminative signal, and removal degrades reliability. The paper is essentially saying: "We found a problem, it's real, we can measure it, but we can't fix it, and actually it might not need fixing because rankings are preserved." While this is honest, it leaves the reader wondering what to *do* with this information. The monitoring protocol in Section 5.4 is the most actionable element, but it is brief (7 lines) and untested.

The conclusion "LLM benchmarks need psychometric monitoring alongside score reporting" is uncontroversial to the point of being obvious -- who would disagree? The contribution would be stronger if it either (a) demonstrated a case where DIF-based monitoring would have caught a real problem before it manifested in rankings, or (b) provided a concrete, tested monitoring tool or dashboard.

**Is the framing earned by the evidence?** The paper does not use the phrase "construct validity crisis" in the main text (it appears only in the briefing). The actual framing is more measured: "measurement drift across model generations." This is appropriate and well-supported.

---

### 4. Related Work Gaps

The related work section is substantially more comprehensive than the 12-reference count initially indicated. The paper actually cites **50 unique references**, covering contamination detection, IRT in NLP, DIF methodology, measurement invariance, benchmark quality, and dynamic benchmarks. The related work section is well-organized into four clear paragraphs. Nevertheless, several gaps remain:

**Missing or underrepresented areas:**

1. **HELM / Holistic Evaluation**: Liang et al. (2022) "Holistic Evaluation of Language Models" is a foundational evaluation framework that systematically evaluates models across multiple scenarios. Its approach to standardized evaluation is relevant to the measurement comparability question. Similarly, the Open LLM Leaderboard itself (from which METABENCH draws data) deserves a citation -- the paper uses it as a data source but does not cite the infrastructure work behind it.

2. **Multi-group DIF and intersectionality**: The paper uses only pairwise (2023 vs. 2024) comparisons. The DIF literature has extensive work on multi-group comparisons (e.g., Penfield 2001, Magis et al. 2011) that could address finer-grained temporal cohorts or simultaneous family comparisons. This is particularly relevant because the paper notes that "finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns" (Limitations).

3. **Effect size interpretation for LLMs**: The ETS classification thresholds (A/B/C) were developed for human test-takers where DIF has equity implications. The paper applies these thresholds to LLMs without discussing whether the same effect-size boundaries are meaningful in this context. A discussion of whether $|\Delta_{MH}| \geq 1.5$ represents the same "practical significance" when examinees are models rather than humans would strengthen the paper. Some work on adapting psychometric standards to non-human test-takers (if it exists) should be cited; if it doesn't, this gap should be acknowledged.

4. **Measurement invariance testing beyond DIF**: The paper cites Meredith (1993) and Vandenberg & Lance (2000) but does not engage with the multi-group CFA / measurement invariance testing framework (configural, metric, scalar, strict invariance). This framework provides a more structured hierarchy of invariance levels than DIF alone. Given that the paper reports IRT model misspecification (CFI < 0.72, RMSEA > 0.08 in the briefing -- though I note this result does not appear in the main text, only in supplementary materials or was cut), the CFA-based approach might be informative.

5. **Benchmark saturation / ceiling effects**: Kieval et al. (2024) and others have documented MMLU saturation for frontier models. This is directly relevant because saturation could interact with DIF: when many models score near ceiling on easy items, the MH contingency tables become sparse in certain cells, potentially inflating or deflating $\Delta_{MH}$. The paper does not discuss this.

6. **Robustness of MH under violation of assumptions**: The paper notes LLM-specific challenges (local dependence, non-normal ability distribution) but the related work section could benefit from citing work on MH robustness under these violations beyond Belzak (2020), e.g., Narayanan & Swaminathan (1996) on MH under model violations.

---

### 5. Contribution Clarity

**Are contributions clearly stated?** Yes. The three numbered contributions in the introduction are well-defined and supported by the experimental sections. The distinction between semi-synthetic validation, ground-truth meta-critique, and temporal measurement drift at scale is clear.

**Does breadth dilute the message?** This is a significant concern. The paper packs an enormous amount of empirical content into 8 pages. The experiments section covers: power analysis, temporal comparability (with 4 control conditions), ground-truth mismatch, structural analysis (6 alternative explanations), semi-synthetic validation, downstream impact analysis, and cross-benchmark validation across 6 benchmarks. This breadth is simultaneously a strength (thoroughness) and a weakness (each analysis gets insufficient space for the reader to absorb its implications).

The paper reads more like a technical report than a narrative-driven conference paper. Each subsection introduces a result, reports a number, and moves on. For example, the GSM1K correlation analysis gets 4 lines despite being one of the more interesting results (it provides the only external anchor connecting DIF to an independent contamination measure). The Simpson's paradox result is mentioned in passing in one sentence but is actually a key finding that deserves more explanation.

**What should the reader take away?** The takeaway is clear: ~30% of MMLU items function differently across model generations, but this doesn't break rankings. The ground-truth meta-critique (web-overlap labels are wrong for evaluating differential methods) is arguably the most impactful finding for the community, but it is buried as "Contribution 2" and gets relatively brief treatment.

**Recommendation.** The paper would benefit from a stronger narrative arc. Currently it reads as "we ran DIF, here's what we found, and also here are 10 other things we checked." A more compelling structure might foreground the ground-truth meta-critique (since it has immediate methodological implications for the contamination detection community) and use the temporal DIF analysis as supporting evidence.

---

### 6. Strengths

- **Scale and thoroughness.** 5,227 models across 6 benchmarks with 27,125 items is genuinely large-scale. The battery of controls (random split, ability quintile, within-family, matched-ability, theta-conditioning, de-duplication) is exemplary and exceeds what most papers in this area provide.

- **Ground-truth meta-critique.** The demonstration that web-overlap labels are near-independent of DIF flags (enrichment = 0.964, phi = 0.012) is a conceptually important finding that should change how the community validates contamination detectors. This alone is a meaningful contribution.

- **Semi-synthetic validation with zero FPR inflation.** The cross-subject matching protocol is clean, principled, and well-validated. The proposition (Proposition 1) and its empirical verification across all five MMLU domains are convincing.

- **Honest reporting of negative/null results.** The paper does not oversell. It reports that DIF does not affect rankings (rho = 0.997), that the matching boundary degrades gracefully, and that DIF cannot determine causation. This intellectual honesty is refreshing.

- **Appropriate scope of claims.** The paper carefully distinguishes "that" from "why" -- DIF detects that items function differently, not why. This restraint is appropriate.

- **Comprehensive related work.** 50 references spanning psychometrics, NLP, and evaluation methodology, with proper positioning relative to concurrent work (Growing Pains, BHI, Benchmark^2, Hardy et al.).

- **Cross-benchmark replication.** The finding generalizes across all 6 METABENCH benchmarks, with the knowledge/procedural dichotomy providing interpretive structure.

---

### 7. Weaknesses

- **Limited actionability (moderate severity).** The paper's conclusion is essentially "monitor, don't fix." The monitoring protocol (Section 5.4) is a 7-line sketch with arbitrary thresholds (15%, 25%) that are not derived from any principled analysis. What happens when C% > 25%? "Rotate or retire flagged items" -- but the paper itself shows this degrades the benchmark. This creates a paradox at the heart of the paper: the finding is real but the recommended action is vague and possibly counterproductive.

- **DIF detects "that" but not "why" -- so what? (moderate severity).** The paper acknowledges this limitation but doesn't sufficiently grapple with its implications. If we cannot distinguish contamination from genuine capability improvement from training methodology shifts, the practical utility of DIF monitoring is unclear. A practitioner reading this paper cannot determine whether 31% drift is alarming or expected and benign. The paper needs to better articulate the decision theory: what would a benchmark maintainer do differently based on DIF audit results?

- **ETS threshold transferability (moderate severity).** The A/B/C classification was designed for fairness in human testing where DIF has equity implications. When applied to LLMs, the same effect-size thresholds may not be meaningful. A 1.5 log-odds-ratio shift for a model might reflect a qualitative difference in training, or it might be a routine consequence of capability improvement. The paper does not discuss whether the ETS thresholds should be recalibrated for this domain.

- **Temporal cohort definition is coarse (minor-moderate severity).** Calendar year (2023 vs. 2024) is a blunt instrument. Models released in late 2023 vs. early 2024 may share more in common than models released in early 2023 vs. late 2024. The paper reports that even a 6-month window shows substantial DIF (34.35%), but this actually makes the finding harder to interpret: is 6-month drift alarming, or is it simply reflecting a rapid-improvement period?

- **MMLU dominance in the narrative (minor-moderate severity).** MMLU is the primary analysis (12,508 items), while other benchmarks get one table (Table 4) and a few sentences. The cross-benchmark replication is important but thin. HellaSwag (10,042 items) gets no analysis beyond the C% number. The paper's title says "5,227 models" but the depth of analysis is heavily MMLU-centric.

- **Downstream impact analysis is weak (minor severity).** The rho = 0.997 finding actually undermines urgency: if DIF doesn't affect rankings, why should practitioners care? The model-family rank shifts (Llama-3 +53, Mistral -35) are interesting but not clearly actionable. The paper needs to make a stronger case for why measurement drift matters when it doesn't affect the thing people use benchmarks for (ranking models).

- **Writing density (minor severity).** The experiments section is extremely dense, with 7 subsections covering distinct analyses. Some results are stated without sufficient context for a reader unfamiliar with DIF methodology. The Simpson's paradox finding, for instance, is compressed into a single sentence despite being one of the more nuanced results.

---

### 8. Questions for Authors

1. **On ETS threshold calibration**: Have you considered what the "right" DIF threshold would be for LLM benchmarks? The ETS A/B/C system was designed for fairness in high-stakes human testing. What is the analog of "fairness" when examinees are models? Would a different threshold change the 31% headline number substantially? (The threshold sensitivity analysis partially addresses this but doesn't engage with the conceptual question.)

2. **On the monitoring protocol**: Your Section 5.4 proposes C% thresholds of 15% and 25%. How were these chosen? Are they based on operational experience, theoretical considerations, or arbitrary? What would "rotate or retire flagged items" look like in practice, given your finding that DIF-flagged items concentrate discriminative signal?

3. **On the ground-truth meta-critique**: You show that web-overlap labels are near-independent of DIF flags. But what *would* constitute appropriate ground truth for DIF validation? Is the semi-synthetic framework the only option, or could you propose an external validation using models with known training data composition?

4. **On the knowledge/procedural dichotomy**: You find that knowledge/reasoning benchmarks show higher DIF rates than procedural ones. Is this consistent with the hypothesis that knowledge-intensive items are more sensitive to training data composition? Could you test this more directly by correlating item-level DIF with features of the items (e.g., required factual knowledge, reasoning depth)?

5. **On the rho = 0.997 finding**: If DIF does not affect rankings, what is the practical harm of measurement drift? Can you articulate a concrete scenario where DIF-based monitoring would have prevented a real-world evaluation failure?

6. **On within-family DIF**: The Llama-2 vs. Llama-3 comparison yields 61.3% C% (ability-confounded) and 28.3% (ability-matched). Given that this is a known generational improvement, isn't ~28% DIF a natural consequence of capability improvement rather than a measurement problem? How do you distinguish "measurement drift" from "the measure correctly detecting that the thing being measured changed"?

---

### 9. Preliminary Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | 4.0 | Methodology is rigorous with extensive controls. The MH-DIF application is technically correct. Minor concerns about ETS threshold transferability and the coarse temporal cohort definition, but these do not undermine the core findings. The semi-synthetic validation is convincing. |
| **Excitement** | 3.0 | The ground-truth meta-critique is a genuine insight. The scale is impressive. However, the contribution is primarily empirical characterization with limited actionability. The method is off-the-shelf. The main finding (31% drift doesn't affect rankings) somewhat deflates the urgency of the paper's own narrative. The "monitor, don't fix" conclusion is unsatisfying for an 8-page paper. |
| **Reproducibility** | 4.5 | Data is publicly available (METABENCH), method is fully specified (MH-DIF with ETS classification), code is promised at an anonymous repository. The 50 references and detailed appendix support reproducibility. The semi-synthetic framework is well-documented. |
| **Overall** | 3.0 | A solid empirical contribution that belongs in Findings. The ground-truth meta-critique elevates it above a routine application paper. The thoroughness is commendable. However, the limited actionability, off-the-shelf methodology, and the tension between "31% drift exists" and "it doesn't matter for rankings" prevent it from reaching the Main conference threshold. The paper would benefit from either (a) a more concrete monitoring tool with demonstrated utility, or (b) a sharper narrative focus on the ground-truth meta-critique as the primary contribution, with temporal DIF as supporting evidence. |

**Confidence:** 4/5 (I have strong familiarity with both DIF methodology and LLM evaluation; I am less certain about whether the NLP community would find the empirical characterization sufficiently novel on its own.)

**Best paper consideration:** No.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7e2ddf-0066-4fd0-bcbc-f859d7a4bff3",
  "isSidechain": true,
  "agentId": "a16ad29a4bc1edec4",
  "requestId": "req_011CbG8q3fwEZ97G3But1hVa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9053a4b-285e-47c3-8675-fc5bbbb235da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "443e7d3b-018c-4cf7-ba4a-be177b1d8eb5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6PStetjQhBfw9ggkixzjb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 45768,
      "output_tokens": 4918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4918,
          "cache_read_input_tokens": 45768,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 264,
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
