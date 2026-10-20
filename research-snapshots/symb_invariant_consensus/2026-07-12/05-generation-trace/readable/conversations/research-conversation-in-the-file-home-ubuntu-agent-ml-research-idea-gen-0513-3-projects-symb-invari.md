# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5d56391d6cff8d65.jsonl`
- **Structured JSON:** [`7517565be55c87f9c122.json`](../../sessions/75/7517565be55c87f9c122.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-22T20:25:01.782Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex, find the Table 1 rows for Qwen3-14B. I need to see the exact values for:
1. Qwen3-14B × FOLIO row — what are the SC and SICA values?
2. Qwen3-14B × PW-D5 row — what are the SC and SICA values?

Also check if there's a Qwen2.5-14B × FOLIO row and what its SC/SICA values are.

Report exact line numbers and the raw LaTeX content for these rows.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f174627-1c82-4337-a249-ad0788c18219",
  "agentId": "a5d56391d6cff8d65",
  "type": "user",
  "uuid": "08ded761-3e9f-42d1-9f58-f34dd838b7bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "cec144ca-982b-493f-9bb4-f6fe13f44d38",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ticklish-frolicking-acorn"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T20:25:03.153Z_

I'll help you find the exact values in the experiments.tex file. Let me first read that file to locate Table 1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08ded761-3e9f-42d1-9f58-f34dd838b7bc",
  "isSidechain": true,
  "agentId": "a5d56391d6cff8d65",
  "requestId": "req_011CbJEXQ2zVW4h1uQ8pjajR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9729d7c-d00c-4aed-b99e-df017c431bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "cec144ca-982b-493f-9bb4-f6fe13f44d38",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ticklish-frolicking-acorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017JkX8sawAJXjQf1N6MBR2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21197,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21197,
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

_source line 3 · 2026-05-22T20:25:03.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YJFB4juYZHxE9ybbSGfWtk`</summary>

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
  "parentUuid": "f9729d7c-d00c-4aed-b99e-df017c431bb3",
  "isSidechain": true,
  "agentId": "a5d56391d6cff8d65",
  "requestId": "req_011CbJEXQ2zVW4h1uQ8pjajR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c16f3b6c-b714-4543-9066-5029347b948b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "cec144ca-982b-493f-9bb4-f6fe13f44d38",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ticklish-frolicking-acorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017JkX8sawAJXjQf1N6MBR2q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21197,
      "cache_read_input_tokens": 0,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21197,
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

_source line 4 · 2026-05-22T20:25:03.296Z_

<details><summary>↩ Tool result · `toolu_01YJFB4juYZHxE9ybbSGfWtk`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We additionally evaluate SCB universality via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\ref{tab:frontier-scb}), where Mistral-7B extracts constraints from the target model's traces since closed-source APIs do not expose internals suitable for self-extraction.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} (exploratory, $n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); $^{3s}$\,3-seed; $^{4s}$\,4-seed confirmatory (unmarked: single-seed exploratory). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME, Qwen2.5-14B GSM8K) yield $\Delta = 0$; oracle upper bounds are reported in Appendix~\ref{app:oracle}.}
25	\label{tab:main_results}
26	\begin{tabular}{@{}llrrrrl@{}}
27	\toprule
28	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
29	\midrule
30	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
31	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
32	\midrule
33	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
34	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
35	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
36	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
37	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
38	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
39	\midrule
40	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
41	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
42	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
43	\addlinespace
44	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
45	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
46	Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\
47	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
48	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
49	\addlinespace
50	Qwen3-14B & FOLIO & 204 & 84.80 & 84.31 & $-$0.49 & 1.000 \\
51	Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\
52	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
53	\bottomrule
54	\end{tabular}
55	\end{table*}
56	
57	\looseness=-1 No non-degenerate condition shows a significant SICA effect after FDR control (BH, $m{=}16$). Two show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); adjusted $p = 0.112$ for both. The intermediate-SC region (50--60\%) contains the only positive trends, none reaching $p < 0.05$. An aggregate sign test across self-extraction conditions yields 5 positive and 10 negative $\Delta$ values ($p = 0.30$, two-sided); including all conditions gives 8+/15$-$ ($p = 0.21$). Three-seed replication on Mistral-7B confirms seed-level noise: two of three seeds produce null or negative $\Delta$ (mean $+0.16 \pm 2.70$\,pp; Table~\ref{tab:multi-seed}). Four-seed replication on Qwen2.5-14B $\times$ FOLIO confirms the single-seed pattern: $\Delta \in [0.00, -2.01]$\,pp (mean $-1.24 \pm 0.86$; Table~\ref{tab:multi-seed}). TOST equivalence tests \citep{lakens2017equivalence} with margin $\pm 2$\,pp confirm 4 equivalent, 2 genuinely different (both negative), 10 underpowered. For the 10 underpowered conditions, our tests cannot rule out effects smaller than 1.86--4.84\,pp at 80\% power; the largest study ($n{=}804$) achieves MDE $= 1.86$\,pp (Appendix~\ref{app:power}). Absence of evidence is not evidence of absence for small effects. Margin sensitivity is robust: at $\pm 1$\,pp, 0/16 equivalent; at $\pm 3$\,pp, 10/16 equivalent; no margin yields a significant positive effect (Appendix Table~\ref{tab:tost-sensitivity}). We adopt $\pm 2$\,pp based on the lower bound of SC literature gains (2--5\,pp \citep{wang2023sc}), acknowledging this choice is anchored to SC effect sizes. We trace the failure below.
58	
59	
60	\looseness=-1 Oracle controls replacing self-extracted constraints with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+14.22$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\sim}$12\% of this ceiling (Appendix~\ref{app:oracle}).
61	
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c16f3b6c-b714-4543-9066-5029347b948b",
  "isSidechain": true,
  "promptId": "1f174627-1c82-4337-a249-ad0788c18219",
  "agentId": "a5d56391d6cff8d65",
  "type": "user",
  "uuid": "dd292ae2-9c5f-44bd-8755-7d038617c8e6",
  "sourceToolAssistantUUID": "c16f3b6c-b714-4543-9066-5029347b948b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "cec144ca-982b-493f-9bb4-f6fe13f44d38",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ticklish-frolicking-acorn"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T20:25:07.865Z_

Perfect! I found the file. Let me extract the exact information you requested from Table 1 (which is labeled as `tab:main_results`):

## Qwen3-14B × FOLIO row
**Line 50:** `Qwen3-14B & FOLIO & 204 & 84.80 & 84.31 & $-$0.49 & 1.000 \\`
- **SC value:** 84.80%
- **SICA value:** 84.31%

## Qwen3-14B × PW-D5 row
**Line 51:** `Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\`
- **SC value:** 85.00%
- **SICA value:** 85.67%

## Qwen2.5-14B × FOLIO row
**Yes, there is a row for this condition:**

**Line 46:** `Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\`
- **SC value:** 75.49%
- **SICA value:** 74.51%

Note: This row is marked with a superscript `{4s}` indicating it's a "4-seed confirmatory" condition (as explained in the table caption). There's also another Qwen2.5-14B × FOLIO variant on line 44 with the ICL (In-Context Learning) variant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd292ae2-9c5f-44bd-8755-7d038617c8e6",
  "isSidechain": true,
  "agentId": "a5d56391d6cff8d65",
  "requestId": "req_011CbJEXWiLC2ecs1vpg3t3A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7de6e4e-1d17-4b1e-939f-abce4e7974f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "cec144ca-982b-493f-9bb4-f6fe13f44d38",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ticklish-frolicking-acorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pu1VqhVQeS6YcAyGCtmN8Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3740,
      "cache_read_input_tokens": 21197,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3740
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 405,
          "cache_read_input_tokens": 21197,
          "cache_creation_input_tokens": 3740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3740,
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
