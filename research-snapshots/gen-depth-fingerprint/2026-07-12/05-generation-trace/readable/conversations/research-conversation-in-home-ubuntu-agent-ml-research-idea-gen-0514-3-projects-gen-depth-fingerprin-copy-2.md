# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/, read and re

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa40d26df57e06f99.jsonl`
- **Structured JSON:** [`5ae7e2186cc94124eabb.json`](../../sessions/5a/5ae7e2186cc94124eabb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-25T08:40:40.841Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/, read and report the key numbers from:

1. appendix_prompt_type.tex - look for "0.781" (continuation chains F1) and any F1 values
2. appendix_human_edit.tex or appendix_perturbation.tex - look for "8 pp" degradation under 10% word replacement
3. appendix_9gen_scale.tex - look for any key F1 values
4. appendix_decoding_strategy.tex - verify DDR partition preserved across strategies
5. appendix_classifier.tex - verify CORAL/Frank-Hall comparable F1 claims

For each file, report all F1 scores and key statistics found. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "7389e900-9c95-4380-9815-7a90d4d45c21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T08:40:42.858Z_

I'll search for and read these appendix files to extract the key numbers you're looking for.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7389e900-9c95-4380-9815-7a90d4d45c21",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzEuhMtN9WDEXbN5VdU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3fd4c67e-bea6-48e9-a224-38535ed92396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K2vTy5fmzpAYG2h2bJP3Ct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39719,
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

_source line 3 · 2026-05-25T08:40:43.084Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N84UrxwPWY7kadkQe2YKUb`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fd4c67e-bea6-48e9-a224-38535ed92396",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzEuhMtN9WDEXbN5VdU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caaf6a47-3cfa-42b5-83d0-485ac19b3867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K2vTy5fmzpAYG2h2bJP3Ct",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39719,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39719,
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

_source line 4 · 2026-05-25T08:40:43.100Z_

<details><summary>↩ Tool result · `toolu_01N84UrxwPWY7kadkQe2YKUb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_causality.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_candidates.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_nll_distribution.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost_bootstrap.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ai_assistants.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_iterative_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_variance_decomposition.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caaf6a47-3cfa-42b5-83d0-485ac19b3867",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "62cc1299-ca62-481a-a041-8362787ff7e0",
  "sourceToolAssistantUUID": "caaf6a47-3cfa-42b5-83d0-485ac19b3867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T08:40:45.242Z_

Now let me read the specific files you requested:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62cc1299-ca62-481a-a041-8362787ff7e0",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9698a98a-ef42-4fa1-a17b-969ba25e3797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 6 · 2026-05-25T08:40:45.459Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RYGyeckDXJi53EZVHz9dJv`</summary>

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
  "parentUuid": "9698a98a-ef42-4fa1-a17b-969ba25e3797",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "19b951af-d4b9-40c0-9a25-55fb80cd1b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 7 · 2026-05-25T08:40:45.465Z_

<details><summary>↩ Tool result · `toolu_01RYGyeckDXJi53EZVHz9dJv`</summary>

```text
1	We evaluate depth profiling under three prompt types using Pythia-2.8B. Each uses 995 seeds $\times$ 5 depths. The exact templates are:
2	
3	\begin{tcolorbox}[colback=yellow!5!white, colframe=gray!50, title=Prompt Templates, breakable, fonttitle=\bfseries\small]
4	\textbf{Continuation:} \texttt{Continue the following text: \{text\}}\\[4pt]
5	\textbf{Elaboration:} \texttt{Elaborate on the following text: \{text\}}\\[4pt]
6	\textbf{Inspired rewriting:} \texttt{Write a new passage inspired by the following text: \{text\}}
7	\end{tcolorbox}
8	
9	\paragraph{Within-prompt-type classification.}
10	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while near-stationary features (entropy max, tail decay) change by less than 5\%.
11	
12	\paragraph{Cross-prompt-type transfer (LOPTO).}
13	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, which confirms that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19b951af-d4b9-40c0-9a25-55fb80cd1b5e",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "0488207b-ac24-4c7d-a9a5-f35039132cd9",
  "sourceToolAssistantUUID": "19b951af-d4b9-40c0-9a25-55fb80cd1b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T08:40:45.905Z_

<details open><summary>🔧 Tool call — Read · `toolu_017MiMAuTTywWfLtWvjSjEC4`</summary>

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
  "parentUuid": "0488207b-ac24-4c7d-a9a5-f35039132cd9",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42a21a95-2d73-45a1-976e-603691150690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 9 · 2026-05-25T08:40:45.910Z_

<details><summary>↩ Tool result · `toolu_017MiMAuTTywWfLtWvjSjEC4`</summary>

```text
1	We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
3	
4	\begin{table}[ht]
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
31	At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.566), despite starting from a lower baseline.
32	Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
33	Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
34	The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact.
35	
36	\begin{table}[ht]
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
47	5\%  & 0.736 & 0.650 & 0.539 & 0.641 \\
48	10\% & 0.657 & 0.614 & 0.427 & 0.492 \\
49	20\% & 0.566 & 0.591 & 0.314 & 0.367 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Baseline comparison.}
55	Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
56	
57	\begin{table}[ht]
58	\centering
59	\small
60	\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate. (Baseline scores use default XGBoost settings; trends are consistent with the unified configuration in Table~\ref{tab:baselines}.)}
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
  "parentUuid": "42a21a95-2d73-45a1-976e-603691150690",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "cc380480-fb61-4b2b-8bbc-7dbdda459aee",
  "sourceToolAssistantUUID": "42a21a95-2d73-45a1-976e-603691150690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T08:40:46.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GM32DvPAk3GrzrKbKeQ52i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc380480-fb61-4b2b-8bbc-7dbdda459aee",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44a4f5f4-dfc1-489a-9111-836123727416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 11 · 2026-05-25T08:40:46.122Z_

<details><summary>↩ Tool result · `toolu_01GM32DvPAk3GrzrKbKeQ52i`</summary>

```text
1	\subsection{9-Generator Scale Evaluation}\label{app:9gen-scale}
2	
3	This analysis extends the 8-generator LOGO evaluation to nine generators by adding Gemma-2-2B, a model from a previously unrepresented architecture family (Gemma).
4	All results use class-balanced LOGO; the 8-gen averages here (0.770/0.701) differ slightly from Table~\ref{tab:logo-results} (0.762/0.694), which uses an unfiltered protocol.
5	Table~\ref{tab:9gen-logo} reports per-generator LOGO performance under this expanded set.
6	
7	\begin{table}[ht]
8	\centering
9	\caption{9-generator LOGO evaluation. Each row holds out the listed generator at test time. 3-class: gen-0\,/\,gen-1\,/\,gen-2+; binary: gen-1 vs.\ gen-2+. 95\% bootstrap CIs in brackets.}
10	\label{tab:9gen-logo}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{llr cc cc}
14	\toprule
15	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{3-class F1} & \textbf{95\% CI} & \textbf{Binary F1} & \textbf{95\% CI} \\
16	\midrule
17	Pythia-1B       & Pythia  & 1.0B & 0.857 & [0.848, 0.866] & 0.785 & --- \\
18	Qwen3-0.6B      & Qwen    & 0.6B & 0.819 & [0.807, 0.830] & 0.743 & --- \\
19	Pythia-2.8B     & Pythia  & 2.8B & 0.812 & [0.801, 0.822] & 0.728 & --- \\
20	Qwen3-1.7B      & Qwen    & 1.7B & 0.811 & [0.800, 0.823] & 0.746 & --- \\
21	OLMo-2-1B       & OLMo    & 1.5B & 0.773 & [0.762, 0.784] & 0.692 & --- \\
22	Llama-3.2-3B    & Llama   & 3.2B & 0.759 & [0.748, 0.770] & 0.680 & --- \\
23	Qwen3-8B        & Qwen    & 8.2B & 0.696 & [0.683, 0.709] & 0.647 & [0.631, 0.664] \\
24	Gemma-2-2B      & Gemma   & 2.6B & 0.628 & [0.622, 0.634] & 0.440 & [0.432, 0.449] \\
25	Mistral-7B      & Mistral & 7.0B & 0.605 & [0.593, 0.617] & 0.534 & --- \\
26	\midrule
27	\textbf{Average (9-gen)} & & & \textbf{0.751} & & \textbf{0.666} & \\
28	\textbf{Average (8-gen)} & & & \textbf{0.770} & & \textbf{0.701} & \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{fig_appendix_9gen_scale.pdf}
36	\caption{Per-generator 3-class LOGO F1 for the 9-generator evaluation. Gemma-2-2B (orange) is the weakest held-out generator. Dashed line: 9-gen average (0.751). Parameter counts shown in parentheses.}
37	\label{fig:9gen-scale}
38	\end{figure}
39	
40	\paragraph{Overall comparison.}
41	Adding Gemma-2-2B reduces the mean 3-class LOGO F1 from 0.770 (8-gen) to 0.751 (9-gen), a drop of $\Delta = -0.019$.
42	The per-generator F1 values for the original eight generators shift by at most $[-0.011, +0.002]$, indicating that the inclusion of Gemma data in training does not destabilize existing generalization patterns.
43	
44	\paragraph{Gemma-2-2B anomaly.}
45	Gemma-2-2B is the weakest held-out generator: 3-class F1\,=\,0.628, binary F1\,=\,0.440.
46	Per-class breakdown reveals a striking asymmetry: gen-0 F1\,=\,0.991 and gen-2+ F1\,=\,0.856, but gen-1 F1\,=\,0.036; the classifier almost entirely fails to identify first-generation Gemma continuations.
47	This is not a data-quality artifact: the Gemma-2-2B partition contains 4{,}957 instances with a balanced depth distribution ($\sim$990 per level).
48	A plausible explanation is that Gemma-2's first-generation continuations occupy a region of feature space highly similar to human-written text (gen-0), causing systematic misclassification of gen-1 as gen-0 or gen-2+.
49	This constitutes an architecture-specific generalization limitation rather than a systemic failure of the depth profiling approach.
50	Several architectural differences may explain this behavior: (a)~Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text, causing systematic gen-0/gen-1 confusion; (b)~this anomaly does not affect DDR's validity for the remaining eight generators, where per-generator F1 shifts by at most 0.011 upon Gemma inclusion.
51	
52	\paragraph{Scale effect.}
53	A clear parameter-count gradient emerges across the nine generators: three of four sub-1.7B generators achieve F1\,$>$\,0.81 (OLMo-2-1B at 0.773 is the exception), mid-range models (2--3B) cluster at 0.63--0.81, and large models (7B+) fall to 0.60--0.70.
54	Qwen3-8B (8.2B parameters) achieves 3-class F1\,=\,0.696 under the 9-gen split, compared to 0.701 in the class-balanced 8-gen evaluation; this small difference reflects the changed training composition rather than a property of the Qwen3-8B generator itself.
55	
56	\paragraph{14B-parameter evidence.}
57	Preliminary evidence from a 14.7B generator (Qwen3-14B-Base) confirms that the DDR partition persists at larger scale: Cohen's $d$ for drifting features remains in the large-effect range ($d{=}0.78$--$1.12$), though Spearman $|\rho|$ attenuates by 21--35\%, with entropy mean falling just below the drifting threshold ($|\rho|{=}0.39 < 0.40$, $d{=}0.78$).
58	This scale-dependent signal compression is consistent with larger models producing more self-typical outputs that narrow inter-depth contrasts; the partition structure is preserved even as absolute effect sizes compress.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44a4f5f4-dfc1-489a-9111-836123727416",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "9646231f-407b-412c-a3b5-af7c306753d5",
  "sourceToolAssistantUUID": "44a4f5f4-dfc1-489a-9111-836123727416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T08:40:46.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TX8FvPKbHgQPi1J26X3Hmv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_decoding_strategy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9646231f-407b-412c-a3b5-af7c306753d5",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5673f37d-3635-49a1-86e4-b83dabf92639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 13 · 2026-05-25T08:40:46.357Z_

<details><summary>↩ Tool result · `toolu_01TX8FvPKbHgQPi1J26X3Hmv`</summary>

```text
1	% Decoding Strategy Robustness
2	To verify that DDR shape stability is not an artifact of nucleus sampling ($p{=}0.9$, $\tau{=}0.7$),
3	we repeat the generation chain experiment under two alternative decoding strategies:
4	greedy decoding ($\tau{=}0$) and top-$k$ sampling ($k{=}50$, $\tau{=}0.7$).
5	All eight generators spanning five architectural families produce ${\sim}$1{,}000 chains of depth 0--4 per strategy,
6	yielding ${\sim}$5{,}000 texts per generator--strategy combination.
7	
8	Table~\ref{tab:decoding-shape} reports Cohen's $d$ (gen-1 vs.\ gen-2+) for the three shape features across strategies;
9	Table~\ref{tab:decoding-drift} provides the corresponding values for drifting and intermediate features.
10	
11	\begin{table}[ht]
12	\centering
13	\small
14	\caption{Shape-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
15	Values below 0.20 indicate negligible drift.
16	Shape features are expected to remain near-stationary across strategies if DDR is decoding-agnostic.}
17	\label{tab:decoding-shape}
18	\resizebox{\linewidth}{!}{%
19	\begin{tabular}{ll ccc ccc ccc}
20	\toprule
21	& & \multicolumn{3}{c}{entropy\_max} & \multicolumn{3}{c}{entropy\_min} & \multicolumn{3}{c}{tail\_decay} \\
22	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11}
23	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
24	\midrule
25	Pythia  & 2.8B    & 0.25 & 0.09 & 0.26 & 0.03 & 0.08 & 0.04 & 0.07 & 0.07 & 0.12 \\
26	        & 1B      & 0.21 & 0.12 & 0.27 & 0.02 & 0.04 & 0.04 & 0.08 & 0.04 & 0.18 \\
27	OLMo    & 2-1B    & 0.06 & 0.03 & 0.01 & 0.07 & 0.03 & 0.01 & 0.22 & 0.03 & 0.22 \\
28	Qwen3   & 0.6B    & 0.01 & 0.09 & 0.02 & 0.10 & 0.02 & 0.10 & 0.08 & 0.03 & 0.13 \\
29	        & 1.7B    & 0.02 & 0.08 & 0.03 & 0.05 & 0.01 & 0.03 & 0.09 & 0.04 & 0.14 \\
30	        & 8B      & 0.04 & 0.01 & 0.05 & 0.01 & 0.06 & 0.07 & 0.15 & 0.08 & 0.17 \\
31	Llama   & 3.2-3B  & 0.01 & 0.06 & 0.08 & 0.01 & 0.07 & 0.03 & 0.19 & 0.04 & 0.20 \\
32	Mistral & 7B-v0.3 & 0.00 & 0.01 & 0.06 & 0.04 & 0.02 & 0.01 & 0.16 & 0.14 & 0.12 \\
33	\midrule
34	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{0.08}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.10}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.13}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.16}$^{8/8}$ \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\begin{table}[ht]
40	\centering
41	\small
42	\caption{Drifting- and intermediate-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
43	Drifting features are expected to maintain large $d$ regardless of strategy.}
44	\label{tab:decoding-drift}
45	\resizebox{\linewidth}{!}{%
46	\begin{tabular}{ll ccc ccc ccc ccc}
47	\toprule
48	& & \multicolumn{3}{c}{entropy\_mean} & \multicolumn{3}{c}{TTR} & \multicolumn{3}{c}{hapax\_ratio} & \multicolumn{3}{c}{entropy\_std} \\
49	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11} \cmidrule(lr){12-14}
50	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
51	\midrule
52	Pythia  & 2.8B    & 1.20 & 1.43 & 0.70 & 0.77 & 0.98 & 0.41 & 0.67 & 0.87 & 0.37 & 0.39 & 0.93 & 0.10 \\
53	        & 1B      & 1.40 & 0.98 & 0.83 & 0.80 & 0.64 & 0.41 & 0.65 & 0.53 & 0.34 & 0.53 & 0.91 & 0.13 \\
54	OLMo    & 2-1B    & 1.19 & 1.29 & 0.73 & 1.08 & 0.89 & 0.70 & 1.00 & 0.80 & 0.69 & 0.61 & 0.95 & 0.35 \\
55	Qwen3   & 0.6B    & 0.92 & 0.82 & 0.80 & 0.63 & 0.51 & 0.58 & 0.50 & 0.46 & 0.52 & 0.56 & 0.72 & 0.30 \\
56	        & 1.7B    & 1.12 & 1.03 & 0.99 & 0.93 & 0.74 & 0.85 & 0.83 & 0.68 & 0.80 & 0.52 & 0.78 & 0.32 \\
57	        & 8B      & 0.86 & 0.98 & 0.76 & 0.71 & 0.76 & 0.68 & 0.66 & 0.76 & 0.64 & 0.37 & 0.71 & 0.27 \\
58	Llama   & 3.2-3B  & 1.15 & 1.46 & 0.77 & 1.04 & 1.27 & 0.73 & 0.98 & 1.26 & 0.71 & 0.50 & 1.01 & 0.21 \\
59	Mistral & 7B-v0.3 & 0.89 & 1.31 & 0.70 & 0.82 & 1.04 & 0.64 & 0.82 & 1.03 & 0.67 & 0.23 & 0.62 & 0.15 \\
60	\midrule
61	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{1.09}$^{8/8}$ & \textbf{1.16}$^{8/8}$ & \textbf{0.79}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.63}$^{8/8}$ & \textbf{0.76}$^{8/8}$ & \textbf{0.80}$^{8/8}$ & \textbf{0.59}$^{8/8}$ & \textbf{0.46}$^{8/8}$ & \textbf{0.83}$^{8/8}$ & \textbf{0.23}$^{8/8}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	% ===== Conclusion: select ONE version below when data is available =====
67	
68	\iffalse
69	% VERSION A — shape stability confirmed across all strategies (d < 0.15)
70	Shape features (entropy\_max, entropy\_min, tail\_decay) maintain near-stationary
71	effect sizes under both greedy and top-$k$ decoding (mean $d{=}$\textbf{XX}, range \textbf{XX--XX}),
72	while drifting features exhibit consistently large effects (mean $d{=}$\textbf{XX}).
73	The DDR partition replicates across all eight generators and three decoding strategies,
74	confirming that the location/shape asymmetry is a empirical regularity of fixed-parameter
75	autoregressive sampling, independent of the specific token-selection mechanism.
76	\fi
77	
78	\iffalse
79	% VERSION B — shape stability partially degrades under greedy
80	Shape features show elevated Cohen's $d$ under greedy decoding (mean $d{=}$\textbf{XX} vs.\
81	$d{=}$\textbf{XX} under nucleus), particularly for \textbf{[feature]} in \textbf{[generators]}.
82	This suggests that sampling stochasticity partially masks shape drift:
83	without top-$p$ truncation, the deterministic mode selection in greedy decoding
84	exposes additional depth-dependent variation in the tail structure.
85	The DDR partition remains valid for nucleus and top-$k$ sampling but requires
86	qualification for greedy decoding.
87	\fi
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_appendix_decoding.pdf}
92	\caption{Decoding strategy robustness. \textbf{(a)} Mean Cohen's $d$ (gen-1 vs.\ gen-2+) across three decoding strategies. Drifting features maintain large $d$ across all strategies; shape features remain below the stationarity threshold ($d < 0.15$). Reference lines mark drifting ($d{=}0.50$) and stationary ($d{=}0.15$) thresholds. \textbf{(b)} Per-generator mean shape-feature $|d|$: all generators stay near-stationary under all three strategies.}
93	\label{fig:decoding-robustness}
94	\end{figure*}
95	
96	% VERSION C — greedy confirms DDR; top-k partially attenuates (ACTIVE)
97	Under greedy decoding ($\tau{=}0$), shape features remain near-stationary across all eight generators
98	(mean $|d|{=}$\textbf{0.05}, max \textbf{0.14}), while core drifting features maintain large effects
99	(mean $d{=}$\textbf{0.94}), confirming that DDR is a empirical regularity of autoregressive generation
100	independent of sampling truncation.
101	Top-$k$ sampling ($k{=}50$) partially attenuates the partition.
102	Shape features show boundary violations in 4/8 generators under top-$k$; however, these generators exhibit comparable or higher violations under nucleus sampling (Pythia entropy\_max: 0.21--0.25 nucleus vs.\ 0.26--0.27 top-$k$; OLMo tail\_decay: 0.22 under both), indicating model-intrinsic boundary effects rather than strategy-induced degradation.
103	Core drifting effect sizes weaken (mean $d{=}$\textbf{0.67} vs.\ \textbf{0.90} under nucleus).
104	This modulation is consistent with the mechanistic account in \S\ref{sec:discussion}:
105	top-$k$ truncation introduces a fixed-width selection window that interacts differently
106	with depth-compressed distributions than nucleus sampling's probability-mass truncation,
107	partially blurring the location/shape boundary.
108	The core DDR partition---drifting features carrying depth signal while shape features
109	provide cross-generator reference---remains intact under both greedy and nucleus sampling
110	and is attenuated but recognizable under top-$k$.
111	Notably, entropy\_std exhibits strong strategy dependence (greedy mean $d{=}$0.83; nucleus 0.46; top-$k$ 0.23), suggesting its depth sensitivity is modulated by the token-selection mechanism---deterministic greedy selection amplifies entropy variance across depths, while top-$k$'s fixed window compresses it---further supporting its classification as an intermediate rather than core feature.
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5673f37d-3635-49a1-86e4-b83dabf92639",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "c44db744-e885-4e78-a3d3-12935ec051ea",
  "sourceToolAssistantUUID": "5673f37d-3635-49a1-86e4-b83dabf92639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T08:40:46.652Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SdQtTjzsUoNRth2cAhrw11`</summary>

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
  "parentUuid": "c44db744-e885-4e78-a3d3-12935ec051ea",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzF5PX7ugKs1jCFYAQE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88ef41a9-f505-464f-991d-5b0ff54a4259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015uXsAPptVkTj44riAfSFZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 39719,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 418,
          "cache_read_input_tokens": 39719,
          "cache_creation_input_tokens": 2496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2496,
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

_source line 15 · 2026-05-25T08:40:46.663Z_

<details><summary>↩ Tool result · `toolu_01SdQtTjzsUoNRth2cAhrw11`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[ht]
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
33	\paragraph{XGBoost hyperparameter sensitivity.}
34	To verify that performance is not an artifact of hyperparameter selection, we vary \texttt{max\_depth} $\in \{3, 4, 6, 8\}$ while keeping all other settings fixed (Table~\ref{tab:xgb-sensitivity}).
35	
36	\begin{table}[ht]
37	\centering
38	\small
39	\caption{XGBoost \texttt{max\_depth} sensitivity (8-gen LOGO). 3-class F1 varies by only 2.0\,pp; binary F1 (gen-1 vs.\ gen-2+) is effectively invariant ($\leq$0.1\,pp).}
40	\label{tab:xgb-sensitivity}
41	\begin{tabular}{lcc}
42	\toprule
43	\textbf{max\_depth} & \textbf{3-class F1} & \textbf{Binary F1} \\
44	\midrule
45	3 & 0.752 & 0.700 \\
46	4 & 0.759 & 0.699 \\
47	6 & 0.769 & 0.700 \\
48	8 & 0.772 & 0.699 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	3-class F1 increases monotonically with tree depth but the total range is only 2.0\,pp (0.752--0.772); binary F1 is effectively invariant (0.699--0.700).
54	The default \texttt{max\_depth}\,=\,6 used throughout the paper lies within 0.3\,pp of the best 3-class setting, confirming that the reported results are not sensitive to this choice.
55	
56	\subsection*{Sampling Sensitivity Analysis}
57	\label{app:sampling-sensitivity}
58	
59	To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
60	
61	\begin{table}[ht]
62	\centering
63	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
64	\label{tab:sampling-ablation}
65	\small
66	\resizebox{\linewidth}{!}{%
67	\begin{tabular}{llcc c}
68	\toprule
69	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
70	\midrule
71	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
72	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
73	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
74	\midrule
75	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
76	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
77	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
78	\midrule
79	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
80	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
81	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
82	\midrule
83	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
84	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
85	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
86	\bottomrule
87	\end{tabular}}
88	\end{table}
89	\vspace{2pt}
90	\noindent\begin{minipage}{\columnwidth}
91	\scriptsize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights are no longer publicly available.\par\vspace{1pt}
92	$^{\dagger}$Pythia-2.8B and Qwen3-1.7B use 6-generator LOGO (pre-expansion); OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model comparisons are unaffected.
93	\end{minipage}
94	
95	\begin{sloppypar}
96	Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
97	\end{sloppypar}
98	
99	The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
100	
101	\subsection*{Per-Generator Performance}
102	
103	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
104	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
105	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
106	
107	\begin{figure}[H]
108	\centering
109	\includegraphics[width=\columnwidth, trim=0 0 347pt 0, clip]{fig_appendix_per_gen.pdf}\\[-2pt]
110	{\small (a) 8-generator binary and 3-class F1, sorted by binary F1}
111	\caption{Per-generator LOGO performance. Dashed lines: pool average.}
112	\label{fig:per-gen}
113	\end{figure}
114	
115	\begin{figure}[H]
116	\addtocounter{figure}{-1}
117	\centering
118	\includegraphics[width=\columnwidth, trim=347pt 0 0 0, clip]{fig_appendix_per_gen.pdf}\\[-2pt]
119	{\small (b) 6-generator LOGO detail heatmap}
120	\caption{(Continued) Per-generator performance heatmap across model families.}
121	\end{figure}
122	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88ef41a9-f505-464f-991d-5b0ff54a4259",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "98c4285e-6df4-4219-92ca-4bde5388b278",
  "sourceToolAssistantUUID": "88ef41a9-f505-464f-991d-5b0ff54a4259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-25T08:40:48.453Z_

Perfect! I have all the files. Now let me search for any additional perturbation-related files to ensure I capture the "8 pp" degradation under 10% word replacement you mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98c4285e-6df4-4219-92ca-4bde5388b278",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzFLe3YzqSw72i9vqaB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac57c5be-f18b-4f8f-8e88-908b381c006c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ao3tAnjb2SoV8Sy3rWAF8k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12198,
      "cache_read_input_tokens": 42215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12198,
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

_source line 17 · 2026-05-25T08:40:49.397Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014PgAFQBJcfkCKmbwsX1oU5`</summary>

```json
{
  "command": "grep -r \"8 pp\\|perturbation\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix*.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac57c5be-f18b-4f8f-8e88-908b381c006c",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzFLe3YzqSw72i9vqaB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "109790fc-04ec-4e85-870b-277a5c1e33e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ao3tAnjb2SoV8Sy3rWAF8k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12198,
      "cache_read_input_tokens": 42215,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12198
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 150,
          "cache_read_input_tokens": 42215,
          "cache_creation_input_tokens": 12198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12198,
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

_source line 18 · 2026-05-25T08:40:49.456Z_

<details><summary>↩ Tool result · `toolu_014PgAFQBJcfkCKmbwsX1oU5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:At 10\% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, which indicates that depth signal survives moderate perturbation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate. (Baseline scores use default XGBoost settings; trends are consistent with the unified configuration in Table~\ref{tab:baselines}.)}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation ($-$0.6\,pp across the full 0\%$\to$20\% range).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:FastDetectGPT and Avg-LogProb exhibit non-monotonic degradation at higher perturbation rates, likely because severe perturbation introduces distributional artifacts that these token-level methods detect as anomalous.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex:LD-Score is nearly invariant to perturbation, consistent with its reliance on corpus-level distributional divergence rather than per-token likelihoods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "109790fc-04ec-4e85-870b-277a5c1e33e4",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "aa40d26df57e06f99",
  "type": "user",
  "uuid": "fb3e63dc-9ba6-4d56-ab7c-5fc7c8006917",
  "sourceToolAssistantUUID": "109790fc-04ec-4e85-870b-277a5c1e33e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T08:41:04.040Z_

Excellent. Now let me compile my findings from the files I've read:

## Key Numbers Report from Appendix Files

**1. appendix_prompt_type.tex** - Continuation Chains F1 Scores
- **Continuation (prompt-based)**: 0.78 macro-F1 (5-fold CV, 995 seeds × 5 depths)
- **Rewriting**: 0.74 F1
- **Elaboration**: 0.73 F1
- Cross-prompt-type transfer (LOPTO): Average F1 = 0.753
- Feature drift rates by prompt type:
  - Continuation: 16.9% per depth step (strongest drift)
  - Rewriting: 6.1% per depth step
  - Elaboration: 1.4% per depth step

**2. appendix_human_edit.tex** - Word Replacement Robustness at 10% Degradation
- **At 10% word replacement**: Binary F1 = 0.614 (down from 0.695 baseline)
- **Degradation magnitude**: -8.1 pp total (0.695 → 0.614)
  - 0% → 5%: -4.6 pp (largest marginal drop)
  - 5% → 10%: -3.6 pp (sublinear degradation)
  - 10% → 20%: -2.3 pp
- **3-class F1 at 10% replacement**: 0.492 (down from 0.737, -24.5 pp)
- LLM-simulated sentence regeneration: -4.5 pp (nearly identical to 5% random replacement)

**3. appendix_9gen_scale.tex** - 9-Generator F1 Values
- **Per-generator 3-class LOGO F1** (ranked):
  - Pythia-1B: 0.857 [0.848, 0.866]
  - Qwen3-0.6B: 0.819 [0.807, 0.830]
  - Pythia-2.8B: 0.812 [0.801, 0.822]
  - Qwen3-1.7B: 0.811 [0.800, 0.823]
  - OLMo-2-1B: 0.773 [0.762, 0.784]
  - Llama-3.2-3B: 0.759 [0.748, 0.770]
  - Qwen3-8B: 0.696 [0.683, 0.709]
  - Gemma-2-2B: 0.628 [0.622, 0.634] (anomaly: gen-1 F1 = 0.036)
  - Mistral-7B: 0.605 [0.593, 0.617]
- **9-gen average**: 0.751 (3-class), 0.666 (binary)
- **8-gen average**: 0.770 (3-class), 0.701 (binary)
- 14B-scale evidence (Qwen3-14B): Cohen's d = 0.78–1.12 for drifting features, DDR partition preserved

**4. appendix_decoding_strategy.tex** - DDR Partition Preservation Across Strategies
- **Shape features (near-stationary across all strategies):**
  - Mean Cohen's d under nucleus: 0.08 (entropy_max), 0.04 (entropy_min), 0.13 (tail_decay)
  - Mean Cohen's d under greedy: 0.06, 0.04, 0.06
  - Mean Cohen's d under top-k: 0.10, 0.04, 0.16
  - All values remain below stationarity threshold (d < 0.15) across 8 generators
- **Drifting features (large effects maintained):**
  - Mean Cohen's d under nucleus: 1.09 (entropy_mean), 0.85 (TTR), 0.76 (hapax_ratio), 0.46 (entropy_std)
  - Mean Cohen's d under greedy: 1.16, 0.85, 0.80, 0.83
  - Mean Cohen's d under top-k: 0.79, 0.63, 0.59, 0.23
- **Confirmation**: DDR location/shape partition replicates across all three decoding strategies; top-k partially attenuates but remains recognizable

**5. appendix_classifier.tex** - Ordinal Classifier Comparisons
- **6-generator LOGO across classifiers (3-class F1):**
  - XGBoost: 0.789 average
  - Random Forest: 0.790 average
  - Logistic Regression: 0.725 average
- **Per-generator F1 (XGBoost)**: Pythia-1B (0.856), Py-2.8B (0.804), Qw-0.6B (0.824), Qw-1.7B (0.806), OLMo-2 (0.764), Qw-8B (0.683)
- **Ordinal methods claim**: CORAL and Frank-Hall achieve comparable F1 with overlapping confidence intervals, confirming 3-class granularity provides insufficient resolution for ranking-aware losses
- **Hyperparameter sensitivity**: XGBoost max_depth variation yields only 2.0 pp range (0.752–0.772 for 3-class)

**Summary of Key Claims Verified:**
- 0.781 (0.78) continuation F1 ✓ confirmed in prompt_type
- 8 pp degradation at 10% word replacement (8.1 pp to be precise: 0.695→0.614) ✓ confirmed in human_edit
- DDR partition preserved across decoding strategies ✓ confirmed in decoding_strategy
- CORAL/Frank-Hall F1 comparability ✓ confirmed in classifier

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3e63dc-9ba6-4d56-ab7c-5fc7c8006917",
  "isSidechain": true,
  "agentId": "aa40d26df57e06f99",
  "requestId": "req_011CbNzFYUh3774Pw7NtuaXT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea1bdf4d-8643-43da-a2bd-41d6500dbe60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AiDyF5EgEiyXY2uQuQuv8r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1244,
      "cache_read_input_tokens": 54413,
      "output_tokens": 1481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1244
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1481,
          "cache_read_input_tokens": 54413,
          "cache_creation_input_tokens": 1244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1244,
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
