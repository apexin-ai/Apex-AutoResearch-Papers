# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/, find th

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a681a1f5c899bf5fa.jsonl`
- **Structured JSON:** [`aa035b38c2058877c2a4.json`](../../sessions/aa/aa035b38c2058877c2a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-20T21:46:18.101Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/, find the file that contains "Table 1" or the main results table with SC accuracy values for Qwen2.5-14B on ProofWriter. Check .tex and .md files. Report what SC accuracy value is listed for Qwen2.5-14B ProofWriter in the table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1d6676c1-24f2-4198-8390-81a9f95ee32d",
  "agentId": "a681a1f5c899bf5fa",
  "type": "user",
  "uuid": "282a8b87-f5ba-4e06-b3eb-d06d416b7c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T21:46:23.463Z_

I'll help you find the SC accuracy value for Qwen2.5-14B on ProofWriter in Table 1. Let me search through the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282a8b87-f5ba-4e06-b3eb-d06d416b7c78",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ729PcxDTvY7V4rEVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "264f2d79-0762-488f-8764-c45d6d3abc89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZ4y87zrdGuPj1fJX2guyV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35722,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35722
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35722,
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

### Tool call

_source line 3 · 2026-05-20T21:46:23.489Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tf5CuxDHGsbBWcCwvLyDRQ`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/**/*.{tex,md}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264f2d79-0762-488f-8764-c45d6d3abc89",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ729PcxDTvY7V4rEVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d555350c-fdcc-4cea-a338-89404ab33399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZ4y87zrdGuPj1fJX2guyV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35722,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35722
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35722,
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

_source line 4 · 2026-05-20T21:46:23.509Z_

<details><summary>↩ Tool result · `toolu_01Tf5CuxDHGsbBWcCwvLyDRQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/v8_outline_drafts.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/v9_aggregation_ceiling.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d555350c-fdcc-4cea-a338-89404ab33399",
  "isSidechain": true,
  "promptId": "1d6676c1-24f2-4198-8390-81a9f95ee32d",
  "agentId": "a681a1f5c899bf5fa",
  "type": "user",
  "uuid": "1bdf4f50-f625-494b-b0b1-918af788cf5d",
  "sourceToolAssistantUUID": "d555350c-fdcc-4cea-a338-89404ab33399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T21:46:25.091Z_

Now let me search for "Table 1" and "Qwen2.5" references in these files, starting with the main paper and experiments sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bdf4f50-f625-494b-b0b1-918af788cf5d",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ7RFCZkiLA67FZBj4n",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a1e6b15-c6be-4247-85a6-fcdd9c06f2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01595ncxWWvU5FUtowdHshBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 35722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 6 · 2026-05-20T21:46:25.884Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PRVMMjo3Ya5zW5Pd28guaN`</summary>

```json
{
  "pattern": "Table 1|Qwen2.5|ProofWriter",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a1e6b15-c6be-4247-85a6-fcdd9c06f2d0",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ7RFCZkiLA67FZBj4n",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "084fd1c1-913a-4e6c-a0c1-be790a385cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01595ncxWWvU5FUtowdHshBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 35722,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 171,
          "cache_read_input_tokens": 35722,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1603,
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

_source line 7 · 2026-05-20T21:46:25.913Z_

<details><summary>↩ Tool result · `toolu_01PRVMMjo3Ya5zW5Pd28guaN`</summary>

```text
Found 16 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/gen_capability_gap_scatter.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/v8_outline_drafts.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "084fd1c1-913a-4e6c-a0c1-be790a385cba",
  "isSidechain": true,
  "promptId": "1d6676c1-24f2-4198-8390-81a9f95ee32d",
  "agentId": "a681a1f5c899bf5fa",
  "type": "user",
  "uuid": "6fcd15d6-0b9e-432b-b4a7-c43717187779",
  "sourceToolAssistantUUID": "084fd1c1-913a-4e6c-a0c1-be790a385cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T21:46:27.046Z_

Let me read the experiments.tex file which likely contains Table 1:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fcd15d6-0b9e-432b-b4a7-c43717187779",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ7bnhpKdWaNQtDcDJ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60428cea-e15b-41e0-89d0-42b0857d6ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UjQEccXzuMNe7D7kZQqCi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 37325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 823,
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

_source line 9 · 2026-05-20T21:46:27.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FdtAte19Tr6de8rTmHMTb3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60428cea-e15b-41e0-89d0-42b0857d6ea8",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ7bnhpKdWaNQtDcDJ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "30dc4361-0873-4261-bd38-076045cbf040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UjQEccXzuMNe7D7kZQqCi6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 37325,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 105,
          "cache_read_input_tokens": 37325,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 823,
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

_source line 10 · 2026-05-20T21:46:27.229Z_

<details><summary>↩ Tool result · `toolu_01FdtAte19Tr6de8rTmHMTb3`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 condition-evaluations across ${\sim}$1,250 unique instances. Beyond accuracy comparisons, we conduct diagnostic analyses of symbolic confirmation bias and process-level trace independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\text{ext}}{=}0.3$. Z3 timeout: 10s. $\alpha{=}0.5$. Statistical significance via McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs from 10,000 resamples for $n \geq 200$.
14	
15	\paragraph{Computational cost.} On Mistral-7B FOLIO ($K{=}12$), SICA takes $4.5{\times}$ SC wall-clock time; constraint extraction ($K$ additional LLM calls) accounts for 76\% of overhead, Z3 solving is negligible (${<}0.1\%$).
16	
17	
18	\subsection{Main Results}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. We identify three empirical regimes (thresholds observation-driven, not theoretically derived). SICA effectiveness depends sharply on this accuracy regime.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. Results hold across the full capability range: from Mistral-7B (54.41\% SC) to Qwen3-14B thinking mode (86.27\% SC), SICA delivers no significant gain. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold logical examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}. $^{4s}$\,4-seed replication (confirmatory); unmarked single-seed conditions are exploratory.}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llrrrrl@{}}
29	\toprule
30	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
31	\midrule
32	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
33	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
34	\midrule
35	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--55\%, Mistral-7B only)}} \\
36	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
37	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
38	Mistral-7B$^{4s}$ & FOLIO & 204 & 55.88 & 59.31 & $+$3.43 & 0.092 \\
39	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
40	Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\
41	\midrule
42	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
43	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
44	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
45	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
46	Qwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\mathbf{-2.50}$ & 0.011{*} \\
47	Qwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\
48	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
49	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
50	Qwen3-14B & FOLIO & 204 & 84.80 & 84.31 & $-$0.49 & 1.000 \\
51	Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\
52	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
53	\midrule
54	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
55	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
56	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
57	\midrule
58	\multicolumn{7}{l}{\textit{Oracle upper bound (gold logical annotations + Z3)}} \\
59	Mistral-7B & FOLIO & 204 & 55.88 & \textbf{85.78} & $\mathbf{+29.90}$ & $1.0{\times}10^{-13}${***} \\
60	Qwen2.5-14B & FOLIO & 204 & 75.49 & \textbf{89.71} & $\mathbf{+14.22}$ & $2.0{\times}10^{-7}${***} \\
61	Qwen2.5-14B & ProofWriter & 600 & 75.17 & \textbf{86.67} & $\mathbf{+11.50}$ & $9.21{\times}10^{-15}${***} \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	None of fifteen non-degenerate conditions shows a significant positive effect. Two show significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, $p = 0.011$). The intermediate-SC region (50--55\%) contains the only positive trends, none reaching $p < 0.05$. TOST equivalence tests \citep{lakens2017equivalence} ($\pm 2$\,pp) establish equivalence for 4 conditions; 5 show genuine differences (4 negative); 6 are underpowered (Appendix~\ref{app:tost}). We trace the failure to three mechanisms in \S\ref{sec:confirmation-bias}--\S\ref{sec:remediation}.
67	
68	
69	\subsection{Oracle Control}
70	\label{sec:oracle}
71	
72	Oracle variants replace self-extracted constraints with gold annotations: logical formulae from FOLIO ($n = 204$) and DSL from ProofWriter ($n = 600$). Oracle-SICA yields $+29.90$\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+14.22$\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \times 10^{-7}$), and $+11.50$\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\% (FOLIO) and 97.1\% (ProofWriter) of problems. The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted result ($+3.43$\,pp) captures only 11.5\% of its oracle ceiling, with ${\sim}$88\% lost to extraction quality.
73	
74	
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30dc4361-0873-4261-bd38-076045cbf040",
  "isSidechain": true,
  "promptId": "1d6676c1-24f2-4198-8390-81a9f95ee32d",
  "agentId": "a681a1f5c899bf5fa",
  "type": "user",
  "uuid": "c04cdc85-3274-4408-9daf-53ef6b0f6147",
  "sourceToolAssistantUUID": "30dc4361-0873-4261-bd38-076045cbf040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T21:46:30.085Z_

Perfect! I found the information. Looking at Table 1 (the main results table), I can see the SC accuracy value for Qwen2.5-14B on ProofWriter (PW-D5):

**SC accuracy for Qwen2.5-14B on ProofWriter: 75.17%**

This is shown on line 46 of the experiments.tex file:
```
Qwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\mathbf{-2.50}$ & 0.011{*} \\
```

The table shows that:
- Model: Qwen2.5-14B
- Domain: PW-D5 (ProofWriter depth-5)
- Sample size (n): 600
- SC accuracy: **75.17%**
- SICA accuracy: 72.67%
- Difference: -2.50 pp (with p=0.011, statistically significant)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c04cdc85-3274-4408-9daf-53ef6b0f6147",
  "isSidechain": true,
  "agentId": "a681a1f5c899bf5fa",
  "requestId": "req_011CbEZ7hCeAvDsULHcadrGn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ee7b55f-a34b-45a4-988d-2be011c69da2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KoDqE3gDVsbbAdcbP1MQxe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3029,
      "cache_read_input_tokens": 38148,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 243,
          "cache_read_input_tokens": 38148,
          "cache_creation_input_tokens": 3029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3029,
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
