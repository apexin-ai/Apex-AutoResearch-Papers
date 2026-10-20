# Research conversation: Read the following 10 files and report their content (just the raw LaTeX content, no analysis needed): 1. /home/ubuntu/.

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-abf810ba317d15f6d.jsonl`
- **Structured JSON:** [`cdaa5f2b8e719fd3f2ad.json`](../../sessions/cd/cdaa5f2b8e719fd3f2ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-24T15:49:30.586Z_

Read the following 10 files and report their content (just the raw LaTeX content, no analysis needed):

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex
9. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex
10. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex

Report each file's full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "684d9a5a-5775-45de-9a46-19f911fd664a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T15:49:32.322Z_

I'll read all 10 files for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684d9a5a-5775-45de-9a46-19f911fd664a",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89d52011-4a56-4bca-878b-3cc0cf1fa66a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 3 · 2026-05-24T15:49:32.756Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VVsjC5H1br5LfKojNHcJWh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d52011-4a56-4bca-878b-3cc0cf1fa66a",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb00ac70-bd93-4608-93fa-b02e50b64f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 4 · 2026-05-24T15:49:32.768Z_

<details><summary>↩ Tool result · `toolu_01VVsjC5H1br5LfKojNHcJWh`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\small
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb00ac70-bd93-4608-93fa-b02e50b64f42",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "f8f1ed4f-924d-4b1d-8d1a-c182a217a1f1",
  "sourceToolAssistantUUID": "cb00ac70-bd93-4608-93fa-b02e50b64f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T15:49:32.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_016knngc5cW4YDqGE7za5n4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8f1ed4f-924d-4b1d-8d1a-c182a217a1f1",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b36d2726-a3e2-4a11-ba00-e38307dda76f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 6 · 2026-05-24T15:49:33.011Z_

<details><summary>↩ Tool result · `toolu_016knngc5cW4YDqGE7za5n4t`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\small
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b36d2726-a3e2-4a11-ba00-e38307dda76f",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "a2834e86-eeb8-46eb-822d-041095b4f588",
  "sourceToolAssistantUUID": "b36d2726-a3e2-4a11-ba00-e38307dda76f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T15:49:33.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_018t5TZtcQW7SQmhJhnw5UJv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2834e86-eeb8-46eb-822d-041095b4f588",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e461da8f-e454-4a0f-8263-6ee1abaec229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 8 · 2026-05-24T15:49:33.235Z_

<details><summary>↩ Tool result · `toolu_018t5TZtcQW7SQmhJhnw5UJv`</summary>

```text
1	% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison
2	% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39
3	% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)
4	\begin{table}[h]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\sim}39$ valid conversations in free-form generation mode.}
7	\label{tab:perturn-qwen}
8	\small
9	\begin{tabular}{@{}l ccccc@{}}
10	\toprule
11	\textbf{Configuration} & \textbf{Turn 1} & \textbf{Turn 2} & \textbf{Turn 3} & \textbf{Turn 4} & \textbf{Turn 5} \\
12	\midrule
13	Base         & .085 & .032 & .021 & .013 & .004 \\
14	ThreadGate   & .130 & .073 & .059 & .043 & .066 \\
15	PCGrad       & .090 & .038 & .028 & .029 & .027 \\
16	UG           & .113 & .056 & .033 & .020 & .016 \\
17	LoRA-only    & .107 & .059 & .030 & .049 & .040 \\
18	SS           & \textbf{.458} & \textbf{.381} & \textbf{.344} & \textbf{.370} & \textbf{.365} \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e461da8f-e454-4a0f-8263-6ee1abaec229",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "21f82628-d909-42c2-adcd-f71dbfe1da06",
  "sourceToolAssistantUUID": "e461da8f-e454-4a0f-8263-6ee1abaec229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T15:49:33.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NKDjQKjz2ZxuGUSzdb5u6x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f82628-d909-42c2-adcd-f71dbfe1da06",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d07a0b29-a028-422d-a4ba-b2e37d3eb053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 10 · 2026-05-24T15:49:33.391Z_

<details><summary>↩ Tool result · `toolu_01NKDjQKjz2ZxuGUSzdb5u6x`</summary>

```text
1	% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct
2	% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates
3	% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile
4	\begin{table}[h]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Llama-3.1-8B-Instruct.
7	(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).
8	(b)~Base model decay profile ($N{=}5$, $T{=}10$).}
9	\label{tab:perturn-llama}
10	\small
11	\begin{subtable}[t]{0.55\columnwidth}
12	\centering
13	\caption{$N{=}20$, $T{=}4$}
14	\begin{tabular}{@{}l cccc@{}}
15	\toprule
16	\textbf{Config.} & \textbf{T1} & \textbf{T2} & \textbf{T3} & \textbf{T4} \\
17	\midrule
18	Base      & .028 & .013 & .009 & .008 \\
19	TG        & .041 & .042 & .049 & .038 \\
20	LoRA-only & .033 & .049 & .025 & .031 \\
21	\bottomrule
22	\end{tabular}
23	\end{subtable}
24	\hfill
25	\begin{subtable}[t]{0.42\columnwidth}
26	\centering
27	\caption{Base decay ($N{=}5$, $T{=}10$)}
28	\begin{tabular}{@{}cc@{}}
29	\toprule
30	\textbf{Turn} & \textbf{GAR-ours} \\
31	\midrule
32	1  & .026 \\
33	2  & .018 \\
34	3  & .009 \\
35	4  & .006 \\
36	5  & .006 \\
37	6  & .004 \\
38	7  & .004 \\
39	8  & .004 \\
40	9  & .005 \\
41	10 & .003 \\
42	\bottomrule
43	\end{tabular}
44	\end{subtable}
45	\end{table}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d07a0b29-a028-422d-a4ba-b2e37d3eb053",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "ba216be1-62b1-4943-a1a6-f63c4b6aaed2",
  "sourceToolAssistantUUID": "d07a0b29-a028-422d-a4ba-b2e37d3eb053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T15:49:34.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_012zXqQbLForjLvQJsViBdmM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba216be1-62b1-4943-a1a6-f63c4b6aaed2",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0088d76-768c-4e67-8b2d-a48b749e4d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 12 · 2026-05-24T15:49:34.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VcarMxvVG8J5vvqudPWhyj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0088d76-768c-4e67-8b2d-a48b749e4d6e",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "844395ac-74bd-41bd-8df4-0337b00ac4de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 13 · 2026-05-24T15:49:34.121Z_

<details><summary>↩ Tool result · `toolu_012zXqQbLForjLvQJsViBdmM`</summary>

```text
1	% Dataset statistics table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K~\citep{ding2023enhancing}. All conversations contain $\geq 5$ assistant turns.}
6	\label{tab:dataset_stats}
7	\begin{tabular}{@{}lr@{}}
8	\toprule
9	\textbf{Statistic} & \textbf{Value} \\
10	\midrule
11	\multicolumn{2}{@{}l}{\textit{Source}} \\
12	\quad Dataset & UltraChat-200K (\texttt{train\_sft}) \\
13	\quad Total conversations & 207{,}865 \\
14	\quad After filtering ($\geq 5$ asst.\ turns) & 17{,}302 \\
15	\midrule
16	\multicolumn{2}{@{}l}{\textit{Splits}} \\
17	\quad Training set & 8{,}000 \\
18	\quad Held-out eval (OOD) & 50 \\
19	\quad IID eval (GAR diagnostic) & 50 \\
20	\quad Large eval (instruction retention) & 200 \\
21	\midrule
22	\multicolumn{2}{@{}l}{\textit{Conversation structure}} \\
23	\quad Avg.\ assistant turns & 5.6 \\
24	\quad Min / Max assistant turns & 5 / 7 \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0088d76-768c-4e67-8b2d-a48b749e4d6e",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "b23dadb0-506f-432c-9f34-1cb808cdb698",
  "sourceToolAssistantUUID": "d0088d76-768c-4e67-8b2d-a48b749e4d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T15:49:34.123Z_

<details><summary>↩ Tool result · `toolu_01VcarMxvVG8J5vvqudPWhyj`</summary>

```text
1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "844395ac-74bd-41bd-8df4-0337b00ac4de",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "a662c99b-7f88-40a8-9492-2d854389fcf2",
  "sourceToolAssistantUUID": "844395ac-74bd-41bd-8df4-0337b00ac4de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T15:49:34.483Z_

<details open><summary>🔧 Tool call — Read · `toolu_014yqyruhZaiHcLQYKbP3UcQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a662c99b-7f88-40a8-9492-2d854389fcf2",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a0f9630-24b6-4b65-a665-696fe7429cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 16 · 2026-05-24T15:49:34.495Z_

<details><summary>↩ Tool result · `toolu_014yqyruhZaiHcLQYKbP3UcQ`</summary>

```text
1	% MMLU per-category quality preservation table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{MMLU accuracy (\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\Delta$ denotes deviation from Base.}
6	\label{tab:mmlu_detail}
7	\begin{tabular}{@{}l cccccc@{}}
8	\toprule
9	\textbf{Category} & \textbf{Base} & \textbf{TG} & \textbf{PCGrad} & \textbf{SS} & \textbf{LoRA-only} & \textbf{UG} \\
10	\midrule
11	STEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\
12	Social Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\
13	Humanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\
14	Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
15	\midrule
16	\textbf{Overall} & \textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\
17	$\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a0f9630-24b6-4b65-a665-696fe7429cbd",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "5019531f-b61f-48e2-b768-2397eadeb9a0",
  "sourceToolAssistantUUID": "9a0f9630-24b6-4b65-a665-696fe7429cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T15:49:34.534Z_

<details open><summary>🔧 Tool call — Read · `toolu_019P56UBpQ5VLadDSdPvGBzK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5019531f-b61f-48e2-b768-2397eadeb9a0",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "daae808a-691c-4853-ad96-b5bc587652ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 18 · 2026-05-24T15:49:34.547Z_

<details><summary>↩ Tool result · `toolu_019P56UBpQ5VLadDSdPvGBzK`</summary>

```text
1	% Qwen2.5-1.5B cross-scale results
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\% relative drop). Phase~2 shows TG improves AR at $\beta=0$ (unamplified, $p{=}0.005$) and $\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}
6	\label{tab:qwen15b_results}
7	\begin{tabular}{@{}ll cc c@{}}
8	\toprule
9	\textbf{Phase} & \textbf{Metric} & \textbf{Base} & \textbf{TG} & \textbf{$p$-value} \\
10	\midrule
11	\multicolumn{5}{@{}l}{\textit{Phase 1: GAR diagnostic}} \\
12	\quad & Turn-1 GAR & 0.0336 & --- & --- \\
13	\quad & Mid-turn GAR & 0.0068 & --- & --- \\
14	\quad & Relative drop & 79.8\% & --- & --- \\
15	\midrule
16	\multicolumn{5}{@{}l}{\textit{Phase 2: TG training ($\beta$-amplified AR)}} \\
17	\quad & AR @ $\beta{=}0$ & 0.0167 {\scriptsize$\pm$0.005} & \textbf{0.0233} {\scriptsize$\pm$0.006} & 0.005$^{**}$ \\
18	\quad & AR @ $\beta{=}3$ & 0.1202 {\scriptsize$\pm$0.032} & 0.1143 {\scriptsize$\pm$0.019} & 0.815 \\
19	\quad & AR @ $\beta{=}5$ & 0.6571 {\scriptsize$\pm$0.020} & \textbf{0.7150} {\scriptsize$\pm$0.017} & $<$0.001$^{***}$ \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1mm}
23	\begin{flushleft}
24	\scriptsize
25	$\pm$ values are 95\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\beta{=}0$), $r{=}0.749$ ($\beta{=}5$).
26	\end{flushleft}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daae808a-691c-4853-ad96-b5bc587652ce",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "fd6e2b40-c0ac-439f-a474-947e36359f8e",
  "sourceToolAssistantUUID": "daae808a-691c-4853-ad96-b5bc587652ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T15:49:36.664Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ew9sbkg64JXePYDkehi17`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6e2b40-c0ac-439f-a474-947e36359f8e",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d59c5a1e-5ab1-4c5e-92a7-19cf8677d8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 20 · 2026-05-24T15:49:36.669Z_

<details><summary>↩ Tool result · `toolu_018ew9sbkg64JXePYDkehi17`</summary>

```text
1	% Item 9: Statistical tests summary table
2	% Wilcoxon signed-rank tests for per-dialogue GAR + McNemar for instruction retention
3	\begin{table*}[t]
4	\centering
5	\caption{Summary of statistical significance tests.
6	  Wilcoxon signed-rank tests compare per-dialogue GAR across training configurations ($N\!=\!39$);
7	  McNemar's test assesses instruction-following retention under steering ($N\!=\!54$ paired instances).
8	  Bootstrap 95\% CIs from 10{,}000 resamples.
9	  Significance: $^{***}\!p<.001$, $^{**}\!p<.01$, $^{*}\!p<.05$.}
10	\label{tab:statistical_tests}
11	\small
12	\setlength{\tabcolsep}{4pt}
13	\begin{tabular}{@{}llcrrccl@{}}
14	\toprule
15	$\beta$ & Comparison & Test & Stat. & $p$ & $r$ & $\overline{\mathrm{GAR}}$\;[95\% CI] & Sig. \\
16	\midrule
17	\multirow{4}{*}{0.0}
18	 & TG vs Base    & Wilcoxon & $W\!=\!31$  & ${<}.001$ & .802 & .064\,[.041,\,.091]\;vs\;.019\,[.014,\,.024] & $^{***}$ \\
19	 & TG vs LoRA    & Wilcoxon & $W\!=\!187$ & .004      & .454 & .064\,[.041,\,.091]\;vs\;.037\,[.027,\,.050] & $^{**}$  \\
20	 & SS vs TG      & Wilcoxon & $W\!=\!1$   & ${<}.001$ & .869 & .347\,[.327,\,.366]\;vs\;.064\,[.041,\,.091] & $^{***}$ \\
21	 & PCGrad vs TG  & Wilcoxon & $W\!=\!176$ & .002      & .478 & .030\,[.023,\,.038]\;vs\;.064\,[.041,\,.091] & $^{**}$  \\
22	\midrule
23	\multirow{4}{*}{3.0}
24	 & TG vs Base    & Wilcoxon & $W\!=\!242$ & .039 & .331 & .556\,[.538,\,.575]\;vs\;.531\,[.514,\,.550] & $^{*}$  \\
25	 & TG vs LoRA    & Wilcoxon & $W\!=\!376$ & .852 & .031 & .556\,[.538,\,.575]\;vs\;.560\,[.541,\,.581] & n.s.    \\
26	 & SS vs TG      & Wilcoxon & $W\!=\!207$ & .010 & .409 & .593\,[.574,\,.613]\;vs\;.556\,[.538,\,.575] & $^{**}$ \\
27	 & PCGrad vs TG  & Wilcoxon & $W\!=\!368$ & .767 & .049 & .559\,[.543,\,.576]\;vs\;.556\,[.538,\,.575] & n.s.    \\
28	\midrule
29	\multirow{4}{*}{5.0}
30	 & TG vs Base    & Wilcoxon & $W\!=\!251$ & .084 & .281 & .727\,[.708,\,.747]\;vs\;.704\,[.679,\,.730] & n.s. \\
31	 & TG vs LoRA    & Wilcoxon & $W\!=\!277$ & .180 & .220 & .727\,[.708,\,.747]\;vs\;.708\,[.687,\,.729] & n.s. \\
32	 & SS vs TG      & Wilcoxon & $W\!=\!314$ & .421 & .133 & .717\,[.696,\,.738]\;vs\;.727\,[.708,\,.747] & n.s. \\
33	 & PCGrad vs TG  & Wilcoxon & $W\!=\!266$ & .133 & .246 & .708\,[.690,\,.727]\;vs\;.727\,[.708,\,.747] & n.s. \\
34	\midrule
35	\multicolumn{8}{@{}l}{\textit{Instruction-following retention} ($\beta\!=\!0 \to 3$, ThreadGate only)} \\[2pt]
36	 & $\beta\!=\!0$ vs $\beta\!=\!3$ & McNemar & $\chi^2\!=\!3.13$ & .077 & $.200^{\dagger}$ & Rate: .759\;vs\;.870\;($N\!=\!54$) & n.s.$^{\ddagger}$ \\
37	\bottomrule
38	\end{tabular}
39	\\[4pt]
40	{\footnotesize
41	$^{\dagger}$\,Point-biserial $r$; associated $p=.007$ (significant).
42	$^{\ddagger}$\,Marginal by McNemar ($p=.077$); significant by point-biserial correlation.
43	}
44	\end{table*}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d59c5a1e-5ab1-4c5e-92a7-19cf8677d8c9",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "2eafb095-80dd-4bab-81ac-09f96caac011",
  "sourceToolAssistantUUID": "d59c5a1e-5ab1-4c5e-92a7-19cf8677d8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T15:49:36.956Z_

<details open><summary>🔧 Tool call — Read · `toolu_012pa5AbC7yWw2GyE7WynuCG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eafb095-80dd-4bab-81ac-09f96caac011",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf8ePE3exmqyDeKR21E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21d1866b-f1d7-4d51-ae75-acad60c1073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q2nEbZL13SmufDz78JTnEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 46910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46910,
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

_source line 22 · 2026-05-24T15:49:36.962Z_

<details><summary>↩ Tool result · `toolu_012pa5AbC7yWw2GyE7WynuCG`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	\begin{table}[h]
6	\centering
7	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
8	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
9	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$.}
10	\label{tab:crossmodel-detail}
11	\small
12	\begin{tabular}{@{}ll ccccc@{}}
13	\toprule
14	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
15	\midrule
16	\multirow{3}{*}{Qwen-7B}
17	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
18	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
19	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
20	\midrule
21	\multirow{3}{*}{Llama-8B}
22	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
23	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
24	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21d1866b-f1d7-4d51-ae75-acad60c1073c",
  "isSidechain": true,
  "promptId": "8d54bc45-f36c-4cf2-8730-6151fd2264e8",
  "agentId": "abf810ba317d15f6d",
  "type": "user",
  "uuid": "9ce9bccf-b472-4f7b-9d61-dadbc54d9e83",
  "sourceToolAssistantUUID": "21d1866b-f1d7-4d51-ae75-acad60c1073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T15:49:46.657Z_

## File Contents Report

**File 1: tab_perseed_ss.tex**
Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct with metrics GAR-ours, GAR-Dongre, and PPL across three seeds (42, 123, 456) in both teacher-forced and autoregressive (AR with β=0,3,5) modes.

**File 2: tab_perseed_tg.tex**
Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct with two seeds (42, 123) showing GAR-ours, GAR-Dongre, PPL metrics in TF and AR modes, plus derived gap ratio metric.

**File 3: tab_perturn_qwen.tex**
Per-turn autoregressive GAR-ours (β=0) comparison across six training configurations (Base, ThreadGate, PCGrad, UG, LoRA-only, SS) on Qwen2.5-7B-Instruct for turns 1-5.

**File 4: tab_perturn_llama.tex**
Per-turn autoregressive GAR-ours (β=0) on Llama-3.1-8B-Instruct with two panels: (a) three-way comparison (Base, TG, LoRA-only) with N=20, T=4; (b) Base decay profile with N=5, T=10.

**File 5: tab_dataset_stats.tex**
Dataset statistics table showing UltraChat-200K source data (207,865 total conversations, 17,302 after filtering for ≥5 assistant turns), training/eval splits, and conversation structure metrics.

**File 6: tab_gar_robustness.tex**
GAR robustness evaluation across four token selection strategies (Last, All, First, Goal-only) and three conditions (Base, TG, SS), showing Turn-1 GAR, Mid-turn GAR, and gap ratio metrics.

**File 7: tab_mmlu_detail.tex**
MMLU accuracy (%) by category (STEM, Social Sciences, Humanities, Other) across training conditions on Qwen2.5-7B-Instruct with baseline and delta from base model.

**File 8: tab_qwen15b_results.tex**
Cross-scale validation on Qwen2.5-1.5B-Instruct with Phase 1 GAR diagnostic (79.8% relative drop) and Phase 2 TG training results at β=0, 3, 5 with p-values and 95% CI.

**File 9: tab_statistical_tests.tex**
Summary of statistical significance tests: Wilcoxon signed-rank tests for per-dialogue GAR comparisons (N=39) and McNemar's test for instruction-following retention (N=54), with effect sizes and 95% CIs.

**File 10: tab_crossmodel_detail.tex**
Cross-model comparison of Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct with TF/AR GAR, perplexity, and gap ratio metrics across Base, ThreadGate, and LoRA-only conditions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce9bccf-b472-4f7b-9d61-dadbc54d9e83",
  "isSidechain": true,
  "agentId": "abf810ba317d15f6d",
  "requestId": "req_011CbMf97yQnop89M1bSREKJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30b3c572-03d8-4b5f-bb7f-8cbc25369315",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "34f38b66-6876-4bf8-b07e-de116eb64274",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "elegant-wobbling-wilkes",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XKWT7B91zfha94JY9N47fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9575,
      "cache_read_input_tokens": 46910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9575,
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
