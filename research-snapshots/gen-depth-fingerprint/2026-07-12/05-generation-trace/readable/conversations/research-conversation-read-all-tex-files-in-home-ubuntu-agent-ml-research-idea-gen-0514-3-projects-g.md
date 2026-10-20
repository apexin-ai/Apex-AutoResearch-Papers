# Research conversation: Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 82
- **Recorded user turns:** 1
- **Tool calls:** 39
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a476781bbc33ad56b.jsonl`
- **Structured JSON:** [`140cda20a39884890f25.json`](../../sessions/14/140cda20a39884890f25.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

82 recorded events

### User

_source line 1 · 2026-05-20T05:01:27.771Z_

Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like "cross-model", "temperature", "prompt type", "human edit", "domain", "LoRA", "QLoRA", "seed", "transfer", "convergence", "ablation", etc.), table data, and figure references.

Here is the full list of tex files to read:
- table2.tex, table1.tex, table4.tex
- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex
- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex
- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex
- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex
- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex
- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex
- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex
- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex
- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex
- appendix_cross_model_detail.tex, method.tex

For each file, output:
1. File name
2. Any exp_id strings found (like "eval-xxx", "plan-xxx", etc.)
3. Key metric numbers mentioned
4. Experiment-descriptive keywords/phrases used
5. What tables/figures are defined

Be thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "c68d5bb0-8cfd-4579-9c09-350fe087615d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T05:01:27.776Z_

```json
{
  "parentUuid": "c68d5bb0-8cfd-4579-9c09-350fe087615d",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "321b6b83-ce26-4344-b8c3-c0a3e3c10f80",
  "timestamp": "2026-05-20T05:01:27.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-20T05:01:30.601Z_



I'll read all the .tex files systematically. Let me start by reading them in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321b6b83-ce26-4344-b8c3-c0a3e3c10f80",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e5c8219-41e6-46f9-9b16-70f35ed3edfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 4 · 2026-05-20T05:01:31.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S1UmK7ok5gVMv9f82FzErt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e5c8219-41e6-46f9-9b16-70f35ed3edfd",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea3bbfb6-e4bb-4cd4-ac4c-492616ab1679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 5 · 2026-05-20T05:01:31.554Z_

<details><summary>↩ Tool result · `toolu_01S1UmK7ok5gVMv9f82FzErt`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{lp{3.2cm}ccc}
5	\toprule
6	\textbf{Feature Set} & \textbf{Features} & \textbf{LOGO F1} & \textbf{95\% CI} & \textbf{McNemar $p$} \\
7	\midrule
8	Full (7 features) & all & 0.773 & --- & --- \\
9	Surface only (2)  & TTR, hapax\_ratio & 0.688 & --- & $<$ 0.001 \\
10	Reference only (5) & entropy\_mean/std/min/max, tail\_decay & 0.713 & --- & $<$ 0.001 \\
11	\bottomrule
12	\end{tabular}
13	\caption{Feature group ablation and complementarity (8-gen 10-fold CV).
14	Both subsets significantly underperform the full set (+8.5\,pp, +5.9\,pp).
15	Permutation importance: \texttt{hapax\_ratio} (0.269) $>$ \texttt{entropy\_mean} (0.164) $>$ \texttt{ttr} (0.159).}
16	\label{tab:feature-ablation}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3bbfb6-e4bb-4cd4-ac4c-492616ab1679",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "65b6dad3-c655-49c4-a5d6-5ed0168bc15b",
  "sourceToolAssistantUUID": "ea3bbfb6-e4bb-4cd4-ac4c-492616ab1679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T05:01:32.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JgfcoDqhSBwyKg1593FS4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65b6dad3-c655-49c4-a5d6-5ed0168bc15b",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14fefec8-07be-4cf8-9631-33dd4ed2bebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 7 · 2026-05-20T05:01:32.568Z_

<details><summary>↩ Tool result · `toolu_01JgfcoDqhSBwyKg1593FS4t`</summary>

```text
1	%% NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.
2	\begin{table}[t]
3	\centering
4	\small
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Held-out Generator} & \textbf{Family} & \textbf{Params} & \textbf{Macro-F1} & \textbf{95\% CI} \\
8	\midrule
9	Pythia-2.8B   & Pythia  & 2.8B & ---   & --- \\
10	Pythia-1B     & Pythia  & 1.0B & 0.806 & --- \\
11	Qwen3-1.7B   & Qwen    & 1.7B & ---   & --- \\
12	Llama-3.2-3B & Llama   & 3.2B & ---   & --- \\
13	OLMo-2-1B    & OLMo    & 1.0B & ---   & --- \\
14	Qwen3-8B     & Qwen    & 8.0B & ---   & --- \\
15	Qwen3-0.6B   & Qwen    & 0.6B & ---   & --- \\
16	Mistral-7B   & Mistral & 7.0B & 0.681 & --- \\
17	\midrule
18	\textbf{Average (8-gen)} & & & \textbf{0.762} & [0.758, 0.766] \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-generator-out (LOGO) depth classification results (3-class).
22	Each row holds out one generator for testing and trains on the remaining seven.}
23	\label{tab:logo-results}
24	\end{table}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14fefec8-07be-4cf8-9631-33dd4ed2bebb",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "3576a41a-3842-4ed3-85a6-dd21cf24752a",
  "sourceToolAssistantUUID": "14fefec8-07be-4cf8-9631-33dd4ed2bebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T05:01:32.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_012S35Jvkwf6cGojQRYTKvGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3576a41a-3842-4ed3-85a6-dd21cf24752a",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0726cd92-e0ab-449d-8344-1b2ec0560bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 9 · 2026-05-20T05:01:32.890Z_

<details><summary>↩ Tool result · `toolu_012S35Jvkwf6cGojQRYTKvGy`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\footnotesize
4	\resizebox{\linewidth}{!}{%
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Reference} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Ent.\ Drift} \\
8	\midrule
9	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
10	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
11	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
12	\bottomrule
13	\end{tabular}}
14	\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}
15	\label{tab:cross-ref}
16	\end{table}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0726cd92-e0ab-449d-8344-1b2ec0560bae",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "eae938db-05f8-45c0-b34d-acafff211a16",
  "sourceToolAssistantUUID": "0726cd92-e0ab-449d-8344-1b2ec0560bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T05:01:32.922Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FFAKHFM6wcp3zXWuhatesh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae938db-05f8-45c0-b34d-acafff211a16",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87871f22-a40f-44a5-be89-c5a6b8067f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 11 · 2026-05-20T05:01:32.933Z_

<details><summary>↩ Tool result · `toolu_01FFAKHFM6wcp3zXWuhatesh`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +11.6\,pp improvement over the XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87871f22-a40f-44a5-be89-c5a6b8067f92",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "db0c599f-8699-4ef9-9dcd-aa09aafc3c67",
  "sourceToolAssistantUUID": "87871f22-a40f-44a5-be89-c5a6b8067f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T05:01:33.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FetqKQt8gQA8CZahhsbWSb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db0c599f-8699-4ef9-9dcd-aa09aafc3c67",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b805d7f8-56ff-439e-8571-517305d44ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 13 · 2026-05-20T05:01:33.340Z_

<details><summary>↩ Tool result · `toolu_01FetqKQt8gQA8CZahhsbWSb`</summary>

```text
1	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
9	\midrule
10	entropy\_max    & 0.774 & $-$1.50\,pp \\
11	entropy\_mean   & 0.783 & $-$0.63\,pp \\
12	ttr             & 0.784 & $-$0.55\,pp \\
13	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
14	tail\_decay     & 0.786 & $-$0.33\,pp \\
15	entropy\_std    & 0.786 & $-$0.29\,pp \\
16	entropy\_min    & 0.789 & $+$0.01\,pp \\
17	\midrule
18	Full (7 features) & 0.789 & --- \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
22	\label{tab:lofo}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal (capturing the most surprising token under the reference model) that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, which confirms that the 7-feature design is not over-specified.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b805d7f8-56ff-439e-8571-517305d44ddb",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "615998e5-a67c-4d25-9e8e-166ce8a326d8",
  "sourceToolAssistantUUID": "b805d7f8-56ff-439e-8571-517305d44ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T05:01:33.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_011pbquQHp1i4KmHAVRSPbth`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "615998e5-a67c-4d25-9e8e-166ce8a326d8",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f032cb61-e113-450c-8ed6-8d1311deb837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 15 · 2026-05-20T05:01:33.782Z_

<details><summary>↩ Tool result · `toolu_011pbquQHp1i4KmHAVRSPbth`</summary>

```text
1	% Appendix — Length Confound Analysis
2	% Data source: 8-generator LOGO corpus (37,058 samples)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We investigate with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	Spearman rank correlation between word count and generation depth is weak across all eight generators ($|\rho| < 0.14$); depth does not systematically shorten or lengthen text in our corpus.
11	
12	\paragraph{(b) Length--feature correlations.}
13	While length--depth correlation is weak, individual features show moderate length dependence:
14	tail\_decay ($|\rho| = 0.38$), hapax\_ratio ($|\rho| = 0.30$), and TTR ($|\rho| = 0.29$).
15	Reference-model features show weaker length correlations (entropy\_mean $|\rho| = 0.09$, entropy\_std $|\rho| = 0.18$).
16	This motivates the length-matched evaluation below: if length mediates some depth--feature association, controlling for length will reduce classification performance.
17	
18	\paragraph{(c) Length-matched classification.}
19	We subsample the dataset so that word-count distributions are equalized across depth classes (gen-0\,/\,gen-1\,/\,gen-2+), then retrain the binary XGBoost classifier under pooled LOGO (8-fold).
20	Length-matched binary F1\,=\,0.724, down from 0.770 on the unmatched set ($\Delta$\,=\,$-$0.046).
21	To distinguish this from a sample-size effect, we run a random-subsample control at equal $N$ without length matching: F1\,=\,0.767, which confirms that the 0.046 drop reflects genuine length deconfounding rather than reduced data.
22	
23	\paragraph{Conclusion.}
24	Length accounts for approximately 6\% of discriminative performance ($\Delta$\,=\,0.046 out of 0.770).
25	The majority of the depth signal is length-independent: length-matched F1 (0.724) remains far above chance and significantly above all individual detection baselines (\S\ref{sec:results-baselines}).
26	Surface features (TTR, hapax\_ratio) partially co-vary with length, but their depth-discriminative contribution persists after length control, consistent with generation-induced vocabulary compression operating independently of text truncation.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f032cb61-e113-450c-8ed6-8d1311deb837",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "800797db-1df0-492d-9ab6-5f893c12f25a",
  "sourceToolAssistantUUID": "f032cb61-e113-450c-8ed6-8d1311deb837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T05:01:34.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Nud4FbAK4JvcPmLyddqpa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800797db-1df0-492d-9ab6-5f893c12f25a",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a727b8b-084f-4614-8e26-e1e62abb9cc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 17 · 2026-05-20T05:01:34.745Z_

<details><summary>↩ Tool result · `toolu_017Nud4FbAK4JvcPmLyddqpa`</summary>

```text
1	\section{Qualitative Examples}
2	\label{app:qualitative}
3	
4	Table~\ref{tab:qualitative-text} presents an example generation chain from seed 120 (Pythia-2.8B, continuation prompt), illustrating how text evolves across recursive generation steps.
5	Table~\ref{tab:qualitative-features} reports the corresponding 7-feature values. Central-tendency features ($\bar{H}$, TTR, hapax ratio) drift monotonically while shape features ($H_{\max}$, tail decay) remain near-stationary, consistent with the differential depth response pattern.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Example text chain from seed 120 (Pythia-2.8B, continuation prompt). Gen-0 is the original Wikipedia passage; gen-1 and gen-2 are successive LLM continuations. Text is truncated for space.}
10	\label{tab:qualitative-text}
11	\small
12	\begin{tabular}{p{0.93\columnwidth}}
13	\toprule
14	\textbf{Gen-0 (Wikipedia seed)} \\
15	\midrule
16	Aquarius is an equatorial constellation of the zodiac, between Capricornus and Pisces. Its name is Latin for ``water-carrier'' or ``cup-carrier''. Aquarius is one of the oldest of the recognized constellations along the zodiac (the Sun's apparent path). It was one of the 48 constellations listed by the 2nd century astronomer Ptolemy, and it remains one of the 88 modern constellations. It is found in a region often called the Sea due to its profusion of constellations with watery associations such as Cetus the whale, Pisces the fish, and Eridanus the river. [\ldots] \\
17	\midrule
18	\textbf{Gen-1} \\
19	\midrule
20	Babylonian astrology and was also depicted in ancient Egyptian art. In Greek mythology, Aquarius is the son of Poseidon and Gaia. He is also the god of the sea and the sky, the god of travelers, and the guardian of the underworld. In Roman mythology, Aquarius is the son of Saturn and the nymph Egeria, and the god of the sea. In Jewish mythology, Aquarius is the son of the God of the Air and the Goddess of the Moon. In Chinese mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
21	\midrule
22	\textbf{Gen-2} \\
23	\midrule
24	God of the Sky and the Goddess of the Earth. In the ancient Greek mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the Hindu mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the ancient Egyptian mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
29	\begin{table}[t]
30	\centering
31	\caption{Feature values for the chain in Table~\ref{tab:qualitative-text}. Drifting features ($\bar{H}$, TTR, hapax) show monotonic degradation; shape features ($H_{\max}$, tail decay) remain stable (range $<$2\% and $<$4\% respectively).}
32	\label{tab:qualitative-features}
33	\small
34	\begin{tabular}{lrrr}
35	\toprule
36	Feature & Gen-0 & Gen-1 & Gen-2 \\
37	\midrule
38	$\bar{H}$ (entropy mean) & 2.720 & 2.206 & 0.780 \\
39	$\sigma_H$ (entropy std) & 1.772 & 1.816 & 1.517 \\
40	$H_{\min}$ (entropy min) & 0.002 & 0.005 & 0.000 \\
41	$H_{\max}$ (entropy max) & 7.000 & 7.016 & 6.926 \\
42	tail decay & $-$0.00227 & $-$0.00231 & $-$0.00223 \\
43	TTR & 0.659 & 0.272 & 0.081 \\
44	hapax ratio & 0.561 & 0.183 & 0.005 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a727b8b-084f-4614-8e26-e1e62abb9cc4",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "b3f3b991-b7d5-433d-8f54-886ed0e63d70",
  "sourceToolAssistantUUID": "2a727b8b-084f-4614-8e26-e1e62abb9cc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T05:01:35.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C7xFiDXKRkd4yxsuJKrtYS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f3b991-b7d5-433d-8f54-886ed0e63d70",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f971852-2773-474a-bc97-1742eddcfb80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 19 · 2026-05-20T05:01:35.483Z_

<details><summary>↩ Tool result · `toolu_01C7xFiDXKRkd4yxsuJKrtYS`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f971852-2773-474a-bc97-1742eddcfb80",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "6b3a9d55-df3c-440e-a376-8fcd3f3ea540",
  "sourceToolAssistantUUID": "8f971852-2773-474a-bc97-1742eddcfb80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T05:01:35.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DpjgyTReg6uay33x8MnVGj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b3a9d55-df3c-440e-a376-8fcd3f3ea540",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d87dced0-6c6a-4013-be1c-a323624047ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 21 · 2026-05-20T05:01:35.712Z_

<details><summary>↩ Tool result · `toolu_01DpjgyTReg6uay33x8MnVGj`</summary>

```text
1	We evaluate depth profiling under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
2	
3	\paragraph{Within-prompt-type classification.}
4	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while near-stationary features (entropy max, tail decay) change by less than 5\%.
5	
6	\paragraph{Cross-prompt-type transfer (LOPTO).}
7	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, which confirms that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d87dced0-6c6a-4013-be1c-a323624047ae",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "04bf4819-f9bb-463c-a4c0-19cd4936cd0b",
  "sourceToolAssistantUUID": "d87dced0-6c6a-4013-be1c-a323624047ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T05:01:36.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VTkWt8c9hqyAEygunAs49m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04bf4819-f9bb-463c-a4c0-19cd4936cd0b",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEUm5RdLQebLjagepUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb654b47-8415-41b6-a174-7ca5d2486883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 802,
          "cache_read_input_tokens": 9196,
          "cache_creation_input_tokens": 7086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7086,
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

_source line 23 · 2026-05-20T05:01:36.213Z_

<details><summary>↩ Tool result · `toolu_01VTkWt8c9hqyAEygunAs49m`</summary>

```text
1	We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Robustness to random word replacement under 8-gen LOGO evaluation (binary: gen-1 vs.\ gen-2+). Bootstrap 95\% CIs on binary F1 ($n$\,=\,1000).}
8	\label{tab:human-edit}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	\textbf{Perturbation rate} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
13	\midrule
14	0\% (baseline) & 0.695 & [0.680, 0.710] & 0.737 \\
15	5\%            & 0.650 & [0.635, 0.666] & 0.641 \\
16	10\%           & 0.614 & [0.599, 0.629] & 0.492 \\
17	20\%           & 0.591 & [0.576, 0.605] & 0.367 \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
22	Binary depth discrimination (gen-1 vs.\ gen-2+) degrades sublinearly: the first 5\% replacement causes the largest drop ($-$4.6\,pp), with diminishing marginal impact thereafter ($-$3.6\,pp for 5\%$\to$10\%, $-$2.3\,pp for 10\%$\to$20\%).
23	At 10\% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, which indicates that depth signal survives moderate perturbation.
24	
25	Three-class classification is more sensitive (0.737$\to$0.367 at 20\%), because distinguishing gen-0 from gen-1 relies heavily on lexical diversity features (TTR, hapax ratio) that are directly disrupted by word replacement.
26	The binary metric, which excludes gen-0, is inherently more robust since it depends primarily on reference-model entropy features distributed across many tokens.
27	
28	\paragraph{Feature subset degradation.}
29	Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
30	The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
31	At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.569), despite starting from a lower baseline.
32	Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
33	Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
34	The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact.
35	
36	\begin{table}[h]
37	\centering
38	\small
39	\caption{Feature subset degradation under random word replacement (8-gen LOGO). Entropy-only: 5 reference-model features; 7-feature: full ensemble including lexical features.}
40	\label{tab:feature-degrade}
41	\resizebox{\linewidth}{!}{%
42	\begin{tabular}{lcccc}
43	\toprule
44	\textbf{Perturb.} & \textbf{Ent-only Bin} & \textbf{7-feat Bin} & \textbf{Ent-only 3-cl} & \textbf{7-feat 3-cl} \\
45	\midrule
46	0\%  & 0.833 & 0.695 & 0.688 & 0.737 \\
47	5\%  & 0.738 & 0.650 & 0.539 & 0.641 \\
48	10\% & 0.667 & 0.614 & 0.427 & 0.492 \\
49	20\% & 0.569 & 0.591 & 0.314 & 0.367 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Baseline comparison.}
55	Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
56	
57	\begin{table}[h]
58	\centering
59	\small
60	\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate.}
61	\label{tab:baseline-robustness}
62	\begin{tabular}{lcccc}
63	\toprule
64	\textbf{Method} & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{20\%} \\
65	\midrule
66	7-feature ensemble & \textbf{0.695} & 0.650 & 0.614 & 0.591 \\
67	LD-Score           & 0.677 & \textbf{0.673} & \textbf{0.677} & \textbf{0.671} \\
68	Avg-LogProb        & 0.682 & 0.419 & 0.335 & 0.375 \\
69	FastDetectGPT      & 0.571 & 0.437 & 0.468 & 0.514 \\
70	Binoculars\textsuperscript{\dag}         & 0.500 & 0.461 & 0.446 & 0.425 \\
71	\bottomrule
72	\end{tabular}
73	
74	\vspace{2pt}
75	{\footnotesize \textsuperscript{\dag}Binoculars operates at chance level on this binary task; its degradation figures are not meaningful.}
76	\end{table}
77	
78	The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation ($-$0.6\,pp across the full 0\%$\to$20\% range).
79	FastDetectGPT and Avg-LogProb exhibit non-monotonic degradation at higher perturbation rates, likely because severe perturbation introduces distributional artifacts that these token-level methods detect as anomalous.
80	Avg-LogProb is the most fragile overall ($-$34.7\,pp at 10\%), while FastDetectGPT drops sharply at 5\% ($-$13.4\,pp) before partially recovering.
81	LD-Score is nearly invariant to perturbation, consistent with its reliance on corpus-level distributional divergence rather than per-token likelihoods.
82	The 7-feature ensemble offers the highest starting performance among single-reference methods, with sublinear degradation ($-$10.4\,pp at 20\%).
83	
84	\paragraph{LLM-simulated sentence regeneration.}
85	To test robustness under semantically coherent editing, we use Qwen3-0.6B-Base to randomly regenerate 1--3 sentences per passage (avg 1.69 sentences, ${\sim}$50\% edit distance) and re-evaluate the 8-gen LOGO pipeline.
86	Binary F1 drops from 0.692 to 0.647 ($-$4.5\,pp, 6.5\% relative); 3-class F1 drops from 0.739 to 0.667 ($-$7.1\,pp, 9.7\% relative).
87	The binary degradation ($-$4.5\,pp) is nearly identical to that caused by 5\% random word replacement ($-$4.6\,pp), despite the LLM rephrase altering ${\sim}$50\% of characters.
88	This asymmetry arises because LLM-generated replacements preserve the underlying statistical signature of the generation process (entropy dynamics, depth-accumulated distributional drift), whereas random word substitution directly destroys local statistical signals.
89	Depth profiling thus captures deep generative structure that survives semantic-preserving edits.
90	
91	\paragraph{Seed complexity.}
92	Performance is stable across seed text complexity: stratifying seeds by vocabulary richness (TTR terciles) yields maximum F1 variation of 1.1\,pp across groups.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb654b47-8415-41b6-a174-7ca5d2486883",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "5223bd8a-bb1c-43c3-a5b4-db09432c4141",
  "sourceToolAssistantUUID": "cb654b47-8415-41b6-a174-7ca5d2486883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T05:01:40.535Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MtK3pvGRhowS6pUSfN8hS1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5223bd8a-bb1c-43c3-a5b4-db09432c4141",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e12fd933-31f3-4e0c-be95-3ecde9bdfa7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 25 · 2026-05-20T05:01:40.541Z_

<details><summary>↩ Tool result · `toolu_01MtK3pvGRhowS6pUSfN8hS1`</summary>

```text
1	We analyze the distribution and characteristics of binary classification errors (gen-1 vs.\ gen-2+) across the 8-generator LOGO evaluation ($N$\,=\,29{,}095 samples, overall error rate 28.08\%).
2	
3	\paragraph{Error asymmetry.}
4	Errors are heavily asymmetric: 86.2\% are false negatives (gen-2+ predicted as gen-1) and only 13.8\% are false positives (gen-1 predicted as gen-2+).
5	The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
6	
7	\paragraph{Per-depth error rates.}
8	Error rates decrease monotonically with depth: depth-2 samples are the primary failure point (48.42\% error rate), followed by depth-3 (29.17\%) and depth-4 (20.32\%).
9	Depth-1 false positive rate is 7.11\%.
10	The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is therefore the hardest to detect.
11	
12	\paragraph{Per-generator variation.}
13	Table~\ref{tab:error-by-gen} shows error rates vary substantially across generators, correlating with model scale: larger models (Mistral-7B, Qwen3-8B) produce text closer to gen-1 characteristics, which makes depth discrimination harder.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Binary classification error rates by generator (8-gen LOGO). Sorted by error rate descending.}
19	\label{tab:error-by-gen}
20	\begin{tabular}{llccc}
21	\toprule
22	\textbf{Generator} & \textbf{Family} & \textbf{Samples} & \textbf{Errors} & \textbf{Error rate} \\
23	\midrule
24	Mistral-7B-v0.3 & Mistral & 3{,}853 & 1{,}734 & 45.00\% \\
25	Qwen3-8B        & Qwen    & 3{,}502 & 1{,}197 & 34.18\% \\
26	Llama-3.2-3B    & Llama   & 3{,}685 & 1{,}112 & 30.18\% \\
27	OLMo-2-1B      & OLMo    & 3{,}718 & 1{,}054 & 28.35\% \\
28	Pythia-2.8B     & Pythia  & 3{,}614 &   866 & 23.96\% \\
29	Qwen3-1.7B     & Qwen    & 3{,}621 &   814 & 22.48\% \\
30	Qwen3-0.6B     & Qwen    & 3{,}542 &   745 & 21.03\% \\
31	Pythia-1B       & Pythia  & 3{,}560 &   648 & 18.20\% \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	\paragraph{Feature-level explanation.}
37	Mann-Whitney U tests comparing correctly vs.\ incorrectly classified samples reveal that drifting features show significant distributional differences between correct and incorrect predictions: entropy\_mean ($p < 10^{-300}$), TTR ($p < 10^{-300}$), and hapax\_ratio ($p < 10^{-300}$).
38	In contrast, shape features show no discriminating power: entropy\_max ($p = 0.584$) and tail\_decay ($p = 0.653$).
39	Misclassified gen-2+ samples have systematically higher TTR (0.464 vs.\ 0.302 for correct) and entropy\_mean (2.26 vs.\ 1.57); these samples retain gen-1-like lexical diversity and have not undergone the distributional convergence characteristic of deeper generations.
40	This is consistent with the DDR pattern (\S\ref{sec:results-differential}): errors concentrate where depth-accumulated drift is insufficient, and shape features (which are near-stationary by design) provide no additional discriminative signal for error correction.
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e12fd933-31f3-4e0c-be95-3ecde9bdfa7f",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "7bb40174-769e-413e-8602-1043618ac2cb",
  "sourceToolAssistantUUID": "e12fd933-31f3-4e0c-be95-3ecde9bdfa7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T05:01:41.085Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FGLKYxb4Lem1MGXXRkmrdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb40174-769e-413e-8602-1043618ac2cb",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e0392bb-19a1-4955-8797-1ddef20ffd8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 27 · 2026-05-20T05:01:41.097Z_

<details><summary>↩ Tool result · `toolu_01FGLKYxb4Lem1MGXXRkmrdj`</summary>

```text
1	We evaluate whether depth signal generalizes beyond Wikipedia by constructing generation chains from three additional domains: News articles, Academic abstracts, and Code documentation.
2	For each domain, we sample 200 seed texts and generate chains of depth 3 using three generators (Pythia-1B, Qwen3-1.7B, Mistral-7B).
3	The same 7-feature ensemble and LOGO protocol are applied.
4	
5	\noindent\textbf{Important caveat:} Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$, which falls outside the method's reliable operating range ($t \leq 0.7$; Appendix~\ref{app:sampling-sensitivity}). Domain and temperature effects are therefore confounded in the results below; the cross-domain signal may partly reflect temperature-induced distributional divergence rather than domain generalization alone.
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\caption{Cross-domain depth classification under LOGO evaluation (binary: gen-1 vs.\ gen-2+). Three generators $\times$ 200 seeds per domain. Bootstrap 95\% CIs ($n$\,=\,1000).}
11	\label{tab:domain}
12	\begin{tabular}{lccc}
13	\toprule
14	\textbf{Domain} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
15	\midrule
16	Code           & 0.754 & [0.737, 0.770] & 0.634 \\
17	News           & 0.746 & [0.726, 0.764] & 0.652 \\
18	Academic       & 0.739 & [0.720, 0.757] & 0.622 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	All three non-Wikipedia domains achieve binary F1 $>$ 0.73 under leave-one-generator-out evaluation, which demonstrates that depth signal is not an artifact of Wikipedia text properties.
24	
25	\paragraph{Domain $\times$ temperature interaction.}
26	Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$ (vs.\ the main experiment's $t{=}0.7$, top-$p{=}0.9$).
27	Supplementary evaluation at $t{=}0.7$ reveals a domain $\times$ temperature interaction: the main Wikipedia experiment favors lower temperature (depth signal degrades monotonically with rising temperature; Appendix~\ref{app:sampling-sensitivity}), while cross-domain evaluation favors higher temperature ($t{=}1.0$ yields +3 to +11\,pp over $t{=}0.7$; News 0.746 vs.\ 0.712, Academic 0.739 vs.\ 0.628, Code 0.754 vs.\ 0.687).
28	This asymmetry likely reflects reference-model calibration: Pythia-410M, trained predominantly on web text, detects subtle per-step drift in Wikipedia but requires larger distributional divergence (produced by higher temperature) to detect depth signal in out-of-distribution domains.
29	This finding suggests that reference model selection is a key factor for cross-domain deployment of depth profiling.
30	
31	\paragraph{3-class inversion as DDR evidence.}
32	In the cross-domain setting, 3-class F1 (0.62--0.65) falls below binary F1 (0.74--0.75), reversing the pattern observed in the main experiment (3-class 0.762 $>$ binary 0.694).
33	This inversion reflects degraded gen-0 vs.\ gen-1 separation: the Pythia-410M reference model is calibrated to Wikipedia text, so its baseline entropy estimates are less discriminative for out-of-domain human text and compresses the feature distance between gen-0 and gen-1.
34	The binary task (gen-1 vs.\ gen-2+) is unaffected because both classes are generated under identical domain and decoding conditions; recursive drift is a relative change that does not depend on absolute calibration.
35	This pattern provides additional evidence that DDR captures generation-process invariants rather than domain-specific text properties: depth signal remains robust even when the human-vs-machine boundary becomes less distinct.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e0392bb-19a1-4955-8797-1ddef20ffd8f",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "6ac52d1a-4779-42b7-8711-398603ed09a9",
  "sourceToolAssistantUUID": "7e0392bb-19a1-4955-8797-1ddef20ffd8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T05:01:41.407Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SNhGWbqVgyPrUxdzU7kFeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ac52d1a-4779-42b7-8711-398603ed09a9",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "701adbe1-0843-4b04-a8e6-0e36e26f20ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 29 · 2026-05-20T05:01:41.415Z_

<details><summary>↩ Tool result · `toolu_01SNhGWbqVgyPrUxdzU7kFeQ`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lrc}
8	\toprule
9	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
10	\midrule
11	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
12	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
13	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
14	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
15	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
16	\bottomrule
17	\end{tabular}
18	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
19	\label{tab:downstream}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[h]
44	\centering
45	\small
46	\resizebox{\linewidth}{!}{%
47	\begin{tabular}{llcc}
48	\toprule
49	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
50	\midrule
51	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
52	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
53	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
54	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
55	\midrule
56	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
57	                                            & $\pm$2\% & No & 1.0 \\
58	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
59	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
60	\bottomrule
61	\end{tabular}}
62	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
63	\label{tab:tost-margins}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	However, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "701adbe1-0843-4b04-a8e6-0e36e26f20ba",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "cd1451f6-9ab7-4617-af4e-66e5352adef3",
  "sourceToolAssistantUUID": "701adbe1-0843-4b04-a8e6-0e36e26f20ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T05:01:42.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ZHkGz4n1oK3dKAcc1VRtz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd1451f6-9ab7-4617-af4e-66e5352adef3",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16041c41-c91d-4a87-aeb1-cfa392db96e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 31 · 2026-05-20T05:01:42.356Z_

<details><summary>↩ Tool result · `toolu_015ZHkGz4n1oK3dKAcc1VRtz`</summary>

```text
1	Table~\ref{tab:gen-subsets} summarizes the generator subsets used across experiments.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\caption{Generator subsets by experiment type.}
7	\label{tab:gen-subsets}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcl}
10	\toprule
11	\textbf{Experiment} & $\boldsymbol{N}$ & \textbf{Generators} \\
12	\midrule
13	Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
14	Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
15	QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
16	Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
17	Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
18	Cross-domain (Table~\ref{tab:domain}) & 3 & Py-1B, Qw-1.7B, Mistral \\
19	Instruct (Table~\ref{tab:instruct}) & 3 & OLMo, Qw-1.7B, Llama \\
20	Downstream (Appendix~\ref{app:downstream}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	The 5-generator set was the initial development subset; Qwen3-8B was added for scale evaluation, and Llama-3.2-3B and Mistral-7B-v0.3 were added last for family-diversity testing.
26	Subset differences reflect chronological expansion rather than selective reporting.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16041c41-c91d-4a87-aeb1-cfa392db96e0",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "1b412172-1364-405e-9e96-886665f29531",
  "sourceToolAssistantUUID": "16041c41-c91d-4a87-aeb1-cfa392db96e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T05:01:42.826Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AnYNzkKQYxKPnPDU2HX2Uf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b412172-1364-405e-9e96-886665f29531",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc02045a-4b57-4384-8995-f1411118349d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 33 · 2026-05-20T05:01:42.830Z_

<details><summary>↩ Tool result · `toolu_01AnYNzkKQYxKPnPDU2HX2Uf`</summary>

```text
1	\section{Per-Generator Equivalence Testing}
2	\label{app:tost}
3	
4	To confirm that the near-stationary classification is not a pooling artifact, we apply two one-sided $t$-tests (TOST) \cite{lakens_equivalence} for each feature within each generator separately (gen-1 vs.\ gen-2+, equivalence bound $|d| < 0.20$).
5	We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
6	LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
7	Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (see DDR Validation appendix).
8	Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
9	
10	Entropy min passes equivalence for all eight generators; entropy max passes for six of eight (exceeding $\varepsilon$ only for Pythia-1B and Pythia-2.8B, where $|d| \approx 0.21$--$0.25$); tail decay passes for four of eight.
11	All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
12	The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
13	Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
14	
15	\begin{table}[h]
16	\centering
17	\footnotesize
18	\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
19	\label{tab:tost-per-gen}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{l ccc c ccc}
22	\toprule
23	& \multicolumn{3}{c}{\textbf{Drifting}} & \textbf{Int.} & \multicolumn{3}{c}{\textbf{Near-stationary}} \\
24	\cmidrule(lr){2-4} \cmidrule(lr){5-5} \cmidrule(lr){6-8}
25	\textbf{Generator} & $\bar{H}$ & TTR & hapax & $\sigma_H$ & $H_{\max}$ & tail & $H_{\min}$ \\
26	\midrule
27	Pythia-2.8B  & 1.20 & 0.77 & 0.67 & 0.39 & 0.25          & 0.07\,\checkmark & 0.03\,\checkmark \\
28	Pythia-1B    & 1.40 & 0.80 & 0.65 & 0.53 & 0.21          & 0.08\,\checkmark & 0.02\,\checkmark \\
29	Qwen3-1.7B  & 1.12 & 0.93 & 0.83 & 0.52 & 0.02\,\checkmark & 0.09\,\checkmark & 0.05\,\checkmark \\
30	Llama-3.2-3B & 1.15 & 1.04 & 0.98 & 0.50 & 0.01\,\checkmark & 0.19          & 0.01\,\checkmark \\
31	OLMo-2-1B   & 1.19 & 1.08 & 1.00 & 0.61 & 0.06\,\checkmark & 0.22          & 0.07\,\checkmark \\
32	Qwen3-8B    & 0.86 & 0.71 & 0.66 & 0.37 & 0.04\,\checkmark & 0.15          & 0.01\,\checkmark \\
33	Qwen3-0.6B  & 0.92 & 0.63 & 0.50 & 0.56 & 0.01\,\checkmark & 0.08\,\checkmark & 0.10\,\checkmark \\
34	Mistral-7B   & 0.89 & 0.82 & 0.82 & 0.23 & 0.00\,\checkmark & 0.16          & 0.04\,\checkmark \\
35	\midrule
36	\textbf{Equiv.\ count} & 0/8 & 0/8 & 0/8 & 0/8 & 6/8 & 4/8 & 8/8 \\
37	\bottomrule
38	\end{tabular}}
39	\end{table}
40	
41	\begin{figure}[h]
42	\centering
43	\includegraphics[width=0.85\columnwidth]{fig_ddr_scatter.pdf}
44	\caption{DDR partition in pooled ($|\rho|$, Cohen's $d$) space. Drifting features (green) cluster at high $|\rho|$ and $d$; near-stationary features (orange) cluster near the origin; entropy std (purple) occupies a sole intermediate position. Dashed lines: TOST equivalence bound ($d{=}0.20$) and $|\rho|{=}0.30$. Diamond marker: entropy min (pooled $|\rho|{=}0.40$ reflects the gen-0/gen-1 boundary; gen-1 vs.\ gen-2+ $d{=}0.03$).}
45	\label{fig:ddr-scatter}
46	\end{figure}
47	
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc02045a-4b57-4384-8995-f1411118349d",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "c71747b5-762d-45da-9217-1e2c2c9d6895",
  "sourceToolAssistantUUID": "dc02045a-4b57-4384-8995-f1411118349d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T05:01:43.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_013W4oPiH4VSRtCXEg55JZkF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c71747b5-762d-45da-9217-1e2c2c9d6895",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1ff0601-3dc3-4e23-a697-5aa5f4d4811f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 35 · 2026-05-20T05:01:43.774Z_

<details><summary>↩ Tool result · `toolu_013W4oPiH4VSRtCXEg55JZkF`</summary>

```text
1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\linewidth}{!}{%
8	\begin{tabular}{lccc}
9	\toprule
10	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
11	\midrule
12	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
13	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
14	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
18	\label{tab:confusion}
19	\end{table}
20	
21	Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
22	The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
23	
24	\begin{figure}[ht]
25	\centering
26	\includegraphics[width=\columnwidth]{fig_appendix_confusion.pdf}
27	\caption{3-class LOGO confusion matrix ($N$\,=\,27{,}529). (a) Raw counts. (b) Row-normalized recall percentages. Gen-0 achieves near-perfect classification; the primary confusion axis is gen-1 $\leftrightarrow$ gen-2+.}
28	\label{fig:confusion-heatmap}
29	\end{figure}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1ff0601-3dc3-4e23-a697-5aa5f4d4811f",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "48dd9e44-46c3-4ae0-9319-f1299deed22f",
  "sourceToolAssistantUUID": "f1ff0601-3dc3-4e23-a697-5aa5f4d4811f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T05:01:44.243Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NQsZpEXGM5ctMdXSx5Xr5z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48dd9e44-46c3-4ae0-9319-f1299deed22f",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7c0585b-bde2-4974-9f70-bccc5dd03a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 37 · 2026-05-20T05:01:44.248Z_

<details><summary>↩ Tool result · `toolu_01NQsZpEXGM5ctMdXSx5Xr5z`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
10	\label{tab:alt-classifier}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{lc cccccc}
14	\toprule
15	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
16	\midrule
17	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
18	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
19	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
25	and even a linear model reaches $0.725$, well above the $0.33$ chance baseline for
26	three classes.
27	The per-generator ranking is also consistent across classifiers
28	(Pythia-1B easiest, Qwen3-8B hardest),
29	confirming that discriminative power originates in the entropy and lexical features,
30	not in classifier capacity.
31	Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
32	
33	\subsection*{Sampling Sensitivity Analysis}
34	\label{app:sampling-sensitivity}
35	
36	To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
37	
38	\begin{table}[h]
39	\centering
40	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
41	\label{tab:sampling-ablation}
42	\small
43	\begin{tabular}{llcc c}
44	\toprule
45	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
46	\midrule
47	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
48	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
49	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
50	\midrule
51	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
52	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
53	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
54	\midrule
55	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
56	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
57	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
58	\midrule
59	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
60	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
61	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	\noindent{\footnotesize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights used in the main experiments are no longer publicly available.}\\
66	\noindent{\footnotesize $^{\dagger}$Pythia-2.8B and Qwen3-1.7B temperature experiments predate the 8-generator expansion and use 6-generator LOGO; OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model temperature comparisons (the focus of this analysis) are unaffected.}
67	
68	Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
69	
70	The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
71	
72	\subsection*{Per-Generator Performance}
73	
74	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
75	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
76	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
77	
78	\begin{figure}[ht]
79	\centering
80	\includegraphics[width=\columnwidth]{fig_appendix_per_gen.pdf}
81	\caption{Per-generator LOGO performance. (a) 8-generator binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b) 6-generator LOGO detail heatmap showing the performance spread across model families.}
82	\label{fig:per-gen}
83	\end{figure}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7c0585b-bde2-4974-9f70-bccc5dd03a1f",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "d776cb2b-cc9c-469a-b988-33f7e14958e9",
  "sourceToolAssistantUUID": "e7c0585b-bde2-4974-9f70-bccc5dd03a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T05:01:44.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_017BhLiwfwW2Zf4RiHj3zDzg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d776cb2b-cc9c-469a-b988-33f7e14958e9",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cdc4c7e-c301-4f90-a3e3-9623e9add6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 39 · 2026-05-20T05:01:44.725Z_

<details><summary>↩ Tool result · `toolu_017BhLiwfwW2Zf4RiHj3zDzg`</summary>

```text
1	\subsection*{DDR Trend Lines}
2	
3	Figure~\ref{fig:ddr-trends} shows the per-feature depth trend (mean across all samples at each depth) with individual generator traces overlaid.
4	The consistent downward trajectories for drifting features across all generators confirm that DDR is a universal property of recursive generation.
5	Shape features exhibit flat trajectories regardless of generator, with near-zero $R^2$ for the linear fit.
6	
7	\FloatBarrier
8	\begin{figure*}[ht]
9	\centering
10	\includegraphics[width=\textwidth]{fig_appendix_ddr_trends.pdf}
11	\caption{Per-feature depth trends. Black line: pooled mean ($\pm$1 std shading) across all generators. Colored traces: individual generators. Features are labeled by DDR category (drifting, intermediate, near-stationary). Spearman $\rho$ and linear $R^2$ are annotated per panel.}
12	\label{fig:ddr-trends}
13	\end{figure*}
14	
15	\subsection*{UMAP Embedding}
16	
17	Figure~\ref{fig:umap} shows a 2D UMAP projection of the 7-feature space (7{,}500 stratified samples, StandardScaler normalization, $k$\,=\,30 neighbors, min\_dist\,=\,0.3).
18	Panel (a) reveals a depth gradient from gen-0 through gen-4, with progressive overlap at deeper generations consistent with the convergence that motivates the gen-2+ class collapse.
19	Panel (b) shows the 3-class view: gen-0 forms a separable cluster, while gen-1 and gen-2+ overlap substantially, which explains the classification difficulty at this boundary.
20	
21	\FloatBarrier
22	\begin{figure}[ht]
23	\centering
24	\includegraphics[width=\columnwidth]{fig_appendix_umap.pdf}
25	\caption{UMAP 2D projection of the 7-feature space ($N$\,=\,7{,}500 stratified sample). (a) Colored by raw generation depth (0--4): a gradient structure emerges, with deeper depths converging. (b) Colored by 3-class label: gen-0 separates clearly; gen-1 and gen-2+ overlap, consistent with the high false-negative rate at the gen-1/gen-2+ boundary.}
26	\label{fig:umap}
27	\end{figure}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdc4c7e-c301-4f90-a3e3-9623e9add6e9",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "c0be4c32-3cbd-41ac-a793-622e3c9ffb33",
  "sourceToolAssistantUUID": "0cdc4c7e-c301-4f90-a3e3-9623e9add6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T05:01:45.656Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PL2fjDKMCXqz5oueqTeV2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0be4c32-3cbd-41ac-a793-622e3c9ffb33",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42baea5-57cb-44e0-8062-a7bb2e878c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 41 · 2026-05-20T05:01:45.659Z_

<details><summary>↩ Tool result · `toolu_018PL2fjDKMCXqz5oueqTeV2`</summary>

```text
1	Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
2	We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
3	
4	\begin{figure}[ht]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
7	\caption{Cross-temperature transfer evaluation (6-gen LOGO). (a) Overall F1 by train$\rightarrow$test temperature condition. Matched conditions (0.7$\rightarrow$0.7, 1.0$\rightarrow$1.0) outperform cross-temperature transfer, with 0.7$\rightarrow$1.0 showing the largest degradation ($-6.6$\,pp in 3-class F1). (b) Per-generator 3-class F1 heatmap: Qwen3-1.7B shows dramatic degradation under cross-temperature conditions (0.418) while other generators remain stable. The temperature mismatch disproportionately affects the generator whose data was regenerated.}
8	\label{fig:cross-temp}
9	\end{figure}
10	
11	Key observations from the cross-temperature analysis:
12	
13	\begin{enumerate}[nosep]
14	\item \textbf{Matched-temperature robustness}: Both $t{=}0.7$ and $t{=}1.0$ matched conditions yield comparable performance (3-class F1: 0.789 vs.\ 0.726), with the gap attributable to weaker depth signal at high temperature rather than classifier degradation.
15	
16	\item \textbf{Asymmetric transfer}: Training at $t{=}1.0$ and testing at $t{=}0.7$ (F1\,=\,0.791) transfers well, but the reverse (0.7$\rightarrow$1.0, F1\,=\,0.723) degrades. This asymmetry reflects the information structure: features learned from high-variance (high-temperature) data generalize to low-variance settings, but not vice versa.
17	
18	\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
19	
20	\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b42baea5-57cb-44e0-8062-a7bb2e878c1a",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "20dbab1e-b7d0-4074-8456-fd15e50b60a6",
  "sourceToolAssistantUUID": "b42baea5-57cb-44e0-8062-a7bb2e878c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T05:01:46.035Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UobuCAMfiXLefrJYyZ1uKV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20dbab1e-b7d0-4074-8456-fd15e50b60a6",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEVPRTZJrWaANNXkMjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be42e158-b59a-4a52-8eb0-2cdadd0dbc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "output_tokens": 792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 792,
          "cache_read_input_tokens": 16282,
          "cache_creation_input_tokens": 9930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9930,
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

_source line 43 · 2026-05-20T05:01:46.040Z_

<details><summary>↩ Tool result · `toolu_01UobuCAMfiXLefrJYyZ1uKV`</summary>

```text
1	\subsection*{Data-Driven Clustering}
2	
3	To assess whether the 3/1/3 DDR partition emerges from the data rather than post-hoc grouping, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\caption{$k$-means clustering of 7 features in $(|\rho|, d)$ space.}
9	\label{tab:clustering}
10	\begin{tabular}{ccp{5.5cm}}
11	\toprule
12	$k$ & Silhouette & Clusters \\
13	\midrule
14	2 & \textbf{0.632} & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} \\
15	3 & 0.499 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\max}$, tail\} $\mid$ \{$H_{\min}$\} \\
16	4 & 0.571 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$H_{\max}$, tail\} $\mid$ \{$\sigma_H$\} $\mid$ \{$H_{\min}$\} \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
21	The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.632) is the strongest cluster structure.
22	At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
23	The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
24	At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
25	
26	\subsection*{TOST Equivalence Bound Sensitivity}
27	\label{app:tost-sensitivity}
28	
29	Table~\ref{tab:tost-sensitivity} shows the fraction of generators for which each feature passes the TOST equivalence test (gen-1 vs.\ gen-2+, $\alpha{=}0.05$) at three equivalence bounds $\varepsilon$.
30	
31	\begin{table}[h]
32	\centering
33	\small
34	\caption{TOST equivalence pass rate across 8 generators at varying $\varepsilon$.}
35	\label{tab:tost-sensitivity}
36	\begin{tabular}{llccc}
37	\toprule
38	\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
39	\midrule
40	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
41	 & TTR & 0/8 & 0/8 & 0/8 \\
42	 & hapax ratio & 0/8 & 0/8 & 0/8 \\
43	\midrule
44	Intermediate & $\sigma_H$ (ent.\ std) & 0/8 & 0/8 & 0/8 \\
45	\midrule
46	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 7/8 & 8/8 & 8/8 \\
47	 & $H_{\max}$ (ent.\ max) & 6/8 & 6/8 & 6/8 \\
48	 & tail decay & 4/8 & 4/8 & 7/8 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	The partition is robust to the equivalence bound: drifting features reject equivalence at all $\varepsilon$ for all generators, while entropy min passes even at the stricter bound $\varepsilon{=}0.15$ (7/8 generators).
54	Tail decay is the most $\varepsilon$-sensitive near-stationary feature, passing 4/8 at $\varepsilon{=}0.20$ but 7/8 at $\varepsilon{=}0.25$; the four non-passing generators show $|d|{=}0.15$--$0.22$, still well below the drifting threshold ($d > 0.50$).
55	Entropy max is stable across all three bounds (6/8), with the two failures (Pythia-1B $d{=}0.21$, Pythia-2.8B $d{=}0.25$) reflecting same-family reference affinity with the Pythia-410M reference model.
56	
57	\subsection*{Holdout Generator Split Validation}
58	\label{app:holdout-split}
59	
60	To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
61	We evaluate two complementary splits to avoid dependence on a single partition:
62	Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
63	Split~B selects \{Pythia-1B, Qwen3-0.6B, OLMo, Mistral\} (validation: Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama).
64	
65	\begin{table}[h]
66	\centering
67	\small
68	\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
69	\label{tab:holdout-split}
70	\resizebox{\linewidth}{!}{%
71	\begin{tabular}{llcccccc}
72	\toprule
73	& & \multicolumn{3}{c}{\textbf{Split A}} & \multicolumn{3}{c}{\textbf{Split B}} \\
74	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
75	\textbf{Zone} & \textbf{Feature} & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ \\
76	\midrule
77	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0.60 & 0.58 & 0.02 & 0.60 & 0.58 & 0.02 \\
78	 & TTR & 0.61 & 0.59 & 0.02 & 0.60 & 0.59 & 0.01 \\
79	 & hapax ratio & 0.62 & 0.60 & 0.02 & 0.62 & 0.61 & 0.01 \\
80	\midrule
81	Intermediate & $\sigma_H$ (ent.\ std) & 0.19 & 0.21 & 0.02 & 0.22 & 0.17 & 0.05 \\
82	\midrule
83	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 0.39 & 0.36 & 0.03 & 0.38 & 0.37 & 0.01 \\
84	 & $H_{\max}$ (ent.\ max) & 0.05 & 0.05 & 0.00 & 0.04 & 0.06 & 0.02 \\
85	 & tail decay & 0.10 & 0.08 & 0.02 & 0.11 & 0.07 & 0.04 \\
86	\bottomrule
87	\end{tabular}}
88	\end{table}
89	
90	Under simple joint $(|\rho|, d)$ thresholds, both splits produce a 3/2/2 partition: entropy min is classified as a second intermediate feature due to its elevated pooled $|\rho|$ (0.36--0.39).
91	However, entropy min's binary (gen-1 vs.\ gen-2+) $d$ values are uniformly below 0.06 across all four split${\times}$subset combinations, consistent with near-stationarity on the task-relevant metric; its pooled $|\rho|$ reflects change concentrated at the gen-0/gen-1 boundary rather than sustained drift.
92	Five of seven features are unambiguously classified under any reasonable criterion; entropy min's boundary status is resolved by the binary-task $d$ criterion.
93	
94	Selection and validation subsets produce identical partitions in both splits (Table~\ref{tab:holdout-split}; Figure~\ref{fig:holdout-scatter}).
95	The maximum $\Delta|\rho|$ between selection and validation is 0.05 (entropy std, Split~B), and the minimum gap between adjacent zones remains $>$0.15 in all subsets.
96	
97	\begin{figure}[h]
98	\centering
99	\includegraphics[width=\linewidth]{fig_ddr_holdout_split.pdf}
100	\caption{Holdout split validation in $(|\rho|, d)$ space. Filled markers: selection set; hollow: validation set. Zone assignments are identical across subsets; selection/validation pairs cluster tightly for all features.}
101	\label{fig:holdout-scatter}
102	\end{figure}
103	
104	\subsection*{Heteroscedasticity Sensitivity}
105	\label{app:heteroscedasticity}
106	
107	Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
108	To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
109	
110	\begin{table}[h]
111	\centering
112	\small
113	\caption{Effect size comparison (gen-1 vs.\ gen-2+, $N$\,=\,29{,}095). Glass's $\Delta$ uses the gen-1 SD as denominator; Cliff's $\delta$ thresholds follow Romano et al.\ (2006): $|\delta| < 0.147$ negligible, $< 0.33$ small, $< 0.474$ medium, otherwise large.}
114	\label{tab:effect-sizes}
115	\begin{tabular}{llrrr}
116	\toprule
117	\textbf{Zone} & \textbf{Feature} & \textbf{$|d|$} & \textbf{$|\Delta|$} & \textbf{$|\delta|$} \\
118	\midrule
119	\multirow{3}{*}{Drifting} & ent.\ mean & 1.054 & 1.410 & 0.587 \\
120	 & TTR & 0.814 & 1.116 & 0.510 \\
121	 & hapax ratio & 0.735 & 0.936 & 0.528 \\
122	\midrule
123	Intermediate & ent.\ std & 0.457 & 0.605 & 0.295 \\
124	\midrule
125	\multirow{3}{*}{Near-stat.} & tail decay & 0.087 & 0.099 & 0.072 \\
126	 & ent.\ max & 0.062 & 0.065 & 0.021 \\
127	 & ent.\ min & 0.016 & 0.015 & 0.354$^{\dagger}$ \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\noindent Effect sizes in Table~\ref{tab:effect-sizes} are computed on the binary task (gen-1 vs.\ gen-2+); the main text (\S\ref{sec:results-differential}) reports 3-class pooled $d$ values (e.g., hapax ratio $d{=}0.76$), which are slightly larger because the gen-0/gen-1 contrast contributes additional separation.
133	Glass's $\Delta$ amplifies drifting effects (1.41 vs.\ 1.05 for entropy mean) because gen-2+ variance exceeds gen-1 variance (ratio 2.08), making the pooled Cohen's $d$ conservative.
134	Near-stationary features remain negligible under both parametric metrics ($|\Delta| \leq 0.099$).
135	The minimum drifting-to-maximum-near-stationary gap is $9.5\times$ under Glass's $\Delta$ (0.936\,/\,0.099); heteroscedasticity does not erode the partition.
136	Cliff's $\delta$ classifies all drifting features as ``large'' ($|\delta| > 0.474$) and entropy std as ``small'' ($|\delta|{=}0.295$), consistent with the parametric partition.
137	
138	\noindent $^{\dagger}$Entropy min's elevated Cliff's $\delta$ (0.354, ``medium'') reflects distributional shape asymmetry between gen-1 and gen-2+ that rank-based statistics detect but location measures do not (Cohen's $d{=}0.016$, Glass's $\Delta{=}0.015$).
139	This is consistent with its documented boundary status (\S\ref{sec:results-differential}): the gen-0/gen-1 transition produces rank-order shifts that persist into deeper generations without affecting the mean.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be42e158-b59a-4a52-8eb0-2cdadd0dbc93",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "be3e9af3-6b04-4779-9095-34767d3b32b2",
  "sourceToolAssistantUUID": "be42e158-b59a-4a52-8eb0-2cdadd0dbc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T05:01:50.982Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANBLjzeLYa4vY1PAWLvW8v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be3e9af3-6b04-4779-9095-34767d3b32b2",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c53bcbfc-44e3-4fbc-bf8c-a1b973666717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 45 · 2026-05-20T05:01:50.987Z_

<details><summary>↩ Tool result · `toolu_01ANBLjzeLYa4vY1PAWLvW8v`</summary>

```text
1	\section{Dataset Statistics}
2	\label{app:dataset-stats}
3	
4	Table~\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).
5	Under the 3-class evaluation scheme, the dataset contains 7{,}963 gen-0 samples (21.5\%), 7{,}896 gen-1 (21.3\%), and 21{,}199 gen-2+ (57.2\%, combining depths 2--4).
6	The gen-2+ majority reflects the chain structure (three deeper depths per chain vs.\ one each for gen-0 and gen-1); class-balanced sampling is applied during evaluation.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{llcc}
12	\toprule
13	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Samples} \\
14	\midrule
15	Pythia-1B       & Pythia  & 1.0B & 4{,}555 \\
16	Pythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\
17	OLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\
18	Qwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\
19	Qwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\
20	Qwen3-8B       & Qwen    & 8.2B & 4{,}497 \\
21	Llama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\
22	Mistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\
23	\midrule
24	\multicolumn{3}{l}{\textbf{Total}} & \textbf{37{,}058} \\
25	\bottomrule
26	\end{tabular}
27	\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\protect\footnotemark}
28	\label{tab:dataset-stats}
29	\end{table}
30	\footnotetext{Table~\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}
31	
32	Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
33	The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
34	
35	\begin{figure*}[ht]
36	\centering
37	\includegraphics[width=\textwidth]{fig_appendix_violin.pdf}
38	\caption{Feature distributions by generation depth (violin plots, $N$\,=\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}
39	\label{fig:violin}
40	\end{figure*}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c53bcbfc-44e3-4fbc-bf8c-a1b973666717",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "2e5030cb-eede-4b1a-91b1-b756d9f09d60",
  "sourceToolAssistantUUID": "c53bcbfc-44e3-4fbc-bf8c-a1b973666717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T05:01:51.919Z_

<details open><summary>🔧 Tool call — Read · `toolu_011rws6Bndvoiph9ugoGEKBx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e5030cb-eede-4b1a-91b1-b756d9f09d60",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bfff5ce-f7ec-4cdf-96a9-eb39f91356d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 47 · 2026-05-20T05:01:51.925Z_

<details><summary>↩ Tool result · `toolu_011rws6Bndvoiph9ugoGEKBx`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\resizebox{\linewidth}{!}{%
7	\begin{tabular}{lcccc}
8	\toprule
9	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
10	\midrule
11	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
12	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
13	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
14	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
15	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
16	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
17	\midrule
18	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
19	\bottomrule
20	\end{tabular}}
21	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
22	\label{tab:5class-logo}
23	\end{table}
24	
25	\begin{table}[h]
26	\centering
27	\small
28	\resizebox{\linewidth}{!}{%
29	\begin{tabular}{lccccc}
30	\toprule
31	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
32	\midrule
33	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
34	\bottomrule
35	\end{tabular}}
36	\caption{Per-class F1 averaged across all six LOGO folds.}
37	\label{tab:5class-perclass}
38	\end{table}
39	
40	\paragraph{Analysis.}
41	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 to approximately 0.50 (six-generator subset; the 3-class baseline for this subset is comparable to the 8-generator result of 0.762 in Table~\ref{tab:logo-results}).
42	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
43	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
44	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical signatures.
45	Gen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).
46	Shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
47	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
48	
49	\paragraph{Classifier comparison.}
50	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
51	All classifiers perform comparably to the default XGBoost ensemble (0.501), indicating that classifier capacity is not the bottleneck.
52	The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
53	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bfff5ce-f7ec-4cdf-96a9-eb39f91356d3",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "b5869b50-27e7-4010-969c-64161b1a4fd0",
  "sourceToolAssistantUUID": "0bfff5ce-f7ec-4cdf-96a9-eb39f91356d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T05:01:52.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_016jHAZX7yhAxbqF4GbMsjZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5869b50-27e7-4010-969c-64161b1a4fd0",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3895dace-ee38-45b3-83c1-dc2584a86e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 49 · 2026-05-20T05:01:52.443Z_

<details><summary>↩ Tool result · `toolu_016jHAZX7yhAxbqF4GbMsjZu`</summary>

```text
1	To isolate the depth signal from generator identity, we train a binary classifier (gen-1 vs.\ gen-2+) on each of the eight generators independently and evaluate on all others.
2	Table~\ref{tab:transfer} reports the full 8$\times$8 transfer matrix and Figure~\ref{fig:transfer} visualizes it as a heatmap.
3	Note that these classifiers are trained with a binary objective, whereas the LOGO classifiers in Table~\ref{tab:logo-results} are trained on a 3-class task and evaluated on the binary subtask; the two setups are therefore not directly comparable.
4	
5	\begin{table}[h]
6	\centering
7	\scriptsize
8	\setlength{\tabcolsep}{3pt}
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{l|cccccccc}
11	\toprule
12	\textbf{Train $\backslash$ Test} & \textbf{Py-2.8B} & \textbf{Py-1B} & \textbf{Qw-0.6B} & \textbf{Qw-1.7B} & \textbf{Qw-8B} & \textbf{OLMo-1B} & \textbf{Ll-3B} & \textbf{Mi-7B} \\
13	\midrule
14	Py-2.8B  & \underline{0.985} & 0.873 & 0.823 & 0.833 & 0.741 & 0.829 & 0.815 & 0.712 \\
15	Py-1B    & 0.834 & \underline{0.987} & 0.828 & 0.821 & 0.704 & 0.778 & 0.764 & 0.620 \\
16	Qw-0.6B  & 0.786 & 0.846 & \underline{0.991} & 0.851 & 0.786 & 0.795 & 0.760 & 0.680 \\
17	Qw-1.7B  & 0.794 & 0.839 & 0.859 & \underline{0.989} & 0.790 & 0.817 & 0.798 & 0.717 \\
18	Qw-8B   & 0.811 & 0.836 & 0.853 & 0.855 & \underline{0.984} & 0.848 & 0.839 & 0.790 \\
19	OLMo-1B  & 0.811 & 0.827 & 0.837 & 0.852 & 0.803 & \underline{0.988} & 0.828 & 0.763 \\
20	Ll-3B    & 0.856 & 0.860 & 0.845 & 0.851 & 0.798 & 0.851 & \underline{0.987} & 0.787 \\
21	Mi-7B    & 0.834 & 0.837 & 0.837 & 0.845 & 0.817 & 0.849 & 0.851 & \underline{0.969} \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Cross-generator binary F1 transfer matrix (gen-1 vs.\ gen-2+). Each row trains on one generator; each column evaluates on another. Diagonal entries (\underline{underlined}) are within-generator. All 56 off-diagonal pairs exceed chance (0.5). Classifiers use the same 7-feature XGBoost configuration as LOGO but are trained with a binary objective.}
25	\label{tab:transfer}
26	\end{table}
27	
28	\begin{figure}[h]
29	\centering
30	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
31	\caption{Heatmap of the cross-generator binary F1 transfer matrix (Table~\ref{tab:transfer}). Same-family pairs (e.g., Pythia$\leftrightarrow$Pythia, Qwen$\leftrightarrow$Qwen) show slightly higher transfer; Mi-7B is the hardest transfer target (column minimum 0.62) yet remains well above chance.}
32	\label{fig:transfer}
33	\end{figure}
34	
35	All 56 off-diagonal transfer pairs yield F1 above chance, with a mean of 0.810 (95\% bootstrap CI [0.796, 0.822]; one-sample $t=46.58$, $p < 10^{-10}$).
36	Transfer is strongest within families (e.g., Py-2.8B$\to$Py-1B: 0.87) and weakest for Py-1B$\to$Mi-7B (0.62), consistent with the scale and reference-affinity effects discussed in \S\ref{sec:results-differential}.
37	These results confirm that depth signatures generalize across architectures, parameter scales, and model families, providing evidence against generator identity as a primary confound.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3895dace-ee38-45b3-83c1-dc2584a86e2d",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "d297e7c7-92c7-4959-869f-829ca200cb0c",
  "sourceToolAssistantUUID": "3895dace-ee38-45b3-83c1-dc2584a86e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T05:01:53.342Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KeQmyE3BoBvc3wTXpVezQv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d297e7c7-92c7-4959-869f-829ca200cb0c",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ca6ffc5-3537-4237-875e-6ba55aa579e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 51 · 2026-05-20T05:01:53.347Z_

<details><summary>↩ Tool result · `toolu_01KeQmyE3BoBvc3wTXpVezQv`</summary>

```text
1	To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\caption{Mean $|d|$ (gen-1 vs.\ gen-2+) across 4 generators at each temperature. Partition labels: \textbf{D}rifting ($|d|>0.5$), \textbf{I}ntermediate ($0.1{<}|d|{<}0.5$), near-\textbf{S}tationary ($|d|{<}0.1$). Boldface marks features that shift from their $\tau{=}0.7$ partition.}
7	\label{tab:ddr-temp-stability}
8	\begin{tabular}{lccc l}
9	\toprule
10	\textbf{Feature} & $\boldsymbol{\tau{=}0.5}$ & $\boldsymbol{\tau{=}0.7}$ & $\boldsymbol{\tau{=}0.9}$ & \textbf{Group} \\
11	\midrule
12	Entropy mean  & 1.39\,\textsuperscript{D} & 1.10\,\textsuperscript{D} & 0.58\,\textsuperscript{D} & Drifting \\
13	TTR           & 1.00\,\textsuperscript{D} & 0.85\,\textsuperscript{D} & \textbf{0.45}\,\textsuperscript{I} & Drifting \\
14	Hapax ratio   & 0.87\,\textsuperscript{D} & 0.75\,\textsuperscript{D} & \textbf{0.42}\,\textsuperscript{I} & Drifting \\
15	\midrule
16	Entropy std   & \textbf{0.84}\,\textsuperscript{D} & 0.52\,\textsuperscript{D} & \textbf{0.20}\,\textsuperscript{I} & Intermediate \\
17	\midrule
18	Entropy max   & 0.06\,\textsuperscript{S} & 0.09\,\textsuperscript{S} & \textbf{0.11}\,\textsuperscript{I} & Stationary \\
19	Tail decay    & 0.07\,\textsuperscript{S} & \textbf{0.12}\,\textsuperscript{I} & \textbf{0.15}\,\textsuperscript{I} & Stationary \\
20	Entropy min   & 0.04\,\textsuperscript{S} & 0.06\,\textsuperscript{S} & 0.04\,\textsuperscript{S} & Stationary \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
26	The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
27	Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ca6ffc5-3537-4237-875e-6ba55aa579e8",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "246cd45e-1d50-4480-a1e3-60b7dbfc4004",
  "sourceToolAssistantUUID": "5ca6ffc5-3537-4237-875e-6ba55aa579e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T05:01:53.817Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VidzcNVwX67jxt9h8u5mCv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "246cd45e-1d50-4480-a1e3-60b7dbfc4004",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cd339be-df17-456a-ba32-e7b4d2031f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 53 · 2026-05-20T05:01:53.829Z_

<details><summary>↩ Tool result · `toolu_01VidzcNVwX67jxt9h8u5mCv`</summary>

```text
1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	To test for topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
5	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
6	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lcc}
12	\toprule
13	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
14	\midrule
15	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
16	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
17	\midrule
18	Independent-seed average & 0.680 & --- \\
19	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
20	\bottomrule
21	\end{tabular}
22	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694). The classifier thus captures generative degradation patterns rather than seed-specific topic content.}
23	\label{tab:seed-control}
24	\end{table}
25	
26	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
27	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
28	
29	\paragraph{Semantic similarity analysis.}
30	Embedding cosine similarity between consecutive depth steps increases monotonically: 0$\rightarrow$1 (0.622), 1$\rightarrow$2 (0.683), 2$\rightarrow$3 (0.801), 3$\rightarrow$4 (0.859).
31	Deeper generations are thus \emph{more} semantically similar to their inputs, yet the classifier still distinguishes depth classes, suggesting that the depth signal resides in distributional rather than topical properties.
32	Prompt type modulates the baseline similarity level (continuation 0.717 $<$ elaboration 0.809 $\approx$ rewriting 0.808), plausibly because semantic-preservation constraints reduce topic drift while leaving the distributional location shift intact.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cd339be-df17-456a-ba32-e7b4d2031f1c",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "acc71448-d22f-4a83-a686-e0dbcadae367",
  "sourceToolAssistantUUID": "6cd339be-df17-456a-ba32-e7b4d2031f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T05:01:54.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jxp5ndn4hEAeyq7wPe1NLY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acc71448-d22f-4a83-a686-e0dbcadae367",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6354c43-c45c-4afd-84eb-bfad5a068009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 55 · 2026-05-20T05:01:54.148Z_

<details><summary>↩ Tool result · `toolu_01Jxp5ndn4hEAeyq7wPe1NLY`</summary>

```text
1	\subsection*{Instruction-Tuned Model Results}
2	
3	Table~\ref{tab:instruct} summarizes depth classification under instruction tuning for three model families.
4	All results use within-model 5-fold CV on single-generator chains; LOGO evaluation is available for two models but uses earlier generator subsets (5--6 generators), so cross-model numbers are not directly comparable across rows.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Depth classification: base vs.\ instruction-tuned models (within-model 5-fold CV). $\rho$: Spearman correlation of entropy mean with depth. Rev.: number of features (out of 7) whose $\rho$ reverses sign under instruction tuning.}
10	\label{tab:instruct}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{lcc cc cc c}
13	\toprule
14	& \multicolumn{2}{c}{\textbf{3-class F1}} & \multicolumn{2}{c}{\textbf{Binary F1}} & \multicolumn{2}{c}{$\boldsymbol{\rho}$\textbf{(ent.\ mean)}} & \\
15	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
16	\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
17	\midrule
18	OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
19	Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
20	Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
26	The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
27	Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
28	This pattern is consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (\S\ref{sec:discussion}).
29	
30	\paragraph{Retraining on instruction-tuned data.}
31	To test whether the depth signal persists under instruction tuning with reversed polarity, we retrain the XGBoost classifier on instruction-tuned feature data (Table~\ref{tab:instruct-retrain}).
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Classification recovery under instruction-tuned retraining (binary-only: gen-1 vs.\ gen-2+, gen-0 excluded from training and evaluation). Base$\rightarrow$Inst: base-trained classifier tested on instruct data. Note: Table~\ref{tab:instruct} reports higher instruct binary F1 (e.g., OLMo 0.813) because it uses 3-class training with binary evaluation, where gen-0 in training helps the classifier learn the feature space.}
37	\label{tab:instruct-retrain}
38	\begin{tabular}{lccc}
39	\toprule
40	\textbf{Model} & \textbf{Base$\rightarrow$Inst} & \textbf{Retrained} & \textbf{$\Delta$} \\
41	\midrule
42	OLMo-2-1B-Inst   & 0.321 & 0.590 & $+$0.269 \\
43	Qwen3-1.7B-Inst  & 0.500 & 0.660 & $+$0.160 \\
44	Qwen3-0.6B-Inst  & 0.532 & 0.600 & $+$0.068 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
50	Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
51	
52	\paragraph{DDR structure under instruction tuning.}
53	$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.338 (vs.\ 0.632 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
54	The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
55	Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
56	These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions.
57	
58	\paragraph{End-to-end instruct classification.}
59	To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
60	
61	\begin{table}[h]
62	\centering
63	\small
64	\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
65	\label{tab:instruct-qlora}
66	\begin{tabular}{lccccc}
67	\toprule
68	& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
69	\cmidrule(lr){2-3}
70	\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
71	\midrule
72	OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
73	Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\
74	\midrule
75	OLMo-2-1B (base) &       & 0.859\,$\pm$\,0.004 &             & 2{,}379 \\
76	Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\
77	\bottomrule
78	\end{tabular}
79	\end{table}
80	
81	The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp), indicating that depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
82	Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
83	All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6354c43-c45c-4afd-84eb-bfad5a068009",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "c1ee8227-57d5-44be-a0c4-aca0f4c999ab",
  "sourceToolAssistantUUID": "e6354c43-c45c-4afd-84eb-bfad5a068009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T05:01:55.208Z_

<details open><summary>🔧 Tool call — Read · `toolu_013s18X4H8gm8GspdQFNzxNp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1ee8227-57d5-44be-a0c4-aca0f4c999ab",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb696ab8-2f53-4fbb-88a2-e2523addcbd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 57 · 2026-05-20T05:01:55.212Z_

<details><summary>↩ Tool result · `toolu_013s18X4H8gm8GspdQFNzxNp`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The central finding is that recursive generation alters \emph{where} the token-level surprise distribution sits but not \emph{how} it is shaped: autoregressive sampling with fixed top-$p$ plausibly truncates the conditional distribution at a consistent shape regardless of input, while mean surprisal systematically decreases as the model conditions on its own increasingly typical outputs.
5	This asymmetry is not intrinsic to recursion but parameter-dependent: at $t{=}1.0$, the location signal collapses ($\rho$ from $-0.60$ to $-0.002$; Appendix~\ref{app:sampling-sensitivity}), and semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone}; cross-type transfer remains viable (F1\,=\,0.753).
6	
7	Several boundary conditions constrain practical applicability.
8	Document-level gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\sqrt{n})$ error scaling); the primary difficulty is distinguishing gen-1 from gen-2+, consistent with DDR producing the smallest location shift at the first recursive step (86\% false negatives; Appendix~\ref{app:error-analysis}).
9	Cross-temperature transfer degrades when test-time temperature exceeds training ($t{=}0.7 \rightarrow 1.0$: overall 3-class F1 drops from 0.789 to 0.723; the most affected single generator, Qwen3-1.7B, drops to per-generator F1\,=\,0.418; Appendix~\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature.
10	These patterns hold across reference model families (F1 within 0.013; Table~\ref{tab:cross-ref}).
11	
12	DDR occupies a distinct position among recursive generation phenomena.
13	Model collapse \cite{curse_of_recursion,strong_model_collapse} describes irreversible degradation from \emph{retraining} on model outputs; inference-chain drift operates in a different regime where parameters are fixed, drift is fully reversible, and shape features are affected an order of magnitude less.
14	This divergence has practical implications: model collapse remediation focuses on restoring tail coverage, while inference-chain contamination preserves shape and thus requires location-based detection---a strategy that DDR directly enables.
15	Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}), though richer representations recover substantially more signal (QLoRA F1\,=\,0.905; Appendix~\ref{app:qlora}).
16	Instruction-tuned models show attenuated fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base), but QLoRA on instruct data (F1\,=\,0.89--0.91 vs.\ XGBoost 0.58--0.73; Appendix~\ref{app:instruct}) indicates instruction tuning reorganizes rather than eliminates the signal, though this is demonstrated under within-model CV only; cross-generator instruct transfer (XGBoost LOGO F1\,=\,0.487) remains weak.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb696ab8-2f53-4fbb-88a2-e2523addcbd3",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "802dfa9b-6c92-4c74-9a15-e98a1b90ce78",
  "sourceToolAssistantUUID": "fb696ab8-2f53-4fbb-88a2-e2523addcbd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T05:01:55.756Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TqLA7LsrbDuxQ8wRrAN9Je`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "802dfa9b-6c92-4c74-9a15-e98a1b90ce78",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3637f2-202a-4028-99d3-cce18cf1491a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 59 · 2026-05-20T05:01:55.760Z_

<details><summary>↩ Tool result · `toolu_01TqLA7LsrbDuxQ8wRrAN9Je`</summary>

```text
1	This appendix presents feature ablation results supporting the complementarity analysis in \S\ref{sec:results-differential}.
2	
3	\begin{table}[t]
4	\centering
5	\footnotesize
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (imp.)} \\
9	\midrule
10	Full (7 features)     & 0.773 & hapax\_ratio (0.35) \\
11	Surface only (2)      & 0.688 & hapax\_ratio (0.41) \\
12	Reference only (5)    & 0.713 & entropy\_mean (0.27) \\
13	\bottomrule
14	\end{tabular}
15	\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+6.0\,pp) confirms complementarity.}
16	\label{tab:ablation}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3637f2-202a-4028-99d3-cce18cf1491a",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "4010ad0e-5dd3-4a39-85ec-16493718f98c",
  "sourceToolAssistantUUID": "1b3637f2-202a-4028-99d3-cce18cf1491a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T05:01:56.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KfXRb19TVeY2z2W8aJTFW7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4010ad0e-5dd3-4a39-85ec-16493718f98c",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dae9aca-21ae-43e0-b127-7e6ebaf4fd2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 61 · 2026-05-20T05:01:56.179Z_

<details><summary>↩ Tool result · `toolu_01KfXRb19TVeY2z2W8aJTFW7`</summary>

```text
1	\section{Feature Correlation Matrix}
2	\label{sec:appendix-feature-correlation}
3	
4	This appendix documents inter-feature correlations and the PCA analysis referenced in \S\ref{sec:results-differential}.
5	
6	\begin{table}[t]
7	\centering
8	\caption{Pearson correlation matrix of the seven depth features ($N=27{,}529$).}
9	\label{tab:feature-corr}
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{lrrrrrrr}
12	\toprule
13	 & $\bar{H}$ & $\sigma_H$ & $H_{\min}$ & $H_{\max}$ & $\tau$ & TTR & Hapax \\
14	\midrule
15	$\bar{H}$ & \textemdash & 0.49 & 0.31 & 0.01 & 0.07 & \textbf{0.86} & \textbf{0.81} \\
16	$\sigma_H$ & 0.49 & \textemdash & $-$0.15 & 0.16 & 0.26 & 0.43 & 0.34 \\
17	$H_{\min}$ & 0.31 & $-$0.15 & \textemdash & $-$0.04 & 0.01 & 0.20 & 0.23 \\
18	$H_{\max}$ & 0.01 & 0.16 & $-$0.04 & \textemdash & $-$0.08 & $-$0.13 & $-$0.15 \\
19	$\tau$ & 0.07 & 0.26 & 0.01 & $-$0.08 & \textemdash & 0.13 & 0.14 \\
20	TTR & \textbf{0.86} & 0.43 & 0.20 & $-$0.13 & 0.13 & \textemdash & \textbf{0.97} \\
21	Hapax & \textbf{0.81} & 0.34 & 0.23 & $-$0.15 & 0.14 & \textbf{0.97} & \textemdash \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	TTR and hapax ratio are near-perfectly correlated ($r=0.97$), and both correlate strongly with mean entropy ($r=0.86$ and $0.81$).
27	These three drifting features form a tightly coupled cluster: PCA on the standardized drifting-feature subset shows that a single principal component explains 92.3\% of their joint variance, with near-uniform loadings (0.56--0.59). These three features thus share a single latent dimension.
28	Full 7-feature PCA yields PC1 (44.4\% variance) loading on the drifting triplet (0.53--0.55) and PC2 (18.3\% variance) capturing entropy distributional shape (entropy std vs.\ entropy min contrast).
29	In contrast, $H_{\max}$, $\tau$ (tail decay), and $H_{\min}$ show weak pairwise correlations with all other features ($|r| < 0.27$); these features capture independent aspects of the token-probability distribution.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dae9aca-21ae-43e0-b127-7e6ebaf4fd2d",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "4eaf6244-4fa5-4b8c-8467-b5c5f9be1bda",
  "sourceToolAssistantUUID": "2dae9aca-21ae-43e0-b127-7e6ebaf4fd2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T05:01:56.625Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HQgzoJ9nkVLsiB8hfGfYDH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eaf6244-4fa5-4b8c-8467-b5c5f9be1bda",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEW7V3H7t9B7JQMbm5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16483028-91c0-487b-8589-ff99dd2a2f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 26212,
          "cache_creation_input_tokens": 16411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16411,
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

_source line 63 · 2026-05-20T05:01:56.632Z_

<details><summary>↩ Tool result · `toolu_01HQgzoJ9nkVLsiB8hfGfYDH`</summary>

```text
1	This appendix visualizes per-feature convergence trajectories across generation depth, complementing the DDR analysis in \S\ref{sec:results-differential}.
2	
3	\begin{figure}[h]
4	\centering
5	\includegraphics[width=\columnwidth]{fig_convergence_dynamics.pdf}
6	\caption{Per-feature convergence dynamics across generation depths 0--4, averaged over 8 generators. Each feature is expressed as Cohen's $d$ relative to depth~0, so all features start at zero and the $y$-axis directly reflects effect size. (a)~Drifting features (hapax ratio, TTR, entropy mean) and the intermediate feature (entropy std) diverge monotonically; lexical diversity features (TTR, hapax ratio) form a fast-convergence group ($|d| > 2$ by depth~2), while entropy mean and entropy std drift more slowly. (b)~Near-stationary features (entropy max, tail decay, entropy min) remain within $|d| < 0.25$ across all depths, confirming location stability. Shaded bands indicate $\pm 1$ standard deviation across generators.}
7	\label{fig:convergence-dynamics}
8	\end{figure}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16483028-91c0-487b-8589-ff99dd2a2f54",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "82e2f5a4-fa67-41fc-addd-0bee357f8434",
  "sourceToolAssistantUUID": "16483028-91c0-487b-8589-ff99dd2a2f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T05:02:01.206Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QdNT43KiZw9GLz9LBis7yv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82e2f5a4-fa67-41fc-addd-0bee357f8434",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1adcf537-78f7-476f-ad17-598f9e829348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 65 · 2026-05-20T05:02:01.211Z_

<details><summary>↩ Tool result · `toolu_01QdNT43KiZw9GLz9LBis7yv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text range from statistical tests \cite{gltr,grover,release_strategies} through zero-shot approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} to learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}, with extensions to intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gaps \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	Recent work moves beyond binary decisions---recognizing collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all target \emph{source} or \emph{production mode} taxonomies rather than recursive generation \emph{depth}; detection scores exhibit high cross-generator variance as depth predictors (binary F1 0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
9	Our contribution is the task formulation (generation depth classification \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance, orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}.
10	
11	\subsection{Model Collapse and Iterative Generation}
12	\label{sec:related-collapse}
13	
14	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}; these studies address \emph{training-loop} degradation, whereas we study \emph{inference chains} with fixed parameters.
15	Iterative self-refinement \cite{self_refine} targets output improvement through feedback rather than unconstrained recursive generation.
16	Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains showing progressive information loss, and \citet{markovian_chains} demonstrate attractor dynamics bounding distinguishable depth to approximately three classes.
17	We differ by studying \emph{non-paraphrastic continuation} chains, framing depth as \emph{ordinal classification} (gen-0/gen-1/gen-2+), and providing DDR feature-level diagnostics revealing \emph{what} converges (location) versus what remains stable (shape)---complementing their analysis of \emph{why} convergence occurs.
18	That all three works independently converge on ${\sim}$3 distinguishable classes---from Markovian dynamics \cite{markovian_chains}, information loss \cite{broken_telephone}, and feature compression (this work)---suggests a shared ceiling.
19	
20	\subsection{Vocabulary Diversity and Stylometry}
21	\label{sec:related-diversity}
22	
23	Declining lexical diversity in LLM text is documented in training \cite{curious_decline} and deployment \cite{writing_diversity}; our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship} that we extend beyond generator identity \cite{uchendu_attribution} to the depth dimension under top-$p$ sampling \cite{nucleus_sampling}.
24	
25	\subsection{Data Quality and Provenance}
26	\label{sec:related-provenance}
27	
28	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth is a complementary provenance signal.
29	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns, but strength decays across multi-step chains \cite{chainwash}, motivating passive methods; our NLL analysis connects to \citet{min_k_percent} (probability-tail membership inference), extending to full distributional analysis for depth.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1adcf537-78f7-476f-ad17-598f9e829348",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "ae625ad7-168d-46a3-b503-ab3781951afb",
  "sourceToolAssistantUUID": "1adcf537-78f7-476f-ad17-598f9e829348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T05:02:01.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YYQSRB1wVSR6y3K5hQkJVJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae625ad7-168d-46a3-b503-ab3781951afb",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88c927ec-43dd-407d-8064-96890b12c670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 67 · 2026-05-20T05:02:01.874Z_

<details><summary>↩ Tool result · `toolu_01YYQSRB1wVSR6y3K5hQkJVJ`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	Recursive LLM generation shifts \emph{where} text sits in distributional space but leaves \emph{how} it is shaped nearly unchanged, and this asymmetry is consistent across five model families spanning 0.6B to 8B parameters.
4	We term this \emph{differential depth response} (DDR): under standard decoding, mean entropy and lexical diversity drift monotonically with generation depth while entropy max and tail decay show an order-of-magnitude smaller effect size.
5	Prior work on iterative generation tracks aggregate convergence without separating what changes from what is preserved; DDR provides this decomposition and enables coarse depth classification (gen-0\,/\,gen-1\,/\,gen-2+): a 7-feature ensemble achieves leak-free binary F1\,=\,0.694 (95\% CI [.688, .700]) under leave-one-generator-out evaluation and 0.830 on cross-model chains (5-generator subset, LOGO; 95\% CI [.818, .841]), at lower cost than multi-detector alternatives.
6	Despite measurable distributional drift, equivalence testing (TOST $\pm$2\%, $p < 0.001$) suggests no downstream training quality degradation.
7	The depth signal degrades under instruction tuning; current applicability is restricted to base models.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88c927ec-43dd-407d-8064-96890b12c670",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "532cfb58-0623-4fde-baa2-7d828437d5ca",
  "sourceToolAssistantUUID": "88c927ec-43dd-407d-8064-96890b12c670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T05:02:02.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P6YyrwZvSWCeJepZLYLkuN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "532cfb58-0623-4fde-baa2-7d828437d5ca",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da8e280f-52b0-4d3d-80b5-5dc12a3f4379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 69 · 2026-05-20T05:02:02.184Z_

<details><summary>↩ Tool result · `toolu_01P6YyrwZvSWCeJepZLYLkuN`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When the output of a language model is fed back as input to another (or the same) model, the resulting generation chain defines a discrete dynamical system over text distributions.
5	How do the distributional properties of generated text evolve across successive steps of this recursion?
6	Understanding this evolution is fundamental to characterizing how language models transform distributions under iterative conditioning, with implications for model collapse theory \cite{curse_of_recursion,strong_model_collapse} and data provenance \cite{ccnet,dsir} as model outputs increasingly re-enter training corpora \cite{dolma,fineweb} (an estimated 7--17\% of recent scientific publications contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}).
7	Yet existing detection methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
8	
9	We formulate \emph{generation depth classification}, classifying text by coarse ordinal depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
10	Concurrent studies characterize convergence in paraphrastic and translation chains \cite{broken_telephone,markovian_chains}, but none decompose the drift into structurally distinct components; our work addresses this gap in non-paraphrastic continuation chains.
11	We restrict to base (pretrained) models as a deliberate design choice: instruction-tuning introduces confounds (length regulation, format constraints, safety-driven shaping) that obscure the distributional dynamics of recursive generation; preliminary experiments confirm substantially degraded depth signal under instruction tuning (\S\ref{sec:discussion}).
12	
13	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) show an order-of-magnitude smaller effect size.
14	This pattern is consistent with recursive generation producing a location shift in the token-level NLL distribution; one hypothesis is that the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive generation compresses the location toward the model's preferred output distribution.
15	
16	Because drifting features capture the progressive location shift while stationary features provide a stable reference, combining them yields a classifier that generalizes across generators: binary F1\,=\,0.830 on heterogeneous cross-model chains (5-generator subset) and 0.694 under leave-one-generator-out evaluation, outperforming individual detection baselines by 6.7--36.3\,pp while matching a 4-detector ensemble (within 0.3\,pp) at 2.4$\times$ lower computational cost.
17	
18	Our contributions are threefold:
19	\begin{enumerate}[nosep,leftmargin=*]
20	    \item We formulate generation depth classification, moving beyond binary detection to ordinal depth estimation (gen-0\,/\,gen-1\,/\,gen-2+), and construct an evaluation suite of 37K texts from eight generators spanning five model families (0.6B--8B parameters).
21	    \item We decompose inference-chain drift into structurally distinct components: central-tendency features drift monotonically ($d = 0.76$--$1.17$) while shape features remain an order of magnitude more stable ($d < 0.10$), a decomposition absent from existing attractor dynamics and model collapse analyses. A 7-feature ensemble exploiting this \emph{differential depth response} achieves binary F1\,=\,0.830 on cross-model chains.
22	    \item Comprehensive evaluation reveals that DDR is robust within $t \in [0.5, 0.7]$ but degrades at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp), is prompt-type modulated (continuation $>$ elaboration), and is substantially attenuated under instruction tuning; equivalence testing (TOST $\pm$2\%, $p < 0.001$) suggests no downstream quality degradation (Appendix~\ref{app:downstream}).
23	\end{enumerate}
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da8e280f-52b0-4d3d-80b5-5dc12a3f4379",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "02025264-dc2d-4437-8271-8aebf462f224",
  "sourceToolAssistantUUID": "da8e280f-52b0-4d3d-80b5-5dc12a3f4379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-20T05:02:02.589Z_

<details open><summary>🔧 Tool call — Read · `toolu_012XNTeVNvLMPQucczmyYoWq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02025264-dc2d-4437-8271-8aebf462f224",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5d6925c-5e73-40c6-9527-3ac6305e20bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 71 · 2026-05-20T05:02:02.593Z_

<details><summary>↩ Tool result · `toolu_012XNTeVNvLMPQucczmyYoWq`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Recursive generation produces a consistent, interpretable distributional signature: central-tendency features drift monotonically across depth while shape features remain an order of magnitude more stable.
5	This differential depth response enables depth classification across five model families (leak-free binary F1\,=\,0.694 under LOGO evaluation, 0.830 on cross-model chains, 5-generator subset) with no detected downstream quality degradation (preliminary TOST $\pm$2\%, $p < 0.001$; $n$\,=\,3 seeds).
6	The location-shape decomposition suggests that depth signal may arise in any iterative autoregressive process with fixed decoding, a hypothesis testable beyond text generation; current boundaries remain at instruction tuning (where token-level signal persists but handcrafted features fail to capture it) and frontier scale (70B+).
7	Code, data, and models will be released upon publication.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5d6925c-5e73-40c6-9527-3ac6305e20bb",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "eb5ce8f0-f6dc-4b42-ac48-822627ba1abc",
  "sourceToolAssistantUUID": "c5d6925c-5e73-40c6-9527-3ac6305e20bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-20T05:02:03.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LePDGJZG7tv7KvWBEnCcpF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb5ce8f0-f6dc-4b42-ac48-822627ba1abc",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98a6a6e8-6062-413f-98e7-8774c7f7db06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 73 · 2026-05-20T05:02:03.151Z_

<details><summary>↩ Tool result · `toolu_01LePDGJZG7tv7KvWBEnCcpF`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\usepackage{multirow}
14	\linenumbers
15	
16	\graphicspath{{../chart/}}
17	
18	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{results}
31	
32	\input{discussion}
33	\input{conclusion}
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\appendix
40	
41	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
42	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
43	
44	\input{appendix_dataset_stats}
45	\FloatBarrier
46	
47	\section{Length Confound Analysis}
48	\label{app:length}
49	\input{appendix_length}
50	\FloatBarrier
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	\FloatBarrier
56	
57	\section{Finer-Grained Depth Classification}
58	\label{app:finer-depth}
59	\input{appendix_finer_depth}
60	\FloatBarrier
61	
62	\section{End-to-End Depth Classification (QLoRA)}
63	\label{app:qlora}
64	\input{appendix_qlora}
65	\FloatBarrier
66	
67	\section{Leave-One-Feature-Out Analysis}
68	\label{app:lofo}
69	\input{appendix_lofo}
70	\FloatBarrier
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	\FloatBarrier
76	
77	\section{Classifier Sensitivity}
78	\label{app:classifier}
79	\input{appendix_classifier}
80	\FloatBarrier
81	
82	\section{Robustness to Text Perturbation}
83	\label{app:human-edit}
84	\input{appendix_human_edit}
85	\FloatBarrier
86	
87	\section{Cross-Domain Generalization}
88	\label{app:domain}
89	\input{appendix_domain}
90	\FloatBarrier
91	
92	\section{Instruction-Tuned Model Analysis}
93	\label{app:instruct}
94	\input{appendix_instruct}
95	\FloatBarrier
96	
97	\section{Error Analysis of Binary Classification}
98	\label{app:error-analysis}
99	\input{appendix_error_analysis}
100	\FloatBarrier
101	
102	\section{Downstream Utility}
103	\label{app:downstream}
104	\input{appendix_downstream}
105	\FloatBarrier
106	
107	\section{Cross-Model Chain Per-Class Detail}
108	\label{app:cross-model-detail}
109	\input{appendix_cross_model_detail}
110	\FloatBarrier
111	
112	\section{Feature Distribution Analysis}
113	\label{app:feature-distributions}
114	\input{appendix_feature_distributions}
115	\FloatBarrier
116	
117	\section{Cross-Temperature Transfer}
118	\label{app:cross-temp}
119	\input{appendix_cross_temp}
120	\FloatBarrier
121	
122	\section{Feature Ablation}
123	\label{app:ablation-table}
124	\input{appendix_ablation}
125	
126	\begin{figure}[h]
127	\centering
128	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
129	\caption{LOGO binary F1 (gen-1 vs.\ gen-2+, 8-gen pooled) with inference cost. Ensembles achieve marginally higher F1 at 2.4$\times$ inference time and 3.2$\times$ GPU memory; individual detectors vary widely when repurposed for depth.}
130	\label{fig:baseline-ci}
131	\end{figure}
132	\FloatBarrier
133	
134	\input{appendix_feature_correlation}
135	\FloatBarrier
136	
137	\section{Cross-Family Reference Models}
138	\label{app:cross-ref}
139	\input{table4}
140	\FloatBarrier
141	
142	\input{appendix_seed_control}
143	\FloatBarrier
144	
145	\input{appendix_tost}
146	\FloatBarrier
147	
148	\section{DDR Partition Validation}
149	\label{app:ddr-validation}
150	\input{appendix_ddr_validation}
151	\FloatBarrier
152	
153	\section{Generator Subset Summary}
154	\label{app:gen-subsets-section}
155	\input{appendix_generator_subsets}
156	\FloatBarrier
157	
158	\input{appendix_qualitative_examples}
159	
160	\section{Cross-Generator Transfer Analysis}
161	\label{app:transfer}
162	\input{appendix_transfer}
163	\FloatBarrier
164	
165	\section{Supplementary DDR Characterization}
166	\label{app:ddr-supplement}
167	
168	\subsection{Partition Stability Across Temperatures}
169	\label{app:ddr-temp-stability}
170	\input{appendix_temperature_stability}
171	
172	\subsection{Per-Feature Convergence Dynamics}
173	\label{app:convergence}
174	\input{appendix_convergence}
175	\FloatBarrier
176	
177	\end{document}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98a6a6e8-6062-413f-98e7-8774c7f7db06",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "63e9b3a9-02af-4248-9e17-3faa9cc2bf14",
  "sourceToolAssistantUUID": "98a6a6e8-6062-413f-98e7-8774c7f7db06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T05:02:04.147Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CNYmsTttLZMUfshG85x2hA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63e9b3a9-02af-4248-9e17-3faa9cc2bf14",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7196645-d640-4722-8c2f-dd2e9b5b9904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 75 · 2026-05-20T05:02:04.151Z_

<details><summary>↩ Tool result · `toolu_01CNYmsTttLZMUfshG85x2hA`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: within-type 3-class F1 ranges from 0.78 (continuation) to 0.73 (elaboration), with inspired rewriting intermediate at 0.74 (Appendix~\ref{app:prompt-type}).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.789, binary F1\,=\,0.830; evaluated on the 5-generator subset for which cross-model chains were available), though these generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	Independent gen-0 seed sets per generator would eliminate potential memorization effects in 3-class LOGO evaluation; we report leak-free binary F1 as the primary metric to mitigate this limitation.
22	
23	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).
24	All seed texts in the main evaluation are English Wikipedia excerpts.
25	Cross-domain evaluation (Appendix~\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\,=\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.
26	The reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.
27	Generalization to other languages remains untested.
28	
29	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
30	Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings, limiting deployment to scenarios where the generation temperature is approximately known.
31	
32	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7196645-d640-4722-8c2f-dd2e9b5b9904",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "3fbd4df2-9866-4cdc-b440-ec0723bff07e",
  "sourceToolAssistantUUID": "d7196645-d640-4722-8c2f-dd2e9b5b9904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T05:02:04.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LWwA5QgVMfZMSU8FfJKioD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbd4df2-9866-4cdc-b440-ec0723bff07e",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93c56eed-cd9e-4487-83af-2ab8da4ec64d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 77 · 2026-05-20T05:02:04.611Z_

<details><summary>↩ Tool result · `toolu_01LWwA5QgVMfZMSU8FfJKioD`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	Generation depth is classifiable across diverse architectures: the 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under generator-level leave-one-out evaluation on the 5-generator subset for which cross-model chains were available (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B).\footnote{We corrected the cross-model chain evaluation from sample-level CV to generator-level LOGO for consistency with our main evaluation protocol. CIs are case-level bootstrap ($n$\,=\,2{,}000). The 5-generator result is not directly comparable to the 8-generator LOGO (binary F1\,=\,0.694) due to differing generator subsets.}
14	The higher cross-model binary F1 relative to the 8-generator LOGO (0.694) is not directly comparable: the cross-model evaluation uses a 5-generator subset, and generator heterogeneity in mixed chains may amplify depth-correlated distributional shifts.
15	A single-generator transfer analysis (Appendix~\ref{app:transfer}) provides evidence against this confound: classifiers trained on one generator transfer to all seven others with mean binary F1\,=\,0.810 (95\% CI [0.796, 0.822]), significantly above chance.
16	Leave-one-family-out (LOFO) evaluation yields binary F1\,=\,0.686, consistent with cross-family transfer.
17	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}).
18	Preliminary cross-domain evaluation suggests the signal persists with variation, though a domain$\times$temperature interaction exists (Appendix~\ref{app:domain}).
19	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 (6-generator LOGO; $+$11.6\,pp; Appendix~\ref{app:qlora}), which indicates that richer representations capture additional depth signal beyond the 7-feature set; on instruct data, QLoRA recovers to 0.89--0.91 (Appendix~\ref{app:instruct}).
20	
21	\paragraph{Length confound control.}
22	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\ref{app:length}).
23	
24	\paragraph{Seed-sharing control.}
25	Seed-level demeaning (F1\,=\,0.701) and an independent-seed experiment with disjoint seed pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.
26	
27	\begin{table}[t]
28	\centering
29	\footnotesize
30	\resizebox{\columnwidth}{!}{%
31	\begin{tabular}{llcccc}
32	\toprule
33	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-cl F1}$^{\dagger}$ \\
34	\midrule
35	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
36	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
37	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
38	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
39	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
40	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
41	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
42	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
43	\midrule
44	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
45	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
46	\bottomrule
47	\end{tabular}}
48	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
49	\label{tab:logo-results}
50	\end{table}
51	
52	\subsection{Differential Depth Response}
53	\label{sec:results-differential}
54	
55	Features exhibit a continuous gradient of depth sensitivity, with a data-driven binary partition as the strongest structure: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields silhouette\,=\,0.632 (Appendix~\ref{app:ddr-validation}), separating \emph{drifting} features (entropy mean, TTR, hapax ratio; $|\rho| > 0.60$, $d{=}0.76$--$1.17$) from \emph{non-drifting} ones.
56	We use the shorthand \emph{differential depth response} (DDR) for this partition and further resolve a 3/1/3 characterization using domain-informed criteria: entropy std occupies a sole \emph{intermediate} position (large level shift $d{=}0.55$, low monotonicity $|\rho|{=}0.16$); the remaining three \emph{near-stationary} features (entropy max, tail decay, entropy min) show negligible depth effects ($d < 0.10$; CV shift $<$3\% vs.\ $>$15\% for drifting).
57	This partition is robust under heteroscedasticity-corrected metrics (below).
58	The partition is demonstrated for this seven-feature set; alternative features (e.g., syntactic complexity, n-gram frequencies) may yield different groupings, though the convergence of five independent effect-size metrics suggests the location/shape asymmetry reflects distributional structure rather than feature-selection artifact.
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
63	\caption{Differential depth response: Spearman correlations between individual features and generation depth. Drifting features (hapax ratio, TTR, entropy mean) show $|\rho| > 0.60$; entropy std ($|\rho|{=}0.16$, $d{=}0.55$) is the sole intermediate feature; near-stationary features (entropy max, tail decay, entropy min) show $d < 0.10$ for gen-1 vs.\ gen-2+ (entropy min's elevated pooled $|\rho|$ reflects the gen-0/gen-1 boundary; \S\ref{sec:results-differential}).}
64	\label{fig:feature-drift}
65	\end{figure}
66	
67	Pooled class-balanced Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
68	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.64$, TTR $\rho = -0.63$, entropy mean $\rho = -0.60$),
69	while shape features remain near-stationary (tail decay $|\rho| = 0.04$; per-depth distributions in Appendix~\ref{app:feature-distributions}).
70	The six-fold magnitude gap between drifting ($|\rho| > 0.60$) and near-stationary features ($|\rho| < 0.10$) defines the DDR partition, with entropy std ($|\rho| = 0.16$, $d{=}0.55$) as the sole intermediate member.
71	The 3/1/3 partition is stable across $d$ thresholds in $[0.56, 0.75]$; data-driven clustering confirms the primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.632; Appendix~\ref{app:ddr-validation}).
72	
73	\paragraph{Distributional shift quantification.}
74	Two-sample KS tests confirm the split: drifting-feature statistics (0.516--0.537) are ${\sim}10\times$ larger than shape-feature statistics (0.043--0.052; all $p \approx 0$ after Bonferroni correction).
75	Cohen's $d$ \cite{cohen1988statistical} (pooled, class-balanced) converges with $\rho$: drifting features show large effects (entropy mean $d{=}1.17$, TTR $d{=}0.88$, hapax ratio $d{=}0.76$), while shape features are near zero (entropy max $d{=}0.08$, tail decay $d{=}0.08$).
76	Levene tests reject strict equal-variance ($p < 10^{-10}$); Glass's $\Delta$ (using gen-1 SD) amplifies drifting effects (entropy mean $\Delta{=}1.41$, hapax $\Delta{=}0.94$) while near-stationary features remain negligible ($\Delta \leq 0.10$), yielding a ${\geq}9.5\times$ gap. Cliff's $\delta$ corroborates the partition (Appendix~\ref{app:ddr-validation}).
77	Shape-feature CV shift ($<$3\% vs.\ $>$15\% for drifting features) supports ``near-stationary'' as a practical characterization.
78	Five features fall cleanly into the drifting or near-stationary groups under both $\rho$ and $d$; the remaining two require qualification: entropy min's pooled $|\rho|$ (0.40) reflects change concentrated at the gen-0/gen-1 boundary, but for gen-1 vs.\ gen-2+ it is near-stationary ($d{=}0.03$), placing it in the near-stationary group; entropy std shows a substantial level shift ($d{=}0.55$) despite low monotonicity ($|\rho|{=}0.16$), making it the sole intermediate feature.
79	Entropy min exhibits a discrepancy between location-based (Cohen's $d$\,=\,0.016) and rank-based (Cliff's $\delta$\,=\,0.354) effect sizes, indicating distributional shape change without location shift: recursive generation produces more extreme minimum-entropy tokens while preserving the mean. The near-stationary label refers specifically to location stability; rank-order sensitivity is documented in Appendix~\ref{app:ddr-validation}.
80	The location/shape decomposition rests on the convergence of $\rho$, Levene, CV shift, and $d$, not the omnibus KS statistic alone.
81	Per-generator TOST equivalence testing confirms the partition is not a pooling artifact; holdout generator validation confirms stability across two 4/4 splits (Appendix~\ref{app:tost}).
82	Tail decay shows generator-dependent variation ($d{=}0.15$--$0.22$), but reclassifying it as intermediate preserves the core split and classification performance.
83	
84	\paragraph{Feature complementarity.}
85	The full 7-feature set (F1\,=\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
86	Permutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18).
87	PCA confirms the three drifting features share a single latent dimension (92.3\% variance, loadings 0.56--0.59; Appendix~\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\,pp binary F1, and retaining any single drifting feature with the four non-drifting features yields F1\,=\,0.692 (vs.\ 0.701 full).
88	DDR's contribution is identifying which distributional properties (NLL location vs.\ shape) are depth-sensitive; PC scores achieve equivalent classification but obscure which specific properties drift.
89	TTR and hapax ratio ($r = 0.97$) show permutation importance differences (0.35 vs.\ 0.18) due to feature masking \cite{strobl_conditional_2008}; all three are retained for marginal LOFO gains (Appendix~\ref{app:lofo}).
90	
91	\paragraph{Cross-family reference models.}
92	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Table~\ref{tab:cross-ref} in Appendix~\ref{app:cross-ref}), with consistently negative entropy drift.
93	Pythia generators' highest F1 (0.718--0.724) may partly reflect same-family affinity with the Pythia-410M reference model, but the 0.013 cross-reference spread bounds this effect; depth features are robust to reference model choice, though this does not alone establish DDR as a fundamental property of recursive generation.
94	
95	\paragraph{Temperature and prompt-type sensitivity.}
96	The depth signal is modulated by decoding parameters and prompt type (Appendices~\ref{app:sampling-sensitivity},~\ref{app:prompt-type}).
97	All four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp binary F1); low-temperature improvement is model-family-dependent ($+7$--$9$\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen).
98	Continuation chains show the strongest drift (binary F1\,=\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\,=\,0.753).
99	Per-feature convergence trajectories confirm this ordering (Appendix~\ref{app:convergence}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\ref{app:ddr-temp-stability}).
100	
101	
102	\subsection{Comparison with Detection Baselines}
103	\label{sec:results-baselines}
104	
105	Do existing detection methods already capture depth signal?
106	To contextualize depth discrimination ability rather than claim competitive advantage, we repurpose four detection scores as ordinal depth predictors using the same XGBoost framework and LOGO splits (Table~\ref{tab:baselines}).
107	
108	\begin{table}[t]
109	\centering
110	\footnotesize
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
114	\midrule
115	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
116	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
117	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
118	\midrule
119	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
120	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
121	LD-Score              & 1 & 0.630 & 0.675 & --- \\
122	Binoculars            & 1 & 0.411 & 0.539 & --- \\
123	\bottomrule
124	\end{tabular}
125	\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}
126	\label{tab:baselines}
127	\end{table}
128	
129	The 7-feature ensemble exceeds all individual baselines in 3-class F1 ($\Delta$\,=\,6.7--36.3\,pp; Figure~\ref{fig:baseline-ci}).
130	Multi-detector ensembles achieve marginally higher binary F1 (0.708 vs.\ 0.705) at 2.4$\times$ inference cost, suggesting depth information is implicitly encoded in distributional divergence measures.
131	DDR's contribution is not classification performance but decomposing depth signal into location-sensitive and shape-stable components, a distinction absent from both binary detection methods and model collapse analyses (\S\ref{sec:discussion}).
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93c56eed-cd9e-4487-83af-2ab8da4ec64d",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "00263b34-4c26-466c-aaf9-97b79c2c0742",
  "sourceToolAssistantUUID": "93c56eed-cd9e-4487-83af-2ab8da4ec64d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-20T05:02:05.649Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NvkJyKA15Qu8TLtfDWaF7m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00263b34-4c26-466c-aaf9-97b79c2c0742",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f13db25d-6776-4a4f-b226-9d402503f922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 42623,
          "cache_creation_input_tokens": 11729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11729,
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

_source line 79 · 2026-05-20T05:02:05.652Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PgrHFRGxBRF92xLmZJpM41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f13db25d-6776-4a4f-b226-9d402503f922",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEWtmLiGoLS2SMcMwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e44446bc-8c7c-4b0e-b56e-e0696255cf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 42623,
          "cache_creation_input_tokens": 11729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11729,
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

_source line 80 · 2026-05-20T05:02:05.655Z_

<details><summary>↩ Tool result · `toolu_01NvkJyKA15Qu8TLtfDWaF7m`</summary>

```text
1	This appendix reports per-generator breakdowns for the cross-model chain evaluation described in \S\ref{sec:results-classification}.
2	
3	\begin{table}[h]
4	\centering
5	\footnotesize
6	\begin{tabular}{lcccc}
7	\toprule
8	\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
9	\midrule
10	gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
11	gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
12	gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
13	\midrule
14	\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
15	\bottomrule
16	\end{tabular}
17	\caption{Cross-model chain per-class performance (generator-level leave-one-out, $N$\,=\,2{,}964, $n_{\text{generators}}$\,=\,5: Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B). Macro F1\,=\,0.831 under class balancing; under natural class distribution, macro F1\,=\,0.789. Binary F1 (gen-1 vs.\ gen-2+)\,=\,0.830 (95\% CI [.818, .841], case-level bootstrap, $n$\,=\,2{,}000). Cross-model chains avoid the gen-0 seed sharing issue present in single-generator LOGO.}
18	\label{tab:cross-model-perclass}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f13db25d-6776-4a4f-b226-9d402503f922",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "d67b42d4-82ea-4801-bd1d-bcaef9116b5f",
  "sourceToolAssistantUUID": "f13db25d-6776-4a4f-b226-9d402503f922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-20T05:02:05.656Z_

<details><summary>↩ Tool result · `toolu_01PgrHFRGxBRF92xLmZJpM41`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection; this allows finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, which allows evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
22	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
23	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
24	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
25	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
26	The theoretical yield is $8 \times {\sim}1{,}000 \times 5 = 39{,}815$ texts; after removing 2{,}746 chain breaks (empty or degenerate outputs at intermediate depths that prevented deeper generation) and 11 passages too short for feature extraction, 37{,}058 texts remain (Appendix~\ref{app:dataset-stats}).
27	For classification, depths 2--4 are collapsed into the $2{+}$ class.
28	
29	\subsection{Feature Extraction}
30	\label{sec:features}
31	
32	The seven features are motivated by two complementary views of distributional drift.
33	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
34	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
35	We use interpretable distributional statistics rather than learned representations so that the DDR tri-partition (our primary contribution) remains transparent; neural features would yield a black-box classifier.
36	This two-pronged design is validated through leave-one-feature-out analysis (Appendix~\ref{app:lofo}) and cross-group ablation (\S\ref{sec:results-differential}); both analyses confirm that the two feature groups contribute to depth discrimination.
37	
38	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
39	
40	\paragraph{Reference-model features.}
41	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
42	We use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.
43	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
44	From the resulting NLL sequence, we extract five statistics:
45	\begin{itemize}[nosep,leftmargin=*]
46	    \item \textbf{entropy\_mean}: mean token-level NLL, which captures the average predictability of the text under the reference model;
47	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, which measures the spread of per-token surprise;
48	    \item \textbf{entropy\_max}: maximum token-level NLL, which captures the most surprising token;
49	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the reference model's confidence floor on the most predictable token;
50	    \item \textbf{tail\_decay}: slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.
51	\end{itemize}
52	
53	\paragraph{Surface features.}
54	Two features capture lexical diversity without requiring a reference model:
55	\begin{itemize}[nosep,leftmargin=*]
56	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
57	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
58	\end{itemize}
59	
60	\paragraph{Feature complementarity.}
61	The seven features were selected a priori from two complementary perspectives (reference-model NLL distribution and surface lexical diversity) to enable interpretable decomposition of depth signal; exploring richer feature spaces (syntactic complexity, semantic coherence) may improve classification but at the cost of the location/shape analysis that is the paper's primary contribution.
62	These features exhibit a \emph{differential depth response} (DDR) into drifting, intermediate, and near-stationary groups (\S\ref{sec:results-differential}), motivating their combination (pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
63	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
64	
65	\subsection{Evaluation Protocol}
66	\label{sec:evaluation}
67	
68	\paragraph{Cross-validation.}
69	Our experiments use three overlapping generator subsets reflecting chronological expansion: the original 5-generator set (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO. Each table notes its subset.
70	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.
71	LOGO holds out individual generators but does not isolate family effects (e.g., when Pythia-1B is held out, Pythia-2.8B remains in training).
72	\textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families; cross-family generalization holds (average binary F1\,=\,0.686; \S\ref{sec:results-classification}).
73	
74	\paragraph{Classifier.}
75	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$; standard defaults), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
76	LOGO F1 is stable across random seeds (std\,$<$\,0.001 over 5 seeds); this near-zero variance reflects the deterministic LOGO splits (each generator held out exactly once) with seeds controlling only XGBoost's internal stochasticity. Bootstrap CIs on held-out folds provide the relevant generalization uncertainty.
77	Alternative classifiers and ordinal-specific methods (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power therefore resides in the features, not the classifier.
78	
79	\paragraph{Metrics and statistical testing.}
80	The primary metric is \textbf{macro-averaged F1} over the three depth classes.
81	We report 95\% confidence intervals via percentile bootstrap ($n{=}1{,}000$ unless otherwise noted), McNemar tests for pairwise comparisons, and paired bootstrap for baseline comparisons.
82	All $p$-values are two-sided; Bonferroni correction is applied within each family of simultaneous tests: the 21 distributional comparisons (7 features $\times$ 3 depth-group pairs, \S\ref{sec:results-differential}) and the 4 pairwise baseline comparisons (\S\ref{sec:results-baselines}).
83	Feature--depth correlations (\S\ref{sec:results-differential}) use class-balanced subsamples to control for depth-class imbalance.
84	
85	\paragraph{Baselines.}
86	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
87	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
88	
89	\paragraph{Length confound control.}
90	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e44446bc-8c7c-4b0e-b56e-e0696255cf25",
  "isSidechain": true,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "agentId": "a476781bbc33ad56b",
  "type": "user",
  "uuid": "aab0e37d-aa79-40c3-9dbb-e8613553ab54",
  "sourceToolAssistantUUID": "e44446bc-8c7c-4b0e-b56e-e0696255cf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-20T05:05:57.932Z_

Here is the complete extraction from all 41 .tex files:

---

## 1. `table1.tex`
- **Exp IDs**: None
- **Key metrics**: LOGO Macro-F1 per generator: Pythia-1B 0.806, Mistral-7B 0.681; Average 8-gen 0.762, 95% CI [0.758, 0.766]
- **Keywords**: leave-one-generator-out (LOGO), 3-class depth classification, held-out generator
- **Tables/Figures**: `\label{tab:logo-results}` (Table: LOGO results, 8-gen, 3-class). NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.

## 2. `table2.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.773; Surface only (2 features) = 0.688; Reference only (5 features) = 0.713; McNemar p < 0.001 for both subsets. Permutation importance: hapax_ratio 0.269, entropy_mean 0.164, ttr 0.159
- **Keywords**: feature group ablation, complementarity, 8-gen 10-fold CV, permutation importance, surface features, reference features
- **Tables/Figures**: `\label{tab:feature-ablation}` (Table: feature group ablation)

## 3. `table4.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-410M LOGO F1 = 0.803, Ent. Drift [-1.19, -1.40]; OLMo-2-1B LOGO F1 = 0.807, Ent. Drift [-0.61, -0.91]; Qwen3-0.6B LOGO F1 = 0.816, Ent. Drift [-0.96, -1.35]; F1 spread = 0.013
- **Keywords**: cross-family reference model validation, 5-gen LOGO subset, entropy drift, reference model choice
- **Tables/Figures**: `\label{tab:cross-ref}` (Table: cross-family reference models)

## 4. `appendix_qlora.tex`
- **Exp IDs**: None
- **Key metrics**: XGBoost 5-class F1 = 0.501 +/- 0.038, 3-class F1 = 0.789; QLoRA 5-class F1 = 0.583 +/- 0.010, 3-class F1 = 0.905 +/- 0.003; Per-class F1 (5-class): 0.999/0.796/0.413/0.259/0.447; Hyperparameter robustness: rank 32 seed 123 yields 5-class 0.587 +/- 0.005, 3-class 0.905 +/- 0.004
- **Keywords**: QLoRA, end-to-end depth classification, Qwen3-0.6B-Base, LoRA rank 16, learning rate 2e-4, 3 epochs, 5-class sequence classification, hyperparameter robustness, LoRA rank 32, seed 123, token-level patterns
- **Tables/Figures**: `\label{tab:qlora}` (Table: QLoRA vs XGBoost)

## 5. `appendix_lofo.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.789 (6-gen); entropy_max dropped: 0.774 (-1.50 pp); entropy_mean: 0.783 (-0.63 pp); ttr: 0.784 (-0.55 pp); hapax_ratio: 0.785 (-0.42 pp); tail_decay: 0.786 (-0.33 pp); entropy_std: 0.786 (-0.29 pp); entropy_min: 0.789 (+0.01 pp)
- **Keywords**: leave-one-feature-out (LOFO), ablation, permutation importance, feature redundancy, 6-gen LOGO
- **Tables/Figures**: `\label{tab:lofo}` (Table: LOFO ablation)

## 6. `appendix_length.tex`
- **Exp IDs**: None
- **Key metrics**: Spearman |rho| < 0.14 (length-depth); tail_decay |rho| = 0.38, hapax_ratio |rho| = 0.30, TTR |rho| = 0.29 (length-feature); entropy_mean |rho| = 0.09, entropy_std |rho| = 0.18; Length-matched binary F1 = 0.724 (down from 0.770, delta = -0.046); Random-subsample control F1 = 0.767; Length accounts for ~6% of discriminative performance
- **Keywords**: length confound, Spearman correlation, length-matched classification, random-subsample control, deconfounding, 8-gen LOGO
- **Tables/Figures**: None (inline results only)

## 7. `appendix_qualitative_examples.tex`
- **Exp IDs**: seed 120
- **Key metrics**: Feature values per depth: entropy_mean 2.720/2.206/0.780; TTR 0.659/0.272/0.081; hapax ratio 0.561/0.183/0.005; entropy_max 7.000/7.016/6.926; tail_decay -0.00227/-0.00231/-0.00223
- **Keywords**: qualitative examples, generation chain, Pythia-2.8B, continuation prompt, monotonic drift, near-stationary shape features, seed 120
- **Tables/Figures**: `\label{tab:qualitative-text}` (Table: example text chain), `\label{tab:qualitative-features}` (Table: feature values)

## 8. `ethics.tex`
- **Exp IDs**: None
- **Key metrics**: 62 GPU-hours total; 4x NVIDIA RTX 5090 GPUs (32 GB each)
- **Keywords**: ethics, Wikipedia seeds, CC BY-SA 3.0, Apache 2.0, Qwen License, Llama Community License, compute budget, Python 3.12.3, PyTorch 2.10.0, CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0
- **Tables/Figures**: None

## 9. `appendix_prompt_type.tex`
- **Exp IDs**: None
- **Key metrics**: Within-prompt-type 5-fold CV F1: continuation 0.78, rewriting 0.74, elaboration 0.73; Cross-prompt-type (LOPTO) avg F1 = 0.753; Feature decay rates: continuation 16.9%/step, rewriting 6.1%, elaboration 1.4%
- **Keywords**: prompt type, continuation, elaboration, inspired rewriting, LOPTO (leave-one-prompt-type-out), cross-prompt transfer, Pythia-2.8B, 995 seeds, 5 depths
- **Tables/Figures**: None (inline results)

## 10. `appendix_human_edit.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Perturbation robustness: 0% binary F1=0.695 [0.680,0.710], 3-class=0.737; 5% binary=0.650, 3-class=0.641; 10% binary=0.614, 3-class=0.492; 20% binary=0.591, 3-class=0.367
  - Feature subset: Ent-only 0% bin=0.833, 7-feat bin=0.695; at 20%: ent-only=0.569, 7-feat=0.591 (crossover)
  - Baseline robustness: 7-feat 0.695, LD-Score 0.677, Avg-LogProb 0.682, FastDetectGPT 0.571, Binoculars 0.500
  - LLM-simulated regen: binary drops 0.692->0.647 (-4.5 pp), 3-class 0.739->0.667 (-7.1 pp)
  - Seed complexity: max F1 variation 1.1 pp across TTR terciles
- **Keywords**: human edit, random word replacement, perturbation robustness, 8-gen LOGO, binary gen-1 vs gen-2+, feature subset degradation, entropy-only subset, baseline robustness, LD-Score, FastDetectGPT, Binoculars, Avg-LogProb, LLM-simulated sentence regeneration, Qwen3-0.6B-Base, seed complexity
- **Tables/Figures**: `\label{tab:human-edit}`, `\label{tab:feature-degrade}`, `\label{tab:baseline-robustness}`

## 11. `appendix_error_analysis.tex`
- **Exp IDs**: None
- **Key metrics**: N=29,095, overall error rate 28.08%; 86.2% false negatives, 13.8% false positives; Depth-2 error 48.42%, depth-3 29.17%, depth-4 20.32%, depth-1 FP 7.11%; Per-generator: Mistral-7B 45.00%, Qwen3-8B 34.18%, Llama-3.2-3B 30.18%, OLMo-2-1B 28.35%, Pythia-2.8B 23.96%, Qwen3-1.7B 22.48%, Qwen3-0.6B 21.03%, Pythia-1B 18.20%; Mann-Whitney: entropy_mean p<1e-300, TTR p<1e-300, hapax_ratio p<1e-300; entropy_max p=0.584, tail_decay p=0.653; Misclassified gen-2+ TTR 0.464 vs 0.302 correct; entropy_mean 2.26 vs 1.57
- **Keywords**: error analysis, binary classification, false negatives, false positives, error asymmetry, per-depth error rates, per-generator error rates, Mann-Whitney U test, model scale effect
- **Tables/Figures**: `\label{tab:error-by-gen}`

## 12. `appendix_domain.tex`
- **Exp IDs**: None
- **Key metrics**: Code binary F1=0.754 [0.737,0.770], 3-class=0.634; News binary=0.746 [0.726,0.764], 3-class=0.652; Academic binary=0.739 [0.720,0.757], 3-class=0.622; Domain x temperature: News 0.746 vs 0.712 (t=1.0 vs 0.7), Academic 0.739 vs 0.628, Code 0.754 vs 0.687
- **Keywords**: cross-domain, News, Academic, Code documentation, Wikipedia, domain generalization, temperature interaction, 3 generators (Pythia-1B, Qwen3-1.7B, Mistral-7B), 200 seeds, t=1.0, top-p=1.0, reference model calibration, 3-class inversion, DDR evidence
- **Tables/Figures**: `\label{tab:domain}`

## 13. `appendix_downstream.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-2-0425-1B downstream PPL: All depths (12,299) 2.335+/-0.000; Size-matched random (3,951) 2.367+/-0.000; Depth 0-1 (3,951) 2.387+/-0.001; Binary-filtered (3,951) 2.389+/-0.000; Depth 0 only (797) 2.681+/-0.001; TOST p=1.1e-4 at +/-2% margin; Cohen's d: 86.0 (full vs random), 119.7 (full vs depth 0-1); Margin sensitivity: Full vs Random passes at +/-2% (p=1e-6), Full vs Depth 0-1 requires +/-3%
- **Keywords**: downstream, fine-tuning, perplexity, data curation, OLMo-2-0425-1B, depth-aware curation, TOST equivalence testing, null result, 3 seeds, size-matched, data quantity dominates, margin sensitivity
- **Tables/Figures**: `\label{tab:downstream}`, `\label{tab:tost-margins}`

## 14. `appendix_generator_subsets.tex`
- **Exp IDs**: None
- **Key metrics**: None (summary table only)
- **Keywords**: generator subsets, 8-gen main LOGO, 5-gen cross-model chains, 6-gen QLoRA, 4-gen temperature ablation, 1-gen prompt-type, 3-gen cross-domain, 3-gen instruct, 5-gen downstream, chronological expansion
- **Tables/Figures**: `\label{tab:gen-subsets}`

## 15. `appendix_tost.tex`
- **Exp IDs**: None
- **Key metrics**: Per-generator TOST (epsilon=|d|<0.20): entropy_min passes 8/8; entropy_max passes 6/8 (Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25); tail_decay passes 4/8; all drifting features 0/8; Per-generator |d| values: Pythia-2.8B entropy_mean=1.20, Pythia-1B=1.40, Qwen3-1.7B=1.12, etc.
- **Keywords**: TOST equivalence testing, per-generator, Cohen's d, epsilon=0.20, near-stationary, drifting, gen-1 vs gen-2+, alpha=0.05, DDR scatter
- **Tables/Figures**: `\label{tab:tost-per-gen}`, `\label{fig:ddr-scatter}` (fig_ddr_scatter.pdf)

## 16. `appendix_confusion_matrix.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529 (6-gen); gen-0 recall 99.4%; gen-1: 75.0% correct, 18.8% -> gen-2+, 6.2% -> gen-0; gen-2+: 73.7% correct, 23.3% -> gen-1, 3.0% -> gen-0
- **Keywords**: confusion matrix, 6-generator LOGO, 3-class, gen-0/gen-1/gen-2+, row-normalized, DDR predictions
- **Tables/Figures**: `\label{tab:confusion}`, `\label{fig:confusion-heatmap}` (fig_appendix_confusion.pdf)

## 17. `appendix_classifier.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO: XGBoost 0.789, Random Forest 0.790, Logistic Regression 0.725; Per-generator: Pythia-1B easiest (0.856/0.856/0.781), Qwen3-8B hardest (0.683/0.684/0.624); CORAL, Frank-Hall comparable with overlapping CIs; Temperature ablation (4-gen LOGO): Pythia-2.8B t=0.5 binary=0.814, t=0.7=0.740, t=0.9=0.480; OLMo t=0.5=0.783, t=0.7=0.695, t=0.9=0.453; Qwen3-1.7B t=0.5=0.751, t=0.7=0.751, t=0.9=0.566; Qwen3-0.6B t=0.5=0.711, t=0.7=0.691, t=0.9=0.598; rho(ent mean) ranges -0.72 to -0.26
- **Keywords**: classifier sensitivity, XGBoost, Random Forest, Logistic Regression, CORAL ordinal, Frank-Hall ordinal, sampling sensitivity, temperature ablation, t=0.5/0.7/0.9, nucleus p=0.9, per-generator performance, scale effect, OLMo-2-0425-1B (April 2025 release)
- **Tables/Figures**: `\label{tab:alt-classifier}`, `\label{tab:sampling-ablation}`, `\label{fig:per-gen}` (fig_appendix_per_gen.pdf)

## 18. `appendix_feature_distributions.tex`
- **Exp IDs**: None
- **Key metrics**: None (visualization appendix)
- **Keywords**: DDR trend lines, per-feature depth trends, Spearman rho, linear R^2, UMAP embedding, 7-feature space, N=7500, k=30, min_dist=0.3, StandardScaler, depth gradient, convergence
- **Tables/Figures**: `\label{fig:ddr-trends}` (fig_appendix_ddr_trends.pdf), `\label{fig:umap}` (fig_appendix_umap.pdf)

## 19. `appendix_cross_temp.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO cross-temperature: 0.7->0.7 3-class F1=0.789; 1.0->1.0=0.726; 1.0->0.7=0.791; 0.7->1.0=0.723 (-6.6 pp); Qwen3-1.7B drops to 0.418 under cross-temp; Binary: Qwen3-1.7B 0.948->0.713 (0.7->1.0), recovers 0.948 (1.0->0.7); Aggregate binary range 0.900-0.958
- **Keywords**: cross-temperature transfer, train/test temperature mismatch, Qwen3-1.7B, asymmetric transfer, generator-specific vulnerability, t=1.0, top-p=0.95
- **Tables/Figures**: `\label{fig:cross-temp}` (fig_appendix_cross_temp.pdf)

## 20. `appendix_ddr_validation.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - k-means clustering: k=2 silhouette=0.632, k=3=0.499, k=4=0.571
  - TOST sensitivity: entropy_min passes 7/8 at eps=0.15, 8/8 at eps=0.20; tail_decay 4/8 at eps=0.20, 7/8 at eps=0.25; all drifting 0/8 at all eps
  - Holdout split validation: max delta|rho|=0.05, min gap between zones >0.15
  - Effect sizes: entropy_mean |d|=1.054, |Delta|=1.410, |delta|=0.587; TTR |d|=0.814, |Delta|=1.116, |delta|=0.510; hapax |d|=0.735, |Delta|=0.936, |delta|=0.528; ent_std |d|=0.457, |Delta|=0.605, |delta|=0.295; tail_decay |d|=0.087; ent_max |d|=0.062; ent_min |d|=0.016, Cliff's delta=0.354
  - Levene tests: p<1e-10, variance ratios 1.86-2.21
  - Minimum drifting-to-max-stationary gap: 9.5x under Glass's Delta
- **Keywords**: data-driven clustering, k-means, silhouette, TOST sensitivity, epsilon 0.15/0.20/0.25, holdout generator split validation, Split A, Split B, 4/4 partition, heteroscedasticity, Levene test, Glass's Delta, Cliff's delta, Cohen's d, DDR partition validation, gen-1 vs gen-2+ N=29,095
- **Tables/Figures**: `\label{tab:clustering}`, `\label{tab:tost-sensitivity}`, `\label{tab:holdout-split}`, `\label{fig:holdout-scatter}` (fig_ddr_holdout_split.pdf), `\label{tab:effect-sizes}`

## 21. `appendix_dataset_stats.tex`
- **Exp IDs**: None
- **Key metrics**: Total N=37,058; per-generator: Pythia-1B 4,555; Pythia-2.8B 4,609; OLMo-2-1B 4,713; Qwen3-0.6B 4,538; Qwen3-1.7B 4,617; Qwen3-8B 4,497; Llama-3.2-3B 4,680; Mistral-7B 4,849; Class breakdown: gen-0 7,963 (21.5%), gen-1 7,896 (21.3%), gen-2+ 21,199 (57.2%); Baseline subset 34,131
- **Keywords**: dataset statistics, per-generator sample counts, filtering, 8 generators, 5 families, class-balanced sampling, chain structure
- **Tables/Figures**: `\label{tab:dataset-stats}`, `\label{fig:violin}` (fig_appendix_violin.pdf)

## 22. `appendix_finer_depth.tex`
- **Exp IDs**: None
- **Key metrics**: 5-class LOGO (6-gen): OLMo 0.484, Pythia-1B 0.543, Pythia-2.8B 0.523, Qwen3-0.6B 0.513, Qwen3-1.7B 0.510, Qwen3-8B 0.434; Average 0.501+/-0.038, weighted F1 0.521, accuracy 0.541; Per-class: gen-0 0.921, gen-1 0.634, gen-2 0.268, gen-3 0.259, gen-4 0.423; Confusion: 36.5% gen-2->gen-1, 37.8% gen-3->gen-4; Classifier comparison: HistGradientBoosting 0.501 [0.496,0.506], RF 0.476, LR 0.447, Frank-Hall 0.451; Permutation importance: entropy_std +93%, tail_decay +400% under 5-class
- **Keywords**: finer-grained, 5-class depth classification, LOGO, 6-gen subset, per-class F1, gen-2/gen-3 boundary, classifier comparison, HistGradientBoosting, Frank-Hall, ordinal, CORAL, practical resolution ceiling
- **Tables/Figures**: `\label{tab:5class-logo}`, `\label{tab:5class-perclass}`

## 23. `appendix_transfer.tex`
- **Exp IDs**: None
- **Key metrics**: 8x8 transfer matrix: diagonal 0.969-0.991; off-diagonal mean 0.810 [0.796, 0.822], t=46.58 p<1e-10; Best transfer: Py-2.8B->Py-1B 0.873; Worst: Py-1B->Mi-7B 0.620; Within-family strongest, Mistral hardest target (column min 0.62)
- **Keywords**: cross-generator transfer, binary F1 gen-1 vs gen-2+, transfer matrix, heatmap, same-family, cross-family, generator identity confound
- **Tables/Figures**: `\label{tab:transfer}`, `\label{fig:transfer}` (fig_transfer_heatmap.pdf)

## 24. `appendix_temperature_stability.tex`
- **Exp IDs**: None
- **Key metrics**: Mean |d| across 4 generators: entropy_mean tau=0.5: 1.39, 0.7: 1.10, 0.9: 0.58; TTR 1.00/0.85/0.45; hapax 0.87/0.75/0.42; ent_std 0.84/0.52/0.20; ent_max 0.06/0.09/0.11; tail_decay 0.07/0.12/0.15; ent_min 0.04/0.06/0.04; Mean drifting |d|: 1.09 (0.5), 0.90 (0.7), 0.48 (0.9)
- **Keywords**: DDR partition stability, temperature, tau=0.5/0.7/0.9, Cohen's d, gen-1 vs gen-2+, drifting/intermediate/stationary labels, effect-size compression, boundary features, 4 generators, 12 conditions
- **Tables/Figures**: `\label{tab:ddr-temp-stability}`

## 25. `appendix_seed_control.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-2.8B->OLMo binary F1=0.695 [0.673,0.717]; OLMo->Pythia-2.8B F1=0.666 [0.643,0.689]; Independent-seed avg 0.680; Shared-seed LOGO ref 0.694; Gap -1.4 pp; Semantic similarity: 0->1: 0.622, 1->2: 0.683, 2->3: 0.801, 3->4: 0.859; Prompt type similarity: continuation 0.717, elaboration 0.809, rewriting 0.808
- **Keywords**: independent-seed control, disjoint Wikipedia seed pools, 500 seeds each, topic leakage, Pythia-2.8B, OLMo-2-1B, embedding cosine similarity, semantic similarity, depth-topic independence
- **Tables/Figures**: `\label{tab:seed-control}`

## 26. `appendix_instruct.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Base vs instruct 3-class F1: OLMo 0.754->0.575, Qwen3-1.7B 0.769->0.732, Llama-3.2-3B 0.742->0.544; Binary: OLMo 0.845->0.813, Qwen3-1.7B 0.861->0.875, Llama 0.849->0.838
  - rho(ent mean): base -0.64/-0.60/-0.63 -> instruct +0.48/+0.48/+0.23; Feature reversals: OLMo 6/7, Qwen 6/7, Llama 3/7
  - Retraining: OLMo base->inst 0.321 -> retrained 0.590 (+0.269); Qwen3-1.7B 0.500->0.660 (+0.160); Qwen3-0.6B 0.532->0.600 (+0.068)
  - 3-gen instruct LOGO binary F1=0.487
  - DDR clustering: instruct silhouette=0.338 vs base 0.632; OLMo-Instruct TTR |rho|=0.006, hapax |rho|=0.025; Cross-condition: base->instruct binary=0.490, instruct->base=0.454
  - QLoRA on instruct: OLMo-Inst XGB 0.575 -> QLoRA 0.888+/-0.007 (+31.3 pp); Qwen3-1.7B-Inst XGB 0.732 -> QLoRA 0.907+/-0.008 (+17.5 pp); Base QLoRA: OLMo 0.859+/-0.004, Qwen 0.904+/-0.009
- **Keywords**: instruction-tuned, RLHF, base vs instruct, rho reversal, feature reversal, retraining, cross-condition transfer, DDR compression, silhouette, QLoRA end-to-end, within-model 5-fold CV, Qwen3-0.6B backbone, OLMo-2-1B-Instruct, Qwen3-1.7B-Instruct, Llama-3.2-3B-Instruct
- **Tables/Figures**: `\label{tab:instruct}`, `\label{tab:instruct-retrain}`, `\label{tab:instruct-qlora}`

## 27. `discussion.tex`
- **Exp IDs**: None
- **Key metrics**: rho collapse at t=1.0: -0.60 to -0.002; elaboration F1=0.730 vs continuation 0.781; LOPTO F1=0.753; gen-1 per-class F1=0.63; 86% false negatives; t=0.7->1.0: 3-class drops 0.789->0.723, Qwen3-1.7B to 0.418; Cross-ref spread <=0.013; 5-class ~0.50; QLoRA 0.905; OLMo-Instruct LOGO F1=0.338 vs 0.763 base; QLoRA instruct 0.89-0.91 vs XGB 0.58-0.73; Cross-gen instruct LOGO=0.487
- **Keywords**: discussion, DDR mechanism, location vs shape, top-p truncation, mean surprisal, temperature sensitivity, boundary conditions, false negatives, cross-temperature, model collapse, inference chains, fixed parameters, reversible drift, 3-class ceiling, instruction tuning attenuation
- **Tables/Figures**: None

## 28. `appendix_ablation.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature F1=0.773; Surface only=0.688 (+8.5 pp gap); Reference only=0.713 (+6.0 pp gap); Top feature importance: hapax_ratio 0.35, entropy_mean 0.27
- **Keywords**: feature ablation, complementarity, 8-gen 10-fold stratified CV, 3-class, surface features, reference features
- **Tables/Figures**: `\label{tab:ablation}`

## 29. `appendix_feature_correlation.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529; TTR-hapax r=0.97; entropy_mean-TTR r=0.86; entropy_mean-hapax r=0.81; PCA: drifting PC1 explains 92.3% variance, loadings 0.56-0.59; Full 7-feature: PC1 44.4% variance, PC2 18.3%
- **Keywords**: feature correlation, Pearson correlation matrix, PCA, principal component analysis, drifting triplet, near-uniform loadings, entropy distributional shape
- **Tables/Figures**: `\label{tab:feature-corr}`

## 30. `appendix_convergence.tex`
- **Exp IDs**: None
- **Key metrics**: Drifting features: |d|>2 by depth 2 (TTR, hapax); Near-stationary: |d|<0.25 across all depths
- **Keywords**: convergence dynamics, per-feature, Cohen's d relative to depth 0, fast-convergence group, location stability, 8 generators
- **Tables/Figures**: `\label{fig:convergence-dynamics}` (fig_convergence_dynamics.pdf)

## 31. `related_work.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1 0.52-0.71 (detection scores as depth predictors)
- **Keywords**: AI-generated text detection, GLTR, DetectGPT, FastDetectGPT, Binoculars, LD-Score, Ghostbuster, beyond binary, attribution, model collapse, self-consuming, broken telephone, Markovian chains, iterative generation, vocabulary diversity, stylometry, TTR, hapax, data provenance, watermarking, ordinal classification, CORAL, Frank-Hall
- **Tables/Figures**: None

## 32. `abstract.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 [0.688, 0.700] under LOGO; 0.830 on cross-model chains (5-gen, LOGO) [0.818, 0.841]; TOST +/-2% p<0.001; 5 families, 0.6B-8B
- **Keywords**: differential depth response (DDR), mean entropy, lexical diversity, entropy max, tail decay, order-of-magnitude, 7-feature ensemble, leave-one-generator-out, cross-model chains, TOST equivalence, instruction tuning degradation, base models
- **Tables/Figures**: None

## 33. `introduction.tex`
- **Exp IDs**: None
- **Key metrics**: 37K texts, 8 generators, 5 families, 0.6B-8B; d=0.76-1.17 drifting, d<0.10 stationary; Binary F1=0.830 cross-model, 0.694 LOGO; Outperforms by 6.7-36.3 pp; Matches 4-detector within 0.3 pp at 2.4x lower cost; t degradation -9.3 to -26.0 pp at t=0.9; TOST +/-2% p<0.001; 7-17% estimated LLM content in publications
- **Keywords**: generation depth classification, depth fingerprinting, recursive generation, distributional drift, model collapse, data provenance, binary detection, ordinal classification, gen-0/gen-1/gen-2+, DDR, continuation chains, base models, instruction tuning confounds
- **Tables/Figures**: None

## 34. `conclusion.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 LOGO, 0.830 cross-model (5-gen); TOST +/-2% p<0.001 n=3 seeds; 5 model families
- **Keywords**: conclusion, location-shape decomposition, DDR, instruction tuning boundary, frontier scale 70B+
- **Tables/Figures**: None

## 35. `main.tex`
- **Exp IDs**: None
- **Key metrics**: None (document structure only); footnote: 34,131 samples for baseline comparison
- **Keywords**: EMNLP 2026 ARR, ACL 2023 template, 6-gen vs 8-gen subsets, Llama-3.2-3B, Mistral-7B-v0.3 added last
- **Tables/Figures**: `\label{fig:baseline-ci}` (fig3_baseline_comparison.pdf), plus all \input'd appendices

## 36. `limitations.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-Instruct LOGO F1=0.338 vs 0.763 base; Qwen3-0.6B chat template 0.667 vs 0.816; Qwen3-8B 3-class F1=0.714; Cross-scale gap vs <=2.8B (0.77-0.81); Prompt-type 3-class: continuation 0.78, elaboration 0.73, rewriting 0.74; LOPTO 0.753; Cross-model 3-class=0.789, binary=0.830 (5-gen); Academic t=0.7 binary=0.628; 5-class LOGO~0.50; Cross-ref spread 0.013; Length-matched |rho|<0.02 for Qwen instruct; t degradation -6 pp at t=1.0
- **Keywords**: limitations, base models only, instruction tuning, 8.2B max, frontier 70B+ untested, prompt-type dependent, continuation vs elaboration, cross-model chains, cross-domain, temperature, 3-class ceiling, reference model dependency, Pythia-410M, English-only, length confound for instruct
- **Tables/Figures**: None

## 37. `results.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - LOGO 3-class F1=0.762 [0.758,0.766], N=37,058; Binary=0.694 [0.688,0.700]; Per-gen binary: Pythia-2.8B 0.724, Pythia-1B 0.718, Qwen3-1.7B 0.709, Llama-3.2-3B 0.697, OLMo-2-1B 0.695, Qwen3-8B 0.692, Qwen3-0.6B 0.691, Mistral-7B 0.633; LOFO binary=0.686
  - Cross-model binary=0.830 [0.818,0.841], 5-gen LOGO
  - Single-gen transfer mean binary=0.810 [0.796,0.822]
  - QLoRA 3-class=0.905, +11.6 pp (6-gen); QLoRA instruct 0.89-0.91
  - Length-matched binary=0.724 vs 0.770 unmatched
  - Seed-level demeaning F1=0.701; Independent-seed F1=0.680
  - DDR: k=2 silhouette=0.632; drifting |rho|>0.60, d=0.76-1.17; near-stationary d<0.10, CV<3%; intermediate (ent_std) |rho|=0.16, d=0.55
  - Spearman: hapax -0.64, TTR -0.63, ent_mean -0.60, tail_decay |rho|=0.04
  - KS: drifting 0.516-0.537 vs shape 0.043-0.052; Cohen's d: ent_mean 1.17, TTR 0.88, hapax 0.76, ent_max 0.08, tail_decay 0.08; Glass's Delta: ent_mean 1.41, hapax 0.94, <=0.10 for stationary; gap >=9.5x
  - ent_min pooled |rho|=0.40 but gen-1 vs gen-2+ d=0.03; Cliff's delta=0.354
  - Full F1=0.773 vs surface 0.688 vs reference 0.713, McNemar p~0; Permutation: hapax 0.35, ent_mean 0.23, TTR 0.18
  - PCA: drifting PC1 92.3%; replacing drifting with PC1 costs 1.1 pp; single drifting + 4 non-drifting = 0.692 vs 0.701 full; TTR-hapax r=0.97
  - Cross-ref spread <=0.013
  - Baselines: 4-det+surface 3-class=0.795, binary=0.708, 22.8ms; 4-det 0.785/0.700; 7-feat 0.774/0.705/9.7ms; Avg-LogProb 0.707/0.673; FastDetectGPT 0.660/0.569; LD-Score 0.630/0.675; Binoculars 0.411/0.539; Delta=6.7-36.3 pp over individual
- **Keywords**: depth classification, LOGO, LOFO, cross-model, cross-generator transfer, QLoRA, length confound, seed-sharing control, seed-level demeaning, differential depth response (DDR), Spearman rho, KS test, Cohen's d, Glass's Delta, Cliff's delta, Levene test, Bonferroni, feature complementarity, PCA, permutation importance, cross-family reference, temperature, prompt-type, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, 4-detector ensemble, inference cost, ms/text
- **Tables/Figures**: `\label{tab:logo-results}` (inline), `\label{fig:feature-drift}` (fig1_differential_response.pdf), `\label{tab:baselines}`

## 38. `appendix_cross_model_detail.tex`
- **Exp IDs**: None
- **Key metrics**: N=2,964; 5 generators; Per-class: gen-0 prec=0.921 rec=0.948 F1=0.935 [0.923,0.946]; gen-1 prec=0.737 rec=0.803 F1=0.768 [0.748,0.788]; gen-2+ prec=0.842 rec=0.742 F1=0.789 [0.768,0.809]; Macro F1=0.831 [0.817,0.844]; Natural class macro=0.789; Binary F1=0.830 [0.818,0.841], bootstrap n=2000
- **Keywords**: cross-model chains, per-class detail, generator-level leave-one-out, class balancing, natural class distribution, 5-gen (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)
- **Tables/Figures**: `\label{tab:cross-model-perclass}`

## 39. `method.tex`
- **Exp IDs**: None
- **Key metrics**: 8 generators x ~1000 seeds x 5 depths = 39,815 theoretical; 37,058 after filtering (2,746 chain breaks + 11 short); XGBoost: n_estimators=200, max_depth=6, lr=0.1; Seed std < 0.001 over 5 seeds; LOGO F1: binary=0.686 LOFO; Cross-ref spread <=0.013; 3 subsets: 5-gen, 6-gen, 8-gen; t=0.7, p=0.9, 256 max tokens
- **Keywords**: task formulation, ordinal classification, gen-0/gen-1/gen-2+, generation chain construction, 8 generators, 5 families, Pythia 2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B, Llama-3.2-3B, Mistral-7B-v0.3, Wikipedia seeds, continuation prompt, temperature 0.7, nucleus p=0.9, 256 tokens, feature extraction, Pythia-410M reference, NLL, entropy_mean/std/max/min, tail_decay, TTR, hapax_ratio, LOGO, LOFO, XGBoost, McNemar, bootstrap, Bonferroni, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, length confound control
- **Tables/Figures**: None

---

**Summary of exp_id strings**: No explicit exp_id strings (like "eval-xxx" or "plan-xxx") were found in any .tex file. The paper uses experiment names/labels descriptively (e.g., "8-gen LOGO", "6-gen LOGO", "5-gen cross-model", "QLoRA", etc.) rather than coded IDs.

**Key metric numbers consolidated** (primary results):
- 8-gen LOGO 3-class F1 = 0.762, binary F1 = 0.694
- 5-gen cross-model binary F1 = 0.830
- QLoRA 3-class F1 = 0.905
- 5-class F1 = 0.501
- LOFO (family-level) binary = 0.686
- Independent-seed = 0.680
- Length-matched binary = 0.724
- Downstream PPL: 2.335 (all), 2.367 (random), 2.387 (depth 0-1); TOST p = 1.1e-4
- Instruct degradation: OLMo 0.754->0.575 (3-class); QLoRA recovers to 0.888-0.907
- Transfer matrix mean off-diagonal = 0.810
- Temperature: reliable at t in [0.5, 0.7], degrades -9.3 to -26.0 pp at t=0.9

**All tables defined** (by label): tab:logo-results, tab:feature-ablation, tab:cross-ref, tab:qlora, tab:lofo, tab:qualitative-text, tab:qualitative-features, tab:human-edit, tab:feature-degrade, tab:baseline-robustness, tab:error-by-gen, tab:domain, tab:downstream, tab:tost-margins, tab:gen-subsets, tab:tost-per-gen, tab:confusion, tab:alt-classifier, tab:sampling-ablation, tab:clustering, tab:tost-sensitivity, tab:holdout-split, tab:effect-sizes, tab:dataset-stats, tab:5class-logo, tab:5class-perclass, tab:transfer, tab:ddr-temp-stability, tab:seed-control, tab:instruct, tab:instruct-retrain, tab:instruct-qlora, tab:ablation, tab:feature-corr, tab:baselines, tab:cross-model-perclass

**All figures defined** (by label): fig:feature-drift (fig1_differential_response.pdf), fig:baseline-ci (fig3_baseline_comparison.pdf), fig:ddr-scatter (fig_ddr_scatter.pdf), fig:confusion-heatmap (fig_appendix_confusion.pdf), fig:per-gen (fig_appendix_per_gen.pdf), fig:ddr-trends (fig_appendix_ddr_trends.pdf), fig:umap (fig_appendix_umap.pdf), fig:cross-temp (fig_appendix_cross_temp.pdf), fig:holdout-scatter (fig_ddr_holdout_split.pdf), fig:violin (fig_appendix_violin.pdf), fig:convergence-dynamics (fig_convergence_dynamics.pdf), fig:transfer (fig_transfer_heatmap.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aab0e37d-aa79-40c3-9dbb-e8613553ab54",
  "isSidechain": true,
  "agentId": "a476781bbc33ad56b",
  "requestId": "req_011CbDEXZAA3Wb3P7q8dHTq2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7272e18-a3ed-4ba4-ad08-d5ad3da487ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdiEDpsELHAopobVKVYp7E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15452,
      "cache_read_input_tokens": 54352,
      "output_tokens": 11769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11769,
          "cache_read_input_tokens": 54352,
          "cache_creation_input_tokens": 15452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15452,
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
