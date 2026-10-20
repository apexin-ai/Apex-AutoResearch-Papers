# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, fi

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3a32e9faecbd9fb9.jsonl`
- **Structured JSON:** [`d4d1c12f7d887506cc02.json`](../../sessions/d4/d4d1c12f7d887506cc02.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-25T07:37:21.130Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, find ALL occurrences of \begin{figure}, \begin{figure*}, \begin{table}, \begin{table*}. For each, report: (1) line number, (2) placement option [t], [h], etc., (3) whether it's single-column or double-column (figure vs figure*), (4) the caption or label nearby so I can identify which figure/table it is. Report a concise structured list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "1b5c6da8-7bf1-4b52-84e1-806e441c5a7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T07:37:22.195Z_

I'll search for all figure and table environments in the appendix.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b5c6da8-7bf1-4b52-84e1-806e441c5a7d",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuQpGP24gcjPkd4xSni",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eef1fae5-c051-43d2-92b3-11be4e7663d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xxa8BUmaRuKbBWe7hLfRKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 36741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 564,
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

_source line 3 · 2026-05-25T07:37:22.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BF2hB22djoeZgjvzURarw6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eef1fae5-c051-43d2-92b3-11be4e7663d2",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuQpGP24gcjPkd4xSni",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a04104c5-2cfb-4e8c-b0db-045d67f08e11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xxa8BUmaRuKbBWe7hLfRKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 36741,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 36741,
          "cache_creation_input_tokens": 564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 564,
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

_source line 4 · 2026-05-25T07:37:22.918Z_

<details><summary>↩ Tool result · reported error · `toolu_01BF2hB22djoeZgjvzURarw6`</summary>

```text
File content (43554 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a04104c5-2cfb-4e8c-b0db-045d67f08e11",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "5d9a3c3b-8efb-477d-a135-36f30edfa3b3",
  "toolUseResult": "Error: File content (43554 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "a04104c5-2cfb-4e8c-b0db-045d67f08e11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T07:37:24.303Z_

Let me search for the figure and table environments using grep to find all occurrences with their line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d9a3c3b-8efb-477d-a135-36f30edfa3b3",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuQwrnAf8vTvr7v1F8X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cce40b4f-ede3-49a8-a5eb-012fac352604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L8DfQiUY9vV7TFwKsnELWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 37305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1003,
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

_source line 6 · 2026-05-25T07:37:24.813Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LBtFzGqrYGm9qV3F8eLotA`</summary>

```json
{
  "pattern": "\\\\begin\\{(figure\\*?|table\\*?)\\}(\\[.*?\\])?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce40b4f-ede3-49a8-a5eb-012fac352604",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuQwrnAf8vTvr7v1F8X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f337ca5c-5689-4b85-84fe-bd912fd38e6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L8DfQiUY9vV7TFwKsnELWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 37305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1003,
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

_source line 7 · 2026-05-25T07:37:24.836Z_

<details><summary>↩ Tool result · `toolu_01LBtFzGqrYGm9qV3F8eLotA`</summary>

```text
18:\begin{table}[t]
56:\begin{table}[t]
101:\begin{table}[t]
149:\begin{figure}[t]
156:\begin{table}[t]
190:\begin{table}[t]
275:\begin{table}[t]
366:\begin{figure}[t]
373:\begin{figure}[t]
403:\begin{table}[t]
464:\begin{table}[t]
490:\begin{table}[t]
513:\begin{figure}[t]
541:\begin{table}[t]
583:\begin{figure}[t]
590:\begin{figure}[t]\ContinuedFloat
668:\begin{table}[t]
696:\begin{figure}[t]
703:\begin{table}[t]
727:\begin{table}[t]
761:\begin{table}[t]
789:\begin{figure}[t]
796:\begin{table}[t]
822:\begin{table}[t]
850:\begin{table}[t]
887:\begin{figure}[t]
894:\begin{figure}[t]
901:\begin{figure}[t]
908:\begin{table}[t]
933:\begin{table}[t]
952:\begin{table}[t]
998:\begin{table}[t]
1021:\begin{figure}[t]
1050:\begin{figure}[t]
1069:\begin{table}[t]
1094:\begin{table}[t]
1120:\begin{figure}[t]
1140:\begin{table}[t]
1163:\begin{table}[t]
1184:\begin{figure}[t]
1191:\begin{figure}[t]
1215:\begin{table}[t]
1242:\begin{table}[t]
1336:\begin{table}[t]
1363:\begin{table}[t]
1413:\begin{table}[t]
1454:\begin{table}[t]
1471:\begin{figure}[t]
1492:\begin{table}[t]
1516:\begin{figure}[t]
1530:\begin{table}[t]
1566:\begin{table}[t]
1599:\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f337ca5c-5689-4b85-84fe-bd912fd38e6e",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "512c3575-33d3-4119-a3ea-5004e6c451ff",
  "sourceToolAssistantUUID": "f337ca5c-5689-4b85-84fe-bd912fd38e6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-25T07:37:26.278Z_

Now let me read sections around each of these line numbers to extract captions and labels. I'll do this efficiently by reading chunks of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "512c3575-33d3-4119-a3ea-5004e6c451ff",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7506f4a0-4c62-4598-be1b-8d35538bb3c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 9 · 2026-05-25T07:37:26.691Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AL5GmHmP4Fw8gPhtUCri5J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7506f4a0-4c62-4598-be1b-8d35538bb3c6",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "08d44462-3950-43f8-85ee-d21c88610cc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 10 · 2026-05-25T07:37:26.699Z_

<details><summary>↩ Tool result · `toolu_01AL5GmHmP4Fw8gPhtUCri5J`</summary>

```text
1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Architecture-specific training.}
14	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
15	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Per-architecture training hyperparameters.}
22	\label{tab:arch_hyperparams}
23	\begin{tabular}{lcccl}
24	\toprule
25	Model & Batch & LR & Steps & Precision \\
26	\midrule
27	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
29	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
30	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
31	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\paragraph{Metric computation details.}
39	Token entropy is computed as $H(p_\theta | x) = -\sum_{v} p_\theta(v|x) \log_2 p_\theta(v|x)$, averaged over 1{,}000 held-out WikiText-103 samples using greedy teacher-forcing (no sampling stochasticity).
40	ECE uses 15 equal-width bins on the confidence axis $c(x) = \max_v p_\theta(v|x)$, following the standard definition~\citep{naeini2015obtaining}:
41	$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|b|}{N} |\mathrm{acc}(b) - \mathrm{conf}(b)|$.
42	Distinct-$n$ ($n \in \{1, 2, 3\}$) is the ratio of unique $n$-grams to total $n$-grams across all 5{,}000 generated samples per generation, following~\citet{li2016diversity}.
43	Perplexity is computed on a fixed 1{,}000-sample held-out split (disjoint from training and generation prompts).
44	
45	\paragraph{Seed and replication structure.}
46	The primary experiments use seeds 42, 43, 44 (3-seed cohort) for the phase diagram ($T{=}10$, 13 $\alpha$ levels).
47	Seed 45 is added for $\alpha{=}1.0$ experiments (4-seed).
48	Extended FPR analysis uses seeds 45--51 (6-pair basis, excluding MAUVE) for a total of 10 distinct seeds.
49	Cross-$T$ extensions ($T{=}15$, $20$, $25$) use the same seed set as the corresponding $\alpha$ condition.
50	
51	\paragraph{Metric drift.}
52	Table~\ref{tab:drift_summary} reports the relative change in each metric from generation~0 to generation~10 across six contamination levels.
53	Two patterns emerge: (1)~entropy and calibration (ECE) degrade monotonically with $\alpha$, while (2)~diversity metrics exhibit a non-monotonic relationship where the largest relative decline occurs at moderate contamination ($\alpha{=}0.25$) rather than full replacement ($\alpha{=}1.0$).
54	Figure~\ref{fig:metric_trajectory} (main text) visualizes representative per-generation trajectories, showing the distinct temporal profiles that underlie the Granger-precedence analysis in \S\ref{sec:method}.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
60	\label{tab:drift_summary}
61	\resizebox{\columnwidth}{!}{%
62	\begin{tabular}{lccccc}
63	\toprule
64	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
65	\midrule
66	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
67	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
68	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
69	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
70	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
71	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
72	\bottomrule
73	\end{tabular}}
74	\end{table}
75	
76	\paragraph{Data pipeline.}
77	Each generation follows a fixed protocol: (1)~sample 5{,}000 prompts from WikiText-103 (first 32 tokens of random paragraphs); (2)~generate 512-token continuations using the current model $M_t$ with temperature~$1.0$, top-$k{=}50$; (3)~mix $\alpha$ fraction of generated text with $(1{-}\alpha)$ fraction of fresh WikiText-103 samples; (4)~fine-tune from the \emph{previous generation's} checkpoint (not from pretrained $M_0$).
78	Step~(4) produces iterative collapse by accumulating distributional biases across generations, distinct from single-generation fine-tuning drift.
79	The ``replace'' paradigm (step~3) means each generation trains on a completely fresh synthetic pool---there is no accumulation of earlier-generation synthetic data within the training set.
80	
81	\paragraph{Null-condition drift interpretation.}
82	At $\alpha{=}0.0$ (Table~\ref{tab:drift_summary}), all metrics exhibit non-trivial drift despite zero synthetic contamination: distinct-1 drops $14.1\%$, entropy drops $4.6\%$, and perplexity \emph{improves} by $20.6\%$.
83	This null drift reflects iterated fine-tuning on a fixed corpus: the model progressively memorizes WikiText-103, narrowing its effective vocabulary (lower distinct-$n$, lower entropy) while fitting the held-out distribution better (lower PPL).
84	The distinction between null drift and contamination-induced collapse is critical: our detection framework specifically tests whether canary metrics \emph{temporally precede} downstream metrics, not whether drift exists.
85	Null drift produces shared downward trends but without the temporal structure (lag) that Granger testing requires.
86	
87	\paragraph{Non-monotonic diversity-contamination relationship.}
88	A counterintuitive finding in Table~\ref{tab:drift_summary}: diversity loss is \emph{largest} at $\alpha{=}0.25$ (distinct-1: $-40.3\%$) and \emph{smallest} at $\alpha{=}1.0$ ($-27.8\%$).
89	This non-monotonicity arises because at high $\alpha$, the model collapses rapidly into a few dominant modes (by gen~3--4), after which diversity stabilizes near a floor.
90	The gen-0$\to$10 relative decline is smaller because the trajectory is concave (fast initial drop, then plateau).
91	At $\alpha{=}0.25$, the real-data fraction prevents catastrophic collapse but allows a steady, monotonic diversity decline across all 10 generations, producing a larger cumulative loss.
92	
93	
94	\FloatBarrier
95	\section{Distinct-3 Results}
96	\label{app:distinct3}
97	
98	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
99	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
100	
101	\begin{table}[t]
102	\centering
103	\small
104	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
105	\label{tab:distinct3_drift}
106	\begin{tabular}{lc}
107	\toprule
108	$\alpha$ & Distinct-3 drift (\%) \\
109	\midrule
110	0.00 & $-4.4{\pm}0.5$ \\
111	0.25 & $-58.9{\pm}0.9$ \\
112	0.50 & $-52.4$ \\
113	0.75 & $-38.6{\pm}1.3$ \\
114	1.00 & $-30.5{\pm}4.0$ \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	Distinct-3 exhibits higher lag instability than distinct-1/2 (bimodal lag distribution, std${>}1.5$ vs.\ ${<}0.5$ generations), reflecting its lower signal-to-noise ratio at 512-token generation length.
120	
121	\paragraph{Non-monotonic attenuation.}
122	The inverted-U shape of diversity loss (peaking at $\alpha{=}0.25$--$0.50$, attenuating at $\alpha{=}1.0$) is consistent across all three distinct-$n$ metrics.
123	At low contamination, diversity loss reflects fine-tuning drift amplified by weak synthetic contamination, which narrows the vocabulary without triggering the catastrophic mode collapse that dominates at high $\alpha$.
124	At $\alpha{=}1.0$, the model collapses into a small set of high-frequency modes quickly (by gen~3--4), after which diversity stabilizes at a low floor; the relative decline from gen-0 is therefore smaller because the trajectory is concave rather than linear.
125	
126	\paragraph{Granger detectability of distinct-3.}
127	Despite its large magnitude, distinct-3 drift is less Granger-detectable than distinct-1/2 because of its higher temporal noise.
128	PermG detection rates at $\alpha{=}1.0$: entropy$\to$distinct-1 achieves 6/8 across all seeds; entropy$\to$distinct-3 achieves only 4/8, with 2 seeds failing due to lag instability (bimodal lag distribution shifting the peak between lag~$-1$ and lag~$-2$ across seeds).
129	This motivates our focus on distinct-1 and distinct-2 as the primary downstream metrics in the main text.
130	
131	
132	\FloatBarrier
133	\section{Observation Window Sensitivity}
134	\label{app:window_sensitivity}
135	
136	Consensus classification stabilizes at $T_{\min}{\geq}5$ (Table~\ref{tab:window_sensitivity}): all six effect-size reference pairs reach $K{\geq}4/5$ agreement at every window from $T_{\min}{=}5$ through $T_{\min}{=}10$.
137	
138	\paragraph{Per-method stability.}
139	At $\alpha{=}1.0$ (Pythia-410M, 4~seeds), we evaluate detection stability as $T_{\min}$ varies from 5 to 10 (i.e., using only generations $T_{\min}$ through $T{=}10$).
140	NaiveXCorr, DiffXCorr, ThresholdOnset, and PermG all maintain 6/6 validated pairs at every window length, confirming complete invariance to the observation start point.
141	Toda--Yamamoto shows the most variability: 3/6 at $T_{\min}{=}5$, rising to 6/6 at $T_{\min}{=}7$, then fluctuating between 3/6 and 6/6 at $T_{\min}{=}8$--$10$.
142	This instability reflects TY's higher sensitivity to degrees of freedom in short series (each 1-generation reduction removes ${\sim}10\%$ of available data at $T{=}10$).
143	
144	\paragraph{Implications for deployment.}
145	The stability result has a practical implication: a monitoring system need not wait for a full $T{=}10$ observation window before running detection.
146	As few as 6 data points ($T_{\min}{=}5$) suffice for reliable consensus-based detection at high contamination ($\alpha{=}1.0$), though the detection boundary $\alpha_c$ at shorter windows remains above $\alpha{=}0.50$ (insufficient power at $T{=}5$ for onset-level contamination).
147	The minimum requirement for Granger-type tests is $T_{\min}{\geq}5$ (below which degrees of freedom are insufficient for lag-1 regression with 2~parameters).
148	
149	\begin{figure}[t]
150	\centering
151	\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
152	\caption{Detection stability as a function of minimum observation window $T_{\min}$ (Pythia-410M, $\alpha{=}1.0$, 4~seeds). PermG forward detection (6/8) and consensus classification ($K{\geq}4$) both stabilize at $T_{\min}{\geq}5$, with no significance flips for $T_{\min} \in [5, 10]$. This robustness confirms that the choice of $T_{\min}{=}5$ in the main analysis does not drive results.}
153	\label{fig:window_sensitivity}
154	\end{figure}
155	
156	\begin{table}[t]
157	\centering
158	\small
159	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
160	\label{tab:window_sensitivity}
161	\resizebox{\columnwidth}{!}{%
162	\begin{tabular}{lccccccccc}
163	\toprule
164	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
165	\cmidrule(lr){2-9}
166	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
167	\midrule
168	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
169	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
170	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
171	\bottomrule
172	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
173	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
174	\end{tabular}}
175	\end{table}
176	
177	\FloatBarrier
178	\section{Robustness Analysis}
179	\label{app:robustness}
180	\label{app:spec_curve}
181	
182	\paragraph{Permutation count and FDR sensitivity.}
183	PermG $p$-values are stable between 5{,}000 and 10{,}000 permutations (max $|\Delta p|{=}0.010$, 0/24 significance flips at $\alpha{=}0.75$).
184	Treatment/null separation is robust to FDR threshold choice: at $q{=}0.05$, 4/36 null pairs vs.\ 19/24 treatment pairs reach significance; at $q{=}0.10$, null rejections rise to 8/36.
185	At the onset boundary ($\alpha{=}0.45$), minimum FDR-corrected $p$-values ($0.059$--$0.091$) are consistent with a continuous power transition rather than binary absence of signal.
186	
187	\paragraph{Specification curve.}
188	We construct 1{,}160 specifications from 13 contamination levels, 4~seeds, and 8 canary$\to$downstream pairs (all PermG, $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
194	\label{tab:spec_curve}
195	\begin{tabular}{lc}
196	\toprule
197	Metric & Value \\
198	\midrule
199	Total specifications & 1{,}160 \\
200	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
201	\midrule
202	\emph{By regime} & \\
203	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
204	\quad Onset ($\alpha{=}0.50$) & 75\% \\
205	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	The blind$\to$onset jump holds across the vast majority of specifications (Figure~\ref{fig:spec_curve}, main text).
211	
212	\paragraph{Specification decomposition.}
213	Within the 536 significant specifications (46.2\% of 1{,}160), the detection rate varies by canary$\to$downstream pair:
214	entropy$\to$distinct-1 and entropy$\to$distinct-2 are the most consistently detectable (significant in 75\% of above-onset specifications), while ECE$\to$perplexity is never significant (0\%, consistent with the first-differencing result in \S\ref{sec:regime}).
215	MAUVE-paired specifications show intermediate rates (50\% at $\alpha{=}1.0$, 0\% at $\alpha{=}0.50$), reflecting MAUVE's floor saturation at 1.4B scale.
216	
217	\paragraph{Cross-seed invariance.}
218	The specification curve's most notable feature is the \emph{absence} of seed-dependent specifications: no specification is significant at one seed but non-significant at another within the same $(\alpha, \text{pair})$ cell for $\alpha \in \{0.50, 0.75, 1.0\}$.
219	This uniformity (Fisher exact: $p = 3.45 \times 10^{-11}$ for the 0/8$\to$6/8 transition) provides the strongest evidence that the detection onset is a property of the data-generating process rather than a particular random initialization.
220	
221	\paragraph{Alternative FDR thresholds.}
222	Repeating the specification curve at $q{=}0.10$ increases significant specifications from 46.2\% to 53.8\%, with the additional detections concentrated at $\alpha{=}0.45$ (4 specifications cross from non-significant to significant) and $\alpha{=}0.60$ (2 specifications).
223	At $q{=}0.01$, the rate drops to 38.4\%, losing detections at $\alpha{=}0.50$ (onset boundary becomes less reliable).
224	The blind$\to$onset jump persists at all three thresholds, confirming structural robustness.
225	
226	\FloatBarrier
227	\section{Transfer Entropy and Change-Point Analysis}
228	\label{app:transfer_entropy}
229	\phantomsection\label{app:te_mi}
230	
231	Transfer entropy (TE; \citealp{schreiber2000measuring}; 3-bin discretization, $n{=}5{,}000$ permutations) yields 0/192 BH-corrected significant pairs across all conditions, confirming that nonparametric information-theoretic methods lack power at $T{=}11$.
232	A KNN-based TE estimator ($k{=}5$) shows forward-dominant TE fraction increasing monotonically with $\alpha$ (4/8 at $\alpha{=}0.25$ to 8/8 at $\alpha{=}1.0$), but this does not reach statistical significance after FDR correction.
233	
234	\paragraph{Symbolic transfer entropy.}
235	Symbolic TE~\citep{staniek2008symbolic} using Bandt--Pompe ordinal patterns ($m{=}2$, lag${=}1$, 500 circular-shift surrogates, $p{<}0.05$) provides a complementary view.
236	At the $\alpha{=}0.60$ sync-dip where PermG detects 0/8, symbolic TE detects forward causation in 4/6 pairs ($p{<}0.001$): MAUVE-channel TE${=}0.539$ at $T{=}10$ and $0.496$ at $T{=}15$; distinct-1-channel TE${=}0.122$ at $T{=}20$.
237	Positive controls where PermG succeeds (6/8) yield 0/6 significant symbolic TE pairs (TE values 0.000--0.379, all $p{>}0.14$), and baseline conditions ($T{=}5$, $\alpha{=}0.50$) yield 0/2 significant (TE${=}0.000$--$0.189$, $p{=}1.000$).
238	This pattern---symbolic TE detecting signal precisely where PermG fails---suggests the sync-dip reflects compressed temporal lag rather than absent coupling: ordinal-pattern methods capture contemporaneous co-movement that Granger's lag-based framework misses.
239	
240	\paragraph{Conditional Granger analysis.}
241	To test whether ECE confounds the entropy$\to$diversity relationship, we run conditional Granger tests controlling for ECE when testing entropy$\to$diversity and vice versa.
242	Conditioning on ECE does not eliminate entropy's predictive contribution, consistent with the ECE co-movement argument (Appendix~\ref{app:cascade_theory}): both metrics respond to the same underlying mode amplification, but entropy provides the earliest signal.
243	
244	\phantomsection\label{app:change_point}
245	\paragraph{Change-point detection.}
246	Max-split change-point tests ($n{=}5{,}000$ bootstrap) yield 66.7\% FPR under null control (12/18, $\alpha{=}0.00$), precluding use as a standalone detector.
247	However, the temporal ordering of change-points reverses between null and treatment: under null, downstream metrics break first (gen~2) before canary (gen~4--8); under treatment ($\alpha{\geq}0.75$), canary breaks first (gen~1) before downstream (gen~2--4).
248	This ordering reversal shifts monotonically with $\alpha$, consistent with the Granger-precedence analysis.
249	
250	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08d44462-3950-43f8-85ee-d21c88610cc7",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "69cd7e9a-ba9a-4c1c-9c85-3a810f32d6f6",
  "sourceToolAssistantUUID": "08d44462-3950-43f8-85ee-d21c88610cc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T07:37:27.123Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XZCenoLHyPZeYxG5og97yR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 250,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69cd7e9a-ba9a-4c1c-9c85-3a810f32d6f6",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b49fc481-1fe7-4354-a643-73469f757932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 12 · 2026-05-25T07:37:27.142Z_

<details><summary>↩ Tool result · `toolu_01XZCenoLHyPZeYxG5og97yR`</summary>

```text
250	
251	\FloatBarrier
252	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
253	\label{app:csmp}
254	
255	CUSUM sequential testing~\citep{page1954continuous} calibrated against $\alpha{=}0.0$ null control (FAR${=}$0\%) produces identical alarm times as a simple $2\sigma$ threshold at all tested operating points: both trigger at generation~1 for $\alpha{\geq}0.50$.
256	The equivalence arises because the generation-0$\to$1 entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$); CUSUM's cumulative memory provides no advantage when the initial shift dominates.
257	
258	\paragraph{Operating characteristics.}
259	We evaluate both methods across the full contamination range:
260	\begin{itemize}
261	\item $\alpha{=}0.00$--$0.45$: neither method triggers within $T{=}10$ generations (entropy drift ${\leq}5.3\%$, within null variability band).
262	\item $\alpha{=}0.50$: both trigger at generation~1 (entropy drop $18.0{\pm}0.5\%$, exceeding $2\sigma$ and CUSUM threshold simultaneously).
263	\item $\alpha{=}0.75$--$1.0$: both trigger at generation~1 (entropy drop $27.6$--$60.8\%$).
264	\end{itemize}
265	The regime structure of CUSUM/threshold monitoring thus recapitulates the PermG blind zone: no detection below $\alpha{=}0.50$ at $T{=}10$, immediate detection above.
266	The critical difference is that these methods detect \emph{deviation from baseline}, not \emph{temporal precedence}---they cannot distinguish whether entropy leads or lags diversity without additional directional analysis.
267	
268	\paragraph{Practical implications.}
269	For production monitoring where establishing Granger precedence is unnecessary, a calibrated entropy threshold ($[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}) provides a simple, zero-cost alarm.
270	CUSUM adds value only when the signal emerges gradually across multiple generations (e.g., at contamination levels near $\alpha_c$ where the generation-0$\to$1 drop is small); in our setting, the large initial entropy shift renders CUSUM's cumulative advantage moot.
271	
272	\paragraph{Detection timing comparison.}
273	Table~\ref{tab:sequential_timing} compares alarm generation for CUSUM and calibrated threshold across the full contamination range.
274	
275	\begin{table}[t]
276	\centering
277	\small
278	\caption{Sequential monitoring alarm timing (Pythia-410M, seed~42, fp32). ``---'' = no alarm within $T{=}10$. Both methods produce identical alarm patterns: no detection below $\alpha{=}0.50$, immediate (gen-1) detection above.}
279	\label{tab:sequential_timing}
280	\begin{tabular}{lccl}
281	\toprule
282	$\alpha$ & CUSUM alarm & Threshold alarm & Entropy drop (\%) \\
283	\midrule
284	0.00 & --- & --- & $-4.6$ \\
285	0.10 & --- & --- & $-5.3$ \\
286	0.25 & --- & --- & $-4.7$ \\
287	0.45 & --- & --- & $-5.1$ \\
288	0.50 & gen-1 & gen-1 & $-18.0$ \\
289	0.60 & gen-1 & gen-1 & $-28.5$ \\
290	0.75 & gen-1 & gen-1 & $-27.6$ \\
291	1.00 & gen-1 & gen-1 & $-60.8$ \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	The binary alarm pattern (no alarm below $\alpha{=}0.50$, immediate alarm above) mirrors PermG's regime structure, confirming that the blind zone is a property of the data-generating process rather than the detection method.
297	However, sequential monitoring methods cannot distinguish between causal temporal precedence and synchronous co-movement---a system relying solely on CUSUM would flag $\alpha{=}0.50$ contamination but could not determine whether entropy decline \emph{causes} or merely \emph{accompanies} diversity loss.
298	
299	\paragraph{False alarm rate calibration.}
300	Under null control ($\alpha{=}0.0$), neither method triggers false alarms at any threshold within the safe operating band $[10\%, 22\%]$, yielding FAR${=}0\%$ across all 3 null-condition seeds.
301	At thresholds below 7.5\%, both methods produce false alarms at gen-3 ($\alpha{=}0.0$ entropy drift: $-4.6\%$ approaches the threshold), giving FAR${=}100\%$.
302	This calibration sensitivity motivates a two-threshold deployment strategy: use the lenient bound ($10\%$) for early warning and the strict bound ($22\%$) for confirmed alarm, with the gap serving as a monitoring zone requiring additional diagnostic tests (e.g., Granger analysis) before triggering intervention.
303	
304	\FloatBarrier
305	\section{Background and Notation}
306	\label{app:background}
307	\label{sec:background}
308	
309	This section establishes the formal setup and notation used throughout the paper.
310	
311	\paragraph{Iterative training loop.}
312	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
313	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
314	\begin{equation}
315	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
316	    \label{eq:mixing}
317	\end{equation}
318	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
319	
320	\paragraph{Metric families.}
321	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
322	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\citep{li2016diversity} and perplexity.
323	Each metric produces a time series of $T{+}1$ observations.
324	
325	\paragraph{Lead-lag testing.}
326	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
327	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\citep{shojaie2022granger}, and Toda--Yamamoto Granger causality~\citep{toda1995statistical}.
328	
329	\paragraph{Method details.}
330	\emph{Naive cross-correlation (NaiveXCorr)} computes Pearson $r$ between $X_{t}$ and $Y_{t+\ell}$ at lag $\ell \in [-5, 5]$; significance at any lag below uncorrected $p{<}0.05$ counts as detection.
331	This method is permissive because it ignores shared trends and applies no multiplicity correction.
332	\emph{Differenced cross-correlation (DiffXCorr)} applies the same procedure to first-differenced series $\Delta X_t = X_t - X_{t-1}$, controlling for common trends but remaining bidirectional (cannot distinguish $X \to Y$ from $Y \to X$).
333	\emph{Threshold onset detection} identifies the first generation where each metric crosses a $3\sigma$ threshold below its generation-0 value (where $\sigma$ is the null-control standard deviation); detection is declared if canary onset strictly precedes downstream onset.
334	\emph{Permutation Granger causality (PermG)} tests whether lagged $X$ values improve prediction of $Y$ beyond $Y$'s own history, using 5{,}000 temporal permutations to construct a nonparametric null distribution, followed by BH-FDR correction at $q{=}0.05$ across 8 metric pairs.
335	\emph{Toda--Yamamoto (TY)} augments a VAR model with $d_{\max}$ extra lags to handle potential non-stationarity, then tests the original lag coefficients via Wald test.
336	
337	\paragraph{PermG implementation details.}
338	The permutation Granger procedure operates as follows:
339	(1)~First-difference both series: $\Delta X_t = X_t - X_{t-1}$, $\Delta Y_t = Y_t - Y_{t-1}$.
340	(2)~Fit unrestricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \sum_{j=1}^{L} b_j \Delta X_{t-j} + \epsilon_t$ (max lag $L{=}5$).
341	(3)~Fit restricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \epsilon_t$.
342	(4)~Compute observed $F$-statistic from the residual sum of squares reduction.
343	(5)~Generate 5{,}000 null realizations by randomly permuting the temporal order of $\Delta X$, re-fitting unrestricted model each time.
344	(6)~$p$-value $= (\text{count}(F_{\text{perm}} \geq F_{\text{obs}}) + 1) / (n_{\text{perm}} + 1)$ following~\citet{phipson2010permutation}.
345	The permutation scheme destroys temporal structure in $X$ while preserving its marginal distribution, providing an exact null for the hypothesis ``past $X$ does not improve prediction of $Y$.''
346	Lag selection uses AIC with maximum $L{=}5$ (constrained by $T{-}2L \geq 3$ degrees of freedom at $T{=}11$).
347	
348	\paragraph{Direction checking.}
349	For each significant pair, we additionally test the reverse direction ($Y \to X$).
350	A pair is classified as ``forward-only'' if $X \to Y$ is significant and $Y \to X$ is not; ``bidirectional'' if both are significant; and ``reverse-only'' if only $Y \to X$ is significant.
351	Forward-only pairs provide the strongest evidence for temporal precedence.
352	In the main analysis, we report forward detection counts; bidirectional pairs are flagged in the failure mode taxonomy (\S\ref{sec:generalization}).
353	
354	\paragraph{Multiple testing structure.}
355	At each contamination level and seed, we test 8 canary$\to$downstream pairs (2 canary $\times$ 4 downstream metrics; MAUVE is a 9th pair included in some analyses).
356	BH-FDR correction at $q{=}0.05$ is applied within each $(\alpha, \text{seed}, \text{method})$ family of 8 tests, yielding corrected $p$-values $p_{\mathrm{fdr}}$.
357	We do not correct across $\alpha$ levels or seeds, as these represent genuinely different conditions rather than multiple looks at the same hypothesis.
358	The 8-pair correction is conservative relative to per-family error rate control: BH-FDR at $q{=}0.05$ guarantees that at most 5\% of rejected hypotheses are false discoveries, averaging across the 8 tests within each family.
359	
360	\FloatBarrier
361	\section{MMCT Algorithm}
362	\label{app:mmct}
363	
364	\noindent\emph{See Algorithm~\ref{alg:mmct} in the main text (\S\ref{sec:mmct}) for the full MMCT pseudocode and design rationale.}
365	
366	\begin{figure}[t]
367	\centering
368	\includegraphics[width=\columnwidth]{figures/consensus_heatmap.pdf}
369	\caption{$K{\geq}3$ consensus heatmap across the $\alpha \times T$ grid (Pythia-410M, fp32). Each cell shows the number of canary$\to$diversity pairs reaching majority agreement (${\geq}3/5$ methods). Consensus detection aligns with PermG's onset at $\alpha{=}0.50$ but eliminates the non-monotonic anomaly at $\alpha{=}0.60$ (consensus detects 8/8 where PermG detects 0/8), indicating the anomaly is PermG-specific.}
370	\label{fig:consensus_heatmap}
371	\end{figure}
372	
373	\begin{figure}[t]
374	\centering
375	\includegraphics[width=\columnwidth]{figures/fig_mmct_k_operating.pdf}
376	\caption{MMCT operating characteristics as a function of consensus threshold $K$. Left axis: FPR (null-control false positives); right axis: FNR (missed detections at $\alpha{\geq}0.50$). $K{=}3$ balances FPR and sensitivity; $K{=}4$ reduces FPR further but increases FNR, particularly at boundary conditions. $K{=}2$ is dominated by high-FPR methods (NaiveXCorr, TY) and provides no useful filtering.}
377	\label{fig:mmct_k_operating}
378	\end{figure}
379	
380	\paragraph{MMCT design rationale.}
381	The MMCT consensus approach is motivated by the observation that no single method achieves both low FPR and high detection rate across all contamination levels.
382	PermG has the lowest FPR (6.7\%) but misses the $\alpha{=}0.60$ regime; DiffXCorr detects everywhere but cannot establish directionality; NaiveXCorr's 94.4\% FPR makes it unsuitable as a standalone detector.
383	By requiring $K{\geq}3$ methods to agree, MMCT effectively requires that at least one conservative method (PermG or DiffXCorr) participates in the consensus, filtering out detections driven solely by permissive methods.
384	
385	\paragraph{FPR-inverse weighting design.}
386	The weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$ ensures that methods with lower empirical FPR have proportionally higher influence on the consensus score.
387	The floor $\epsilon{=}0.01$ prevents division by zero for methods with 0\% FPR (none in our case).
388	Under this scheme, PermG's weight ($w{=}14.9$) dominates NaiveXCorr's ($w{=}1.06$) by $14{\times}$: a detection requires PermG agreement unless ${\geq}4$ other methods agree without it.
389	The empirical null distribution (step~7 of Algorithm~\ref{alg:mmct}) avoids parametric assumptions that would be unreliable for our short ($T{=}5$--$25$), non-stationary series.
390	
391	\paragraph{Sensitivity to $K$.}
392	Table~\ref{tab:mmct_k_operating} (main text) reports operating characteristics for $K \in \{2, 3, 4, 5\}$.
393	The $K{=}3$ threshold represents a Pareto-optimal operating point: decreasing to $K{=}2$ raises FPR from 10.0\% to 38.9\% with modest TPR gain ($66.7\% \to 85.4\%$ at $\alpha{=}0.50$); increasing to $K{=}4$ eliminates false positives ($0\%$) but drops TPR to ${\leq}25\%$ across all conditions.
394	At $K{=}5$ (unanimity), the expected detection rate is below 5\% everywhere---only achievable when all five methods, including the 94\%-FPR NaiveXCorr, agree.
395	
396	\FloatBarrier
397	\section{Methodological Comparison Table}
398	\label{app:method_comparison}
399	
400	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
401	No prior work combines all six dimensions.
402	
403	\begin{table}[t]
404	\centering
405	\small
406	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
407	\label{tab:method-comparison}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{lccccccl}
410	\toprule
411	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
412	\midrule
413	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
414	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
415	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
416	SIGMA~\citep{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
417	DCES~\citep{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
418	\midrule
419	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
420	\bottomrule
421	\end{tabular}%
422	}
423	\end{table}
424	
425	\paragraph{Dimension justification.}
426	The six diagnostic dimensions in Table~\ref{tab:method-comparison} are motivated by known failure modes in time-series causal inference:
427	\emph{Differencing} controls spurious regression when both series share a deterministic trend~\citep{granger1974spurious}---without it, any two monotonically declining series will appear correlated.
428	\emph{Multi-method comparison} addresses the method sensitivity documented in \S\ref{sec:mmct}: a single method's conclusion may reflect its assumptions rather than the data.
429	\emph{Multiple testing correction} is necessary because each contamination level generates 8 metric pairs; uncorrected testing at $p{<}0.05$ expects ${\sim}0.4$ false positives per condition.
430	\emph{Regime variation} is required to map the detection landscape rather than reporting a single operating point.
431	\emph{Seed replication} distinguishes signal from initialization artifacts.
432	\emph{Cross-architecture evaluation} tests whether findings are specific to one model family or reflect general properties of iterative collapse.
433	Among existing works, \citet{du2025scales} comes closest (4/6 dimensions) but omits differencing and multi-method analysis, both of which our results show are critical.
434	
435	\FloatBarrier
436	\section{Extended Discussion}
437	\label{app:extended_discussion}
438	
439	\paragraph{Calibration scope.}
440	All calibration results are specific to our setup (Pythia-410M, WikiText-103, $T{=}10$).
441	On C4 at $\alpha{=}0.50$, PermG reverse reaches 7/8 (seed-dependent: s43 1/8), indicating directional asymmetry should be verified per domain.
442	Token entropy ($H(p_\theta|\text{context})$ on held-out data) and perplexity ($\exp(H_\text{cross})$ on generated text) co-move synchronously, explaining why first-differencing eliminates canary$\to$perplexity but preserves canary$\to$diversity.
443	
444	\paragraph{Alternative explanations for the blind zone.}
445	Three mechanisms could explain why detection fails below $\alpha_c$:
446	\emph{(1)~Signal absence}: at low $\alpha$, the real-data fraction dominates, and the model's distributional shift is too small to generate temporal structure detectable by any linear method.
447	\emph{(2)~Power limitation}: the signal exists but falls below PermG's detection threshold at $T{=}10$ (supported by the $T{=}20$ result showing 5/8 at $\alpha{=}0.45$).
448	\emph{(3)~Contemporaneous coupling}: at low $\alpha$, entropy and diversity respond simultaneously rather than sequentially, eliminating the lag that Granger tests require.
449	The MI analysis (Appendix~\ref{app:mi_analysis}) favors explanation~(2): coupling between entropy and diversity exists throughout the blind zone ($\hat{I}_G > 0$ at all $\alpha$), and the cross-$T$ results confirm that longer observation resolves detection at $\alpha{=}0.45$.
450	However, explanation~(3) may contribute at very low $\alpha$ (${\leq}0.10$), where the contamination signal is minimal and both metrics drift primarily due to fine-tuning.
451	
452	\paragraph{Entropy as a measurement artifact.}
453	A potential concern is that entropy's ``leading'' behavior reflects measurement sensitivity rather than a genuine temporal cascade: entropy is a continuous quantity computed from the full probability distribution, while distinct-$n$ is a discrete count computed from a finite sample.
454	Entropy can therefore respond to arbitrarily small distributional shifts that leave the token-level generation unchanged.
455	We note three counterarguments:
456	(1)~The ECE co-movement result confirms that calibration---a separate measurement---also shifts at gen-1, suggesting the signal is real.
457	(2)~First-differencing preserves the canary$\to$diversity relationship while eliminating canary$\to$perplexity, which would not occur if the signal were purely a measurement artifact.
458	(3)~The intervention experiment demonstrates that acting on the entropy signal at gen-1 produces a measurably different outcome (64\% lower peak perplexity), confirming functional relevance.
459	Nonetheless, the possibility that entropy's sensitivity partly reflects measurement properties rather than causal priority cannot be fully excluded without mechanistic analysis.
460	
461	\paragraph{Cross-architecture failure mode analysis.}
462	The four non-confirming conditions in the cross-architecture evaluation each isolate a distinct assumption violation:
463	
464	\begin{table}[t]
465	\centering
466	\small
467	\caption{Failure mode taxonomy for non-confirming cross-architecture conditions ($\alpha{=}1.0$).}
468	\label{tab:failure_modes}
469	\resizebox{\columnwidth}{!}{%
470	\begin{tabular}{llll}
471	\toprule
472	Condition & PermG & Failure mode & Root cause \\
473	\midrule
474	GPT-2 bf16 & 0/8 & Precision & bf16 noise masks signal \\
475	GPT-2 s43 & 6/8 both & Bidirectional & No directional separation \\
476	Pythia-1.4B s42 & 2/8 & Seed & Initialization-dependent \\
477	SmolLM3-3B & 3/8 & Decoupling & Entropy non-monotonic \\
478	\bottomrule
479	\end{tabular}}
480	\end{table}
481	
482	The precision failure (GPT-2 bf16) is actionable: switching to fp32 resolves detection (0/8$\to$6/8) with no change to the underlying collapse dynamics.
483	The bidirectional failure (GPT-2 s43) is more fundamental: it indicates that for some model-seed combinations, the entropy-diversity temporal structure is symmetric, preventing directional assignment.
484	The seed dependence (Pythia-1.4B s42 vs.\ s43: 2/8 vs.\ 6/8) highlights the fragility of directional testing in short series.
485	The entropy decoupling (SmolLM3-3B: entropy 0/4, ECE 3/4) directly violates the cascade ordering assumption, suggesting that SmolLM3's architecture produces a qualitatively different collapse trajectory.
486	
487	\paragraph{Scale verification (Pythia-1.4B).}
488	\label{app:scale_14b}
489	
490	\begin{table}[t]
491	\centering
492	\small
493	\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, 6-pair basis excl.\ MAUVE).}
494	\label{tab:14b_phase}
495	\begin{tabular}{lcccc}
496	\toprule
497	$\alpha$ & \multicolumn{2}{c}{$T{=}10$} & \multicolumn{2}{c}{$T{=}15$} \\
498	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
499	         & s42 & s44 & s42 & s43 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b49fc481-1fe7-4354-a643-73469f757932",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "faeb3d93-ac94-44f5-97bc-6de5ba2e29ba",
  "sourceToolAssistantUUID": "b49fc481-1fe7-4354-a643-73469f757932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T07:37:27.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FWdPKzG31TAi8gnZMuN6mU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faeb3d93-ac94-44f5-97bc-6de5ba2e29ba",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04c10c17-bc88-4756-9274-b5f5434bb990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 14 · 2026-05-25T07:37:27.792Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L5DwUXLBcVzTeWxSDzTP2k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 750,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04c10c17-bc88-4756-9274-b5f5434bb990",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "038926d1-8ca8-4253-ab79-532400d49c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 15 · 2026-05-25T07:37:27.798Z_

<details><summary>↩ Tool result · `toolu_01FWdPKzG31TAi8gnZMuN6mU`</summary>

```text
500	\midrule
501	0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\
502	0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\
503	0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\
504	0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\
505	\bottomrule
506	\end{tabular}
507	\end{table}
508	
509	Phase-diagram structure is qualitatively preserved at 1.4B (Table~\ref{tab:14b_phase}; Figure~\ref{fig:14b_phase}): detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$).
510	The 410M sync-dip does not reproduce at 1.4B (4/6 at $\alpha{=}0.60$, $T{=}10$).
511	Directional asymmetry is seed-specific (s42 reverse 0/6 across all conditions; s43 reverse 6/6 at $\alpha{\geq}0.60$).
512	
513	\begin{figure}[t]
514	\centering
515	\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
516	\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
517	\label{fig:14b_phase}
518	\end{figure}
519	
520	\paragraph{Scale effects on detection topology.}
521	Three scale-dependent effects emerge from comparing 410M and 1.4B:
522	\begin{enumerate}
523	\item \emph{Sync-dip suppression}: The $\alpha{=}0.60$ non-monotonic anomaly is absent at 1.4B (4/6--6/6 vs.\ 0/8 at 410M), suggesting that larger models maintain wider entropy-diversity temporal separation, preventing the lag compression that produces the dip.
524	\item \emph{Seed variability amplification}: Cross-seed detection variance is higher at 1.4B (s42: 2/8 vs.\ s43: 6/8 at $\alpha{=}1.0$) than at 410M (6/8 across all seeds), possibly reflecting the larger model's richer attractor landscape.
525	\item \emph{Domain transfer}: Pythia-1.4B on C4 yields 8/8 PermG forward detection ($K{\geq}3{=}8/8$) compared to 2--6/8 on WikiText, indicating that domain characteristics (vocabulary coverage, topic diversity) interact with scale to affect detection sensitivity.
526	\end{enumerate}
527	
528	\paragraph{Intervention at 1.4B.}
529	Predictive cessation replicates at 1.4B: entropy drops $51.9\%$ ($2.946 \to 1.418$) at gen-1, triggering intervention.
530	Peak PPL rises from $19.68$ to $65.37$ (a $232\%$ increase, vs.\ $112\%$ at 410M), but recovery is faster (gen-2 PPL${=}17.44$, below the gen-0 baseline).
531	The larger entropy drop at 1.4B ($51.9\%$ vs.\ $40.7\%$) reflects stronger mode amplification at scale, consistent with the theoretical prediction that higher-capacity models amplify dominant modes more aggressively~\citep{shumailov2024curse}.
532	
533	
534	\FloatBarrier
535	\section{Per-Method Dose-Response Profiles}
536	\label{app:dose_response}
537	
538	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
539	PermG exhibits a sharp 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
540	
541	\begin{table}[t]
542	\centering
543	\small
544	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
545	\label{tab:dose_response_full}
546	\resizebox{\columnwidth}{!}{%
547	\begin{tabular}{lccccc}
548	\toprule
549	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
550	\midrule
551	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
552	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
553	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
554	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
555	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
556	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
557	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
558	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
559	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
560	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
561	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
562	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
563	\bottomrule
564	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
565	\end{tabular}}
566	\end{table}
567	
568	PermG's dose-response profile most cleanly separates detection regimes: 0/8 at null, sharp 0$\to$6 onset at $\alpha{=}0.50$, non-monotonic dip at $\alpha{=}0.55$--$0.60$.
569	Naive monitoring baselines (PPL-slope, variance-threshold) fire at $\alpha{=}0.0$ (FPR 67--100\%) because fine-tuning drift is indistinguishable from contamination without directional testing.
570	
571	\paragraph{Method-specific observations.}
572	\emph{NaiveXCorr} saturates at 7--8/8 at every $\alpha$ including null, making it useless for regime discrimination---its FPR (94.4\%) means it would declare detection in 19 out of 20 null-control runs.
573	\emph{DiffXCorr} shows the highest detection rate at $\alpha{\geq}0.50$ (6--8/8) but maintains 4/8 at null, yielding FPR${=}37.5\%$.
574	Its bidirectional nature (significant in both forward and reverse) prevents causal attribution but confirms the presence of coupling.
575	\emph{Threshold onset} is highly specific (3/8 at null) but insensitive (0/8 at $\alpha{=}0.10$--$0.45$ and $\alpha{=}0.55$--$0.75$), detecting only when the generation-1 entropy drop is unambiguously large.
576	\emph{Toda--Yamamoto} fluctuates between 0/8 and 4/8 across all $\alpha$ levels with no clear dose-response structure, reflecting its poor finite-sample properties at $T{=}10$.
577	
578	\paragraph{Inter-method agreement.}
579	Cohen's $\kappa$ between all method pairs ranges from $-0.04$ (NaiveXCorr vs.\ Threshold, near-random disagreement) to $0.42$ (PermG vs.\ DiffXCorr, moderate agreement above onset).
580	The low overall $\kappa{=}0.185$ across all five methods reflects the fundamental tension: permissive methods detect everywhere (including null), conservative methods detect rarely, and moderate methods disagree about boundary cases.
581	This motivates the MMCT consensus approach (\S\ref{sec:mmct}), which aggregates information from all methods while weighting by empirical reliability.
582	
583	\begin{figure}[t]
584	\centering
585	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_top.pdf}
586	\caption{Per-method FDR-significant pair counts (/8) across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG~(d) exhibits the cleanest regime separation---zero detections through $\alpha{=}0.45$, then a sharp 0$\to$6 jump at $\alpha{=}0.50$; NaiveXCorr~(a) saturates at 7--8/8 across all levels including null; DiffXCorr~(b) detects signal but cannot separate forward from reverse. The visual contrast across panels illustrates why method choice is itself a primary source of variability ($\kappa{=}0.185$).}
587	\label{fig:per_method_phase}
588	\end{figure}
589	
590	\begin{figure}[t]\ContinuedFloat
591	\centering
592	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_bottom.pdf}
593	\caption[]{(\textit{continued})}
594	\end{figure}
595	
596	\section{Cross-Seed Consistency at $\alpha{=}0.60$}
597	\label{app:alpha060}
598	
599	The non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}) is consistent across seeds: PermG yields 0/8 FDR-significant forward pairs for both seed~42 (v4 recompilation) and seed~43.
600	An earlier pipeline version (v3, seed~42) reported 3/8; the discrepancy is resolved by the d120 recompilation that corrected FPR calibration.
601	
602	\paragraph{Detailed metrics at $\alpha{=}0.60$.}
603	Despite PermG non-detection, metric drift at $\alpha{=}0.60$ is substantial: token entropy $-28.5\%$ (gen-0: $3.234$, gen-10: $2.311$), ECE $+1561\%$ ($0.0108 \to 0.179$), perplexity $+92.3\%$ ($26.95 \to 51.83$).
604	Raw (pre-FDR) $p$-values are marginal: ECE$\to$distinct-1 $p{=}0.034$, ECE$\to$distinct-2 $p{=}0.047$---both would pass at uncorrected $\alpha{=}0.05$ but fail BH-FDR correction ($q{=}0.05$, 8 simultaneous tests).
605	This indicates that the signal exists but falls below the corrected significance threshold, consistent with the temporal-compression interpretation.
606	
607	\paragraph{Cross-$T$ behavior.}
608	The sync-dip at $\alpha{=}0.60$ persists across observation windows: $T{=}5$: 0/8; $T{=}10$: 0/8 (both s42, s43); $T{=}15$: 0/8 (s42); $T{=}20$: 0/8 (s42), 3/8 (s43, partial dissolution).
609	Full dissolution occurs only at $T{=}25$: PermG 5/8 (s42), $K{\geq}3$ consensus 6/8.
610	The pattern---persistent non-detection for $T{\leq}20$, resolution at $T{=}25$---is consistent with $\sqrt{T}$ power accumulation eventually resolving a compressed (but non-zero) temporal lag.
611	
612	\paragraph{Scale dependence.}
613	Pythia-1.4B does \emph{not} exhibit the sync-dip at $\alpha{=}0.60$: PermG detects 4/8 (s42) and 4/6 (s43) at $T{=}10$, rising to 6/8 and 6/6 at $T{=}15$.
614	This scale-dependence suggests the phenomenon is architecture-specific: at larger scale, the entropy-diversity lag may be structurally wider (more capacity $\to$ slower mode collapse propagation), preventing the temporal compression that produces the dip at 410M.
615	
616	\paragraph{Sigmoid fit impact.}
617	The sigmoid fit excluding $\alpha{=}0.60$ yields $k{=}5.66$, $\alpha_c{=}0.765$, $R^2{=}0.286$; including it degrades $R^2$ to 0.205 and shifts $\alpha_c$ rightward by 0.058, confirming the point is a genuine outlier rather than noise.
618	Predicted detection probability at $\alpha{=}0.60$ under the sigmoid model is $P(\mathrm{det}){=}0.282$, far below the observed 0/8 (0.00), indicating the anomaly cannot be explained by smooth dose-response variation.
619	
620	\FloatBarrier
621	\section{PPL Threshold Baseline}
622	\label{app:ppl_threshold}
623	
624	A reviewer asked whether a naive perplexity threshold could match entropy's detection timing.
625	We evaluate thresholds at $+10\%$, $+25\%$, $+50\%$, $+100\%$, $+150\%$, and $+200\%$ above the generation-0 baseline PPL (26.95).
626	
627	\paragraph{Threshold-by-threshold results.}
628	The PPL trajectory at $\alpha{=}1.0$ (Pythia-410M, s42) evolves rapidly: gen-0${=}26.95$, gen-1${=}57.42$ ($+113.1\%$), gen-2${=}162.15$ ($+501.9\%$), gen-3${=}279.17$, gen-5${=}508.85$, gen-10${=}1017.81$.
629	All thresholds from $+10\%$ through $+100\%$ trigger at generation~1, because the gen-0$\to$gen-1 jump ($+113.1\%$) exceeds them all.
630	Thresholds at $+150\%$ and $+200\%$ delay triggering to generation~2 (PPL${=}162.15$ exceeds both).
631	
632	\paragraph{Comparison with entropy.}
633	Entropy's advantage over PPL monitoring is operational rather than temporal at $\alpha{=}1.0$:
634	\begin{enumerate}
635	\item \emph{Zero cost}: entropy is computed from the model's output distribution during generation---no held-out evaluation set or separate forward pass required.
636	\item \emph{Direct signal}: entropy detects distributional narrowing (mode collapse) directly; PPL detects its downstream consequence (degraded generalization).
637	\item \emph{Regime sensitivity}: at lower contamination ($\alpha{=}0.50$), entropy drops $18.0\%$ at gen-1 while PPL rises only $21.0\%$ over 10~generations---a PPL threshold calibrated for $\alpha{=}1.0$ would miss $\alpha{=}0.50$ entirely.
638	\end{enumerate}
639	
640	\paragraph{When PPL monitoring suffices.}
641	For production systems where $\alpha$ is expected to be high (e.g., known synthetic data pipelines), a PPL threshold at $+50\%$ provides equivalent detection timing to entropy with the added benefit of measuring a directly user-relevant quantity (generation quality).
642	The operational cost difference becomes relevant only for online monitoring at scale, where computing held-out PPL on every generation adds latency and requires maintaining a clean reference set.
643	
644	
645	\FloatBarrier
646	\section{PermG Power Analysis}
647	\label{app:power_analysis}
648	
649	We simulate PermG power under a bivariate DGP with linear coupling $\beta$ ($T \in \{6,\ldots,20\}$, 100 replications, 5{,}000 permutations, BH FDR $q{=}0.05$).
650	At $T{=}10$, $\beta_{50}{=}2.0$ (50\% power requires strong coupling); at $T{=}20$, $\beta_{50}$ drops to 0.9 (Table~\ref{tab:beta50}).
651	Power grows faster than $\sqrt{T}$, so the $\sqrt{T}$ formula in \S\ref{sec:theory} is a conservative lower bound.
652	FPR under FDR correction remains ${\leq}2\%$ across all $T$.
653	
654	\paragraph{Detailed power values.}
655	Selected FDR-corrected power levels illustrate the gain from longer observation: at $\beta{=}1.0$, power rises from 0.17 ($T{=}10$) to 0.30 ($T{=}15$) to 0.66 ($T{=}20$); at $\beta{=}2.0$, from 0.51 ($T{=}10$) to 0.92 ($T{=}15$) to 0.98 ($T{=}20$).
656	Raw FPR (before FDR correction) is higher but still controlled: $T{=}6$: 1\%, $T{=}8$: 6\%, $T{=}10$: 9\%, $T{=}15$: 6\%, $T{=}20$: 5\%.
657	The non-monotonic raw FPR peak at $T{=}10$ reflects the discrete-sample properties of permutation tests at small $T$; FDR correction absorbs this variation.
658	
659	\paragraph{$\sqrt{T}$ scaling product.}
660	If power scaled exactly as $\sqrt{T}$, the product $\beta_{50} \cdot \sqrt{T}$ would be constant.
661	Observed values: $T{=}8$: 5.09; $T{=}10$: 6.32; $T{=}15$: 4.65; $T{=}20$: 4.02.
662	The downward trend indicates that power grows faster than $\sqrt{T}$---each additional generation contributes more information than a simple $\sqrt{T}$ model predicts, likely because the cumulative signal (not just instantaneous SNR) drives detection in Granger-type tests.
663	
664	\paragraph{Toda--Yamamoto bootstrap comparison.}
665	TY bootstrap power simulations (200 reps, same DGP) yield substantially lower power at comparable $T$: $T{=}10$ power${=}0.205$ (vs.\ PermG 0.51 at $\beta{=}2.0$), $T{=}20$ power${=}0.409$, with Type~I error rate 8.1\% (above nominal).
666	TY's $d$-augmented lag structure wastes degrees of freedom in short series, explaining its inferior power-FPR tradeoff relative to PermG.
667	
668	\begin{table}[t]
669	\centering
670	\small
671	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
672	\label{tab:beta50}
673	\begin{tabular}{lcccc}
674	\toprule
675	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
676	\midrule
677	6  & ---  & ---  & 1\% & 0\% \\
678	8  & ---  & ---  & 6\% & 2\% \\
679	10 & 2.0  & 6.32 & 9\% & 2\% \\
680	15 & 1.2  & 4.65 & 6\% & 2\% \\
681	20 & 0.9  & 4.02 & 5\% & 1\% \\
682	\bottomrule
683	\end{tabular}
684	\end{table}
685	
686	
687	\FloatBarrier
688	\section{Non-Stationarity Robustness Analysis}
689	\label{app:nonstationarity}
690	
691	Monte Carlo simulation (AR(1) DGP, $T{=}11$, 1{,}000 reps) shows PermG FPR inflates to ${\sim}10\%$ under strong non-stationarity ($\varphi{\geq}0.95$), while first-differencing maintains proper size ($4.2$--$6.6\%$) at the cost of reduced power (Table~\ref{tab:nonstationarity_sim}).
692	Our pipeline applies first-differencing before permutation testing, combining both advantages.
693	Under null conditions ($\alpha{=}0.0$), token entropy exhibits $\varphi{=}-0.51$ (far from the danger zone); first-differencing reduces distinct-1's high raw $\varphi$ ($0.81$--$0.97$, reflecting deterministic trend) to $-0.14$--$0.44$.
694	Our empirical FPR of 4/60 (6.7\%) confirms adequate size control.
695	
696	\begin{figure}[t]
697	\centering
698	\includegraphics[width=\columnwidth]{figures/fig_ar1_diagnostic.pdf}
699	\caption{AR(1) coefficient estimates across five contamination levels (Pythia-410M, seed~42). (a)~Token entropy: raw $\varphi$ transitions from negative ($-0.51$ at $\alpha{=}0.00$) to near-unit-root ($1.00$ at $\alpha{=}1.00$), but first-differencing keeps all values below 0.98. (b)~Distinct-1: raw $\varphi$ is uniformly high ($0.75$--$0.95$) even at null, driven by deterministic trend; first-differencing reduces all to ${\leq}0.24$. Dashed red line: $\varphi{=}0.95$ danger zone.}
700	\label{fig:ar1_diagnostic}
701	\end{figure}
702	
703	\begin{table}[t]
704	\centering
705	\small
706	\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
707	\label{tab:nonstationarity_sim}
708	\resizebox{\columnwidth}{!}{%
709	\begin{tabular}{lcccccc}
710	\toprule
711	& \multicolumn{3}{c}{Size (\%, $\beta{=}0$)} & \multicolumn{3}{c}{Power (\%, $\beta{=}0.6$)} \\
712	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
713	$\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\
714	\midrule
715	0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\
716	0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\
717	0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\
718	\bottomrule
719	\end{tabular}}
720	\end{table}
721	
722	\paragraph{Empirical AR(1) coefficients.}
723	Table~\ref{tab:empirical_ar1} reports estimated AR(1) coefficients for all metric series under null ($\alpha{=}0.0$) and treatment ($\alpha{=}1.0$) conditions.
724	Under the null, all metrics exhibit $|\varphi| < 0.60$ in raw levels and $|\varphi| < 0.30$ after first-differencing, well within the safe zone.
725	Under treatment, raw distinct-$n$ series reach $\varphi{=}0.81$--$0.97$ (near unit root), but first-differencing reduces these to $\varphi{=}-0.14$--$0.44$---confirming that the deterministic trend, not stochastic persistence, drives the high raw autocorrelation.
726	
727	\begin{table}[t]
728	\centering
729	\small
730	\caption{Empirical AR(1) coefficients (Pythia-410M, 4~seeds). ``Raw'' = levels; ``Diff'' = first-differenced.}
731	\label{tab:empirical_ar1}
732	\resizebox{\columnwidth}{!}{%
733	\begin{tabular}{lcccc}
734	\toprule
735	& \multicolumn{2}{c}{$\alpha{=}0.0$} & \multicolumn{2}{c}{$\alpha{=}1.0$} \\
736	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
737	Metric & Raw $\varphi$ & Diff $\varphi$ & Raw $\varphi$ & Diff $\varphi$ \\
738	\midrule
739	Token entropy & $-0.51$ & $-0.28$ & $0.72$ & $0.15$ \\
740	ECE & $0.31$ & $-0.15$ & $0.95$ & $0.38$ \\
741	Distinct-1 & $0.55$ & $0.12$ & $0.97$ & $0.44$ \\
742	Distinct-2 & $0.48$ & $0.08$ & $0.95$ & $0.31$ \\
743	Perplexity & $0.42$ & $-0.22$ & $0.93$ & $-0.14$ \\
744	\bottomrule
745	\end{tabular}}
746	\end{table}
747	
748	\paragraph{ADF test results.}
749	Augmented Dickey--Fuller tests on first-differenced series reject the unit root hypothesis at $p{<}0.05$ in all 40 series (5~metrics $\times$ 4~seeds $\times$ 2~conditions), confirming that first-order differencing ($d{=}1$) is sufficient and higher-order differencing ($d{\geq}2$) would unnecessarily reduce power (Figure~\ref{fig:differencing_dmax}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04c10c17-bc88-4756-9274-b5f5434bb990",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "eda74540-e6fa-4b5f-b801-6de257c9d828",
  "sourceToolAssistantUUID": "04c10c17-bc88-4756-9274-b5f5434bb990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T07:37:27.800Z_

<details><summary>↩ Tool result · `toolu_01L5DwUXLBcVzTeWxSDzTP2k`</summary>

```text
750	
751	\paragraph{Why not KPSS?}
752	We use ADF (null: unit root) rather than KPSS (null: stationarity) because ADF is more conservative for our purpose: rejecting the unit-root null provides positive evidence of stationarity, while KPSS's failure to reject would only indicate insufficient evidence against stationarity.
753	In the short-series regime ($T{\leq}25$), KPSS has limited power; ADF's rejection at $p{<}0.05$ across all differenced series provides stronger evidence.
754	
755	\paragraph{Power cost of first-differencing.}
756	First-differencing eliminates spurious regression but reduces effective power by discarding level information (Table~\ref{tab:diff_power_cost}).
757	Under the AR(1) DGP ($\varphi{=}0.50$, $\beta{=}0.6$), first-differenced PermG achieves 17.7\% power versus 36.8\% for raw PermG---a 52\% relative power reduction.
758	At $\varphi{=}0.95$ the cost narrows (28.7\% vs.\ 41.5\%, 31\% reduction) because the stronger persistence makes the raw test less reliable (inflated FPR).
759	Our pipeline accepts this power cost as a necessary tradeoff: at the empirical autocorrelation levels observed in treatment series ($\varphi{=}0.72$--$0.97$ in raw levels), raw Granger testing would produce ${\sim}10\%$ FPR, invalidating the detection framework.
760	
761	\begin{table}[t]
762	\centering
763	\small
764	\caption{Power cost of first-differencing under simulated AR(1) DGP ($T{=}11$, $\beta{=}0.6$, 1{,}000 reps). The power reduction is the price paid for valid size control.}
765	\label{tab:diff_power_cost}
766	\begin{tabular}{lcccc}
767	\toprule
768	$\varphi$ & Raw power & Diff power & Reduction & Raw FPR \\
769	\midrule
770	0.50 & 36.8\% & 17.7\% & 52\% & 6.8\% \\
771	0.95 & 41.5\% & 28.7\% & 31\% & 9.5\% \\
772	0.99 & 41.7\% & 24.6\% & 41\% & 10.7\% \\
773	\bottomrule
774	\end{tabular}
775	\end{table}
776	
777	The practical consequence: at $T{=}10$, the differencing-induced power loss is the primary bottleneck for detecting weak contamination ($\alpha < 0.50$).
778	Extending observation to $T{=}20$ more than compensates: differenced power at $T{=}20$ exceeds raw power at $T{=}10$ for $\varphi \leq 0.95$, providing both valid size control and superior detection sensitivity.
779	This explains the large detection gains observed in the $T{=}20$ extension (\S\ref{app:t20_comparison}).
780	
781	\FloatBarrier
782	\section{Shapley Value Analysis}
783	\label{app:shapley}
784	
785	Shapley values~\citep{shapley1953value} computed over all $2^5{=}32$ coalitions quantify each method's marginal contribution to FPR and FNR (Table~\ref{tab:shapley_6pair}).
786	DiffXCorr achieves the best combined Shapley ($-0.299$) but cannot separate forward from reverse; among directional methods, PermG ranks best ($-0.141$).
787	The 8-pair variant (including MAUVE) yields identical rankings.
788	
789	\begin{figure}[t]
790	\centering
791	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution.pdf}
792	\caption{Shapley value decomposition by method. FPR contribution (positive = worse) and FNR contribution (negative = better) are shown for each of the five detection methods. DiffXCorr achieves the best combined Shapley ($-0.299$) but lacks directional separation; among directional methods, PermG ranks best ($-0.141$). NaiveXCorr contributes the most FPR ($+0.609$) due to its inability to distinguish signal from null drift.}
793	\label{fig:shapley_contribution}
794	\end{figure}
795	
796	\begin{table}[t]
797	\centering
798	\small
799	\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
800	\label{tab:shapley_6pair}
801	\begin{tabular}{lccc}
802	\toprule
803	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
804	\midrule
805	Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\
806	\textbf{Diff.\ XCorr}& $\mathbf{+0.007}$ & $\mathbf{-0.306}$ & $\mathbf{-0.299}$ \\
807	Threshold ($3\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\
808	Perm.\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\
809	Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\
810	\bottomrule
811	\end{tabular}
812	\end{table}
813	
814	
815	\FloatBarrier
816	\section{MMCT Weight Robustness Ablation}
817	\label{app:weight_robustness}
818	
819	PermG ranks first among directional methods under all four weighting schemes tested (equal, cap-5, cap-10, FPR-inverse cap-100), confirming the ranking is not an artifact of the weighting scheme.
820	Cap-10 and cap-100 yield identical values (consensus threshold saturates), and equal weighting still gives PermG the best combined Shapley ($-0.152$) among directional methods.
821	
822	\begin{table}[t]
823	\centering
824	\small
825	\caption{PermG combined Shapley ($\phi^{\text{comb}}$) under four weighting schemes. Rankings are invariant to weight choice.}
826	\label{tab:weight_robustness}
827	\begin{tabular}{lcccc}
828	\toprule
829	Method & Equal & Cap-5 & Cap-10 & FPR-inv \\
830	\midrule
831	PermG & $-0.152$ & $-0.148$ & $-0.141$ & $-0.141$ \\
832	DiffXCorr & $-0.285$ & $-0.291$ & $-0.299$ & $-0.299$ \\
833	Threshold & $+0.078$ & $+0.081$ & $+0.084$ & $+0.084$ \\
834	TY & $+0.088$ & $+0.084$ & $+0.082$ & $+0.082$ \\
835	NaiveXCorr & $+0.195$ & $+0.192$ & $+0.190$ & $+0.190$ \\
836	\bottomrule
837	\end{tabular}
838	\end{table}
839	
840	\paragraph{Interpretation.}
841	The FPR-inverse weighting scheme (\S\ref{sec:mmct}) penalizes high-FPR methods by assigning weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$.
842	Under this scheme, NaiveXCorr (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}6.7\%$) receives $w{=}14.9$---a $14{\times}$ differential.
843	Equal weighting gives all methods identical influence, which reduces PermG's advantage but does not change its ranking among directional methods.
844	The invariance across weighting schemes (Table~\ref{tab:weight_robustness}) confirms that PermG's superiority reflects genuine detection properties rather than favorable weighting.
845	
846	\paragraph{Per-pair contribution variability.}
847	Marginal contributions vary substantially across canary$\to$downstream pairs (Table~\ref{tab:shapley_per_pair}).
848	Token entropy$\to$distinct-1 produces the most consistent positive contribution across coalitions (std${=}0.021$), while ECE$\to$perplexity shows the highest variance (std${=}0.089$), reflecting the contemporaneous coupling issue (\S\ref{app:channel_effect_size}).
849	
850	\begin{table}[t]
851	\centering
852	\small
853	\caption{Shapley contribution by canary$\to$downstream pair (PermG, 6-pair basis). $\phi^{\text{FNR}}$ = FNR reduction (more negative = better). Std = standard deviation across all $2^4$ coalitions that include this pair.}
854	\label{tab:shapley_per_pair}
855	\begin{tabular}{lcc}
856	\toprule
857	Pair & Mean $\phi^{\text{FNR}}$ & Std \\
858	\midrule
859	Entropy$\to$Distinct-1 & $-0.042$ & 0.021 \\
860	Entropy$\to$Distinct-2 & $-0.038$ & 0.024 \\
861	ECE$\to$Distinct-1 & $-0.035$ & 0.031 \\
862	ECE$\to$Distinct-2 & $-0.031$ & 0.028 \\
863	Entropy$\to$PPL & $-0.002$ & 0.067 \\
864	ECE$\to$PPL & $-0.001$ & 0.089 \\
865	\bottomrule
866	\end{tabular}
867	\end{table}
868	
869	The four diversity-channel pairs collectively account for 96.2\% of PermG's total FNR reduction, while the two perplexity-channel pairs contribute only 3.8\%---consistent with the channel effect size analysis (\S\ref{app:channel_effect_size}) showing that perplexity channels lack the temporal lead structure required for Granger detection.
870	This concentration motivates a practical simplification: for deployment scenarios where computational cost matters, testing only the four diversity-channel pairs sacrifices less than 4\% of detection sensitivity while halving the multiple testing burden (4~tests instead of 8, reducing the FDR correction penalty).
871	
872	\paragraph{Coalition stability.}
873	PermG's marginal contribution is stable across coalition sizes: when added to a 1-method coalition, its average combined Shapley is $-0.138$ (SE${=}0.015$); when added to a 4-method coalition, $-0.144$ (SE${=}0.008$).
874	The near-zero variation ($\Delta{=}0.006$) confirms that PermG's value is complementary rather than redundant---it provides directional information that no other single method duplicates.
875	DiffXCorr shows the opposite pattern: its marginal contribution \emph{decreases} from $-0.312$ (1-method coalition) to $-0.281$ (4-method coalition) as it becomes partially redundant with NaiveXCorr (both test correlation, differing only in preprocessing).
876	
877	
878	\FloatBarrier
879	\section{PermG FPR Independence Analysis}
880	\label{app:fpr_independence}
881	
882	Table~\ref{tab:null_fpr_methods} reports null-control FPR across nine seeds (54 pairs, 6-pair basis); a tenth seed (s51) yields 0~PermG FP, giving pooled 4/60${=}$6.7\% (CI $[1.8\%, 16.2\%]$).
883	All four FP occur in te$\to$distinct pairs in seeds~45/50 (8/10 seeds yield 0~FP).
884	$K{\geq}3$ consensus produces 6/60 FP (10.0\%), of which PermG contributes to only 2.
885	At $T{=}15$, PermG FPR drops to 0/12 (0\%).
886	
887	\begin{figure}[t]
888	\centering
889	\includegraphics[width=\columnwidth]{figures/fig_fpr_sensitivity.pdf}
890	\caption{Per-seed FPR distribution across detection methods (Pythia-410M, $\alpha{=}0.0$, 10~seeds). Each dot represents one seed's FPR; boxplots show inter-seed variability. PermG FPR concentrates near 0\% (8/10 seeds yield 0 false positives) with two outlier seeds (s45, s50) driving the aggregate 6.7\%. NaiveXCorr exhibits uniformly high FPR (${\geq}83\%$) across all seeds.}
891	\label{fig:fpr_sensitivity}
892	\end{figure}
893	
894	\begin{figure}[t]
895	\centering
896	\includegraphics[width=\columnwidth]{figures/fig_null_fpr_diagnostic.pdf}
897	\caption{Null-control diagnostic: PermG $p$-value distributions under null ($\alpha{=}0.0$) across 10~seeds. Most seeds show $p$-values uniformly distributed above 0.05 (expected under the null); seeds~45 and 50 exhibit a cluster of low $p$-values in token-entropy$\to$distinct pairs, suggesting occasional null-condition coupling that does not generalize across seeds.}
898	\label{fig:null_fpr_diagnostic}
899	\end{figure}
900	
901	\begin{figure}[t]
902	\centering
903	\includegraphics[width=\columnwidth]{figures/fig_bootstrap_fpr.pdf}
904	\caption{Bootstrap confidence intervals for FPR estimates (10{,}000 resamples, 10~seeds). PermG's 95\% CI ($[1.8\%, 16.2\%]$) is the tightest among directional methods; the upper bound remains below Threshold's point estimate (27.8\%). The bootstrap distribution for NaiveXCorr is sharply peaked near 90\%, confirming that its high FPR is systematic rather than driven by individual seed outliers.}
905	\label{fig:bootstrap_fpr}
906	\end{figure}
907	
908	\begin{table}[t]
909	\centering
910	\small
911	\caption{Null-control FPR by method ($\alpha{=}0.0$, BH-FDR $q{=}0.05$). $^\ddagger$PermG: 10~seeds, 60~pairs; other methods: 9~seeds, 54~pairs (s51 6-pair breakdown pending).}
912	\label{tab:null_fpr_methods}
913	\resizebox{\columnwidth}{!}{%
914	\begin{tabular}{llrr}
915	\toprule
916	Method & Criterion & Rejections & FPR (\%) \\
917	\midrule
918	\textbf{Perm.\ Granger}$^\ddagger$ & \textbf{BH-FDR} & \textbf{4/60} & \textbf{6.7} \\
919	Diff.\ XCorr$^\dagger$ & BH-FDR & 8/54 & 14.8 \\
920	Threshold & $3\sigma$ (det.) & 13/54 & 24.1 \\
921	Toda--Yamamoto & BH-FDR & 18/54 & 33.3 \\
922	Naive XCorr & uncorr. & 51/54 & 94.4 \\
923	\bottomrule
924	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
925	\end{tabular}}
926	\end{table}
927	
928	\subsection{Per-Seed FPR Breakdown}
929	\label{app:per_seed_fpr}
930	
931	Table~\ref{tab:per_seed_fpr_8pair} reports FPR on a per-seed, per-method basis for the original 3-seed cohort (s42, s43, s44; 8-pair basis including MAUVE), while Table~\ref{tab:per_seed_fpr_6pair} extends to the 6-seed expansion (s45--s51; 6-pair basis excluding MAUVE).
932	
933	\begin{table}[t]
934	\centering
935	\small
936	\caption{Per-seed FPR (8-pair basis, $\alpha{=}0.0$, Pythia-410M, seeds 42--44). PermG achieves 0/8 on all three seeds; NaiveXCorr ${\geq}7/8$ on all.}
937	\label{tab:per_seed_fpr_8pair}
938	\resizebox{\columnwidth}{!}{%
939	\begin{tabular}{lccccc}
940	\toprule
941	Seed & PermG & DiffXCorr & Threshold & TY & NaiveXCorr \\
942	\midrule
943	42 & 0/8 & 4/8 & 3/8 & 2/8 & 8/8 \\
944	43 & 0/8 & 2/8 & 1/8 & 2/8 & 7/8 \\
945	44 & 0/8 & 3/8 & 2/8 & 0/8 & 7/8 \\
946	\midrule
947	Pooled & 0.0\% & 37.5\% & 25.0\% & 16.7\% & 91.7\% \\
948	\bottomrule
949	\end{tabular}}
950	\end{table}
951	
952	\begin{table}[t]
953	\centering
954	\small
955	\caption{Per-seed PermG FPR (6-pair basis, $\alpha{=}0.0$, seeds 45--51). Two seeds (s45, s50) contribute all 4 false positives; remaining seeds yield 0/6.}
956	\label{tab:per_seed_fpr_6pair}
957	\begin{tabular}{lccl}
958	\toprule
959	Seed & PermG fwd & $K{\geq}3$ & Affected pairs \\
960	\midrule
961	45 & 2/6 & 0/6 & te$\to$d1, te$\to$d2 \\
962	46 & 0/6 & 1/6 & --- \\
963	47 & 0/6 & 0/6 & --- \\
964	48 & 0/6 & 0/6 & --- \\
965	49 & 0/6 & 0/6 & --- \\
966	50 & 2/6 & 2/6 & te$\to$d1, te$\to$d2 \\
967	51 & 0/6 & 0/6 & --- \\
968	\bottomrule
969	\end{tabular}
970	\end{table}
971	
972	The concentration of false positives in token-entropy$\to$distinct pairs at seeds~45 and 50 suggests stochastic null-condition coupling in these specific initializations rather than a systematic calibration failure.
973	$K{\geq}3$ consensus FPR on the 6-pair basis is 6/36${=}$16.7\%; of these 6 false positives, only 2 include PermG (both at s50)---the remaining 4 are driven by high-FPR methods (NaiveXCorr $+$ Threshold $+$ TY) reaching consensus without PermG participation.
974	This decomposition clarifies why $K{\geq}3$ FPR exceeds standalone PermG FPR: the consensus mechanism aggregates false positives from multiple methods rather than filtering them.
975	
976	\FloatBarrier
977	\section{Sigmoid Transition Shape}
978	\label{app:sigmoid_shape}
979	
980	Sigmoid regression on the original 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ but $k = 478 \pm 475$ ($\mathrm{SE}(k) \approx k$), indicating that the coarse grid cannot constrain the transition shape.
981	Dense $\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\% CI $[9.4, 28.2]$).
982	The transition is steep but finite-width, not a literal discontinuity.
983	This observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\S\ref{app:power_sim}), yielding steepness ratios $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 2.6$--$3.2$ (CI lower bound ratio ${\approx}2$).
984	
985	\paragraph{Combined $T{=}10 + T{=}20$ fit.}
986	Fitting a single sigmoid to both $T$ values yields $k{=}279.3$ (SE${=}527.6$), $\alpha_c{=}0.451$, $y_{\max}{=}0.75$, AIC${=}79.86$.
987	The 90\% transition width narrows from $[0.478, 0.487]$ (width$=0.0092$) at $T{=}10$ alone to $[0.443, 0.459]$ (width$=0.0158$) in the combined fit---a leftward shift of $\alpha_c$ by $0.031$ reflecting the $T{=}20$ data's detection at $\alpha{=}0.45$.
988	The combined $k$ drops by 41.6\% relative to $T{=}10$-only, confirming that the transition appears broader when viewed across observation lengths (different $T$ values yield different effective detection thresholds).
989	We ultimately do not report the combined sigmoid in the main text because $\alpha{=}0.45$ yields contradictory counts (0/8 at $T{=}10$ vs.\ 5/8 at $T{=}20$), reflecting genuine power dependence rather than a single dose-response curve.
990	
991	\paragraph{Alternative functional forms.}
992	Probit and sigmoid fits produce identical AIC (32.99 at $T{=}10$, 79.86 combined), as expected given that both are sigmoidal CDFs differing only in tail behavior.
993	A generalized logistic ($+1$ parameter for asymmetry $\nu$) adds $+2$ AIC penalty without improving fit, confirming that a symmetric sigmoid is sufficient.
994	
995	\paragraph{Transition width characterization.}
996	The 90\% transition width---the $\alpha$ range over which detection probability rises from 5\% to 95\%---quantifies the sharpness of the regime boundary (Table~\ref{tab:transition_width}).
997	
998	\begin{table}[t]
999	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "038926d1-8ca8-4253-ab79-532400d49c50",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "fe5d1a91-99c9-4d9d-b008-b7b2fa414f30",
  "sourceToolAssistantUUID": "038926d1-8ca8-4253-ab79-532400d49c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T07:37:28.096Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKvymM7JH8GHgqX6LSjxtp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1000,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe5d1a91-99c9-4d9d-b008-b7b2fa414f30",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuR68cSf8DyNEkJ4yQR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9834deb7-04d6-48cd-92a7-f39c4f6ee08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018c4matEB6SQrmkSDg4Uaym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 38308,
      "output_tokens": 584,
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
          "input_tokens": 6,
          "output_tokens": 584,
          "cache_read_input_tokens": 38308,
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

_source line 18 · 2026-05-25T07:37:28.105Z_

<details><summary>↩ Tool result · `toolu_01DKvymM7JH8GHgqX6LSjxtp`</summary>

```text
1000	\small
1001	\caption{Sigmoid transition width (90\% range) by observation length and signal model. Narrower width indicates sharper regime onset.}
1002	\label{tab:transition_width}
1003	\begin{tabular}{lccc}
1004	\toprule
1005	Setting & Width ($\Delta\alpha$) & $\alpha_c$ & $k$ \\
1006	\midrule
1007	$T{=}10$ observed (13-pt) & 0.009 & 0.483 & 478 \\
1008	$T{=}10$ dense (17-pt) & 0.028 & 0.481 & 15.7 \\
1009	$T{=}10{+}20$ combined & 0.016 & 0.451 & 279 \\
1010	H0 linear simulation & 0.072 & 0.507 & 6.1 \\
1011	H0$'$ concave simulation & 0.090 & 0.521 & 4.9 \\
1012	\bottomrule
1013	\end{tabular}
1014	\end{table}
1015	
1016	The dense-sampling transition width ($\Delta\alpha{=}0.028$, corresponding to $\alpha \in [0.467, 0.495]$) is ${\sim}3{\times}$ narrower than smooth-model predictions (0.072--0.090), confirming the anomalous sharpness.
1017	In practical terms, a difference of $\Delta\alpha{=}0.03$ in contamination fraction determines whether detection is impossible (0\%) or reliable (75\%)---this represents approximately 150 additional synthetic samples out of 5{,}000.
1018	The narrow transition has implications for monitoring systems: slight increases in synthetic data fraction near the boundary produce large changes in detectability, creating a ``cliff effect'' where monitoring transitions from false security to reliable alarm with minimal change in the underlying contamination level.
1019	A system operating at $\alpha{=}0.47$ (undetectable) and drifting to $\alpha{=}0.50$ (detectable) would experience an abrupt shift from zero alarm rate to 75\% alarm rate---a three percentage-point contamination increase produces a qualitative change in monitoring behavior.
1020	
1021	\begin{figure}[t]
1022	\centering
1023	\includegraphics[width=\columnwidth]{figures/differencing_dmax.pdf}
1024	\caption{First-differencing order selection diagnostic. The optimal differencing order $d_{\max}$ is evaluated via ADF test statistics across all canary$\to$downstream series at $\alpha{=}1.0$. First-order differencing ($d{=}1$) achieves stationarity in all series (ADF $p{<}0.05$), confirming that higher-order differencing is unnecessary and would incur additional power loss.}
1025	\label{fig:differencing_dmax}
1026	\end{figure}
1027	
1028	\FloatBarrier
1029	\section{Intervention Threshold Sensitivity}
1030	\label{app:intervention_sensitivity}
1031	
1032	At $\alpha{=}1.0$, all five tested thresholds (5\%--25\%) trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical outcomes (peak PPL 57.0, final PPL 21.3).
1033	The safe operating band is $[10\%, 22\%]$: below 7.5\% triggers false alarms on $\alpha{=}0.0$ drift; above 22.4\% misses $\alpha{=}0.50$.
1034	
1035	\paragraph{Cross-seed and cross-scale replication.}
1036	The predictive cessation result replicates on seed~43 (bf16 precision): trigger at gen-1 with a milder entropy drop ($-22.5\%$ vs.\ $-40.7\%$ in fp32), peak PPL${=}24.65$ (lower due to bf16 dampening).
1037	On Pythia-1.4B (s42, fp32): trigger at gen-1, entropy drop $-51.9\%$ ($2.946 \to 1.418$), peak PPL spike from $19.68$ to $65.37$, recovery by gen-2 (PPL${=}17.44$), final PPL at gen-10${=}17.6$.
1038	ECE follows the same pattern: $0.007 \to 0.281$ at the spike, recovering to $0.017$ post-intervention.
1039	
1040	\paragraph{Alpha=0.75 predictive intervention.}
1041	At $\alpha{=}0.75$ (fp32, v4 pipeline), predictive cessation also triggers at gen-1, with recovery by gen-2.
1042	Post-intervention PermG detection reaches 6/8 forward, $K{\geq}4{=}6/8$, confirming that the intervention preserves the statistical detection signal while preventing perplexity degradation.
1043	Entropy drift post-intervention is only $-5.7\%$ over 10~generations (vs.\ $-27.6\%$ without intervention), consistent with the generation-1 trigger halting the collapse cascade before downstream metrics respond.
1044	
1045	\paragraph{No-intervention baseline comparison.}
1046	Without intervention at $\alpha{=}1.0$: gen-10 PPL${=}1003.73$, distinct-1${=}0.0704$.
1047	With predictive cessation: gen-10 PPL${=}21.29$, distinct-1${=}0.0844$ ($+19.9\%$ higher diversity).
1048	The intervention reduces peak perplexity by 64\% ($56.99$ vs.\ $157.09$ reactive) and preserves substantially more lexical diversity, though neither intervention strategy fully prevents the initial diversity loss at gen-1.
1049	
1050	\begin{figure}[t]
1051	\centering
1052	\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
1053	\caption{CUSUM sequential monitoring versus calibrated threshold (Pythia-410M, $\alpha{=}1.0$). Both methods trigger at generation~1 because the entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$). CUSUM's cumulative memory provides no advantage when the initial signal dominates. The shaded region marks the safe operating band $[10\%, 22\%]$ for threshold-based detection.}
1054	\label{fig:cusum_monitoring}
1055	\end{figure}
1056	
1057	
1058	\FloatBarrier
1059	\section{Channel Effect Size Analysis}
1060	\label{app:channel_effect_size}
1061	
1062	First-differencing retains comparable $|r|$ for both diversity (0.952) and perplexity (1.00) channels, ruling out selective power loss.
1063	The Granger $F$-statistic asymmetry ($20$--$28{\times}$ higher for diversity) reflects temporal structure: diversity channels peak at canary-leading lags (81\% at lag${<}0$, median $-1$), while perplexity peaks at lag${=}0$ (contemporaneous co-movement).
1064	Granger tests correctly assign low $F$ to contemporaneous relationships.
1065	
1066	\paragraph{Lag structure decomposition.}
1067	Table~\ref{tab:lag_structure} reports the cross-correlation peak lag for each canary$\to$downstream channel, illustrating the structural difference that drives Granger detectability.
1068	
1069	\begin{table}[t]
1070	\centering
1071	\small
1072	\caption{Cross-correlation peak lag by channel (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Negative lag = canary leads. Diversity channels show consistent canary-leading structure; perplexity channels peak at lag~0.}
1073	\label{tab:lag_structure}
1074	\begin{tabular}{lccl}
1075	\toprule
1076	Channel & Peak lag & $|r|$ at peak & Structure \\
1077	\midrule
1078	Entropy$\to$Dist-1 & $-1$ & 0.96 & canary leads \\
1079	Entropy$\to$Dist-2 & $-1$ & 0.95 & canary leads \\
1080	ECE$\to$Dist-1 & $-1$ & 0.94 & canary leads \\
1081	ECE$\to$Dist-2 & $-1$ & 0.93 & canary leads \\
1082	Entropy$\to$PPL & $0$ & 0.99 & contemporaneous \\
1083	ECE$\to$PPL & $0$ & 0.98 & contemporaneous \\
1084	\bottomrule
1085	\end{tabular}
1086	\end{table}
1087	
1088	The contemporaneous co-movement of canary$\to$perplexity explains why Granger tests fail ($F{\approx}0$, $p{=}0.99$ after differencing): perplexity and entropy respond to the same underlying distributional shift at the same time step, so neither provides predictive improvement over the other's own history.
1089	This is not a limitation of the test but a correct inference---perplexity is not ``downstream'' of entropy in the temporal sense.
1090	
1091	\paragraph{Fisher Z-transform comparison.}
1092	To formally test whether diversity and perplexity channels differ in lagged correlation magnitude, we apply the Fisher Z-transform to peak cross-correlation coefficients (Table~\ref{tab:fisher_z}).
1093	
1094	\begin{table}[t]
1095	\centering
1096	\small
1097	\caption{Fisher Z-transform comparison of channel correlations (Pythia-410M, $\alpha{=}1.0$, 4~seeds). $Z_{\text{diff}}$ tests whether lagged ($\ell{=}{-}1$) correlation differs between diversity and perplexity channels.}
1098	\label{tab:fisher_z}
1099	\begin{tabular}{lcccc}
1100	\toprule
1101	Comparison & $r_{\text{div}}$ & $r_{\text{ppl}}$ & $Z_{\text{diff}}$ & $p$ \\
1102	\midrule
1103	\emph{Lag${=}0$ (contemp.)} \\
1104	\quad Entropy$\to$ & 0.955 & 0.990 & $-2.13$ & 0.033 \\
1105	\quad ECE$\to$ & 0.935 & 0.980 & $-2.41$ & 0.016 \\
1106	\midrule
1107	\emph{Lag${=}{-}1$ (canary leads)} \\
1108	\quad Entropy$\to$ & 0.952 & 0.812 & $+3.67$ & ${<}0.001$ \\
1109	\quad ECE$\to$ & 0.941 & 0.795 & $+3.89$ & ${<}0.001$ \\
1110	\bottomrule
1111	\end{tabular}
1112	\end{table}
1113	
1114	At lag${=}0$ (contemporaneous), perplexity channels show \emph{higher} correlation than diversity channels ($r{=}0.990$ vs.\ $0.955$, $Z{=}-2.13$, $p{=}0.033$), reflecting the synchronous entropy-perplexity coupling.
1115	At lag${=}-1$ (canary leading by one generation), the pattern reverses decisively: diversity channels achieve $r{=}0.952$ vs.\ perplexity's $r{=}0.812$ ($Z{=}3.67$, $p{<}0.001$).
1116	This reversal explains the Granger $F$-statistic asymmetry: perplexity channels do not have weaker coupling overall, but their coupling is \emph{contemporaneous rather than lagged}.
1117	A Granger test measures whether \emph{past} values of $X$ predict \emph{current} $Y$ beyond $Y$'s own history; contemporaneous coupling produces zero improvement, hence $F \approx 0$.
1118	The Fisher Z analysis confirms that the canary$\to$perplexity non-detection is a correct statistical inference about temporal structure rather than a power limitation.
1119	
1120	\begin{figure}[t]
1121	\centering
1122	\includegraphics[width=\columnwidth]{figures/fig_channel_effect.pdf}
1123	\caption{Channel effect size comparison: Granger $F$-statistic for canary$\to$diversity versus canary$\to$perplexity channels (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Diversity channels produce $20$--$28{\times}$ higher $F$-statistics than perplexity channels, reflecting the temporal structure difference: diversity correlations peak at canary-leading lags (81\% at lag${<}0$), while perplexity correlations are contemporaneous (50\% at lag${=}0$).}
1124	\label{fig:channel_effect}
1125	\end{figure}
1126	
1127	
1128	\FloatBarrier
1129	\section{Mutual Information and Partial Correlation}
1130	\label{app:mi_analysis}
1131	
1132	Gaussian MI lower bound ($\hat{I}_G = -\frac{1}{2}\log_2(1{-}r^2)$) between token entropy and distinct-$n$ remains positive throughout the blind zone (0.010--0.141~bits), confirming coupling exists below PermG's detection threshold.
1133	No discontinuity at $\alpha_c$: detection onset reflects power accumulation, not an information transition.
1134	
1135	\paragraph{MI across the blind zone.}
1136	Table~\ref{tab:mi_blind} reports Gaussian MI between token entropy and distinct-1 at each contamination level below $\alpha_c$.
1137	MI increases monotonically with $\alpha$, confirming that the entropy--diversity coupling strengthens continuously across the blind$\to$detection boundary.
1138	The detection onset at $\alpha_c$ therefore reflects a power threshold (sufficient signal-to-noise for PermG to detect the coupling) rather than a qualitative change in the underlying statistical relationship.
1139	
1140	\begin{table}[t]
1141	\centering
1142	\small
1143	\caption{Gaussian MI lower bound between token entropy and distinct-1 across the blind zone (Pythia-410M, $T{=}10$, seed~42).}
1144	\label{tab:mi_blind}
1145	\begin{tabular}{lcc}
1146	\toprule
1147	$\alpha$ & $\hat{I}_G$ (bits) & PermG \\
1148	\midrule
1149	0.00 & 0.010 & 0/8 \\
1150	0.10 & 0.025 & 0/8 \\
1151	0.25 & 0.048 & 0/8 \\
1152	0.45 & 0.141 & 0/8 \\
1153	0.50 & 0.312 & 6/8 \\
1154	\bottomrule
1155	\end{tabular}
1156	\end{table}
1157	
1158	\subsection{Partial Correlation Analysis}
1159	\label{app:partial_corr}
1160	
1161	Partial correlations controlling for generation number (Table~\ref{tab:partial_corr}) show that contemporaneous associations drop after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 detection-condition pairs retaining significance.
1162	
1163	\begin{table}[t]
1164	\centering
1165	\small
1166	\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
1167	\label{tab:partial_corr}
1168	\resizebox{\columnwidth}{!}{%
1169	\begin{tabular}{@{}l cc cc cc cc@{}}
1170	\toprule
1171	& \multicolumn{4}{c}{Contemporaneous} & \multicolumn{4}{c}{Lagged (canary$_{t-1}$)} \\
1172	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
1173	& \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} & \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} \\
1174	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
1175	$\alpha$ & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. \\
1176	\midrule
1177	0.00 & 0.414 & 3/18 & 0.323 & 0/18 & 0.563 & 8/18 & 0.524 & 9/18 \\
1178	0.50 & 0.590 & 9/18 & 0.381 & 2/18 & 0.759 & 12/18 & 0.841 & 17/18 \\
1179	0.75 & 0.636 & 9/18 & 0.521 & 3/18 & 0.831 & 17/18 & 0.913 & 18/18 \\
1180	\bottomrule
1181	\end{tabular}}
1182	\end{table}
1183	
1184	\begin{figure}[t]
1185	\centering
1186	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation.pdf}
1187	\caption{Partial correlation scatter plots for canary$\to$diversity pairs at $\alpha{=}0.75$ (Pythia-410M). Left: contemporaneous partial correlations drop after controlling for generation trend. Right: lagged partial correlations \emph{strengthen} after trend removal ($\bar{|r|}$: $0.831{\to}0.913$), confirming that the temporal precedence signal is not a shared-trend artifact.}
1188	\label{fig:partial_corr}
1189	\end{figure}
1190	
1191	\begin{figure}[t]
1192	\centering
1193	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation_agg.pdf}
1194	\caption{Aggregated partial correlation analysis across contamination levels. Lagged canary$\to$diversity correlations increase monotonically with $\alpha$ (from $0.524$ at null to $0.913$ at $\alpha{=}0.75$), while contemporaneous correlations plateau. The growing gap between lagged and contemporaneous partial $|r|$ with increasing contamination indicates that the temporal lead signal strengthens with signal-to-noise ratio.}
1195	\label{fig:partial_corr_agg}
1196	\end{figure}
1197	
1198	\paragraph{Interpretation.}
1199	The partial correlation analysis serves two purposes:
1200	(1)~It confirms that the canary$\to$diversity temporal precedence is not driven by a shared trend (generation number): removing the linear trend \emph{strengthens} rather than eliminates the lagged association.
1201	(2)~It shows that the temporal signal grows with contamination level: at $\alpha{=}0.00$, lagged partial $|r|{=}0.524$ (marginal significance); at $\alpha{=}0.75$, lagged partial $|r|{=}0.913$ (universal significance, 18/18).
1202	This monotonic growth parallels the MI analysis and confirms that the blind-zone boundary reflects statistical power rather than a qualitative transition in the coupling structure.
1203	
1204	\paragraph{Null behavior.}
1205	At $\alpha{=}0.00$, 9/18 lagged pairs reach significance despite no synthetic contamination, reflecting fine-tuning drift coupling: both entropy and diversity decline during pure fine-tuning (Table~\ref{tab:drift_summary}), creating a weak temporal association.
1206	These null-condition correlations are substantially weaker than treatment-condition correlations ($0.524$ vs.\ $0.913$), and the 9/18 significance rate is consistent with the expected false positive rate under weak coupling (mid-range $p$-values cluster near the significance boundary).
1207	
1208	
1209	\FloatBarrier
1210	\section{Moment Cascade Analysis}
1211	\label{app:moment_cascade}
1212	
1213	Onset (5\% threshold) occurs at generation~1 for entropy in all 6 conditions and at generation~2 for distinct-$n$ in all 18 pairwise comparisons (Table~\ref{tab:moment_cascade}; Figure~\ref{fig:cascade_onset}, main text).
1214	
1215	\begin{table}[t]
1216	\centering
1217	\small
1218	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1219	\label{tab:moment_cascade}
1220	\resizebox{\columnwidth}{!}{%
1221	\begin{tabular}{llcccccc}
1222	\toprule
1223	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
1224	\midrule
1225	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
1226	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1227	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1228	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
1229	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1230	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1231	\bottomrule
1232	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
1233	\end{tabular}}
1234	\end{table}
1235	
1236	
1237	ECE shows onset at generation~1 at $\alpha{\geq}0.50$; perplexity never reaches 5\% onset at low contamination ($\alpha{\leq}0.25$).
1238	
1239	\paragraph{Onset threshold sensitivity.}
1240	Table~\ref{tab:onset_threshold_sensitivity} examines how the cascade ordering result depends on the choice of onset threshold (5\%, 10\%, 15\%, 20\%).
1241	
1242	\begin{table}[t]
1243	\centering
1244	\small
1245	\caption{Cascade ordering $t_H \leq t_D$ validity as a function of onset threshold (Pythia-410M, 6 conditions, $\alpha{\geq}0.10$).}
1246	\label{tab:onset_threshold_sensitivity}
1247	\begin{tabular}{lccc}
1248	\toprule
1249	Threshold & $t_H \leq t_D$ & $t_H = t_D$ & $t_H > t_D$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9834deb7-04d6-48cd-92a7-f39c4f6ee08e",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "632abcd7-2f96-4363-ad5f-8d03fc5cc22d",
  "sourceToolAssistantUUID": "9834deb7-04d6-48cd-92a7-f39c4f6ee08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T07:37:29.692Z_

Now let me continue reading the rest of the file to capture all the remaining figure and table environments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "632abcd7-2f96-4363-ad5f-8d03fc5cc22d",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuRLChQS57WarYJdGNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6386458-cfa2-478c-91eb-b2798460393a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018V3ShKwenJA46UdAJKqkAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 35187,
      "cache_read_input_tokens": 39045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35187,
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

_source line 20 · 2026-05-25T07:37:30.739Z_

<details open><summary>🔧 Tool call — Read · `toolu_017fvkLuEg3gJcEqRY7ieukf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1250,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6386458-cfa2-478c-91eb-b2798460393a",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuRLChQS57WarYJdGNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6394f1c2-2d08-4fe8-829a-3e157032e377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018V3ShKwenJA46UdAJKqkAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 35187,
      "cache_read_input_tokens": 39045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35187,
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

_source line 21 · 2026-05-25T07:37:30.746Z_

<details><summary>↩ Tool result · `toolu_017fvkLuEg3gJcEqRY7ieukf`</summary>

```text
1250	\midrule
1251	5\% & 6/6 & 0/6 & 0/6 \\
1252	10\% & 6/6 & 0/6 & 0/6 \\
1253	15\% & 5/6 & 1/6 & 0/6 \\
1254	20\% & 4/6 & 2/6 & 0/6 \\
1255	\bottomrule
1256	\end{tabular}
1257	\end{table}
1258	
1259	At all thresholds, the ordering $t_H \leq t_D$ is never violated ($t_H > t_D$ in 0/24 cells).
1260	At the strictest threshold (5\%), entropy precedes diversity by exactly one generation in all 6 conditions.
1261	At relaxed thresholds (${\geq}15\%$), some conditions show simultaneous onset ($t_H = t_D$), because the larger threshold absorbs the diversity lag---consistent with the margin condition in Design Principle~\ref{prop:div_lag}.
1262	
1263	\paragraph{MAUVE cascade position.}
1264	MAUVE~\citep{pillutla2021mauve} onset occurs at generation~2--3, consistently after distinct-$n$ onset (gen-2), establishing a three-phase cascade: $\{H, \mathrm{ECE}\} \to \mathrm{Dist}\text{-}n \to \mathrm{MAUVE}$.
1265	MAUVE's later onset reflects its distributional-comparison nature: it measures the divergence between generated and reference text distributions, which requires substantial lexical collapse before the divergence exceeds the detection threshold.
1266	At $\alpha{=}1.0$, MAUVE floor saturation (${\sim}0.033$) occurs by gen-3--4, after which it becomes uninformative (constant series).
1267	
1268	\paragraph{Perplexity irregularity.}
1269	Perplexity onset is condition-dependent rather than cascade-ordered: at $\alpha{=}0.50$ (s42), PPL onset occurs at gen-4 (delayed relative to entropy gen-1 and diversity gen-2); at $\alpha{=}0.75$, PPL onset is gen-1 (contemporaneous with entropy).
1270	This irregularity is consistent with the first-differencing result: PPL is not temporally downstream of entropy in the Granger sense.
1271	Instead, PPL responds to a different aspect of collapse (cross-entropy on held-out data) that can accelerate or decelerate independently of the entropy-diversity cascade.
1272	
1273	
1274	\FloatBarrier
1275	\section{Cascade Ordering Theory: Derivations}
1276	\label{app:cascade_theory}
1277	
1278	This section provides the full derivations for Design Principle~\ref{thm:entropy_leads} and Design Principle~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
1279	
1280	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1281	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
1282	\end{assumption}
1283	
1284	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\citep{shumailov2024curse,dohmatob2024tale}.
1285	
1286	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1287	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
1288	\end{proposition}
1289	
1290	\begin{proof}
1291	Taylor-expanding $H$ around $p$:
1292	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1293	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1294	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
1295	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
1296	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
1297	\end{proof}
1298	
1299	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1300	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
1301	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
1302	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
1303	\end{proposition}
1304	
1305	\begin{proof}
1306	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
1307	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
1308	\end{proof}
1309	
1310	\paragraph{Derivation of Design Principle~\ref{thm:entropy_leads}.}
1311	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
1312	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
1313	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
1314	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
1315	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
1316	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
1317	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
1318	
1319	\paragraph{Derivation of Design Principle~\ref{prop:div_lag}.}
1320	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
1321	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
1322	Since time is discrete, $t_D \geq t_H + 1$. $\square$
1323	
1324	\paragraph{ECE co-movement (qualitative argument).}
1325	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
1326	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
1327	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
1328	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
1329	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Design Principle~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
1330	
1331	\paragraph{Empirical ECE drift across contamination levels.}
1332	ECE co-movement with entropy is monotonic across all tested $\alpha$ values (Table~\ref{tab:ece_drift}).
1333	At $\alpha{=}0.25$, ECE increases by $+79.2\%$ while entropy decreases by $-4.7\%$---the asymmetry in magnitude reflects ECE's nonlinear dependence on confidence via the $\max$ operator.
1334	At $\alpha{=}1.0$, ECE drift reaches $+3762$--$3821\%$ ($0.0108 \to 0.417$--$0.424$ across seeds), the largest proportional change among all tracked metrics.
1335	
1336	\begin{table}[t]
1337	\centering
1338	\small
1339	\caption{ECE drift across contamination levels (Pythia-410M, WikiText, fp32). ECE increases monotonically with $\alpha$, co-moving with entropy decrease.}
1340	\label{tab:ece_drift}
1341	\begin{tabular}{lccc}
1342	\toprule
1343	$\alpha$ & ECE gen-0 & ECE gen-10 & Drift (\%) \\
1344	\midrule
1345	0.00 & 0.0108 & $0.015{\pm}0.002$ & $+37.6{\pm}14$ \\
1346	0.25 & 0.0108 & $0.019{\pm}0.002$ & $+79.2{\pm}15.9$ \\
1347	0.50 & 0.0108 & $0.087{\pm}0.002$ & $+703{\pm}18$ \\
1348	0.60 & 0.0108 & 0.179 & $+1561$ \\
1349	0.75 & 0.0108 & $0.215{\pm}0.002$ & $+1885{\pm}18$ \\
1350	1.00 & 0.0108 & $0.421{\pm}0.004$ & $+3792{\pm}30$ \\
1351	\bottomrule
1352	\end{tabular}
1353	\end{table}
1354	
1355	ECE onset timing (5\% threshold) at $\alpha{\geq}0.50$ is generation~1, coinciding with entropy onset---consistent with the qualitative argument above that $\Delta\mathrm{ECE} > 0$ whenever $\Delta\bar{H} < 0$.
1356	At $\alpha{=}0.25$, ECE onset delays to generation~4 (seed~43), reflecting the weaker mode amplification signal at low contamination.
1357	At 1.4B scale, ECE follows the same pattern: gen-0 values are lower ($0.007$--$0.008$) but gen-10 values track collapse severity monotonically ($0.145$ at $\alpha{=}0.45$ to $0.268$ at $\alpha{=}0.75$).
1358	
1359	\paragraph{Empirical support for cascade ordering.}
1360	Cascade ordering $t_H \leq t_D$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43: bidirectional).
1361	Table~\ref{tab:cascade_onset} reports onset generations for representative conditions.
1362	
1363	\begin{table}[t]
1364	\centering
1365	\small
1366	\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1367	\label{tab:cascade_onset}
1368	\begin{tabular}{llcccc}
1369	\toprule
1370	Seed & $\alpha$ & $t_H$ & $t_{\mathrm{ECE}}$ & $t_D$ & $t_M$ \\
1371	\midrule
1372	42 & 0.50 & 1 & 1 & 2 & 3 \\
1373	43 & 0.50 & 1 & 1 & 2 & 2 \\
1374	42 & 0.75 & 1 & 1 & 2 & 3 \\
1375	43 & 0.75 & 1 & 1 & 2 & 2 \\
1376	\bottomrule
1377	\end{tabular}
1378	\end{table}
1379	
1380	
1381	\phantomsection\label{app:alpha_c_proof}
1382	\paragraph{Justification of the empirical boundary model.}
1383	At the detection threshold, $\mathrm{Power}(\alpha_c, T) = \pi^*$.
1384	Since $\alpha_c$ lies below the non-monotonic dip region ($\alpha_c < 0.55$), the signal model applies directly.
1385	From the power function $\mathrm{Power} = \Phi(S(\alpha) \cdot \sqrt{T} / \sigma)$, setting $S(\alpha_c) \cdot \sqrt{T} / \sigma = z^*$ and substituting the signal model $S(\alpha) = c\,\alpha^\beta$ yields $c\,\alpha_c^\beta = z^* \sigma / \sqrt{T}$.
1386	Solving: $\alpha_c(T) = (z^* \sigma / c)^{1/\beta} \cdot T^{-1/(2\beta)}$, giving the stated form with exponent $\gamma = 1/(2\beta)$.
1387	
1388	\paragraph{Calibration and consistency.}
1389	Fitting $P(\mathrm{det}|\alpha,T) = \Phi(A \cdot \alpha^\beta \cdot \sqrt{T} - z_0)$ to $T \in \{10, 20\}$ yields $\beta{=}0.24$, $\alpha_\infty{=}0$.
1390	Held-out test ($T \in \{5, 15\}$): MAE${=}0.106$, 95\% CI coverage 6/6.
1391	Leave-one-$T$-out CV (15 cells, sync-dip excluded): MAE${=}0.037$, coverage 15/15.
1392	Profile likelihood yields $\hat{\beta}{=}0.66$ (CI $[0.24, 0.78]$); the wide interval reflects a flat surface.
1393	
1394	\paragraph{Worked example.}
1395	At $\alpha{=}0.50$, $T{=}10$ (seed~42): entropy drops from $3.234$ to $2.649$ at gen-1 ($-18.1\%$), while distinct-1 remains at $0.0968$ (unchanged from gen-0).
1396	At gen-2, distinct-1 drops to $0.0812$ ($-16.1\%$).
1397	The mode amplification perturbation $\delta = 0.50 \cdot (\mathcal{T}(p_0) - p_0)$ satisfies $\|\delta\|_\infty < \gamma(p_0, \epsilon)$ at gen-0 (entropy responds, diversity does not), but at gen-1 the accumulated shift $p_1 = p_0 + \delta$ produces $\|\delta_1\|_\infty > \gamma(p_1, \epsilon)$, causing tokens to exit the effective support and triggering distinct-1 decline.
1398	The one-generation lag is thus explained by the margin condition in Design Principle~\ref{prop:div_lag}: the margin $\gamma$ is consumed by the gen-0$\to$1 perturbation, and the gen-1$\to$2 perturbation pushes tokens below the generation threshold $\epsilon$.
1399	
1400	\paragraph{Boundary model limitations.}
1401	The empirical boundary $\alpha_c(T) = A \cdot T^{-\gamma}$ is fitted to 3--4 data points ($T \in \{5, 10, 15, 20\}$) with 3 free parameters ($A$, $\gamma$, and the sub-linear signal exponent $\beta$).
1402	This parametric flexibility means the model can accommodate a wide range of decay shapes, and the $\gamma$ CI ($[0.64, 2.08]$) cannot distinguish sub-linear from super-linear decay.
1403	The boundary should therefore be interpreted as a descriptive summary of the observed pattern rather than a predictive model.
1404	Extrapolation beyond $T{=}25$ or below $\alpha{=}0.25$ is not supported by the data.
1405	The qualitative conclusion---detection improves with longer observation---is robust and does not depend on the specific $\gamma$ value.
1406	
1407	\paragraph{Sensitivity to the generation threshold $\epsilon$.}
1408	Design Principle~\ref{thm:entropy_leads} depends on the margin $\gamma(p, \epsilon)$, which in turn depends on the generation threshold $\epsilon \approx c/N$.
1409	Increasing the generation sample size $N$ (from 5{,}000 to 10{,}000) reduces $\epsilon$ by half, widening the margin and extending the entropy-only phase.
1410	In our experiments ($N{=}5{,}000$, effective $\epsilon \approx 2 \times 10^{-4}$), the margin is consumed after one generation at $\alpha{\geq}0.50$, producing the observed $t_D - t_H = 1$ lag.
1411	At lower contamination ($\alpha{=}0.25$), the smaller perturbation preserves the margin longer: the cumulative perturbation does not exceed $\gamma$ until gen-2--3 (Table~\ref{tab:margin_consumption}), explaining the wider entropy-diversity lag at low $\alpha$.
1412	
1413	\begin{table}[t]
1414	\centering
1415	\small
1416	\caption{Margin consumption across contamination levels (Pythia-410M, seed~42). ``Margin gen'' = first generation where cumulative $\|\delta\|_\infty > \gamma$. The diversity lag $t_D - t_H{=}1$ is invariant despite variable margin consumption timing.}
1417	\label{tab:margin_consumption}
1418	\begin{tabular}{lccc}
1419	\toprule
1420	$\alpha$ & $\gamma(p_0, \epsilon)$ & Margin gen & $t_D - t_H$ \\
1421	\midrule
1422	0.10 & $2.3 \times 10^{-3}$ & 3 & 1 \\
1423	0.25 & $2.3 \times 10^{-3}$ & 2 & 1 \\
1424	0.50 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1425	0.75 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1426	1.00 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1427	\bottomrule
1428	\end{tabular}
1429	\end{table}
1430	
1431	The invariant $t_D - t_H = 1$ across all $\alpha$ levels (despite variable margin consumption timing) reflects the discrete-time nature of the experiment: even when the margin is consumed within a single generation, the diversity response cannot manifest until the next generation's samples are drawn.
1432	This suggests that continuous-time monitoring (within-generation token-level tracking) could reveal a finer-grained cascade with $\Delta t < 1$ generation, but our current experimental design cannot resolve sub-generation dynamics.
1433	
1434	\FloatBarrier
1435	\section{Power Simulation: Shape Comparison}
1436	\label{app:power_sim}
1437	
1438	Simulated PermG detection under linear (H0), concave (H0$'$), and step (H1) signal models (1{,}000 reps, $n_\text{perm}{=}1{,}000$, BH-FDR $q{=}0.05$).
1439	Smooth models produce onset steepness $k{=}4.9$--$6.1$; the observed $k{=}15.7$ is ${\approx}3{\times}$ higher.
1440	The scaling exponent alone cannot distinguish smooth from step boundaries (H0$'$ $\gamma{=}1.87$ vs.\ observed $\gamma{=}2.08$).
1441	The 6/8 detection ceiling reflects MAUVE floor saturation, not signal limitations.
1442	
1443	\paragraph{Signal model specifications.}
1444	\emph{H0 (linear)}: $S(\alpha) = c \cdot \alpha$, where $c$ is calibrated to produce 50\% detection at $\alpha{=}0.50$, $T{=}10$.
1445	\emph{H0$'$ (concave)}: $S(\alpha) = c \cdot \alpha^{0.5}$, capturing sub-linear signal growth as mode amplification saturates.
1446	\emph{H1 (step)}: $S(\alpha) = 0$ for $\alpha < \alpha_c$, $S(\alpha) = c$ for $\alpha \geq \alpha_c$, representing a genuine phase transition.
1447	The simulated DGP generates bivariate time series $(X_t, Y_t)$ with $Y_t = \beta X_{t-1} + \epsilon_t$ (lag-1 coupling); $\beta$ is set to produce the target $S(\alpha)$ at each contamination level.
1448	
1449	\paragraph{Onset steepness comparison.}
1450	Table~\ref{tab:steepness_comparison} reports fitted sigmoid steepness $k$ for each signal model.
1451	The observed $k{=}15.7$ (CI $[9.4, 28.2]$) exceeds all smooth-model predictions, with the lower CI bound ($k{=}9.4$) still ${\sim}2{\times}$ higher than the smoothest model (H0$'$: $k{=}4.9$).
1452	This excess steepness is consistent with---but does not prove---a genuine discontinuity in the signal structure at $\alpha_c$.
1453	
1454	\begin{table}[t]
1455	\centering
1456	\small
1457	\caption{Onset steepness $k$ under different signal models (1{,}000 reps, PermG, BH-FDR $q{=}0.05$).}
1458	\label{tab:steepness_comparison}
1459	\begin{tabular}{lccc}
1460	\toprule
1461	Model & $k$ & $\gamma$ & $k_{\mathrm{obs}}/k$ \\
1462	\midrule
1463	H0 (linear) & 6.1 & 2.08 & 2.6 \\
1464	H0$'$ (concave) & 4.9 & 1.87 & 3.2 \\
1465	H1 (step) & $\infty$ & --- & --- \\
1466	Observed & 15.7 & 2.08 & 1.0 \\
1467	\bottomrule
1468	\end{tabular}
1469	\end{table}
1470	
1471	\begin{figure}[t]
1472	\centering
1473	\includegraphics[width=\columnwidth]{figures/permg_power_curve.pdf}
1474	\caption{PermG power curves as a function of coupling strength $\beta$ for $T \in \{6, 8, 10, 15, 20\}$ (100 replications, 5{,}000 permutations, BH-FDR $q{=}0.05$). Power increases faster than $\sqrt{T}$, confirming that the theoretical $\sqrt{T}$ formula is a conservative lower bound. At $T{=}10$, 50\% power requires $\beta{\geq}2.0$; at $T{=}20$, this drops to $\beta{\approx}0.9$.}
1475	\label{fig:permg_power_curve}
1476	\end{figure}
1477	
1478	\FloatBarrier
1479	\section{T=20 Extension Results}
1480	\label{app:t20_comparison}
1481	
1482	At $\alpha{\geq}0.50$, PermG counts are consistent across $T{=}10$ and $T{=}20$ (6/8 at both), confirming signal-structure determination.
1483	At $\alpha{=}0.45$, the shift from 0/8 ($T{=}10$) to 5/8 ($T{=}20$) supports power-limited (Model~B) over structurally-undetectable (Model~A), lowering $\alpha_c$ below 0.45.
1484	The $\alpha{=}0.60$ dip persists at $T{=}20$ but dissolves at $T{=}25$ (5/8), confirming $\sqrt{T}$ power scaling eventually overcomes it.
1485	Directional selectivity is consistent: forward 6/8, reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ across all tested $T$.
1486	
1487	\paragraph{Full $T{=}25$ results.}
1488	Table~\ref{tab:t25_full} reports PermG forward detection counts at $T{=}25$ across contamination levels.
1489	Two key transitions emerge: (1)~$\alpha{=}0.45$ reaches 6/8 (dual-seed: s42 and s43 both 6/8), confirming that the blind-zone boundary has shifted below $\alpha{=}0.45$ at this observation length; (2)~the $\alpha{=}0.60$ sync-dip dissolves (5/8 at $T{=}25$ vs.\ 0/8 at $T{\leq}20$), with $K{\geq}3$ consensus reaching 6/8.
1490	The 6/8 detection ceiling at $\alpha{=}0.45$, $0.50$, $0.75$ matches the ceiling at shorter $T$, suggesting that 2/8 pairs are structurally non-detectable (likely MAUVE-related; MAUVE floor saturation at ${\sim}0.033$ produces near-constant series).
1491	
1492	\begin{table}[t]
1493	\centering
1494	\small
1495	\caption{PermG forward detection at $T{=}25$ (Pythia-410M, fp32). The $\alpha{=}0.45$ blind zone resolves and the $\alpha{=}0.60$ anomaly dissolves.}
1496	\label{tab:t25_full}
1497	\begin{tabular}{lccc}
1498	\toprule
1499	$\alpha$ & PermG fwd & $K{\geq}3$ & Note \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6394f1c2-2d08-4fe8-829a-3e157032e377",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "fe2bf909-4a61-459e-aed5-1dbca471a1fd",
  "sourceToolAssistantUUID": "6394f1c2-2d08-4fe8-829a-3e157032e377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T07:37:31.057Z_

<details open><summary>🔧 Tool call — Read · `toolu_0113m6GNWXL6dD4foazE71Cg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1500,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2bf909-4a61-459e-aed5-1dbca471a1fd",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuRLChQS57WarYJdGNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63e166f6-6965-4284-8db8-a251da5ef03d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018V3ShKwenJA46UdAJKqkAV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 35187,
      "cache_read_input_tokens": 39045,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 254,
          "cache_read_input_tokens": 39045,
          "cache_creation_input_tokens": 35187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35187,
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

_source line 23 · 2026-05-25T07:37:31.064Z_

<details><summary>↩ Tool result · `toolu_0113m6GNWXL6dD4foazE71Cg`</summary>

```text
1500	\midrule
1501	0.45 (s42) & 6/8 & 6/8 & blind$\to$detection \\
1502	0.45 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1503	0.50 (s42) & 6/8 & 6/8 & stable (matches $T{=}10$) \\
1504	0.60 (s42) & 5/8 & 6/8 & dip dissolves \\
1505	0.75 (s42) & 6/8 & 6/8 & stable \\
1506	0.75 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1507	\bottomrule
1508	\end{tabular}
1509	\end{table}
1510	
1511	\paragraph{$\alpha{=}0.25$ at extended $T$.}
1512	An unexpected result at $T{=}20$: PermG detects 3/8 at $\alpha{=}0.25$, where $T{=}10$ yields 0/8.
1513	This partial detection at very low contamination suggests that the blind zone is not absolute but power-limited: with sufficient observation length, even weak contamination signals may become detectable.
1514	However, 3/8 falls below the 6/8 reliability threshold we use for confirmed detection, and the result awaits multi-seed replication.
1515	
1516	\begin{figure}[t]
1517	\centering
1518	\includegraphics[width=\columnwidth]{figures/regime_map.pdf}
1519	\caption{Extended regime map including $T \in \{5, 10, 15, 20, 25\}$. The detection boundary shifts leftward with increasing $T$: $\alpha{=}0.45$ transitions from undetectable (0/8 at $T{\leq}10$) to reliable detection (6/8 at $T{=}15$). The $\alpha{=}0.60$ non-monotonic anomaly persists through $T{=}20$ but dissolves at $T{=}25$ (5/8).}
1520	\label{fig:regime_map_extended}
1521	\end{figure}
1522	
1523	\phantomsection\label{app:task_degradation}
1524	\paragraph{Task degradation.}
1525	End-of-training perplexity (gen~10, Pythia-410M, s42) improves at $\alpha{=}0.05$ (20.8 vs.\ 26.6 baseline, mild augmentation effect) but degrades sharply between $\alpha{=}0.50$ (31.3) and $0.52$ (41.1), aligning with PermG detection onset.
1526	
1527	\paragraph{Comprehensive cross-$T$ comparison.}
1528	Table~\ref{tab:cross_t_full} consolidates PermG forward detection across all tested observation windows, providing a complete view of the detection landscape evolution.
1529	
1530	\begin{table}[t]
1531	\centering
1532	\small
1533	\caption{PermG forward detection (/8 pairs) across $T$ and $\alpha$ (Pythia-410M, seed~42, fp32). Detection improves with $T$ at all contamination levels; the blind zone narrows monotonically.}
1534	\label{tab:cross_t_full}
1535	\begin{tabular}{lccccc}
1536	\toprule
1537	$\alpha$ & $T{=}5$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1538	\midrule
1539	0.25 & 0/8 & 0/8 & --- & 3/8 & --- \\
1540	0.45 & 0/8 & 0/8 & 6/8 & 5/8 & 6/8 \\
1541	0.50 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1542	0.60 & 0/8 & 0/8 & 0/8 & 0/8 & 5/8 \\
1543	0.75 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1544	1.00 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1545	\bottomrule
1546	\multicolumn{6}{l}{\footnotesize ---: not tested at this combination.}
1547	\end{tabular}
1548	\end{table}
1549	
1550	Key observations from Table~\ref{tab:cross_t_full}:
1551	\begin{enumerate}
1552	\item $T{=}5$ yields 0/8 across all $\alpha$ levels---insufficient degrees of freedom for PermG detection.
1553	\item The 6/8 ceiling at $\alpha \in \{0.50, 0.75, 1.0\}$ is invariant across $T{=}10$--$25$, confirming signal-structure determination.
1554	\item $\alpha{=}0.45$ traverses the full blind$\to$detection boundary: 0/8 at $T{\leq}10$, 6/8 at $T{=}15$, stable thereafter.
1555	\item $\alpha{=}0.60$ is the only condition requiring $T{=}25$ for detection, with all shorter windows yielding 0/8.
1556	\item $\alpha{=}0.25$ at $T{=}20$ (3/8) is the only sub-threshold result, suggesting that very low contamination may eventually become detectable with sufficiently long observation.
1557	\end{enumerate}
1558	
1559	\paragraph{Directional consistency.}
1560	Across all conditions with ${\geq}6/8$ forward detection, reverse detection remains at 0/8 (with the exception of Pythia-1.4B s43 at $\alpha{\geq}0.60$; \S\ref{app:scale_14b}).
1561	This directional selectivity confirms that the forward-only constraint is not an artifact of a single $T$ value but reflects the genuine temporal asymmetry of the entropy-diversity cascade.
1562	
1563	\paragraph{Detection efficiency metrics.}
1564	Table~\ref{tab:detection_efficiency} reports detection efficiency---defined as the fraction of FDR-significant pairs out of 8---across observation windows, providing a normalized summary of the detection landscape.
1565	
1566	\begin{table}[t]
1567	\centering
1568	\small
1569	\caption{Detection efficiency (fraction of pairs reaching FDR significance) across the $\alpha \times T$ grid (Pythia-410M, seed~42, fp32). Efficiency plateaus at 0.75 for above-onset conditions, indicating a structural detection ceiling at 6/8 pairs.}
1570	\label{tab:detection_efficiency}
1571	\begin{tabular}{lcccc}
1572	\toprule
1573	$\alpha$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1574	\midrule
1575	0.25 & 0.00 & --- & 0.375 & --- \\
1576	0.45 & 0.00 & 0.75 & 0.625 & 0.75 \\
1577	0.50 & 0.75 & 0.75 & 0.75 & 0.75 \\
1578	0.60 & 0.00 & 0.00 & 0.00 & 0.625 \\
1579	0.75 & 0.75 & 0.75 & 0.75 & 0.75 \\
1580	1.00 & 0.75 & 0.75 & 0.75 & 0.75 \\
1581	\bottomrule
1582	\multicolumn{5}{l}{\footnotesize ---: not tested at this combination.}
1583	\end{tabular}
1584	\end{table}
1585	
1586	The 0.75 plateau (6/8 pairs) is remarkably consistent across all conditions above the detection boundary, regardless of $T$ or $\alpha$.
1587	The 2/8 pairs that never reach significance involve MAUVE (floor saturation at ${\sim}0.033$ producing near-constant series) and perplexity (contemporaneous coupling; \S\ref{app:channel_effect_size}).
1588	This structural ceiling has practical implications: extending observation beyond $T{=}10$ at high contamination ($\alpha{\geq}0.50$) provides no additional detection power---the benefit of longer observation is concentrated in the boundary region ($\alpha \in [0.45, 0.60]$).
1589	
1590	\paragraph{Information gain per additional generation.}
1591	The marginal value of each additional generation varies by region.
1592	At $\alpha{=}0.45$, extending from $T{=}10$ to $T{=}15$ produces $+6$ newly significant pairs (information gain rate: $1.2$ pairs/gen); from $T{=}15$ to $T{=}20$, the rate drops to $-0.2$ pairs/gen (slight regression, likely noise).
1593	At $\alpha{=}0.60$ (sync-dip), the marginal value is zero through $T{=}20$ (0 new pairs across 10 additional generations) before producing $+5$ pairs in the $T{=}20{\to}25$ window (rate: $1.0$ pairs/gen).
1594	This non-uniform marginal return implies that a fixed-$T$ deployment strategy is suboptimal: adaptive monitoring that continues observation only when marginal information gain exceeds a threshold would reduce computational cost by 40--60\% without sacrificing detection reliability at high-$\alpha$ operating points.
1595	
1596	\subsection{Cross-Architecture Detection Table}
1597	\label{app:cross_arch_table}
1598	
1599	\begin{table}[t]
1600	\centering
1601	\small
1602	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
1603	\label{tab:generalization}
1604	\resizebox{\columnwidth}{!}{%
1605	\begin{tabular}{lrcl}
1606	\toprule
1607	Model & Params & Domain & PermG fwd \\
1608	\midrule
1609	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
1610	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
1611	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
1612	\addlinespace
1613	GPT-2-medium   & 345M & Wiki & \textbf{6/8}$^\S$ \\
1614	\addlinespace
1615	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
1616	\addlinespace
1617	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
1618	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
1619	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
1620	\addlinespace
1621	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
1622	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
1623	\bottomrule
1624	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dep.\ (s42: 2/8, s43: 6/8); 8-pair incl.\ MAUVE} \\
1625	\multicolumn{4}{l}{\footnotesize \phantom{$^\dagger$}(floor ${\sim}0.033$ at 1.4B; 6-pair in Table~\ref{tab:14b_phase}). $^*$bf16. $^\ddagger$ECE-only (ent.\ 0/4).} \\
1626	\multicolumn{4}{l}{\footnotesize $^\S$s42 fp32: 6/8 fwd, 0 rev; s43: 6/8 both; bf16: 0/8.} \\
1627	\multicolumn{4}{l}{\footnotesize 2 seeds each for Pythia-410M/1.4B, GPT-2, OPT, Pythia-1B C4.} \\
1628	\end{tabular}%
1629	}
1630	\end{table}
1631	
1632	\subsection{Cross-Architecture FPR Sensitivity}
1633	\label{app:cross_arch_fpr}
1634	
1635	GPT-2-medium null-condition PermG FPR is 50\% (6/12 pooled, 2~seeds), dramatically higher than Pythia-410M (6.7\%), driven by ${\sim}4{\times}$ stronger null drift (entropy $-20.5\%$ vs.\ $-4.9\%$; distinct-3 $-35.8\%$ vs.\ $-4.9\%$).
1636	$K{\geq}3$ consensus maintains 0\% FPR (0/12) on GPT-2-medium, providing some protection, but standalone PermG requires architecture-specific null calibration.
1637	
1638	The cross-architecture detection heatmap is shown in Figure~\ref{fig:cross_arch_heatmap} (main text).
1639	
1640	\paragraph{GPT-2-medium: precision sensitivity.}
1641	GPT-2-medium at fp32 (seed~42) achieves 6/8 forward detection with 0/8 reverse, matching the Pythia-410M profile.
1642	Switching to bf16 drops detection to 0/8 without changing the underlying collapse dynamics (distinct-1 drift: $-28.4\%$ in both precisions).
1643	The mechanism is quantization noise masking the entropy signal: bf16 entropy time series exhibit ${\sim}2{\times}$ higher inter-generation variance than fp32, pushing PermG $p$-values from $p{<}0.01$ (fp32) to $p{>}0.20$ (bf16).
1644	This failure mode is fully resolved by using fp32 precision; architectures with native bf16 training (e.g., SmolLM3) require separate investigation.
1645	
1646	\paragraph{GPT-2-medium: seed-specific bidirectionality.}
1647	At seed~43, GPT-2-medium detects 6/8 in \emph{both} forward and reverse directions, preventing directional assignment.
1648	This bidirectionality is absent at seed~42 (6/8 forward, 0/8 reverse) and does not appear for any Pythia seed, suggesting it reflects GPT-2's specific learned dynamics rather than a general property of iterative collapse.
1649	Possible explanations include: (1)~GPT-2's attention patterns create feedback loops where diversity changes instantaneously feed back into entropy through the generation process; (2)~seed~43 produces a collapse trajectory where the entropy-diversity lag is below PermG's temporal resolution.
1650	
1651	\paragraph{SmolLM3-3B: entropy decoupling.}
1652	SmolLM3-3B achieves only 3/8 detection, with all significant pairs involving ECE rather than entropy (entropy: 0/4; ECE: 3/4).
1653	This violates the cascade ordering assumption (Design Principle~\ref{thm:entropy_leads}): in 3/8 conditions, entropy does not monotonically decrease across generations, exhibiting a recovery pattern between gen-3 and gen-5 before resuming decline.
1654	The non-monotonic entropy trajectory breaks the mode amplification assumption underlying the cascade ordering, suggesting that SmolLM3's architecture (likely due to its different attention mechanism or training objective) produces qualitatively different collapse dynamics.
1655	
1656	\paragraph{Domain effects: WikiText vs.\ C4.}
1657	C4-domain experiments (Pythia-1B and Pythia-1.4B) achieve uniformly higher detection rates (8/8) than their WikiText counterparts (6/8 and 2--6/8 respectively).
1658	This domain advantage may reflect C4's greater vocabulary diversity (broader token distribution $\to$ larger effective support $S_\epsilon$), which increases the margin $\gamma$ and produces a cleaner cascade ordering.
1659	Alternatively, WikiText's specialized vocabulary (encyclopedia-style text) may create mode amplification patterns that compress the entropy-diversity lag.
1660	
1661	\paragraph{Deployment recommendations.}
1662	Based on the cross-architecture results, we recommend:
1663	\begin{enumerate}
1664	\item Run null-control calibration on each target architecture before deployment (GPT-2 FPR: 50\% without calibration).
1665	\item Use fp32 precision for the detection pipeline even if training uses mixed precision.
1666	\item Apply $K{\geq}3$ consensus to reduce architecture-specific FPR inflation (0/12 on GPT-2 vs.\ 50\% standalone PermG).
1667	\item Verify monotonic entropy decline on the target architecture; non-monotonic cases (SmolLM3-3B) require ECE-based detection.
1668	\end{enumerate}
1669	
1670	\FloatBarrier
1671	\section*{Reproducibility Details}
1672	\label{app:reproducibility}
1673	
1674	\paragraph{Compute requirements.}
1675	Each Pythia-410M experiment (10 generations $\times$ 5{,}000 training steps $+$ 5{,}000 generation samples) requires approximately 4 GPU-hours on a single NVIDIA A100 (40GB).
1676	The full experimental matrix (13 $\alpha$ levels $\times$ 4~seeds $\times$ 5 observation windows $+$ cross-architecture) required approximately 800 GPU-hours total.
1677	Statistical analysis (permutation testing, Shapley computation, specification curves) runs on CPU in under 2 hours for the complete dataset.
1678	
1679	\paragraph{Software versions.}
1680	PyTorch 2.1.0, Transformers 4.36.0, Python 3.10.
1681	All experiments use deterministic mode (\texttt{torch.use\_deterministic\_algorithms(True)}) except generation (stochastic sampling), ensuring that training trajectories are reproducible given the same seed.
1682	
1683	\paragraph{Key implementation choices.}
1684	Several implementation decisions affect reproducibility:
1685	\begin{itemize}
1686	\item \emph{Checkpoint strategy}: each generation fine-tunes from the previous generation's checkpoint (not from pretrained $M_0$), implementing true iterative collapse rather than independent fine-tuning.
1687	\item \emph{Generation prompts}: the same 5{,}000 prompt set (sampled once per experiment) is used across all generations within a run, controlling for prompt-selection variance.
1688	\item \emph{Metric computation}: all metrics are computed on the same held-out set across generations; distinct-$n$ uses the full 5{,}000 generated samples (not a subsample).
1689	\item \emph{Pipeline versioning}: results in this paper use the d120 pipeline version, which corrected FPR calibration errors present in earlier versions (d103, d061). The d120 recompilation changed PermG detection at $\alpha{=}0.60$ from 3/8 (v3) to 0/8 (v4, reported).
1690	\end{itemize}
1691	
1692	\paragraph{Data availability.}
1693	WikiText-103~\citep{merity2017pointer} is publicly available.
1694	Synthetic data generated during experiments is not released (too large), but the generation scripts are included in the code release.
1695	All statistical analysis code, including the five detection methods, MMCT consensus, and specification curve construction, will be released upon acceptance.
1696	
1697	\FloatBarrier
1698	\section*{Use of AI Assistants}
1699	\label{app:ai-assistants}
1700	
1701	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
1702	\begin{itemize}
1703	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
1704	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
1705	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
1706	\end{itemize}
1707	
1708	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63e166f6-6965-4284-8db8-a251da5ef03d",
  "isSidechain": true,
  "promptId": "704ecbd0-1db0-429a-8741-fa7757b3b520",
  "agentId": "a3a32e9faecbd9fb9",
  "type": "user",
  "uuid": "9b8c3fe5-0666-470d-af46-f19f4a32dd15",
  "sourceToolAssistantUUID": "63e166f6-6965-4284-8db8-a251da5ef03d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T07:37:51.302Z_

Perfect! Now I have all the information needed. Let me compile the structured report of all figures and tables in appendix.tex.

## Summary: All Figures and Tables in appendix.tex

Based on my search through the appendix.tex file, here is a complete structured list of all 52 occurrences of `\begin{figure}`, `\begin{figure*}`, `\begin{table}`, and `\begin{table*}` environments:

| # | Line | Type | Placement | Column Width | Caption / Label | ID |
|---|------|------|-----------|--------------|-----------------|-----|
| 1 | 18 | table | [t] | single | Per-architecture training hyperparameters | tab:arch_hyperparams |
| 2 | 56 | table | [t] | single | Metric drift (%, gen 0→10) | tab:drift_summary |
| 3 | 101 | table | [t] | single | Distinct-3 drift (%) across contamination levels | tab:distinct3_drift |
| 4 | 149 | figure | [t] | single | Detection stability as function of $T_{\min}$ | fig:window_sensitivity |
| 5 | 156 | table | [t] | single | Observation window sensitivity for Tier 3 consensus | tab:window_sensitivity |
| 6 | 190 | table | [t] | single | Specification curve summary (1,160 specifications) | tab:spec_curve |
| 7 | 275 | table | [t] | single | Sequential monitoring alarm timing | tab:sequential_timing |
| 8 | 366 | figure | [t] | single | $K\geq3$ consensus heatmap across $\alpha \times T$ grid | fig:consensus_heatmap |
| 9 | 373 | figure | [t] | single | MMCT operating characteristics as function of K | fig:mmct_k_operating |
| 10 | 403 | table | [t] | single | Methodological comparison of canary and monitoring analyses | tab:method-comparison |
| 11 | 464 | table | [t] | single | Failure mode taxonomy for non-confirming conditions | tab:failure_modes |
| 12 | 490 | table | [t] | single | Pythia-1.4B phase-diagram cells (fp32, PermG) | tab:14b_phase |
| 13 | 513 | figure | [t] | single | Pythia-1.4B phase diagram (PermG forward, 6-pair basis) | fig:14b_phase |
| 14 | 541 | table | [t] | single | Per-method FDR significance (/8 pairs) across levels | tab:dose_response_full |
| 15 | 583 | figure | [t] | single | Per-method FDR-significant pair counts (top) | fig:per_method_phase |
| 16 | 590 | figure | [t] | single | Per-method phase diagram (bottom, continued) | fig:per_method_phase |
| 17 | 668 | table | [t] | single | Null-control FPR by method | tab:null_fpr_methods |
| 18 | 696 | figure | [t] | single | Per-seed FPR distribution across detection methods | fig:fpr_sensitivity |
| 19 | 703 | table | [t] | single | Per-seed PermG FPR (8-pair basis, seeds 42–44) | tab:per_seed_fpr_8pair |
| 20 | 727 | table | [t] | single | Per-seed PermG FPR (6-pair basis, seeds 45–51) | tab:per_seed_fpr_6pair |
| 21 | 761 | table | [t] | single | Power cost of first-differencing under AR(1) DGP | tab:diff_power_cost |
| 22 | 789 | figure | [t] | single | Shapley value decomposition by method | fig:shapley_contribution |
| 23 | 796 | table | [t] | single | Shapley value decomposition (6-pair, MAUVE excluded) | tab:shapley_6pair |
| 24 | 822 | table | [t] | single | PermG combined Shapley under weighting schemes | tab:weight_robustness |
| 25 | 850 | table | [t] | single | Shapley contribution by canary→downstream pair | tab:shapley_per_pair |
| 26 | 887 | figure | [t] | single | Null-control FPR sensitivity across seeds | fig:fpr_sensitivity |
| 27 | 894 | figure | [t] | single | Null-control diagnostic: PermG p-value distributions | fig:null_fpr_diagnostic |
| 28 | 901 | figure | [t] | single | Bootstrap confidence intervals for FPR estimates | fig:bootstrap_fpr |
| 29 | 908 | table | [t] | single | Size and power under AR(1) DGP | tab:nonstationarity_sim |
| 30 | 933 | table | [t] | single | Empirical AR(1) coefficients (Pythia-410M, 4 seeds) | tab:empirical_ar1 |
| 31 | 952 | table | [t] | single | PermG power analysis: $\beta_{50}$ for 50% power | tab:beta50 |
| 32 | 998 | table | [t] | single | Sigmoid transition width (90% range) | tab:transition_width |
| 33 | 1021 | figure | [t] | single | First-differencing order selection diagnostic | fig:differencing_dmax |
| 34 | 1050 | figure | [t] | single | CUSUM sequential monitoring vs calibrated threshold | fig:cusum_monitoring |
| 35 | 1069 | table | [t] | single | Cross-correlation peak lag by channel | tab:lag_structure |
| 36 | 1094 | table | [t] | single | Fisher Z-transform comparison of channel correlations | tab:fisher_z |
| 37 | 1120 | figure | [t] | single | Channel effect size: Granger F-statistic comparison | fig:channel_effect |
| 38 | 1140 | table | [t] | single | Gaussian MI lower bound (blind zone) | tab:mi_blind |
| 39 | 1163 | table | [t] | single | Partial correlation controlling for generation | tab:partial_corr |
| 40 | 1184 | figure | [t] | single | Partial correlation scatter plots ($\alpha=0.75$) | fig:partial_correlation |
| 41 | 1191 | figure | [t] | single | Aggregated partial correlation analysis | fig:partial_corr_agg |
| 42 | 1215 | table | [t] | single | Degradation onset generation by metric and condition | tab:moment_cascade |
| 43 | 1242 | table | [t] | single | Cascade ordering validity as function of threshold | tab:onset_threshold_sensitivity |
| 44 | 1336 | table | [t] | single | ECE drift across contamination levels | tab:ece_drift |
| 45 | 1363 | table | [t] | single | Cascade onset generations (5% threshold) | tab:cascade_onset |
| 46 | 1413 | table | [t] | single | Margin consumption across contamination levels | tab:margin_consumption |
| 47 | 1454 | table | [t] | single | Onset steepness $k$ under different signal models | tab:steepness_comparison |
| 48 | 1471 | figure | [t] | single | PermG power curves as function of coupling strength | fig:permg_power_curve |
| 49 | 1492 | table | [t] | single | PermG forward detection at $T=25$ | tab:t25_full |
| 50 | 1516 | figure | [t] | single | Extended regime map for $T \in \{5,10,15,20,25\}$ | fig:regime_map_extended |
| 51 | 1530 | table | [t] | single | PermG forward detection across $T$ and $\alpha$ | tab:cross_t_full |
| 52 | 1566 | table | [t] | single | Detection efficiency across $\alpha \times T$ grid | tab:detection_efficiency |
| 53 | 1599 | table | [t] | single | Cross-architecture PermG forward detection | tab:generalization |

**Key Observations:**
- **Total environments**: 53 total (48 tables, 5 figures)
- **Placement option**: All use `[t]` (top placement)
- **Column width**: All are single-column (no `figure*` or `table*` environments)
- **Structure**: All follow the pattern `\begin{table}[t]` or `\begin{figure}[t]` with captions and labels immediately after or within the environment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b8c3fe5-0666-470d-af46-f19f4a32dd15",
  "isSidechain": true,
  "agentId": "a3a32e9faecbd9fb9",
  "requestId": "req_011CbNuRZ85cSRhpKA4LhVyQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e760825-d552-4c28-bba0-66c785d3bce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "36cb22b8-86b0-4028-b0c2-9fe60f48bf51",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "starry-kindling-newell",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WeDgrSScQkn3HfhWiupVhz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13762,
      "cache_read_input_tokens": 74232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13762,
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
